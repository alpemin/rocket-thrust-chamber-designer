"""Regenerative cooling: 1-D march of the fuel through milled channels in the liner.

The fuel enters the channels at the nozzle exit and flows toward the injector
(counter-flow). At each axial station the code balances three thermal
resistances in series:

    hot gas  --(Bartz h_g)-->  hot wall  --(conduction t/k)-->  cold wall
             --(Dittus-Boelter h_c, with rib fin efficiency)-->  coolant

then adds the absorbed heat to the coolant's enthalpy (real-fluid properties
from CoolProp) and subtracts the friction pressure drop (Haaland friction factor).

Liner stress at each station = thermal stress across the hot wall
+ bending of the hot wall between ribs from the coolant-to-gas pressure difference.
"""
import math
import numpy as np
from .data import MATERIALS, PROPELLANTS
from .performance import mach_from_area_ratio, static_pressure_ratio

try:
    import CoolProp.CoolProp as CP
except ImportError:  # pragma: no cover
    CP = None


class Coolant:
    """Real-fluid coolant properties via CoolProp."""

    def __init__(self, fluid):
        if CP is None:
            raise ImportError("CoolProp is required: pip install CoolProp")
        self.fluid = fluid

    def h_from_T(self, T, p):
        return CP.PropsSI("H", "T", T, "P", p, self.fluid)

    def state(self, h, p):
        f = self.fluid
        T = CP.PropsSI("T", "H", h, "P", p, f)
        return dict(T=T, rho=CP.PropsSI("D", "H", h, "P", p, f), cp=CP.PropsSI("C", "H", h, "P", p, f),
                    mu=CP.PropsSI("V", "H", h, "P", p, f), k=CP.PropsSI("L", "H", h, "P", p, f))


def liner_thickness(r_hot, design, Rt):
    """Hot-wall thickness (m). It scales with radius, like the channels, so the
    wall-span-to-thickness ratio (which sets pressure bending stress) stays
    constant along the nozzle. Capped at 3 mm."""
    return min(design["liner_thickness_mm"] / 1e3 * r_hot / Rt, 0.003)


def channel_geometry(r_hot, design, Rt):
    """Channel width/height/hydraulic diameter at a station with hot-wall radius r_hot (m).

    Channels are wedge-shaped (constant angle), so rib and channel widths grow in
    proportion to radius. This matches the CAD model exactly.
    """
    t = liner_thickness(r_hot, design, Rt)
    h = design["channel_height_mm"] / 1e3
    N = design["channel_count"]
    r_mid = r_hot + t + h / 2
    r_mid_throat = Rt + t + h / 2
    pitch = 2 * math.pi * r_mid / N
    rib = design["rib_width_at_throat_mm"] / 1e3 * r_mid / r_mid_throat
    w = pitch - rib
    A = w * h
    Dh = 4 * A / (2 * (w + h))
    return dict(w=w, h=h, rib=rib, pitch=pitch, A=A, Dh=Dh, t=t, N=N)


def run_cooling(design, perf, contour):
    prop = PROPELLANTS[design["propellant"]]
    liner = MATERIALS[design["liner_material"]]
    g, Tc, R, Pc, cstar = perf["gamma"], perf["Tc"], perf["R"], perf["Pc"], perf["cstar"]
    Rt = perf["Rt"]
    x, r = contour["x"], contour["r"]
    n = len(x)

    # Bartz gas-side constants
    Mgas = perf["M_gas"]
    mu_g = 1.184e-7 * Mgas ** 0.5 * Tc ** 0.6            # Pa-s
    cp_g = g * R / (g - 1)
    Pr = 4 * g / (9 * g - 5)
    rec = Pr ** (1 / 3)
    Dt = 2 * Rt
    r_curv = (1.5 + 0.382) / 2 * Rt
    h0 = 0.026 / Dt ** 0.2 * (mu_g ** 0.2 * cp_g / Pr ** 0.6) * (Pc / cstar) ** 0.8 * (Dt / r_curv) ** 0.1

    cool = Coolant(prop["coolant"])
    mdot_c = perf["mdot_fuel"]
    p_c = design["coolant_inlet_pressure_bar"] * 1e5
    T_in = design.get("coolant_inlet_temp_K", prop["T_cool_in"])
    h_c_enth = cool.h_from_T(T_in, p_c)
    eps_rough = design.get("channel_roughness_um", 10) / 1e6
    kw = liner["k"]

    out = {k: np.zeros(n) for k in ["M", "p_gas", "hg", "Taw", "q", "Twg", "Twc", "T_cool", "p_cool",
                                    "v_cool", "t_liner", "hc", "hc_eff", "fin_eff", "w", "rib", "Re_cool",
                                    "sigma_thermal", "sigma_pressure", "sigma_total", "margin"]}
    Q_total, Twg_guess = 0.0, 700.0
    for i in range(n - 1, -1, -1):          # exit -> injector
        xi, ri = x[i], r[i]
        ar = (ri / Rt) ** 2
        M = 1.0 if i == contour["throat_index"] else mach_from_area_ratio(ar, g, xi > 0)
        wfac = 1 + (g - 1) / 2 * M * M
        Taw = Tc * (1 + rec * (g - 1) / 2 * M * M) / wfac
        p_gas = Pc * static_pressure_ratio(M, g)

        ch = channel_geometry(ri, design, Rt)
        t_l = ch["t"]
        st = cool.state(h_c_enth, p_c)
        v = mdot_c / (ch["N"] * ch["A"] * st["rho"])
        Re_c = st["rho"] * v * ch["Dh"] / st["mu"]
        Pr_c = st["mu"] * st["cp"] / st["k"]
        hc = 0.023 * Re_c ** 0.8 * Pr_c ** 0.4 * st["k"] / ch["Dh"]
        m_fin = math.sqrt(2 * hc / (kw * ch["rib"]))
        fin_eff = math.tanh(m_fin * ch["h"]) / (m_fin * ch["h"])
        hc_eff = hc * (ch["w"] + 2 * fin_eff * ch["h"]) / ch["pitch"]

        Twg = Twg_guess
        for _ in range(40):
            sig = 1 / ((0.5 * Twg / Tc * wfac + 0.5) ** 0.68 * wfac ** 0.12)
            hg = h0 * (1 / ar) ** 0.9 * sig
            q = (Taw - st["T"]) / (1 / hg + t_l / kw + 1 / hc_eff)
            Twg_new = Taw - q / hg
            if abs(Twg_new - Twg) < 0.01:
                Twg = Twg_new
                break
            Twg = 0.5 * Twg + 0.5 * Twg_new
        Twg_guess = Twg
        Twc = Twg - q * t_l / kw

        s_th = liner["E"] * liner["alpha"] * q * t_l / (2 * (1 - liner["nu"]) * kw)
        s_p = 0.5 * max(p_c - p_gas, 0) * (ch["w"] / t_l) ** 2
        s_tot = s_th + s_p
        # Pressure bending is a primary stress: keep it below yield / safety factor.
        # Thermal stress is secondary (self-limiting). The ASME shakedown rule limits
        # primary + secondary to 2 x yield, so the wall settles into elastic cycling.
        margin = min(liner["sy"] / (design["safety_factor"] * s_p) - 1 if s_p > 0 else 9.99,
                     2 * liner["sy"] / s_tot - 1)

        for k_, v_ in dict(t_liner=t_l, M=M, p_gas=p_gas, hg=hg, Taw=Taw, q=q, Twg=Twg, Twc=Twc, T_cool=st["T"],
                           p_cool=p_c, v_cool=v, hc=hc, hc_eff=hc_eff, fin_eff=fin_eff, w=ch["w"],
                           rib=ch["rib"], Re_cool=Re_c, sigma_thermal=s_th, sigma_pressure=s_p,
                           sigma_total=s_tot, margin=margin).items():
            out[k_][i] = v_

        # advance coolant to the next upstream station
        if i > 0:
            ds = math.hypot(x[i] - x[i - 1], r[i] - r[i - 1])
            dQ = q * 2 * math.pi * ri * ds
            Q_total += dQ
            h_c_enth += dQ / mdot_c
            f = (-1.8 * math.log10((eps_rough / ch["Dh"] / 3.7) ** 1.11 + 6.9 / Re_c)) ** -2
            p_c -= f * ds / ch["Dh"] * st["rho"] * v * v / 2
            if p_c <= p_gas:
                raise ValueError("Coolant pressure fell below chamber pressure: raise the inlet "
                                 "pressure or enlarge the channels.")

    out["r_hot"] = r.copy()
    out["x"] = x.copy()
    out["Q_total"] = Q_total
    out["coolant_dT"] = out["T_cool"][0] - out["T_cool"][-1]
    out["coolant_dp"] = out["p_cool"][-1] - out["p_cool"][0]
    out["coolant"] = prop["coolant"]
    return out


def jacket_thickness(design, perf, cooling):
    """Constant jacket thickness from hoop stress at the highest coolant pressure (min 2 mm)."""
    jm = MATERIALS[design["jacket_material"]]
    h = design["channel_height_mm"] / 1e3
    r_out = cooling["r_hot"] + cooling["t_liner"] + h
    need = cooling["p_cool"] * r_out * design["safety_factor"] / jm["sy"]
    return max(0.002, float(np.max(need)))

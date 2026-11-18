"""Ideal rocket performance: sizes the throat and exit from thrust and pressure.

Uses one-dimensional isentropic flow of a calorically perfect gas
(Sutton & Biblarz, Rocket Propulsion Elements, ch. 3).
"""
import math
from .data import PROPELLANTS, G0, R_UNIVERSAL


def area_ratio(M, g):
    """A/A* for Mach number M."""
    return (1 / M) * ((2 / (g + 1)) * (1 + (g - 1) / 2 * M * M)) ** ((g + 1) / (2 * (g - 1)))


def mach_from_area_ratio(ar, g, supersonic):
    """Invert the area-Mach relation by bisection."""
    if ar <= 1.0 + 1e-9:
        return 1.0
    lo, hi = (1.0, 60.0) if supersonic else (1e-5, 1.0)
    for _ in range(200):
        m = 0.5 * (lo + hi)
        f = area_ratio(m, g) - ar
        if (f > 0) == supersonic:
            hi = m
        else:
            lo = m
    return 0.5 * (lo + hi)


def static_pressure_ratio(M, g):
    """p/p0 for Mach number M."""
    return (1 + (g - 1) / 2 * M * M) ** (-g / (g - 1))


def size_engine(design):
    """Return a dict with the main performance numbers and dimensions (SI)."""
    p = PROPELLANTS[design["propellant"]]
    g, Tc = p["gamma"], p["Tc"]
    R = R_UNIVERSAL / p["M"]
    Pc = design["chamber_pressure_bar"] * 1e5
    Pa = design["ambient_pressure_bar"] * 1e5
    eps = design["expansion_ratio"]
    F = design["thrust_kN"] * 1e3

    cstar = math.sqrt(g * R * Tc) / (g * math.sqrt((2 / (g + 1)) ** ((g + 1) / (g - 1))))
    Me = mach_from_area_ratio(eps, g, True)
    pe_ratio = static_pressure_ratio(Me, g)
    Pe = pe_ratio * Pc
    cf_momentum = math.sqrt(2 * g * g / (g - 1) * (2 / (g + 1)) ** ((g + 1) / (g - 1))
                            * (1 - pe_ratio ** ((g - 1) / g)))
    CF = cf_momentum + eps * (Pe - Pa) / Pc
    CF_vac = cf_momentum + eps * pe_ratio
    CF_sl = cf_momentum + eps * (Pe - 101325) / Pc

    At = F / (CF * Pc)
    Rt = math.sqrt(At / math.pi)
    mdot = Pc * At / cstar
    mdot_fuel = mdot / (1 + p["OF"])

    warnings = []
    if Pa > 0 and Pe < 0.4 * Pa:
        warnings.append(f"Exit pressure {Pe/1e5:.2f} bar is below 40% of ambient: "
                        "flow separation likely (Summerfield criterion).")

    return dict(
        gamma=g, R=R, Tc=Tc, M_gas=p["M"], OF=p["OF"], Lstar=p["Lstar"],
        Pc=Pc, Pa=Pa, eps=eps, F=F, contraction_ratio=design["contraction_ratio"],
        cstar=cstar, Me=Me, Pe=Pe, CF=CF, CF_vac=CF_vac, CF_sl=CF_sl,
        Isp=CF * cstar / G0, Isp_vac=CF_vac * cstar / G0, Isp_sl=CF_sl * cstar / G0,
        At=At, Rt=Rt, Re=Rt * math.sqrt(eps), Rc=Rt * math.sqrt(design["contraction_ratio"]),
        mdot=mdot, mdot_fuel=mdot_fuel, mdot_ox=mdot - mdot_fuel, warnings=warnings,
    )

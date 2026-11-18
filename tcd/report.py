"""Plots, data tables, SolidWorks curve files and a Markdown design report."""
import math
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle

from .data import MATERIALS, PROPELLANTS
from .geometry import offset_curve

COPPER, STEEL, GAS, COOL, INK = "#c0713a", "#8a9299", "#f2d7c9", "#2f6fdb", "#111418"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.grid": True, "grid.alpha": 0.25})


def write_curves(outdir, contour, cooling, design, t_jacket):
    """SolidWorks 'Curve Through XYZ Points' files (mm, tab separated) + full CSV."""
    os.makedirs(outdir, exist_ok=True)
    x, r = contour["x"], contour["r"]
    h = design["channel_height_mm"] / 1e3
    layers = {
        "1_hot_gas_wall": (x, r),
        "2_channel_floor": offset_curve(x, r, cooling["t_liner"]),
        "3_liner_outer": offset_curve(x, r, cooling["t_liner"] + h),
        "4_jacket_outer": offset_curve(x, r, cooling["t_liner"] + h + t_jacket),
    }
    files = []
    for name, (lx, lr) in layers.items():
        f = os.path.join(outdir, f"solidworks_curve_{name}.txt")
        with open(f, "w") as fh:
            for a, b in zip(lx, lr):
                fh.write(f"{a*1e3:.4f}\t{b*1e3:.4f}\t0\n")
        files.append(f)
    cols = ["x", "r_hot_wall", "t_liner", "M", "p_gas", "Taw", "hg", "q", "Twg", "Twc", "T_cool",
            "p_cool", "v_cool", "Re_cool", "hc", "fin_eff", "w", "rib", "sigma_thermal",
            "sigma_pressure", "sigma_total", "margin"]
    units = ["mm", "mm", "mm", "-", "bar", "K", "W/m2K", "MW/m2", "K", "K", "K", "bar", "m/s", "-",
             "W/m2K", "-", "mm", "mm", "MPa", "MPa", "MPa", "-"]
    scale = dict(x=1e3, r_hot_wall=1e3, t_liner=1e3, p_gas=1e-5, q=1e-6, p_cool=1e-5, w=1e3, rib=1e3,
                 sigma_thermal=1e-6, sigma_pressure=1e-6, sigma_total=1e-6)
    data = dict(cooling); data["r_hot_wall"] = r
    f = os.path.join(outdir, "station_data.csv")
    with open(f, "w") as fh:
        fh.write(",".join(f"{c}[{u}]" for c, u in zip(cols, units)) + "\n")
        for i in range(len(x)):
            fh.write(",".join(f"{data[c][i]*scale.get(c,1):.6g}" for c in cols) + "\n")
    files.append(f)
    return files


def plot_section(ax, contour, cooling, design, t_jacket, perf):
    x, r = contour["x"] * 1e3, contour["r"] * 1e3
    h = design["channel_height_mm"]
    t = cooling["t_liner"] * 1e3
    xb, rb = offset_curve(x, r, t)
    xc, rc = offset_curve(x, r, t + h)
    xd, rd = offset_curve(x, r, t + h + t_jacket * 1e3)
    for s in (1, -1):
        ax.fill_between(x, 0, s * r, color=GAS, lw=0)
        ax.fill(np.r_[x, xb[::-1]], s * np.r_[r, rb[::-1]], color=COPPER, lw=0)
        ax.fill(np.r_[xb, xc[::-1]], s * np.r_[rb, rc[::-1]], color=COOL, alpha=0.55, lw=0)
        ax.fill(np.r_[xc, xd[::-1]], s * np.r_[rc, rd[::-1]], color=STEEL, lw=0)
        ax.plot(x, s * r, color=INK, lw=0.8)
    ax.axhline(0, color=INK, lw=0.6, ls=(0, (12, 3, 2, 3)))
    ax.axvline(0, color="#d62f1f", lw=0.8)
    ax.set_aspect("equal"); ax.grid(False)
    ax.set_xlabel("axial position from throat [mm]"); ax.set_ylabel("radius [mm]")
    ax.text(0, -r.min() * 0.45, f"throat Ø{2*perf['Rt']*1e3:.1f}", ha="center", va="center", color="#d62f1f", fontsize=9,
            bbox=dict(fc=GAS, ec="none", pad=1.5))
    ax.text(x[0], r[0] + h + 12, f"chamber Ø{2*perf['Rc']*1e3:.0f}", fontsize=9)
    ax.text(x[-1], r[-1] + h + 12, f"exit Ø{2*perf['Re']*1e3:.0f}", ha="right", fontsize=9)


def plot_channel_section(ax, design, cooling, contour, t_jacket):
    """Radial cut at the throat: hot wall, channels, ribs and jacket (one sector, to scale)."""
    it = contour["throat_index"]
    r0 = contour["r"][it] * 1e3
    t = cooling["t_liner"][it] * 1e3
    h = design["channel_height_mm"]
    tj = t_jacket * 1e3
    N = design["channel_count"]
    pitch_deg = 360 / N
    frac = cooling["w"][it] / (cooling["w"][it] + cooling["rib"][it])
    span = 6
    base = 90 - span * pitch_deg / 2
    ax.add_patch(Wedge((0, 0), r0 + t + h + tj, base, base + span * pitch_deg, width=tj, color=STEEL))
    ax.add_patch(Wedge((0, 0), r0 + t + h, base, base + span * pitch_deg, width=h + t, color=COPPER))
    for k in range(span):
        a0 = base + k * pitch_deg + (1 - frac) * pitch_deg / 2
        ax.add_patch(Wedge((0, 0), r0 + t + h, a0, a0 + frac * pitch_deg, width=h, color=COOL, alpha=0.75))
    ax.add_patch(Wedge((0, 0), r0, base, base + span * pitch_deg, color=GAS))
    th = math.radians(90)
    ax.set_xlim(-(r0 + 12) * math.sin(math.radians(span * pitch_deg / 2)) - 2,
                (r0 + 12) * math.sin(math.radians(span * pitch_deg / 2)) + 2)
    ax.set_ylim(r0 - 3, r0 + t + h + tj + 2)
    ax.set_aspect("equal"); ax.grid(False)
    ax.set_xlabel("mm"); ax.set_ylabel("radius [mm]")
    ax.set_title(f"Throat cross-section: {N} channels, {cooling['w'][it]*1e3:.2f} × {h:.2f} mm, "
                 f"rib {cooling['rib'][it]*1e3:.2f} mm, hot wall {t:.2f} mm", fontsize=10)


def make_plots(outdir, perf, contour, cooling, design, t_jacket):
    os.makedirs(outdir, exist_ok=True)
    x = contour["x"] * 1e3
    files = []

    fig, ax = plt.subplots(figsize=(11, 4.6))
    plot_section(ax, contour, cooling, design, t_jacket, perf)
    ax.set_title("Half-section: hot gas (pink), copper liner, cooling channels (blue), Inconel jacket (grey)")
    f = os.path.join(outdir, "section.png"); fig.tight_layout(); fig.savefig(f, dpi=150); plt.close(fig); files.append(f)

    fig, ax = plt.subplots(figsize=(8, 4.2))
    plot_channel_section(ax, design, cooling, contour, t_jacket)
    f = os.path.join(outdir, "channel_section.png"); fig.tight_layout(); fig.savefig(f, dpi=150); plt.close(fig); files.append(f)

    fig, axs = plt.subplots(2, 2, figsize=(12, 7.5), sharex=True)
    a = axs[0, 0]
    a.plot(x, cooling["q"] / 1e6, color="#d62f1f"); a.set_ylabel("heat flux [MW/m²]"); a.set_title("Gas-side heat flux (Bartz)")
    a = axs[0, 1]
    lim = MATERIALS[design["liner_material"]]["T_max"]
    a.plot(x, cooling["Twg"], color="#d62f1f", label="hot wall")
    a.plot(x, cooling["Twc"], color=COPPER, label="channel-side wall")
    a.plot(x, cooling["T_cool"], color=COOL, label="coolant")
    a.axhline(lim, color=INK, ls="--", lw=0.8, label=f"{design['liner_material']} limit")
    a.set_ylabel("temperature [K]"); a.legend(fontsize=8); a.set_title("Wall and coolant temperature")
    a = axs[1, 0]
    a.plot(x, cooling["p_cool"] / 1e5, color=COOL, label="coolant pressure")
    a.set_ylabel("pressure [bar]")
    a2 = a.twinx(); a2.plot(x, cooling["v_cool"], color=INK, lw=0.9, ls="--"); a2.set_ylabel("coolant velocity [m/s] (dashed)")
    a2.grid(False); a.set_title("Coolant pressure (flows right to left) and velocity")
    a.set_xlabel("axial position from throat [mm]")
    a = axs[1, 1]
    a.plot(x, cooling["sigma_thermal"] / 1e6, color="#d62f1f", label="thermal (secondary)")
    a.plot(x, cooling["sigma_pressure"] / 1e6, color=COOL, label="pressure bending (primary)")
    sy = MATERIALS[design["liner_material"]]["sy"] / 1e6
    a.axhline(2 * sy, color=INK, ls="--", lw=0.8, label="shakedown limit 2·Sy")
    a.axhline(sy / design["safety_factor"], color=COOL, ls=":", lw=1, label="primary allowable Sy/SF")
    a.set_ylabel("stress [MPa]"); a.legend(fontsize=8); a.set_title("Hot-wall stress")
    a.set_xlabel("axial position from throat [mm]")
    for a in axs.flat:
        a.axvline(0, color="#999", lw=0.6)
    fig.tight_layout()
    f = os.path.join(outdir, "thermal_analysis.png"); fig.savefig(f, dpi=150); plt.close(fig); files.append(f)
    return files


def _vtk_render(shapes, outfile, cam_pos, focal, view_up=(0, 1, 0), size=(1600, 900), zoom=1.0):
    """Render CadQuery shapes offscreen with VTK. shapes = [(shape, rgb), ...]"""
    import vtk
    ren = vtk.vtkRenderer()
    ren.SetBackground(1, 1, 1)
    for shp, rgb in shapes:
        pd = shp.toVtkPolyData(0.05, 0.1, normals=True)
        m = vtk.vtkPolyDataMapper(); m.SetInputData(pd)
        a = vtk.vtkActor(); a.SetMapper(m)
        pr = a.GetProperty(); pr.SetColor(*rgb); pr.SetSpecular(0.35); pr.SetSpecularPower(25)
        pr.SetDiffuse(0.85); pr.SetAmbient(0.18)
        ren.AddActor(a)
    kit = vtk.vtkLightKit(); kit.AddLightsToRenderer(ren)
    rw = vtk.vtkRenderWindow(); rw.SetOffScreenRendering(1); rw.AddRenderer(ren); rw.SetSize(*size)
    rw.SetMultiSamples(8)
    cam = ren.GetActiveCamera()
    cam.SetPosition(*cam_pos); cam.SetFocalPoint(*focal); cam.SetViewUp(*view_up)
    ren.ResetCamera(); cam.Zoom(zoom); ren.ResetCameraClippingRange()
    rw.Render()
    w = vtk.vtkWindowToImageFilter(); w.SetInput(rw); w.Update()
    png = vtk.vtkPNGWriter(); png.SetFileName(outfile); png.SetInputConnection(w.GetOutputPort()); png.Write()
    return outfile


def render_cutaway(parts, outdir, throat_x=0.0, throat_r=50.0):
    """Two renders: the whole chamber with a quarter cut away, and a throat slice showing the channels."""
    import cadquery as cq
    os.makedirs(outdir, exist_ok=True)
    cu, st = matplotlib.colors.to_rgb(COPPER), matplotlib.colors.to_rgb(STEEL)
    L, J = parts["liner"].val(), parts["jacket"].val()
    quarter = cq.Solid.makeBox(4000, 2000, 2000, cq.Vector(-2000, 0, 0))     # removes y>0, z>0
    shapes = [(L.cut(quarter), cu), (J.cut(quarter), st)]
    f1 = _vtk_render(shapes, os.path.join(outdir, "cutaway.png"),
                     cam_pos=(-900, 900, 1300), focal=(0, 0, 0), view_up=(0, 1, 0), zoom=1.35)
    w = max(25.0, 0.6 * throat_r)
    keep = cq.Solid.makeBox(2 * w, 4000, 4000, cq.Vector(throat_x - w, -2000, -2000))
    half = cq.Solid.makeBox(4000, 2000, 4000, cq.Vector(-2000, -2000, -2000))  # keep y>=0 only
    sl = [(L.intersect(keep).intersect(half), cu), (J.intersect(keep).intersect(half), st)]
    f2 = _vtk_render(sl, os.path.join(outdir, "throat_slice.png"),
                     cam_pos=(throat_x - 6 * throat_r, 3 * throat_r, 2.5 * throat_r), focal=(throat_x, throat_r, 0),
                     view_up=(0, 1, 0), zoom=1.2)
    return [f1, f2]


def write_report(path, design, perf, contour, cooling, t_jacket, volumes=None):
    it = contour["throat_index"]
    lm, jm = MATERIALS[design["liner_material"]], MATERIALS[design["jacket_material"]]
    imax = int(np.argmax(cooling["Twg"])); imin = int(np.argmin(cooling["margin"]))
    rows = [
        ("Propellant", f"{design['propellant']} at O/F {perf['OF']}"),
        ("Thrust (design ambient)", f"{perf['F']/1e3:.1f} kN at {perf['Pa']/1e5:.3f} bar"),
        ("Chamber pressure", f"{perf['Pc']/1e5:.0f} bar"),
        ("Specific impulse: design / sea level / vacuum", f"{perf['Isp']:.0f} / {perf['Isp_sl']:.0f} / {perf['Isp_vac']:.0f} s"),
        ("Characteristic velocity c*", f"{perf['cstar']:.0f} m/s"),
        ("Thrust coefficient C_F", f"{perf['CF']:.3f}"),
        ("Mass flow: total / fuel / oxidizer", f"{perf['mdot']:.2f} / {perf['mdot_fuel']:.2f} / {perf['mdot_ox']:.2f} kg/s"),
        ("Throat / chamber / exit diameter", f"{2*perf['Rt']*1e3:.1f} / {2*perf['Rc']*1e3:.1f} / {2*perf['Re']*1e3:.1f} mm"),
        ("Expansion / contraction ratio", f"{perf['eps']:.1f} / {perf['contraction_ratio']:.1f}"),
        ("Exit Mach / exit pressure", f"{perf['Me']:.2f} / {perf['Pe']/1e5:.3f} bar"),
        ("Length: cylinder / converging / nozzle / total", f"{contour['L_cyl']*1e3:.0f} / {contour['L_conv']*1e3:.0f} / {contour['L_nozzle']*1e3:.0f} / {contour['L_total']*1e3:.0f} mm"),
        ("Bell angles θn / θe", f"{math.degrees(contour['theta_n']):.1f}° / {math.degrees(contour['theta_e']):.1f}°"),
    ]
    cool = [
        ("Coolant", f"{cooling['coolant']} (all fuel), {perf['mdot_fuel']:.2f} kg/s"),
        ("Channels", f"{design['channel_count']} × {design['channel_height_mm']} mm deep; throat width {cooling['w'][it]*1e3:.2f} mm, rib {cooling['rib'][it]*1e3:.2f} mm"),
        ("Channel wedge angle (for a SolidWorks revolved cut)",
         f"{360/design['channel_count']*cooling['w'][it]/(cooling['w'][it]+cooling['rib'][it]):.2f}° of every {360/design['channel_count']:.2f}°"),
        ("Hot-wall thickness at throat", f"{cooling['t_liner'][it]*1e3:.2f} mm ({design['liner_material']})"),
        ("Total heat load", f"{cooling['Q_total']/1e6:.2f} MW"),
        ("Peak heat flux", f"{cooling['q'].max()/1e6:.1f} MW/m²"),
        ("Peak hot-wall temperature", f"{cooling['Twg'][imax]:.0f} K at x = {contour['x'][imax]*1e3:.0f} mm (limit ≈ {lm['T_max']:.0f} K)"),
        ("Coolant temperature: in → out", f"{cooling['T_cool'][-1]:.0f} → {cooling['T_cool'][0]:.0f} K"),
        ("Coolant pressure: in → out (drop)", f"{cooling['p_cool'][-1]/1e5:.1f} → {cooling['p_cool'][0]/1e5:.1f} bar ({cooling['coolant_dp']/1e5:.1f} bar)"),
        ("Peak coolant velocity", f"{cooling['v_cool'].max():.0f} m/s"),
        ("Lowest liner stress margin", f"{cooling['margin'][imin]:+.2f} at x = {contour['x'][imin]*1e3:.0f} mm"),
        ("Jacket thickness", f"{t_jacket*1e3:.2f} mm ({design['jacket_material']})"),
    ]
    if volumes:
        ml, mj = volumes["liner"] * 1e-9 * lm["rho"], volumes["jacket"] * 1e-9 * jm["rho"]
        cool.append(("Estimated mass: liner / jacket+flange", f"{ml:.1f} / {mj:.1f} kg (total {ml+mj:.1f} kg)"))
    warn = list(perf["warnings"])
    if cooling["Twg"].max() > lm["T_max"]:
        warn.append("Hot-wall temperature exceeds the liner material limit.")
    if cooling["margin"].min() < 0:
        warn.append("Liner stress margin is negative somewhere: see thermal_analysis.png.")
    if cooling["coolant_dp"] > 0.3 * perf["Pc"]:
        warn.append("Coolant pressure drop exceeds 30% of chamber pressure: pump power penalty.")
    tbl = lambda rs: "| | |\n|---|---|\n" + "\n".join(f"| {a} | {b} |" for a, b in rs)
    md = f"""# Design report: {design.get('name','thrust chamber')}

Generated by `run.py`. All numbers are preliminary-design estimates (see README, *Assumptions*).

![Half-section](section.png)

## Performance and geometry
{tbl(rows)}

## Regenerative cooling and structure
{tbl(cool)}

![Thermal analysis](thermal_analysis.png)

![Throat channel section](channel_section.png)

## Design checks
{chr(10).join('- ⚠️ ' + w for w in warn) if warn else '- ✅ All checks pass: wall temperature under the material limit, positive liner stress margins, coolant pressure drop under 30% of chamber pressure.'}
"""
    with open(path, "w") as fh:
        fh.write(md)
    return path

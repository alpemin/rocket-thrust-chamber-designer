"""3-D CAD model of the thrust chamber with CadQuery (OpenCASCADE kernel).

Bodies:
  liner   - copper-alloy hot wall with N milled cooling channels
  jacket  - structural closeout over the channels, with an injector flange
            and bolt holes

Exports STEP (opens as a solid part in SolidWorks, Fusion 360, Onshape,
CATIA, NX, FreeCAD) and STL (3-D printing / slicers).
All CAD units are millimetres. The engine axis is the X axis; the throat is at x = 0.
"""
import math
import numpy as np
import cadquery as cq

from .geometry import offset_curve


def _profile_solid(x_in, r_in, x_out, r_out, angle=360.0):
    """Revolve the region between two curves (mm) about the X axis."""
    pin = list(zip(x_in, r_in))
    pout = list(zip(x_out, r_out))[::-1]
    wp = (cq.Workplane("XY").moveTo(*pin[0]).spline(pin[1:], includeCurrent=True)
          .lineTo(*pout[0]).spline(pout[1:], includeCurrent=True).close())
    return wp.revolve(angle, (0, 0, 0), (1, 0, 0))


N_SPLINE = 60   # points per spline (same for every layer): CAD stays within ~0.05 mm of the contour


def _thin(x, r, *arrs, n=N_SPLINE):
    """Downsample curves to n points, packed where the wall curves sharply (the throat),
    so a short spline still follows the contour closely. All layers use the same indices."""
    dx, dr = np.gradient(x), np.gradient(r)
    ddx, ddr = np.gradient(dx), np.gradient(dr)
    kappa = np.abs(dx * ddr - dr * ddx) / (dx * dx + dr * dr) ** 1.5
    ds = np.hypot(dx, dr)
    dens = ds * (1 + 6 * kappa * r.min())
    c = np.concatenate([[0], np.cumsum(dens[1:])])
    idx = np.unique(np.searchsorted(c, np.linspace(0, c[-1], n)).clip(0, len(x) - 1))
    return [a[idx] for a in (x, r) + arrs]


def build_cad(design, contour, cooling, t_jacket, channels=True, flange=True):
    x, r = contour["x"], contour["r"]
    t_l = cooling["t_liner"]
    h = design["channel_height_mm"] / 1e3
    N = int(design["channel_count"])

    mm = 1e3
    # layer surfaces (offset along the wall normal)
    xa, ra = x, r
    xb, rb = offset_curve(x, r, t_l)                 # liner outer / channel floor
    xc, rc = offset_curve(x, r, t_l + h)              # channel top / jacket inner
    xd, rd = offset_curve(x, r, t_l + h + t_jacket)   # jacket outer

    X = lambda *a: [v * mm for v in a]
    xa_, ra_, xc_, rc_ = _thin(*X(xa, ra, xc, rc))
    liner = _profile_solid(xa_, ra_, xc_, rc_)

    if channels:
        # Channels stop 4 mm short of each end so they close inside the liner;
        # the coolant manifolds that feed them are left for the designer.
        L = len(x)
        sx = np.concatenate([[0], np.cumsum(np.hypot(np.diff(x), np.diff(r)))]) * mm
        keep = (sx > 4) & (sx < sx[-1] - 4)
        # cut 0.3 mm past the liner's outer surface so the faces are not coincident
        xe, re_ = offset_curve(x, r, t_l + h + 0.3e-3)
        bx, br, cx_, cr_ = _thin(xb[keep] * mm, rb[keep] * mm, xe[keep] * mm, re_[keep] * mm)
        # Rib fraction from the throat definition (constant angle wedges).
        it = contour["throat_index"]
        r_mid_t = (r[it] + t_l[it] + h / 2)
        pitch_t = 2 * math.pi * r_mid_t / N
        frac = 1 - (design["rib_width_at_throat_mm"] / 1e3) / pitch_t
        ang = 360.0 / N * frac
        wedge = _profile_solid(bx, br, cx_, cr_, angle=ang).val()
        wedges = [wedge.rotate(cq.Vector(0, 0, 0), cq.Vector(1, 0, 0), k * 360.0 / N) for k in range(N)]
        liner = cq.Workplane("XY").add(liner.val().cut(cq.Compound.makeCompound(wedges)))

    xc2, rc2, xd2, rd2 = _thin(*X(xc, rc, xd, rd))
    jacket = _profile_solid(xc2, rc2, xd2, rd2)

    if flange:
        # Injector flange at the upstream end: ring + bolt circle.
        x0 = xd[0] * mm
        r_in = rc[0] * mm
        r_out = rd[0] * mm + max(25.0, 0.25 * rd[0] * mm)
        thk = max(10.0, 0.08 * rd[0] * mm)
        ring = (cq.Workplane("YZ", origin=(x0, 0, 0)).circle(r_out).circle(r_in).extrude(thk))
        n_bolts = 12 if r_out < 150 else 24
        r_bc = (rd[0] * mm + r_out) / 2
        d_bolt = 8.4 if r_out < 150 else 10.5   # clearance for M8 / M10
        holes = (cq.Workplane("YZ", origin=(x0, 0, 0))
                 .polarArray(r_bc, 0, 360, n_bolts).circle(d_bolt / 2).extrude(thk))
        jacket = jacket.union(ring.cut(holes))

    return dict(liner=liner, jacket=jacket,
                bolt_note="12 x M8 clearance holes" if flange else "")


def export_cad(parts, outdir):
    import os
    from cadquery import exporters
    os.makedirs(outdir, exist_ok=True)
    asm = cq.Assembly(name="thrust_chamber")
    asm.add(parts["liner"], name="liner", color=cq.Color(0.72, 0.45, 0.2))
    asm.add(parts["jacket"], name="jacket", color=cq.Color(0.6, 0.62, 0.65))
    files = {}
    for name in ("liner", "jacket"):
        f = os.path.join(outdir, f"{name}.step")
        exporters.export(parts[name], f)
        files[name + "_step"] = f
    f = os.path.join(outdir, "thrust_chamber_assembly.step")
    asm.export(f)
    files["assembly_step"] = f
    both = parts["liner"].val().fuse(parts["jacket"].val())
    f = os.path.join(outdir, "thrust_chamber.stl")
    exporters.export(cq.Workplane().add(both), f, tolerance=0.05, angularTolerance=0.15)
    files["stl"] = f
    # GitHub's browser upload limit is 25 MB per file: zip any STEP file bigger than 20 MB
    import zipfile
    for key in ("liner_step", "assembly_step"):
        f = files[key]
        if os.path.getsize(f) > 20e6:
            z = f[:-5] + "_STEP.zip"
            with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
                zf.write(f, os.path.basename(f))
            os.remove(f)
            files[key] = z
    vol = {n: parts[n].val().Volume() for n in ("liner", "jacket")}   # mm^3
    return files, vol

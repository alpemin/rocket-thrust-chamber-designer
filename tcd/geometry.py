"""Chamber and nozzle contour.

Layout along the axis (x = 0 at the throat, negative x upstream):
  cylindrical chamber -> fillet (radius 1.0 Rt) -> 30 deg converging cone
  -> upstream throat arc (1.5 Rt) -> downstream throat arc (0.382 Rt)
  -> Rao 80% bell drawn as a quadratic Bezier curve to the exit.

The whole curve is tangent-continuous, so it can be offset outward to get the
liner, cooling channel and jacket surfaces.
"""
import math
import numpy as np

# Rao 80% bell: initial (theta_n) and exit (theta_e) wall angles vs expansion ratio.
_RAO_EPS = [4, 10, 25, 50, 100]
_RAO_TN = [21.5, 26.5, 30.0, 32.5, 35.0]
_RAO_TE = [14.0, 10.0, 8.5, 7.5, 7.0]


def rao_angles(eps):
    le = math.log(eps)
    xs = [math.log(e) for e in _RAO_EPS]
    return (math.radians(np.interp(le, xs, _RAO_TN)), math.radians(np.interp(le, xs, _RAO_TE)))


def build_contour(perf, n_points=600, conv_half_angle_deg=30.0):
    """Return dict with x, r arrays (m), ordered injector -> exit, plus key lengths."""
    Rt, Rc, Re, eps = perf["Rt"], perf["Rc"], perf["Re"], perf["eps"]
    b = math.radians(conv_half_angle_deg)
    Ru, Rd, R1 = 1.5 * Rt, 0.382 * Rt, 1.0 * Rt
    tn, te = rao_angles(eps)

    # Upstream throat arc starts where its slope equals the cone angle.
    xa, ra = -Ru * math.sin(b), Rt + Ru - Ru * math.cos(b)
    # Chamber fillet: ends on the cone at radius r1e.
    r1e = Rc - R1 * (1 - math.cos(b))
    x1e = xa - (r1e - ra) / math.tan(b)
    xc = x1e - R1 * math.sin(b)                      # end of cylinder / start of fillet

    # Chamber volume from L* sets the cylinder length.
    At = perf["At"]
    Vc_target = perf["Lstar"] * At
    seg = []
    # sample converging section first to get its volume
    conv = []
    for phi in np.linspace(0, b, 20):
        conv.append((xc + R1 * math.sin(phi), Rc - R1 + R1 * math.cos(phi)))
    for t in np.linspace(0, 1, 20)[1:]:
        conv.append((x1e + (xa - x1e) * t, r1e + (ra - r1e) * t))
    for a in np.linspace(-(math.pi / 2 + b), -math.pi / 2, 30)[1:]:
        conv.append((Ru * math.cos(a), Ru * math.sin(a) + Rt + Ru))
    cx = np.array([p[0] for p in conv]); cr = np.array([p[1] for p in conv])
    V_conv = float(np.trapezoid(math.pi * cr ** 2, cx))
    L_cyl = max((Vc_target - V_conv) / (math.pi * Rc ** 2), 0.5 * Rc)
    x0 = xc - L_cyl

    for t in np.linspace(0, 1, 20)[:-1]:
        seg.append((x0 + L_cyl * t, Rc))
    seg += conv
    for a in np.linspace(0, tn, 25)[1:]:
        seg.append((Rd * math.sin(a), Rt + Rd - Rd * math.cos(a)))

    Nx, Ny = Rd * math.sin(tn), Rt + Rd * (1 - math.cos(tn))
    Ln = 0.8 * (math.sqrt(eps) - 1) * Rt / math.tan(math.radians(15))
    Ex, Ey = Ln, Re
    Qx = (Ey - Ny + math.tan(tn) * Nx - math.tan(te) * Ex) / (math.tan(tn) - math.tan(te))
    Qy = Ny + math.tan(tn) * (Qx - Nx)
    for t in np.linspace(0, 1, 80)[1:]:
        u = 1 - t
        seg.append((u * u * Nx + 2 * u * t * Qx + t * t * Ex, u * u * Ny + 2 * u * t * Qy + t * t * Ey))

    x = np.array([p[0] for p in seg]); r = np.array([p[1] for p in seg])
    # resample at uniform arc length, then make sure the exact throat point is included
    s = np.concatenate([[0], np.cumsum(np.hypot(np.diff(x), np.diff(r)))])
    su = np.linspace(0, s[-1], n_points)
    xu, ru = np.interp(su, s, x), np.interp(su, s, r)
    it = int(np.argmin(np.abs(xu)))
    xu[it], ru[it] = 0.0, Rt

    return dict(x=xu, r=ru, s=su, throat_index=it, L_cyl=L_cyl, L_conv=-x0 - L_cyl,
                L_nozzle=Ln, L_total=Ln - x0, x_injector=x0, theta_n=tn, theta_e=te,
                V_chamber=Vc_target)


def offset_curve(x, r, d):
    """Offset a curve by distance d along its outward normal (away from the axis)."""
    dx, dr = np.gradient(x), np.gradient(r)
    L = np.hypot(dx, dr)
    nx, nr = -dr / L, dx / L
    return x + d * nx, r + d * nr

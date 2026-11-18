"""Design a regeneratively cooled rocket thrust chamber and export CAD.

Usage:
    python run.py                                 # default design
    python run.py designs/methane_100kN.json      # pick a design file
    python run.py designs/my_engine.json --no-cad # analysis only (fast)

Outputs go to outputs/<design file name>/
"""
import argparse
import json
import os
import time

from tcd.performance import size_engine
from tcd.geometry import build_contour
from tcd.cooling import run_cooling, jacket_thickness
from tcd import report


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("design", nargs="?", default="designs/methane_100kN.json")
    ap.add_argument("--no-cad", action="store_true", help="skip the 3-D model (CadQuery not needed)")
    ap.add_argument("--no-channels", action="store_true", help="CAD without cooling channels (much faster)")
    args = ap.parse_args()

    with open(args.design) as fh:
        design = json.load(fh)
    out = os.path.join("outputs", os.path.splitext(os.path.basename(args.design))[0])
    os.makedirs(out, exist_ok=True)
    t0 = time.time()

    print(f"Designing: {design.get('name', args.design)}")
    perf = size_engine(design)
    contour = build_contour(perf)
    cooling = run_cooling(design, perf, contour)
    t_jacket = jacket_thickness(design, perf, cooling)
    print(f"  Isp {perf['Isp']:.0f} s, throat Ø{2*perf['Rt']*1e3:.1f} mm, mass flow {perf['mdot']:.1f} kg/s")
    print(f"  peak hot wall {cooling['Twg'].max():.0f} K, coolant dp {cooling['coolant_dp']/1e5:.1f} bar, "
          f"min stress margin {cooling['margin'].min():+.2f}")

    report.write_curves(out, contour, cooling, design, t_jacket)
    report.make_plots(out, perf, contour, cooling, design, t_jacket)

    volumes = None
    if not args.no_cad:
        from tcd.cad import build_cad, export_cad
        print("  building 3-D model (a few minutes with channels)...")
        parts = build_cad(design, contour, cooling, t_jacket, channels=not args.no_channels)
        files, volumes = export_cad(parts, out)
        try:
            report.render_cutaway(parts, out, throat_r=perf["Rt"] * 1e3)
        except Exception as e:  # rendering is optional
            print(f"  (cutaway render skipped: {e})")

    report.write_report(os.path.join(out, "REPORT.md"), design, perf, contour, cooling, t_jacket, volumes)
    print(f"Done in {time.time()-t0:.0f} s. Results in {out}/")


if __name__ == "__main__":
    main()

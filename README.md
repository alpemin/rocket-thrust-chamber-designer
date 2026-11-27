# Rocket Thrust Chamber Designer

**Preliminary design of a regeneratively cooled liquid-rocket thrust chamber, from requirements to SolidWorks-ready CAD.**

You enter thrust, chamber pressure and propellant. The program sizes the nozzle, designs the cooling
channels, checks that the walls survive the heat and pressure, and builds a 3-D model with all
100 cooling channels that opens directly in SolidWorks.

![Cutaway of the 100 kN methane thrust chamber](outputs/methane_100kN/cutaway.png)

| Throat slice: 100 milled cooling channels in a GRCop-42 copper liner, closed out by an Inconel 718 jacket |
|---|
| ![Throat slice](outputs/methane_100kN/throat_slice.png) |

🔗 **[Open the interactive 3D calculator](https://alpemin.github.io/rocket-thrust-chamber-designer/web/)**
Enter thrust, chamber pressure and propellant, and get a rotatable 3D thrust chamber with all 100 cooling
channels, a heat-flux colour map and a SolidWorks curve export, live in your browser.

🧊 **3D model of the example engine:** [`thrust_chamber.stl`](outputs/methane_100kN/thrust_chamber.stl) opens in GitHub's built-in 3D viewer, so you can rotate it right here.

## 3D model: rotate it

Drag to rotate, scroll to zoom. This is a simplified cutaway of the 100 kN example engine (chamber, throat and Rao bell, wall layers merged).
The full model with all 100 cooling channels is in the STEP/STL files below and in the [3D calculator](https://alpemin.github.io/rocket-thrust-chamber-designer/web/).

```stl
solid chamber
facet normal 0.00 -0.99 -0.12
outer loop
vertex -393.4 85.1 0
vertex -260.1 85.1 0
vertex -260.1 82.7 19.9
endloop
endfacet
facet normal 0.00 -0.99 -0.12
outer loop
vertex -393.4 85.1 0
vertex -260.1 82.7 19.9
vertex -393.4 82.7 19.9
endloop
endfacet
facet normal 0.00 0.99 0.12
outer loop
vertex -393.4 76.2 0
vertex -393.4 74.1 17.8
vertex -260.1 74.1 17.8
endloop
endfacet
facet normal 0.00 0.99 0.12
outer loop
vertex -393.4 76.2 0
vertex -260.1 74.1 17.8
vertex -260.1 76.2 0
endloop
endfacet
facet normal 0.00 -0.99 -0.12
outer loop
vertex -260.1 85.1 0
vertex -126.8 85.1 0
vertex -126.8 82.7 19.9
endloop
endfacet
facet normal 0.00 -0.99 -0.12
outer loop
vertex -260.1 85.1 0
vertex -126.8 82.7 19.9
vertex -260.1 82.7 19.9
endloop
endfacet
facet normal 0.00 0.99 0.12
outer loop
vertex -260.1 76.2 0
vertex -260.1 74.1 17.8
vertex -126.8 74.1 17.8
endloop
endfacet
facet normal 0.00 0.99 0.12
outer loop
vertex -260.1 76.2 0
vertex -126.8 74.1 17.8
vertex -126.8 76.2 0
endloop
endfacet
facet normal -0.09 -0.99 -0.12
outer loop
vertex -126.8 85.1 0
vertex -63.4 79.2 0
vertex -63.4 77 18.5
endloop
endfacet
facet normal -0.09 -0.99 -0.12
outer loop
vertex -126.8 85.1 0
vertex -63.4 77 18.5
vertex -126.8 82.7 19.9
endloop
endfacet
facet normal 0.09 0.99 0.12
outer loop
vertex -126.8 76.2 0
vertex -126.8 74.1 17.8
vertex -63.4 68.4 16.4
endloop
endfacet
facet normal 0.09 0.99 0.12
outer loop
vertex -126.8 76.2 0
vertex -63.4 68.4 16.4
vertex -63.4 70.4 0
endloop
endfacet
facet normal -0.50 -0.86 -0.10
outer loop
vertex -63.4 79.2 0
vertex -46.5 69.5 0
vertex -46.5 67.6 16.2
endloop
endfacet
facet normal -0.50 -0.86 -0.10
outer loop
vertex -63.4 79.2 0
vertex -46.5 67.6 16.2
vertex -63.4 77 18.5
endloop
endfacet
facet normal 0.50 0.86 0.10
outer loop
vertex -63.4 70.4 0
vertex -63.4 68.4 16.4
vertex -46.5 59 14.2
endloop
endfacet
facet normal 0.50 0.86 0.10
outer loop
vertex -63.4 70.4 0
vertex -46.5 59 14.2
vertex -46.5 60.7 0
endloop
endfacet
facet normal -0.50 -0.86 -0.10
outer loop
vertex -46.5 69.5 0
vertex -31.1 60.7 0
vertex -31.1 59 14.2
endloop
endfacet
facet normal -0.50 -0.86 -0.10
outer loop
vertex -46.5 69.5 0
vertex -31.1 59 14.2
vertex -46.5 67.6 16.2
endloop
endfacet
facet normal 0.50 0.86 0.10
outer loop
vertex -46.5 60.7 0
vertex -46.5 59 14.2
vertex -31.1 50.4 12.1
endloop
endfacet
facet normal 0.50 0.86 0.10
outer loop
vertex -46.5 60.7 0
vertex -31.1 50.4 12.1
vertex -31.1 51.8 0
endloop
endfacet
facet normal -0.40 -0.91 -0.11
outer loop
vertex -31.1 60.7 0
vertex -21.2 56.4 0
vertex -21.2 54.8 13.2
endloop
endfacet
facet normal -0.40 -0.91 -0.11
outer loop
vertex -31.1 60.7 0
vertex -21.2 54.8 13.2
vertex -31.1 59 14.2
endloop
endfacet
facet normal 0.40 0.91 0.11
outer loop
vertex -31.1 51.8 0
vertex -31.1 50.4 12.1
vertex -21.2 46.2 11.1
endloop
endfacet
facet normal 0.40 0.91 0.11
outer loop
vertex -31.1 51.8 0
vertex -21.2 46.2 11.1
vertex -21.2 47.5 0
endloop
endfacet
facet normal -0.24 -0.96 -0.11
outer loop
vertex -21.2 56.4 0
vertex -10.8 53.7 0
vertex -10.8 52.3 12.5
endloop
endfacet
facet normal -0.24 -0.96 -0.11
outer loop
vertex -21.2 56.4 0
vertex -10.8 52.3 12.5
vertex -21.2 54.8 13.2
endloop
endfacet
facet normal 0.24 0.96 0.11
outer loop
vertex -21.2 47.5 0
vertex -21.2 46.2 11.1
vertex -10.8 43.7 10.5
endloop
endfacet
facet normal 0.24 0.96 0.11
outer loop
vertex -21.2 47.5 0
vertex -10.8 43.7 10.5
vertex -10.8 44.9 0
endloop
endfacet
facet normal -0.08 -0.99 -0.12
outer loop
vertex -10.8 53.7 0
vertex 0 52.9 0
vertex 0 51.4 12.3
endloop
endfacet
facet normal -0.08 -0.99 -0.12
outer loop
vertex -10.8 53.7 0
vertex 0 51.4 12.3
vertex -10.8 52.3 12.5
endloop
endfacet
facet normal 0.08 0.99 0.12
outer loop
vertex -10.8 44.9 0
vertex -10.8 43.7 10.5
vertex 0 42.8 10.3
endloop
endfacet
facet normal 0.08 0.99 0.12
outer loop
vertex -10.8 44.9 0
vertex 0 42.8 10.3
vertex 0 44 0
endloop
endfacet
facet normal 0.10 -0.99 -0.12
outer loop
vertex 0 52.9 0
vertex 3.3 53.2 0
vertex 3.3 51.7 12.4
endloop
endfacet
facet normal 0.10 -0.99 -0.12
outer loop
vertex 0 52.9 0
vertex 3.3 51.7 12.4
vertex 0 51.4 12.3
endloop
endfacet
facet normal -0.10 0.99 0.12
outer loop
vertex 0 44 0
vertex 0 42.8 10.3
vertex 3.3 43.1 10.4
endloop
endfacet
facet normal -0.10 0.99 0.12
outer loop
vertex 0 44 0
vertex 3.3 43.1 10.4
vertex 3.3 44.3 0
endloop
endfacet
facet normal 0.29 -0.95 -0.11
outer loop
vertex 3.3 53.2 0
vertex 6.5 54.2 0
vertex 6.5 52.7 12.6
endloop
endfacet
facet normal 0.29 -0.95 -0.11
outer loop
vertex 3.3 53.2 0
vertex 6.5 52.7 12.6
vertex 3.3 51.7 12.4
endloop
endfacet
facet normal -0.29 0.95 0.11
outer loop
vertex 3.3 44.3 0
vertex 3.3 43.1 10.4
vertex 6.5 44.1 10.6
endloop
endfacet
facet normal -0.29 0.95 0.11
outer loop
vertex 3.3 44.3 0
vertex 6.5 44.1 10.6
vertex 6.5 45.3 0
endloop
endfacet
facet normal 0.44 -0.89 -0.11
outer loop
vertex 6.5 54.2 0
vertex 30.7 66.2 0
vertex 30.7 64.4 15.5
endloop
endfacet
facet normal 0.44 -0.89 -0.11
outer loop
vertex 6.5 54.2 0
vertex 30.7 64.4 15.5
vertex 6.5 52.7 12.6
endloop
endfacet
facet normal -0.44 0.89 0.11
outer loop
vertex 6.5 45.3 0
vertex 6.5 44.1 10.6
vertex 30.7 55.8 13.4
endloop
endfacet
facet normal -0.44 0.89 0.11
outer loop
vertex 6.5 45.3 0
vertex 30.7 55.8 13.4
vertex 30.7 57.4 0
endloop
endfacet
facet normal 0.42 -0.90 -0.11
outer loop
vertex 30.7 66.2 0
vertex 69.4 84.2 0
vertex 69.4 81.9 19.7
endloop
endfacet
facet normal 0.42 -0.90 -0.11
outer loop
vertex 30.7 66.2 0
vertex 69.4 81.9 19.7
vertex 30.7 64.4 15.5
endloop
endfacet
facet normal -0.42 0.90 0.11
outer loop
vertex 30.7 57.4 0
vertex 30.7 55.8 13.4
vertex 69.4 73.3 17.6
endloop
endfacet
facet normal -0.42 0.90 0.11
outer loop
vertex 30.7 57.4 0
vertex 69.4 73.3 17.6
vertex 69.4 75.3 0
endloop
endfacet
facet normal 0.38 -0.92 -0.11
outer loop
vertex 69.4 84.2 0
vertex 108.3 100.5 0
vertex 108.3 97.8 23.5
endloop
endfacet
facet normal 0.38 -0.92 -0.11
outer loop
vertex 69.4 84.2 0
vertex 108.3 97.8 23.5
vertex 69.4 81.9 19.7
endloop
endfacet
facet normal -0.38 0.92 0.11
outer loop
vertex 69.4 75.3 0
vertex 69.4 73.3 17.6
vertex 108.3 89.2 21.4
endloop
endfacet
facet normal -0.38 0.92 0.11
outer loop
vertex 69.4 75.3 0
vertex 108.3 89.2 21.4
vertex 108.3 91.7 0
endloop
endfacet
facet normal 0.35 -0.93 -0.11
outer loop
vertex 108.3 100.5 0
vertex 147.6 115.3 0
vertex 147.6 112.1 26.9
endloop
endfacet
facet normal 0.35 -0.93 -0.11
outer loop
vertex 108.3 100.5 0
vertex 147.6 112.1 26.9
vertex 108.3 97.8 23.5
endloop
endfacet
facet normal -0.35 0.93 0.11
outer loop
vertex 108.3 91.7 0
vertex 108.3 89.2 21.4
vertex 147.6 103.5 24.8
endloop
endfacet
facet normal -0.35 0.93 0.11
outer loop
vertex 108.3 91.7 0
vertex 147.6 103.5 24.8
vertex 147.6 106.4 0
endloop
endfacet
facet normal 0.31 -0.94 -0.11
outer loop
vertex 147.6 115.3 0
vertex 187.1 128.5 0
vertex 187.1 124.9 30
endloop
endfacet
facet normal 0.31 -0.94 -0.11
outer loop
vertex 147.6 115.3 0
vertex 187.1 124.9 30
vertex 147.6 112.1 26.9
endloop
endfacet
facet normal -0.31 0.94 0.11
outer loop
vertex 147.6 106.4 0
vertex 147.6 103.5 24.8
vertex 187.1 116.3 27.9
endloop
endfacet
facet normal -0.31 0.94 0.11
outer loop
vertex 147.6 106.4 0
vertex 187.1 116.3 27.9
vertex 187.1 119.6 0
endloop
endfacet
facet normal 0.28 -0.95 -0.11
outer loop
vertex 187.1 128.5 0
vertex 227 140 0
vertex 227 136.2 32.7
endloop
endfacet
facet normal 0.28 -0.95 -0.11
outer loop
vertex 187.1 128.5 0
vertex 227 136.2 32.7
vertex 187.1 124.9 30
endloop
endfacet
facet normal -0.28 0.95 0.11
outer loop
vertex 187.1 119.6 0
vertex 187.1 116.3 27.9
vertex 227 127.6 30.6
endloop
endfacet
facet normal -0.28 0.95 0.11
outer loop
vertex 187.1 119.6 0
vertex 227 127.6 30.6
vertex 227 131.2 0
endloop
endfacet
facet normal 0.24 -0.96 -0.11
outer loop
vertex 227 140 0
vertex 267.1 150 0
vertex 267.1 145.9 35
endloop
endfacet
facet normal 0.24 -0.96 -0.11
outer loop
vertex 227 140 0
vertex 267.1 145.9 35
vertex 227 136.2 32.7
endloop
endfacet
facet normal -0.24 0.96 0.11
outer loop
vertex 227 131.2 0
vertex 227 127.6 30.6
vertex 267.1 137.3 33
endloop
endfacet
facet normal -0.24 0.96 0.11
outer loop
vertex 227 131.2 0
vertex 267.1 137.3 33
vertex 267.1 141.2 0
endloop
endfacet
facet normal 0.20 -0.97 -0.12
outer loop
vertex 267.1 150 0
vertex 307.6 158.4 0
vertex 307.6 154 37
endloop
endfacet
facet normal 0.20 -0.97 -0.12
outer loop
vertex 267.1 150 0
vertex 307.6 154 37
vertex 267.1 145.9 35
endloop
endfacet
facet normal -0.20 0.97 0.12
outer loop
vertex 267.1 141.2 0
vertex 267.1 137.3 33
vertex 307.6 145.4 34.9
endloop
endfacet
facet normal -0.20 0.97 0.12
outer loop
vertex 267.1 141.2 0
vertex 307.6 145.4 34.9
vertex 307.6 149.6 0
endloop
endfacet
facet normal 0.18 -0.98 -0.12
outer loop
vertex 307.6 158.4 0
vertex 323.8 161.3 0
vertex 323.8 156.9 37.7
endloop
endfacet
facet normal 0.18 -0.98 -0.12
outer loop
vertex 307.6 158.4 0
vertex 323.8 156.9 37.7
vertex 307.6 154 37
endloop
endfacet
facet normal -0.18 0.98 0.12
outer loop
vertex 307.6 149.6 0
vertex 307.6 145.4 34.9
vertex 323.8 148.3 35.6
endloop
endfacet
facet normal -0.18 0.98 0.12
outer loop
vertex 307.6 149.6 0
vertex 323.8 148.3 35.6
vertex 323.8 152.5 0
endloop
endfacet
facet normal 0.00 -0.94 -0.35
outer loop
vertex -393.4 82.7 19.9
vertex -260.1 82.7 19.9
vertex -260.1 75.8 38.6
endloop
endfacet
facet normal 0.00 -0.94 -0.35
outer loop
vertex -393.4 82.7 19.9
vertex -260.1 75.8 38.6
vertex -393.4 75.8 38.6
endloop
endfacet
facet normal 0.00 0.94 0.35
outer loop
vertex -393.4 74.1 17.8
vertex -393.4 67.9 34.6
vertex -260.1 67.9 34.6
endloop
endfacet
facet normal 0.00 0.94 0.35
outer loop
vertex -393.4 74.1 17.8
vertex -260.1 67.9 34.6
vertex -260.1 74.1 17.8
endloop
endfacet
facet normal 0.00 -0.94 -0.35
outer loop
vertex -260.1 82.7 19.9
vertex -126.8 82.7 19.9
vertex -126.8 75.8 38.6
endloop
endfacet
facet normal 0.00 -0.94 -0.35
outer loop
vertex -260.1 82.7 19.9
vertex -126.8 75.8 38.6
vertex -260.1 75.8 38.6
endloop
endfacet
facet normal 0.00 0.94 0.35
outer loop
vertex -260.1 74.1 17.8
vertex -260.1 67.9 34.6
vertex -126.8 67.9 34.6
endloop
endfacet
facet normal 0.00 0.94 0.35
outer loop
vertex -260.1 74.1 17.8
vertex -126.8 67.9 34.6
vertex -126.8 74.1 17.8
endloop
endfacet
facet normal -0.09 -0.93 -0.34
outer loop
vertex -126.8 82.7 19.9
vertex -63.4 77 18.5
vertex -63.4 70.6 36
endloop
endfacet
facet normal -0.09 -0.93 -0.34
outer loop
vertex -126.8 82.7 19.9
vertex -63.4 70.6 36
vertex -126.8 75.8 38.6
endloop
endfacet
facet normal 0.09 0.93 0.34
outer loop
vertex -126.8 74.1 17.8
vertex -126.8 67.9 34.6
vertex -63.4 62.7 32
endloop
endfacet
facet normal 0.09 0.93 0.34
outer loop
vertex -126.8 74.1 17.8
vertex -63.4 62.7 32
vertex -63.4 68.4 16.4
endloop
endfacet
facet normal -0.50 -0.81 -0.30
outer loop
vertex -63.4 77 18.5
vertex -46.5 67.6 16.2
vertex -46.5 61.9 31.6
endloop
endfacet
facet normal -0.50 -0.81 -0.30
outer loop
vertex -63.4 77 18.5
vertex -46.5 61.9 31.6
vertex -63.4 70.6 36
endloop
endfacet
facet normal 0.50 0.81 0.30
outer loop
vertex -63.4 68.4 16.4
vertex -63.4 62.7 32
vertex -46.5 54 27.5
endloop
endfacet
facet normal 0.50 0.81 0.30
outer loop
vertex -63.4 68.4 16.4
vertex -46.5 54 27.5
vertex -46.5 59 14.2
endloop
endfacet
facet normal -0.50 -0.81 -0.30
outer loop
vertex -46.5 67.6 16.2
vertex -31.1 59 14.2
vertex -31.1 54 27.5
endloop
endfacet
facet normal -0.50 -0.81 -0.30
outer loop
vertex -46.5 67.6 16.2
vertex -31.1 54 27.5
vertex -46.5 61.9 31.6
endloop
endfacet
facet normal 0.50 0.81 0.30
outer loop
vertex -46.5 59 14.2
vertex -46.5 54 27.5
vertex -31.1 46.2 23.5
endloop
endfacet
facet normal 0.50 0.81 0.30
outer loop
vertex -46.5 59 14.2
vertex -31.1 46.2 23.5
vertex -31.1 50.4 12.1
endloop
endfacet
facet normal -0.40 -0.86 -0.32
outer loop
vertex -31.1 59 14.2
vertex -21.2 54.8 13.2
vertex -21.2 50.2 25.6
endloop
endfacet
facet normal -0.40 -0.86 -0.32
outer loop
vertex -31.1 59 14.2
vertex -21.2 50.2 25.6
vertex -31.1 54 27.5
endloop
endfacet
facet normal 0.40 0.86 0.32
outer loop
vertex -31.1 50.4 12.1
vertex -31.1 46.2 23.5
vertex -21.2 42.3 21.6
endloop
endfacet
facet normal 0.40 0.86 0.32
outer loop
vertex -31.1 50.4 12.1
vertex -21.2 42.3 21.6
vertex -21.2 46.2 11.1
endloop
endfacet
facet normal -0.24 -0.91 -0.34
outer loop
vertex -21.2 54.8 13.2
vertex -10.8 52.3 12.5
vertex -10.8 47.9 24.4
endloop
endfacet
facet normal -0.24 -0.91 -0.34
outer loop
vertex -21.2 54.8 13.2
vertex -10.8 47.9 24.4
vertex -21.2 50.2 25.6
endloop
endfacet
facet normal 0.24 0.91 0.34
outer loop
vertex -21.2 46.2 11.1
vertex -21.2 42.3 21.6
vertex -10.8 40 20.4
endloop
endfacet
facet normal 0.24 0.91 0.34
outer loop
vertex -21.2 46.2 11.1
vertex -10.8 40 20.4
vertex -10.8 43.7 10.5
endloop
endfacet
facet normal -0.08 -0.94 -0.34
outer loop
vertex -10.8 52.3 12.5
vertex 0 51.4 12.3
vertex 0 47.1 24
endloop
endfacet
facet normal -0.08 -0.94 -0.34
outer loop
vertex -10.8 52.3 12.5
vertex 0 47.1 24
vertex -10.8 47.9 24.4
endloop
endfacet
facet normal 0.08 0.94 0.34
outer loop
vertex -10.8 43.7 10.5
vertex -10.8 40 20.4
vertex 0 39.2 20
endloop
endfacet
facet normal 0.08 0.94 0.34
outer loop
vertex -10.8 43.7 10.5
vertex 0 39.2 20
vertex 0 42.8 10.3
endloop
endfacet
facet normal 0.10 -0.93 -0.34
outer loop
vertex 0 51.4 12.3
vertex 3.3 51.7 12.4
vertex 3.3 47.4 24.1
endloop
endfacet
facet normal 0.10 -0.93 -0.34
outer loop
vertex 0 51.4 12.3
vertex 3.3 47.4 24.1
vertex 0 47.1 24
endloop
endfacet
facet normal -0.10 0.93 0.34
outer loop
vertex 0 42.8 10.3
vertex 0 39.2 20
vertex 3.3 39.5 20.1
endloop
endfacet
facet normal -0.10 0.93 0.34
outer loop
vertex 0 42.8 10.3
vertex 3.3 39.5 20.1
vertex 3.3 43.1 10.4
endloop
endfacet
facet normal 0.29 -0.90 -0.33
outer loop
vertex 3.3 51.7 12.4
vertex 6.5 52.7 12.6
vertex 6.5 48.3 24.6
endloop
endfacet
facet normal 0.29 -0.90 -0.33
outer loop
vertex 3.3 51.7 12.4
vertex 6.5 48.3 24.6
vertex 3.3 47.4 24.1
endloop
endfacet
facet normal -0.29 0.90 0.33
outer loop
vertex 3.3 43.1 10.4
vertex 3.3 39.5 20.1
vertex 6.5 40.4 20.6
endloop
endfacet
facet normal -0.29 0.90 0.33
outer loop
vertex 3.3 43.1 10.4
vertex 6.5 40.4 20.6
vertex 6.5 44.1 10.6
endloop
endfacet
facet normal 0.44 -0.84 -0.31
outer loop
vertex 6.5 52.7 12.6
vertex 30.7 64.4 15.5
vertex 30.7 59 30.1
endloop
endfacet
facet normal 0.44 -0.84 -0.31
outer loop
vertex 6.5 52.7 12.6
vertex 30.7 59 30.1
vertex 6.5 48.3 24.6
endloop
endfacet
facet normal -0.44 0.84 0.31
outer loop
vertex 6.5 44.1 10.6
vertex 6.5 40.4 20.6
vertex 30.7 51.1 26.1
endloop
endfacet
facet normal -0.44 0.84 0.31
outer loop
vertex 6.5 44.1 10.6
vertex 30.7 51.1 26.1
vertex 30.7 55.8 13.4
endloop
endfacet
facet normal 0.42 -0.85 -0.31
outer loop
vertex 30.7 64.4 15.5
vertex 69.4 81.9 19.7
vertex 69.4 75 38.2
endloop
endfacet
facet normal 0.42 -0.85 -0.31
outer loop
vertex 30.7 64.4 15.5
vertex 69.4 75 38.2
vertex 30.7 59 30.1
endloop
endfacet
facet normal -0.42 0.85 0.31
outer loop
vertex 30.7 55.8 13.4
vertex 30.7 51.1 26.1
vertex 69.4 67.1 34.2
endloop
endfacet
facet normal -0.42 0.85 0.31
outer loop
vertex 30.7 55.8 13.4
vertex 69.4 67.1 34.2
vertex 69.4 73.3 17.6
endloop
endfacet
facet normal 0.38 -0.87 -0.32
outer loop
vertex 69.4 81.9 19.7
vertex 108.3 97.8 23.5
vertex 108.3 89.6 45.6
endloop
endfacet
facet normal 0.38 -0.87 -0.32
outer loop
vertex 69.4 81.9 19.7
vertex 108.3 89.6 45.6
vertex 69.4 75 38.2
endloop
endfacet
facet normal -0.38 0.87 0.32
outer loop
vertex 69.4 73.3 17.6
vertex 69.4 67.1 34.2
vertex 108.3 81.7 41.6
endloop
endfacet
facet normal -0.38 0.87 0.32
outer loop
vertex 69.4 73.3 17.6
vertex 108.3 81.7 41.6
vertex 108.3 89.2 21.4
endloop
endfacet
facet normal 0.35 -0.88 -0.32
outer loop
vertex 108.3 97.8 23.5
vertex 147.6 112.1 26.9
vertex 147.6 102.7 52.3
endloop
endfacet
facet normal 0.35 -0.88 -0.32
outer loop
vertex 108.3 97.8 23.5
vertex 147.6 102.7 52.3
vertex 108.3 89.6 45.6
endloop
endfacet
facet normal -0.35 0.88 0.32
outer loop
vertex 108.3 89.2 21.4
vertex 108.3 81.7 41.6
vertex 147.6 94.8 48.3
endloop
endfacet
facet normal -0.35 0.88 0.32
outer loop
vertex 108.3 89.2 21.4
vertex 147.6 94.8 48.3
vertex 147.6 103.5 24.8
endloop
endfacet
facet normal 0.31 -0.89 -0.33
outer loop
vertex 147.6 112.1 26.9
vertex 187.1 124.9 30
vertex 187.1 114.5 58.3
endloop
endfacet
facet normal 0.31 -0.89 -0.33
outer loop
vertex 147.6 112.1 26.9
vertex 187.1 114.5 58.3
vertex 147.6 102.7 52.3
endloop
endfacet
facet normal -0.31 0.89 0.33
outer loop
vertex 147.6 103.5 24.8
vertex 147.6 94.8 48.3
vertex 187.1 106.6 54.3
endloop
endfacet
facet normal -0.31 0.89 0.33
outer loop
vertex 147.6 103.5 24.8
vertex 187.1 106.6 54.3
vertex 187.1 116.3 27.9
endloop
endfacet
facet normal 0.28 -0.90 -0.33
outer loop
vertex 187.1 124.9 30
vertex 227 136.2 32.7
vertex 227 124.8 63.6
endloop
endfacet
facet normal 0.28 -0.90 -0.33
outer loop
vertex 187.1 124.9 30
vertex 227 124.8 63.6
vertex 187.1 114.5 58.3
endloop
endfacet
facet normal -0.28 0.90 0.33
outer loop
vertex 187.1 116.3 27.9
vertex 187.1 106.6 54.3
vertex 227 116.9 59.6
endloop
endfacet
facet normal -0.28 0.90 0.33
outer loop
vertex 187.1 116.3 27.9
vertex 227 116.9 59.6
vertex 227 127.6 30.6
endloop
endfacet
facet normal 0.24 -0.91 -0.34
outer loop
vertex 227 136.2 32.7
vertex 267.1 145.9 35
vertex 267.1 133.7 68.1
endloop
endfacet
facet normal 0.24 -0.91 -0.34
outer loop
vertex 227 136.2 32.7
vertex 267.1 133.7 68.1
vertex 227 124.8 63.6
endloop
endfacet
facet normal -0.24 0.91 0.34
outer loop
vertex 227 127.6 30.6
vertex 227 116.9 59.6
vertex 267.1 125.8 64.1
endloop
endfacet
facet normal -0.24 0.91 0.34
outer loop
vertex 227 127.6 30.6
vertex 267.1 125.8 64.1
vertex 267.1 137.3 33
endloop
endfacet
facet normal 0.20 -0.92 -0.34
outer loop
vertex 267.1 145.9 35
vertex 307.6 154 37
vertex 307.6 141.1 71.9
endloop
endfacet
facet normal 0.20 -0.92 -0.34
outer loop
vertex 267.1 145.9 35
vertex 307.6 141.1 71.9
vertex 267.1 133.7 68.1
endloop
endfacet
facet normal -0.20 0.92 0.34
outer loop
vertex 267.1 137.3 33
vertex 267.1 125.8 64.1
vertex 307.6 133.3 67.9
endloop
endfacet
facet normal -0.20 0.92 0.34
outer loop
vertex 267.1 137.3 33
vertex 307.6 133.3 67.9
vertex 307.6 145.4 34.9
endloop
endfacet
facet normal 0.18 -0.92 -0.34
outer loop
vertex 307.6 154 37
vertex 323.8 156.9 37.7
vertex 323.8 143.7 73.2
endloop
endfacet
facet normal 0.18 -0.92 -0.34
outer loop
vertex 307.6 154 37
vertex 323.8 143.7 73.2
vertex 307.6 141.1 71.9
endloop
endfacet
facet normal -0.18 0.92 0.34
outer loop
vertex 307.6 145.4 34.9
vertex 307.6 133.3 67.9
vertex 323.8 135.9 69.2
endloop
endfacet
facet normal -0.18 0.92 0.34
outer loop
vertex 307.6 145.4 34.9
vertex 323.8 135.9 69.2
vertex 323.8 148.3 35.6
endloop
endfacet
facet normal 0.00 -0.83 -0.56
outer loop
vertex -393.4 75.8 38.6
vertex -260.1 75.8 38.6
vertex -260.1 64.7 55.3
endloop
endfacet
facet normal 0.00 -0.83 -0.56
outer loop
vertex -393.4 75.8 38.6
vertex -260.1 64.7 55.3
vertex -393.4 64.7 55.3
endloop
endfacet
facet normal 0.00 0.83 0.56
outer loop
vertex -393.4 67.9 34.6
vertex -393.4 58 49.5
vertex -260.1 58 49.5
endloop
endfacet
facet normal 0.00 0.83 0.56
outer loop
vertex -393.4 67.9 34.6
vertex -260.1 58 49.5
vertex -260.1 67.9 34.6
endloop
endfacet
facet normal 0.00 -0.83 -0.56
outer loop
vertex -260.1 75.8 38.6
vertex -126.8 75.8 38.6
vertex -126.8 64.7 55.3
endloop
endfacet
facet normal 0.00 -0.83 -0.56
outer loop
vertex -260.1 75.8 38.6
vertex -126.8 64.7 55.3
vertex -260.1 64.7 55.3
endloop
endfacet
facet normal 0.00 0.83 0.56
outer loop
vertex -260.1 67.9 34.6
vertex -260.1 58 49.5
vertex -126.8 58 49.5
endloop
endfacet
facet normal 0.00 0.83 0.56
outer loop
vertex -260.1 67.9 34.6
vertex -126.8 58 49.5
vertex -126.8 67.9 34.6
endloop
endfacet
facet normal -0.09 -0.83 -0.55
outer loop
vertex -126.8 75.8 38.6
vertex -63.4 70.6 36
vertex -63.4 60.3 51.5
endloop
endfacet
facet normal -0.09 -0.83 -0.55
outer loop
vertex -126.8 75.8 38.6
vertex -63.4 60.3 51.5
vertex -126.8 64.7 55.3
endloop
endfacet
facet normal 0.09 0.83 0.55
outer loop
vertex -126.8 67.9 34.6
vertex -126.8 58 49.5
vertex -63.4 53.5 45.7
endloop
endfacet
facet normal 0.09 0.83 0.55
outer loop
vertex -126.8 67.9 34.6
vertex -63.4 53.5 45.7
vertex -63.4 62.7 32
endloop
endfacet
facet normal -0.50 -0.72 -0.48
outer loop
vertex -63.4 70.6 36
vertex -46.5 61.9 31.6
vertex -46.5 52.8 45.1
endloop
endfacet
facet normal -0.50 -0.72 -0.48
outer loop
vertex -63.4 70.6 36
vertex -46.5 52.8 45.1
vertex -63.4 60.3 51.5
endloop
endfacet
facet normal 0.50 0.72 0.48
outer loop
vertex -63.4 62.7 32
vertex -63.4 53.5 45.7
vertex -46.5 46.1 39.4
endloop
endfacet
facet normal 0.50 0.72 0.48
outer loop
vertex -63.4 62.7 32
vertex -46.5 46.1 39.4
vertex -46.5 54 27.5
endloop
endfacet
facet normal -0.50 -0.72 -0.48
outer loop
vertex -46.5 61.9 31.6
vertex -31.1 54 27.5
vertex -31.1 46.1 39.4
endloop
endfacet
facet normal -0.50 -0.72 -0.48
outer loop
vertex -46.5 61.9 31.6
vertex -31.1 46.1 39.4
vertex -46.5 52.8 45.1
endloop
endfacet
facet normal 0.50 0.72 0.48
outer loop
vertex -46.5 54 27.5
vertex -46.5 46.1 39.4
vertex -31.1 39.4 33.6
endloop
endfacet
facet normal 0.50 0.72 0.48
outer loop
vertex -46.5 54 27.5
vertex -31.1 39.4 33.6
vertex -31.1 46.2 23.5
endloop
endfacet
facet normal -0.40 -0.76 -0.51
outer loop
vertex -31.1 54 27.5
vertex -21.2 50.2 25.6
vertex -21.2 42.9 36.6
endloop
endfacet
facet normal -0.40 -0.76 -0.51
outer loop
vertex -31.1 54 27.5
vertex -21.2 42.9 36.6
vertex -31.1 46.1 39.4
endloop
endfacet
facet normal 0.40 0.76 0.51
outer loop
vertex -31.1 46.2 23.5
vertex -31.1 39.4 33.6
vertex -21.2 36.1 30.9
endloop
endfacet
facet normal 0.40 0.76 0.51
outer loop
vertex -31.1 46.2 23.5
vertex -21.2 36.1 30.9
vertex -21.2 42.3 21.6
endloop
endfacet
facet normal -0.24 -0.81 -0.54
outer loop
vertex -21.2 50.2 25.6
vertex -10.8 47.9 24.4
vertex -10.8 40.9 34.9
endloop
endfacet
facet normal -0.24 -0.81 -0.54
outer loop
vertex -21.2 50.2 25.6
vertex -10.8 40.9 34.9
vertex -21.2 42.9 36.6
endloop
endfacet
facet normal 0.24 0.81 0.54
outer loop
vertex -21.2 42.3 21.6
vertex -21.2 36.1 30.9
vertex -10.8 34.1 29.2
endloop
endfacet
facet normal 0.24 0.81 0.54
outer loop
vertex -21.2 42.3 21.6
vertex -10.8 34.1 29.2
vertex -10.8 40 20.4
endloop
endfacet
facet normal -0.08 -0.83 -0.55
outer loop
vertex -10.8 47.9 24.4
vertex 0 47.1 24
vertex 0 40.2 34.3
endloop
endfacet
facet normal -0.08 -0.83 -0.55
outer loop
vertex -10.8 47.9 24.4
vertex 0 40.2 34.3
vertex -10.8 40.9 34.9
endloop
endfacet
facet normal 0.08 0.83 0.55
outer loop
vertex -10.8 40 20.4
vertex -10.8 34.1 29.2
vertex 0 33.5 28.6
endloop
endfacet
facet normal 0.08 0.83 0.55
outer loop
vertex -10.8 40 20.4
vertex 0 33.5 28.6
vertex 0 39.2 20
endloop
endfacet
facet normal 0.10 -0.83 -0.55
outer loop
vertex 0 47.1 24
vertex 3.3 47.4 24.1
vertex 3.3 40.4 34.5
endloop
endfacet
facet normal 0.10 -0.83 -0.55
outer loop
vertex 0 47.1 24
vertex 3.3 40.4 34.5
vertex 0 40.2 34.3
endloop
endfacet
facet normal -0.10 0.83 0.55
outer loop
vertex 0 39.2 20
vertex 0 33.5 28.6
vertex 3.3 33.7 28.8
endloop
endfacet
facet normal -0.10 0.83 0.55
outer loop
vertex 0 39.2 20
vertex 3.3 33.7 28.8
vertex 3.3 39.5 20.1
endloop
endfacet
facet normal 0.29 -0.80 -0.53
outer loop
vertex 3.3 47.4 24.1
vertex 6.5 48.3 24.6
vertex 6.5 41.2 35.2
endloop
endfacet
facet normal 0.29 -0.80 -0.53
outer loop
vertex 3.3 47.4 24.1
vertex 6.5 41.2 35.2
vertex 3.3 40.4 34.5
endloop
endfacet
facet normal -0.29 0.80 0.53
outer loop
vertex 3.3 39.5 20.1
vertex 3.3 33.7 28.8
vertex 6.5 34.5 29.4
endloop
endfacet
facet normal -0.29 0.80 0.53
outer loop
vertex 3.3 39.5 20.1
vertex 6.5 34.5 29.4
vertex 6.5 40.4 20.6
endloop
endfacet
facet normal 0.44 -0.75 -0.50
outer loop
vertex 6.5 48.3 24.6
vertex 30.7 59 30.1
vertex 30.7 50.4 43
endloop
endfacet
facet normal 0.44 -0.75 -0.50
outer loop
vertex 6.5 48.3 24.6
vertex 30.7 50.4 43
vertex 6.5 41.2 35.2
endloop
endfacet
facet normal -0.44 0.75 0.50
outer loop
vertex 6.5 40.4 20.6
vertex 6.5 34.5 29.4
vertex 30.7 43.6 37.3
endloop
endfacet
facet normal -0.44 0.75 0.50
outer loop
vertex 6.5 40.4 20.6
vertex 30.7 43.6 37.3
vertex 30.7 51.1 26.1
endloop
endfacet
facet normal 0.42 -0.76 -0.50
outer loop
vertex 30.7 59 30.1
vertex 69.4 75 38.2
vertex 69.4 64 54.7
endloop
endfacet
facet normal 0.42 -0.76 -0.50
outer loop
vertex 30.7 59 30.1
vertex 69.4 64 54.7
vertex 30.7 50.4 43
endloop
endfacet
facet normal -0.42 0.76 0.50
outer loop
vertex 30.7 51.1 26.1
vertex 30.7 43.6 37.3
vertex 69.4 57.3 48.9
endloop
endfacet
facet normal -0.42 0.76 0.50
outer loop
vertex 30.7 51.1 26.1
vertex 69.4 57.3 48.9
vertex 69.4 67.1 34.2
endloop
endfacet
facet normal 0.38 -0.77 -0.51
outer loop
vertex 69.4 75 38.2
vertex 108.3 89.6 45.6
vertex 108.3 76.4 65.3
endloop
endfacet
facet normal 0.38 -0.77 -0.51
outer loop
vertex 69.4 75 38.2
vertex 108.3 76.4 65.3
vertex 69.4 64 54.7
endloop
endfacet
facet normal -0.38 0.77 0.51
outer loop
vertex 69.4 67.1 34.2
vertex 69.4 57.3 48.9
vertex 108.3 69.7 59.5
endloop
endfacet
facet normal -0.38 0.77 0.51
outer loop
vertex 69.4 67.1 34.2
vertex 108.3 69.7 59.5
vertex 108.3 81.7 41.6
endloop
endfacet
facet normal 0.35 -0.78 -0.52
outer loop
vertex 108.3 89.6 45.6
vertex 147.6 102.7 52.3
vertex 147.6 87.7 74.9
endloop
endfacet
facet normal 0.35 -0.78 -0.52
outer loop
vertex 108.3 89.6 45.6
vertex 147.6 87.7 74.9
vertex 108.3 76.4 65.3
endloop
endfacet
facet normal -0.35 0.78 0.52
outer loop
vertex 108.3 81.7 41.6
vertex 108.3 69.7 59.5
vertex 147.6 80.9 69.1
endloop
endfacet
facet normal -0.35 0.78 0.52
outer loop
vertex 108.3 81.7 41.6
vertex 147.6 80.9 69.1
vertex 147.6 94.8 48.3
endloop
endfacet
facet normal 0.31 -0.79 -0.53
outer loop
vertex 147.6 102.7 52.3
vertex 187.1 114.5 58.3
vertex 187.1 97.7 83.4
endloop
endfacet
facet normal 0.31 -0.79 -0.53
outer loop
vertex 147.6 102.7 52.3
vertex 187.1 97.7 83.4
vertex 147.6 87.7 74.9
endloop
endfacet
facet normal -0.31 0.79 0.53
outer loop
vertex 147.6 94.8 48.3
vertex 147.6 80.9 69.1
vertex 187.1 91 77.7
endloop
endfacet
facet normal -0.31 0.79 0.53
outer loop
vertex 147.6 94.8 48.3
vertex 187.1 91 77.7
vertex 187.1 106.6 54.3
endloop
endfacet
facet normal 0.28 -0.80 -0.53
outer loop
vertex 187.1 114.5 58.3
vertex 227 124.8 63.6
vertex 227 106.5 90.9
endloop
endfacet
facet normal 0.28 -0.80 -0.53
outer loop
vertex 187.1 114.5 58.3
vertex 227 106.5 90.9
vertex 187.1 97.7 83.4
endloop
endfacet
facet normal -0.28 0.80 0.53
outer loop
vertex 187.1 106.6 54.3
vertex 187.1 91 77.7
vertex 227 99.8 85.2
endloop
endfacet
facet normal -0.28 0.80 0.53
outer loop
vertex 187.1 106.6 54.3
vertex 227 99.8 85.2
vertex 227 116.9 59.6
endloop
endfacet
facet normal 0.24 -0.81 -0.54
outer loop
vertex 227 124.8 63.6
vertex 267.1 133.7 68.1
vertex 267.1 114.1 97.4
endloop
endfacet
facet normal 0.24 -0.81 -0.54
outer loop
vertex 227 124.8 63.6
vertex 267.1 114.1 97.4
vertex 227 106.5 90.9
endloop
endfacet
facet normal -0.24 0.81 0.54
outer loop
vertex 227 116.9 59.6
vertex 227 99.8 85.2
vertex 267.1 107.3 91.7
endloop
endfacet
facet normal -0.24 0.81 0.54
outer loop
vertex 227 116.9 59.6
vertex 267.1 107.3 91.7
vertex 267.1 125.8 64.1
endloop
endfacet
facet normal 0.20 -0.81 -0.54
outer loop
vertex 267.1 133.7 68.1
vertex 307.6 141.1 71.9
vertex 307.6 120.5 102.9
endloop
endfacet
facet normal 0.20 -0.81 -0.54
outer loop
vertex 267.1 133.7 68.1
vertex 307.6 120.5 102.9
vertex 267.1 114.1 97.4
endloop
endfacet
facet normal -0.20 0.81 0.54
outer loop
vertex 267.1 125.8 64.1
vertex 267.1 107.3 91.7
vertex 307.6 113.7 97.1
endloop
endfacet
facet normal -0.20 0.81 0.54
outer loop
vertex 267.1 125.8 64.1
vertex 307.6 113.7 97.1
vertex 307.6 133.3 67.9
endloop
endfacet
facet normal 0.18 -0.82 -0.55
outer loop
vertex 307.6 141.1 71.9
vertex 323.8 143.7 73.2
vertex 323.8 122.7 104.8
endloop
endfacet
facet normal 0.18 -0.82 -0.55
outer loop
vertex 307.6 141.1 71.9
vertex 323.8 122.7 104.8
vertex 307.6 120.5 102.9
endloop
endfacet
facet normal -0.18 0.82 0.55
outer loop
vertex 307.6 133.3 67.9
vertex 307.6 113.7 97.1
vertex 323.8 115.9 99
endloop
endfacet
facet normal -0.18 0.82 0.55
outer loop
vertex 307.6 133.3 67.9
vertex 323.8 115.9 99
vertex 323.8 135.9 69.2
endloop
endfacet
facet normal 0.00 -0.68 -0.73
outer loop
vertex -393.4 64.7 55.3
vertex -260.1 64.7 55.3
vertex -260.1 50 68.8
endloop
endfacet
facet normal 0.00 -0.68 -0.73
outer loop
vertex -393.4 64.7 55.3
vertex -260.1 50 68.8
vertex -393.4 50 68.8
endloop
endfacet
facet normal 0.00 0.68 0.73
outer loop
vertex -393.4 58 49.5
vertex -393.4 44.8 61.7
vertex -260.1 44.8 61.7
endloop
endfacet
facet normal 0.00 0.68 0.73
outer loop
vertex -393.4 58 49.5
vertex -260.1 44.8 61.7
vertex -260.1 58 49.5
endloop
endfacet
facet normal 0.00 -0.68 -0.73
outer loop
vertex -260.1 64.7 55.3
vertex -126.8 64.7 55.3
vertex -126.8 50 68.8
endloop
endfacet
facet normal 0.00 -0.68 -0.73
outer loop
vertex -260.1 64.7 55.3
vertex -126.8 50 68.8
vertex -260.1 50 68.8
endloop
endfacet
facet normal 0.00 0.68 0.73
outer loop
vertex -260.1 58 49.5
vertex -260.1 44.8 61.7
vertex -126.8 44.8 61.7
endloop
endfacet
facet normal 0.00 0.68 0.73
outer loop
vertex -260.1 58 49.5
vertex -126.8 44.8 61.7
vertex -126.8 58 49.5
endloop
endfacet
facet normal -0.09 -0.68 -0.73
outer loop
vertex -126.8 64.7 55.3
vertex -63.4 60.3 51.5
vertex -63.4 46.6 64.1
endloop
endfacet
facet normal -0.09 -0.68 -0.73
outer loop
vertex -126.8 64.7 55.3
vertex -63.4 46.6 64.1
vertex -126.8 50 68.8
endloop
endfacet
facet normal 0.09 0.68 0.73
outer loop
vertex -126.8 58 49.5
vertex -126.8 44.8 61.7
vertex -63.4 41.4 57
endloop
endfacet
facet normal 0.09 0.68 0.73
outer loop
vertex -126.8 58 49.5
vertex -63.4 41.4 57
vertex -63.4 53.5 45.7
endloop
endfacet
facet normal -0.50 -0.59 -0.64
outer loop
vertex -63.4 60.3 51.5
vertex -46.5 52.8 45.1
vertex -46.5 40.8 56.2
endloop
endfacet
facet normal -0.50 -0.59 -0.64
outer loop
vertex -63.4 60.3 51.5
vertex -46.5 40.8 56.2
vertex -63.4 46.6 64.1
endloop
endfacet
facet normal 0.50 0.59 0.64
outer loop
vertex -63.4 53.5 45.7
vertex -63.4 41.4 57
vertex -46.5 35.7 49.1
endloop
endfacet
facet normal 0.50 0.59 0.64
outer loop
vertex -63.4 53.5 45.7
vertex -46.5 35.7 49.1
vertex -46.5 46.1 39.4
endloop
endfacet
facet normal -0.50 -0.59 -0.64
outer loop
vertex -46.5 52.8 45.1
vertex -31.1 46.1 39.4
vertex -31.1 35.7 49.1
endloop
endfacet
facet normal -0.50 -0.59 -0.64
outer loop
vertex -46.5 52.8 45.1
vertex -31.1 35.7 49.1
vertex -46.5 40.8 56.2
endloop
endfacet
facet normal 0.50 0.59 0.64
outer loop
vertex -46.5 46.1 39.4
vertex -46.5 35.7 49.1
vertex -31.1 30.5 41.9
endloop
endfacet
facet normal 0.50 0.59 0.64
outer loop
vertex -46.5 46.1 39.4
vertex -31.1 30.5 41.9
vertex -31.1 39.4 33.6
endloop
endfacet
facet normal -0.40 -0.62 -0.67
outer loop
vertex -31.1 46.1 39.4
vertex -21.2 42.9 36.6
vertex -21.2 33.1 45.6
endloop
endfacet
facet normal -0.40 -0.62 -0.67
outer loop
vertex -31.1 46.1 39.4
vertex -21.2 33.1 45.6
vertex -31.1 35.7 49.1
endloop
endfacet
facet normal 0.40 0.62 0.67
outer loop
vertex -31.1 39.4 33.6
vertex -31.1 30.5 41.9
vertex -21.2 27.9 38.4
endloop
endfacet
facet normal 0.40 0.62 0.67
outer loop
vertex -31.1 39.4 33.6
vertex -21.2 27.9 38.4
vertex -21.2 36.1 30.9
endloop
endfacet
facet normal -0.24 -0.66 -0.71
outer loop
vertex -21.2 42.9 36.6
vertex -10.8 40.9 34.9
vertex -10.8 31.6 43.5
endloop
endfacet
facet normal -0.24 -0.66 -0.71
outer loop
vertex -21.2 42.9 36.6
vertex -10.8 31.6 43.5
vertex -21.2 33.1 45.6
endloop
endfacet
facet normal 0.24 0.66 0.71
outer loop
vertex -21.2 36.1 30.9
vertex -21.2 27.9 38.4
vertex -10.8 26.4 36.3
endloop
endfacet
facet normal 0.24 0.66 0.71
outer loop
vertex -21.2 36.1 30.9
vertex -10.8 26.4 36.3
vertex -10.8 34.1 29.2
endloop
endfacet
facet normal -0.08 -0.68 -0.73
outer loop
vertex -10.8 40.9 34.9
vertex 0 40.2 34.3
vertex 0 31.1 42.8
endloop
endfacet
facet normal -0.08 -0.68 -0.73
outer loop
vertex -10.8 40.9 34.9
vertex 0 31.1 42.8
vertex -10.8 31.6 43.5
endloop
endfacet
facet normal 0.08 0.68 0.73
outer loop
vertex -10.8 34.1 29.2
vertex -10.8 26.4 36.3
vertex 0 25.9 35.6
endloop
endfacet
facet normal 0.08 0.68 0.73
outer loop
vertex -10.8 34.1 29.2
vertex 0 25.9 35.6
vertex 0 33.5 28.6
endloop
endfacet
facet normal 0.10 -0.68 -0.73
outer loop
vertex 0 40.2 34.3
vertex 3.3 40.4 34.5
vertex 3.3 31.3 43
endloop
endfacet
facet normal 0.10 -0.68 -0.73
outer loop
vertex 0 40.2 34.3
vertex 3.3 31.3 43
vertex 0 31.1 42.8
endloop
endfacet
facet normal -0.10 0.68 0.73
outer loop
vertex 0 33.5 28.6
vertex 0 25.9 35.6
vertex 3.3 26.1 35.9
endloop
endfacet
facet normal -0.10 0.68 0.73
outer loop
vertex 0 33.5 28.6
vertex 3.3 26.1 35.9
vertex 3.3 33.7 28.8
endloop
endfacet
facet normal 0.29 -0.65 -0.70
outer loop
vertex 3.3 40.4 34.5
vertex 6.5 41.2 35.2
vertex 6.5 31.8 43.8
endloop
endfacet
facet normal 0.29 -0.65 -0.70
outer loop
vertex 3.3 40.4 34.5
vertex 6.5 31.8 43.8
vertex 3.3 31.3 43
endloop
endfacet
facet normal -0.29 0.65 0.70
outer loop
vertex 3.3 33.7 28.8
vertex 3.3 26.1 35.9
vertex 6.5 26.6 36.7
endloop
endfacet
facet normal -0.29 0.65 0.70
outer loop
vertex 3.3 33.7 28.8
vertex 6.5 26.6 36.7
vertex 6.5 34.5 29.4
endloop
endfacet
facet normal 0.44 -0.61 -0.66
outer loop
vertex 6.5 41.2 35.2
vertex 30.7 50.4 43
vertex 30.7 38.9 53.6
endloop
endfacet
facet normal 0.44 -0.61 -0.66
outer loop
vertex 6.5 41.2 35.2
vertex 30.7 38.9 53.6
vertex 6.5 31.8 43.8
endloop
endfacet
facet normal -0.44 0.61 0.66
outer loop
vertex 6.5 34.5 29.4
vertex 6.5 26.6 36.7
vertex 30.7 33.7 46.4
endloop
endfacet
facet normal -0.44 0.61 0.66
outer loop
vertex 6.5 34.5 29.4
vertex 30.7 33.7 46.4
vertex 30.7 43.6 37.3
endloop
endfacet
facet normal 0.42 -0.62 -0.67
outer loop
vertex 30.7 50.4 43
vertex 69.4 64 54.7
vertex 69.4 49.5 68.1
endloop
endfacet
facet normal 0.42 -0.62 -0.67
outer loop
vertex 30.7 50.4 43
vertex 69.4 49.5 68.1
vertex 30.7 38.9 53.6
endloop
endfacet
facet normal -0.42 0.62 0.67
outer loop
vertex 30.7 43.6 37.3
vertex 30.7 33.7 46.4
vertex 69.4 44.3 61
endloop
endfacet
facet normal -0.42 0.62 0.67
outer loop
vertex 30.7 43.6 37.3
vertex 69.4 44.3 61
vertex 69.4 57.3 48.9
endloop
endfacet
facet normal 0.38 -0.63 -0.68
outer loop
vertex 69.4 64 54.7
vertex 108.3 76.4 65.3
vertex 108.3 59.1 81.3
endloop
endfacet
facet normal 0.38 -0.63 -0.68
outer loop
vertex 69.4 64 54.7
vertex 108.3 59.1 81.3
vertex 69.4 49.5 68.1
endloop
endfacet
facet normal -0.38 0.63 0.68
outer loop
vertex 69.4 57.3 48.9
vertex 69.4 44.3 61
vertex 108.3 53.9 74.2
endloop
endfacet
facet normal -0.38 0.63 0.68
outer loop
vertex 69.4 57.3 48.9
vertex 108.3 53.9 74.2
vertex 108.3 69.7 59.5
endloop
endfacet
facet normal 0.35 -0.64 -0.69
outer loop
vertex 108.3 76.4 65.3
vertex 147.6 87.7 74.9
vertex 147.6 67.8 93.3
endloop
endfacet
facet normal 0.35 -0.64 -0.69
outer loop
vertex 108.3 76.4 65.3
vertex 147.6 67.8 93.3
vertex 108.3 59.1 81.3
endloop
endfacet
facet normal -0.35 0.64 0.69
outer loop
vertex 108.3 69.7 59.5
vertex 108.3 53.9 74.2
vertex 147.6 62.6 86.1
endloop
endfacet
facet normal -0.35 0.64 0.69
outer loop
vertex 108.3 69.7 59.5
vertex 147.6 62.6 86.1
vertex 147.6 80.9 69.1
endloop
endfacet
facet normal 0.31 -0.64 -0.70
outer loop
vertex 147.6 87.7 74.9
vertex 187.1 97.7 83.4
vertex 187.1 75.5 103.9
endloop
endfacet
facet normal 0.31 -0.64 -0.70
outer loop
vertex 147.6 87.7 74.9
vertex 187.1 75.5 103.9
vertex 147.6 67.8 93.3
endloop
endfacet
facet normal -0.31 0.64 0.70
outer loop
vertex 147.6 80.9 69.1
vertex 147.6 62.6 86.1
vertex 187.1 70.3 96.8
endloop
endfacet
facet normal -0.31 0.64 0.70
outer loop
vertex 147.6 80.9 69.1
vertex 187.1 70.3 96.8
vertex 187.1 91 77.7
endloop
endfacet
facet normal 0.28 -0.65 -0.71
outer loop
vertex 187.1 97.7 83.4
vertex 227 106.5 90.9
vertex 227 82.3 113.3
endloop
endfacet
facet normal 0.28 -0.65 -0.71
outer loop
vertex 187.1 97.7 83.4
vertex 227 82.3 113.3
vertex 187.1 75.5 103.9
endloop
endfacet
facet normal -0.28 0.65 0.71
outer loop
vertex 187.1 91 77.7
vertex 187.1 70.3 96.8
vertex 227 77.1 106.1
endloop
endfacet
facet normal -0.28 0.65 0.71
outer loop
vertex 187.1 91 77.7
vertex 227 77.1 106.1
vertex 227 99.8 85.2
endloop
endfacet
facet normal 0.24 -0.66 -0.71
outer loop
vertex 227 106.5 90.9
vertex 267.1 114.1 97.4
vertex 267.1 88.2 121.4
endloop
endfacet
facet normal 0.24 -0.66 -0.71
outer loop
vertex 227 106.5 90.9
vertex 267.1 88.2 121.4
vertex 227 82.3 113.3
endloop
endfacet
facet normal -0.24 0.66 0.71
outer loop
vertex 227 99.8 85.2
vertex 227 77.1 106.1
vertex 267.1 83 114.2
endloop
endfacet
facet normal -0.24 0.66 0.71
outer loop
vertex 227 99.8 85.2
vertex 267.1 83 114.2
vertex 267.1 107.3 91.7
endloop
endfacet
facet normal 0.20 -0.66 -0.72
outer loop
vertex 267.1 114.1 97.4
vertex 307.6 120.5 102.9
vertex 307.6 93.1 128.2
endloop
endfacet
facet normal 0.20 -0.66 -0.72
outer loop
vertex 267.1 114.1 97.4
vertex 307.6 93.1 128.2
vertex 267.1 88.2 121.4
endloop
endfacet
facet normal -0.20 0.66 0.72
outer loop
vertex 267.1 107.3 91.7
vertex 267.1 83 114.2
vertex 307.6 87.9 121
endloop
endfacet
facet normal -0.20 0.66 0.72
outer loop
vertex 267.1 107.3 91.7
vertex 307.6 87.9 121
vertex 307.6 113.7 97.1
endloop
endfacet
facet normal 0.18 -0.67 -0.72
outer loop
vertex 307.6 120.5 102.9
vertex 323.8 122.7 104.8
vertex 323.8 94.8 130.5
endloop
endfacet
facet normal 0.18 -0.67 -0.72
outer loop
vertex 307.6 120.5 102.9
vertex 323.8 94.8 130.5
vertex 307.6 93.1 128.2
endloop
endfacet
facet normal -0.18 0.67 0.72
outer loop
vertex 307.6 113.7 97.1
vertex 307.6 87.9 121
vertex 323.8 89.6 123.4
endloop
endfacet
facet normal -0.18 0.67 0.72
outer loop
vertex 307.6 113.7 97.1
vertex 323.8 89.6 123.4
vertex 323.8 115.9 99
endloop
endfacet
facet normal 0.00 -0.49 -0.87
outer loop
vertex -393.4 50 68.8
vertex -260.1 50 68.8
vertex -260.1 32.6 78.6
endloop
endfacet
facet normal 0.00 -0.49 -0.87
outer loop
vertex -393.4 50 68.8
vertex -260.1 32.6 78.6
vertex -393.4 32.6 78.6
endloop
endfacet
facet normal 0.00 0.49 0.87
outer loop
vertex -393.4 44.8 61.7
vertex -393.4 29.2 70.4
vertex -260.1 29.2 70.4
endloop
endfacet
facet normal 0.00 0.49 0.87
outer loop
vertex -393.4 44.8 61.7
vertex -260.1 29.2 70.4
vertex -260.1 44.8 61.7
endloop
endfacet
facet normal 0.00 -0.49 -0.87
outer loop
vertex -260.1 50 68.8
vertex -126.8 50 68.8
vertex -126.8 32.6 78.6
endloop
endfacet
facet normal 0.00 -0.49 -0.87
outer loop
vertex -260.1 50 68.8
vertex -126.8 32.6 78.6
vertex -260.1 32.6 78.6
endloop
endfacet
facet normal 0.00 0.49 0.87
outer loop
vertex -260.1 44.8 61.7
vertex -260.1 29.2 70.4
vertex -126.8 29.2 70.4
endloop
endfacet
facet normal 0.00 0.49 0.87
outer loop
vertex -260.1 44.8 61.7
vertex -126.8 29.2 70.4
vertex -126.8 44.8 61.7
endloop
endfacet
facet normal -0.09 -0.49 -0.87
outer loop
vertex -126.8 50 68.8
vertex -63.4 46.6 64.1
vertex -63.4 30.3 73.2
endloop
endfacet
facet normal -0.09 -0.49 -0.87
outer loop
vertex -126.8 50 68.8
vertex -63.4 30.3 73.2
vertex -126.8 32.6 78.6
endloop
endfacet
facet normal 0.09 0.49 0.87
outer loop
vertex -126.8 44.8 61.7
vertex -126.8 29.2 70.4
vertex -63.4 26.9 65
endloop
endfacet
facet normal 0.09 0.49 0.87
outer loop
vertex -126.8 44.8 61.7
vertex -63.4 26.9 65
vertex -63.4 41.4 57
endloop
endfacet
facet normal -0.50 -0.42 -0.76
outer loop
vertex -63.4 46.6 64.1
vertex -46.5 40.8 56.2
vertex -46.5 26.6 64.2
endloop
endfacet
facet normal -0.50 -0.42 -0.76
outer loop
vertex -63.4 46.6 64.1
vertex -46.5 26.6 64.2
vertex -63.4 30.3 73.2
endloop
endfacet
facet normal 0.50 0.42 0.76
outer loop
vertex -63.4 41.4 57
vertex -63.4 26.9 65
vertex -46.5 23.2 56
endloop
endfacet
facet normal 0.50 0.42 0.76
outer loop
vertex -63.4 41.4 57
vertex -46.5 23.2 56
vertex -46.5 35.7 49.1
endloop
endfacet
facet normal -0.50 -0.42 -0.76
outer loop
vertex -46.5 40.8 56.2
vertex -31.1 35.7 49.1
vertex -31.1 23.2 56
endloop
endfacet
facet normal -0.50 -0.42 -0.76
outer loop
vertex -46.5 40.8 56.2
vertex -31.1 23.2 56
vertex -46.5 26.6 64.2
endloop
endfacet
facet normal 0.50 0.42 0.76
outer loop
vertex -46.5 35.7 49.1
vertex -46.5 23.2 56
vertex -31.1 19.8 47.9
endloop
endfacet
facet normal 0.50 0.42 0.76
outer loop
vertex -46.5 35.7 49.1
vertex -31.1 19.8 47.9
vertex -31.1 30.5 41.9
endloop
endfacet
facet normal -0.40 -0.45 -0.80
outer loop
vertex -31.1 35.7 49.1
vertex -21.2 33.1 45.6
vertex -21.2 21.6 52.1
endloop
endfacet
facet normal -0.40 -0.45 -0.80
outer loop
vertex -31.1 35.7 49.1
vertex -21.2 21.6 52.1
vertex -31.1 23.2 56
endloop
endfacet
facet normal 0.40 0.45 0.80
outer loop
vertex -31.1 30.5 41.9
vertex -31.1 19.8 47.9
vertex -21.2 18.2 43.9
endloop
endfacet
facet normal 0.40 0.45 0.80
outer loop
vertex -31.1 30.5 41.9
vertex -21.2 18.2 43.9
vertex -21.2 27.9 38.4
endloop
endfacet
facet normal -0.24 -0.47 -0.85
outer loop
vertex -21.2 33.1 45.6
vertex -10.8 31.6 43.5
vertex -10.8 20.6 49.7
endloop
endfacet
facet normal -0.24 -0.47 -0.85
outer loop
vertex -21.2 33.1 45.6
vertex -10.8 20.6 49.7
vertex -21.2 21.6 52.1
endloop
endfacet
facet normal 0.24 0.47 0.85
outer loop
vertex -21.2 27.9 38.4
vertex -21.2 18.2 43.9
vertex -10.8 17.2 41.5
endloop
endfacet
facet normal 0.24 0.47 0.85
outer loop
vertex -21.2 27.9 38.4
vertex -10.8 17.2 41.5
vertex -10.8 26.4 36.3
endloop
endfacet
facet normal -0.08 -0.49 -0.87
outer loop
vertex -10.8 31.6 43.5
vertex 0 31.1 42.8
vertex 0 20.2 48.8
endloop
endfacet
facet normal -0.08 -0.49 -0.87
outer loop
vertex -10.8 31.6 43.5
vertex 0 20.2 48.8
vertex -10.8 20.6 49.7
endloop
endfacet
facet normal 0.08 0.49 0.87
outer loop
vertex -10.8 26.4 36.3
vertex -10.8 17.2 41.5
vertex 0 16.8 40.7
endloop
endfacet
facet normal 0.08 0.49 0.87
outer loop
vertex -10.8 26.4 36.3
vertex 0 16.8 40.7
vertex 0 25.9 35.6
endloop
endfacet
facet normal 0.10 -0.49 -0.87
outer loop
vertex 0 31.1 42.8
vertex 3.3 31.3 43
vertex 3.3 20.4 49.1
endloop
endfacet
facet normal 0.10 -0.49 -0.87
outer loop
vertex 0 31.1 42.8
vertex 3.3 20.4 49.1
vertex 0 20.2 48.8
endloop
endfacet
facet normal -0.10 0.49 0.87
outer loop
vertex 0 25.9 35.6
vertex 0 16.8 40.7
vertex 3.3 17 41
endloop
endfacet
facet normal -0.10 0.49 0.87
outer loop
vertex 0 25.9 35.6
vertex 3.3 17 41
vertex 3.3 26.1 35.9
endloop
endfacet
facet normal 0.29 -0.47 -0.83
outer loop
vertex 3.3 31.3 43
vertex 6.5 31.8 43.8
vertex 6.5 20.7 50
endloop
endfacet
facet normal 0.29 -0.47 -0.83
outer loop
vertex 3.3 31.3 43
vertex 6.5 20.7 50
vertex 3.3 20.4 49.1
endloop
endfacet
facet normal -0.29 0.47 0.83
outer loop
vertex 3.3 26.1 35.9
vertex 3.3 17 41
vertex 6.5 17.3 41.9
endloop
endfacet
facet normal -0.29 0.47 0.83
outer loop
vertex 3.3 26.1 35.9
vertex 6.5 17.3 41.9
vertex 6.5 26.6 36.7
endloop
endfacet
facet normal 0.44 -0.44 -0.78
outer loop
vertex 6.5 31.8 43.8
vertex 30.7 38.9 53.6
vertex 30.7 25.4 61.2
endloop
endfacet
facet normal 0.44 -0.44 -0.78
outer loop
vertex 6.5 31.8 43.8
vertex 30.7 25.4 61.2
vertex 6.5 20.7 50
endloop
endfacet
facet normal -0.44 0.44 0.78
outer loop
vertex 6.5 26.6 36.7
vertex 6.5 17.3 41.9
vertex 30.7 22 53
endloop
endfacet
facet normal -0.44 0.44 0.78
outer loop
vertex 6.5 26.6 36.7
vertex 30.7 22 53
vertex 30.7 33.7 46.4
endloop
endfacet
facet normal 0.42 -0.44 -0.79
outer loop
vertex 30.7 38.9 53.6
vertex 69.4 49.5 68.1
vertex 69.4 32.2 77.8
endloop
endfacet
facet normal 0.42 -0.44 -0.79
outer loop
vertex 30.7 38.9 53.6
vertex 69.4 32.2 77.8
vertex 30.7 25.4 61.2
endloop
endfacet
facet normal -0.42 0.44 0.79
outer loop
vertex 30.7 33.7 46.4
vertex 30.7 22 53
vertex 69.4 28.8 69.6
endloop
endfacet
facet normal -0.42 0.44 0.79
outer loop
vertex 30.7 33.7 46.4
vertex 69.4 28.8 69.6
vertex 69.4 44.3 61
endloop
endfacet
facet normal 0.38 -0.45 -0.81
outer loop
vertex 69.4 49.5 68.1
vertex 108.3 59.1 81.3
vertex 108.3 38.5 92.9
endloop
endfacet
facet normal 0.38 -0.45 -0.81
outer loop
vertex 69.4 49.5 68.1
vertex 108.3 38.5 92.9
vertex 69.4 32.2 77.8
endloop
endfacet
facet normal -0.38 0.45 0.81
outer loop
vertex 69.4 44.3 61
vertex 69.4 28.8 69.6
vertex 108.3 35.1 84.7
endloop
endfacet
facet normal -0.38 0.45 0.81
outer loop
vertex 69.4 44.3 61
vertex 108.3 35.1 84.7
vertex 108.3 53.9 74.2
endloop
endfacet
facet normal 0.35 -0.46 -0.82
outer loop
vertex 108.3 59.1 81.3
vertex 147.6 67.8 93.3
vertex 147.6 44.1 106.5
endloop
endfacet
facet normal 0.35 -0.46 -0.82
outer loop
vertex 108.3 59.1 81.3
vertex 147.6 44.1 106.5
vertex 108.3 38.5 92.9
endloop
endfacet
facet normal -0.35 0.46 0.82
outer loop
vertex 108.3 53.9 74.2
vertex 108.3 35.1 84.7
vertex 147.6 40.7 98.3
endloop
endfacet
facet normal -0.35 0.46 0.82
outer loop
vertex 108.3 53.9 74.2
vertex 147.6 40.7 98.3
vertex 147.6 62.6 86.1
endloop
endfacet
facet normal 0.31 -0.46 -0.83
outer loop
vertex 147.6 67.8 93.3
vertex 187.1 75.5 103.9
vertex 187.1 49.2 118.7
endloop
endfacet
facet normal 0.31 -0.46 -0.83
outer loop
vertex 147.6 67.8 93.3
vertex 187.1 49.2 118.7
vertex 147.6 44.1 106.5
endloop
endfacet
facet normal -0.31 0.46 0.83
outer loop
vertex 147.6 62.6 86.1
vertex 147.6 40.7 98.3
vertex 187.1 45.8 110.5
endloop
endfacet
facet normal -0.31 0.46 0.83
outer loop
vertex 147.6 62.6 86.1
vertex 187.1 45.8 110.5
vertex 187.1 70.3 96.8
endloop
endfacet
facet normal 0.28 -0.47 -0.84
outer loop
vertex 187.1 75.5 103.9
vertex 227 82.3 113.3
vertex 227 53.6 129.4
endloop
endfacet
facet normal 0.28 -0.47 -0.84
outer loop
vertex 187.1 75.5 103.9
vertex 227 53.6 129.4
vertex 187.1 49.2 118.7
endloop
endfacet
facet normal -0.28 0.47 0.84
outer loop
vertex 187.1 70.3 96.8
vertex 187.1 45.8 110.5
vertex 227 50.2 121.2
endloop
endfacet
facet normal -0.28 0.47 0.84
outer loop
vertex 187.1 70.3 96.8
vertex 227 50.2 121.2
vertex 227 77.1 106.1
endloop
endfacet
facet normal 0.24 -0.47 -0.85
outer loop
vertex 227 82.3 113.3
vertex 267.1 88.2 121.4
vertex 267.1 57.4 138.6
endloop
endfacet
facet normal 0.24 -0.47 -0.85
outer loop
vertex 227 82.3 113.3
vertex 267.1 57.4 138.6
vertex 227 53.6 129.4
endloop
endfacet
facet normal -0.24 0.47 0.85
outer loop
vertex 227 77.1 106.1
vertex 227 50.2 121.2
vertex 267.1 54 130.4
endloop
endfacet
facet normal -0.24 0.47 0.85
outer loop
vertex 227 77.1 106.1
vertex 267.1 54 130.4
vertex 267.1 83 114.2
endloop
endfacet
facet normal 0.20 -0.48 -0.85
outer loop
vertex 267.1 88.2 121.4
vertex 307.6 93.1 128.2
vertex 307.6 60.6 146.4
endloop
endfacet
facet normal 0.20 -0.48 -0.85
outer loop
vertex 267.1 88.2 121.4
vertex 307.6 60.6 146.4
vertex 267.1 57.4 138.6
endloop
endfacet
facet normal -0.20 0.48 0.85
outer loop
vertex 267.1 83 114.2
vertex 267.1 54 130.4
vertex 307.6 57.2 138.2
endloop
endfacet
facet normal -0.20 0.48 0.85
outer loop
vertex 267.1 83 114.2
vertex 307.6 57.2 138.2
vertex 307.6 87.9 121
endloop
endfacet
facet normal 0.18 -0.48 -0.86
outer loop
vertex 307.6 93.1 128.2
vertex 323.8 94.8 130.5
vertex 323.8 61.7 149
endloop
endfacet
facet normal 0.18 -0.48 -0.86
outer loop
vertex 307.6 93.1 128.2
vertex 323.8 61.7 149
vertex 307.6 60.6 146.4
endloop
endfacet
facet normal -0.18 0.48 0.86
outer loop
vertex 307.6 87.9 121
vertex 307.6 57.2 138.2
vertex 323.8 58.4 140.9
endloop
endfacet
facet normal -0.18 0.48 0.86
outer loop
vertex 307.6 87.9 121
vertex 323.8 58.4 140.9
vertex 323.8 89.6 123.4
endloop
endfacet
facet normal 0.00 -0.27 -0.96
outer loop
vertex -393.4 32.6 78.6
vertex -260.1 32.6 78.6
vertex -260.1 13.3 84
endloop
endfacet
facet normal 0.00 -0.27 -0.96
outer loop
vertex -393.4 32.6 78.6
vertex -260.1 13.3 84
vertex -393.4 13.3 84
endloop
endfacet
facet normal 0.00 0.27 0.96
outer loop
vertex -393.4 29.2 70.4
vertex -393.4 11.9 75.3
vertex -260.1 11.9 75.3
endloop
endfacet
facet normal 0.00 0.27 0.96
outer loop
vertex -393.4 29.2 70.4
vertex -260.1 11.9 75.3
vertex -260.1 29.2 70.4
endloop
endfacet
facet normal 0.00 -0.27 -0.96
outer loop
vertex -260.1 32.6 78.6
vertex -126.8 32.6 78.6
vertex -126.8 13.3 84
endloop
endfacet
facet normal 0.00 -0.27 -0.96
outer loop
vertex -260.1 32.6 78.6
vertex -126.8 13.3 84
vertex -260.1 13.3 84
endloop
endfacet
facet normal 0.00 0.27 0.96
outer loop
vertex -260.1 29.2 70.4
vertex -260.1 11.9 75.3
vertex -126.8 11.9 75.3
endloop
endfacet
facet normal 0.00 0.27 0.96
outer loop
vertex -260.1 29.2 70.4
vertex -126.8 11.9 75.3
vertex -126.8 29.2 70.4
endloop
endfacet
facet normal -0.09 -0.27 -0.96
outer loop
vertex -126.8 32.6 78.6
vertex -63.4 30.3 73.2
vertex -63.4 12.4 78.3
endloop
endfacet
facet normal -0.09 -0.27 -0.96
outer loop
vertex -126.8 32.6 78.6
vertex -63.4 12.4 78.3
vertex -126.8 13.3 84
endloop
endfacet
facet normal 0.09 0.27 0.96
outer loop
vertex -126.8 29.2 70.4
vertex -126.8 11.9 75.3
vertex -63.4 11 69.5
endloop
endfacet
facet normal 0.09 0.27 0.96
outer loop
vertex -126.8 29.2 70.4
vertex -63.4 11 69.5
vertex -63.4 26.9 65
endloop
endfacet
facet normal -0.50 -0.24 -0.83
outer loop
vertex -63.4 30.3 73.2
vertex -46.5 26.6 64.2
vertex -46.5 10.9 68.6
endloop
endfacet
facet normal -0.50 -0.24 -0.83
outer loop
vertex -63.4 30.3 73.2
vertex -46.5 10.9 68.6
vertex -63.4 12.4 78.3
endloop
endfacet
facet normal 0.50 0.24 0.83
outer loop
vertex -63.4 26.9 65
vertex -63.4 11 69.5
vertex -46.5 9.5 59.9
endloop
endfacet
facet normal 0.50 0.24 0.83
outer loop
vertex -63.4 26.9 65
vertex -46.5 9.5 59.9
vertex -46.5 23.2 56
endloop
endfacet
facet normal -0.50 -0.24 -0.84
outer loop
vertex -46.5 26.6 64.2
vertex -31.1 23.2 56
vertex -31.1 9.5 59.9
endloop
endfacet
facet normal -0.50 -0.24 -0.84
outer loop
vertex -46.5 26.6 64.2
vertex -31.1 9.5 59.9
vertex -46.5 10.9 68.6
endloop
endfacet
facet normal 0.50 0.24 0.84
outer loop
vertex -46.5 23.2 56
vertex -46.5 9.5 59.9
vertex -31.1 8.1 51.2
endloop
endfacet
facet normal 0.50 0.24 0.84
outer loop
vertex -46.5 23.2 56
vertex -31.1 8.1 51.2
vertex -31.1 19.8 47.9
endloop
endfacet
facet normal -0.40 -0.25 -0.88
outer loop
vertex -31.1 23.2 56
vertex -21.2 21.6 52.1
vertex -21.2 8.8 55.7
endloop
endfacet
facet normal -0.40 -0.25 -0.88
outer loop
vertex -31.1 23.2 56
vertex -21.2 8.8 55.7
vertex -31.1 9.5 59.9
endloop
endfacet
facet normal 0.40 0.25 0.88
outer loop
vertex -31.1 19.8 47.9
vertex -31.1 8.1 51.2
vertex -21.2 7.4 46.9
endloop
endfacet
facet normal 0.40 0.25 0.88
outer loop
vertex -31.1 19.8 47.9
vertex -21.2 7.4 46.9
vertex -21.2 18.2 43.9
endloop
endfacet
facet normal -0.24 -0.26 -0.93
outer loop
vertex -21.2 21.6 52.1
vertex -10.8 20.6 49.7
vertex -10.8 8.4 53.1
endloop
endfacet
facet normal -0.24 -0.26 -0.93
outer loop
vertex -21.2 21.6 52.1
vertex -10.8 8.4 53.1
vertex -21.2 8.8 55.7
endloop
endfacet
facet normal 0.24 0.26 0.93
outer loop
vertex -21.2 18.2 43.9
vertex -21.2 7.4 46.9
vertex -10.8 7 44.3
endloop
endfacet
facet normal 0.24 0.26 0.93
outer loop
vertex -21.2 18.2 43.9
vertex -10.8 7 44.3
vertex -10.8 17.2 41.5
endloop
endfacet
facet normal -0.08 -0.27 -0.96
outer loop
vertex -10.8 20.6 49.7
vertex 0 20.2 48.8
vertex 0 8.3 52.2
endloop
endfacet
facet normal -0.08 -0.27 -0.96
outer loop
vertex -10.8 20.6 49.7
vertex 0 8.3 52.2
vertex -10.8 8.4 53.1
endloop
endfacet
facet normal 0.08 0.27 0.96
outer loop
vertex -10.8 17.2 41.5
vertex -10.8 7 44.3
vertex 0 6.9 43.5
endloop
endfacet
facet normal 0.08 0.27 0.96
outer loop
vertex -10.8 17.2 41.5
vertex 0 6.9 43.5
vertex 0 16.8 40.7
endloop
endfacet
facet normal 0.10 -0.27 -0.96
outer loop
vertex 0 20.2 48.8
vertex 3.3 20.4 49.1
vertex 3.3 8.3 52.5
endloop
endfacet
facet normal 0.10 -0.27 -0.96
outer loop
vertex 0 20.2 48.8
vertex 3.3 8.3 52.5
vertex 0 8.3 52.2
endloop
endfacet
facet normal -0.10 0.27 0.96
outer loop
vertex 0 16.8 40.7
vertex 0 6.9 43.5
vertex 3.3 6.9 43.8
endloop
endfacet
facet normal -0.10 0.27 0.96
outer loop
vertex 0 16.8 40.7
vertex 3.3 6.9 43.8
vertex 3.3 17 41
endloop
endfacet
facet normal 0.29 -0.26 -0.92
outer loop
vertex 3.3 20.4 49.1
vertex 6.5 20.7 50
vertex 6.5 8.5 53.5
endloop
endfacet
facet normal 0.29 -0.26 -0.92
outer loop
vertex 3.3 20.4 49.1
vertex 6.5 8.5 53.5
vertex 3.3 8.3 52.5
endloop
endfacet
facet normal -0.29 0.26 0.92
outer loop
vertex 3.3 17 41
vertex 3.3 6.9 43.8
vertex 6.5 7.1 44.8
endloop
endfacet
facet normal -0.29 0.26 0.92
outer loop
vertex 3.3 17 41
vertex 6.5 7.1 44.8
vertex 6.5 17.3 41.9
endloop
endfacet
facet normal 0.44 -0.24 -0.86
outer loop
vertex 6.5 20.7 50
vertex 30.7 25.4 61.2
vertex 30.7 10.4 65.4
endloop
endfacet
facet normal 0.44 -0.24 -0.86
outer loop
vertex 6.5 20.7 50
vertex 30.7 10.4 65.4
vertex 6.5 8.5 53.5
endloop
endfacet
facet normal -0.44 0.24 0.86
outer loop
vertex 6.5 17.3 41.9
vertex 6.5 7.1 44.8
vertex 30.7 9 56.7
endloop
endfacet
facet normal -0.44 0.24 0.86
outer loop
vertex 6.5 17.3 41.9
vertex 30.7 9 56.7
vertex 30.7 22 53
endloop
endfacet
facet normal 0.42 -0.25 -0.87
outer loop
vertex 30.7 25.4 61.2
vertex 69.4 32.2 77.8
vertex 69.4 13.2 83.1
endloop
endfacet
facet normal 0.42 -0.25 -0.87
outer loop
vertex 30.7 25.4 61.2
vertex 69.4 13.2 83.1
vertex 30.7 10.4 65.4
endloop
endfacet
facet normal -0.42 0.25 0.87
outer loop
vertex 30.7 22 53
vertex 30.7 9 56.7
vertex 69.4 11.8 74.4
endloop
endfacet
facet normal -0.42 0.25 0.87
outer loop
vertex 30.7 22 53
vertex 69.4 11.8 74.4
vertex 69.4 28.8 69.6
endloop
endfacet
facet normal 0.38 -0.25 -0.89
outer loop
vertex 69.4 32.2 77.8
vertex 108.3 38.5 92.9
vertex 108.3 15.7 99.3
endloop
endfacet
facet normal 0.38 -0.25 -0.89
outer loop
vertex 69.4 32.2 77.8
vertex 108.3 15.7 99.3
vertex 69.4 13.2 83.1
endloop
endfacet
facet normal -0.38 0.25 0.89
outer loop
vertex 69.4 28.8 69.6
vertex 69.4 11.8 74.4
vertex 108.3 14.3 90.6
endloop
endfacet
facet normal -0.38 0.25 0.89
outer loop
vertex 69.4 28.8 69.6
vertex 108.3 14.3 90.6
vertex 108.3 35.1 84.7
endloop
endfacet
facet normal 0.35 -0.25 -0.90
outer loop
vertex 108.3 38.5 92.9
vertex 147.6 44.1 106.5
vertex 147.6 18 113.9
endloop
endfacet
facet normal 0.35 -0.25 -0.90
outer loop
vertex 108.3 38.5 92.9
vertex 147.6 18 113.9
vertex 108.3 15.7 99.3
endloop
endfacet
facet normal -0.35 0.25 0.90
outer loop
vertex 108.3 35.1 84.7
vertex 108.3 14.3 90.6
vertex 147.6 16.7 105.1
endloop
endfacet
facet normal -0.35 0.25 0.90
outer loop
vertex 108.3 35.1 84.7
vertex 147.6 16.7 105.1
vertex 147.6 40.7 98.3
endloop
endfacet
facet normal 0.31 -0.26 -0.91
outer loop
vertex 147.6 44.1 106.5
vertex 187.1 49.2 118.7
vertex 187.1 20.1 126.9
endloop
endfacet
facet normal 0.31 -0.26 -0.91
outer loop
vertex 147.6 44.1 106.5
vertex 187.1 20.1 126.9
vertex 147.6 18 113.9
endloop
endfacet
facet normal -0.31 0.26 0.91
outer loop
vertex 147.6 40.7 98.3
vertex 147.6 16.7 105.1
vertex 187.1 18.7 118.1
endloop
endfacet
facet normal -0.31 0.26 0.91
outer loop
vertex 147.6 40.7 98.3
vertex 187.1 18.7 118.1
vertex 187.1 45.8 110.5
endloop
endfacet
facet normal 0.28 -0.26 -0.92
outer loop
vertex 187.1 49.2 118.7
vertex 227 53.6 129.4
vertex 227 21.9 138.3
endloop
endfacet
facet normal 0.28 -0.26 -0.92
outer loop
vertex 187.1 49.2 118.7
vertex 227 21.9 138.3
vertex 187.1 20.1 126.9
endloop
endfacet
facet normal -0.28 0.26 0.92
outer loop
vertex 187.1 45.8 110.5
vertex 187.1 18.7 118.1
vertex 227 20.5 129.6
endloop
endfacet
facet normal -0.28 0.26 0.92
outer loop
vertex 187.1 45.8 110.5
vertex 227 20.5 129.6
vertex 227 50.2 121.2
endloop
endfacet
facet normal 0.24 -0.26 -0.93
outer loop
vertex 227 53.6 129.4
vertex 267.1 57.4 138.6
vertex 267.1 23.5 148.2
endloop
endfacet
facet normal 0.24 -0.26 -0.93
outer loop
vertex 227 53.6 129.4
vertex 267.1 23.5 148.2
vertex 227 21.9 138.3
endloop
endfacet
facet normal -0.24 0.26 0.93
outer loop
vertex 227 50.2 121.2
vertex 227 20.5 129.6
vertex 267.1 22.1 139.4
endloop
endfacet
facet normal -0.24 0.26 0.93
outer loop
vertex 227 50.2 121.2
vertex 267.1 22.1 139.4
vertex 267.1 54 130.4
endloop
endfacet
facet normal 0.20 -0.27 -0.94
outer loop
vertex 267.1 57.4 138.6
vertex 307.6 60.6 146.4
vertex 307.6 24.8 156.5
endloop
endfacet
facet normal 0.20 -0.27 -0.94
outer loop
vertex 267.1 57.4 138.6
vertex 307.6 24.8 156.5
vertex 267.1 23.5 148.2
endloop
endfacet
facet normal -0.20 0.27 0.94
outer loop
vertex 267.1 54 130.4
vertex 267.1 22.1 139.4
vertex 307.6 23.4 147.7
endloop
endfacet
facet normal -0.20 0.27 0.94
outer loop
vertex 267.1 54 130.4
vertex 307.6 23.4 147.7
vertex 307.6 57.2 138.2
endloop
endfacet
facet normal 0.18 -0.27 -0.95
outer loop
vertex 307.6 60.6 146.4
vertex 323.8 61.7 149
vertex 323.8 25.2 159.3
endloop
endfacet
facet normal 0.18 -0.27 -0.95
outer loop
vertex 307.6 60.6 146.4
vertex 323.8 25.2 159.3
vertex 307.6 24.8 156.5
endloop
endfacet
facet normal -0.18 0.27 0.95
outer loop
vertex 307.6 57.2 138.2
vertex 307.6 23.4 147.7
vertex 323.8 23.9 150.6
endloop
endfacet
facet normal -0.18 0.27 0.95
outer loop
vertex 307.6 57.2 138.2
vertex 323.8 23.9 150.6
vertex 323.8 58.4 140.9
endloop
endfacet
facet normal 0.00 -0.04 -1.00
outer loop
vertex -393.4 13.3 84
vertex -260.1 13.3 84
vertex -260.1 -6.7 84.8
endloop
endfacet
facet normal 0.00 -0.04 -1.00
outer loop
vertex -393.4 13.3 84
vertex -260.1 -6.7 84.8
vertex -393.4 -6.7 84.8
endloop
endfacet
facet normal 0.00 0.04 1.00
outer loop
vertex -393.4 11.9 75.3
vertex -393.4 -6 76
vertex -260.1 -6 76
endloop
endfacet
facet normal 0.00 0.04 1.00
outer loop
vertex -393.4 11.9 75.3
vertex -260.1 -6 76
vertex -260.1 11.9 75.3
endloop
endfacet
facet normal 0.00 -0.04 -1.00
outer loop
vertex -260.1 13.3 84
vertex -126.8 13.3 84
vertex -126.8 -6.7 84.8
endloop
endfacet
facet normal 0.00 -0.04 -1.00
outer loop
vertex -260.1 13.3 84
vertex -126.8 -6.7 84.8
vertex -260.1 -6.7 84.8
endloop
endfacet
facet normal 0.00 0.04 1.00
outer loop
vertex -260.1 11.9 75.3
vertex -260.1 -6 76
vertex -126.8 -6 76
endloop
endfacet
facet normal 0.00 0.04 1.00
outer loop
vertex -260.1 11.9 75.3
vertex -126.8 -6 76
vertex -126.8 11.9 75.3
endloop
endfacet
facet normal -0.09 -0.04 -1.00
outer loop
vertex -126.8 13.3 84
vertex -63.4 12.4 78.3
vertex -63.4 -6.2 79
endloop
endfacet
facet normal -0.09 -0.04 -1.00
outer loop
vertex -126.8 13.3 84
vertex -63.4 -6.2 79
vertex -126.8 -6.7 84.8
endloop
endfacet
facet normal 0.09 0.04 1.00
outer loop
vertex -126.8 11.9 75.3
vertex -126.8 -6 76
vertex -63.4 -5.5 70.2
endloop
endfacet
facet normal 0.09 0.04 1.00
outer loop
vertex -126.8 11.9 75.3
vertex -63.4 -5.5 70.2
vertex -63.4 11 69.5
endloop
endfacet
facet normal -0.50 -0.03 -0.87
outer loop
vertex -63.4 12.4 78.3
vertex -46.5 10.9 68.6
vertex -46.5 -5.5 69.3
endloop
endfacet
facet normal -0.50 -0.03 -0.87
outer loop
vertex -63.4 12.4 78.3
vertex -46.5 -5.5 69.3
vertex -63.4 -6.2 79
endloop
endfacet
facet normal 0.50 0.03 0.87
outer loop
vertex -63.4 11 69.5
vertex -63.4 -5.5 70.2
vertex -46.5 -4.8 60.5
endloop
endfacet
facet normal 0.50 0.03 0.87
outer loop
vertex -63.4 11 69.5
vertex -46.5 -4.8 60.5
vertex -46.5 9.5 59.9
endloop
endfacet
facet normal -0.50 -0.03 -0.87
outer loop
vertex -46.5 10.9 68.6
vertex -31.1 9.5 59.9
vertex -31.1 -4.8 60.5
endloop
endfacet
facet normal -0.50 -0.03 -0.87
outer loop
vertex -46.5 10.9 68.6
vertex -31.1 -4.8 60.5
vertex -46.5 -5.5 69.3
endloop
endfacet
facet normal 0.50 0.03 0.87
outer loop
vertex -46.5 9.5 59.9
vertex -46.5 -4.8 60.5
vertex -31.1 -4.1 51.7
endloop
endfacet
facet normal 0.50 0.03 0.87
outer loop
vertex -46.5 9.5 59.9
vertex -31.1 -4.1 51.7
vertex -31.1 8.1 51.2
endloop
endfacet
facet normal -0.40 -0.04 -0.92
outer loop
vertex -31.1 9.5 59.9
vertex -21.2 8.8 55.7
vertex -21.2 -4.4 56.2
endloop
endfacet
facet normal -0.40 -0.04 -0.92
outer loop
vertex -31.1 9.5 59.9
vertex -21.2 -4.4 56.2
vertex -31.1 -4.8 60.5
endloop
endfacet
facet normal 0.40 0.04 0.92
outer loop
vertex -31.1 8.1 51.2
vertex -31.1 -4.1 51.7
vertex -21.2 -3.7 47.4
endloop
endfacet
facet normal 0.40 0.04 0.92
outer loop
vertex -31.1 8.1 51.2
vertex -21.2 -3.7 47.4
vertex -21.2 7.4 46.9
endloop
endfacet
facet normal -0.24 -0.04 -0.97
outer loop
vertex -21.2 8.8 55.7
vertex -10.8 8.4 53.1
vertex -10.8 -4.2 53.6
endloop
endfacet
facet normal -0.24 -0.04 -0.97
outer loop
vertex -21.2 8.8 55.7
vertex -10.8 -4.2 53.6
vertex -21.2 -4.4 56.2
endloop
endfacet
facet normal 0.24 0.04 0.97
outer loop
vertex -21.2 7.4 46.9
vertex -21.2 -3.7 47.4
vertex -10.8 -3.5 44.8
endloop
endfacet
facet normal 0.24 0.04 0.97
outer loop
vertex -21.2 7.4 46.9
vertex -10.8 -3.5 44.8
vertex -10.8 7 44.3
endloop
endfacet
facet normal -0.08 -0.04 -1.00
outer loop
vertex -10.8 8.4 53.1
vertex 0 8.3 52.2
vertex 0 -4.1 52.7
endloop
endfacet
facet normal -0.08 -0.04 -1.00
outer loop
vertex -10.8 8.4 53.1
vertex 0 -4.1 52.7
vertex -10.8 -4.2 53.6
endloop
endfacet
facet normal 0.08 0.04 1.00
outer loop
vertex -10.8 7 44.3
vertex -10.8 -3.5 44.8
vertex 0 -3.5 43.9
endloop
endfacet
facet normal 0.08 0.04 1.00
outer loop
vertex -10.8 7 44.3
vertex 0 -3.5 43.9
vertex 0 6.9 43.5
endloop
endfacet
facet normal 0.10 -0.04 -0.99
outer loop
vertex 0 8.3 52.2
vertex 3.3 8.3 52.5
vertex 3.3 -4.2 53
endloop
endfacet
facet normal 0.10 -0.04 -0.99
outer loop
vertex 0 8.3 52.2
vertex 3.3 -4.2 53
vertex 0 -4.1 52.7
endloop
endfacet
facet normal -0.10 0.04 0.99
outer loop
vertex 0 6.9 43.5
vertex 0 -3.5 43.9
vertex 3.3 -3.5 44.2
endloop
endfacet
facet normal -0.10 0.04 0.99
outer loop
vertex 0 6.9 43.5
vertex 3.3 -3.5 44.2
vertex 3.3 6.9 43.8
endloop
endfacet
facet normal 0.29 -0.04 -0.96
outer loop
vertex 3.3 8.3 52.5
vertex 6.5 8.5 53.5
vertex 6.5 -4.2 54
endloop
endfacet
facet normal 0.29 -0.04 -0.96
outer loop
vertex 3.3 8.3 52.5
vertex 6.5 -4.2 54
vertex 3.3 -4.2 53
endloop
endfacet
facet normal -0.29 0.04 0.96
outer loop
vertex 3.3 6.9 43.8
vertex 3.3 -3.5 44.2
vertex 6.5 -3.6 45.2
endloop
endfacet
facet normal -0.29 0.04 0.96
outer loop
vertex 3.3 6.9 43.8
vertex 6.5 -3.6 45.2
vertex 6.5 7.1 44.8
endloop
endfacet
facet normal 0.44 -0.04 -0.90
outer loop
vertex 6.5 8.5 53.5
vertex 30.7 10.4 65.4
vertex 30.7 -5.2 66
endloop
endfacet
facet normal 0.44 -0.04 -0.90
outer loop
vertex 6.5 8.5 53.5
vertex 30.7 -5.2 66
vertex 6.5 -4.2 54
endloop
endfacet
facet normal -0.44 0.04 0.90
outer loop
vertex 6.5 7.1 44.8
vertex 6.5 -3.6 45.2
vertex 30.7 -4.5 57.2
endloop
endfacet
facet normal -0.44 0.04 0.90
outer loop
vertex 6.5 7.1 44.8
vertex 30.7 -4.5 57.2
vertex 30.7 9 56.7
endloop
endfacet
facet normal 0.42 -0.04 -0.91
outer loop
vertex 30.7 10.4 65.4
vertex 69.4 13.2 83.1
vertex 69.4 -6.6 83.9
endloop
endfacet
facet normal 0.42 -0.04 -0.91
outer loop
vertex 30.7 10.4 65.4
vertex 69.4 -6.6 83.9
vertex 30.7 -5.2 66
endloop
endfacet
facet normal -0.42 0.04 0.91
outer loop
vertex 30.7 9 56.7
vertex 30.7 -4.5 57.2
vertex 69.4 -5.9 75.1
endloop
endfacet
facet normal -0.42 0.04 0.91
outer loop
vertex 30.7 9 56.7
vertex 69.4 -5.9 75.1
vertex 69.4 11.8 74.4
endloop
endfacet
facet normal 0.38 -0.04 -0.92
outer loop
vertex 69.4 13.2 83.1
vertex 108.3 15.7 99.3
vertex 108.3 -7.9 100.2
endloop
endfacet
facet normal 0.38 -0.04 -0.92
outer loop
vertex 69.4 13.2 83.1
vertex 108.3 -7.9 100.2
vertex 69.4 -6.6 83.9
endloop
endfacet
facet normal -0.38 0.04 0.92
outer loop
vertex 69.4 11.8 74.4
vertex 69.4 -5.9 75.1
vertex 108.3 -7.2 91.4
endloop
endfacet
facet normal -0.38 0.04 0.92
outer loop
vertex 69.4 11.8 74.4
vertex 108.3 -7.2 91.4
vertex 108.3 14.3 90.6
endloop
endfacet
facet normal 0.35 -0.04 -0.94
outer loop
vertex 108.3 15.7 99.3
vertex 147.6 18 113.9
vertex 147.6 -9 114.9
endloop
endfacet
facet normal 0.35 -0.04 -0.94
outer loop
vertex 108.3 15.7 99.3
vertex 147.6 -9 114.9
vertex 108.3 -7.9 100.2
endloop
endfacet
facet normal -0.35 0.04 0.94
outer loop
vertex 108.3 14.3 90.6
vertex 108.3 -7.2 91.4
vertex 147.6 -8.4 106.1
endloop
endfacet
facet normal -0.35 0.04 0.94
outer loop
vertex 108.3 14.3 90.6
vertex 147.6 -8.4 106.1
vertex 147.6 16.7 105.1
endloop
endfacet
facet normal 0.31 -0.04 -0.95
outer loop
vertex 147.6 18 113.9
vertex 187.1 20.1 126.9
vertex 187.1 -10.1 128.1
endloop
endfacet
facet normal 0.31 -0.04 -0.95
outer loop
vertex 147.6 18 113.9
vertex 187.1 -10.1 128.1
vertex 147.6 -9 114.9
endloop
endfacet
facet normal -0.31 0.04 0.95
outer loop
vertex 147.6 16.7 105.1
vertex 147.6 -8.4 106.1
vertex 187.1 -9.4 119.2
endloop
endfacet
facet normal -0.31 0.04 0.95
outer loop
vertex 147.6 16.7 105.1
vertex 187.1 -9.4 119.2
vertex 187.1 18.7 118.1
endloop
endfacet
facet normal 0.28 -0.04 -0.96
outer loop
vertex 187.1 20.1 126.9
vertex 227 21.9 138.3
vertex 227 -11 139.6
endloop
endfacet
facet normal 0.28 -0.04 -0.96
outer loop
vertex 187.1 20.1 126.9
vertex 227 -11 139.6
vertex 187.1 -10.1 128.1
endloop
endfacet
facet normal -0.28 0.04 0.96
outer loop
vertex 187.1 18.7 118.1
vertex 187.1 -9.4 119.2
vertex 227 -10.3 130.8
endloop
endfacet
facet normal -0.28 0.04 0.96
outer loop
vertex 187.1 18.7 118.1
vertex 227 -10.3 130.8
vertex 227 20.5 129.6
endloop
endfacet
facet normal 0.24 -0.04 -0.97
outer loop
vertex 227 21.9 138.3
vertex 267.1 23.5 148.2
vertex 267.1 -11.8 149.6
endloop
endfacet
facet normal 0.24 -0.04 -0.97
outer loop
vertex 227 21.9 138.3
vertex 267.1 -11.8 149.6
vertex 227 -11 139.6
endloop
endfacet
facet normal -0.24 0.04 0.97
outer loop
vertex 227 20.5 129.6
vertex 227 -10.3 130.8
vertex 267.1 -11.1 140.7
endloop
endfacet
facet normal -0.24 0.04 0.97
outer loop
vertex 227 20.5 129.6
vertex 267.1 -11.1 140.7
vertex 267.1 22.1 139.4
endloop
endfacet
facet normal 0.20 -0.04 -0.98
outer loop
vertex 267.1 23.5 148.2
vertex 307.6 24.8 156.5
vertex 307.6 -12.4 157.9
endloop
endfacet
facet normal 0.20 -0.04 -0.98
outer loop
vertex 267.1 23.5 148.2
vertex 307.6 -12.4 157.9
vertex 267.1 -11.8 149.6
endloop
endfacet
facet normal -0.20 0.04 0.98
outer loop
vertex 267.1 22.1 139.4
vertex 267.1 -11.1 140.7
vertex 307.6 -11.7 149.1
endloop
endfacet
facet normal -0.20 0.04 0.98
outer loop
vertex 267.1 22.1 139.4
vertex 307.6 -11.7 149.1
vertex 307.6 23.4 147.7
endloop
endfacet
facet normal 0.18 -0.04 -0.98
outer loop
vertex 307.6 24.8 156.5
vertex 323.8 25.2 159.3
vertex 323.8 -12.7 160.8
endloop
endfacet
facet normal 0.18 -0.04 -0.98
outer loop
vertex 307.6 24.8 156.5
vertex 323.8 -12.7 160.8
vertex 307.6 -12.4 157.9
endloop
endfacet
facet normal -0.18 0.04 0.98
outer loop
vertex 307.6 23.4 147.7
vertex 307.6 -11.7 149.1
vertex 323.8 -12 152
endloop
endfacet
facet normal -0.18 0.04 0.98
outer loop
vertex 307.6 23.4 147.7
vertex 323.8 -12 152
vertex 323.8 23.9 150.6
endloop
endfacet
facet normal 0.00 0.20 -0.98
outer loop
vertex -393.4 -6.7 84.8
vertex -260.1 -6.7 84.8
vertex -260.1 -26.3 80.9
endloop
endfacet
facet normal 0.00 0.20 -0.98
outer loop
vertex -393.4 -6.7 84.8
vertex -260.1 -26.3 80.9
vertex -393.4 -26.3 80.9
endloop
endfacet
facet normal 0.00 -0.20 0.98
outer loop
vertex -393.4 -6 76
vertex -393.4 -23.6 72.5
vertex -260.1 -23.6 72.5
endloop
endfacet
facet normal 0.00 -0.20 0.98
outer loop
vertex -393.4 -6 76
vertex -260.1 -23.6 72.5
vertex -260.1 -6 76
endloop
endfacet
facet normal 0.00 0.20 -0.98
outer loop
vertex -260.1 -6.7 84.8
vertex -126.8 -6.7 84.8
vertex -126.8 -26.3 80.9
endloop
endfacet
facet normal 0.00 0.20 -0.98
outer loop
vertex -260.1 -6.7 84.8
vertex -126.8 -26.3 80.9
vertex -260.1 -26.3 80.9
endloop
endfacet
facet normal 0.00 -0.20 0.98
outer loop
vertex -260.1 -6 76
vertex -260.1 -23.6 72.5
vertex -126.8 -23.6 72.5
endloop
endfacet
facet normal 0.00 -0.20 0.98
outer loop
vertex -260.1 -6 76
vertex -126.8 -23.6 72.5
vertex -126.8 -6 76
endloop
endfacet
facet normal -0.09 0.19 -0.98
outer loop
vertex -126.8 -6.7 84.8
vertex -63.4 -6.2 79
vertex -63.4 -24.5 75.4
endloop
endfacet
facet normal -0.09 0.19 -0.98
outer loop
vertex -126.8 -6.7 84.8
vertex -63.4 -24.5 75.4
vertex -126.8 -26.3 80.9
endloop
endfacet
facet normal 0.09 -0.19 0.98
outer loop
vertex -126.8 -6 76
vertex -126.8 -23.6 72.5
vertex -63.4 -21.8 66.9
endloop
endfacet
facet normal 0.09 -0.19 0.98
outer loop
vertex -126.8 -6 76
vertex -63.4 -21.8 66.9
vertex -63.4 -5.5 70.2
endloop
endfacet
facet normal -0.50 0.17 -0.85
outer loop
vertex -63.4 -6.2 79
vertex -46.5 -5.5 69.3
vertex -46.5 -21.5 66.1
endloop
endfacet
facet normal -0.50 0.17 -0.85
outer loop
vertex -63.4 -6.2 79
vertex -46.5 -21.5 66.1
vertex -63.4 -24.5 75.4
endloop
endfacet
facet normal 0.50 -0.17 0.85
outer loop
vertex -63.4 -5.5 70.2
vertex -63.4 -21.8 66.9
vertex -46.5 -18.7 57.7
endloop
endfacet
facet normal 0.50 -0.17 0.85
outer loop
vertex -63.4 -5.5 70.2
vertex -46.5 -18.7 57.7
vertex -46.5 -4.8 60.5
endloop
endfacet
facet normal -0.50 0.17 -0.85
outer loop
vertex -46.5 -5.5 69.3
vertex -31.1 -4.8 60.5
vertex -31.1 -18.7 57.7
endloop
endfacet
facet normal -0.50 0.17 -0.85
outer loop
vertex -46.5 -5.5 69.3
vertex -31.1 -18.7 57.7
vertex -46.5 -21.5 66.1
endloop
endfacet
facet normal 0.50 -0.17 0.85
outer loop
vertex -46.5 -4.8 60.5
vertex -46.5 -18.7 57.7
vertex -31.1 -16 49.3
endloop
endfacet
facet normal 0.50 -0.17 0.85
outer loop
vertex -46.5 -4.8 60.5
vertex -31.1 -16 49.3
vertex -31.1 -4.1 51.7
endloop
endfacet
facet normal -0.40 0.18 -0.90
outer loop
vertex -31.1 -4.8 60.5
vertex -21.2 -4.4 56.2
vertex -21.2 -17.4 53.6
endloop
endfacet
facet normal -0.40 0.18 -0.90
outer loop
vertex -31.1 -4.8 60.5
vertex -21.2 -17.4 53.6
vertex -31.1 -18.7 57.7
endloop
endfacet
facet normal 0.40 -0.18 0.90
outer loop
vertex -31.1 -4.1 51.7
vertex -31.1 -16 49.3
vertex -21.2 -14.7 45.2
endloop
endfacet
facet normal 0.40 -0.18 0.90
outer loop
vertex -31.1 -4.1 51.7
vertex -21.2 -14.7 45.2
vertex -21.2 -3.7 47.4
endloop
endfacet
facet normal -0.24 0.19 -0.95
outer loop
vertex -21.2 -4.4 56.2
vertex -10.8 -4.2 53.6
vertex -10.8 -16.6 51.1
endloop
endfacet
facet normal -0.24 0.19 -0.95
outer loop
vertex -21.2 -4.4 56.2
vertex -10.8 -16.6 51.1
vertex -21.2 -17.4 53.6
endloop
endfacet
facet normal 0.24 -0.19 0.95
outer loop
vertex -21.2 -3.7 47.4
vertex -21.2 -14.7 45.2
vertex -10.8 -13.9 42.7
endloop
endfacet
facet normal 0.24 -0.19 0.95
outer loop
vertex -21.2 -3.7 47.4
vertex -10.8 -13.9 42.7
vertex -10.8 -3.5 44.8
endloop
endfacet
facet normal -0.08 0.19 -0.98
outer loop
vertex -10.8 -4.2 53.6
vertex 0 -4.1 52.7
vertex 0 -16.3 50.3
endloop
endfacet
facet normal -0.08 0.19 -0.98
outer loop
vertex -10.8 -4.2 53.6
vertex 0 -16.3 50.3
vertex -10.8 -16.6 51.1
endloop
endfacet
facet normal 0.08 -0.19 0.98
outer loop
vertex -10.8 -3.5 44.8
vertex -10.8 -13.9 42.7
vertex 0 -13.6 41.9
endloop
endfacet
facet normal 0.08 -0.19 0.98
outer loop
vertex -10.8 -3.5 44.8
vertex 0 -13.6 41.9
vertex 0 -3.5 43.9
endloop
endfacet
facet normal 0.10 0.19 -0.98
outer loop
vertex 0 -4.1 52.7
vertex 3.3 -4.2 53
vertex 3.3 -16.4 50.6
endloop
endfacet
facet normal 0.10 0.19 -0.98
outer loop
vertex 0 -4.1 52.7
vertex 3.3 -16.4 50.6
vertex 0 -16.3 50.3
endloop
endfacet
facet normal -0.10 -0.19 0.98
outer loop
vertex 0 -3.5 43.9
vertex 0 -13.6 41.9
vertex 3.3 -13.7 42.2
endloop
endfacet
facet normal -0.10 -0.19 0.98
outer loop
vertex 0 -3.5 43.9
vertex 3.3 -13.7 42.2
vertex 3.3 -3.5 44.2
endloop
endfacet
facet normal 0.29 0.19 -0.94
outer loop
vertex 3.3 -4.2 53
vertex 6.5 -4.2 54
vertex 6.5 -16.7 51.5
endloop
endfacet
facet normal 0.29 0.19 -0.94
outer loop
vertex 3.3 -4.2 53
vertex 6.5 -16.7 51.5
vertex 3.3 -16.4 50.6
endloop
endfacet
facet normal -0.29 -0.19 0.94
outer loop
vertex 3.3 -3.5 44.2
vertex 3.3 -13.7 42.2
vertex 6.5 -14 43.1
endloop
endfacet
facet normal -0.29 -0.19 0.94
outer loop
vertex 3.3 -3.5 44.2
vertex 6.5 -14 43.1
vertex 6.5 -3.6 45.2
endloop
endfacet
facet normal 0.44 0.17 -0.88
outer loop
vertex 6.5 -4.2 54
vertex 30.7 -5.2 66
vertex 30.7 -20.5 63
endloop
endfacet
facet normal 0.44 0.17 -0.88
outer loop
vertex 6.5 -4.2 54
vertex 30.7 -20.5 63
vertex 6.5 -16.7 51.5
endloop
endfacet
facet normal -0.44 -0.17 0.88
outer loop
vertex 6.5 -3.6 45.2
vertex 6.5 -14 43.1
vertex 30.7 -17.7 54.6
endloop
endfacet
facet normal -0.44 -0.17 0.88
outer loop
vertex 6.5 -3.6 45.2
vertex 30.7 -17.7 54.6
vertex 30.7 -4.5 57.2
endloop
endfacet
facet normal 0.42 0.18 -0.89
outer loop
vertex 30.7 -5.2 66
vertex 69.4 -6.6 83.9
vertex 69.4 -26 80.1
endloop
endfacet
facet normal 0.42 0.18 -0.89
outer loop
vertex 30.7 -5.2 66
vertex 69.4 -26 80.1
vertex 30.7 -20.5 63
endloop
endfacet
facet normal -0.42 -0.18 0.89
outer loop
vertex 30.7 -4.5 57.2
vertex 30.7 -17.7 54.6
vertex 69.4 -23.3 71.7
endloop
endfacet
facet normal -0.42 -0.18 0.89
outer loop
vertex 30.7 -4.5 57.2
vertex 69.4 -23.3 71.7
vertex 69.4 -5.9 75.1
endloop
endfacet
facet normal 0.38 0.18 -0.91
outer loop
vertex 69.4 -6.6 83.9
vertex 108.3 -7.9 100.2
vertex 108.3 -31.1 95.6
endloop
endfacet
facet normal 0.38 0.18 -0.91
outer loop
vertex 69.4 -6.6 83.9
vertex 108.3 -31.1 95.6
vertex 69.4 -26 80.1
endloop
endfacet
facet normal -0.38 -0.18 0.91
outer loop
vertex 69.4 -5.9 75.1
vertex 69.4 -23.3 71.7
vertex 108.3 -28.3 87.2
endloop
endfacet
facet normal -0.38 -0.18 0.91
outer loop
vertex 69.4 -5.9 75.1
vertex 108.3 -28.3 87.2
vertex 108.3 -7.2 91.4
endloop
endfacet
facet normal 0.35 0.18 -0.92
outer loop
vertex 108.3 -7.9 100.2
vertex 147.6 -9 114.9
vertex 147.6 -35.6 109.6
endloop
endfacet
facet normal 0.35 0.18 -0.92
outer loop
vertex 108.3 -7.9 100.2
vertex 147.6 -35.6 109.6
vertex 108.3 -31.1 95.6
endloop
endfacet
facet normal -0.35 -0.18 0.92
outer loop
vertex 108.3 -7.2 91.4
vertex 108.3 -28.3 87.2
vertex 147.6 -32.9 101.2
endloop
endfacet
facet normal -0.35 -0.18 0.92
outer loop
vertex 108.3 -7.2 91.4
vertex 147.6 -32.9 101.2
vertex 147.6 -8.4 106.1
endloop
endfacet
facet normal 0.31 0.19 -0.93
outer loop
vertex 147.6 -9 114.9
vertex 187.1 -10.1 128.1
vertex 187.1 -39.7 122.2
endloop
endfacet
facet normal 0.31 0.19 -0.93
outer loop
vertex 147.6 -9 114.9
vertex 187.1 -39.7 122.2
vertex 147.6 -35.6 109.6
endloop
endfacet
facet normal -0.31 -0.19 0.93
outer loop
vertex 147.6 -8.4 106.1
vertex 147.6 -32.9 101.2
vertex 187.1 -37 113.8
endloop
endfacet
facet normal -0.31 -0.19 0.93
outer loop
vertex 147.6 -8.4 106.1
vertex 187.1 -37 113.8
vertex 187.1 -9.4 119.2
endloop
endfacet
facet normal 0.28 0.19 -0.94
outer loop
vertex 187.1 -10.1 128.1
vertex 227 -11 139.6
vertex 227 -43.3 133.2
endloop
endfacet
facet normal 0.28 0.19 -0.94
outer loop
vertex 187.1 -10.1 128.1
vertex 227 -43.3 133.2
vertex 187.1 -39.7 122.2
endloop
endfacet
facet normal -0.28 -0.19 0.94
outer loop
vertex 187.1 -9.4 119.2
vertex 187.1 -37 113.8
vertex 227 -40.5 124.8
endloop
endfacet
facet normal -0.28 -0.19 0.94
outer loop
vertex 187.1 -9.4 119.2
vertex 227 -40.5 124.8
vertex 227 -10.3 130.8
endloop
endfacet
facet normal 0.24 0.19 -0.95
outer loop
vertex 227 -11 139.6
vertex 267.1 -11.8 149.6
vertex 267.1 -46.4 142.7
endloop
endfacet
facet normal 0.24 0.19 -0.95
outer loop
vertex 227 -11 139.6
vertex 267.1 -46.4 142.7
vertex 227 -43.3 133.2
endloop
endfacet
facet normal -0.24 -0.19 0.95
outer loop
vertex 227 -10.3 130.8
vertex 227 -40.5 124.8
vertex 267.1 -43.6 134.3
endloop
endfacet
facet normal -0.24 -0.19 0.95
outer loop
vertex 227 -10.3 130.8
vertex 267.1 -43.6 134.3
vertex 267.1 -11.1 140.7
endloop
endfacet
facet normal 0.20 0.19 -0.96
outer loop
vertex 267.1 -11.8 149.6
vertex 307.6 -12.4 157.9
vertex 307.6 -49 150.7
endloop
endfacet
facet normal 0.20 0.19 -0.96
outer loop
vertex 267.1 -11.8 149.6
vertex 307.6 -49 150.7
vertex 267.1 -46.4 142.7
endloop
endfacet
facet normal -0.20 -0.19 0.96
outer loop
vertex 267.1 -11.1 140.7
vertex 267.1 -43.6 134.3
vertex 307.6 -46.2 142.2
endloop
endfacet
facet normal -0.20 -0.19 0.96
outer loop
vertex 267.1 -11.1 140.7
vertex 307.6 -46.2 142.2
vertex 307.6 -11.7 149.1
endloop
endfacet
facet normal 0.18 0.19 -0.97
outer loop
vertex 307.6 -12.4 157.9
vertex 323.8 -12.7 160.8
vertex 323.8 -49.9 153.4
endloop
endfacet
facet normal 0.18 0.19 -0.97
outer loop
vertex 307.6 -12.4 157.9
vertex 323.8 -49.9 153.4
vertex 307.6 -49 150.7
endloop
endfacet
facet normal -0.18 -0.19 0.97
outer loop
vertex 307.6 -11.7 149.1
vertex 307.6 -46.2 142.2
vertex 323.8 -47.1 145
endloop
endfacet
facet normal -0.18 -0.19 0.97
outer loop
vertex 307.6 -11.7 149.1
vertex 323.8 -47.1 145
vertex 323.8 -12 152
endloop
endfacet
facet normal 0.00 0.42 -0.91
outer loop
vertex -393.4 -26.3 80.9
vertex -260.1 -26.3 80.9
vertex -260.1 -44.5 72.5
endloop
endfacet
facet normal 0.00 0.42 -0.91
outer loop
vertex -393.4 -26.3 80.9
vertex -260.1 -44.5 72.5
vertex -393.4 -44.5 72.5
endloop
endfacet
facet normal 0.00 -0.42 0.91
outer loop
vertex -393.4 -23.6 72.5
vertex -393.4 -39.8 65
vertex -260.1 -39.8 65
endloop
endfacet
facet normal 0.00 -0.42 0.91
outer loop
vertex -393.4 -23.6 72.5
vertex -260.1 -39.8 65
vertex -260.1 -23.6 72.5
endloop
endfacet
facet normal 0.00 0.42 -0.91
outer loop
vertex -260.1 -26.3 80.9
vertex -126.8 -26.3 80.9
vertex -126.8 -44.5 72.5
endloop
endfacet
facet normal 0.00 0.42 -0.91
outer loop
vertex -260.1 -26.3 80.9
vertex -126.8 -44.5 72.5
vertex -260.1 -44.5 72.5
endloop
endfacet
facet normal 0.00 -0.42 0.91
outer loop
vertex -260.1 -23.6 72.5
vertex -260.1 -39.8 65
vertex -126.8 -39.8 65
endloop
endfacet
facet normal 0.00 -0.42 0.91
outer loop
vertex -260.1 -23.6 72.5
vertex -126.8 -39.8 65
vertex -126.8 -23.6 72.5
endloop
endfacet
facet normal -0.09 0.42 -0.90
outer loop
vertex -126.8 -26.3 80.9
vertex -63.4 -24.5 75.4
vertex -63.4 -41.4 67.6
endloop
endfacet
facet normal -0.09 0.42 -0.90
outer loop
vertex -126.8 -26.3 80.9
vertex -63.4 -41.4 67.6
vertex -126.8 -44.5 72.5
endloop
endfacet
facet normal 0.09 -0.42 0.90
outer loop
vertex -126.8 -23.6 72.5
vertex -126.8 -39.8 65
vertex -63.4 -36.8 60
endloop
endfacet
facet normal 0.09 -0.42 0.90
outer loop
vertex -126.8 -23.6 72.5
vertex -63.4 -36.8 60
vertex -63.4 -21.8 66.9
endloop
endfacet
facet normal -0.50 0.36 -0.79
outer loop
vertex -63.4 -24.5 75.4
vertex -46.5 -21.5 66.1
vertex -46.5 -36.3 59.3
endloop
endfacet
facet normal -0.50 0.36 -0.79
outer loop
vertex -63.4 -24.5 75.4
vertex -46.5 -36.3 59.3
vertex -63.4 -41.4 67.6
endloop
endfacet
facet normal 0.50 -0.36 0.79
outer loop
vertex -63.4 -21.8 66.9
vertex -63.4 -36.8 60
vertex -46.5 -31.7 51.7
endloop
endfacet
facet normal 0.50 -0.36 0.79
outer loop
vertex -63.4 -21.8 66.9
vertex -46.5 -31.7 51.7
vertex -46.5 -18.7 57.7
endloop
endfacet
facet normal -0.50 0.36 -0.79
outer loop
vertex -46.5 -21.5 66.1
vertex -31.1 -18.7 57.7
vertex -31.1 -31.7 51.7
endloop
endfacet
facet normal -0.50 0.36 -0.79
outer loop
vertex -46.5 -21.5 66.1
vertex -31.1 -31.7 51.7
vertex -46.5 -36.3 59.3
endloop
endfacet
facet normal 0.50 -0.36 0.79
outer loop
vertex -46.5 -18.7 57.7
vertex -46.5 -31.7 51.7
vertex -31.1 -27.1 44.2
endloop
endfacet
facet normal 0.50 -0.36 0.79
outer loop
vertex -46.5 -18.7 57.7
vertex -31.1 -27.1 44.2
vertex -31.1 -16 49.3
endloop
endfacet
facet normal -0.40 0.38 -0.83
outer loop
vertex -31.1 -18.7 57.7
vertex -21.2 -17.4 53.6
vertex -21.2 -29.5 48.1
endloop
endfacet
facet normal -0.40 0.38 -0.83
outer loop
vertex -31.1 -18.7 57.7
vertex -21.2 -29.5 48.1
vertex -31.1 -31.7 51.7
endloop
endfacet
facet normal 0.40 -0.38 0.83
outer loop
vertex -31.1 -16 49.3
vertex -31.1 -27.1 44.2
vertex -21.2 -24.8 40.5
endloop
endfacet
facet normal 0.40 -0.38 0.83
outer loop
vertex -31.1 -16 49.3
vertex -21.2 -24.8 40.5
vertex -21.2 -14.7 45.2
endloop
endfacet
facet normal -0.24 0.41 -0.88
outer loop
vertex -21.2 -17.4 53.6
vertex -10.8 -16.6 51.1
vertex -10.8 -28.1 45.8
endloop
endfacet
facet normal -0.24 0.41 -0.88
outer loop
vertex -21.2 -17.4 53.6
vertex -10.8 -28.1 45.8
vertex -21.2 -29.5 48.1
endloop
endfacet
facet normal 0.24 -0.41 0.88
outer loop
vertex -21.2 -14.7 45.2
vertex -21.2 -24.8 40.5
vertex -10.8 -23.5 38.3
endloop
endfacet
facet normal 0.24 -0.41 0.88
outer loop
vertex -21.2 -14.7 45.2
vertex -10.8 -23.5 38.3
vertex -10.8 -13.9 42.7
endloop
endfacet
facet normal -0.08 0.42 -0.91
outer loop
vertex -10.8 -16.6 51.1
vertex 0 -16.3 50.3
vertex 0 -27.6 45.1
endloop
endfacet
facet normal -0.08 0.42 -0.91
outer loop
vertex -10.8 -16.6 51.1
vertex 0 -27.6 45.1
vertex -10.8 -28.1 45.8
endloop
endfacet
facet normal 0.08 -0.42 0.91
outer loop
vertex -10.8 -13.9 42.7
vertex -10.8 -23.5 38.3
vertex 0 -23 37.5
endloop
endfacet
facet normal 0.08 -0.42 0.91
outer loop
vertex -10.8 -13.9 42.7
vertex 0 -23 37.5
vertex 0 -13.6 41.9
endloop
endfacet
facet normal 0.10 0.42 -0.90
outer loop
vertex 0 -16.3 50.3
vertex 3.3 -16.4 50.6
vertex 3.3 -27.8 45.4
endloop
endfacet
facet normal 0.10 0.42 -0.90
outer loop
vertex 0 -16.3 50.3
vertex 3.3 -27.8 45.4
vertex 0 -27.6 45.1
endloop
endfacet
facet normal -0.10 -0.42 0.90
outer loop
vertex 0 -13.6 41.9
vertex 0 -23 37.5
vertex 3.3 -23.2 37.8
endloop
endfacet
facet normal -0.10 -0.42 0.90
outer loop
vertex 0 -13.6 41.9
vertex 3.3 -23.2 37.8
vertex 3.3 -13.7 42.2
endloop
endfacet
facet normal 0.29 0.40 -0.87
outer loop
vertex 3.3 -16.4 50.6
vertex 6.5 -16.7 51.5
vertex 6.5 -28.3 46.2
endloop
endfacet
facet normal 0.29 0.40 -0.87
outer loop
vertex 3.3 -16.4 50.6
vertex 6.5 -28.3 46.2
vertex 3.3 -27.8 45.4
endloop
endfacet
facet normal -0.29 -0.40 0.87
outer loop
vertex 3.3 -13.7 42.2
vertex 3.3 -23.2 37.8
vertex 6.5 -23.7 38.6
endloop
endfacet
facet normal -0.29 -0.40 0.87
outer loop
vertex 3.3 -13.7 42.2
vertex 6.5 -23.7 38.6
vertex 6.5 -14 43.1
endloop
endfacet
facet normal 0.44 0.38 -0.81
outer loop
vertex 6.5 -16.7 51.5
vertex 30.7 -20.5 63
vertex 30.7 -34.6 56.5
endloop
endfacet
facet normal 0.44 0.38 -0.81
outer loop
vertex 6.5 -16.7 51.5
vertex 30.7 -34.6 56.5
vertex 6.5 -28.3 46.2
endloop
endfacet
facet normal -0.44 -0.38 0.81
outer loop
vertex 6.5 -14 43.1
vertex 6.5 -23.7 38.6
vertex 30.7 -30 48.9
endloop
endfacet
facet normal -0.44 -0.38 0.81
outer loop
vertex 6.5 -14 43.1
vertex 30.7 -30 48.9
vertex 30.7 -17.7 54.6
endloop
endfacet
facet normal 0.42 0.38 -0.82
outer loop
vertex 30.7 -20.5 63
vertex 69.4 -26 80.1
vertex 69.4 -44 71.8
endloop
endfacet
facet normal 0.42 0.38 -0.82
outer loop
vertex 30.7 -20.5 63
vertex 69.4 -44 71.8
vertex 30.7 -34.6 56.5
endloop
endfacet
facet normal -0.42 -0.38 0.82
outer loop
vertex 30.7 -17.7 54.6
vertex 30.7 -30 48.9
vertex 69.4 -39.4 64.2
endloop
endfacet
facet normal -0.42 -0.38 0.82
outer loop
vertex 30.7 -17.7 54.6
vertex 69.4 -39.4 64.2
vertex 69.4 -23.3 71.7
endloop
endfacet
facet normal 0.38 0.39 -0.84
outer loop
vertex 69.4 -26 80.1
vertex 108.3 -31.1 95.6
vertex 108.3 -52.5 85.7
endloop
endfacet
facet normal 0.38 0.39 -0.84
outer loop
vertex 69.4 -26 80.1
vertex 108.3 -52.5 85.7
vertex 69.4 -44 71.8
endloop
endfacet
facet normal -0.38 -0.39 0.84
outer loop
vertex 69.4 -23.3 71.7
vertex 69.4 -39.4 64.2
vertex 108.3 -47.9 78.2
endloop
endfacet
facet normal -0.38 -0.39 0.84
outer loop
vertex 69.4 -23.3 71.7
vertex 108.3 -47.9 78.2
vertex 108.3 -28.3 87.2
endloop
endfacet
facet normal 0.35 0.39 -0.85
outer loop
vertex 108.3 -31.1 95.6
vertex 147.6 -35.6 109.6
vertex 147.6 -60.2 98.3
endloop
endfacet
facet normal 0.35 0.39 -0.85
outer loop
vertex 108.3 -31.1 95.6
vertex 147.6 -60.2 98.3
vertex 108.3 -52.5 85.7
endloop
endfacet
facet normal -0.35 -0.39 0.85
outer loop
vertex 108.3 -28.3 87.2
vertex 108.3 -47.9 78.2
vertex 147.6 -55.6 90.8
endloop
endfacet
facet normal -0.35 -0.39 0.85
outer loop
vertex 108.3 -28.3 87.2
vertex 147.6 -55.6 90.8
vertex 147.6 -32.9 101.2
endloop
endfacet
facet normal 0.31 0.40 -0.86
outer loop
vertex 147.6 -35.6 109.6
vertex 187.1 -39.7 122.2
vertex 187.1 -67.1 109.5
endloop
endfacet
facet normal 0.31 0.40 -0.86
outer loop
vertex 147.6 -35.6 109.6
vertex 187.1 -67.1 109.5
vertex 147.6 -60.2 98.3
endloop
endfacet
facet normal -0.31 -0.40 0.86
outer loop
vertex 147.6 -32.9 101.2
vertex 147.6 -55.6 90.8
vertex 187.1 -62.5 102
endloop
endfacet
facet normal -0.31 -0.40 0.86
outer loop
vertex 147.6 -32.9 101.2
vertex 187.1 -62.5 102
vertex 187.1 -37 113.8
endloop
endfacet
facet normal 0.28 0.40 -0.87
outer loop
vertex 187.1 -39.7 122.2
vertex 227 -43.3 133.2
vertex 227 -73.2 119.4
endloop
endfacet
facet normal 0.28 0.40 -0.87
outer loop
vertex 187.1 -39.7 122.2
vertex 227 -73.2 119.4
vertex 187.1 -67.1 109.5
endloop
endfacet
facet normal -0.28 -0.40 0.87
outer loop
vertex 187.1 -37 113.8
vertex 187.1 -62.5 102
vertex 227 -68.5 111.9
endloop
endfacet
facet normal -0.28 -0.40 0.87
outer loop
vertex 187.1 -37 113.8
vertex 227 -68.5 111.9
vertex 227 -40.5 124.8
endloop
endfacet
facet normal 0.24 0.41 -0.88
outer loop
vertex 227 -43.3 133.2
vertex 267.1 -46.4 142.7
vertex 267.1 -78.4 127.9
endloop
endfacet
facet normal 0.24 0.41 -0.88
outer loop
vertex 227 -43.3 133.2
vertex 267.1 -78.4 127.9
vertex 227 -73.2 119.4
endloop
endfacet
facet normal -0.24 -0.41 0.88
outer loop
vertex 227 -40.5 124.8
vertex 227 -68.5 111.9
vertex 267.1 -73.8 120.4
endloop
endfacet
facet normal -0.24 -0.41 0.88
outer loop
vertex 227 -40.5 124.8
vertex 267.1 -73.8 120.4
vertex 267.1 -43.6 134.3
endloop
endfacet
facet normal 0.20 0.41 -0.89
outer loop
vertex 267.1 -46.4 142.7
vertex 307.6 -49 150.7
vertex 307.6 -82.8 135.1
endloop
endfacet
facet normal 0.20 0.41 -0.89
outer loop
vertex 267.1 -46.4 142.7
vertex 307.6 -82.8 135.1
vertex 267.1 -78.4 127.9
endloop
endfacet
facet normal -0.20 -0.41 0.89
outer loop
vertex 267.1 -43.6 134.3
vertex 267.1 -73.8 120.4
vertex 307.6 -78.1 127.5
endloop
endfacet
facet normal -0.20 -0.41 0.89
outer loop
vertex 267.1 -43.6 134.3
vertex 307.6 -78.1 127.5
vertex 307.6 -46.2 142.2
endloop
endfacet
facet normal 0.18 0.41 -0.89
outer loop
vertex 307.6 -49 150.7
vertex 323.8 -49.9 153.4
vertex 323.8 -84.3 137.5
endloop
endfacet
facet normal 0.18 0.41 -0.89
outer loop
vertex 307.6 -49 150.7
vertex 323.8 -84.3 137.5
vertex 307.6 -82.8 135.1
endloop
endfacet
facet normal -0.18 -0.41 0.89
outer loop
vertex 307.6 -46.2 142.2
vertex 307.6 -78.1 127.5
vertex 323.8 -79.7 130
endloop
endfacet
facet normal -0.18 -0.41 0.89
outer loop
vertex 307.6 -46.2 142.2
vertex 323.8 -79.7 130
vertex 323.8 -47.1 145
endloop
endfacet
facet normal 0.00 0.62 -0.79
outer loop
vertex -393.4 -44.5 72.5
vertex -260.1 -44.5 72.5
vertex -260.1 -60.2 60.2
endloop
endfacet
facet normal 0.00 0.62 -0.79
outer loop
vertex -393.4 -44.5 72.5
vertex -260.1 -60.2 60.2
vertex -393.4 -60.2 60.2
endloop
endfacet
facet normal 0.00 -0.62 0.79
outer loop
vertex -393.4 -39.8 65
vertex -393.4 -53.9 53.9
vertex -260.1 -53.9 53.9
endloop
endfacet
facet normal 0.00 -0.62 0.79
outer loop
vertex -393.4 -39.8 65
vertex -260.1 -53.9 53.9
vertex -260.1 -39.8 65
endloop
endfacet
facet normal 0.00 0.62 -0.79
outer loop
vertex -260.1 -44.5 72.5
vertex -126.8 -44.5 72.5
vertex -126.8 -60.2 60.2
endloop
endfacet
facet normal 0.00 0.62 -0.79
outer loop
vertex -260.1 -44.5 72.5
vertex -126.8 -60.2 60.2
vertex -260.1 -60.2 60.2
endloop
endfacet
facet normal 0.00 -0.62 0.79
outer loop
vertex -260.1 -39.8 65
vertex -260.1 -53.9 53.9
vertex -126.8 -53.9 53.9
endloop
endfacet
facet normal 0.00 -0.62 0.79
outer loop
vertex -260.1 -39.8 65
vertex -126.8 -53.9 53.9
vertex -126.8 -39.8 65
endloop
endfacet
facet normal -0.09 0.62 -0.78
outer loop
vertex -126.8 -44.5 72.5
vertex -63.4 -41.4 67.6
vertex -63.4 -56 56
endloop
endfacet
facet normal -0.09 0.62 -0.78
outer loop
vertex -126.8 -44.5 72.5
vertex -63.4 -56 56
vertex -126.8 -60.2 60.2
endloop
endfacet
facet normal 0.09 -0.62 0.78
outer loop
vertex -126.8 -39.8 65
vertex -126.8 -53.9 53.9
vertex -63.4 -49.8 49.8
endloop
endfacet
facet normal 0.09 -0.62 0.78
outer loop
vertex -126.8 -39.8 65
vertex -63.4 -49.8 49.8
vertex -63.4 -36.8 60
endloop
endfacet
facet normal -0.50 0.54 -0.68
outer loop
vertex -63.4 -41.4 67.6
vertex -46.5 -36.3 59.3
vertex -46.5 -49.1 49.1
endloop
endfacet
facet normal -0.50 0.54 -0.68
outer loop
vertex -63.4 -41.4 67.6
vertex -46.5 -49.1 49.1
vertex -63.4 -56 56
endloop
endfacet
facet normal 0.50 -0.54 0.68
outer loop
vertex -63.4 -36.8 60
vertex -63.4 -49.8 49.8
vertex -46.5 -42.9 42.9
endloop
endfacet
facet normal 0.50 -0.54 0.68
outer loop
vertex -63.4 -36.8 60
vertex -46.5 -42.9 42.9
vertex -46.5 -31.7 51.7
endloop
endfacet
facet normal -0.50 0.54 -0.68
outer loop
vertex -46.5 -36.3 59.3
vertex -31.1 -31.7 51.7
vertex -31.1 -42.9 42.9
endloop
endfacet
facet normal -0.50 0.54 -0.68
outer loop
vertex -46.5 -36.3 59.3
vertex -31.1 -42.9 42.9
vertex -46.5 -49.1 49.1
endloop
endfacet
facet normal 0.50 -0.54 0.68
outer loop
vertex -46.5 -31.7 51.7
vertex -46.5 -42.9 42.9
vertex -31.1 -36.6 36.6
endloop
endfacet
facet normal 0.50 -0.54 0.68
outer loop
vertex -46.5 -31.7 51.7
vertex -31.1 -36.6 36.6
vertex -31.1 -27.1 44.2
endloop
endfacet
facet normal -0.40 0.57 -0.72
outer loop
vertex -31.1 -31.7 51.7
vertex -21.2 -29.5 48.1
vertex -21.2 -39.9 39.9
endloop
endfacet
facet normal -0.40 0.57 -0.72
outer loop
vertex -31.1 -31.7 51.7
vertex -21.2 -39.9 39.9
vertex -31.1 -42.9 42.9
endloop
endfacet
facet normal 0.40 -0.57 0.72
outer loop
vertex -31.1 -27.1 44.2
vertex -31.1 -36.6 36.6
vertex -21.2 -33.6 33.6
endloop
endfacet
facet normal 0.40 -0.57 0.72
outer loop
vertex -31.1 -27.1 44.2
vertex -21.2 -33.6 33.6
vertex -21.2 -24.8 40.5
endloop
endfacet
facet normal -0.24 0.60 -0.76
outer loop
vertex -21.2 -29.5 48.1
vertex -10.8 -28.1 45.8
vertex -10.8 -38 38
endloop
endfacet
facet normal -0.24 0.60 -0.76
outer loop
vertex -21.2 -29.5 48.1
vertex -10.8 -38 38
vertex -21.2 -39.9 39.9
endloop
endfacet
facet normal 0.24 -0.60 0.76
outer loop
vertex -21.2 -24.8 40.5
vertex -21.2 -33.6 33.6
vertex -10.8 -31.7 31.7
endloop
endfacet
facet normal 0.24 -0.60 0.76
outer loop
vertex -21.2 -24.8 40.5
vertex -10.8 -31.7 31.7
vertex -10.8 -23.5 38.3
endloop
endfacet
facet normal -0.08 0.62 -0.78
outer loop
vertex -10.8 -28.1 45.8
vertex 0 -27.6 45.1
vertex 0 -37.4 37.4
endloop
endfacet
facet normal -0.08 0.62 -0.78
outer loop
vertex -10.8 -28.1 45.8
vertex 0 -37.4 37.4
vertex -10.8 -38 38
endloop
endfacet
facet normal 0.08 -0.62 0.78
outer loop
vertex -10.8 -23.5 38.3
vertex -10.8 -31.7 31.7
vertex 0 -31.1 31.1
endloop
endfacet
facet normal 0.08 -0.62 0.78
outer loop
vertex -10.8 -23.5 38.3
vertex 0 -31.1 31.1
vertex 0 -23 37.5
endloop
endfacet
facet normal 0.10 0.62 -0.78
outer loop
vertex 0 -27.6 45.1
vertex 3.3 -27.8 45.4
vertex 3.3 -37.6 37.6
endloop
endfacet
facet normal 0.10 0.62 -0.78
outer loop
vertex 0 -27.6 45.1
vertex 3.3 -37.6 37.6
vertex 0 -37.4 37.4
endloop
endfacet
facet normal -0.10 -0.62 0.78
outer loop
vertex 0 -23 37.5
vertex 0 -31.1 31.1
vertex 3.3 -31.4 31.4
endloop
endfacet
facet normal -0.10 -0.62 0.78
outer loop
vertex 0 -23 37.5
vertex 3.3 -31.4 31.4
vertex 3.3 -23.2 37.8
endloop
endfacet
facet normal 0.29 0.59 -0.75
outer loop
vertex 3.3 -27.8 45.4
vertex 6.5 -28.3 46.2
vertex 6.5 -38.3 38.3
endloop
endfacet
facet normal 0.29 0.59 -0.75
outer loop
vertex 3.3 -27.8 45.4
vertex 6.5 -38.3 38.3
vertex 3.3 -37.6 37.6
endloop
endfacet
facet normal -0.29 -0.59 0.75
outer loop
vertex 3.3 -23.2 37.8
vertex 3.3 -31.4 31.4
vertex 6.5 -32 32
endloop
endfacet
facet normal -0.29 -0.59 0.75
outer loop
vertex 3.3 -23.2 37.8
vertex 6.5 -32 32
vertex 6.5 -23.7 38.6
endloop
endfacet
facet normal 0.44 0.55 -0.70
outer loop
vertex 6.5 -28.3 46.2
vertex 30.7 -34.6 56.5
vertex 30.7 -46.8 46.8
endloop
endfacet
facet normal 0.44 0.55 -0.70
outer loop
vertex 6.5 -28.3 46.2
vertex 30.7 -46.8 46.8
vertex 6.5 -38.3 38.3
endloop
endfacet
facet normal -0.44 -0.55 0.70
outer loop
vertex 6.5 -23.7 38.6
vertex 6.5 -32 32
vertex 30.7 -40.6 40.6
endloop
endfacet
facet normal -0.44 -0.55 0.70
outer loop
vertex 6.5 -23.7 38.6
vertex 30.7 -40.6 40.6
vertex 30.7 -30 48.9
endloop
endfacet
facet normal 0.42 0.56 -0.71
outer loop
vertex 30.7 -34.6 56.5
vertex 69.4 -44 71.8
vertex 69.4 -59.5 59.5
endloop
endfacet
facet normal 0.42 0.56 -0.71
outer loop
vertex 30.7 -34.6 56.5
vertex 69.4 -59.5 59.5
vertex 30.7 -46.8 46.8
endloop
endfacet
facet normal -0.42 -0.56 0.71
outer loop
vertex 30.7 -30 48.9
vertex 30.7 -40.6 40.6
vertex 69.4 -53.3 53.3
endloop
endfacet
facet normal -0.42 -0.56 0.71
outer loop
vertex 30.7 -30 48.9
vertex 69.4 -53.3 53.3
vertex 69.4 -39.4 64.2
endloop
endfacet
facet normal 0.38 0.57 -0.72
outer loop
vertex 69.4 -44 71.8
vertex 108.3 -52.5 85.7
vertex 108.3 -71.1 71.1
endloop
endfacet
facet normal 0.38 0.57 -0.72
outer loop
vertex 69.4 -44 71.8
vertex 108.3 -71.1 71.1
vertex 69.4 -59.5 59.5
endloop
endfacet
facet normal -0.38 -0.57 0.72
outer loop
vertex 69.4 -39.4 64.2
vertex 69.4 -53.3 53.3
vertex 108.3 -64.8 64.8
endloop
endfacet
facet normal -0.38 -0.57 0.72
outer loop
vertex 69.4 -39.4 64.2
vertex 108.3 -64.8 64.8
vertex 108.3 -47.9 78.2
endloop
endfacet
facet normal 0.35 0.58 -0.74
outer loop
vertex 108.3 -52.5 85.7
vertex 147.6 -60.2 98.3
vertex 147.6 -81.5 81.5
endloop
endfacet
facet normal 0.35 0.58 -0.74
outer loop
vertex 108.3 -52.5 85.7
vertex 147.6 -81.5 81.5
vertex 108.3 -71.1 71.1
endloop
endfacet
facet normal -0.35 -0.58 0.74
outer loop
vertex 108.3 -47.9 78.2
vertex 108.3 -64.8 64.8
vertex 147.6 -75.3 75.3
endloop
endfacet
facet normal -0.35 -0.58 0.74
outer loop
vertex 108.3 -47.9 78.2
vertex 147.6 -75.3 75.3
vertex 147.6 -55.6 90.8
endloop
endfacet
facet normal 0.31 0.59 -0.75
outer loop
vertex 147.6 -60.2 98.3
vertex 187.1 -67.1 109.5
vertex 187.1 -90.8 90.8
endloop
endfacet
facet normal 0.31 0.59 -0.75
outer loop
vertex 147.6 -60.2 98.3
vertex 187.1 -90.8 90.8
vertex 147.6 -81.5 81.5
endloop
endfacet
facet normal -0.31 -0.59 0.75
outer loop
vertex 147.6 -55.6 90.8
vertex 147.6 -75.3 75.3
vertex 187.1 -84.6 84.6
endloop
endfacet
facet normal -0.31 -0.59 0.75
outer loop
vertex 147.6 -55.6 90.8
vertex 187.1 -84.6 84.6
vertex 187.1 -62.5 102
endloop
endfacet
facet normal 0.28 0.59 -0.75
outer loop
vertex 187.1 -67.1 109.5
vertex 227 -73.2 119.4
vertex 227 -99 99
endloop
endfacet
facet normal 0.28 0.59 -0.75
outer loop
vertex 187.1 -67.1 109.5
vertex 227 -99 99
vertex 187.1 -90.8 90.8
endloop
endfacet
facet normal -0.28 -0.59 0.75
outer loop
vertex 187.1 -62.5 102
vertex 187.1 -84.6 84.6
vertex 227 -92.8 92.8
endloop
endfacet
facet normal -0.28 -0.59 0.75
outer loop
vertex 187.1 -62.5 102
vertex 227 -92.8 92.8
vertex 227 -68.5 111.9
endloop
endfacet
facet normal 0.24 0.60 -0.76
outer loop
vertex 227 -73.2 119.4
vertex 267.1 -78.4 127.9
vertex 267.1 -106.1 106.1
endloop
endfacet
facet normal 0.24 0.60 -0.76
outer loop
vertex 227 -73.2 119.4
vertex 267.1 -106.1 106.1
vertex 227 -99 99
endloop
endfacet
facet normal -0.24 -0.60 0.76
outer loop
vertex 227 -68.5 111.9
vertex 227 -92.8 92.8
vertex 267.1 -99.8 99.8
endloop
endfacet
facet normal -0.24 -0.60 0.76
outer loop
vertex 227 -68.5 111.9
vertex 267.1 -99.8 99.8
vertex 267.1 -73.8 120.4
endloop
endfacet
facet normal 0.20 0.61 -0.77
outer loop
vertex 267.1 -78.4 127.9
vertex 307.6 -82.8 135.1
vertex 307.6 -112 112
endloop
endfacet
facet normal 0.20 0.61 -0.77
outer loop
vertex 267.1 -78.4 127.9
vertex 307.6 -112 112
vertex 267.1 -106.1 106.1
endloop
endfacet
facet normal -0.20 -0.61 0.77
outer loop
vertex 267.1 -73.8 120.4
vertex 267.1 -99.8 99.8
vertex 307.6 -105.8 105.8
endloop
endfacet
facet normal -0.20 -0.61 0.77
outer loop
vertex 267.1 -73.8 120.4
vertex 307.6 -105.8 105.8
vertex 307.6 -78.1 127.5
endloop
endfacet
facet normal 0.18 0.61 -0.77
outer loop
vertex 307.6 -82.8 135.1
vertex 323.8 -84.3 137.5
vertex 323.8 -114.1 114.1
endloop
endfacet
facet normal 0.18 0.61 -0.77
outer loop
vertex 307.6 -82.8 135.1
vertex 323.8 -114.1 114.1
vertex 307.6 -112 112
endloop
endfacet
facet normal -0.18 -0.61 0.77
outer loop
vertex 307.6 -78.1 127.5
vertex 307.6 -105.8 105.8
vertex 323.8 -107.8 107.8
endloop
endfacet
facet normal -0.18 -0.61 0.77
outer loop
vertex 307.6 -78.1 127.5
vertex 323.8 -107.8 107.8
vertex 323.8 -79.7 130
endloop
endfacet
facet normal 0.00 0.79 -0.62
outer loop
vertex -393.4 -60.2 60.2
vertex -260.1 -60.2 60.2
vertex -260.1 -72.5 44.5
endloop
endfacet
facet normal 0.00 0.79 -0.62
outer loop
vertex -393.4 -60.2 60.2
vertex -260.1 -72.5 44.5
vertex -393.4 -72.5 44.5
endloop
endfacet
facet normal 0.00 -0.79 0.62
outer loop
vertex -393.4 -53.9 53.9
vertex -393.4 -65 39.8
vertex -260.1 -65 39.8
endloop
endfacet
facet normal 0.00 -0.79 0.62
outer loop
vertex -393.4 -53.9 53.9
vertex -260.1 -65 39.8
vertex -260.1 -53.9 53.9
endloop
endfacet
facet normal 0.00 0.79 -0.62
outer loop
vertex -260.1 -60.2 60.2
vertex -126.8 -60.2 60.2
vertex -126.8 -72.5 44.5
endloop
endfacet
facet normal 0.00 0.79 -0.62
outer loop
vertex -260.1 -60.2 60.2
vertex -126.8 -72.5 44.5
vertex -260.1 -72.5 44.5
endloop
endfacet
facet normal 0.00 -0.79 0.62
outer loop
vertex -260.1 -53.9 53.9
vertex -260.1 -65 39.8
vertex -126.8 -65 39.8
endloop
endfacet
facet normal 0.00 -0.79 0.62
outer loop
vertex -260.1 -53.9 53.9
vertex -126.8 -65 39.8
vertex -126.8 -53.9 53.9
endloop
endfacet
facet normal -0.09 0.78 -0.62
outer loop
vertex -126.8 -60.2 60.2
vertex -63.4 -56 56
vertex -63.4 -67.6 41.4
endloop
endfacet
facet normal -0.09 0.78 -0.62
outer loop
vertex -126.8 -60.2 60.2
vertex -63.4 -67.6 41.4
vertex -126.8 -72.5 44.5
endloop
endfacet
facet normal 0.09 -0.78 0.62
outer loop
vertex -126.8 -53.9 53.9
vertex -126.8 -65 39.8
vertex -63.4 -60 36.8
endloop
endfacet
facet normal 0.09 -0.78 0.62
outer loop
vertex -126.8 -53.9 53.9
vertex -63.4 -60 36.8
vertex -63.4 -49.8 49.8
endloop
endfacet
facet normal -0.50 0.68 -0.54
outer loop
vertex -63.4 -56 56
vertex -46.5 -49.1 49.1
vertex -46.5 -59.3 36.3
endloop
endfacet
facet normal -0.50 0.68 -0.54
outer loop
vertex -63.4 -56 56
vertex -46.5 -59.3 36.3
vertex -63.4 -67.6 41.4
endloop
endfacet
facet normal 0.50 -0.68 0.54
outer loop
vertex -63.4 -49.8 49.8
vertex -63.4 -60 36.8
vertex -46.5 -51.7 31.7
endloop
endfacet
facet normal 0.50 -0.68 0.54
outer loop
vertex -63.4 -49.8 49.8
vertex -46.5 -51.7 31.7
vertex -46.5 -42.9 42.9
endloop
endfacet
facet normal -0.50 0.68 -0.54
outer loop
vertex -46.5 -49.1 49.1
vertex -31.1 -42.9 42.9
vertex -31.1 -51.7 31.7
endloop
endfacet
facet normal -0.50 0.68 -0.54
outer loop
vertex -46.5 -49.1 49.1
vertex -31.1 -51.7 31.7
vertex -46.5 -59.3 36.3
endloop
endfacet
facet normal 0.50 -0.68 0.54
outer loop
vertex -46.5 -42.9 42.9
vertex -46.5 -51.7 31.7
vertex -31.1 -44.2 27.1
endloop
endfacet
facet normal 0.50 -0.68 0.54
outer loop
vertex -46.5 -42.9 42.9
vertex -31.1 -44.2 27.1
vertex -31.1 -36.6 36.6
endloop
endfacet
facet normal -0.40 0.72 -0.57
outer loop
vertex -31.1 -42.9 42.9
vertex -21.2 -39.9 39.9
vertex -21.2 -48.1 29.5
endloop
endfacet
facet normal -0.40 0.72 -0.57
outer loop
vertex -31.1 -42.9 42.9
vertex -21.2 -48.1 29.5
vertex -31.1 -51.7 31.7
endloop
endfacet
facet normal 0.40 -0.72 0.57
outer loop
vertex -31.1 -36.6 36.6
vertex -31.1 -44.2 27.1
vertex -21.2 -40.5 24.8
endloop
endfacet
facet normal 0.40 -0.72 0.57
outer loop
vertex -31.1 -36.6 36.6
vertex -21.2 -40.5 24.8
vertex -21.2 -33.6 33.6
endloop
endfacet
facet normal -0.24 0.76 -0.60
outer loop
vertex -21.2 -39.9 39.9
vertex -10.8 -38 38
vertex -10.8 -45.8 28.1
endloop
endfacet
facet normal -0.24 0.76 -0.60
outer loop
vertex -21.2 -39.9 39.9
vertex -10.8 -45.8 28.1
vertex -21.2 -48.1 29.5
endloop
endfacet
facet normal 0.24 -0.76 0.60
outer loop
vertex -21.2 -33.6 33.6
vertex -21.2 -40.5 24.8
vertex -10.8 -38.3 23.5
endloop
endfacet
facet normal 0.24 -0.76 0.60
outer loop
vertex -21.2 -33.6 33.6
vertex -10.8 -38.3 23.5
vertex -10.8 -31.7 31.7
endloop
endfacet
facet normal -0.08 0.78 -0.62
outer loop
vertex -10.8 -38 38
vertex 0 -37.4 37.4
vertex 0 -45.1 27.6
endloop
endfacet
facet normal -0.08 0.78 -0.62
outer loop
vertex -10.8 -38 38
vertex 0 -45.1 27.6
vertex -10.8 -45.8 28.1
endloop
endfacet
facet normal 0.08 -0.78 0.62
outer loop
vertex -10.8 -31.7 31.7
vertex -10.8 -38.3 23.5
vertex 0 -37.5 23
endloop
endfacet
facet normal 0.08 -0.78 0.62
outer loop
vertex -10.8 -31.7 31.7
vertex 0 -37.5 23
vertex 0 -31.1 31.1
endloop
endfacet
facet normal 0.10 0.78 -0.62
outer loop
vertex 0 -37.4 37.4
vertex 3.3 -37.6 37.6
vertex 3.3 -45.4 27.8
endloop
endfacet
facet normal 0.10 0.78 -0.62
outer loop
vertex 0 -37.4 37.4
vertex 3.3 -45.4 27.8
vertex 0 -45.1 27.6
endloop
endfacet
facet normal -0.10 -0.78 0.62
outer loop
vertex 0 -31.1 31.1
vertex 0 -37.5 23
vertex 3.3 -37.8 23.2
endloop
endfacet
facet normal -0.10 -0.78 0.62
outer loop
vertex 0 -31.1 31.1
vertex 3.3 -37.8 23.2
vertex 3.3 -31.4 31.4
endloop
endfacet
facet normal 0.29 0.75 -0.59
outer loop
vertex 3.3 -37.6 37.6
vertex 6.5 -38.3 38.3
vertex 6.5 -46.2 28.3
endloop
endfacet
facet normal 0.29 0.75 -0.59
outer loop
vertex 3.3 -37.6 37.6
vertex 6.5 -46.2 28.3
vertex 3.3 -45.4 27.8
endloop
endfacet
facet normal -0.29 -0.75 0.59
outer loop
vertex 3.3 -31.4 31.4
vertex 3.3 -37.8 23.2
vertex 6.5 -38.6 23.7
endloop
endfacet
facet normal -0.29 -0.75 0.59
outer loop
vertex 3.3 -31.4 31.4
vertex 6.5 -38.6 23.7
vertex 6.5 -32 32
endloop
endfacet
facet normal 0.44 0.70 -0.55
outer loop
vertex 6.5 -38.3 38.3
vertex 30.7 -46.8 46.8
vertex 30.7 -56.5 34.6
endloop
endfacet
facet normal 0.44 0.70 -0.55
outer loop
vertex 6.5 -38.3 38.3
vertex 30.7 -56.5 34.6
vertex 6.5 -46.2 28.3
endloop
endfacet
facet normal -0.44 -0.70 0.55
outer loop
vertex 6.5 -32 32
vertex 6.5 -38.6 23.7
vertex 30.7 -48.9 30
endloop
endfacet
facet normal -0.44 -0.70 0.55
outer loop
vertex 6.5 -32 32
vertex 30.7 -48.9 30
vertex 30.7 -40.6 40.6
endloop
endfacet
facet normal 0.42 0.71 -0.56
outer loop
vertex 30.7 -46.8 46.8
vertex 69.4 -59.5 59.5
vertex 69.4 -71.8 44
endloop
endfacet
facet normal 0.42 0.71 -0.56
outer loop
vertex 30.7 -46.8 46.8
vertex 69.4 -71.8 44
vertex 30.7 -56.5 34.6
endloop
endfacet
facet normal -0.42 -0.71 0.56
outer loop
vertex 30.7 -40.6 40.6
vertex 30.7 -48.9 30
vertex 69.4 -64.2 39.4
endloop
endfacet
facet normal -0.42 -0.71 0.56
outer loop
vertex 30.7 -40.6 40.6
vertex 69.4 -64.2 39.4
vertex 69.4 -53.3 53.3
endloop
endfacet
facet normal 0.38 0.72 -0.57
outer loop
vertex 69.4 -59.5 59.5
vertex 108.3 -71.1 71.1
vertex 108.3 -85.7 52.5
endloop
endfacet
facet normal 0.38 0.72 -0.57
outer loop
vertex 69.4 -59.5 59.5
vertex 108.3 -85.7 52.5
vertex 69.4 -71.8 44
endloop
endfacet
facet normal -0.38 -0.72 0.57
outer loop
vertex 69.4 -53.3 53.3
vertex 69.4 -64.2 39.4
vertex 108.3 -78.2 47.9
endloop
endfacet
facet normal -0.38 -0.72 0.57
outer loop
vertex 69.4 -53.3 53.3
vertex 108.3 -78.2 47.9
vertex 108.3 -64.8 64.8
endloop
endfacet
facet normal 0.35 0.74 -0.58
outer loop
vertex 108.3 -71.1 71.1
vertex 147.6 -81.5 81.5
vertex 147.6 -98.3 60.2
endloop
endfacet
facet normal 0.35 0.74 -0.58
outer loop
vertex 108.3 -71.1 71.1
vertex 147.6 -98.3 60.2
vertex 108.3 -85.7 52.5
endloop
endfacet
facet normal -0.35 -0.74 0.58
outer loop
vertex 108.3 -64.8 64.8
vertex 108.3 -78.2 47.9
vertex 147.6 -90.8 55.6
endloop
endfacet
facet normal -0.35 -0.74 0.58
outer loop
vertex 108.3 -64.8 64.8
vertex 147.6 -90.8 55.6
vertex 147.6 -75.3 75.3
endloop
endfacet
facet normal 0.31 0.75 -0.59
outer loop
vertex 147.6 -81.5 81.5
vertex 187.1 -90.8 90.8
vertex 187.1 -109.5 67.1
endloop
endfacet
facet normal 0.31 0.75 -0.59
outer loop
vertex 147.6 -81.5 81.5
vertex 187.1 -109.5 67.1
vertex 147.6 -98.3 60.2
endloop
endfacet
facet normal -0.31 -0.75 0.59
outer loop
vertex 147.6 -75.3 75.3
vertex 147.6 -90.8 55.6
vertex 187.1 -102 62.5
endloop
endfacet
facet normal -0.31 -0.75 0.59
outer loop
vertex 147.6 -75.3 75.3
vertex 187.1 -102 62.5
vertex 187.1 -84.6 84.6
endloop
endfacet
facet normal 0.28 0.75 -0.59
outer loop
vertex 187.1 -90.8 90.8
vertex 227 -99 99
vertex 227 -119.4 73.2
endloop
endfacet
facet normal 0.28 0.75 -0.59
outer loop
vertex 187.1 -90.8 90.8
vertex 227 -119.4 73.2
vertex 187.1 -109.5 67.1
endloop
endfacet
facet normal -0.28 -0.75 0.59
outer loop
vertex 187.1 -84.6 84.6
vertex 187.1 -102 62.5
vertex 227 -111.9 68.5
endloop
endfacet
facet normal -0.28 -0.75 0.59
outer loop
vertex 187.1 -84.6 84.6
vertex 227 -111.9 68.5
vertex 227 -92.8 92.8
endloop
endfacet
facet normal 0.24 0.76 -0.60
outer loop
vertex 227 -99 99
vertex 267.1 -106.1 106.1
vertex 267.1 -127.9 78.4
endloop
endfacet
facet normal 0.24 0.76 -0.60
outer loop
vertex 227 -99 99
vertex 267.1 -127.9 78.4
vertex 227 -119.4 73.2
endloop
endfacet
facet normal -0.24 -0.76 0.60
outer loop
vertex 227 -92.8 92.8
vertex 227 -111.9 68.5
vertex 267.1 -120.4 73.8
endloop
endfacet
facet normal -0.24 -0.76 0.60
outer loop
vertex 227 -92.8 92.8
vertex 267.1 -120.4 73.8
vertex 267.1 -99.8 99.8
endloop
endfacet
facet normal 0.20 0.77 -0.61
outer loop
vertex 267.1 -106.1 106.1
vertex 307.6 -112 112
vertex 307.6 -135.1 82.8
endloop
endfacet
facet normal 0.20 0.77 -0.61
outer loop
vertex 267.1 -106.1 106.1
vertex 307.6 -135.1 82.8
vertex 267.1 -127.9 78.4
endloop
endfacet
facet normal -0.20 -0.77 0.61
outer loop
vertex 267.1 -99.8 99.8
vertex 267.1 -120.4 73.8
vertex 307.6 -127.5 78.1
endloop
endfacet
facet normal -0.20 -0.77 0.61
outer loop
vertex 267.1 -99.8 99.8
vertex 307.6 -127.5 78.1
vertex 307.6 -105.8 105.8
endloop
endfacet
facet normal 0.18 0.77 -0.61
outer loop
vertex 307.6 -112 112
vertex 323.8 -114.1 114.1
vertex 323.8 -137.5 84.3
endloop
endfacet
facet normal 0.18 0.77 -0.61
outer loop
vertex 307.6 -112 112
vertex 323.8 -137.5 84.3
vertex 307.6 -135.1 82.8
endloop
endfacet
facet normal -0.18 -0.77 0.61
outer loop
vertex 307.6 -105.8 105.8
vertex 307.6 -127.5 78.1
vertex 323.8 -130 79.7
endloop
endfacet
facet normal -0.18 -0.77 0.61
outer loop
vertex 307.6 -105.8 105.8
vertex 323.8 -130 79.7
vertex 323.8 -107.8 107.8
endloop
endfacet
facet normal 0.00 0.91 -0.42
outer loop
vertex -393.4 -72.5 44.5
vertex -260.1 -72.5 44.5
vertex -260.1 -80.9 26.3
endloop
endfacet
facet normal 0.00 0.91 -0.42
outer loop
vertex -393.4 -72.5 44.5
vertex -260.1 -80.9 26.3
vertex -393.4 -80.9 26.3
endloop
endfacet
facet normal 0.00 -0.91 0.42
outer loop
vertex -393.4 -65 39.8
vertex -393.4 -72.5 23.6
vertex -260.1 -72.5 23.6
endloop
endfacet
facet normal 0.00 -0.91 0.42
outer loop
vertex -393.4 -65 39.8
vertex -260.1 -72.5 23.6
vertex -260.1 -65 39.8
endloop
endfacet
facet normal 0.00 0.91 -0.42
outer loop
vertex -260.1 -72.5 44.5
vertex -126.8 -72.5 44.5
vertex -126.8 -80.9 26.3
endloop
endfacet
facet normal 0.00 0.91 -0.42
outer loop
vertex -260.1 -72.5 44.5
vertex -126.8 -80.9 26.3
vertex -260.1 -80.9 26.3
endloop
endfacet
facet normal 0.00 -0.91 0.42
outer loop
vertex -260.1 -65 39.8
vertex -260.1 -72.5 23.6
vertex -126.8 -72.5 23.6
endloop
endfacet
facet normal 0.00 -0.91 0.42
outer loop
vertex -260.1 -65 39.8
vertex -126.8 -72.5 23.6
vertex -126.8 -65 39.8
endloop
endfacet
facet normal -0.09 0.90 -0.42
outer loop
vertex -126.8 -72.5 44.5
vertex -63.4 -67.6 41.4
vertex -63.4 -75.4 24.5
endloop
endfacet
facet normal -0.09 0.90 -0.42
outer loop
vertex -126.8 -72.5 44.5
vertex -63.4 -75.4 24.5
vertex -126.8 -80.9 26.3
endloop
endfacet
facet normal 0.09 -0.90 0.42
outer loop
vertex -126.8 -65 39.8
vertex -126.8 -72.5 23.6
vertex -63.4 -66.9 21.8
endloop
endfacet
facet normal 0.09 -0.90 0.42
outer loop
vertex -126.8 -65 39.8
vertex -63.4 -66.9 21.8
vertex -63.4 -60 36.8
endloop
endfacet
facet normal -0.50 0.79 -0.36
outer loop
vertex -63.4 -67.6 41.4
vertex -46.5 -59.3 36.3
vertex -46.5 -66.1 21.5
endloop
endfacet
facet normal -0.50 0.79 -0.36
outer loop
vertex -63.4 -67.6 41.4
vertex -46.5 -66.1 21.5
vertex -63.4 -75.4 24.5
endloop
endfacet
facet normal 0.50 -0.79 0.36
outer loop
vertex -63.4 -60 36.8
vertex -63.4 -66.9 21.8
vertex -46.5 -57.7 18.7
endloop
endfacet
facet normal 0.50 -0.79 0.36
outer loop
vertex -63.4 -60 36.8
vertex -46.5 -57.7 18.7
vertex -46.5 -51.7 31.7
endloop
endfacet
facet normal -0.50 0.79 -0.36
outer loop
vertex -46.5 -59.3 36.3
vertex -31.1 -51.7 31.7
vertex -31.1 -57.7 18.7
endloop
endfacet
facet normal -0.50 0.79 -0.36
outer loop
vertex -46.5 -59.3 36.3
vertex -31.1 -57.7 18.7
vertex -46.5 -66.1 21.5
endloop
endfacet
facet normal 0.50 -0.79 0.36
outer loop
vertex -46.5 -51.7 31.7
vertex -46.5 -57.7 18.7
vertex -31.1 -49.3 16
endloop
endfacet
facet normal 0.50 -0.79 0.36
outer loop
vertex -46.5 -51.7 31.7
vertex -31.1 -49.3 16
vertex -31.1 -44.2 27.1
endloop
endfacet
facet normal -0.40 0.83 -0.38
outer loop
vertex -31.1 -51.7 31.7
vertex -21.2 -48.1 29.5
vertex -21.2 -53.6 17.4
endloop
endfacet
facet normal -0.40 0.83 -0.38
outer loop
vertex -31.1 -51.7 31.7
vertex -21.2 -53.6 17.4
vertex -31.1 -57.7 18.7
endloop
endfacet
facet normal 0.40 -0.83 0.38
outer loop
vertex -31.1 -44.2 27.1
vertex -31.1 -49.3 16
vertex -21.2 -45.2 14.7
endloop
endfacet
facet normal 0.40 -0.83 0.38
outer loop
vertex -31.1 -44.2 27.1
vertex -21.2 -45.2 14.7
vertex -21.2 -40.5 24.8
endloop
endfacet
facet normal -0.24 0.88 -0.41
outer loop
vertex -21.2 -48.1 29.5
vertex -10.8 -45.8 28.1
vertex -10.8 -51.1 16.6
endloop
endfacet
facet normal -0.24 0.88 -0.41
outer loop
vertex -21.2 -48.1 29.5
vertex -10.8 -51.1 16.6
vertex -21.2 -53.6 17.4
endloop
endfacet
facet normal 0.24 -0.88 0.41
outer loop
vertex -21.2 -40.5 24.8
vertex -21.2 -45.2 14.7
vertex -10.8 -42.7 13.9
endloop
endfacet
facet normal 0.24 -0.88 0.41
outer loop
vertex -21.2 -40.5 24.8
vertex -10.8 -42.7 13.9
vertex -10.8 -38.3 23.5
endloop
endfacet
facet normal -0.08 0.91 -0.42
outer loop
vertex -10.8 -45.8 28.1
vertex 0 -45.1 27.6
vertex 0 -50.3 16.3
endloop
endfacet
facet normal -0.08 0.91 -0.42
outer loop
vertex -10.8 -45.8 28.1
vertex 0 -50.3 16.3
vertex -10.8 -51.1 16.6
endloop
endfacet
facet normal 0.08 -0.91 0.42
outer loop
vertex -10.8 -38.3 23.5
vertex -10.8 -42.7 13.9
vertex 0 -41.9 13.6
endloop
endfacet
facet normal 0.08 -0.91 0.42
outer loop
vertex -10.8 -38.3 23.5
vertex 0 -41.9 13.6
vertex 0 -37.5 23
endloop
endfacet
facet normal 0.10 0.90 -0.42
outer loop
vertex 0 -45.1 27.6
vertex 3.3 -45.4 27.8
vertex 3.3 -50.6 16.4
endloop
endfacet
facet normal 0.10 0.90 -0.42
outer loop
vertex 0 -45.1 27.6
vertex 3.3 -50.6 16.4
vertex 0 -50.3 16.3
endloop
endfacet
facet normal -0.10 -0.90 0.42
outer loop
vertex 0 -37.5 23
vertex 0 -41.9 13.6
vertex 3.3 -42.2 13.7
endloop
endfacet
facet normal -0.10 -0.90 0.42
outer loop
vertex 0 -37.5 23
vertex 3.3 -42.2 13.7
vertex 3.3 -37.8 23.2
endloop
endfacet
facet normal 0.29 0.87 -0.40
outer loop
vertex 3.3 -45.4 27.8
vertex 6.5 -46.2 28.3
vertex 6.5 -51.5 16.7
endloop
endfacet
facet normal 0.29 0.87 -0.40
outer loop
vertex 3.3 -45.4 27.8
vertex 6.5 -51.5 16.7
vertex 3.3 -50.6 16.4
endloop
endfacet
facet normal -0.29 -0.87 0.40
outer loop
vertex 3.3 -37.8 23.2
vertex 3.3 -42.2 13.7
vertex 6.5 -43.1 14
endloop
endfacet
facet normal -0.29 -0.87 0.40
outer loop
vertex 3.3 -37.8 23.2
vertex 6.5 -43.1 14
vertex 6.5 -38.6 23.7
endloop
endfacet
facet normal 0.44 0.81 -0.38
outer loop
vertex 6.5 -46.2 28.3
vertex 30.7 -56.5 34.6
vertex 30.7 -63 20.5
endloop
endfacet
facet normal 0.44 0.81 -0.38
outer loop
vertex 6.5 -46.2 28.3
vertex 30.7 -63 20.5
vertex 6.5 -51.5 16.7
endloop
endfacet
facet normal -0.44 -0.81 0.38
outer loop
vertex 6.5 -38.6 23.7
vertex 6.5 -43.1 14
vertex 30.7 -54.6 17.7
endloop
endfacet
facet normal -0.44 -0.81 0.38
outer loop
vertex 6.5 -38.6 23.7
vertex 30.7 -54.6 17.7
vertex 30.7 -48.9 30
endloop
endfacet
facet normal 0.42 0.82 -0.38
outer loop
vertex 30.7 -56.5 34.6
vertex 69.4 -71.8 44
vertex 69.4 -80.1 26
endloop
endfacet
facet normal 0.42 0.82 -0.38
outer loop
vertex 30.7 -56.5 34.6
vertex 69.4 -80.1 26
vertex 30.7 -63 20.5
endloop
endfacet
facet normal -0.42 -0.82 0.38
outer loop
vertex 30.7 -48.9 30
vertex 30.7 -54.6 17.7
vertex 69.4 -71.7 23.3
endloop
endfacet
facet normal -0.42 -0.82 0.38
outer loop
vertex 30.7 -48.9 30
vertex 69.4 -71.7 23.3
vertex 69.4 -64.2 39.4
endloop
endfacet
facet normal 0.38 0.84 -0.39
outer loop
vertex 69.4 -71.8 44
vertex 108.3 -85.7 52.5
vertex 108.3 -95.6 31.1
endloop
endfacet
facet normal 0.38 0.84 -0.39
outer loop
vertex 69.4 -71.8 44
vertex 108.3 -95.6 31.1
vertex 69.4 -80.1 26
endloop
endfacet
facet normal -0.38 -0.84 0.39
outer loop
vertex 69.4 -64.2 39.4
vertex 69.4 -71.7 23.3
vertex 108.3 -87.2 28.3
endloop
endfacet
facet normal -0.38 -0.84 0.39
outer loop
vertex 69.4 -64.2 39.4
vertex 108.3 -87.2 28.3
vertex 108.3 -78.2 47.9
endloop
endfacet
facet normal 0.35 0.85 -0.39
outer loop
vertex 108.3 -85.7 52.5
vertex 147.6 -98.3 60.2
vertex 147.6 -109.6 35.6
endloop
endfacet
facet normal 0.35 0.85 -0.39
outer loop
vertex 108.3 -85.7 52.5
vertex 147.6 -109.6 35.6
vertex 108.3 -95.6 31.1
endloop
endfacet
facet normal -0.35 -0.85 0.39
outer loop
vertex 108.3 -78.2 47.9
vertex 108.3 -87.2 28.3
vertex 147.6 -101.2 32.9
endloop
endfacet
facet normal -0.35 -0.85 0.39
outer loop
vertex 108.3 -78.2 47.9
vertex 147.6 -101.2 32.9
vertex 147.6 -90.8 55.6
endloop
endfacet
facet normal 0.31 0.86 -0.40
outer loop
vertex 147.6 -98.3 60.2
vertex 187.1 -109.5 67.1
vertex 187.1 -122.2 39.7
endloop
endfacet
facet normal 0.31 0.86 -0.40
outer loop
vertex 147.6 -98.3 60.2
vertex 187.1 -122.2 39.7
vertex 147.6 -109.6 35.6
endloop
endfacet
facet normal -0.31 -0.86 0.40
outer loop
vertex 147.6 -90.8 55.6
vertex 147.6 -101.2 32.9
vertex 187.1 -113.8 37
endloop
endfacet
facet normal -0.31 -0.86 0.40
outer loop
vertex 147.6 -90.8 55.6
vertex 187.1 -113.8 37
vertex 187.1 -102 62.5
endloop
endfacet
facet normal 0.28 0.87 -0.40
outer loop
vertex 187.1 -109.5 67.1
vertex 227 -119.4 73.2
vertex 227 -133.2 43.3
endloop
endfacet
facet normal 0.28 0.87 -0.40
outer loop
vertex 187.1 -109.5 67.1
vertex 227 -133.2 43.3
vertex 187.1 -122.2 39.7
endloop
endfacet
facet normal -0.28 -0.87 0.40
outer loop
vertex 187.1 -102 62.5
vertex 187.1 -113.8 37
vertex 227 -124.8 40.5
endloop
endfacet
facet normal -0.28 -0.87 0.40
outer loop
vertex 187.1 -102 62.5
vertex 227 -124.8 40.5
vertex 227 -111.9 68.5
endloop
endfacet
facet normal 0.24 0.88 -0.41
outer loop
vertex 227 -119.4 73.2
vertex 267.1 -127.9 78.4
vertex 267.1 -142.7 46.4
endloop
endfacet
facet normal 0.24 0.88 -0.41
outer loop
vertex 227 -119.4 73.2
vertex 267.1 -142.7 46.4
vertex 227 -133.2 43.3
endloop
endfacet
facet normal -0.24 -0.88 0.41
outer loop
vertex 227 -111.9 68.5
vertex 227 -124.8 40.5
vertex 267.1 -134.3 43.6
endloop
endfacet
facet normal -0.24 -0.88 0.41
outer loop
vertex 227 -111.9 68.5
vertex 267.1 -134.3 43.6
vertex 267.1 -120.4 73.8
endloop
endfacet
facet normal 0.20 0.89 -0.41
outer loop
vertex 267.1 -127.9 78.4
vertex 307.6 -135.1 82.8
vertex 307.6 -150.7 49
endloop
endfacet
facet normal 0.20 0.89 -0.41
outer loop
vertex 267.1 -127.9 78.4
vertex 307.6 -150.7 49
vertex 267.1 -142.7 46.4
endloop
endfacet
facet normal -0.20 -0.89 0.41
outer loop
vertex 267.1 -120.4 73.8
vertex 267.1 -134.3 43.6
vertex 307.6 -142.2 46.2
endloop
endfacet
facet normal -0.20 -0.89 0.41
outer loop
vertex 267.1 -120.4 73.8
vertex 307.6 -142.2 46.2
vertex 307.6 -127.5 78.1
endloop
endfacet
facet normal 0.18 0.89 -0.41
outer loop
vertex 307.6 -135.1 82.8
vertex 323.8 -137.5 84.3
vertex 323.8 -153.4 49.9
endloop
endfacet
facet normal 0.18 0.89 -0.41
outer loop
vertex 307.6 -135.1 82.8
vertex 323.8 -153.4 49.9
vertex 307.6 -150.7 49
endloop
endfacet
facet normal -0.18 -0.89 0.41
outer loop
vertex 307.6 -127.5 78.1
vertex 307.6 -142.2 46.2
vertex 323.8 -145 47.1
endloop
endfacet
facet normal -0.18 -0.89 0.41
outer loop
vertex 307.6 -127.5 78.1
vertex 323.8 -145 47.1
vertex 323.8 -130 79.7
endloop
endfacet
facet normal 0.00 0.98 -0.20
outer loop
vertex -393.4 -80.9 26.3
vertex -260.1 -80.9 26.3
vertex -260.1 -84.8 6.7
endloop
endfacet
facet normal 0.00 0.98 -0.20
outer loop
vertex -393.4 -80.9 26.3
vertex -260.1 -84.8 6.7
vertex -393.4 -84.8 6.7
endloop
endfacet
facet normal 0.00 -0.98 0.20
outer loop
vertex -393.4 -72.5 23.6
vertex -393.4 -76 6
vertex -260.1 -76 6
endloop
endfacet
facet normal 0.00 -0.98 0.20
outer loop
vertex -393.4 -72.5 23.6
vertex -260.1 -76 6
vertex -260.1 -72.5 23.6
endloop
endfacet
facet normal 0.00 0.98 -0.20
outer loop
vertex -260.1 -80.9 26.3
vertex -126.8 -80.9 26.3
vertex -126.8 -84.8 6.7
endloop
endfacet
facet normal 0.00 0.98 -0.20
outer loop
vertex -260.1 -80.9 26.3
vertex -126.8 -84.8 6.7
vertex -260.1 -84.8 6.7
endloop
endfacet
facet normal 0.00 -0.98 0.20
outer loop
vertex -260.1 -72.5 23.6
vertex -260.1 -76 6
vertex -126.8 -76 6
endloop
endfacet
facet normal 0.00 -0.98 0.20
outer loop
vertex -260.1 -72.5 23.6
vertex -126.8 -76 6
vertex -126.8 -72.5 23.6
endloop
endfacet
facet normal -0.09 0.98 -0.19
outer loop
vertex -126.8 -80.9 26.3
vertex -63.4 -75.4 24.5
vertex -63.4 -79 6.2
endloop
endfacet
facet normal -0.09 0.98 -0.19
outer loop
vertex -126.8 -80.9 26.3
vertex -63.4 -79 6.2
vertex -126.8 -84.8 6.7
endloop
endfacet
facet normal 0.09 -0.98 0.19
outer loop
vertex -126.8 -72.5 23.6
vertex -126.8 -76 6
vertex -63.4 -70.2 5.5
endloop
endfacet
facet normal 0.09 -0.98 0.19
outer loop
vertex -126.8 -72.5 23.6
vertex -63.4 -70.2 5.5
vertex -63.4 -66.9 21.8
endloop
endfacet
facet normal -0.50 0.85 -0.17
outer loop
vertex -63.4 -75.4 24.5
vertex -46.5 -66.1 21.5
vertex -46.5 -69.3 5.5
endloop
endfacet
facet normal -0.50 0.85 -0.17
outer loop
vertex -63.4 -75.4 24.5
vertex -46.5 -69.3 5.5
vertex -63.4 -79 6.2
endloop
endfacet
facet normal 0.50 -0.85 0.17
outer loop
vertex -63.4 -66.9 21.8
vertex -63.4 -70.2 5.5
vertex -46.5 -60.5 4.8
endloop
endfacet
facet normal 0.50 -0.85 0.17
outer loop
vertex -63.4 -66.9 21.8
vertex -46.5 -60.5 4.8
vertex -46.5 -57.7 18.7
endloop
endfacet
facet normal -0.50 0.85 -0.17
outer loop
vertex -46.5 -66.1 21.5
vertex -31.1 -57.7 18.7
vertex -31.1 -60.5 4.8
endloop
endfacet
facet normal -0.50 0.85 -0.17
outer loop
vertex -46.5 -66.1 21.5
vertex -31.1 -60.5 4.8
vertex -46.5 -69.3 5.5
endloop
endfacet
facet normal 0.50 -0.85 0.17
outer loop
vertex -46.5 -57.7 18.7
vertex -46.5 -60.5 4.8
vertex -31.1 -51.7 4.1
endloop
endfacet
facet normal 0.50 -0.85 0.17
outer loop
vertex -46.5 -57.7 18.7
vertex -31.1 -51.7 4.1
vertex -31.1 -49.3 16
endloop
endfacet
facet normal -0.40 0.90 -0.18
outer loop
vertex -31.1 -57.7 18.7
vertex -21.2 -53.6 17.4
vertex -21.2 -56.2 4.4
endloop
endfacet
facet normal -0.40 0.90 -0.18
outer loop
vertex -31.1 -57.7 18.7
vertex -21.2 -56.2 4.4
vertex -31.1 -60.5 4.8
endloop
endfacet
facet normal 0.40 -0.90 0.18
outer loop
vertex -31.1 -49.3 16
vertex -31.1 -51.7 4.1
vertex -21.2 -47.4 3.7
endloop
endfacet
facet normal 0.40 -0.90 0.18
outer loop
vertex -31.1 -49.3 16
vertex -21.2 -47.4 3.7
vertex -21.2 -45.2 14.7
endloop
endfacet
facet normal -0.24 0.95 -0.19
outer loop
vertex -21.2 -53.6 17.4
vertex -10.8 -51.1 16.6
vertex -10.8 -53.6 4.2
endloop
endfacet
facet normal -0.24 0.95 -0.19
outer loop
vertex -21.2 -53.6 17.4
vertex -10.8 -53.6 4.2
vertex -21.2 -56.2 4.4
endloop
endfacet
facet normal 0.24 -0.95 0.19
outer loop
vertex -21.2 -45.2 14.7
vertex -21.2 -47.4 3.7
vertex -10.8 -44.8 3.5
endloop
endfacet
facet normal 0.24 -0.95 0.19
outer loop
vertex -21.2 -45.2 14.7
vertex -10.8 -44.8 3.5
vertex -10.8 -42.7 13.9
endloop
endfacet
facet normal -0.08 0.98 -0.19
outer loop
vertex -10.8 -51.1 16.6
vertex 0 -50.3 16.3
vertex 0 -52.7 4.1
endloop
endfacet
facet normal -0.08 0.98 -0.19
outer loop
vertex -10.8 -51.1 16.6
vertex 0 -52.7 4.1
vertex -10.8 -53.6 4.2
endloop
endfacet
facet normal 0.08 -0.98 0.19
outer loop
vertex -10.8 -42.7 13.9
vertex -10.8 -44.8 3.5
vertex 0 -43.9 3.5
endloop
endfacet
facet normal 0.08 -0.98 0.19
outer loop
vertex -10.8 -42.7 13.9
vertex 0 -43.9 3.5
vertex 0 -41.9 13.6
endloop
endfacet
facet normal 0.10 0.98 -0.19
outer loop
vertex 0 -50.3 16.3
vertex 3.3 -50.6 16.4
vertex 3.3 -53 4.2
endloop
endfacet
facet normal 0.10 0.98 -0.19
outer loop
vertex 0 -50.3 16.3
vertex 3.3 -53 4.2
vertex 0 -52.7 4.1
endloop
endfacet
facet normal -0.10 -0.98 0.19
outer loop
vertex 0 -41.9 13.6
vertex 0 -43.9 3.5
vertex 3.3 -44.2 3.5
endloop
endfacet
facet normal -0.10 -0.98 0.19
outer loop
vertex 0 -41.9 13.6
vertex 3.3 -44.2 3.5
vertex 3.3 -42.2 13.7
endloop
endfacet
facet normal 0.29 0.94 -0.19
outer loop
vertex 3.3 -50.6 16.4
vertex 6.5 -51.5 16.7
vertex 6.5 -54 4.2
endloop
endfacet
facet normal 0.29 0.94 -0.19
outer loop
vertex 3.3 -50.6 16.4
vertex 6.5 -54 4.2
vertex 3.3 -53 4.2
endloop
endfacet
facet normal -0.29 -0.94 0.19
outer loop
vertex 3.3 -42.2 13.7
vertex 3.3 -44.2 3.5
vertex 6.5 -45.2 3.6
endloop
endfacet
facet normal -0.29 -0.94 0.19
outer loop
vertex 3.3 -42.2 13.7
vertex 6.5 -45.2 3.6
vertex 6.5 -43.1 14
endloop
endfacet
facet normal 0.44 0.88 -0.17
outer loop
vertex 6.5 -51.5 16.7
vertex 30.7 -63 20.5
vertex 30.7 -66 5.2
endloop
endfacet
facet normal 0.44 0.88 -0.17
outer loop
vertex 6.5 -51.5 16.7
vertex 30.7 -66 5.2
vertex 6.5 -54 4.2
endloop
endfacet
facet normal -0.44 -0.88 0.17
outer loop
vertex 6.5 -43.1 14
vertex 6.5 -45.2 3.6
vertex 30.7 -57.2 4.5
endloop
endfacet
facet normal -0.44 -0.88 0.17
outer loop
vertex 6.5 -43.1 14
vertex 30.7 -57.2 4.5
vertex 30.7 -54.6 17.7
endloop
endfacet
facet normal 0.42 0.89 -0.18
outer loop
vertex 30.7 -63 20.5
vertex 69.4 -80.1 26
vertex 69.4 -83.9 6.6
endloop
endfacet
facet normal 0.42 0.89 -0.18
outer loop
vertex 30.7 -63 20.5
vertex 69.4 -83.9 6.6
vertex 30.7 -66 5.2
endloop
endfacet
facet normal -0.42 -0.89 0.18
outer loop
vertex 30.7 -54.6 17.7
vertex 30.7 -57.2 4.5
vertex 69.4 -75.1 5.9
endloop
endfacet
facet normal -0.42 -0.89 0.18
outer loop
vertex 30.7 -54.6 17.7
vertex 69.4 -75.1 5.9
vertex 69.4 -71.7 23.3
endloop
endfacet
facet normal 0.38 0.91 -0.18
outer loop
vertex 69.4 -80.1 26
vertex 108.3 -95.6 31.1
vertex 108.3 -100.2 7.9
endloop
endfacet
facet normal 0.38 0.91 -0.18
outer loop
vertex 69.4 -80.1 26
vertex 108.3 -100.2 7.9
vertex 69.4 -83.9 6.6
endloop
endfacet
facet normal -0.38 -0.91 0.18
outer loop
vertex 69.4 -71.7 23.3
vertex 69.4 -75.1 5.9
vertex 108.3 -91.4 7.2
endloop
endfacet
facet normal -0.38 -0.91 0.18
outer loop
vertex 69.4 -71.7 23.3
vertex 108.3 -91.4 7.2
vertex 108.3 -87.2 28.3
endloop
endfacet
facet normal 0.35 0.92 -0.18
outer loop
vertex 108.3 -95.6 31.1
vertex 147.6 -109.6 35.6
vertex 147.6 -114.9 9
endloop
endfacet
facet normal 0.35 0.92 -0.18
outer loop
vertex 108.3 -95.6 31.1
vertex 147.6 -114.9 9
vertex 108.3 -100.2 7.9
endloop
endfacet
facet normal -0.35 -0.92 0.18
outer loop
vertex 108.3 -87.2 28.3
vertex 108.3 -91.4 7.2
vertex 147.6 -106.1 8.4
endloop
endfacet
facet normal -0.35 -0.92 0.18
outer loop
vertex 108.3 -87.2 28.3
vertex 147.6 -106.1 8.4
vertex 147.6 -101.2 32.9
endloop
endfacet
facet normal 0.31 0.93 -0.19
outer loop
vertex 147.6 -109.6 35.6
vertex 187.1 -122.2 39.7
vertex 187.1 -128.1 10.1
endloop
endfacet
facet normal 0.31 0.93 -0.19
outer loop
vertex 147.6 -109.6 35.6
vertex 187.1 -128.1 10.1
vertex 147.6 -114.9 9
endloop
endfacet
facet normal -0.31 -0.93 0.19
outer loop
vertex 147.6 -101.2 32.9
vertex 147.6 -106.1 8.4
vertex 187.1 -119.2 9.4
endloop
endfacet
facet normal -0.31 -0.93 0.19
outer loop
vertex 147.6 -101.2 32.9
vertex 187.1 -119.2 9.4
vertex 187.1 -113.8 37
endloop
endfacet
facet normal 0.28 0.94 -0.19
outer loop
vertex 187.1 -122.2 39.7
vertex 227 -133.2 43.3
vertex 227 -139.6 11
endloop
endfacet
facet normal 0.28 0.94 -0.19
outer loop
vertex 187.1 -122.2 39.7
vertex 227 -139.6 11
vertex 187.1 -128.1 10.1
endloop
endfacet
facet normal -0.28 -0.94 0.19
outer loop
vertex 187.1 -113.8 37
vertex 187.1 -119.2 9.4
vertex 227 -130.8 10.3
endloop
endfacet
facet normal -0.28 -0.94 0.19
outer loop
vertex 187.1 -113.8 37
vertex 227 -130.8 10.3
vertex 227 -124.8 40.5
endloop
endfacet
facet normal 0.24 0.95 -0.19
outer loop
vertex 227 -133.2 43.3
vertex 267.1 -142.7 46.4
vertex 267.1 -149.6 11.8
endloop
endfacet
facet normal 0.24 0.95 -0.19
outer loop
vertex 227 -133.2 43.3
vertex 267.1 -149.6 11.8
vertex 227 -139.6 11
endloop
endfacet
facet normal -0.24 -0.95 0.19
outer loop
vertex 227 -124.8 40.5
vertex 227 -130.8 10.3
vertex 267.1 -140.7 11.1
endloop
endfacet
facet normal -0.24 -0.95 0.19
outer loop
vertex 227 -124.8 40.5
vertex 267.1 -140.7 11.1
vertex 267.1 -134.3 43.6
endloop
endfacet
facet normal 0.20 0.96 -0.19
outer loop
vertex 267.1 -142.7 46.4
vertex 307.6 -150.7 49
vertex 307.6 -157.9 12.4
endloop
endfacet
facet normal 0.20 0.96 -0.19
outer loop
vertex 267.1 -142.7 46.4
vertex 307.6 -157.9 12.4
vertex 267.1 -149.6 11.8
endloop
endfacet
facet normal -0.20 -0.96 0.19
outer loop
vertex 267.1 -134.3 43.6
vertex 267.1 -140.7 11.1
vertex 307.6 -149.1 11.7
endloop
endfacet
facet normal -0.20 -0.96 0.19
outer loop
vertex 267.1 -134.3 43.6
vertex 307.6 -149.1 11.7
vertex 307.6 -142.2 46.2
endloop
endfacet
facet normal 0.18 0.97 -0.19
outer loop
vertex 307.6 -150.7 49
vertex 323.8 -153.4 49.9
vertex 323.8 -160.8 12.7
endloop
endfacet
facet normal 0.18 0.97 -0.19
outer loop
vertex 307.6 -150.7 49
vertex 323.8 -160.8 12.7
vertex 307.6 -157.9 12.4
endloop
endfacet
facet normal -0.18 -0.97 0.19
outer loop
vertex 307.6 -142.2 46.2
vertex 307.6 -149.1 11.7
vertex 323.8 -152 12
endloop
endfacet
facet normal -0.18 -0.97 0.19
outer loop
vertex 307.6 -142.2 46.2
vertex 323.8 -152 12
vertex 323.8 -145 47.1
endloop
endfacet
facet normal 0.00 1.00 0.04
outer loop
vertex -393.4 -84.8 6.7
vertex -260.1 -84.8 6.7
vertex -260.1 -84 -13.3
endloop
endfacet
facet normal 0.00 1.00 0.04
outer loop
vertex -393.4 -84.8 6.7
vertex -260.1 -84 -13.3
vertex -393.4 -84 -13.3
endloop
endfacet
facet normal 0.00 -1.00 -0.04
outer loop
vertex -393.4 -76 6
vertex -393.4 -75.3 -11.9
vertex -260.1 -75.3 -11.9
endloop
endfacet
facet normal 0.00 -1.00 -0.04
outer loop
vertex -393.4 -76 6
vertex -260.1 -75.3 -11.9
vertex -260.1 -76 6
endloop
endfacet
facet normal 0.00 1.00 0.04
outer loop
vertex -260.1 -84.8 6.7
vertex -126.8 -84.8 6.7
vertex -126.8 -84 -13.3
endloop
endfacet
facet normal 0.00 1.00 0.04
outer loop
vertex -260.1 -84.8 6.7
vertex -126.8 -84 -13.3
vertex -260.1 -84 -13.3
endloop
endfacet
facet normal 0.00 -1.00 -0.04
outer loop
vertex -260.1 -76 6
vertex -260.1 -75.3 -11.9
vertex -126.8 -75.3 -11.9
endloop
endfacet
facet normal 0.00 -1.00 -0.04
outer loop
vertex -260.1 -76 6
vertex -126.8 -75.3 -11.9
vertex -126.8 -76 6
endloop
endfacet
facet normal -0.09 1.00 0.04
outer loop
vertex -126.8 -84.8 6.7
vertex -63.4 -79 6.2
vertex -63.4 -78.3 -12.4
endloop
endfacet
facet normal -0.09 1.00 0.04
outer loop
vertex -126.8 -84.8 6.7
vertex -63.4 -78.3 -12.4
vertex -126.8 -84 -13.3
endloop
endfacet
facet normal 0.09 -1.00 -0.04
outer loop
vertex -126.8 -76 6
vertex -126.8 -75.3 -11.9
vertex -63.4 -69.5 -11
endloop
endfacet
facet normal 0.09 -1.00 -0.04
outer loop
vertex -126.8 -76 6
vertex -63.4 -69.5 -11
vertex -63.4 -70.2 5.5
endloop
endfacet
facet normal -0.50 0.87 0.03
outer loop
vertex -63.4 -79 6.2
vertex -46.5 -69.3 5.5
vertex -46.5 -68.6 -10.9
endloop
endfacet
facet normal -0.50 0.87 0.03
outer loop
vertex -63.4 -79 6.2
vertex -46.5 -68.6 -10.9
vertex -63.4 -78.3 -12.4
endloop
endfacet
facet normal 0.50 -0.87 -0.03
outer loop
vertex -63.4 -70.2 5.5
vertex -63.4 -69.5 -11
vertex -46.5 -59.9 -9.5
endloop
endfacet
facet normal 0.50 -0.87 -0.03
outer loop
vertex -63.4 -70.2 5.5
vertex -46.5 -59.9 -9.5
vertex -46.5 -60.5 4.8
endloop
endfacet
facet normal -0.50 0.87 0.03
outer loop
vertex -46.5 -69.3 5.5
vertex -31.1 -60.5 4.8
vertex -31.1 -59.9 -9.5
endloop
endfacet
facet normal -0.50 0.87 0.03
outer loop
vertex -46.5 -69.3 5.5
vertex -31.1 -59.9 -9.5
vertex -46.5 -68.6 -10.9
endloop
endfacet
facet normal 0.50 -0.87 -0.03
outer loop
vertex -46.5 -60.5 4.8
vertex -46.5 -59.9 -9.5
vertex -31.1 -51.2 -8.1
endloop
endfacet
facet normal 0.50 -0.87 -0.03
outer loop
vertex -46.5 -60.5 4.8
vertex -31.1 -51.2 -8.1
vertex -31.1 -51.7 4.1
endloop
endfacet
facet normal -0.40 0.92 0.04
outer loop
vertex -31.1 -60.5 4.8
vertex -21.2 -56.2 4.4
vertex -21.2 -55.7 -8.8
endloop
endfacet
facet normal -0.40 0.92 0.04
outer loop
vertex -31.1 -60.5 4.8
vertex -21.2 -55.7 -8.8
vertex -31.1 -59.9 -9.5
endloop
endfacet
facet normal 0.40 -0.92 -0.04
outer loop
vertex -31.1 -51.7 4.1
vertex -31.1 -51.2 -8.1
vertex -21.2 -46.9 -7.4
endloop
endfacet
facet normal 0.40 -0.92 -0.04
outer loop
vertex -31.1 -51.7 4.1
vertex -21.2 -46.9 -7.4
vertex -21.2 -47.4 3.7
endloop
endfacet
facet normal -0.24 0.97 0.04
outer loop
vertex -21.2 -56.2 4.4
vertex -10.8 -53.6 4.2
vertex -10.8 -53.1 -8.4
endloop
endfacet
facet normal -0.24 0.97 0.04
outer loop
vertex -21.2 -56.2 4.4
vertex -10.8 -53.1 -8.4
vertex -21.2 -55.7 -8.8
endloop
endfacet
facet normal 0.24 -0.97 -0.04
outer loop
vertex -21.2 -47.4 3.7
vertex -21.2 -46.9 -7.4
vertex -10.8 -44.3 -7
endloop
endfacet
facet normal 0.24 -0.97 -0.04
outer loop
vertex -21.2 -47.4 3.7
vertex -10.8 -44.3 -7
vertex -10.8 -44.8 3.5
endloop
endfacet
facet normal -0.08 1.00 0.04
outer loop
vertex -10.8 -53.6 4.2
vertex 0 -52.7 4.1
vertex 0 -52.2 -8.3
endloop
endfacet
facet normal -0.08 1.00 0.04
outer loop
vertex -10.8 -53.6 4.2
vertex 0 -52.2 -8.3
vertex -10.8 -53.1 -8.4
endloop
endfacet
facet normal 0.08 -1.00 -0.04
outer loop
vertex -10.8 -44.8 3.5
vertex -10.8 -44.3 -7
vertex 0 -43.5 -6.9
endloop
endfacet
facet normal 0.08 -1.00 -0.04
outer loop
vertex -10.8 -44.8 3.5
vertex 0 -43.5 -6.9
vertex 0 -43.9 3.5
endloop
endfacet
facet normal 0.10 0.99 0.04
outer loop
vertex 0 -52.7 4.1
vertex 3.3 -53 4.2
vertex 3.3 -52.5 -8.3
endloop
endfacet
facet normal 0.10 0.99 0.04
outer loop
vertex 0 -52.7 4.1
vertex 3.3 -52.5 -8.3
vertex 0 -52.2 -8.3
endloop
endfacet
facet normal -0.10 -0.99 -0.04
outer loop
vertex 0 -43.9 3.5
vertex 0 -43.5 -6.9
vertex 3.3 -43.8 -6.9
endloop
endfacet
facet normal -0.10 -0.99 -0.04
outer loop
vertex 0 -43.9 3.5
vertex 3.3 -43.8 -6.9
vertex 3.3 -44.2 3.5
endloop
endfacet
facet normal 0.29 0.96 0.04
outer loop
vertex 3.3 -53 4.2
vertex 6.5 -54 4.2
vertex 6.5 -53.5 -8.5
endloop
endfacet
facet normal 0.29 0.96 0.04
outer loop
vertex 3.3 -53 4.2
vertex 6.5 -53.5 -8.5
vertex 3.3 -52.5 -8.3
endloop
endfacet
facet normal -0.29 -0.96 -0.04
outer loop
vertex 3.3 -44.2 3.5
vertex 3.3 -43.8 -6.9
vertex 6.5 -44.8 -7.1
endloop
endfacet
facet normal -0.29 -0.96 -0.04
outer loop
vertex 3.3 -44.2 3.5
vertex 6.5 -44.8 -7.1
vertex 6.5 -45.2 3.6
endloop
endfacet
facet normal 0.44 0.90 0.04
outer loop
vertex 6.5 -54 4.2
vertex 30.7 -66 5.2
vertex 30.7 -65.4 -10.4
endloop
endfacet
facet normal 0.44 0.90 0.04
outer loop
vertex 6.5 -54 4.2
vertex 30.7 -65.4 -10.4
vertex 6.5 -53.5 -8.5
endloop
endfacet
facet normal -0.44 -0.90 -0.04
outer loop
vertex 6.5 -45.2 3.6
vertex 6.5 -44.8 -7.1
vertex 30.7 -56.7 -9
endloop
endfacet
facet normal -0.44 -0.90 -0.04
outer loop
vertex 6.5 -45.2 3.6
vertex 30.7 -56.7 -9
vertex 30.7 -57.2 4.5
endloop
endfacet
facet normal 0.42 0.91 0.04
outer loop
vertex 30.7 -66 5.2
vertex 69.4 -83.9 6.6
vertex 69.4 -83.1 -13.2
endloop
endfacet
facet normal 0.42 0.91 0.04
outer loop
vertex 30.7 -66 5.2
vertex 69.4 -83.1 -13.2
vertex 30.7 -65.4 -10.4
endloop
endfacet
facet normal -0.42 -0.91 -0.04
outer loop
vertex 30.7 -57.2 4.5
vertex 30.7 -56.7 -9
vertex 69.4 -74.4 -11.8
endloop
endfacet
facet normal -0.42 -0.91 -0.04
outer loop
vertex 30.7 -57.2 4.5
vertex 69.4 -74.4 -11.8
vertex 69.4 -75.1 5.9
endloop
endfacet
facet normal 0.38 0.92 0.04
outer loop
vertex 69.4 -83.9 6.6
vertex 108.3 -100.2 7.9
vertex 108.3 -99.3 -15.7
endloop
endfacet
facet normal 0.38 0.92 0.04
outer loop
vertex 69.4 -83.9 6.6
vertex 108.3 -99.3 -15.7
vertex 69.4 -83.1 -13.2
endloop
endfacet
facet normal -0.38 -0.92 -0.04
outer loop
vertex 69.4 -75.1 5.9
vertex 69.4 -74.4 -11.8
vertex 108.3 -90.6 -14.3
endloop
endfacet
facet normal -0.38 -0.92 -0.04
outer loop
vertex 69.4 -75.1 5.9
vertex 108.3 -90.6 -14.3
vertex 108.3 -91.4 7.2
endloop
endfacet
facet normal 0.35 0.94 0.04
outer loop
vertex 108.3 -100.2 7.9
vertex 147.6 -114.9 9
vertex 147.6 -113.9 -18
endloop
endfacet
facet normal 0.35 0.94 0.04
outer loop
vertex 108.3 -100.2 7.9
vertex 147.6 -113.9 -18
vertex 108.3 -99.3 -15.7
endloop
endfacet
facet normal -0.35 -0.94 -0.04
outer loop
vertex 108.3 -91.4 7.2
vertex 108.3 -90.6 -14.3
vertex 147.6 -105.1 -16.7
endloop
endfacet
facet normal -0.35 -0.94 -0.04
outer loop
vertex 108.3 -91.4 7.2
vertex 147.6 -105.1 -16.7
vertex 147.6 -106.1 8.4
endloop
endfacet
facet normal 0.31 0.95 0.04
outer loop
vertex 147.6 -114.9 9
vertex 187.1 -128.1 10.1
vertex 187.1 -126.9 -20.1
endloop
endfacet
facet normal 0.31 0.95 0.04
outer loop
vertex 147.6 -114.9 9
vertex 187.1 -126.9 -20.1
vertex 147.6 -113.9 -18
endloop
endfacet
facet normal -0.31 -0.95 -0.04
outer loop
vertex 147.6 -106.1 8.4
vertex 147.6 -105.1 -16.7
vertex 187.1 -118.1 -18.7
endloop
endfacet
facet normal -0.31 -0.95 -0.04
outer loop
vertex 147.6 -106.1 8.4
vertex 187.1 -118.1 -18.7
vertex 187.1 -119.2 9.4
endloop
endfacet
facet normal 0.28 0.96 0.04
outer loop
vertex 187.1 -128.1 10.1
vertex 227 -139.6 11
vertex 227 -138.3 -21.9
endloop
endfacet
facet normal 0.28 0.96 0.04
outer loop
vertex 187.1 -128.1 10.1
vertex 227 -138.3 -21.9
vertex 187.1 -126.9 -20.1
endloop
endfacet
facet normal -0.28 -0.96 -0.04
outer loop
vertex 187.1 -119.2 9.4
vertex 187.1 -118.1 -18.7
vertex 227 -129.6 -20.5
endloop
endfacet
facet normal -0.28 -0.96 -0.04
outer loop
vertex 187.1 -119.2 9.4
vertex 227 -129.6 -20.5
vertex 227 -130.8 10.3
endloop
endfacet
facet normal 0.24 0.97 0.04
outer loop
vertex 227 -139.6 11
vertex 267.1 -149.6 11.8
vertex 267.1 -148.2 -23.5
endloop
endfacet
facet normal 0.24 0.97 0.04
outer loop
vertex 227 -139.6 11
vertex 267.1 -148.2 -23.5
vertex 227 -138.3 -21.9
endloop
endfacet
facet normal -0.24 -0.97 -0.04
outer loop
vertex 227 -130.8 10.3
vertex 227 -129.6 -20.5
vertex 267.1 -139.4 -22.1
endloop
endfacet
facet normal -0.24 -0.97 -0.04
outer loop
vertex 227 -130.8 10.3
vertex 267.1 -139.4 -22.1
vertex 267.1 -140.7 11.1
endloop
endfacet
facet normal 0.20 0.98 0.04
outer loop
vertex 267.1 -149.6 11.8
vertex 307.6 -157.9 12.4
vertex 307.6 -156.5 -24.8
endloop
endfacet
facet normal 0.20 0.98 0.04
outer loop
vertex 267.1 -149.6 11.8
vertex 307.6 -156.5 -24.8
vertex 267.1 -148.2 -23.5
endloop
endfacet
facet normal -0.20 -0.98 -0.04
outer loop
vertex 267.1 -140.7 11.1
vertex 267.1 -139.4 -22.1
vertex 307.6 -147.7 -23.4
endloop
endfacet
facet normal -0.20 -0.98 -0.04
outer loop
vertex 267.1 -140.7 11.1
vertex 307.6 -147.7 -23.4
vertex 307.6 -149.1 11.7
endloop
endfacet
facet normal 0.18 0.98 0.04
outer loop
vertex 307.6 -157.9 12.4
vertex 323.8 -160.8 12.7
vertex 323.8 -159.3 -25.2
endloop
endfacet
facet normal 0.18 0.98 0.04
outer loop
vertex 307.6 -157.9 12.4
vertex 323.8 -159.3 -25.2
vertex 307.6 -156.5 -24.8
endloop
endfacet
facet normal -0.18 -0.98 -0.04
outer loop
vertex 307.6 -149.1 11.7
vertex 307.6 -147.7 -23.4
vertex 323.8 -150.6 -23.9
endloop
endfacet
facet normal -0.18 -0.98 -0.04
outer loop
vertex 307.6 -149.1 11.7
vertex 323.8 -150.6 -23.9
vertex 323.8 -152 12
endloop
endfacet
facet normal 0.00 0.96 0.27
outer loop
vertex -393.4 -84 -13.3
vertex -260.1 -84 -13.3
vertex -260.1 -78.6 -32.6
endloop
endfacet
facet normal 0.00 0.96 0.27
outer loop
vertex -393.4 -84 -13.3
vertex -260.1 -78.6 -32.6
vertex -393.4 -78.6 -32.6
endloop
endfacet
facet normal 0.00 -0.96 -0.27
outer loop
vertex -393.4 -75.3 -11.9
vertex -393.4 -70.4 -29.2
vertex -260.1 -70.4 -29.2
endloop
endfacet
facet normal 0.00 -0.96 -0.27
outer loop
vertex -393.4 -75.3 -11.9
vertex -260.1 -70.4 -29.2
vertex -260.1 -75.3 -11.9
endloop
endfacet
facet normal 0.00 0.96 0.27
outer loop
vertex -260.1 -84 -13.3
vertex -126.8 -84 -13.3
vertex -126.8 -78.6 -32.6
endloop
endfacet
facet normal 0.00 0.96 0.27
outer loop
vertex -260.1 -84 -13.3
vertex -126.8 -78.6 -32.6
vertex -260.1 -78.6 -32.6
endloop
endfacet
facet normal 0.00 -0.96 -0.27
outer loop
vertex -260.1 -75.3 -11.9
vertex -260.1 -70.4 -29.2
vertex -126.8 -70.4 -29.2
endloop
endfacet
facet normal 0.00 -0.96 -0.27
outer loop
vertex -260.1 -75.3 -11.9
vertex -126.8 -70.4 -29.2
vertex -126.8 -75.3 -11.9
endloop
endfacet
facet normal -0.09 0.96 0.27
outer loop
vertex -126.8 -84 -13.3
vertex -63.4 -78.3 -12.4
vertex -63.4 -73.2 -30.3
endloop
endfacet
facet normal -0.09 0.96 0.27
outer loop
vertex -126.8 -84 -13.3
vertex -63.4 -73.2 -30.3
vertex -126.8 -78.6 -32.6
endloop
endfacet
facet normal 0.09 -0.96 -0.27
outer loop
vertex -126.8 -75.3 -11.9
vertex -126.8 -70.4 -29.2
vertex -63.4 -65 -26.9
endloop
endfacet
facet normal 0.09 -0.96 -0.27
outer loop
vertex -126.8 -75.3 -11.9
vertex -63.4 -65 -26.9
vertex -63.4 -69.5 -11
endloop
endfacet
facet normal -0.50 0.83 0.24
outer loop
vertex -63.4 -78.3 -12.4
vertex -46.5 -68.6 -10.9
vertex -46.5 -64.2 -26.6
endloop
endfacet
facet normal -0.50 0.83 0.24
outer loop
vertex -63.4 -78.3 -12.4
vertex -46.5 -64.2 -26.6
vertex -63.4 -73.2 -30.3
endloop
endfacet
facet normal 0.50 -0.83 -0.24
outer loop
vertex -63.4 -69.5 -11
vertex -63.4 -65 -26.9
vertex -46.5 -56 -23.2
endloop
endfacet
facet normal 0.50 -0.83 -0.24
outer loop
vertex -63.4 -69.5 -11
vertex -46.5 -56 -23.2
vertex -46.5 -59.9 -9.5
endloop
endfacet
facet normal -0.50 0.84 0.24
outer loop
vertex -46.5 -68.6 -10.9
vertex -31.1 -59.9 -9.5
vertex -31.1 -56 -23.2
endloop
endfacet
facet normal -0.50 0.84 0.24
outer loop
vertex -46.5 -68.6 -10.9
vertex -31.1 -56 -23.2
vertex -46.5 -64.2 -26.6
endloop
endfacet
facet normal 0.50 -0.84 -0.24
outer loop
vertex -46.5 -59.9 -9.5
vertex -46.5 -56 -23.2
vertex -31.1 -47.9 -19.8
endloop
endfacet
facet normal 0.50 -0.84 -0.24
outer loop
vertex -46.5 -59.9 -9.5
vertex -31.1 -47.9 -19.8
vertex -31.1 -51.2 -8.1
endloop
endfacet
facet normal -0.40 0.88 0.25
outer loop
vertex -31.1 -59.9 -9.5
vertex -21.2 -55.7 -8.8
vertex -21.2 -52.1 -21.6
endloop
endfacet
facet normal -0.40 0.88 0.25
outer loop
vertex -31.1 -59.9 -9.5
vertex -21.2 -52.1 -21.6
vertex -31.1 -56 -23.2
endloop
endfacet
facet normal 0.40 -0.88 -0.25
outer loop
vertex -31.1 -51.2 -8.1
vertex -31.1 -47.9 -19.8
vertex -21.2 -43.9 -18.2
endloop
endfacet
facet normal 0.40 -0.88 -0.25
outer loop
vertex -31.1 -51.2 -8.1
vertex -21.2 -43.9 -18.2
vertex -21.2 -46.9 -7.4
endloop
endfacet
facet normal -0.24 0.93 0.26
outer loop
vertex -21.2 -55.7 -8.8
vertex -10.8 -53.1 -8.4
vertex -10.8 -49.7 -20.6
endloop
endfacet
facet normal -0.24 0.93 0.26
outer loop
vertex -21.2 -55.7 -8.8
vertex -10.8 -49.7 -20.6
vertex -21.2 -52.1 -21.6
endloop
endfacet
facet normal 0.24 -0.93 -0.26
outer loop
vertex -21.2 -46.9 -7.4
vertex -21.2 -43.9 -18.2
vertex -10.8 -41.5 -17.2
endloop
endfacet
facet normal 0.24 -0.93 -0.26
outer loop
vertex -21.2 -46.9 -7.4
vertex -10.8 -41.5 -17.2
vertex -10.8 -44.3 -7
endloop
endfacet
facet normal -0.08 0.96 0.27
outer loop
vertex -10.8 -53.1 -8.4
vertex 0 -52.2 -8.3
vertex 0 -48.8 -20.2
endloop
endfacet
facet normal -0.08 0.96 0.27
outer loop
vertex -10.8 -53.1 -8.4
vertex 0 -48.8 -20.2
vertex -10.8 -49.7 -20.6
endloop
endfacet
facet normal 0.08 -0.96 -0.27
outer loop
vertex -10.8 -44.3 -7
vertex -10.8 -41.5 -17.2
vertex 0 -40.7 -16.8
endloop
endfacet
facet normal 0.08 -0.96 -0.27
outer loop
vertex -10.8 -44.3 -7
vertex 0 -40.7 -16.8
vertex 0 -43.5 -6.9
endloop
endfacet
facet normal 0.10 0.96 0.27
outer loop
vertex 0 -52.2 -8.3
vertex 3.3 -52.5 -8.3
vertex 3.3 -49.1 -20.4
endloop
endfacet
facet normal 0.10 0.96 0.27
outer loop
vertex 0 -52.2 -8.3
vertex 3.3 -49.1 -20.4
vertex 0 -48.8 -20.2
endloop
endfacet
facet normal -0.10 -0.96 -0.27
outer loop
vertex 0 -43.5 -6.9
vertex 0 -40.7 -16.8
vertex 3.3 -41 -17
endloop
endfacet
facet normal -0.10 -0.96 -0.27
outer loop
vertex 0 -43.5 -6.9
vertex 3.3 -41 -17
vertex 3.3 -43.8 -6.9
endloop
endfacet
facet normal 0.29 0.92 0.26
outer loop
vertex 3.3 -52.5 -8.3
vertex 6.5 -53.5 -8.5
vertex 6.5 -50 -20.7
endloop
endfacet
facet normal 0.29 0.92 0.26
outer loop
vertex 3.3 -52.5 -8.3
vertex 6.5 -50 -20.7
vertex 3.3 -49.1 -20.4
endloop
endfacet
facet normal -0.29 -0.92 -0.26
outer loop
vertex 3.3 -43.8 -6.9
vertex 3.3 -41 -17
vertex 6.5 -41.9 -17.3
endloop
endfacet
facet normal -0.29 -0.92 -0.26
outer loop
vertex 3.3 -43.8 -6.9
vertex 6.5 -41.9 -17.3
vertex 6.5 -44.8 -7.1
endloop
endfacet
facet normal 0.44 0.86 0.24
outer loop
vertex 6.5 -53.5 -8.5
vertex 30.7 -65.4 -10.4
vertex 30.7 -61.2 -25.4
endloop
endfacet
facet normal 0.44 0.86 0.24
outer loop
vertex 6.5 -53.5 -8.5
vertex 30.7 -61.2 -25.4
vertex 6.5 -50 -20.7
endloop
endfacet
facet normal -0.44 -0.86 -0.24
outer loop
vertex 6.5 -44.8 -7.1
vertex 6.5 -41.9 -17.3
vertex 30.7 -53 -22
endloop
endfacet
facet normal -0.44 -0.86 -0.24
outer loop
vertex 6.5 -44.8 -7.1
vertex 30.7 -53 -22
vertex 30.7 -56.7 -9
endloop
endfacet
facet normal 0.42 0.87 0.25
outer loop
vertex 30.7 -65.4 -10.4
vertex 69.4 -83.1 -13.2
vertex 69.4 -77.8 -32.2
endloop
endfacet
facet normal 0.42 0.87 0.25
outer loop
vertex 30.7 -65.4 -10.4
vertex 69.4 -77.8 -32.2
vertex 30.7 -61.2 -25.4
endloop
endfacet
facet normal -0.42 -0.87 -0.25
outer loop
vertex 30.7 -56.7 -9
vertex 30.7 -53 -22
vertex 69.4 -69.6 -28.8
endloop
endfacet
facet normal -0.42 -0.87 -0.25
outer loop
vertex 30.7 -56.7 -9
vertex 69.4 -69.6 -28.8
vertex 69.4 -74.4 -11.8
endloop
endfacet
facet normal 0.38 0.89 0.25
outer loop
vertex 69.4 -83.1 -13.2
vertex 108.3 -99.3 -15.7
vertex 108.3 -92.9 -38.5
endloop
endfacet
facet normal 0.38 0.89 0.25
outer loop
vertex 69.4 -83.1 -13.2
vertex 108.3 -92.9 -38.5
vertex 69.4 -77.8 -32.2
endloop
endfacet
facet normal -0.38 -0.89 -0.25
outer loop
vertex 69.4 -74.4 -11.8
vertex 69.4 -69.6 -28.8
vertex 108.3 -84.7 -35.1
endloop
endfacet
facet normal -0.38 -0.89 -0.25
outer loop
vertex 69.4 -74.4 -11.8
vertex 108.3 -84.7 -35.1
vertex 108.3 -90.6 -14.3
endloop
endfacet
facet normal 0.35 0.90 0.25
outer loop
vertex 108.3 -99.3 -15.7
vertex 147.6 -113.9 -18
vertex 147.6 -106.5 -44.1
endloop
endfacet
facet normal 0.35 0.90 0.25
outer loop
vertex 108.3 -99.3 -15.7
vertex 147.6 -106.5 -44.1
vertex 108.3 -92.9 -38.5
endloop
endfacet
facet normal -0.35 -0.90 -0.25
outer loop
vertex 108.3 -90.6 -14.3
vertex 108.3 -84.7 -35.1
vertex 147.6 -98.3 -40.7
endloop
endfacet
facet normal -0.35 -0.90 -0.25
outer loop
vertex 108.3 -90.6 -14.3
vertex 147.6 -98.3 -40.7
vertex 147.6 -105.1 -16.7
endloop
endfacet
facet normal 0.31 0.91 0.26
outer loop
vertex 147.6 -113.9 -18
vertex 187.1 -126.9 -20.1
vertex 187.1 -118.7 -49.2
endloop
endfacet
facet normal 0.31 0.91 0.26
outer loop
vertex 147.6 -113.9 -18
vertex 187.1 -118.7 -49.2
vertex 147.6 -106.5 -44.1
endloop
endfacet
facet normal -0.31 -0.91 -0.26
outer loop
vertex 147.6 -105.1 -16.7
vertex 147.6 -98.3 -40.7
vertex 187.1 -110.5 -45.8
endloop
endfacet
facet normal -0.31 -0.91 -0.26
outer loop
vertex 147.6 -105.1 -16.7
vertex 187.1 -110.5 -45.8
vertex 187.1 -118.1 -18.7
endloop
endfacet
facet normal 0.28 0.92 0.26
outer loop
vertex 187.1 -126.9 -20.1
vertex 227 -138.3 -21.9
vertex 227 -129.4 -53.6
endloop
endfacet
facet normal 0.28 0.92 0.26
outer loop
vertex 187.1 -126.9 -20.1
vertex 227 -129.4 -53.6
vertex 187.1 -118.7 -49.2
endloop
endfacet
facet normal -0.28 -0.92 -0.26
outer loop
vertex 187.1 -118.1 -18.7
vertex 187.1 -110.5 -45.8
vertex 227 -121.2 -50.2
endloop
endfacet
facet normal -0.28 -0.92 -0.26
outer loop
vertex 187.1 -118.1 -18.7
vertex 227 -121.2 -50.2
vertex 227 -129.6 -20.5
endloop
endfacet
facet normal 0.24 0.93 0.26
outer loop
vertex 227 -138.3 -21.9
vertex 267.1 -148.2 -23.5
vertex 267.1 -138.6 -57.4
endloop
endfacet
facet normal 0.24 0.93 0.26
outer loop
vertex 227 -138.3 -21.9
vertex 267.1 -138.6 -57.4
vertex 227 -129.4 -53.6
endloop
endfacet
facet normal -0.24 -0.93 -0.26
outer loop
vertex 227 -129.6 -20.5
vertex 227 -121.2 -50.2
vertex 267.1 -130.4 -54
endloop
endfacet
facet normal -0.24 -0.93 -0.26
outer loop
vertex 227 -129.6 -20.5
vertex 267.1 -130.4 -54
vertex 267.1 -139.4 -22.1
endloop
endfacet
facet normal 0.20 0.94 0.27
outer loop
vertex 267.1 -148.2 -23.5
vertex 307.6 -156.5 -24.8
vertex 307.6 -146.4 -60.6
endloop
endfacet
facet normal 0.20 0.94 0.27
outer loop
vertex 267.1 -148.2 -23.5
vertex 307.6 -146.4 -60.6
vertex 267.1 -138.6 -57.4
endloop
endfacet
facet normal -0.20 -0.94 -0.27
outer loop
vertex 267.1 -139.4 -22.1
vertex 267.1 -130.4 -54
vertex 307.6 -138.2 -57.2
endloop
endfacet
facet normal -0.20 -0.94 -0.27
outer loop
vertex 267.1 -139.4 -22.1
vertex 307.6 -138.2 -57.2
vertex 307.6 -147.7 -23.4
endloop
endfacet
facet normal 0.18 0.95 0.27
outer loop
vertex 307.6 -156.5 -24.8
vertex 323.8 -159.3 -25.2
vertex 323.8 -149 -61.7
endloop
endfacet
facet normal 0.18 0.95 0.27
outer loop
vertex 307.6 -156.5 -24.8
vertex 323.8 -149 -61.7
vertex 307.6 -146.4 -60.6
endloop
endfacet
facet normal -0.18 -0.95 -0.27
outer loop
vertex 307.6 -147.7 -23.4
vertex 307.6 -138.2 -57.2
vertex 323.8 -140.9 -58.4
endloop
endfacet
facet normal -0.18 -0.95 -0.27
outer loop
vertex 307.6 -147.7 -23.4
vertex 323.8 -140.9 -58.4
vertex 323.8 -150.6 -23.9
endloop
endfacet
facet normal 0.00 0.87 0.49
outer loop
vertex -393.4 -78.6 -32.6
vertex -260.1 -78.6 -32.6
vertex -260.1 -68.8 -50
endloop
endfacet
facet normal 0.00 0.87 0.49
outer loop
vertex -393.4 -78.6 -32.6
vertex -260.1 -68.8 -50
vertex -393.4 -68.8 -50
endloop
endfacet
facet normal 0.00 -0.87 -0.49
outer loop
vertex -393.4 -70.4 -29.2
vertex -393.4 -61.7 -44.8
vertex -260.1 -61.7 -44.8
endloop
endfacet
facet normal 0.00 -0.87 -0.49
outer loop
vertex -393.4 -70.4 -29.2
vertex -260.1 -61.7 -44.8
vertex -260.1 -70.4 -29.2
endloop
endfacet
facet normal 0.00 0.87 0.49
outer loop
vertex -260.1 -78.6 -32.6
vertex -126.8 -78.6 -32.6
vertex -126.8 -68.8 -50
endloop
endfacet
facet normal 0.00 0.87 0.49
outer loop
vertex -260.1 -78.6 -32.6
vertex -126.8 -68.8 -50
vertex -260.1 -68.8 -50
endloop
endfacet
facet normal 0.00 -0.87 -0.49
outer loop
vertex -260.1 -70.4 -29.2
vertex -260.1 -61.7 -44.8
vertex -126.8 -61.7 -44.8
endloop
endfacet
facet normal 0.00 -0.87 -0.49
outer loop
vertex -260.1 -70.4 -29.2
vertex -126.8 -61.7 -44.8
vertex -126.8 -70.4 -29.2
endloop
endfacet
facet normal -0.09 0.87 0.49
outer loop
vertex -126.8 -78.6 -32.6
vertex -63.4 -73.2 -30.3
vertex -63.4 -64.1 -46.6
endloop
endfacet
facet normal -0.09 0.87 0.49
outer loop
vertex -126.8 -78.6 -32.6
vertex -63.4 -64.1 -46.6
vertex -126.8 -68.8 -50
endloop
endfacet
facet normal 0.09 -0.87 -0.49
outer loop
vertex -126.8 -70.4 -29.2
vertex -126.8 -61.7 -44.8
vertex -63.4 -57 -41.4
endloop
endfacet
facet normal 0.09 -0.87 -0.49
outer loop
vertex -126.8 -70.4 -29.2
vertex -63.4 -57 -41.4
vertex -63.4 -65 -26.9
endloop
endfacet
facet normal -0.50 0.76 0.42
outer loop
vertex -63.4 -73.2 -30.3
vertex -46.5 -64.2 -26.6
vertex -46.5 -56.2 -40.8
endloop
endfacet
facet normal -0.50 0.76 0.42
outer loop
vertex -63.4 -73.2 -30.3
vertex -46.5 -56.2 -40.8
vertex -63.4 -64.1 -46.6
endloop
endfacet
facet normal 0.50 -0.76 -0.42
outer loop
vertex -63.4 -65 -26.9
vertex -63.4 -57 -41.4
vertex -46.5 -49.1 -35.7
endloop
endfacet
facet normal 0.50 -0.76 -0.42
outer loop
vertex -63.4 -65 -26.9
vertex -46.5 -49.1 -35.7
vertex -46.5 -56 -23.2
endloop
endfacet
facet normal -0.50 0.76 0.42
outer loop
vertex -46.5 -64.2 -26.6
vertex -31.1 -56 -23.2
vertex -31.1 -49.1 -35.7
endloop
endfacet
facet normal -0.50 0.76 0.42
outer loop
vertex -46.5 -64.2 -26.6
vertex -31.1 -49.1 -35.7
vertex -46.5 -56.2 -40.8
endloop
endfacet
facet normal 0.50 -0.76 -0.42
outer loop
vertex -46.5 -56 -23.2
vertex -46.5 -49.1 -35.7
vertex -31.1 -41.9 -30.5
endloop
endfacet
facet normal 0.50 -0.76 -0.42
outer loop
vertex -46.5 -56 -23.2
vertex -31.1 -41.9 -30.5
vertex -31.1 -47.9 -19.8
endloop
endfacet
facet normal -0.40 0.80 0.45
outer loop
vertex -31.1 -56 -23.2
vertex -21.2 -52.1 -21.6
vertex -21.2 -45.6 -33.1
endloop
endfacet
facet normal -0.40 0.80 0.45
outer loop
vertex -31.1 -56 -23.2
vertex -21.2 -45.6 -33.1
vertex -31.1 -49.1 -35.7
endloop
endfacet
facet normal 0.40 -0.80 -0.45
outer loop
vertex -31.1 -47.9 -19.8
vertex -31.1 -41.9 -30.5
vertex -21.2 -38.4 -27.9
endloop
endfacet
facet normal 0.40 -0.80 -0.45
outer loop
vertex -31.1 -47.9 -19.8
vertex -21.2 -38.4 -27.9
vertex -21.2 -43.9 -18.2
endloop
endfacet
facet normal -0.24 0.85 0.47
outer loop
vertex -21.2 -52.1 -21.6
vertex -10.8 -49.7 -20.6
vertex -10.8 -43.5 -31.6
endloop
endfacet
facet normal -0.24 0.85 0.47
outer loop
vertex -21.2 -52.1 -21.6
vertex -10.8 -43.5 -31.6
vertex -21.2 -45.6 -33.1
endloop
endfacet
facet normal 0.24 -0.85 -0.47
outer loop
vertex -21.2 -43.9 -18.2
vertex -21.2 -38.4 -27.9
vertex -10.8 -36.3 -26.4
endloop
endfacet
facet normal 0.24 -0.85 -0.47
outer loop
vertex -21.2 -43.9 -18.2
vertex -10.8 -36.3 -26.4
vertex -10.8 -41.5 -17.2
endloop
endfacet
facet normal -0.08 0.87 0.49
outer loop
vertex -10.8 -49.7 -20.6
vertex 0 -48.8 -20.2
vertex 0 -42.8 -31.1
endloop
endfacet
facet normal -0.08 0.87 0.49
outer loop
vertex -10.8 -49.7 -20.6
vertex 0 -42.8 -31.1
vertex -10.8 -43.5 -31.6
endloop
endfacet
facet normal 0.08 -0.87 -0.49
outer loop
vertex -10.8 -41.5 -17.2
vertex -10.8 -36.3 -26.4
vertex 0 -35.6 -25.9
endloop
endfacet
facet normal 0.08 -0.87 -0.49
outer loop
vertex -10.8 -41.5 -17.2
vertex 0 -35.6 -25.9
vertex 0 -40.7 -16.8
endloop
endfacet
facet normal 0.10 0.87 0.49
outer loop
vertex 0 -48.8 -20.2
vertex 3.3 -49.1 -20.4
vertex 3.3 -43 -31.3
endloop
endfacet
facet normal 0.10 0.87 0.49
outer loop
vertex 0 -48.8 -20.2
vertex 3.3 -43 -31.3
vertex 0 -42.8 -31.1
endloop
endfacet
facet normal -0.10 -0.87 -0.49
outer loop
vertex 0 -40.7 -16.8
vertex 0 -35.6 -25.9
vertex 3.3 -35.9 -26.1
endloop
endfacet
facet normal -0.10 -0.87 -0.49
outer loop
vertex 0 -40.7 -16.8
vertex 3.3 -35.9 -26.1
vertex 3.3 -41 -17
endloop
endfacet
facet normal 0.29 0.83 0.47
outer loop
vertex 3.3 -49.1 -20.4
vertex 6.5 -50 -20.7
vertex 6.5 -43.8 -31.8
endloop
endfacet
facet normal 0.29 0.83 0.47
outer loop
vertex 3.3 -49.1 -20.4
vertex 6.5 -43.8 -31.8
vertex 3.3 -43 -31.3
endloop
endfacet
facet normal -0.29 -0.83 -0.47
outer loop
vertex 3.3 -41 -17
vertex 3.3 -35.9 -26.1
vertex 6.5 -36.7 -26.6
endloop
endfacet
facet normal -0.29 -0.83 -0.47
outer loop
vertex 3.3 -41 -17
vertex 6.5 -36.7 -26.6
vertex 6.5 -41.9 -17.3
endloop
endfacet
facet normal 0.44 0.78 0.44
outer loop
vertex 6.5 -50 -20.7
vertex 30.7 -61.2 -25.4
vertex 30.7 -53.6 -38.9
endloop
endfacet
facet normal 0.44 0.78 0.44
outer loop
vertex 6.5 -50 -20.7
vertex 30.7 -53.6 -38.9
vertex 6.5 -43.8 -31.8
endloop
endfacet
facet normal -0.44 -0.78 -0.44
outer loop
vertex 6.5 -41.9 -17.3
vertex 6.5 -36.7 -26.6
vertex 30.7 -46.4 -33.7
endloop
endfacet
facet normal -0.44 -0.78 -0.44
outer loop
vertex 6.5 -41.9 -17.3
vertex 30.7 -46.4 -33.7
vertex 30.7 -53 -22
endloop
endfacet
facet normal 0.42 0.79 0.44
outer loop
vertex 30.7 -61.2 -25.4
vertex 69.4 -77.8 -32.2
vertex 69.4 -68.1 -49.5
endloop
endfacet
facet normal 0.42 0.79 0.44
outer loop
vertex 30.7 -61.2 -25.4
vertex 69.4 -68.1 -49.5
vertex 30.7 -53.6 -38.9
endloop
endfacet
facet normal -0.42 -0.79 -0.44
outer loop
vertex 30.7 -53 -22
vertex 30.7 -46.4 -33.7
vertex 69.4 -61 -44.3
endloop
endfacet
facet normal -0.42 -0.79 -0.44
outer loop
vertex 30.7 -53 -22
vertex 69.4 -61 -44.3
vertex 69.4 -69.6 -28.8
endloop
endfacet
facet normal 0.38 0.81 0.45
outer loop
vertex 69.4 -77.8 -32.2
vertex 108.3 -92.9 -38.5
vertex 108.3 -81.3 -59.1
endloop
endfacet
facet normal 0.38 0.81 0.45
outer loop
vertex 69.4 -77.8 -32.2
vertex 108.3 -81.3 -59.1
vertex 69.4 -68.1 -49.5
endloop
endfacet
facet normal -0.38 -0.81 -0.45
outer loop
vertex 69.4 -69.6 -28.8
vertex 69.4 -61 -44.3
vertex 108.3 -74.2 -53.9
endloop
endfacet
facet normal -0.38 -0.81 -0.45
outer loop
vertex 69.4 -69.6 -28.8
vertex 108.3 -74.2 -53.9
vertex 108.3 -84.7 -35.1
endloop
endfacet
facet normal 0.35 0.82 0.46
outer loop
vertex 108.3 -92.9 -38.5
vertex 147.6 -106.5 -44.1
vertex 147.6 -93.3 -67.8
endloop
endfacet
facet normal 0.35 0.82 0.46
outer loop
vertex 108.3 -92.9 -38.5
vertex 147.6 -93.3 -67.8
vertex 108.3 -81.3 -59.1
endloop
endfacet
facet normal -0.35 -0.82 -0.46
outer loop
vertex 108.3 -84.7 -35.1
vertex 108.3 -74.2 -53.9
vertex 147.6 -86.1 -62.6
endloop
endfacet
facet normal -0.35 -0.82 -0.46
outer loop
vertex 108.3 -84.7 -35.1
vertex 147.6 -86.1 -62.6
vertex 147.6 -98.3 -40.7
endloop
endfacet
facet normal 0.31 0.83 0.46
outer loop
vertex 147.6 -106.5 -44.1
vertex 187.1 -118.7 -49.2
vertex 187.1 -103.9 -75.5
endloop
endfacet
facet normal 0.31 0.83 0.46
outer loop
vertex 147.6 -106.5 -44.1
vertex 187.1 -103.9 -75.5
vertex 147.6 -93.3 -67.8
endloop
endfacet
facet normal -0.31 -0.83 -0.46
outer loop
vertex 147.6 -98.3 -40.7
vertex 147.6 -86.1 -62.6
vertex 187.1 -96.8 -70.3
endloop
endfacet
facet normal -0.31 -0.83 -0.46
outer loop
vertex 147.6 -98.3 -40.7
vertex 187.1 -96.8 -70.3
vertex 187.1 -110.5 -45.8
endloop
endfacet
facet normal 0.28 0.84 0.47
outer loop
vertex 187.1 -118.7 -49.2
vertex 227 -129.4 -53.6
vertex 227 -113.3 -82.3
endloop
endfacet
facet normal 0.28 0.84 0.47
outer loop
vertex 187.1 -118.7 -49.2
vertex 227 -113.3 -82.3
vertex 187.1 -103.9 -75.5
endloop
endfacet
facet normal -0.28 -0.84 -0.47
outer loop
vertex 187.1 -110.5 -45.8
vertex 187.1 -96.8 -70.3
vertex 227 -106.1 -77.1
endloop
endfacet
facet normal -0.28 -0.84 -0.47
outer loop
vertex 187.1 -110.5 -45.8
vertex 227 -106.1 -77.1
vertex 227 -121.2 -50.2
endloop
endfacet
facet normal 0.24 0.85 0.47
outer loop
vertex 227 -129.4 -53.6
vertex 267.1 -138.6 -57.4
vertex 267.1 -121.4 -88.2
endloop
endfacet
facet normal 0.24 0.85 0.47
outer loop
vertex 227 -129.4 -53.6
vertex 267.1 -121.4 -88.2
vertex 227 -113.3 -82.3
endloop
endfacet
facet normal -0.24 -0.85 -0.47
outer loop
vertex 227 -121.2 -50.2
vertex 227 -106.1 -77.1
vertex 267.1 -114.2 -83
endloop
endfacet
facet normal -0.24 -0.85 -0.47
outer loop
vertex 227 -121.2 -50.2
vertex 267.1 -114.2 -83
vertex 267.1 -130.4 -54
endloop
endfacet
facet normal 0.20 0.85 0.48
outer loop
vertex 267.1 -138.6 -57.4
vertex 307.6 -146.4 -60.6
vertex 307.6 -128.2 -93.1
endloop
endfacet
facet normal 0.20 0.85 0.48
outer loop
vertex 267.1 -138.6 -57.4
vertex 307.6 -128.2 -93.1
vertex 267.1 -121.4 -88.2
endloop
endfacet
facet normal -0.20 -0.85 -0.48
outer loop
vertex 267.1 -130.4 -54
vertex 267.1 -114.2 -83
vertex 307.6 -121 -87.9
endloop
endfacet
facet normal -0.20 -0.85 -0.48
outer loop
vertex 267.1 -130.4 -54
vertex 307.6 -121 -87.9
vertex 307.6 -138.2 -57.2
endloop
endfacet
facet normal 0.18 0.86 0.48
outer loop
vertex 307.6 -146.4 -60.6
vertex 323.8 -149 -61.7
vertex 323.8 -130.5 -94.8
endloop
endfacet
facet normal 0.18 0.86 0.48
outer loop
vertex 307.6 -146.4 -60.6
vertex 323.8 -130.5 -94.8
vertex 307.6 -128.2 -93.1
endloop
endfacet
facet normal -0.18 -0.86 -0.48
outer loop
vertex 307.6 -138.2 -57.2
vertex 307.6 -121 -87.9
vertex 323.8 -123.4 -89.6
endloop
endfacet
facet normal -0.18 -0.86 -0.48
outer loop
vertex 307.6 -138.2 -57.2
vertex 323.8 -123.4 -89.6
vertex 323.8 -140.9 -58.4
endloop
endfacet
facet normal 0.00 0.73 0.68
outer loop
vertex -393.4 -68.8 -50
vertex -260.1 -68.8 -50
vertex -260.1 -55.3 -64.7
endloop
endfacet
facet normal 0.00 0.73 0.68
outer loop
vertex -393.4 -68.8 -50
vertex -260.1 -55.3 -64.7
vertex -393.4 -55.3 -64.7
endloop
endfacet
facet normal 0.00 -0.73 -0.68
outer loop
vertex -393.4 -61.7 -44.8
vertex -393.4 -49.5 -58
vertex -260.1 -49.5 -58
endloop
endfacet
facet normal 0.00 -0.73 -0.68
outer loop
vertex -393.4 -61.7 -44.8
vertex -260.1 -49.5 -58
vertex -260.1 -61.7 -44.8
endloop
endfacet
facet normal 0.00 0.73 0.68
outer loop
vertex -260.1 -68.8 -50
vertex -126.8 -68.8 -50
vertex -126.8 -55.3 -64.7
endloop
endfacet
facet normal 0.00 0.73 0.68
outer loop
vertex -260.1 -68.8 -50
vertex -126.8 -55.3 -64.7
vertex -260.1 -55.3 -64.7
endloop
endfacet
facet normal 0.00 -0.73 -0.68
outer loop
vertex -260.1 -61.7 -44.8
vertex -260.1 -49.5 -58
vertex -126.8 -49.5 -58
endloop
endfacet
facet normal 0.00 -0.73 -0.68
outer loop
vertex -260.1 -61.7 -44.8
vertex -126.8 -49.5 -58
vertex -126.8 -61.7 -44.8
endloop
endfacet
facet normal -0.09 0.73 0.68
outer loop
vertex -126.8 -68.8 -50
vertex -63.4 -64.1 -46.6
vertex -63.4 -51.5 -60.3
endloop
endfacet
facet normal -0.09 0.73 0.68
outer loop
vertex -126.8 -68.8 -50
vertex -63.4 -51.5 -60.3
vertex -126.8 -55.3 -64.7
endloop
endfacet
facet normal 0.09 -0.73 -0.68
outer loop
vertex -126.8 -61.7 -44.8
vertex -126.8 -49.5 -58
vertex -63.4 -45.7 -53.5
endloop
endfacet
facet normal 0.09 -0.73 -0.68
outer loop
vertex -126.8 -61.7 -44.8
vertex -63.4 -45.7 -53.5
vertex -63.4 -57 -41.4
endloop
endfacet
facet normal -0.50 0.64 0.59
outer loop
vertex -63.4 -64.1 -46.6
vertex -46.5 -56.2 -40.8
vertex -46.5 -45.1 -52.8
endloop
endfacet
facet normal -0.50 0.64 0.59
outer loop
vertex -63.4 -64.1 -46.6
vertex -46.5 -45.1 -52.8
vertex -63.4 -51.5 -60.3
endloop
endfacet
facet normal 0.50 -0.64 -0.59
outer loop
vertex -63.4 -57 -41.4
vertex -63.4 -45.7 -53.5
vertex -46.5 -39.4 -46.1
endloop
endfacet
facet normal 0.50 -0.64 -0.59
outer loop
vertex -63.4 -57 -41.4
vertex -46.5 -39.4 -46.1
vertex -46.5 -49.1 -35.7
endloop
endfacet
facet normal -0.50 0.64 0.59
outer loop
vertex -46.5 -56.2 -40.8
vertex -31.1 -49.1 -35.7
vertex -31.1 -39.4 -46.1
endloop
endfacet
facet normal -0.50 0.64 0.59
outer loop
vertex -46.5 -56.2 -40.8
vertex -31.1 -39.4 -46.1
vertex -46.5 -45.1 -52.8
endloop
endfacet
facet normal 0.50 -0.64 -0.59
outer loop
vertex -46.5 -49.1 -35.7
vertex -46.5 -39.4 -46.1
vertex -31.1 -33.6 -39.4
endloop
endfacet
facet normal 0.50 -0.64 -0.59
outer loop
vertex -46.5 -49.1 -35.7
vertex -31.1 -33.6 -39.4
vertex -31.1 -41.9 -30.5
endloop
endfacet
facet normal -0.40 0.67 0.62
outer loop
vertex -31.1 -49.1 -35.7
vertex -21.2 -45.6 -33.1
vertex -21.2 -36.6 -42.9
endloop
endfacet
facet normal -0.40 0.67 0.62
outer loop
vertex -31.1 -49.1 -35.7
vertex -21.2 -36.6 -42.9
vertex -31.1 -39.4 -46.1
endloop
endfacet
facet normal 0.40 -0.67 -0.62
outer loop
vertex -31.1 -41.9 -30.5
vertex -31.1 -33.6 -39.4
vertex -21.2 -30.9 -36.1
endloop
endfacet
facet normal 0.40 -0.67 -0.62
outer loop
vertex -31.1 -41.9 -30.5
vertex -21.2 -30.9 -36.1
vertex -21.2 -38.4 -27.9
endloop
endfacet
facet normal -0.24 0.71 0.66
outer loop
vertex -21.2 -45.6 -33.1
vertex -10.8 -43.5 -31.6
vertex -10.8 -34.9 -40.9
endloop
endfacet
facet normal -0.24 0.71 0.66
outer loop
vertex -21.2 -45.6 -33.1
vertex -10.8 -34.9 -40.9
vertex -21.2 -36.6 -42.9
endloop
endfacet
facet normal 0.24 -0.71 -0.66
outer loop
vertex -21.2 -38.4 -27.9
vertex -21.2 -30.9 -36.1
vertex -10.8 -29.2 -34.1
endloop
endfacet
facet normal 0.24 -0.71 -0.66
outer loop
vertex -21.2 -38.4 -27.9
vertex -10.8 -29.2 -34.1
vertex -10.8 -36.3 -26.4
endloop
endfacet
facet normal -0.08 0.73 0.68
outer loop
vertex -10.8 -43.5 -31.6
vertex 0 -42.8 -31.1
vertex 0 -34.3 -40.2
endloop
endfacet
facet normal -0.08 0.73 0.68
outer loop
vertex -10.8 -43.5 -31.6
vertex 0 -34.3 -40.2
vertex -10.8 -34.9 -40.9
endloop
endfacet
facet normal 0.08 -0.73 -0.68
outer loop
vertex -10.8 -36.3 -26.4
vertex -10.8 -29.2 -34.1
vertex 0 -28.6 -33.5
endloop
endfacet
facet normal 0.08 -0.73 -0.68
outer loop
vertex -10.8 -36.3 -26.4
vertex 0 -28.6 -33.5
vertex 0 -35.6 -25.9
endloop
endfacet
facet normal 0.10 0.73 0.68
outer loop
vertex 0 -42.8 -31.1
vertex 3.3 -43 -31.3
vertex 3.3 -34.5 -40.4
endloop
endfacet
facet normal 0.10 0.73 0.68
outer loop
vertex 0 -42.8 -31.1
vertex 3.3 -34.5 -40.4
vertex 0 -34.3 -40.2
endloop
endfacet
facet normal -0.10 -0.73 -0.68
outer loop
vertex 0 -35.6 -25.9
vertex 0 -28.6 -33.5
vertex 3.3 -28.8 -33.7
endloop
endfacet
facet normal -0.10 -0.73 -0.68
outer loop
vertex 0 -35.6 -25.9
vertex 3.3 -28.8 -33.7
vertex 3.3 -35.9 -26.1
endloop
endfacet
facet normal 0.29 0.70 0.65
outer loop
vertex 3.3 -43 -31.3
vertex 6.5 -43.8 -31.8
vertex 6.5 -35.2 -41.2
endloop
endfacet
facet normal 0.29 0.70 0.65
outer loop
vertex 3.3 -43 -31.3
vertex 6.5 -35.2 -41.2
vertex 3.3 -34.5 -40.4
endloop
endfacet
facet normal -0.29 -0.70 -0.65
outer loop
vertex 3.3 -35.9 -26.1
vertex 3.3 -28.8 -33.7
vertex 6.5 -29.4 -34.5
endloop
endfacet
facet normal -0.29 -0.70 -0.65
outer loop
vertex 3.3 -35.9 -26.1
vertex 6.5 -29.4 -34.5
vertex 6.5 -36.7 -26.6
endloop
endfacet
facet normal 0.44 0.66 0.61
outer loop
vertex 6.5 -43.8 -31.8
vertex 30.7 -53.6 -38.9
vertex 30.7 -43 -50.4
endloop
endfacet
facet normal 0.44 0.66 0.61
outer loop
vertex 6.5 -43.8 -31.8
vertex 30.7 -43 -50.4
vertex 6.5 -35.2 -41.2
endloop
endfacet
facet normal -0.44 -0.66 -0.61
outer loop
vertex 6.5 -36.7 -26.6
vertex 6.5 -29.4 -34.5
vertex 30.7 -37.3 -43.6
endloop
endfacet
facet normal -0.44 -0.66 -0.61
outer loop
vertex 6.5 -36.7 -26.6
vertex 30.7 -37.3 -43.6
vertex 30.7 -46.4 -33.7
endloop
endfacet
facet normal 0.42 0.67 0.62
outer loop
vertex 30.7 -53.6 -38.9
vertex 69.4 -68.1 -49.5
vertex 69.4 -54.7 -64
endloop
endfacet
facet normal 0.42 0.67 0.62
outer loop
vertex 30.7 -53.6 -38.9
vertex 69.4 -54.7 -64
vertex 30.7 -43 -50.4
endloop
endfacet
facet normal -0.42 -0.67 -0.62
outer loop
vertex 30.7 -46.4 -33.7
vertex 30.7 -37.3 -43.6
vertex 69.4 -48.9 -57.3
endloop
endfacet
facet normal -0.42 -0.67 -0.62
outer loop
vertex 30.7 -46.4 -33.7
vertex 69.4 -48.9 -57.3
vertex 69.4 -61 -44.3
endloop
endfacet
facet normal 0.38 0.68 0.63
outer loop
vertex 69.4 -68.1 -49.5
vertex 108.3 -81.3 -59.1
vertex 108.3 -65.3 -76.4
endloop
endfacet
facet normal 0.38 0.68 0.63
outer loop
vertex 69.4 -68.1 -49.5
vertex 108.3 -65.3 -76.4
vertex 69.4 -54.7 -64
endloop
endfacet
facet normal -0.38 -0.68 -0.63
outer loop
vertex 69.4 -61 -44.3
vertex 69.4 -48.9 -57.3
vertex 108.3 -59.5 -69.7
endloop
endfacet
facet normal -0.38 -0.68 -0.63
outer loop
vertex 69.4 -61 -44.3
vertex 108.3 -59.5 -69.7
vertex 108.3 -74.2 -53.9
endloop
endfacet
facet normal 0.35 0.69 0.64
outer loop
vertex 108.3 -81.3 -59.1
vertex 147.6 -93.3 -67.8
vertex 147.6 -74.9 -87.7
endloop
endfacet
facet normal 0.35 0.69 0.64
outer loop
vertex 108.3 -81.3 -59.1
vertex 147.6 -74.9 -87.7
vertex 108.3 -65.3 -76.4
endloop
endfacet
facet normal -0.35 -0.69 -0.64
outer loop
vertex 108.3 -74.2 -53.9
vertex 108.3 -59.5 -69.7
vertex 147.6 -69.1 -80.9
endloop
endfacet
facet normal -0.35 -0.69 -0.64
outer loop
vertex 108.3 -74.2 -53.9
vertex 147.6 -69.1 -80.9
vertex 147.6 -86.1 -62.6
endloop
endfacet
facet normal 0.31 0.70 0.64
outer loop
vertex 147.6 -93.3 -67.8
vertex 187.1 -103.9 -75.5
vertex 187.1 -83.4 -97.7
endloop
endfacet
facet normal 0.31 0.70 0.64
outer loop
vertex 147.6 -93.3 -67.8
vertex 187.1 -83.4 -97.7
vertex 147.6 -74.9 -87.7
endloop
endfacet
facet normal -0.31 -0.70 -0.64
outer loop
vertex 147.6 -86.1 -62.6
vertex 147.6 -69.1 -80.9
vertex 187.1 -77.7 -91
endloop
endfacet
facet normal -0.31 -0.70 -0.64
outer loop
vertex 147.6 -86.1 -62.6
vertex 187.1 -77.7 -91
vertex 187.1 -96.8 -70.3
endloop
endfacet
facet normal 0.28 0.71 0.65
outer loop
vertex 187.1 -103.9 -75.5
vertex 227 -113.3 -82.3
vertex 227 -90.9 -106.5
endloop
endfacet
facet normal 0.28 0.71 0.65
outer loop
vertex 187.1 -103.9 -75.5
vertex 227 -90.9 -106.5
vertex 187.1 -83.4 -97.7
endloop
endfacet
facet normal -0.28 -0.71 -0.65
outer loop
vertex 187.1 -96.8 -70.3
vertex 187.1 -77.7 -91
vertex 227 -85.2 -99.8
endloop
endfacet
facet normal -0.28 -0.71 -0.65
outer loop
vertex 187.1 -96.8 -70.3
vertex 227 -85.2 -99.8
vertex 227 -106.1 -77.1
endloop
endfacet
facet normal 0.24 0.71 0.66
outer loop
vertex 227 -113.3 -82.3
vertex 267.1 -121.4 -88.2
vertex 267.1 -97.4 -114.1
endloop
endfacet
facet normal 0.24 0.71 0.66
outer loop
vertex 227 -113.3 -82.3
vertex 267.1 -97.4 -114.1
vertex 227 -90.9 -106.5
endloop
endfacet
facet normal -0.24 -0.71 -0.66
outer loop
vertex 227 -106.1 -77.1
vertex 227 -85.2 -99.8
vertex 267.1 -91.7 -107.3
endloop
endfacet
facet normal -0.24 -0.71 -0.66
outer loop
vertex 227 -106.1 -77.1
vertex 267.1 -91.7 -107.3
vertex 267.1 -114.2 -83
endloop
endfacet
facet normal 0.20 0.72 0.66
outer loop
vertex 267.1 -121.4 -88.2
vertex 307.6 -128.2 -93.1
vertex 307.6 -102.9 -120.5
endloop
endfacet
facet normal 0.20 0.72 0.66
outer loop
vertex 267.1 -121.4 -88.2
vertex 307.6 -102.9 -120.5
vertex 267.1 -97.4 -114.1
endloop
endfacet
facet normal -0.20 -0.72 -0.66
outer loop
vertex 267.1 -114.2 -83
vertex 267.1 -91.7 -107.3
vertex 307.6 -97.1 -113.7
endloop
endfacet
facet normal -0.20 -0.72 -0.66
outer loop
vertex 267.1 -114.2 -83
vertex 307.6 -97.1 -113.7
vertex 307.6 -121 -87.9
endloop
endfacet
facet normal 0.18 0.72 0.67
outer loop
vertex 307.6 -128.2 -93.1
vertex 323.8 -130.5 -94.8
vertex 323.8 -104.8 -122.7
endloop
endfacet
facet normal 0.18 0.72 0.67
outer loop
vertex 307.6 -128.2 -93.1
vertex 323.8 -104.8 -122.7
vertex 307.6 -102.9 -120.5
endloop
endfacet
facet normal -0.18 -0.72 -0.67
outer loop
vertex 307.6 -121 -87.9
vertex 307.6 -97.1 -113.7
vertex 323.8 -99 -115.9
endloop
endfacet
facet normal -0.18 -0.72 -0.67
outer loop
vertex 307.6 -121 -87.9
vertex 323.8 -99 -115.9
vertex 323.8 -123.4 -89.6
endloop
endfacet
facet normal 0.00 0.56 0.83
outer loop
vertex -393.4 -55.3 -64.7
vertex -260.1 -55.3 -64.7
vertex -260.1 -38.6 -75.8
endloop
endfacet
facet normal 0.00 0.56 0.83
outer loop
vertex -393.4 -55.3 -64.7
vertex -260.1 -38.6 -75.8
vertex -393.4 -38.6 -75.8
endloop
endfacet
facet normal 0.00 -0.56 -0.83
outer loop
vertex -393.4 -49.5 -58
vertex -393.4 -34.6 -67.9
vertex -260.1 -34.6 -67.9
endloop
endfacet
facet normal 0.00 -0.56 -0.83
outer loop
vertex -393.4 -49.5 -58
vertex -260.1 -34.6 -67.9
vertex -260.1 -49.5 -58
endloop
endfacet
facet normal 0.00 0.56 0.83
outer loop
vertex -260.1 -55.3 -64.7
vertex -126.8 -55.3 -64.7
vertex -126.8 -38.6 -75.8
endloop
endfacet
facet normal 0.00 0.56 0.83
outer loop
vertex -260.1 -55.3 -64.7
vertex -126.8 -38.6 -75.8
vertex -260.1 -38.6 -75.8
endloop
endfacet
facet normal 0.00 -0.56 -0.83
outer loop
vertex -260.1 -49.5 -58
vertex -260.1 -34.6 -67.9
vertex -126.8 -34.6 -67.9
endloop
endfacet
facet normal 0.00 -0.56 -0.83
outer loop
vertex -260.1 -49.5 -58
vertex -126.8 -34.6 -67.9
vertex -126.8 -49.5 -58
endloop
endfacet
facet normal -0.09 0.55 0.83
outer loop
vertex -126.8 -55.3 -64.7
vertex -63.4 -51.5 -60.3
vertex -63.4 -36 -70.6
endloop
endfacet
facet normal -0.09 0.55 0.83
outer loop
vertex -126.8 -55.3 -64.7
vertex -63.4 -36 -70.6
vertex -126.8 -38.6 -75.8
endloop
endfacet
facet normal 0.09 -0.55 -0.83
outer loop
vertex -126.8 -49.5 -58
vertex -126.8 -34.6 -67.9
vertex -63.4 -32 -62.7
endloop
endfacet
facet normal 0.09 -0.55 -0.83
outer loop
vertex -126.8 -49.5 -58
vertex -63.4 -32 -62.7
vertex -63.4 -45.7 -53.5
endloop
endfacet
facet normal -0.50 0.48 0.72
outer loop
vertex -63.4 -51.5 -60.3
vertex -46.5 -45.1 -52.8
vertex -46.5 -31.6 -61.9
endloop
endfacet
facet normal -0.50 0.48 0.72
outer loop
vertex -63.4 -51.5 -60.3
vertex -46.5 -31.6 -61.9
vertex -63.4 -36 -70.6
endloop
endfacet
facet normal 0.50 -0.48 -0.72
outer loop
vertex -63.4 -45.7 -53.5
vertex -63.4 -32 -62.7
vertex -46.5 -27.5 -54
endloop
endfacet
facet normal 0.50 -0.48 -0.72
outer loop
vertex -63.4 -45.7 -53.5
vertex -46.5 -27.5 -54
vertex -46.5 -39.4 -46.1
endloop
endfacet
facet normal -0.50 0.48 0.72
outer loop
vertex -46.5 -45.1 -52.8
vertex -31.1 -39.4 -46.1
vertex -31.1 -27.5 -54
endloop
endfacet
facet normal -0.50 0.48 0.72
outer loop
vertex -46.5 -45.1 -52.8
vertex -31.1 -27.5 -54
vertex -46.5 -31.6 -61.9
endloop
endfacet
facet normal 0.50 -0.48 -0.72
outer loop
vertex -46.5 -39.4 -46.1
vertex -46.5 -27.5 -54
vertex -31.1 -23.5 -46.2
endloop
endfacet
facet normal 0.50 -0.48 -0.72
outer loop
vertex -46.5 -39.4 -46.1
vertex -31.1 -23.5 -46.2
vertex -31.1 -33.6 -39.4
endloop
endfacet
facet normal -0.40 0.51 0.76
outer loop
vertex -31.1 -39.4 -46.1
vertex -21.2 -36.6 -42.9
vertex -21.2 -25.6 -50.2
endloop
endfacet
facet normal -0.40 0.51 0.76
outer loop
vertex -31.1 -39.4 -46.1
vertex -21.2 -25.6 -50.2
vertex -31.1 -27.5 -54
endloop
endfacet
facet normal 0.40 -0.51 -0.76
outer loop
vertex -31.1 -33.6 -39.4
vertex -31.1 -23.5 -46.2
vertex -21.2 -21.6 -42.3
endloop
endfacet
facet normal 0.40 -0.51 -0.76
outer loop
vertex -31.1 -33.6 -39.4
vertex -21.2 -21.6 -42.3
vertex -21.2 -30.9 -36.1
endloop
endfacet
facet normal -0.24 0.54 0.81
outer loop
vertex -21.2 -36.6 -42.9
vertex -10.8 -34.9 -40.9
vertex -10.8 -24.4 -47.9
endloop
endfacet
facet normal -0.24 0.54 0.81
outer loop
vertex -21.2 -36.6 -42.9
vertex -10.8 -24.4 -47.9
vertex -21.2 -25.6 -50.2
endloop
endfacet
facet normal 0.24 -0.54 -0.81
outer loop
vertex -21.2 -30.9 -36.1
vertex -21.2 -21.6 -42.3
vertex -10.8 -20.4 -40
endloop
endfacet
facet normal 0.24 -0.54 -0.81
outer loop
vertex -21.2 -30.9 -36.1
vertex -10.8 -20.4 -40
vertex -10.8 -29.2 -34.1
endloop
endfacet
facet normal -0.08 0.55 0.83
outer loop
vertex -10.8 -34.9 -40.9
vertex 0 -34.3 -40.2
vertex 0 -24 -47.1
endloop
endfacet
facet normal -0.08 0.55 0.83
outer loop
vertex -10.8 -34.9 -40.9
vertex 0 -24 -47.1
vertex -10.8 -24.4 -47.9
endloop
endfacet
facet normal 0.08 -0.55 -0.83
outer loop
vertex -10.8 -29.2 -34.1
vertex -10.8 -20.4 -40
vertex 0 -20 -39.2
endloop
endfacet
facet normal 0.08 -0.55 -0.83
outer loop
vertex -10.8 -29.2 -34.1
vertex 0 -20 -39.2
vertex 0 -28.6 -33.5
endloop
endfacet
facet normal 0.10 0.55 0.83
outer loop
vertex 0 -34.3 -40.2
vertex 3.3 -34.5 -40.4
vertex 3.3 -24.1 -47.4
endloop
endfacet
facet normal 0.10 0.55 0.83
outer loop
vertex 0 -34.3 -40.2
vertex 3.3 -24.1 -47.4
vertex 0 -24 -47.1
endloop
endfacet
facet normal -0.10 -0.55 -0.83
outer loop
vertex 0 -28.6 -33.5
vertex 0 -20 -39.2
vertex 3.3 -20.1 -39.5
endloop
endfacet
facet normal -0.10 -0.55 -0.83
outer loop
vertex 0 -28.6 -33.5
vertex 3.3 -20.1 -39.5
vertex 3.3 -28.8 -33.7
endloop
endfacet
facet normal 0.29 0.53 0.80
outer loop
vertex 3.3 -34.5 -40.4
vertex 6.5 -35.2 -41.2
vertex 6.5 -24.6 -48.3
endloop
endfacet
facet normal 0.29 0.53 0.80
outer loop
vertex 3.3 -34.5 -40.4
vertex 6.5 -24.6 -48.3
vertex 3.3 -24.1 -47.4
endloop
endfacet
facet normal -0.29 -0.53 -0.80
outer loop
vertex 3.3 -28.8 -33.7
vertex 3.3 -20.1 -39.5
vertex 6.5 -20.6 -40.4
endloop
endfacet
facet normal -0.29 -0.53 -0.80
outer loop
vertex 3.3 -28.8 -33.7
vertex 6.5 -20.6 -40.4
vertex 6.5 -29.4 -34.5
endloop
endfacet
facet normal 0.44 0.50 0.75
outer loop
vertex 6.5 -35.2 -41.2
vertex 30.7 -43 -50.4
vertex 30.7 -30.1 -59
endloop
endfacet
facet normal 0.44 0.50 0.75
outer loop
vertex 6.5 -35.2 -41.2
vertex 30.7 -30.1 -59
vertex 6.5 -24.6 -48.3
endloop
endfacet
facet normal -0.44 -0.50 -0.75
outer loop
vertex 6.5 -29.4 -34.5
vertex 6.5 -20.6 -40.4
vertex 30.7 -26.1 -51.1
endloop
endfacet
facet normal -0.44 -0.50 -0.75
outer loop
vertex 6.5 -29.4 -34.5
vertex 30.7 -26.1 -51.1
vertex 30.7 -37.3 -43.6
endloop
endfacet
facet normal 0.42 0.50 0.76
outer loop
vertex 30.7 -43 -50.4
vertex 69.4 -54.7 -64
vertex 69.4 -38.2 -75
endloop
endfacet
facet normal 0.42 0.50 0.76
outer loop
vertex 30.7 -43 -50.4
vertex 69.4 -38.2 -75
vertex 30.7 -30.1 -59
endloop
endfacet
facet normal -0.42 -0.50 -0.76
outer loop
vertex 30.7 -37.3 -43.6
vertex 30.7 -26.1 -51.1
vertex 69.4 -34.2 -67.1
endloop
endfacet
facet normal -0.42 -0.50 -0.76
outer loop
vertex 30.7 -37.3 -43.6
vertex 69.4 -34.2 -67.1
vertex 69.4 -48.9 -57.3
endloop
endfacet
facet normal 0.38 0.51 0.77
outer loop
vertex 69.4 -54.7 -64
vertex 108.3 -65.3 -76.4
vertex 108.3 -45.6 -89.6
endloop
endfacet
facet normal 0.38 0.51 0.77
outer loop
vertex 69.4 -54.7 -64
vertex 108.3 -45.6 -89.6
vertex 69.4 -38.2 -75
endloop
endfacet
facet normal -0.38 -0.51 -0.77
outer loop
vertex 69.4 -48.9 -57.3
vertex 69.4 -34.2 -67.1
vertex 108.3 -41.6 -81.7
endloop
endfacet
facet normal -0.38 -0.51 -0.77
outer loop
vertex 69.4 -48.9 -57.3
vertex 108.3 -41.6 -81.7
vertex 108.3 -59.5 -69.7
endloop
endfacet
facet normal 0.35 0.52 0.78
outer loop
vertex 108.3 -65.3 -76.4
vertex 147.6 -74.9 -87.7
vertex 147.6 -52.3 -102.7
endloop
endfacet
facet normal 0.35 0.52 0.78
outer loop
vertex 108.3 -65.3 -76.4
vertex 147.6 -52.3 -102.7
vertex 108.3 -45.6 -89.6
endloop
endfacet
facet normal -0.35 -0.52 -0.78
outer loop
vertex 108.3 -59.5 -69.7
vertex 108.3 -41.6 -81.7
vertex 147.6 -48.3 -94.8
endloop
endfacet
facet normal -0.35 -0.52 -0.78
outer loop
vertex 108.3 -59.5 -69.7
vertex 147.6 -48.3 -94.8
vertex 147.6 -69.1 -80.9
endloop
endfacet
facet normal 0.31 0.53 0.79
outer loop
vertex 147.6 -74.9 -87.7
vertex 187.1 -83.4 -97.7
vertex 187.1 -58.3 -114.5
endloop
endfacet
facet normal 0.31 0.53 0.79
outer loop
vertex 147.6 -74.9 -87.7
vertex 187.1 -58.3 -114.5
vertex 147.6 -52.3 -102.7
endloop
endfacet
facet normal -0.31 -0.53 -0.79
outer loop
vertex 147.6 -69.1 -80.9
vertex 147.6 -48.3 -94.8
vertex 187.1 -54.3 -106.6
endloop
endfacet
facet normal -0.31 -0.53 -0.79
outer loop
vertex 147.6 -69.1 -80.9
vertex 187.1 -54.3 -106.6
vertex 187.1 -77.7 -91
endloop
endfacet
facet normal 0.28 0.53 0.80
outer loop
vertex 187.1 -83.4 -97.7
vertex 227 -90.9 -106.5
vertex 227 -63.6 -124.8
endloop
endfacet
facet normal 0.28 0.53 0.80
outer loop
vertex 187.1 -83.4 -97.7
vertex 227 -63.6 -124.8
vertex 187.1 -58.3 -114.5
endloop
endfacet
facet normal -0.28 -0.53 -0.80
outer loop
vertex 187.1 -77.7 -91
vertex 187.1 -54.3 -106.6
vertex 227 -59.6 -116.9
endloop
endfacet
facet normal -0.28 -0.53 -0.80
outer loop
vertex 187.1 -77.7 -91
vertex 227 -59.6 -116.9
vertex 227 -85.2 -99.8
endloop
endfacet
facet normal 0.24 0.54 0.81
outer loop
vertex 227 -90.9 -106.5
vertex 267.1 -97.4 -114.1
vertex 267.1 -68.1 -133.7
endloop
endfacet
facet normal 0.24 0.54 0.81
outer loop
vertex 227 -90.9 -106.5
vertex 267.1 -68.1 -133.7
vertex 227 -63.6 -124.8
endloop
endfacet
facet normal -0.24 -0.54 -0.81
outer loop
vertex 227 -85.2 -99.8
vertex 227 -59.6 -116.9
vertex 267.1 -64.1 -125.8
endloop
endfacet
facet normal -0.24 -0.54 -0.81
outer loop
vertex 227 -85.2 -99.8
vertex 267.1 -64.1 -125.8
vertex 267.1 -91.7 -107.3
endloop
endfacet
facet normal 0.20 0.54 0.81
outer loop
vertex 267.1 -97.4 -114.1
vertex 307.6 -102.9 -120.5
vertex 307.6 -71.9 -141.1
endloop
endfacet
facet normal 0.20 0.54 0.81
outer loop
vertex 267.1 -97.4 -114.1
vertex 307.6 -71.9 -141.1
vertex 267.1 -68.1 -133.7
endloop
endfacet
facet normal -0.20 -0.54 -0.81
outer loop
vertex 267.1 -91.7 -107.3
vertex 267.1 -64.1 -125.8
vertex 307.6 -67.9 -133.3
endloop
endfacet
facet normal -0.20 -0.54 -0.81
outer loop
vertex 267.1 -91.7 -107.3
vertex 307.6 -67.9 -133.3
vertex 307.6 -97.1 -113.7
endloop
endfacet
facet normal 0.18 0.55 0.82
outer loop
vertex 307.6 -102.9 -120.5
vertex 323.8 -104.8 -122.7
vertex 323.8 -73.2 -143.7
endloop
endfacet
facet normal 0.18 0.55 0.82
outer loop
vertex 307.6 -102.9 -120.5
vertex 323.8 -73.2 -143.7
vertex 307.6 -71.9 -141.1
endloop
endfacet
facet normal -0.18 -0.55 -0.82
outer loop
vertex 307.6 -97.1 -113.7
vertex 307.6 -67.9 -133.3
vertex 323.8 -69.2 -135.9
endloop
endfacet
facet normal -0.18 -0.55 -0.82
outer loop
vertex 307.6 -97.1 -113.7
vertex 323.8 -69.2 -135.9
vertex 323.8 -99 -115.9
endloop
endfacet
facet normal 0.00 0.35 0.94
outer loop
vertex -393.4 -38.6 -75.8
vertex -260.1 -38.6 -75.8
vertex -260.1 -19.9 -82.7
endloop
endfacet
facet normal 0.00 0.35 0.94
outer loop
vertex -393.4 -38.6 -75.8
vertex -260.1 -19.9 -82.7
vertex -393.4 -19.9 -82.7
endloop
endfacet
facet normal 0.00 -0.35 -0.94
outer loop
vertex -393.4 -34.6 -67.9
vertex -393.4 -17.8 -74.1
vertex -260.1 -17.8 -74.1
endloop
endfacet
facet normal 0.00 -0.35 -0.94
outer loop
vertex -393.4 -34.6 -67.9
vertex -260.1 -17.8 -74.1
vertex -260.1 -34.6 -67.9
endloop
endfacet
facet normal 0.00 0.35 0.94
outer loop
vertex -260.1 -38.6 -75.8
vertex -126.8 -38.6 -75.8
vertex -126.8 -19.9 -82.7
endloop
endfacet
facet normal 0.00 0.35 0.94
outer loop
vertex -260.1 -38.6 -75.8
vertex -126.8 -19.9 -82.7
vertex -260.1 -19.9 -82.7
endloop
endfacet
facet normal 0.00 -0.35 -0.94
outer loop
vertex -260.1 -34.6 -67.9
vertex -260.1 -17.8 -74.1
vertex -126.8 -17.8 -74.1
endloop
endfacet
facet normal 0.00 -0.35 -0.94
outer loop
vertex -260.1 -34.6 -67.9
vertex -126.8 -17.8 -74.1
vertex -126.8 -34.6 -67.9
endloop
endfacet
facet normal -0.09 0.34 0.93
outer loop
vertex -126.8 -38.6 -75.8
vertex -63.4 -36 -70.6
vertex -63.4 -18.5 -77
endloop
endfacet
facet normal -0.09 0.34 0.93
outer loop
vertex -126.8 -38.6 -75.8
vertex -63.4 -18.5 -77
vertex -126.8 -19.9 -82.7
endloop
endfacet
facet normal 0.09 -0.34 -0.93
outer loop
vertex -126.8 -34.6 -67.9
vertex -126.8 -17.8 -74.1
vertex -63.4 -16.4 -68.4
endloop
endfacet
facet normal 0.09 -0.34 -0.93
outer loop
vertex -126.8 -34.6 -67.9
vertex -63.4 -16.4 -68.4
vertex -63.4 -32 -62.7
endloop
endfacet
facet normal -0.50 0.30 0.81
outer loop
vertex -63.4 -36 -70.6
vertex -46.5 -31.6 -61.9
vertex -46.5 -16.2 -67.6
endloop
endfacet
facet normal -0.50 0.30 0.81
outer loop
vertex -63.4 -36 -70.6
vertex -46.5 -16.2 -67.6
vertex -63.4 -18.5 -77
endloop
endfacet
facet normal 0.50 -0.30 -0.81
outer loop
vertex -63.4 -32 -62.7
vertex -63.4 -16.4 -68.4
vertex -46.5 -14.2 -59
endloop
endfacet
facet normal 0.50 -0.30 -0.81
outer loop
vertex -63.4 -32 -62.7
vertex -46.5 -14.2 -59
vertex -46.5 -27.5 -54
endloop
endfacet
facet normal -0.50 0.30 0.81
outer loop
vertex -46.5 -31.6 -61.9
vertex -31.1 -27.5 -54
vertex -31.1 -14.2 -59
endloop
endfacet
facet normal -0.50 0.30 0.81
outer loop
vertex -46.5 -31.6 -61.9
vertex -31.1 -14.2 -59
vertex -46.5 -16.2 -67.6
endloop
endfacet
facet normal 0.50 -0.30 -0.81
outer loop
vertex -46.5 -27.5 -54
vertex -46.5 -14.2 -59
vertex -31.1 -12.1 -50.4
endloop
endfacet
facet normal 0.50 -0.30 -0.81
outer loop
vertex -46.5 -27.5 -54
vertex -31.1 -12.1 -50.4
vertex -31.1 -23.5 -46.2
endloop
endfacet
facet normal -0.40 0.32 0.86
outer loop
vertex -31.1 -27.5 -54
vertex -21.2 -25.6 -50.2
vertex -21.2 -13.2 -54.8
endloop
endfacet
facet normal -0.40 0.32 0.86
outer loop
vertex -31.1 -27.5 -54
vertex -21.2 -13.2 -54.8
vertex -31.1 -14.2 -59
endloop
endfacet
facet normal 0.40 -0.32 -0.86
outer loop
vertex -31.1 -23.5 -46.2
vertex -31.1 -12.1 -50.4
vertex -21.2 -11.1 -46.2
endloop
endfacet
facet normal 0.40 -0.32 -0.86
outer loop
vertex -31.1 -23.5 -46.2
vertex -21.2 -11.1 -46.2
vertex -21.2 -21.6 -42.3
endloop
endfacet
facet normal -0.24 0.34 0.91
outer loop
vertex -21.2 -25.6 -50.2
vertex -10.8 -24.4 -47.9
vertex -10.8 -12.5 -52.3
endloop
endfacet
facet normal -0.24 0.34 0.91
outer loop
vertex -21.2 -25.6 -50.2
vertex -10.8 -12.5 -52.3
vertex -21.2 -13.2 -54.8
endloop
endfacet
facet normal 0.24 -0.34 -0.91
outer loop
vertex -21.2 -21.6 -42.3
vertex -21.2 -11.1 -46.2
vertex -10.8 -10.5 -43.7
endloop
endfacet
facet normal 0.24 -0.34 -0.91
outer loop
vertex -21.2 -21.6 -42.3
vertex -10.8 -10.5 -43.7
vertex -10.8 -20.4 -40
endloop
endfacet
facet normal -0.08 0.34 0.94
outer loop
vertex -10.8 -24.4 -47.9
vertex 0 -24 -47.1
vertex 0 -12.3 -51.4
endloop
endfacet
facet normal -0.08 0.34 0.94
outer loop
vertex -10.8 -24.4 -47.9
vertex 0 -12.3 -51.4
vertex -10.8 -12.5 -52.3
endloop
endfacet
facet normal 0.08 -0.34 -0.94
outer loop
vertex -10.8 -20.4 -40
vertex -10.8 -10.5 -43.7
vertex 0 -10.3 -42.8
endloop
endfacet
facet normal 0.08 -0.34 -0.94
outer loop
vertex -10.8 -20.4 -40
vertex 0 -10.3 -42.8
vertex 0 -20 -39.2
endloop
endfacet
facet normal 0.10 0.34 0.93
outer loop
vertex 0 -24 -47.1
vertex 3.3 -24.1 -47.4
vertex 3.3 -12.4 -51.7
endloop
endfacet
facet normal 0.10 0.34 0.93
outer loop
vertex 0 -24 -47.1
vertex 3.3 -12.4 -51.7
vertex 0 -12.3 -51.4
endloop
endfacet
facet normal -0.10 -0.34 -0.93
outer loop
vertex 0 -20 -39.2
vertex 0 -10.3 -42.8
vertex 3.3 -10.4 -43.1
endloop
endfacet
facet normal -0.10 -0.34 -0.93
outer loop
vertex 0 -20 -39.2
vertex 3.3 -10.4 -43.1
vertex 3.3 -20.1 -39.5
endloop
endfacet
facet normal 0.29 0.33 0.90
outer loop
vertex 3.3 -24.1 -47.4
vertex 6.5 -24.6 -48.3
vertex 6.5 -12.6 -52.7
endloop
endfacet
facet normal 0.29 0.33 0.90
outer loop
vertex 3.3 -24.1 -47.4
vertex 6.5 -12.6 -52.7
vertex 3.3 -12.4 -51.7
endloop
endfacet
facet normal -0.29 -0.33 -0.90
outer loop
vertex 3.3 -20.1 -39.5
vertex 3.3 -10.4 -43.1
vertex 6.5 -10.6 -44.1
endloop
endfacet
facet normal -0.29 -0.33 -0.90
outer loop
vertex 3.3 -20.1 -39.5
vertex 6.5 -10.6 -44.1
vertex 6.5 -20.6 -40.4
endloop
endfacet
facet normal 0.44 0.31 0.84
outer loop
vertex 6.5 -24.6 -48.3
vertex 30.7 -30.1 -59
vertex 30.7 -15.5 -64.4
endloop
endfacet
facet normal 0.44 0.31 0.84
outer loop
vertex 6.5 -24.6 -48.3
vertex 30.7 -15.5 -64.4
vertex 6.5 -12.6 -52.7
endloop
endfacet
facet normal -0.44 -0.31 -0.84
outer loop
vertex 6.5 -20.6 -40.4
vertex 6.5 -10.6 -44.1
vertex 30.7 -13.4 -55.8
endloop
endfacet
facet normal -0.44 -0.31 -0.84
outer loop
vertex 6.5 -20.6 -40.4
vertex 30.7 -13.4 -55.8
vertex 30.7 -26.1 -51.1
endloop
endfacet
facet normal 0.42 0.31 0.85
outer loop
vertex 30.7 -30.1 -59
vertex 69.4 -38.2 -75
vertex 69.4 -19.7 -81.9
endloop
endfacet
facet normal 0.42 0.31 0.85
outer loop
vertex 30.7 -30.1 -59
vertex 69.4 -19.7 -81.9
vertex 30.7 -15.5 -64.4
endloop
endfacet
facet normal -0.42 -0.31 -0.85
outer loop
vertex 30.7 -26.1 -51.1
vertex 30.7 -13.4 -55.8
vertex 69.4 -17.6 -73.3
endloop
endfacet
facet normal -0.42 -0.31 -0.85
outer loop
vertex 30.7 -26.1 -51.1
vertex 69.4 -17.6 -73.3
vertex 69.4 -34.2 -67.1
endloop
endfacet
facet normal 0.38 0.32 0.87
outer loop
vertex 69.4 -38.2 -75
vertex 108.3 -45.6 -89.6
vertex 108.3 -23.5 -97.8
endloop
endfacet
facet normal 0.38 0.32 0.87
outer loop
vertex 69.4 -38.2 -75
vertex 108.3 -23.5 -97.8
vertex 69.4 -19.7 -81.9
endloop
endfacet
facet normal -0.38 -0.32 -0.87
outer loop
vertex 69.4 -34.2 -67.1
vertex 69.4 -17.6 -73.3
vertex 108.3 -21.4 -89.2
endloop
endfacet
facet normal -0.38 -0.32 -0.87
outer loop
vertex 69.4 -34.2 -67.1
vertex 108.3 -21.4 -89.2
vertex 108.3 -41.6 -81.7
endloop
endfacet
facet normal 0.35 0.32 0.88
outer loop
vertex 108.3 -45.6 -89.6
vertex 147.6 -52.3 -102.7
vertex 147.6 -26.9 -112.1
endloop
endfacet
facet normal 0.35 0.32 0.88
outer loop
vertex 108.3 -45.6 -89.6
vertex 147.6 -26.9 -112.1
vertex 108.3 -23.5 -97.8
endloop
endfacet
facet normal -0.35 -0.32 -0.88
outer loop
vertex 108.3 -41.6 -81.7
vertex 108.3 -21.4 -89.2
vertex 147.6 -24.8 -103.5
endloop
endfacet
facet normal -0.35 -0.32 -0.88
outer loop
vertex 108.3 -41.6 -81.7
vertex 147.6 -24.8 -103.5
vertex 147.6 -48.3 -94.8
endloop
endfacet
facet normal 0.31 0.33 0.89
outer loop
vertex 147.6 -52.3 -102.7
vertex 187.1 -58.3 -114.5
vertex 187.1 -30 -124.9
endloop
endfacet
facet normal 0.31 0.33 0.89
outer loop
vertex 147.6 -52.3 -102.7
vertex 187.1 -30 -124.9
vertex 147.6 -26.9 -112.1
endloop
endfacet
facet normal -0.31 -0.33 -0.89
outer loop
vertex 147.6 -48.3 -94.8
vertex 147.6 -24.8 -103.5
vertex 187.1 -27.9 -116.3
endloop
endfacet
facet normal -0.31 -0.33 -0.89
outer loop
vertex 147.6 -48.3 -94.8
vertex 187.1 -27.9 -116.3
vertex 187.1 -54.3 -106.6
endloop
endfacet
facet normal 0.28 0.33 0.90
outer loop
vertex 187.1 -58.3 -114.5
vertex 227 -63.6 -124.8
vertex 227 -32.7 -136.2
endloop
endfacet
facet normal 0.28 0.33 0.90
outer loop
vertex 187.1 -58.3 -114.5
vertex 227 -32.7 -136.2
vertex 187.1 -30 -124.9
endloop
endfacet
facet normal -0.28 -0.33 -0.90
outer loop
vertex 187.1 -54.3 -106.6
vertex 187.1 -27.9 -116.3
vertex 227 -30.6 -127.6
endloop
endfacet
facet normal -0.28 -0.33 -0.90
outer loop
vertex 187.1 -54.3 -106.6
vertex 227 -30.6 -127.6
vertex 227 -59.6 -116.9
endloop
endfacet
facet normal 0.24 0.34 0.91
outer loop
vertex 227 -63.6 -124.8
vertex 267.1 -68.1 -133.7
vertex 267.1 -35 -145.9
endloop
endfacet
facet normal 0.24 0.34 0.91
outer loop
vertex 227 -63.6 -124.8
vertex 267.1 -35 -145.9
vertex 227 -32.7 -136.2
endloop
endfacet
facet normal -0.24 -0.34 -0.91
outer loop
vertex 227 -59.6 -116.9
vertex 227 -30.6 -127.6
vertex 267.1 -33 -137.3
endloop
endfacet
facet normal -0.24 -0.34 -0.91
outer loop
vertex 227 -59.6 -116.9
vertex 267.1 -33 -137.3
vertex 267.1 -64.1 -125.8
endloop
endfacet
facet normal 0.20 0.34 0.92
outer loop
vertex 267.1 -68.1 -133.7
vertex 307.6 -71.9 -141.1
vertex 307.6 -37 -154
endloop
endfacet
facet normal 0.20 0.34 0.92
outer loop
vertex 267.1 -68.1 -133.7
vertex 307.6 -37 -154
vertex 267.1 -35 -145.9
endloop
endfacet
facet normal -0.20 -0.34 -0.92
outer loop
vertex 267.1 -64.1 -125.8
vertex 267.1 -33 -137.3
vertex 307.6 -34.9 -145.4
endloop
endfacet
facet normal -0.20 -0.34 -0.92
outer loop
vertex 267.1 -64.1 -125.8
vertex 307.6 -34.9 -145.4
vertex 307.6 -67.9 -133.3
endloop
endfacet
facet normal 0.18 0.34 0.92
outer loop
vertex 307.6 -71.9 -141.1
vertex 323.8 -73.2 -143.7
vertex 323.8 -37.7 -156.9
endloop
endfacet
facet normal 0.18 0.34 0.92
outer loop
vertex 307.6 -71.9 -141.1
vertex 323.8 -37.7 -156.9
vertex 307.6 -37 -154
endloop
endfacet
facet normal -0.18 -0.34 -0.92
outer loop
vertex 307.6 -67.9 -133.3
vertex 307.6 -34.9 -145.4
vertex 323.8 -35.6 -148.3
endloop
endfacet
facet normal -0.18 -0.34 -0.92
outer loop
vertex 307.6 -67.9 -133.3
vertex 323.8 -35.6 -148.3
vertex 323.8 -69.2 -135.9
endloop
endfacet
facet normal 0.00 0.12 0.99
outer loop
vertex -393.4 -19.9 -82.7
vertex -260.1 -19.9 -82.7
vertex -260.1 0 -85.1
endloop
endfacet
facet normal 0.00 0.12 0.99
outer loop
vertex -393.4 -19.9 -82.7
vertex -260.1 0 -85.1
vertex -393.4 0 -85.1
endloop
endfacet
facet normal 0.00 -0.12 -0.99
outer loop
vertex -393.4 -17.8 -74.1
vertex -393.4 0 -76.2
vertex -260.1 0 -76.2
endloop
endfacet
facet normal 0.00 -0.12 -0.99
outer loop
vertex -393.4 -17.8 -74.1
vertex -260.1 0 -76.2
vertex -260.1 -17.8 -74.1
endloop
endfacet
facet normal 0.00 0.12 0.99
outer loop
vertex -260.1 -19.9 -82.7
vertex -126.8 -19.9 -82.7
vertex -126.8 0 -85.1
endloop
endfacet
facet normal 0.00 0.12 0.99
outer loop
vertex -260.1 -19.9 -82.7
vertex -126.8 0 -85.1
vertex -260.1 0 -85.1
endloop
endfacet
facet normal 0.00 -0.12 -0.99
outer loop
vertex -260.1 -17.8 -74.1
vertex -260.1 0 -76.2
vertex -126.8 0 -76.2
endloop
endfacet
facet normal 0.00 -0.12 -0.99
outer loop
vertex -260.1 -17.8 -74.1
vertex -126.8 0 -76.2
vertex -126.8 -17.8 -74.1
endloop
endfacet
facet normal -0.09 0.12 0.99
outer loop
vertex -126.8 -19.9 -82.7
vertex -63.4 -18.5 -77
vertex -63.4 0 -79.2
endloop
endfacet
facet normal -0.09 0.12 0.99
outer loop
vertex -126.8 -19.9 -82.7
vertex -63.4 0 -79.2
vertex -126.8 0 -85.1
endloop
endfacet
facet normal 0.09 -0.12 -0.99
outer loop
vertex -126.8 -17.8 -74.1
vertex -126.8 0 -76.2
vertex -63.4 0 -70.4
endloop
endfacet
facet normal 0.09 -0.12 -0.99
outer loop
vertex -126.8 -17.8 -74.1
vertex -63.4 0 -70.4
vertex -63.4 -16.4 -68.4
endloop
endfacet
facet normal -0.50 0.10 0.86
outer loop
vertex -63.4 -18.5 -77
vertex -46.5 -16.2 -67.6
vertex -46.5 0 -69.5
endloop
endfacet
facet normal -0.50 0.10 0.86
outer loop
vertex -63.4 -18.5 -77
vertex -46.5 0 -69.5
vertex -63.4 0 -79.2
endloop
endfacet
facet normal 0.50 -0.10 -0.86
outer loop
vertex -63.4 -16.4 -68.4
vertex -63.4 0 -70.4
vertex -46.5 0 -60.7
endloop
endfacet
facet normal 0.50 -0.10 -0.86
outer loop
vertex -63.4 -16.4 -68.4
vertex -46.5 0 -60.7
vertex -46.5 -14.2 -59
endloop
endfacet
facet normal -0.50 0.10 0.86
outer loop
vertex -46.5 -16.2 -67.6
vertex -31.1 -14.2 -59
vertex -31.1 0 -60.7
endloop
endfacet
facet normal -0.50 0.10 0.86
outer loop
vertex -46.5 -16.2 -67.6
vertex -31.1 0 -60.7
vertex -46.5 0 -69.5
endloop
endfacet
facet normal 0.50 -0.10 -0.86
outer loop
vertex -46.5 -14.2 -59
vertex -46.5 0 -60.7
vertex -31.1 0 -51.8
endloop
endfacet
facet normal 0.50 -0.10 -0.86
outer loop
vertex -46.5 -14.2 -59
vertex -31.1 0 -51.8
vertex -31.1 -12.1 -50.4
endloop
endfacet
facet normal -0.40 0.11 0.91
outer loop
vertex -31.1 -14.2 -59
vertex -21.2 -13.2 -54.8
vertex -21.2 0 -56.4
endloop
endfacet
facet normal -0.40 0.11 0.91
outer loop
vertex -31.1 -14.2 -59
vertex -21.2 0 -56.4
vertex -31.1 0 -60.7
endloop
endfacet
facet normal 0.40 -0.11 -0.91
outer loop
vertex -31.1 -12.1 -50.4
vertex -31.1 0 -51.8
vertex -21.2 0 -47.5
endloop
endfacet
facet normal 0.40 -0.11 -0.91
outer loop
vertex -31.1 -12.1 -50.4
vertex -21.2 0 -47.5
vertex -21.2 -11.1 -46.2
endloop
endfacet
facet normal -0.24 0.11 0.96
outer loop
vertex -21.2 -13.2 -54.8
vertex -10.8 -12.5 -52.3
vertex -10.8 0 -53.7
endloop
endfacet
facet normal -0.24 0.11 0.96
outer loop
vertex -21.2 -13.2 -54.8
vertex -10.8 0 -53.7
vertex -21.2 0 -56.4
endloop
endfacet
facet normal 0.24 -0.11 -0.96
outer loop
vertex -21.2 -11.1 -46.2
vertex -21.2 0 -47.5
vertex -10.8 0 -44.9
endloop
endfacet
facet normal 0.24 -0.11 -0.96
outer loop
vertex -21.2 -11.1 -46.2
vertex -10.8 0 -44.9
vertex -10.8 -10.5 -43.7
endloop
endfacet
facet normal -0.08 0.12 0.99
outer loop
vertex -10.8 -12.5 -52.3
vertex 0 -12.3 -51.4
vertex 0 0 -52.9
endloop
endfacet
facet normal -0.08 0.12 0.99
outer loop
vertex -10.8 -12.5 -52.3
vertex 0 0 -52.9
vertex -10.8 0 -53.7
endloop
endfacet
facet normal 0.08 -0.12 -0.99
outer loop
vertex -10.8 -10.5 -43.7
vertex -10.8 0 -44.9
vertex 0 0 -44
endloop
endfacet
facet normal 0.08 -0.12 -0.99
outer loop
vertex -10.8 -10.5 -43.7
vertex 0 0 -44
vertex 0 -10.3 -42.8
endloop
endfacet
facet normal 0.10 0.12 0.99
outer loop
vertex 0 -12.3 -51.4
vertex 3.3 -12.4 -51.7
vertex 3.3 0 -53.2
endloop
endfacet
facet normal 0.10 0.12 0.99
outer loop
vertex 0 -12.3 -51.4
vertex 3.3 0 -53.2
vertex 0 0 -52.9
endloop
endfacet
facet normal -0.10 -0.12 -0.99
outer loop
vertex 0 -10.3 -42.8
vertex 0 0 -44
vertex 3.3 0 -44.3
endloop
endfacet
facet normal -0.10 -0.12 -0.99
outer loop
vertex 0 -10.3 -42.8
vertex 3.3 0 -44.3
vertex 3.3 -10.4 -43.1
endloop
endfacet
facet normal 0.29 0.11 0.95
outer loop
vertex 3.3 -12.4 -51.7
vertex 6.5 -12.6 -52.7
vertex 6.5 0 -54.2
endloop
endfacet
facet normal 0.29 0.11 0.95
outer loop
vertex 3.3 -12.4 -51.7
vertex 6.5 0 -54.2
vertex 3.3 0 -53.2
endloop
endfacet
facet normal -0.29 -0.11 -0.95
outer loop
vertex 3.3 -10.4 -43.1
vertex 3.3 0 -44.3
vertex 6.5 0 -45.3
endloop
endfacet
facet normal -0.29 -0.11 -0.95
outer loop
vertex 3.3 -10.4 -43.1
vertex 6.5 0 -45.3
vertex 6.5 -10.6 -44.1
endloop
endfacet
facet normal 0.44 0.11 0.89
outer loop
vertex 6.5 -12.6 -52.7
vertex 30.7 -15.5 -64.4
vertex 30.7 0 -66.2
endloop
endfacet
facet normal 0.44 0.11 0.89
outer loop
vertex 6.5 -12.6 -52.7
vertex 30.7 0 -66.2
vertex 6.5 0 -54.2
endloop
endfacet
facet normal -0.44 -0.11 -0.89
outer loop
vertex 6.5 -10.6 -44.1
vertex 6.5 0 -45.3
vertex 30.7 0 -57.4
endloop
endfacet
facet normal -0.44 -0.11 -0.89
outer loop
vertex 6.5 -10.6 -44.1
vertex 30.7 0 -57.4
vertex 30.7 -13.4 -55.8
endloop
endfacet
facet normal 0.42 0.11 0.90
outer loop
vertex 30.7 -15.5 -64.4
vertex 69.4 -19.7 -81.9
vertex 69.4 0 -84.2
endloop
endfacet
facet normal 0.42 0.11 0.90
outer loop
vertex 30.7 -15.5 -64.4
vertex 69.4 0 -84.2
vertex 30.7 0 -66.2
endloop
endfacet
facet normal -0.42 -0.11 -0.90
outer loop
vertex 30.7 -13.4 -55.8
vertex 30.7 0 -57.4
vertex 69.4 0 -75.3
endloop
endfacet
facet normal -0.42 -0.11 -0.90
outer loop
vertex 30.7 -13.4 -55.8
vertex 69.4 0 -75.3
vertex 69.4 -17.6 -73.3
endloop
endfacet
facet normal 0.38 0.11 0.92
outer loop
vertex 69.4 -19.7 -81.9
vertex 108.3 -23.5 -97.8
vertex 108.3 0 -100.5
endloop
endfacet
facet normal 0.38 0.11 0.92
outer loop
vertex 69.4 -19.7 -81.9
vertex 108.3 0 -100.5
vertex 69.4 0 -84.2
endloop
endfacet
facet normal -0.38 -0.11 -0.92
outer loop
vertex 69.4 -17.6 -73.3
vertex 69.4 0 -75.3
vertex 108.3 0 -91.7
endloop
endfacet
facet normal -0.38 -0.11 -0.92
outer loop
vertex 69.4 -17.6 -73.3
vertex 108.3 0 -91.7
vertex 108.3 -21.4 -89.2
endloop
endfacet
facet normal 0.35 0.11 0.93
outer loop
vertex 108.3 -23.5 -97.8
vertex 147.6 -26.9 -112.1
vertex 147.6 0 -115.3
endloop
endfacet
facet normal 0.35 0.11 0.93
outer loop
vertex 108.3 -23.5 -97.8
vertex 147.6 0 -115.3
vertex 108.3 0 -100.5
endloop
endfacet
facet normal -0.35 -0.11 -0.93
outer loop
vertex 108.3 -21.4 -89.2
vertex 108.3 0 -91.7
vertex 147.6 0 -106.4
endloop
endfacet
facet normal -0.35 -0.11 -0.93
outer loop
vertex 108.3 -21.4 -89.2
vertex 147.6 0 -106.4
vertex 147.6 -24.8 -103.5
endloop
endfacet
facet normal 0.31 0.11 0.94
outer loop
vertex 147.6 -26.9 -112.1
vertex 187.1 -30 -124.9
vertex 187.1 0 -128.5
endloop
endfacet
facet normal 0.31 0.11 0.94
outer loop
vertex 147.6 -26.9 -112.1
vertex 187.1 0 -128.5
vertex 147.6 0 -115.3
endloop
endfacet
facet normal -0.31 -0.11 -0.94
outer loop
vertex 147.6 -24.8 -103.5
vertex 147.6 0 -106.4
vertex 187.1 0 -119.6
endloop
endfacet
facet normal -0.31 -0.11 -0.94
outer loop
vertex 147.6 -24.8 -103.5
vertex 187.1 0 -119.6
vertex 187.1 -27.9 -116.3
endloop
endfacet
facet normal 0.28 0.11 0.95
outer loop
vertex 187.1 -30 -124.9
vertex 227 -32.7 -136.2
vertex 227 0 -140
endloop
endfacet
facet normal 0.28 0.11 0.95
outer loop
vertex 187.1 -30 -124.9
vertex 227 0 -140
vertex 187.1 0 -128.5
endloop
endfacet
facet normal -0.28 -0.11 -0.95
outer loop
vertex 187.1 -27.9 -116.3
vertex 187.1 0 -119.6
vertex 227 0 -131.2
endloop
endfacet
facet normal -0.28 -0.11 -0.95
outer loop
vertex 187.1 -27.9 -116.3
vertex 227 0 -131.2
vertex 227 -30.6 -127.6
endloop
endfacet
facet normal 0.24 0.11 0.96
outer loop
vertex 227 -32.7 -136.2
vertex 267.1 -35 -145.9
vertex 267.1 0 -150
endloop
endfacet
facet normal 0.24 0.11 0.96
outer loop
vertex 227 -32.7 -136.2
vertex 267.1 0 -150
vertex 227 0 -140
endloop
endfacet
facet normal -0.24 -0.11 -0.96
outer loop
vertex 227 -30.6 -127.6
vertex 227 0 -131.2
vertex 267.1 0 -141.2
endloop
endfacet
facet normal -0.24 -0.11 -0.96
outer loop
vertex 227 -30.6 -127.6
vertex 267.1 0 -141.2
vertex 267.1 -33 -137.3
endloop
endfacet
facet normal 0.20 0.12 0.97
outer loop
vertex 267.1 -35 -145.9
vertex 307.6 -37 -154
vertex 307.6 0 -158.4
endloop
endfacet
facet normal 0.20 0.12 0.97
outer loop
vertex 267.1 -35 -145.9
vertex 307.6 0 -158.4
vertex 267.1 0 -150
endloop
endfacet
facet normal -0.20 -0.12 -0.97
outer loop
vertex 267.1 -33 -137.3
vertex 267.1 0 -141.2
vertex 307.6 0 -149.6
endloop
endfacet
facet normal -0.20 -0.12 -0.97
outer loop
vertex 267.1 -33 -137.3
vertex 307.6 0 -149.6
vertex 307.6 -34.9 -145.4
endloop
endfacet
facet normal 0.18 0.12 0.98
outer loop
vertex 307.6 -37 -154
vertex 323.8 -37.7 -156.9
vertex 323.8 0 -161.3
endloop
endfacet
facet normal 0.18 0.12 0.98
outer loop
vertex 307.6 -37 -154
vertex 323.8 0 -161.3
vertex 307.6 0 -158.4
endloop
endfacet
facet normal -0.18 -0.12 -0.98
outer loop
vertex 307.6 -34.9 -145.4
vertex 307.6 0 -149.6
vertex 323.8 0 -152.5
endloop
endfacet
facet normal -0.18 -0.12 -0.98
outer loop
vertex 307.6 -34.9 -145.4
vertex 323.8 0 -152.5
vertex 323.8 -35.6 -148.3
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -393.4 76.2 0
vertex -260.1 76.2 0
vertex -260.1 85.1 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -393.4 76.2 0
vertex -260.1 85.1 0
vertex -393.4 85.1 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -260.1 76.2 0
vertex -126.8 76.2 0
vertex -126.8 85.1 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -260.1 76.2 0
vertex -126.8 85.1 0
vertex -260.1 85.1 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -126.8 76.2 0
vertex -63.4 70.4 0
vertex -63.4 79.2 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -126.8 76.2 0
vertex -63.4 79.2 0
vertex -126.8 85.1 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -63.4 70.4 0
vertex -46.5 60.7 0
vertex -46.5 69.5 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -63.4 70.4 0
vertex -46.5 69.5 0
vertex -63.4 79.2 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -46.5 60.7 0
vertex -31.1 51.8 0
vertex -31.1 60.7 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -46.5 60.7 0
vertex -31.1 60.7 0
vertex -46.5 69.5 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -31.1 51.8 0
vertex -21.2 47.5 0
vertex -21.2 56.4 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -31.1 51.8 0
vertex -21.2 56.4 0
vertex -31.1 60.7 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -21.2 47.5 0
vertex -10.8 44.9 0
vertex -10.8 53.7 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -21.2 47.5 0
vertex -10.8 53.7 0
vertex -21.2 56.4 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -10.8 44.9 0
vertex 0 44 0
vertex 0 52.9 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex -10.8 44.9 0
vertex 0 52.9 0
vertex -10.8 53.7 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 0 44 0
vertex 3.3 44.3 0
vertex 3.3 53.2 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 0 44 0
vertex 3.3 53.2 0
vertex 0 52.9 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 3.3 44.3 0
vertex 6.5 45.3 0
vertex 6.5 54.2 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 3.3 44.3 0
vertex 6.5 54.2 0
vertex 3.3 53.2 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 6.5 45.3 0
vertex 30.7 57.4 0
vertex 30.7 66.2 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 6.5 45.3 0
vertex 30.7 66.2 0
vertex 6.5 54.2 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 30.7 57.4 0
vertex 69.4 75.3 0
vertex 69.4 84.2 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 30.7 57.4 0
vertex 69.4 84.2 0
vertex 30.7 66.2 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 69.4 75.3 0
vertex 108.3 91.7 0
vertex 108.3 100.5 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 69.4 75.3 0
vertex 108.3 100.5 0
vertex 69.4 84.2 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 108.3 91.7 0
vertex 147.6 106.4 0
vertex 147.6 115.3 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 108.3 91.7 0
vertex 147.6 115.3 0
vertex 108.3 100.5 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 147.6 106.4 0
vertex 187.1 119.6 0
vertex 187.1 128.5 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 147.6 106.4 0
vertex 187.1 128.5 0
vertex 147.6 115.3 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 187.1 119.6 0
vertex 227 131.2 0
vertex 227 140 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 187.1 119.6 0
vertex 227 140 0
vertex 187.1 128.5 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 227 131.2 0
vertex 267.1 141.2 0
vertex 267.1 150 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 227 131.2 0
vertex 267.1 150 0
vertex 227 140 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 267.1 141.2 0
vertex 307.6 149.6 0
vertex 307.6 158.4 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 267.1 141.2 0
vertex 307.6 158.4 0
vertex 267.1 150 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 307.6 149.6 0
vertex 323.8 152.5 0
vertex 323.8 161.3 0
endloop
endfacet
facet normal 0.00 0.00 1.00
outer loop
vertex 307.6 149.6 0
vertex 323.8 161.3 0
vertex 307.6 158.4 0
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex -393.4 0 -76.2
vertex -260.1 0 -76.2
vertex -260.1 0 -85.1
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex -393.4 0 -76.2
vertex -260.1 0 -85.1
vertex -393.4 0 -85.1
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex -260.1 0 -76.2
vertex -126.8 0 -76.2
vertex -126.8 0 -85.1
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex -260.1 0 -76.2
vertex -126.8 0 -85.1
vertex -260.1 0 -85.1
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex -126.8 0 -76.2
vertex -63.4 0 -70.4
vertex -63.4 0 -79.2
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex -126.8 0 -76.2
vertex -63.4 0 -79.2
vertex -126.8 0 -85.1
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex -63.4 0 -70.4
vertex -46.5 0 -60.7
vertex -46.5 0 -69.5
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex -63.4 0 -70.4
vertex -46.5 0 -69.5
vertex -63.4 0 -79.2
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex -46.5 0 -60.7
vertex -31.1 0 -51.8
vertex -31.1 0 -60.7
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex -46.5 0 -60.7
vertex -31.1 0 -60.7
vertex -46.5 0 -69.5
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex -31.1 0 -51.8
vertex -21.2 0 -47.5
vertex -21.2 0 -56.4
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex -31.1 0 -51.8
vertex -21.2 0 -56.4
vertex -31.1 0 -60.7
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex -21.2 0 -47.5
vertex -10.8 0 -44.9
vertex -10.8 0 -53.7
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex -21.2 0 -47.5
vertex -10.8 0 -53.7
vertex -21.2 0 -56.4
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex -10.8 0 -44.9
vertex 0 0 -44
vertex 0 0 -52.9
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex -10.8 0 -44.9
vertex 0 0 -52.9
vertex -10.8 0 -53.7
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex 0 0 -44
vertex 3.3 0 -44.3
vertex 3.3 0 -53.2
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex 0 0 -44
vertex 3.3 0 -53.2
vertex 0 0 -52.9
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex 3.3 0 -44.3
vertex 6.5 0 -45.3
vertex 6.5 0 -54.2
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex 3.3 0 -44.3
vertex 6.5 0 -54.2
vertex 3.3 0 -53.2
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex 6.5 0 -45.3
vertex 30.7 0 -57.4
vertex 30.7 0 -66.2
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex 6.5 0 -45.3
vertex 30.7 0 -66.2
vertex 6.5 0 -54.2
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex 30.7 0 -57.4
vertex 69.4 0 -75.3
vertex 69.4 0 -84.2
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex 30.7 0 -57.4
vertex 69.4 0 -84.2
vertex 30.7 0 -66.2
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex 69.4 0 -75.3
vertex 108.3 0 -91.7
vertex 108.3 0 -100.5
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex 69.4 0 -75.3
vertex 108.3 0 -100.5
vertex 69.4 0 -84.2
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex 108.3 0 -91.7
vertex 147.6 0 -106.4
vertex 147.6 0 -115.3
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex 108.3 0 -91.7
vertex 147.6 0 -115.3
vertex 108.3 0 -100.5
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex 147.6 0 -106.4
vertex 187.1 0 -119.6
vertex 187.1 0 -128.5
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex 147.6 0 -106.4
vertex 187.1 0 -128.5
vertex 147.6 0 -115.3
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex 187.1 0 -119.6
vertex 227 0 -131.2
vertex 227 0 -140
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex 187.1 0 -119.6
vertex 227 0 -140
vertex 187.1 0 -128.5
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex 227 0 -131.2
vertex 267.1 0 -141.2
vertex 267.1 0 -150
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex 227 0 -131.2
vertex 267.1 0 -150
vertex 227 0 -140
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex 267.1 0 -141.2
vertex 307.6 0 -149.6
vertex 307.6 0 -158.4
endloop
endfacet
facet normal 0.00 1.00 -0.00
outer loop
vertex 267.1 0 -141.2
vertex 307.6 0 -158.4
vertex 267.1 0 -150
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex 307.6 0 -149.6
vertex 323.8 0 -152.5
vertex 323.8 0 -161.3
endloop
endfacet
facet normal -0.00 1.00 -0.00
outer loop
vertex 307.6 0 -149.6
vertex 323.8 0 -161.3
vertex 307.6 0 -158.4
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 76.2 0
vertex -393.4 74.1 17.8
vertex -393.4 82.7 19.9
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 76.2 0
vertex -393.4 82.7 19.9
vertex -393.4 85.1 0
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 74.1 17.8
vertex -393.4 67.9 34.6
vertex -393.4 75.8 38.6
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 74.1 17.8
vertex -393.4 75.8 38.6
vertex -393.4 82.7 19.9
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 67.9 34.6
vertex -393.4 58 49.5
vertex -393.4 64.7 55.3
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 67.9 34.6
vertex -393.4 64.7 55.3
vertex -393.4 75.8 38.6
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 58 49.5
vertex -393.4 44.8 61.7
vertex -393.4 50 68.8
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 58 49.5
vertex -393.4 50 68.8
vertex -393.4 64.7 55.3
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 44.8 61.7
vertex -393.4 29.2 70.4
vertex -393.4 32.6 78.6
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 44.8 61.7
vertex -393.4 32.6 78.6
vertex -393.4 50 68.8
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 29.2 70.4
vertex -393.4 11.9 75.3
vertex -393.4 13.3 84
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 29.2 70.4
vertex -393.4 13.3 84
vertex -393.4 32.6 78.6
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 11.9 75.3
vertex -393.4 -6 76
vertex -393.4 -6.7 84.8
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 11.9 75.3
vertex -393.4 -6.7 84.8
vertex -393.4 13.3 84
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -6 76
vertex -393.4 -23.6 72.5
vertex -393.4 -26.3 80.9
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -6 76
vertex -393.4 -26.3 80.9
vertex -393.4 -6.7 84.8
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -23.6 72.5
vertex -393.4 -39.8 65
vertex -393.4 -44.5 72.5
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -23.6 72.5
vertex -393.4 -44.5 72.5
vertex -393.4 -26.3 80.9
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -39.8 65
vertex -393.4 -53.9 53.9
vertex -393.4 -60.2 60.2
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -39.8 65
vertex -393.4 -60.2 60.2
vertex -393.4 -44.5 72.5
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -53.9 53.9
vertex -393.4 -65 39.8
vertex -393.4 -72.5 44.5
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -53.9 53.9
vertex -393.4 -72.5 44.5
vertex -393.4 -60.2 60.2
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -65 39.8
vertex -393.4 -72.5 23.6
vertex -393.4 -80.9 26.3
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -65 39.8
vertex -393.4 -80.9 26.3
vertex -393.4 -72.5 44.5
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -72.5 23.6
vertex -393.4 -76 6
vertex -393.4 -84.8 6.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -72.5 23.6
vertex -393.4 -84.8 6.7
vertex -393.4 -80.9 26.3
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -76 6
vertex -393.4 -75.3 -11.9
vertex -393.4 -84 -13.3
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -76 6
vertex -393.4 -84 -13.3
vertex -393.4 -84.8 6.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -75.3 -11.9
vertex -393.4 -70.4 -29.2
vertex -393.4 -78.6 -32.6
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -75.3 -11.9
vertex -393.4 -78.6 -32.6
vertex -393.4 -84 -13.3
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -70.4 -29.2
vertex -393.4 -61.7 -44.8
vertex -393.4 -68.8 -50
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -70.4 -29.2
vertex -393.4 -68.8 -50
vertex -393.4 -78.6 -32.6
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -61.7 -44.8
vertex -393.4 -49.5 -58
vertex -393.4 -55.3 -64.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -61.7 -44.8
vertex -393.4 -55.3 -64.7
vertex -393.4 -68.8 -50
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -49.5 -58
vertex -393.4 -34.6 -67.9
vertex -393.4 -38.6 -75.8
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -49.5 -58
vertex -393.4 -38.6 -75.8
vertex -393.4 -55.3 -64.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -34.6 -67.9
vertex -393.4 -17.8 -74.1
vertex -393.4 -19.9 -82.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -34.6 -67.9
vertex -393.4 -19.9 -82.7
vertex -393.4 -38.6 -75.8
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -17.8 -74.1
vertex -393.4 0 -76.2
vertex -393.4 0 -85.1
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex -393.4 -17.8 -74.1
vertex -393.4 0 -85.1
vertex -393.4 -19.9 -82.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 152.5 0
vertex 323.8 148.3 35.6
vertex 323.8 156.9 37.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 152.5 0
vertex 323.8 156.9 37.7
vertex 323.8 161.3 0
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 148.3 35.6
vertex 323.8 135.9 69.2
vertex 323.8 143.7 73.2
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 148.3 35.6
vertex 323.8 143.7 73.2
vertex 323.8 156.9 37.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 135.9 69.2
vertex 323.8 115.9 99
vertex 323.8 122.7 104.8
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 135.9 69.2
vertex 323.8 122.7 104.8
vertex 323.8 143.7 73.2
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 115.9 99
vertex 323.8 89.6 123.4
vertex 323.8 94.8 130.5
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 115.9 99
vertex 323.8 94.8 130.5
vertex 323.8 122.7 104.8
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 89.6 123.4
vertex 323.8 58.4 140.9
vertex 323.8 61.7 149
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 89.6 123.4
vertex 323.8 61.7 149
vertex 323.8 94.8 130.5
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 58.4 140.9
vertex 323.8 23.9 150.6
vertex 323.8 25.2 159.3
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 58.4 140.9
vertex 323.8 25.2 159.3
vertex 323.8 61.7 149
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 23.9 150.6
vertex 323.8 -12 152
vertex 323.8 -12.7 160.8
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 23.9 150.6
vertex 323.8 -12.7 160.8
vertex 323.8 25.2 159.3
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -12 152
vertex 323.8 -47.1 145
vertex 323.8 -49.9 153.4
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -12 152
vertex 323.8 -49.9 153.4
vertex 323.8 -12.7 160.8
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -47.1 145
vertex 323.8 -79.7 130
vertex 323.8 -84.3 137.5
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -47.1 145
vertex 323.8 -84.3 137.5
vertex 323.8 -49.9 153.4
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -79.7 130
vertex 323.8 -107.8 107.8
vertex 323.8 -114.1 114.1
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -79.7 130
vertex 323.8 -114.1 114.1
vertex 323.8 -84.3 137.5
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -107.8 107.8
vertex 323.8 -130 79.7
vertex 323.8 -137.5 84.3
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -107.8 107.8
vertex 323.8 -137.5 84.3
vertex 323.8 -114.1 114.1
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -130 79.7
vertex 323.8 -145 47.1
vertex 323.8 -153.4 49.9
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -130 79.7
vertex 323.8 -153.4 49.9
vertex 323.8 -137.5 84.3
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -145 47.1
vertex 323.8 -152 12
vertex 323.8 -160.8 12.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -145 47.1
vertex 323.8 -160.8 12.7
vertex 323.8 -153.4 49.9
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -152 12
vertex 323.8 -150.6 -23.9
vertex 323.8 -159.3 -25.2
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -152 12
vertex 323.8 -159.3 -25.2
vertex 323.8 -160.8 12.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -150.6 -23.9
vertex 323.8 -140.9 -58.4
vertex 323.8 -149 -61.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -150.6 -23.9
vertex 323.8 -149 -61.7
vertex 323.8 -159.3 -25.2
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -140.9 -58.4
vertex 323.8 -123.4 -89.6
vertex 323.8 -130.5 -94.8
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -140.9 -58.4
vertex 323.8 -130.5 -94.8
vertex 323.8 -149 -61.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -123.4 -89.6
vertex 323.8 -99 -115.9
vertex 323.8 -104.8 -122.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -123.4 -89.6
vertex 323.8 -104.8 -122.7
vertex 323.8 -130.5 -94.8
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -99 -115.9
vertex 323.8 -69.2 -135.9
vertex 323.8 -73.2 -143.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -99 -115.9
vertex 323.8 -73.2 -143.7
vertex 323.8 -104.8 -122.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -69.2 -135.9
vertex 323.8 -35.6 -148.3
vertex 323.8 -37.7 -156.9
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -69.2 -135.9
vertex 323.8 -37.7 -156.9
vertex 323.8 -73.2 -143.7
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -35.6 -148.3
vertex 323.8 0 -152.5
vertex 323.8 0 -161.3
endloop
endfacet
facet normal -1.00 0.00 0.00
outer loop
vertex 323.8 -35.6 -148.3
vertex 323.8 0 -161.3
vertex 323.8 -37.7 -156.9
endloop
endfacet
endsolid chamber
```

---

## Results for the example engine

A 100 kN (22,500 lbf) sea-level LOX/methane engine at 100 bar, the propellant combination SpaceX uses in Raptor.

| | |
|---|---|
| Specific impulse (sea level / vacuum) | **303 s / 325 s** |
| Throat / exit diameter | 88.0 mm / 305 mm |
| Propellant flow | 33.7 kg/s (7.3 kg/s methane) |
| Peak gas-side heat flux | **62 MW/m²** at the throat |
| Peak copper wall temperature | **926 K** (limit ≈ 1000 K) |
| Methane coolant | 120 K → 429 K, 22 bar pressure drop |
| Liner stress margin (lowest) | **+0.47** at the throat |
| Estimated mass | 17.8 kg |

Full report: [`outputs/methane_100kN/REPORT.md`](outputs/methane_100kN/REPORT.md)

![Thermal analysis](outputs/methane_100kN/thermal_analysis.png)

---

## How it works, step by step

**1. Size the engine (ideal rocket theory).** From chamber pressure and the combustion gas properties,
the program computes the characteristic velocity *c\** and the thrust coefficient *C<sub>F</sub>*. The
throat area follows from *A<sub>t</sub> = F / (C<sub>F</sub> p<sub>c</sub>)*. The exit Mach number comes from
inverting the isentropic area–Mach relation for the chosen expansion ratio.

**2. Draw the contour.** Cylindrical chamber (length set by the characteristic length *L\**) → fillet →
30° converging cone → throat arcs of 1.5 *R<sub>t</sub>* and 0.382 *R<sub>t</sub>* → **Rao 80% bell nozzle**
(a parabola between the wall angles θ<sub>n</sub> and θ<sub>e</sub>). The curve is tangent-continuous, so it can be
offset outward to make the liner, channel and jacket layers.

**3. Gas-side heat transfer (Bartz correlation).** The heat-transfer coefficient from the hot gas
to the wall, corrected for boundary-layer property changes. The heat flux peaks just upstream of the throat.

**4. Regenerative cooling (1-D march).** All the methane flows through 100 rectangular channels milled into the
copper liner, from the nozzle exit toward the injector. At each of 600 stations the program:
- balances three thermal resistances in series: hot gas → copper wall → coolant;
- gets the coolant-side coefficient from Dittus–Boelter, with **fin efficiency** for the copper ribs;
- uses **real-fluid methane properties (CoolProp)**, because methane passes through its critical point here;
- adds the absorbed heat to the coolant and subtracts the friction pressure drop (Haaland friction factor, 10 µm roughness).

**5. Structural check.** Two stresses act on the 0.7 mm hot wall:
- *Thermal stress* from the temperature drop across the wall, σ = Eα q t / (2(1−ν)k). It is
  self-limiting (secondary).
- *Pressure bending*: the 160 bar coolant pushes the wall between ribs into the chamber gas, σ = Δp w² / (2t²).
  This one is primary.

Following the ASME shakedown approach, primary stress must stay under yield / safety factor, and primary + secondary under 2 × yield.

**6. Jacket.** An Inconel 718 closeout sized for hoop stress at the highest coolant pressure,
plus an injector flange with 12 bolt holes.

**7. CAD.** CadQuery (OpenCASCADE) revolves each layer, cuts 100 channel wedges and exports STEP and STL.
The CAD surfaces stay within 0.05 mm of the analysed contour.

---

## Open it in SolidWorks

Download `outputs/methane_100kN/thrust_chamber_assembly_STEP.zip`, unzip it, and open `thrust_chamber_assembly.step` with **File › Open** (file type STEP). The large STEP files are zipped to stay under GitHub's 25 MB upload limit.
To rebuild the model natively from the exported curves, or to check the thermal analysis with
SolidWorks Simulation, follow **[docs/SOLIDWORKS.md](docs/SOLIDWORKS.md)**.

| Output file | Use |
|---|---|
| `thrust_chamber_assembly_STEP.zip` | Liner + jacket assembly (unzip to get the .step): SolidWorks, Fusion 360, Onshape, CATIA, NX, FreeCAD |
| `liner_STEP.zip`, `jacket.step` | Individual parts |
| `thrust_chamber.stl` | 3-D printing a scale model, slicers (GitHub previews it in 3-D) |
| `solidworks_curve_*.txt` | Wall curves for *Insert › Curve › Curve Through XYZ Points* |
| `station_data.csv` | Every quantity at all 600 stations: open in Excel |
| `REPORT.md` + PNGs | Design report and plots |

---

## Run it yourself

```bash
pip install -r requirements.txt
python run.py                                   # example engine, about 3 minutes with CAD
python run.py designs/methane_100kN.json --no-cad   # analysis + plots only, about 1 second
```

To design your own engine, copy `designs/methane_100kN.json`, change the numbers and run it. Propellants:
`LOX/CH4`, `LOX/RP-1`, `LOX/LH2`. Materials: `GRCop-42`, `Inconel 718`, `316L`.

```
tcd/
  data.py         propellant and material properties
  performance.py  ideal rocket sizing
  geometry.py     chamber + Rao bell contour, wall offsets
  cooling.py      Bartz, regenerative cooling march, liner stress, jacket sizing
  cad.py          CadQuery 3-D model, STEP/STL export
  report.py       plots, CSV, SolidWorks curves, Markdown report, renders
designs/          input files (JSON)
outputs/          generated results for the example engine
web/              interactive 3D calculator (GitHub Pages)
docs/             SolidWorks guide, GitHub guide
```

---

## Assumptions and limitations

This is a **preliminary design tool**. Real hardware needs much more analysis.
- Combustion gas properties are single-point approximations, with no change in composition along the
  nozzle. Use NASA CEA for real values.
- Performance is ideal. Real engines lose about 2–5% Isp to combustion efficiency and nozzle divergence.
- Bartz and Dittus–Boelter are empirical correlations accurate to about ±20–30%. Supercritical methane near its
  pseudo-critical point is especially hard to model. The model ignores channel curvature, wall
  roughness effects on heat transfer, film cooling and radiation.
- The 1-D model treats the wall as a flat plate per station. Use 2-D/3-D FEA for the real temperature field
  around the ribs (see docs/SOLIDWORKS.md, Option C).
- Material properties are approximate elevated-temperature values. The model gives no low-cycle-fatigue life estimate.
- Coolant manifolds, injector and ignition are not modelled.

## References
- G. P. Sutton & O. Biblarz, *Rocket Propulsion Elements*, 9th ed., Wiley.
- D. K. Huzel & D. H. Huang, *Modern Engineering for Design of Liquid-Propellant Rocket Engines*, AIAA, 1992.
- D. R. Bartz, "A Simple Equation for Rapid Estimation of Rocket Nozzle Convective Heat Transfer Coefficients," *Jet Propulsion*, 1957.
- G. V. R. Rao, "Exhaust Nozzle Contour for Optimum Thrust," *Jet Propulsion*, 1958.
- I. H. Bell et al., "Pure and Pseudo-pure Fluid Thermophysical Property Evaluation and the Open-Source Thermophysical Property Library CoolProp," *Ind. Eng. Chem. Res.*, 2014.
- ASME Boiler and Pressure Vessel Code, Section VIII Div. 2: primary and secondary stress limits, shakedown.

## How this was built
- Written in Python
- Fuel properties come from CoolProp, a free library with real data for methane, hydrogen and RP-1
- The 3-D model is made with CadQuery and saved as STEP (for SolidWorks) and STL (for 3-D printing)
- The website is plain HTML and JavaScript, with three.js for the 3D view
- The engineering follows standard rocket textbooks (Sutton, and Huzel & Huang) and well-known heat-transfer formulas (Bartz and Dittus–Boelter)

## Author
ALP EMIN TANRISEVEN · [LinkedIn](https://www.linkedin.com/in/alptanriseven/)

MIT License

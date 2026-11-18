"""Propellant and material data.

All values are approximate, single-point numbers good for preliminary sizing.
For real design work, get combustion properties from NASA CEA and material
data from the supplier's datasheets at the actual operating temperature.
"""

# Combustion properties at a typical mixture ratio (O/F by mass).
#   Tc     chamber temperature [K]
#   M      molar mass of the combustion gas [g/mol]
#   gamma  ratio of specific heats [-]
#   Lstar  characteristic chamber length [m]
#   coolant        CoolProp fluid name used for the regenerative cooling model
#   T_cool_in      coolant temperature entering the channels [K]
PROPELLANTS = {
    "LOX/CH4": dict(OF=3.6, Tc=3550.0, M=21.5, gamma=1.20, Lstar=1.1,
                    coolant="Methane", T_cool_in=120.0),
    "LOX/RP-1": dict(OF=2.6, Tc=3670.0, M=23.3, gamma=1.22, Lstar=1.15,
                     coolant="n-Dodecane", T_cool_in=300.0),
    "LOX/LH2": dict(OF=6.0, Tc=3450.0, M=13.5, gamma=1.21, Lstar=0.85,
                    coolant="Hydrogen", T_cool_in=40.0),
}

# Material properties at elevated temperature (roughly 700-900 K).
#   k      thermal conductivity [W/m-K]
#   E      Young's modulus [Pa]
#   alpha  thermal expansion coefficient [1/K]
#   nu     Poisson's ratio [-]
#   sy     yield strength [Pa]
#   T_max  practical maximum hot-wall temperature [K]
#   rho    density [kg/m^3]
MATERIALS = {
    "GRCop-42": dict(k=300.0, E=100e9, alpha=18e-6, nu=0.33, sy=170e6, T_max=1000.0, rho=8800.0),
    "Inconel 718": dict(k=22.0, E=165e9, alpha=14.5e-6, nu=0.29, sy=900e6, T_max=1100.0, rho=8190.0),
    "316L": dict(k=21.0, E=160e9, alpha=18e-6, nu=0.30, sy=140e6, T_max=1000.0, rho=8000.0),
}

G0 = 9.80665          # standard gravity [m/s^2]
R_UNIVERSAL = 8314.46  # [J/kmol-K]

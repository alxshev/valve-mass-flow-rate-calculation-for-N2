from math import pi
from scipy.constants import psi, atm, bar

def get_density(T, P):
	molecular_mass = 28.0134 /1000 #N2, kg/mol
	R_universal = 8.314472
	return molecular_mass*P/(R_universal*T)

def print_mass_flow_rate(orifice_diameter_mm):
	gamma = 1.4 # for N2
	R = 296.80 #SI, J/kg K for N2
	const = ((gamma/R)**(1/2))*(((gamma+1)/2)**(-(gamma + 1)/(2*(gamma - 1))))
	orifice_diameter = orifice_diameter_mm/1000 # m
	A = pi*(orifice_diameter/2)**2 # m^2
	P = 2500*psi # Pa
	T = 30 + 273.15 # K

	density = get_density(T, P) #kg/m^3

	mdot = A*P*const/(T**(1/2))
	vdot = mdot / density # m^3/s
	print('Area: ' + str(A))
	print('Pressure: '+ str(P) + ' Pa | Area: ' + str(A) + ' m^2')
	print('density: ' + str(density) + ' kg/m^3')
	print('mdot: ' + str(mdot) + ' kg/s' + ' | vdot: ' + str(vdot))

print_mass_flow_rate(.9)
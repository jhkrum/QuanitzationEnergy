import sys
import os

os.system("cls")

print("E = hv")

#prompt the user for wavelength
wavelength = float(input("Wavelength(nm): "))

wavelength *= (10^-9)

#define constants
h = 6.626 * (10^-34)	#Planck's Constant
c = 3 * (10^8)			#Speed of Light

#calculate frequency
f = c/wavelength

#calculate energy
e = h * f

print("F = ",f," Hz")
print("E = ",e," Joules")
import numpy as np

#Constants
h = 6.62607015*pow(10,-34)
hbar = h / (2*np.pi)
elect_q = 1.60217662*pow(10,-19)
elect_m = 9.10938356*pow(10,-31)
proton_m = 1.6726219*pow(10,-27)
c = 2.99792458*pow(10,8)
neutron_m = 1.674929*pow(10,-27)

#return momentum
def momentum(v,m,l):
    if v is not 0:
        p = m*v
        return p
    else:
        p = h/l
        return p

#get wavelength from broglie's law
def broglie(x):
    y = h/x
    return y

#equation used in single slit intensity
def single_slit(a,L,y):
    l = y*a/L
    return l

#photoelectric equation
def photoelectric(workfunction,x):
    #Given wavelength
    if x is not 0:
        k = 1240/x - workfunction
        return k
    #given energy
    else:
        l = 1240/(x + workfunction)
        return l

#Energy-Wavelength Equation(Photon)
def energy(x):
    y = 1240/x
    return y

#Compton Scattering Equation
def compton(theta):
    delta_l = 1240/511000*(1-np.cos(np.pi*theta/180))
    return delta_l

#matter wave of electron
def matter_wave(k):
    l = 1240/np.sqrt(2*511000*k)
    return l

#bohr's energy state
def bohr(n1,n2):
    N = [13.6,3.4,1.51,0.85,0.54,0.38,0.28]
    print(N[n1]-N[n2])
    l = 1240/(N[n1]-N[n2])
    return l

#Converters
#J to eV
def ev(joul):
    return joul/(1.602176634*pow(10,-19))
#eV to J
def joul(ev):
    return 1.602176634*pow(10,-19)*ev

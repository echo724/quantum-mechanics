import scipy.integrate as integrate
import numpy as np
import quantum as qt

#Schrodinger's Probability Function
def prob(function,a,b):
    prob = integrate.quad(function,a,b)
    return prob

#Return uncertainty when one of values is given
def uncertainty(x):
    y = qt.barh/(2*x)
    return y

#Return velocity from uncertainty eq
def vel(m,x):
    v = qt.barh/(2*m*x)
    return v

#Return Kinetic energy from mass and momentum
def kinetic(p,m):
    k = p**2/(2*m)
    return k

#Return energy from given quantum number
def energy(n,m,l):
    e = n**2*np.pi**2*qt.hbar**2/(2*m*(l**2))
    return e

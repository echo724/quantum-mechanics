import scipy.integrate as integrate
import numpy as np
import quantum as qt

def prob(function,a,b):
    prob = integrate.quad(function,a,b)
    return prob

def relation(x):
    y = qt.barh/(2*x)
    return y

def vel(m,x):
    v = qt.barh/(2*m*x)
    return v

def kinetic(p,m):
    k = p**2/(2*m)
    return k

def potential(n,m,l):
    e = n**2*np.pi**2*qt.hbar**2/(2*m*(l**2))
    return e

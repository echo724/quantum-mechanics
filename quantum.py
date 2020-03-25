import numpy as np

class QT:
    _h = 6.626*pow(10,-34)
    _barh = _h / 2*np.pi
    _electron = 1.60217662*pow(10,-19)

    def __init__(self):
        self._m = float(0)
        self._v = float(0)
        self._l = float(0)
        self._p = float(0)
        self._k = float(0)
        self._e = float(0)

    def momentum(self):
        if self._v is not 0:
            self._p = self._m*self._v
            return self._p
        else:
            self._p = self._h/self._l

    def broglie(self):
        self._l = self._h/self._p
        return self._l

    def single_slit(self,a,L,y):
        self._l = y*a/L
        return self._l

    def photoelectric(self,workfunction):
        if self._l is not 0:
            self._k = 1240/self._l - workfunction
            return self._k
        else:
            self._l = 1240/(self._k + workfunction)
            return self._l

    def energy(self):
        self._e = 1240/self._l
        return self._e

    def compton(self,theta):
        delta_l = 1240/511000*(1-np.cos(np.pi*theta/180))
        return delta_l

    def matter_wave(self,k):
        self._l = 1240/np.sqrt(2*511000*k)
        return self._l

    def bohr(self,n1,n2):
        N = [13.6,3.4,1.51,0.85,0.54,0.38,0.28]
        print(N[n1]-N[n2])
        self._l = 1240/(N[n1]-N[n2])
        return self._l

#Static Methods
    def ev(joul):
        return joul/(1.60*pow(10,-19))

    def joul(ev):
        return 1.60*pow(10,-19)*ev

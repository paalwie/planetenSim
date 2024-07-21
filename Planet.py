'''
Created on 08.12.2014

@author: paal
'''
import numpy as np

class Planet(object):
    '''
    the planet class contains position split into x,y,z , mass and speed(in form of an numpy-array)
    '''
    def __init__(self, x, y, z, mass):
        self.__mass=mass
        self.__speed=np.array((0.,0.,0.))
        self.__coordarray=np.array((x,y,z))
    @property
    def mass(self):
        return self.__mass
    @property
    def coordsx(self):
        return self.__coordarray[0]
    @coordsx.setter
    def coordsx(self, x):
        self.__coordarray[0]=x
    @property
    def coordsy(self):
        return self.__coordarray[1]
    @coordsy.setter
    def coordsy(self, y):
        self.__coordarray[1]=y
    @property
    def coordsz(self):
        return self.__coordarray[2]
    @coordsz.setter
    def coordsz(self, z):
        self.__coordarray[2]=z
    @property
    def coordarray(self):
        return self.__coordarray    
    @coordarray.setter
    def coordarray(self, nparray):
        self.__coordarray=nparray
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, nparray):
        self.__speed=nparray
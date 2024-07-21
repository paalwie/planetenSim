'''
Created on 08.12.2014

@author: paal
'''
import Planet as planet
import math
import random
from Orbit_Math import Orbit_Math

class Universe(object):
    '''
    Universe contains a list of all created planets, as well as the total mass of the system
    '''
    def __init__(self):
        self.__planet_list=[]
        self.__total_mass=0
    
    @property
    def planet_list(self):
        return self.__planet_list
    
    @property
    def total_mass(self):
        return self.__total_mass

    def add_planet(self, x, y, z, mass):
        newplanet = planet(x,y,z,mass)
        self.planet_list.append(newplanet)
        self.__total_mass += mass
    
    def random_init(self):
        for planet in self.planet_list:
            planet.coordarray = Orbit_Math.rotation(planet.coordarray, (random.random() * 2 * math.pi))
    
    def without(self, item):
        return filter(lambda b: b!= item, self.planet_list)
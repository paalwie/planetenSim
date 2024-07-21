'''
Created on 08.12.2014

@author: paal
'''
import numpy as np
import math

class Orbit_Math(object):   
    """
    Orbit_Math provides functionalities for calculating position of planets in a solar system, using vectors
    """
    
    GRAV_CONST = 6.67384e-11
    
    @staticmethod
    def vector_length (nparray):
        """
        returns length of a given vector
        """
        return np.linalg.norm(nparray)
    
    @staticmethod
    def vector_normalize (nparray):
        """
        returns a vector normalized with its own length
        """
        length = Orbit_Math.vector_length(nparray)
        return np.array((nparray[0]/length, nparray[1]/length, nparray[2]/length))
    
    @staticmethod
    def vector_cross (nparray1, nparray2):
        """
        returns cross product of two vectors
        """
        return np.array((nparray1[1]*nparray2[2] - nparray1[2]*nparray2[1], 
                        nparray1[2]*nparray2[0] - nparray1[0]*nparray2[2],
                        nparray1[0]*nparray2[1] - nparray1[1]*nparray2[0]))
    
    @staticmethod    
    def vector_scale(nparray, scale):
        """
        scales a given vector with a given scalar
        """
        return np.array((nparray[0]*scale, nparray[1]*scale, nparray[2]*scale))
   
    @staticmethod
    def rotation(nparray, angle):
        """
        rotates a given vector with a given angle
        """
        xylength = math.sqrt(nparray[0]**2+nparray[1]**2)
        return np.array((xylength*math.cos(angle), xylength*math.sin(angle), nparray[2]))
    
    @staticmethod
    def vector_normalized_scale(nparray, scale):
        """
        scales a normalized vector
        """
        normalized = Orbit_Math.vector_normalize(nparray)
        return np.array((normalized[0]*scale, normalized[1]*scale, normalized[2]*scale))
    
    @staticmethod
    def centre_of_gravity(planet_list, total_mass):
        """
        calculates the centre of gravity        
        """
        mass_coords = np.array(sum(list(map(lambda b: Orbit_Math.vector_scale(b.coordarray, b.mass), planet_list)), np.array((0, 0, 0))))
        # sum = summe aller objekte in den folgenden klammern
        # list = erzeuge eine liste aus folgenden objekten
        # map = durchlaufe eine liste und fuehre eine funktion auf jedes objekt aus
        # lambda = laufzeitfunktion
        return Orbit_Math.vector_scale(mass_coords, 1/total_mass)
    
    @staticmethod
    def init_speed(planet, universe):
        grav_centre = Orbit_Math.centre_of_gravity(universe.planet_list, universe.total_mass)
        speed = ((universe.total_mass - planet.mass) / universe.total_mass) * math.sqrt((Orbit_Math.GRAV_CONST * universe.total_mass)/Orbit_Math.vector_length((planet.coordarray - grav_centre)))
        direction  = Orbit_Math.vector_cross(np.array((planet.coordarray - grav_centre)), np.array((0,0,0)))
        planet.speed = np.array((Orbit_Math.vector_scale(direction, speed)))
                                             
                                    
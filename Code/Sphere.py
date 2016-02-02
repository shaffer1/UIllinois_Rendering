"""
University of Illinois/NCSA Open Source License>
Copyright (c) 2016 University of Illinois
All rights reserved.
Developed by: 		Eric Shaffer
                  Department of Computer Science
                  University of Illinois at Urbana Champaign
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal with the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
to permit persons to whom the Software is furnished to do so, subject to the following conditions:
Redistributions of source code must retain the above copyright notice, this list of conditions and the following
disclaimers.Redistributions in binary form must reproduce the above copyright notice, this list
of conditions and the following disclaimers in the documentation and/or other materials provided with the distribution.
Neither the names of <Name of Development Group, Name of Institution>, nor the names of its contributors may be
used to endorse or promote products derived from this Software without specific prior written permission.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS WITH THE SOFTWARE.
""" 



import numpy as np
from numpy import linalg as LA

class Sphere:
    """Simple geometric sphere 

    Attributes:
        kEpsilon: floating value used for allowable error in equality tests
        r: radius
        c: center implemented as a numpy array
        material: tuple representing an RGB color with values in [0,255]
    """
    kEpsilon = 0.0000001
    def __init__(self,r,cntr,mat):
        """Initializes sphere attributes"""
        self.r=r
        self.c=cntr
        self.material=mat
     
    # #419begin #type=3 #src=Ray Tracing from the Ground Up 
          
    def intersectRay(self,ray):
        """ Determine if a ray intersects the sphere
            Returns: the parameter t for the closest intersection point to
                     the ray origin.
                     Returns a value of None for no intersection
        """  
        temp= ray.o - self.c
        a = np.dot(ray.d,ray.d)
        b = 2.0 * np.dot(temp,ray.d)
        cq = np.dot(temp,temp) - np.dot(self.r , self.r)
        disc = b * b -4.0 * a *cq
        if (disc < 0.0):
            return None
        else:
            e = np.sqrt(disc)
            denom = 2.0 * a
            t = (-b - e) / denom
            if (t>self.kEpsilon):
                return t
            t = (-1.0*b+e)/denom
            if (t>self.kEpsilon):
                return t
        return None
        
    # #419end   
    
    def getNormal(self,pt):
        """ Returns unit normal of sphere at the point pt """
        n=pt-self.c
        return n/LA.norm(n)
        
        
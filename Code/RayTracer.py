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
import matplotlib.pyplot as pt
import random

from PIL import Image
from Sphere import Sphere
from Ray import Ray
from ViewPort import ViewPort

#create a viewport and image
v = ViewPort(500,500)
im = Image.new("RGB",(v.w,v.h))
pix = im.load()

#define a sphere
radius = 1.0
center = np.array([0,0, -2.5])
s = Sphere(radius,center,np.array([255,0,0]))

#define a ray
ray = Ray(np.array([0,0,0]),np.array([0,0,-1]))

# define a light direction
ldir = np.array([0,0,1]) #light direction
kd = 0.75  #reflectivity 
illum = 1.0  #light luminosity


def phongDiffuse(x,n,mat):
    """Implements a Phong-style diffuse shading function

    Args:
         x: is a point on a surface
         n: is the unit normal at that point
         mat: is an RGB tuple of the surface color

    Returns: A tuple representing an RGB color with values in [0,255]
        
    """
    factor = kd*illum*max(0,n.dot(ldir))
    color = np.rint(factor*mat).astype(int)
    return (color[0],color[1],color[2])


# Perform orthographic ray-tracing of the sphere

for col in range(v.w):
    for row in range(v.h):
            ray.o = v.getPixelCenter(col,row)
            t = s.intersectRay(ray)
            if (t != None):
                xp = ray.getPoint(t) 
                pix[col,(v.h-1)-row] = phongDiffuse(xp,s.getNormal(xp),s.material)

# Show the image in a window
                
im.show()

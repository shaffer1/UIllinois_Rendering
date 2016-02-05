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

from PIL import Image
from Sphere import Sphere
from Ray import Ray
from Material import Material
from Light import Light
from ViewPort import ViewPort
from PhongShaders import phongShader

#create a viewport and image
v = ViewPort(500,500)
im = Image.new("RGB",(v.w,v.h))
pix = im.load()

#set an eyepoint
eye = np.array([0,0,0])

#define a sphere and material
mat = Material(np.array([255,0,0]),np.array([255,0,0]),120.0)
radius = 1.0
center = np.array([0,0, -2.5])
s = Sphere(radius,center,mat)

#define a ray
ray = Ray(np.array([0,0,0]),np.array([0,0,-1]))

# define a directional light 
light = Light(None,np.array([0,1,1]), np.array([0.75,0,0]), np.array([0.75,0,0])    )

# Perform orthographic ray-tracing of the sphere

for col in range(v.w):
    for row in range(v.h):
            ray.o = v.getPixelCenter(col,row)
            t = s.intersectRay(ray)
            if (t != None):
                xp = ray.getPoint(t) 
                pix[col,(v.h-1)-row] = phongShader(xp,s.getNormal(xp),s.material,light,eye)

# Show the image in a window
                
im.show()

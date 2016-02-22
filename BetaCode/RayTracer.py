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


from Sphere import Sphere
from Material import Material
from Light import Light

from Camera import PerspectiveCamera

#set an eyepoint
eye = np.array([0,0,0])

#set a lookat point
lookat = np.array([0,0,-1])

#set the up vector for viewing
up = np.array([0,1,0])

#set up distance to view plane

d = 8.0

# create a holder for our geometric objects
world=[]

#define a sphere and material
mat = Material(np.array([255,0,0]),np.array([255,0,0]),120.0)
radius = 1.0
center = np.array([0,0, -2.5])
s = Sphere(radius,center,mat)
world.append(s)

#create a holder for lights
lights = []

# define a directional light 
light1 = Light(None,np.array([0,1,1]), np.array([0.75,0,0]), np.array([0.75,0,0]))
lights.append(light1)

# create a camera to render the scene
cam = PerspectiveCamera(eye,lookat,up,d,zoom,exposure=1.0)

#render the scene

cam.render_scene(world,lights)


# Show the image in a window
                
im.show()

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

class ViewPort:
    """ Simple viewport class center on z-axis """
    def __init__(self,width,height,gamma=1.0):
        self.w=width
        self.h=height
        self.g = gamma
        self.inv_g=1/gamma
        self.setCorners(np.array([-1.0,-1.0,0.0]),np.array([1.0,1.0,0.0]))
        
    def setCorners(self,minC,maxC):
        """Sets the lower left and upper right corners"""
        self.minCorner = minC
        self.maxCorner = maxC
        self.s=(self.maxCorner[0]-self.minCorner[0])/self.w
        
        
    def getPixelCenter(self,r,c):
        return np.array([self.s*(c - self.w/2.0 +0.5), self.s*(r - self.h/2.0 +0.5), self.minCorner[2]])
   
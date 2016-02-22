# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from numpy import linalg as LA
from PIL import Image
from ViewPort import ViewPort
from PhongShaders import phongShader
from Ray import Ray

class PerspectiveCamera:
    
    """Simple perspective camera"""
    def __init__(self,eye,lookat,up,d,zoom,exposure=1.0):
        self.up=up
        self.eye=eye
        self.lookat=lookat
        self.zoom=zoom
        self.exposure=exposure
        self.compute_uvw()
        
    def compute_uvw(self):
        self.w = self.eye-self.lookat
        self.w = self.w/LA.norm(self.w)
        self.u = np.cross(self.up,self.w)
        self.u = self.u/LA.norm(self.u)
        self.v = np.cross(self.w,self.u)
    
    def render_scene(self,objects,lights,res):
        #create a viewport and image
        v = ViewPort(res[0],res[1])
        im = Image.new("RGB",(v.w,v.h))
        pix = im.load()

        #define a ray
        ray = Ray(np.array([0,0,0]),np.array([0,0,-1]))

        # Perform perspective ray-tracing

        for col in range(v.w):
            for row in range(v.h):
                color = np.zeros(3)
                ray.o = v.getPixelCenter(col,row)
                for s in objects:
                    t = s.intersectRay(ray)
                    if (t != None):
                        xp = ray.getPoint(t)
                        for light in lights:
                            color+= phongShader(xp,s.getNormal(xp),s.material,light,self.eye)
                        pix[col,(v.h-1)-row] = color

        # Show the image in a window
        im.show()
        
class OrthoCamera:  
    """Simple orthograohic camera"""
    def __init__(self,eye,lookat,up,d,zoom,exposure=1.0):
        self.up=up
        self.eye=eye
        self.lookat=lookat
        self.zoom=zoom
        self.exposure=exposure
        self.compute_uvw()
        
    def compute_uvw(self):
        self.w = self.eye-self.lookat
        self.w = self.w/LA.norm(self.w)
        self.u = np.cross(self.up,self.w)
        self.u = self.u/LA.norm(self.u)
        self.v = np.cross(self.w,self.u)
    
    def render_scene(objects,res):
        #create a viewport and image
        v = ViewPort(res[0],res[1])
        im = Image.new("RGB",(v.w,v.h))
        pix = im.load()

        #define a ray
        ray = Ray(np.array([0,0,0]),np.array([0,0,-1]))

        # Perform perspective ray-tracing

        for col in range(v.w):
            for row in range(v.h):
                ray.o = v.getPixelCenter(col,row)
                t = s.intersectRay(ray)
                if (t != None):
                    xp = ray.getPoint(t) 
                    pix[col,(v.h-1)-row] = phongShader(xp,s.getNormal(xp),s.material,light,eye)

        # Show the image in a window
        im.show()
        
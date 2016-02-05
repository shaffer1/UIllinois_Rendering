# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:11:15 2016

@author: shaffer1
"""
 
import numpy as np
from numpy import linalg as LA
   
def phongShader(x,N,mat,light,eye):
    """Implements a Phong-style shading function

    Args:
         x: is a point on a surface
         n: is the unit normal at that point
         mat: is an RGB tuple of the surface color plus shininess 
         light: a light object allowing us to generate L vector and RGB for
                diffuse and specular components
         eye: position of the viewpoint in space 

    Returns: A tuple representing an RGB color with values in [0,255]
        
    """
    V = eye-x
    V = V/LA.norm(V)
    
    L = light.d
    if L == None:
        L = L-x
        L = L/LA.norm(L)
        
    R=(2.0*L.dot(N)*N)-L
    R= R/LA.norm(R)
    diffuse  = light.diffuse*mat.kd*max(0,N.dot(L))
    specular = light.specular*mat.ks*(max(0,R.dot(V))**mat.shininess)
    color = np.clip(diffuse + specular,0.0,255.0)
    color = np.rint(color).astype(int)
    return (color[0],color[1],color[2])  
    
    
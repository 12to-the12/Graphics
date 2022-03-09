import math
import numpy as np
from math import sin, cos, tan
from math import acos, atan
from math import degrees, radians
import time

def clean(x):
    return round(x*1000)/1000
def barycenter(polygon): # returns the center of the polygon, useful for the painter's algorithm
    a, b, c = polygon
    x1, y1, z1 = a
    x2, y2, z2 = b
    x3, y3, z3 = c
    x = (x1 + x2 + x3) / 3
    y = (y1 + y2 + y3) / 3
    z = (z1 + z2 + z3) / 3
    return (x, y, z)

def hypotenuse(coor):
    x, y = coor
    x = abs(x)
    y = abs(y)
    return math.sqrt( x**2 + y**2)

def xmag(vector_list):
    return np.linalg.norm(vector_list,axis=1)
def magnitude(vector):
    x, y, z = vector
    x = abs(x)
    y = abs(y)
    z = abs(z)
    return math.sqrt( x**2 + y**2 + z**2)
    
def normalize(vector):
    x, y, z = vector
    mag = magnitude(vector)
    return (x/mag, y/mag, z/mag)
    
def xnormalize(vector_list):
    assert vector_list.shape[1] == 3
    mag_list = xmag(vector_list)
    return vector_list / mag_list[:,None]

def xcartesian_to_polar(obj_data): # starts from positive x, counter clockwise
    pass

    #np.where( x[0]==0, )

def cartesian_to_polar(vector): # starts from positive x, counter clockwise
    #stamp = time.time()
    x, y, z = vector
    r = magnitude(vector)
    try: theta = atan(y/x)#doesnt work if x is zero, means point is on y-z plane
    except: 
        if y>0: theta = radians(90)
        elif y<0: theta = radians(270)
        else: theta = 0
    
    hyp = hypotenuse( (x,y) )
    #phi = acos(z/r)) used instead if we want the angle from the z axis instead of the xy plane
    try: phi = acos(z/r)#phi = atan(hyp / z)
    except: phi = 0
    
    theta = degrees(theta)
    if x<0: theta += 180
    phi = degrees(phi)
    return (r, theta, phi)
    
def polar_to_cartesian(vector): # this took hours jesus
    r, theta, phi = vector
    assert theta>0 # you know what you have to do
    assert theta<360
    assert phi>0
    assert phi<360
    #if theta <0: theta += 180
    theta = radians(theta)
    phi = radians(phi)
    x = r * sin(phi) * cos(theta)
    y = r * sin(phi) * sin(theta)
    z = r * cos(phi)
    x = clean(x)
    y = clean(y)
    z = clean(z)
    return (x, y, z)
    
    
def normal_vector(polygon_list): # finds the normal of a list of polygons
    # takes an array of shape(-1,3,3)
    p1 = polygon_list[:,0]
    p2 = polygon_list[:,1]
    p3 = polygon_list[:,2]
    normals = np.cross(p2-p1, p3-p1)
    normals = xnormalize(normals)
    return normals
    
def dot_product(a, b): #return np.multiply(a, b).sum(1)
    # takes two (-1,3) shaped lists and returns a one dimensional list
    assert a.shape[0] == 3
    assert b.shape[0] == 3
    
    return np.einsum('ij, ij->i', a, b)

def angle(a, b):# finds the angle between two (lists of) vectors
    # takes two (-1,3) shaped lists and returns a one dimensional list
    assert a.shape[0] == 3
    assert b.shape[0] == 3
    
    a = xnormalize(a)
    b = xnormalize(b)
    dot = dot_product(a, b)
    angle = np.arccos( dot )
    return angle*57.295779513



































#
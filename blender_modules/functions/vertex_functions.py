#import bpy
import json
import math
import numpy as np

blender_scripts = "C:/Users/j_ber/root/blender_scripts/stored_values/"

##############################################################################
##### Constants ##############################################################

x_ortho_rot = np.array([[1, 0, 0],
                        [0, 0, -1],
                        [0, 1, 0]])

y_ortho_rot = np.array([[0, 0, 1],
                        [0, 1, 0],
                        [-1, 0, 0]])

z_ortho_rot = np.array([[0, -1, 0],
                        [1, 0, 0],
                        [0, 0, 1]])

##############################################################################
##### Functions ##############################################################

def checkElement(line):
    for char in line:
        if char == ":":
            return True
    return False
  
def loadFile(filename, char):
    #Open vertex_data.txt in specified mode
    path = blender_scripts + filename + ".txt"
    file = open(path, char)
        
    return file
    
def getFlushCoordinate(dict):
    axis = dict["flush"]
    return dict[axis]
    
def getFlushAxis(dict):
    axis = dict["flush"]
    if (axis == 'x'):
        return 0
    if (axis == 'y'):
        return 1
    if (axis == 'z'):
        return 2
    else:
        print("fuck man, you're axis isn't valid yooo")

def initializeVertexData():
    # initialize dictionary
    dict = {"x" : 0, "y" : 0, "z" : 0, "flush" : "x"}
        
    # load file, dump dictionary into it
    file = loadFile("vertex_data",'w')
    json.dump(dict, file)

    # close the file
    file.close()
    
    # open init_data in write mode and change vertex_data to True
    otherFile = loadFile("init_data", "r")
    dict = json.load(otherFile)
    otherFile.close()
    
    dict["vertex_data"] = 1
    otherFile = loadFile("init_data", "w")
    
    json.dump(dict, otherFile)
    otherFile.close()

def initializeStoredValues(): 
    # load init_data file
    file = loadFile("init_data",'r')
    dict = json.load(file)
    
    # look for uninitialized files
    if dict["values"] == False:
        print("You still need to add an init function for stored_values!!!")
 
    if dict["vertex_data"] == False:
        initializeVertexData()
        print("Initialized vertex data!")
        
    file.close()
        
def normalize(vector):
    mag = np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    
    return (vector[0]/mag, vector[1]/mag, vector[2]/mag)    

def distance(v1, v2):
    dx = v1[0] - v2[0]
    dy = v1[1] - v2[1]
    dz = v1[2] - v2[2]
    
    return math.sqrt(dx**2 + dy**2 + dz**2)

def getVector(v1,v2):
    x = v2[0] - v1[0]
    y = v2[1] - v1[1]
    z = v2[2] - v1[2]
    
    return (x,y,z)

def dot(vector1, vector2):
    dot_product = vector1[0]*vector2[0] + vector1[1]*vector2[1] + vector1[2]*vector2[2]
    
    return dot_product

def orthoRotate(vertex_co, axis):
    # Rotates the vertex about the x axis, with respect to the origin
    if type(vertex_co) != np.ndarray:
        print("~orthoRotateX~ argument must be a numpy ndarray!")
        return
    
    if axis == 0:
        return x_ortho_rot.dot(vertex_co)
    elif axis == 1:
        return y_ortho_rot.dot(vertex_co)
    elif axis == 2:
        return z_ortho_rot.dot(vertex_co)
            
    print("oh shit axis isn't a valid value, must be 0, 1 or 2")
    return

def orthoRotateObject(vertices, axis):
    
    # Make axis an indexing integer 
    if (axis == 'x' or axis == 'X'):
        axis = 0
    elif (axis == 'y' or axis == 'Y'):
        axis = 1
    elif (axis == 'z' or axis  == 'Z'):
        axis = 2
    
    # get center of mass of the vertices
    print("original center of mass is:")
    com = getCenterOfMass(vertices)
    print("")

    # Shift all vertices so com is origin
    vertices = [vertice - com for vertice in vertices]
    
    # Rotate all vertices about origin, with respect to correct axis
    vertices = [orthoRotate(vertice, axis) for vertice in vertices]
    
    # Shift back to com position
    vertices  = [vertice + com for vertice in vertices]
    
    return vertices

def getCenterOfMass(vertex_array):
    # Start all your cm sums at zero 
    x_cm = 0; y_cm = 0; z_cm = 0
    
    total_mass = len(vertex_array)
    
    # Loop through and find sum of mass*distance for each coordinate
    for vertex in vertex_array:

        x_cm += vertex[0]
        print(x_cm)
        y_cm += vertex[1]
        z_cm += vertex[2]
        
    # Divide by total mass to find center of mass
    x_cm = x_cm/total_mass
    y_cm = y_cm/total_mass
    z_cm = z_cm/total_mass
    
    return np.array([x_cm, y_cm, z_cm])

    
    
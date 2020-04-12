import bpy
import json
import math
import functions.vertex_functions as vf
import numpy as np
#from mathutils import Vector
blender_scripts = "C:/Users/j_ber/root/blender_scripts/stored_values/"

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
         
def distance(v1, v2):
    dx = v1[0] - v2[0]
    dy = v1[1] - v2[1]
    dz = v1[2] - v2[2]
    
    return math.sqrt(dx**2 + dy**2 + dz**2)

 
class VertexTools(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Vertex Tools"
    bl_idname = "OBJECT_PT_operators"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    initializeStoredValues()

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Welcome to Sbruce's Vertex Operators", icon='WORLD_DATA')
        
        row = layout.row()
        row.operator("object.move_vertices",text = "Move Vertices")
        
        row = layout.row()
        row.operator("object.merge_vertices", text = "Merge Vertices")
        
        row = layout.row()
        row.label(text = "Store corresponding vertex data")
        
        row = layout.row()
        row.operator("object.store_vertex_data_x",text = "x")
        row.operator("object.store_vertex_data_y",text = "y")
        row.operator("object.store_vertex_data_z",text = "z")
        
        row = layout.row()
        row.label(text = "Set vertices to corresponding coordinate")
        
        row = layout.row()
        row.operator("object.set_vertice_x", text = "x")
        row.operator("object.set_vertice_y", text = "y")        
        row.operator("object.set_vertice_z", text = "z")

        row = layout.row()
        row.operator("object.move_to_flush", text = "Move selected to flush coordinate")

        row = layout.row()
        row.label(text = "Rotate object 90 degress over specified axis")
        
        row = layout.row()
        row.operator("object.ortho_rotate_x", text = "ortho rotate x")
        row.operator("object.ortho_rotate_y", text = "ortho rotate y")
        row.operator("object.ortho_rotate_z", text = "ortho rotate z")
        

class MoveVertices(bpy.types.Operator):
    
    """Defining the custom operator -copyAndShift-"""
    bl_idname = 'object.move_vertices'
    bl_label = 'Copy and Shift Operator'
    
    def execute(self, context):
        #Load values from stored_values.txt
        path = "C:/Users/j_ber/root/blender_scripts/stored_values/values.txt"
        file = open(path, 'r')
        contents = file.read()
        
        #Read contents of file into list, put them in a dict
        contents = contents.split("\n")
        dict = {}
        for element in contents:
            if checkElement(element):
                temp_list = element.split(":")
                dict[temp_list[0]]=float(temp_list[1].strip())
        
        # store previous mode
        mode = bpy.context.active_object.mode
        
        bpy.ops.object.mode_set(mode='OBJECT')
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        for v in selectedVerts:
            v.co += Vector((dict['x'],dict['y'],dict['z']))
                      
        
        # back to whatever mode we were in
        bpy.ops.object.mode_set(mode=mode)
        
        return {"FINISHED"}
    
class StoreVertexDataX(bpy.types.Operator):
    
    """Defining the custom operator -copyAndShift-"""
    bl_idname = 'object.store_vertex_data_x'
    bl_label = 'Store X vertex data'
    
    def execute(self, context):

        # store previous mode, get selected vertices
        mode = bpy.context.active_object.mode      
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type = "ORIGIN_GEOMETRY" )
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]

        # if more than one selected vertice, print error message
        if len(selectedVerts) != 1:
            print("ERROR: Must have only one selected vertice to store a position")
            
        else:
            # grab your dictionary data
            file = loadFile("vertex_data", 'r')
            dict = json.load(file)
            file.close()
            
            # set your x value in dict to the current vertext x value
            dict["x"] = selectedVerts[0].co.x
            dict["flush"] = "x"
            
            # write new value to your dictionary
            file = loadFile("vertex_data", 'w')
            json.dump(dict, file)      
        
        # back to whatever mode we were in
        bpy.ops.object.mode_set(mode=mode)
        
        return {"FINISHED"}
        
class StoreVertexDataY(bpy.types.Operator):
    
    """Defining the custom operator -copyAndShift-"""
    bl_idname = 'object.store_vertex_data_y'
    bl_label = 'Store Y vertex data'
    
    def execute(self, context):

        # store previous mode, get selected vertices
        mode = bpy.context.active_object.mode      
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type = "ORIGIN_GEOMETRY" )
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]

        # if more than one selected vertice, print error message
        if len(selectedVerts) != 1:
            print("ERROR: Must have only one selected vertice to store a position")
            
        else:
            # grab your dictionary data
            file = loadFile("vertex_data", 'r')
            dict = json.load(file)
            file.close()
            
            # set your x value in dict to the current vertext x value
            dict["y"] = selectedVerts[0].co.y
            dict["flush"] = "y"
            
            # write new value to your dictionary
            file = loadFile("vertex_data", 'w')
            json.dump(dict, file)      
        
        # back to whatever mode we were in
        bpy.ops.object.mode_set(mode=mode)
        
        return {"FINISHED"}    

class StoreVertexDataZ(bpy.types.Operator):
    
    """Defining the custom operator -copyAndShift-"""
    bl_idname = 'object.store_vertex_data_z'
    bl_label = 'Store Z vertex data'
    
    def execute(self, context):

        # store previous mode, get selected vertices
        mode = bpy.context.active_object.mode      
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type = "ORIGIN_GEOMETRY" )
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]

        # if more than one selected vertice, print error message
        if len(selectedVerts) != 1:
            print("ERROR: Must have only one selected vertice to store a position")
            
        else:
            # grab your dictionary data
            file = loadFile("vertex_data", 'r')
            dict = json.load(file)
            file.close()
            
            # set your x value in dict to the current vertext x value
            dict["z"] = selectedVerts[0].co.z
            dict["flush"] = "z"
            
            # write new value to your dictionary
            file = loadFile("vertex_data", 'w')
            json.dump(dict, file)      
        
        # back to whatever mode we were in
        bpy.ops.object.mode_set(mode=mode)
        
        return {"FINISHED"}

class SetVerticeX(bpy.types.Operator):
    
    """Defining the custom operator -copyAndShift-"""
    bl_idname = 'object.set_vertice_x'
    bl_label = 'Set Vertice X'
    
    def execute(self, context):
        #Load values from stored_values.txt
        file = loadFile("vertex_data", 'r')
        dict = json.load(file)
        
        # store previous mode
        mode = bpy.context.active_object.mode
        
        bpy.ops.object.mode_set(mode='OBJECT')
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        for v in selectedVerts:
            v.co.x = dict['x']
                      
        # back to whatever mode we were in
        bpy.ops.object.mode_set(mode=mode)
        
        return {"FINISHED"}

class SetVerticeY(bpy.types.Operator):
    
    """Defining the custom operator -copyAndShift-"""
    bl_idname = 'object.set_vertice_y'
    bl_label = 'Set Vertice Y'
    
    def execute(self, context):
        #Load values from stored_values.txt
        file = loadFile("vertex_data", 'r')
        dict = json.load(file)
        
        # store previous mode
        mode = bpy.context.active_object.mode
        
        bpy.ops.object.mode_set(mode='OBJECT')
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        for v in selectedVerts:
            v.co.y = dict['y']
                      
        # back to whatever mode we were in
        bpy.ops.object.mode_set(mode=mode)
        
        return {"FINISHED"}
        
class SetVerticeZ(bpy.types.Operator):
    
    """Defining the custom operator -copyAndShift-"""
    bl_idname = 'object.set_vertice_z'
    bl_label = 'Set Vertice Z'
    
    def execute(self, context):
        #Load values from stored_values.txt
        file = loadFile("vertex_data", 'r')
        dict = json.load(file)
        
        # store previous mode
        mode = bpy.context.active_object.mode
        
        bpy.ops.object.mode_set(mode='OBJECT')
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        for v in selectedVerts:
            v.co.z = dict['z']
                      
        # back to whatever mode we were in
        bpy.ops.object.mode_set(mode=mode)
        
        return {"FINISHED"}   

class MoveToFlush(bpy.types.Operator):
    
    """Defining the custom operator -Move Vertices to Flush-"""
    bl_idname = 'object.move_to_flush'
    bl_label = 'Move vertices to flush' 

    def execute(self, context):
        # Load values from stored_values.txt
        file = loadFile("vertex_data", 'r')
        dict = json.load(file)
        
        # store previous mode and set new mode
        mode = bpy.context.active_object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type = "ORIGIN_GEOMETRY" )
        
        print("move to flush was ran")
        
        # Collect selected vertices
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        
        # Find move distance to flush
        min_distance = selectedVerts[0].co[getFlushAxis(dict)] - getFlushCoordinate(dict)
        axis = getFlushAxis(dict)

        for v in selectedVerts:
            d = v.co[axis] - getFlushCoordinate(dict)
            if d < min_distance:
                min_distance = d
                
        print("min_distance is:", min_distance)
        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        for v in selectedVerts:
            print(v.co.z)
            v.co += Vector((0,0,min_distance))
            print(v.co.z,"p")
            
           
        # return to stored mode
        bpy.ops.object.mode_set(mode=mode) 
            
        return {"FINISHED"}
    
class MergeVertices(bpy.types.Operator): 
    # Merges vertices within a set distance from each other
    
    bl_idname = 'object.merge_vertices'
    bl_label = 'Merge Vertices'

    # Contants
    merge_limit = .05
    
    def execute(self, context):
        # Get active object
        obj = bpy.context.active_object
        
        # Get all edges
        bpy.ops.object.mode_set(mode='OBJECT')
        edges = obj.data.edges.data
        
        for e in edges:
            print(e)
            
        return {"FINISHED"}    

class OrthoRotateObjectX(bpy.types.Operator):
    bl_idname = 'object.ortho_rotate_x'
    bl_label = 'OrthoRotateX'
    
    def execute(self, context):
    
        # store previous mode and change to edit mode
        mode = bpy.context.active_object.mode
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        # get selected object, and blender vertices
        current_object = bpy.context.selected_objects[0]
        b_vertices = current_object.data.vertices
        
        # convert to a numpy array
        vertices = np.array([[b_vertice.co.x, 
                              b_vertice.co.y, 
                              b_vertice.co.z] for b_vertice in b_vertices])
        
        # perform rotation on vertices about center
        vertices = vf.orthoRotateObject(vertices, 'x')
        
        # set the b_vertice coordinates
        index = 0
        for b_vertice in b_vertices:
            b_vertice.co.x = vertices[index][0]
            b_vertice.co.y = vertices[index][1]
            b_vertice.co.z = vertices[index][2]
            
            index += 1
            
        bpy.ops.object.mode_set(mode = mode)
        
        return {"FINISHED"}
    
class OrthoRotateObjectY(bpy.types.Operator):
    bl_idname = 'object.ortho_rotate_y'
    bl_label = 'OrthoRotateY'
    
    def execute(self, context):
    
        # store previous mode and change to edit mode
        mode = bpy.context.active_object.mode
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        # get selected object, and blender vertices
        current_object = bpy.context.selected_objects[0]
        b_vertices = current_object.data.vertices
        
        # convert to a numpy array
        vertices = np.array([[b_vertice.co.x, 
                              b_vertice.co.y, 
                              b_vertice.co.z] for b_vertice in b_vertices])
        
        # perform rotation on vertices about center
        vertices = vf.orthoRotateObject(vertices, 'y')
        
        # set the b_vertice coordinates
        index = 0
        for b_vertice in b_vertices:
            b_vertice.co.x = vertices[index][0]
            b_vertice.co.y = vertices[index][1]
            b_vertice.co.z = vertices[index][2]
            
            index += 1
            
        bpy.ops.object.mode_set(mode = mode)
        
        return {"FINISHED"}

class OrthoRotateObjectZ(bpy.types.Operator):
    bl_idname = 'object.ortho_rotate_z'
    bl_label = 'OrthoRotateZ'
    
    def execute(self, context):
    
        # store previous mode and change to edit mode
        mode = bpy.context.active_object.mode
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        # get selected object, and blender vertices
        current_object = bpy.context.selected_objects[0]
        b_vertices = current_object.data.vertices
        
        # convert to a numpy array
        vertices = np.array([[b_vertice.co.x, 
                              b_vertice.co.y, 
                              b_vertice.co.z] for b_vertice in b_vertices])
        
        # perform rotation on vertices about center
        vertices = vf.orthoRotateObject(vertices, 'z')
        
        # set the b_vertice coordinates
        index = 0
        for b_vertice in b_vertices:
            b_vertice.co.x = vertices[index][0]
            b_vertice.co.y = vertices[index][1]
            b_vertice.co.z = vertices[index][2]
            
            index += 1
            
        bpy.ops.object.mode_set(mode = mode)
        
        return {"FINISHED"}

def register():
    bpy.utils.register_class(VertexTools)
    bpy.utils.register_class(MoveVertices)
    bpy.utils.register_class(StoreVertexDataX)
    bpy.utils.register_class(StoreVertexDataY)
    bpy.utils.register_class(StoreVertexDataZ) 
    bpy.utils.register_class(SetVerticeX)
    bpy.utils.register_class(SetVerticeY) 
    bpy.utils.register_class(SetVerticeZ)  
    bpy.utils.register_class(MoveToFlush) 
    bpy.utils.register_class(MergeVertices)
    bpy.utils.register_class(OrthoRotateObjectX)
    bpy.utils.register_class(OrthoRotateObjectY)
    bpy.utils.register_class(OrthoRotateObjectZ)

def unregister():
    bpy.utils.unregister_class(VertexTools)
    bpy.utils.unregister_class(MoveVertices)
    bpy.utils.unregister_class(StoreVertexDataX)
    bpy.utils.unregister_class(StoreVertexDataY)
    bpy.utils.unregister_class(StoreVertexDataZ) 
    bpy.utils.unregister_class(SetVerticeX)  
    bpy.utils.unregister_class(SetVerticeY)
    bpy.utils.unregister_class(SetVerticeZ)
    bpy.utils.unregister_class(MoveToFlush) 
    bpy.utils.unregister_class(MergeVertices)
    bpy.utils.unregister_class(OrthoRotateObjectX)
    bpy.utils.unregister_class(OrthoRotateObjectY)
    bpy.utils.unregister_class(OrthoRotateObjectZ)

if __name__ == "__main__":
    register()
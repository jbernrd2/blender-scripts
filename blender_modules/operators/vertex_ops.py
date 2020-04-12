# imports
import bpy
import json
import vertex_functions as vf
from mathutils import Vector


class MergeVertices(bpy.types.Operator):

    """Defining the custom operator -copyAndShift-"""
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
    
class MergeVerticesT(bpy.types.Operator):

    """Defining the custom operator -copyAndShift-"""
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
    
class MoveVertices(bpy.types.Operator):
    """Defining the custom operator -copyAndShift-"""
    bl_idname = 'object.move_vertices'
    bl_label = 'Copy and Shift Operator'
    
    
    def execute(self, context):
        print("ass2")
        #Load values from stored_values.txt
        path = "C:/Users/j_ber/root/blender_scripts/stored_values/values.txt"
        file = open(path, 'r')
        contents = file.read()
        
        #Read contents of file into list, put them in a dict
        contents = contents.split("\n")
        dict = {}
        for element in contents:
            if vf.checkElement(element):
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
            file = vf.loadFile("vertex_data", 'r')
            file_dict = json.load(file)
            file.close()
            
            # set your x value in dict to the current vertext x value
            file_dict["x"] = selectedVerts[0].co.x
            file_dict["flush"] = "x"
            
            # write new value to your dictionary
            file = vf.loadFile("vertex_data", 'w')
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
            file = vf.loadFile("vertex_data", 'r')
            dict = json.load(file)
            file.close()
            
            # set your x value in dict to the current vertext x value
            dict["y"] = selectedVerts[0].co.y
            dict["flush"] = "y"
            
            # write new value to your dictionary
            file = vf.loadFile("vertex_data", 'w')
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
            file = vf.loadFile("vertex_data", 'r')
            dict = json.load(file)
            file.close()
            
            # set your x value in dict to the current vertext x value
            dict["z"] = selectedVerts[0].co.z
            dict["flush"] = "z"
            
            # write new value to your dictionary
            file = vf.loadFile("vertex_data", 'w')
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
        file = vf.loadFile("vertex_data", 'r')
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
        file = vf.loadFile("vertex_data", 'r')
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
        file = vf.loadFile("vertex_data", 'r')
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
        file = vf.loadFile("vertex_data", 'r')
        dict = json.load(file)
        
        # store previous mode and set new mode
        mode = bpy.context.active_object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type = "ORIGIN_GEOMETRY" )
        
        # Collect selected vertices
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        
        # Find move distance to flush
        min_distance = selectedVerts[0].co[vf.getFlushAxis(dict)] - vf.getFlushCoordinate(dict)

        for v in selectedVerts:
            d = v.co[vf.getFlushAxis(dict)] - vf.getFlushCoordinate(dict)
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


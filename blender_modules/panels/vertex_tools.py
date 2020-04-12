#import bpy
import json
import math
import bpy
from mathutils import Vector

#from mathutils import Vector
import functions.vertex_functions as vf
 
class VertexTools(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Vertex Tools"
    bl_idname = "OBJECT_PT_operators"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    vf.initializeVertexData()
    vf.initializeStoredValues()

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
  

def register():
    import json    
    
    print("try merge")
    from operators.vertex_ops import MergeVertices
    print("Merge")
    
    print("try move")
    from operators.vertex_ops import MoveVertices
    print("Move")
    
    print("try mvt")
    from operators.vertex_ops import MoveVerticesT
    print("M2F")
    
    from operators.vertex_ops import StoreVertexDataX
    from operators.vertex_ops import StoreVertexDataY
    from operators.vertex_ops import StoreVertexDataZ
    from operators.vertex_ops import SetVerticeX
    from operators.vertex_ops import SetVerticeY
    from operators.vertex_ops import SetVerticeZ

    
    bpy.utils.register_class(VertexTools)
    bpy.utils.register_class(MoveVertices)
    bpy.utils.register_class(MergeVertices)
    bpy.utils.register_class(StoreVertexDataX())
    bpy.utils.register_class(StoreVertexDataY)
    bpy.utils.register_class(StoreVertexDataZ)   
    bpy.utils.register_class(SetVerticeX)
    bpy.utils.register_class(SetVerticeY) 
    bpy.utils.register_class(SetVerticeZ)  
    bpy.utils.register_class(MoveToFlush) 
    
    


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

if __name__ == "__main__":
    register()
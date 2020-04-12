import bpy
import functions.vertex_functions as vf

class SelectionPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Selection Panel Class"
    bl_idname = "OBJECT_PT_operators1"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Selection Tools", icon='WORLD_DATA')
        
        row = layout.row()
        row.label(text = "Select vertices in current plane")
        
        row = layout.row()
        row.operator("object.plane_select_x", text = "x plane select")
        
        row = layout.row()
        row.operator("object.plane_select_y", text = "y plane select")
        
        row = layout.row()
        row.operator("object.plane_select_z", text = "z plane select")
        
        row = layout.row()
        row.label(text = "Select vertices along a line")
        
        row = layout.row()
        row.operator("object.line_select", text = "Line Select")
     
        
class PlaneSelectX(bpy.types.Operator):
    """Selects all vertices that lie within the plane of the currently 
    selected vertex"""   
    
    bl_idname = 'object.plane_select_x'
    bl_label = 'Plane Select X'
        
    def execute(self, context):
        # tolerance value for selection
        tolerance = .00001
        
        # store previous mode
        mode = bpy.context.active_object.mode
        
        # set mode to object mode and get selected vertices
        bpy.ops.object.mode_set(mode = 'OBJECT')
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        
        if (len(selectedVerts) == 0):
            print("Must have a vertice selected!")
            return {"FINISHED"} 
        
        # set the plane height from the first selected vertice
        xVal = selectedVerts[0].co.x
        
        # set to object mode and select all vertices within tolerance
        for v in bpy.context.active_object.data.vertices:
            if abs(v.co.x - xVal) < tolerance:
                v.select = True
        
        # switch mode back and return
        bpy.ops.object.mode_set(mode=mode)
        return {"FINISHED"}
    
class PlaneSelectY(bpy.types.Operator):
    """Selects all vertices that lie within the plane of the currently 
    selected vertex"""   
    
    bl_idname = 'object.plane_select_y'
    bl_label = 'Plane Select Y'
        
    def execute(self, context):
        # tolerance value for selection
        tolerance = .00001
        
        # store previous mode
        mode = bpy.context.active_object.mode
        
        # set mode to object mode and get selected vertices
        bpy.ops.object.mode_set(mode = 'OBJECT')
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        
        if (len(selectedVerts) == 0):
            print("Must have a vertice selected!")
            return {"FINISHED"} 
        
        # set the plane height from the first selected vertice
        yVal = selectedVerts[0].co.y
        
        # set to object mode and select all vertices within tolerance
        for v in bpy.context.active_object.data.vertices:
            if abs(v.co.y - yVal) < tolerance:
                v.select = True
        
        # switch mode back and return
        bpy.ops.object.mode_set(mode=mode)
        return {"FINISHED"}

class PlaneSelectZ(bpy.types.Operator):
    """Selects all vertices that lie within the plane of the currently 
    selected vertex"""   
    
    bl_idname = 'object.plane_select_z'
    bl_label = 'Plane Select Z'
        
    def execute(self, context):
        # tolerance value for selection
        tolerance = .00001
        
        # store previous mode
        mode = bpy.context.active_object.mode
        
        # set mode to object mode and get selected vertices
        bpy.ops.object.mode_set(mode = 'OBJECT')
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        
        if (len(selectedVerts) == 0):
            print("Must have a vertice selected!")
            return {"FINISHED"} 
        
        # set the plane height from the first selected vertice
        zVal = selectedVerts[0].co.z
        
        # set to object mode and select all vertices within tolerance
        for v in bpy.context.active_object.data.vertices:
            if abs(v.co.z - zVal) < tolerance:
                v.select = True
        
        # switch mode back and return
        bpy.ops.object.mode_set(mode=mode)
        return {"FINISHED"} 
    
class LineSelect(bpy.types.Operator):
    """Selects all vertices that lie on the line of the 
    last two selected vertices"""   
    
    bl_idname = 'object.line_select'
    bl_label = 'Line Select'
        
    def execute(self, context):
        # tolerance value for selection
        tolerance = .0001
        import functions.vertex_functions as vf
        
        # store previous mode
        mode = bpy.context.active_object.mode
        
        # get selected vertices
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        selectedVerts = [v for v in bpy.context.active_object.data.vertices if v.select]
        
        if (len(selectedVerts) < 2):
            print("Must have 2 vertices selected!")
            print("Vertex length is" + str(len(selectedVerts)))
            
            return {"FINISHED"} 
        
        # find the vector between your first two selected vertices
        v1 = selectedVerts[-2].co
        v2 = selectedVerts[-1].co
        
        lineVector = vf.normalize(vf.getVector(v1,v2))
        
        # select all vertices with 1 or -1 dot product
        for v in bpy.context.active_object.data.vertices:
            v_temp = v.co
            vector_temp = vf.normalize(vf.getVector(v1, v_temp))
            
            # Check if dot product is +/- 1
            if abs(vf.dot(lineVector, vector_temp) - 1) <= tolerance:
                v.select = True            
        
        # switch mode back and return
        bpy.ops.object.mode_set(mode=mode)
        return {"FINISHED"}                 
    
def register():
    bpy.utils.register_class(SelectionPanel)
    bpy.utils.register_class(PlaneSelectX)
    bpy.utils.register_class(PlaneSelectY)
    bpy.utils.register_class(PlaneSelectZ)
    bpy.utils.register_class(LineSelect)

def unregister():
    bpy.utils.unregister_class(SelectionPanel)
    bpy.utils.unregister_class(PlaneSelectX)
    bpy.utils.unregister_class(PlaneSelectY)
    bpy.utils.unregister_class(PlaneSelectZ)
    bpy.utils.unregister_class(LineSelect)

if __name__ == "__main__":
    register()
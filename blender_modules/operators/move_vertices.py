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
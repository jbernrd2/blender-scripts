import bpy


class TemplatePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Template Panel Class"
    bl_idname = "OBJECT_PT_operators"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Template Panel", icon='WORLD_DATA')
        
        row = layout.row()
        row.operator()
        
        
        
def register():
    bpy.utils.register_class(TemplatePanel)

def unregister():
    bpy.utils.unregister_class(TemplatePanel)

if __name__ == "__main__":
    register()
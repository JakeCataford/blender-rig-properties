import bpy
from bpy.types import Panel, Menu
import rna_prop_ui

bl_info = {
    "name": "Rig Properties",
    "description": "Show bone properties from the 'PROPERTIES' bone in a panel (in pose mode) at all times.",
    "author": "Jake Cataford",
    "version": (1, 0, 0),
    "blender": (2, 82, 0),
    "location": "3D View > Item",
    "warning": "", 
    "wiki_url": "",
    "doc_url": "",
    "tracker_url": "",
    "category": "Rigging"
}

class RIGPROP_PT_PropertiesAccess(Panel):
    bl_label = "Rig Properties"
    bl_idname = "RIGPROP_PT_properties_panel"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"

    @classmethod
    def poll(self, context):
        return context.active_object and context.active_object.type == 'ARMATURE' and context.mode == 'POSE'

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        rna_prop_ui.draw(col, context, f'object.pose.bones["PROPERTIES"]', bpy.types.PoseBone, use_edit=False)

def unregister():
    bpy.utils.unregister_class(RIGPROP_PT_PropertiesAccess)

def register():
    bpy.utils.register_class(RIGPROP_PT_PropertiesAccess)

if __name__ == "__main__":
    register()
#https://blender.stackexchange.com/questions/41351/is-there-a-way-to-select-edges-marked-as-sharp-via-python/41353#41353
#https://docs.blender.org/api/blender_python_api_2_65_5/info_tutorial_addon.html

#TODO: Add description to the addon

bl_info = {
    "name": "Select Edges Marked Sharp & Seam",
    "author": "Ayodeji Osokoya",
    "version": (0, 2),
    "blender": (2, 80, 0),
    "location": "Edit Mode > Select Menu", #TODO: fix this
    "description": "Select all edges marked as sharp or as seam",
    "warning": "",
    "wiki_url": "",
    "category": "Mesh"
}

import bpy
import bmesh

class SelectSharpEdges(bpy.types.Operator):
    """Select Edges Marked Sharp""" #tooltip for menu items and buttons.
    bl_idname = "object.select_edges_marked_sharp" # unique identifier for buttons and menu items to reference.
    bl_label = "Select Edges Marked Sharp" # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        objects = bpy.context.selected_editable_objects
        
        for obj in objects:
            bm = bmesh.from_edit_mesh(obj.data)

            for e in bm.edges:
                if not e.smooth:
                    e.select = True

            bmesh.update_edit_mesh(obj.data)

        return {'FINISHED'}

class SelectSeamEdges(bpy.types.Operator):
    """Select Edges Marked Seam"""
    bl_idname = "object.select_edges_marked_seam"
    bl_label = "Select Edges Marked Seam"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        objects = bpy.context.selected_editable_objects

        for obj in objects:
            bm = bmesh.from_edit_mesh(obj.data)

            for e in bm.edges:
                if e.seam:
                    e.select = True

            bmesh.update_edit_mesh(obj.data)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(SelectSharpEdges)
    bpy.utils.register_class(SelectSeamEdges)
    bpy.types.VIEW3D_MT_select_edit_mesh.append(menu_func)

def unregister():
    bpy.utils.unregister_class(SelectSharpEdges)
    bpy.utils.unregister_class(SelectSeamEdges)

def menu_func(self, context):
    self.layout.operator(SelectSharpEdges.bl_idname)
    self.layout.operator(SelectSeamEdges.bl_idname)

# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
#if __name__ == "__main__":
#    register()

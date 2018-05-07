#https://blender.stackexchange.com/questions/41351/is-there-a-way-to-select-edges-marked-as-sharp-via-python/41353#41353
#https://docs.blender.org/api/blender_python_api_2_65_5/info_tutorial_addon.html

#TODO: Add to the Select Menu in edit mode
#TODO: Add description to the addon
#TODO: Break apart in to files
#TODO: Experiment with Bpy Context

bl_info = {
    "name": "Select Edges Marked Sharp",
    "author": "Ayodeji Osokoya",
    "version": (0, 1),
    "blender": (2, 79, 0),
    "location": "Edit Mode > Select Menu", #TODO: fix this
    "description": "Select all edges marked as sharp",
    "warning": "",
    "wiki_url": "https://wiki.blender.org/index.php/Extensions:2.6/"
                "Py/Scripts/Modeling/Extra_Tools",
    "category": "Mesh"
}

import bpy
import bmesh

class SelectSharpEdges(bpy.types.Operator):
    """Select Edges Marked Sharp"""      # blender will use this as a tooltip for menu items and buttons.
    bl_idname = "object.select_edges_marked_sharp"        # unique identifier for buttons and menu items to reference.
    bl_label = "Select Edges Marked Sharp"         # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.

    def execute(self, context):        # execute() is called by blender when running the operator.
        obj = bpy.context.edit_object
        me = obj.data

        bm = bmesh.from_edit_mesh(me)
        for e in bm.edges:
            if not e.smooth:
                e.select = True

        bmesh.update_edit_mesh(me, False)

        return {'FINISHED'}            # this lets blender know the operator finished successfully.



def register():
    bpy.utils.register_class(SelectSharpEdges)
    bpy.types.VIEW3D_MT_select_edit_mesh.append(menu_func)

def unregister():
    bpy.utils.unregister_class(SelectSharpEdges)

def menu_func(self, context):
    self.layout.operator(SelectSharpEdges.bl_idname)

# This allows you to run the script directly from blenders text editor
# to test the addon without having to install it.
if __name__ == "__main__":
    register()

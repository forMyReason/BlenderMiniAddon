import bpy

class RenameObjectOperator(bpy.types.Operator):
    bl_idname = "object.rename"
    bl_label = "rename objects"

    def execute(self,context):
        props = context.scene.second_props
        selected_object = context.selected_objects[0]
        selected_object.name = props.new_name
        print("Rename Success:" + selected_object.name)
        return {'FINISHED'}

blender_classes = [
    RenameObjectOperator,
]

def register():
    for b_class in blender_classes:
        bpy.utils.register_class(b_class)

def unregister():
    for b_class in blender_classes:
        bpy.utils.unregister_class(b_class)
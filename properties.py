import bpy
from . import functions
from bpy.types import PropertyGroup
from bpy.props import(
    IntProperty,
    StringProperty,
    PointerProperty,
    EnumProperty,
    BoolProperty,
)

class PluginsProperties(PropertyGroup):
    new_name : StringProperty(
        name = "",
        default = "this is new name"
    )

blender_classes = [
    PluginsProperties,
]

def register():
    for b_class in blender_classes:
        bpy.utils.register_class(b_class)
    bpy.types.Scene.second_props = PointerProperty(type = PluginsProperties)

def unregister():
    for b_class in blender_classes:
        bpy.utils.unregister_class(b_class)
    del bpy.types.Scene.second_props
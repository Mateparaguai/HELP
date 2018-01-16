import bpy

from bpy.types import(
        Panel,
        Operator,
        PropertyGroup
        )

from bpy.props import(
        StringProperty,
        PointerProperty,
        FloatProperty
        )

class HelloWorldPanel(Panel):
    """Creates a Panel in the Scene properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        # you need to get your stored properties to draw them
        scene = context.scene.your_properties 

        col = layout.column()
        col.prop(scene, "string")
        col = layout.column()
        col.prop(scene, "size")
        col = layout.column()
        col.operator("some.thing")

class Add_some_thing(Operator):

    bl_idname = "some.thing"
    bl_label = "Add object"
    bl_description = "some description"

    def execute(self, context):

        # you need to get your stored properties
        scene = context.scene.your_properties 
        # you get some of your properties to use them
        string = scene.string
        size = scene.size

        # you do some thing to use your property with
        bpy.ops.mesh.primitive_cube_add()
        # you can change some of the added object props as the defined in the ui property 
        context.active_object.name = string 
        context.active_object.scale = [size, size, size]
        return {'FINISHED'}

# your properties here
class addon_Properties(PropertyGroup):

    string = StringProperty(
        name = "the name",
        description="name of the object to add",
        default = ""
        )
    size = FloatProperty(
        name = "size",
        description = "size of the object to add",
        default = 1.0,
        )    

classes = (
    HelloWorldPanel,
    addon_Properties,
    Add_some_thing
    )

def register():

    for cls in classes:
        bpy.utils.register_class(cls)
    # you store your properties in the scene
    bpy.types.Scene.your_properties = PointerProperty(type=addon_Properties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    # you delete your properties
    del bpy.types.Scene.your_properties

if __name__ == "__main__":
    register()

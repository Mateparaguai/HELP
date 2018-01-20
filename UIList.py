import bpy


class MATERIAL_UL_matslots_example(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        ob = data
        slot = item
        ma = slot.material

        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            if ma:
                layout.prop(ma, "name", text="", emboss=False, icon_value=icon)
            else:
                layout.label(text="", translate=False, icon_value=icon)
            if ma and not context.scene.render.use_shading_nodes:
                manode = ma.active_node_material
                if manode:
                    layout.label(text="Node %s" % manode.name, translate=False, icon_value=layout.icon(manode))
                elif ma.use_nodes:
                    layout.label(text="Node <none>", translate=False)
                else:
                    layout.label(text="")
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)


class UIListPanelExample(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "UIList Panel"
    bl_idname = "OBJECT_PT_ui_list_example"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object
 
        layout.template_list("MATERIAL_UL_matslots_example", "", obj, "material_slots", obj, "active_material_index")

        layout.template_list("MATERIAL_UL_matslots_example", "compact", obj, "material_slots",
                             obj, "active_material_index", type='COMPACT')

def register():
    bpy.utils.register_class(MATERIAL_UL_matslots_example)
    bpy.utils.register_class(UIListPanelExample)


def unregister():
    bpy.utils.unregister_class(MATERIAL_UL_matslots_example)
    bpy.utils.unregister_class(UIListPanelExample)


if __name__ == "__main__":
    register()

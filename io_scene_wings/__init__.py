bl_info = {
    "name": "Wings3d import/export",
    "description": "import or export Wings3d .wings files",
    "author": "Danni coy",
    "version": (1,0),
    "blender": (2, 5, 7),
    "api": 31236,
    "location": "File > Import-Export",
    "warning": '', # used for warning icon and text in addons panel
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.5/Py/"\
        "Scripts/Wings3d",
    "tracker_url": "http://projects.blender.org/tracker/index.php?"\
        "func=detail&aid=<number>",
    "category": "Import-Export"}

import bpy
from bpy.props import StringProperty, FloatProperty, IntProperty, BoolProperty, EnumProperty
from io_utils import ImportHelper, ExportHelper

class ImportWings(bpy.types.Operator, ImportHelper):
    '''Load a BVH motion capture file'''
    bl_idname = "import_wings.wings"
    bl_label = "Import Wings"
    bl_options = {'REGISTER', 'UNDO'}

    filename_ext = ".wings"
    filter_glob = StringProperty(default="*.wings", options={'HIDDEN'})
    
    def execute(self, context):
        from . import import_wings
        return import_wings.load(self, context, **self.as_keywords(ignore=("filter_glob",)))

#class ExportBVH(bpy.types.Operator, ExportHelper):
#   '''Save a BVH motion capture file from an armature'''
#    bl_idname = "export_wings.wings"
#    bl_label = "Export Wings"

#    filename_ext = ".wings"
#    filter_glob = StringProperty(default="*.wings", options={'HIDDEN'})
    
#    def execute(self, context):
#        from . import export_wings
#        return export_wings.save(self, context, **self.as_keywords(ignore=("check_existing", "filter_glob")))


def menu_func_import(self, context):
    self.layout.operator(ImportWings.bl_idname, text="Wings3d (.wings)")


#def menu_func_export(self, context):
#    self.layout.operator(ExportWings.bl_idname, text="Wings3d (.wings)")
  

def register():
  bpy.utils.register_module(__name__);
  bpy.types.INFO_MT_file_import.append(menu_func_import);
  #bpy.types.INFO_MT_file_export.append(menu_func_export);

def unregister():
  bpy.utils.unregister_module(__name__);
  bpy.types.INFO_MT_file_import.remove(menu_func_import);
  #bpy.types.INFO_MT_file_export.remove(menu_func_export);

if __name__ == "__main__":
  register()
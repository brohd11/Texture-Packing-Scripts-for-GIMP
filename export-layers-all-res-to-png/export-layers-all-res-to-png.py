import os
from gimpfu import *

def python_fu_export_layers_all_res_to_png(image, drawable):
    
    file_path_ext = pdb.gimp_image_get_filename(image)
    file_path = os.path.splitext(file_path_ext)[0]
    file_path_parent = os.path.dirname(file_path)
    file_path_parent_parent = os.path.dirname(file_path_parent)
    file_name_ext = pdb.gimp_item_get_name(image.layers[0])
    file_name = os.path.splitext(file_name_ext)[0]
    
    pdb.python_fu_export_layers_4k_to_png(image, drawable)
    pdb.python_fu_export_layers_2k_to_png(image, drawable)
    pdb.python_fu_export_layers_1k_to_png(image, drawable)
    pdb.python_fu_export_layers_512_to_png(image, drawable)

    pdb.gimp_message("Done all exports.")
    pdb.gimp_progress_end()


# Register the script in GIMP
register(
    "python_fu_export_layers_all_res_to_png",
    "Export Layers All Res to PNG",
    "Export Layers All Res to PNG",
    "Brohd",
    "Brohd",
    "2024",
    "<Image>/Filters/MyScripts/Export Layers All Res to PNG",
    "*",
    [],
    [],
    python_fu_export_layers_all_res_to_png
)

main()
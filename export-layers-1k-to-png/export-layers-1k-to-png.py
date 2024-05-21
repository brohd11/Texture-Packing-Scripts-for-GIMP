import os
from gimpfu import *

def python_fu_export_layers_1k_to_png(image, drawable):
    
    target_res = 1024
    target_res_str = "1k"
    export_file_type = ".png"
    
    file_path_ext = pdb.gimp_image_get_filename(image)
    file_path = os.path.splitext(file_path_ext)[0]
    file_path_parent = os.path.dirname(file_path)
    file_name_ext = pdb.gimp_item_get_name(image.layers[0])
    file_name = os.path.splitext(file_name_ext)[0]

    
    
    
    if not file_path:
        gimp.message("No file path associated with the image.")
    else:
        gimp.message("File path: " + str(file_path))

    original_width = image.width
    original_height = image.height
    
    if not original_width >= target_res and not original_height >= target_res:
        gimp.message("Images smaller than " + target_res_str + ".")
        pdb.gimp_progress_end()
        return
    if not original_height >= target_res and not original_width >= target_res:
        gimp.message("Images smaller than " + target_res_str + ".")
        pdb.gimp_progress_end()
        return

    aspect = float(original_width) / float(original_height)

    width = target_res
    height = target_res

    if original_height > original_width:
        height = target_res
        width = target_res * aspect
    elif original_width > original_height:
        width = target_res
        height = target_res * (1 / aspect)
    else:
        width = target_res
        height = target_res
    gimp.message(str(aspect))
    gimp.message(str(width) + ", " + str(height))

    layers = image.layers

    for i in layers:
        if i.height != original_height:
            gimp.message("All layers must be same size.")
            return
        if i.width != original_width:
            gimp.message("All layers must be same size.")
            return
    
    new_dir = os.path.join(file_path_parent, "1k")

    
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
        gimp.message("Created new folder.")
    
    
    counter = 0

    for i in layers:
        counter += 1
        dupe_image = pdb.gimp_image_new(width, height, 0)

        new_layer = pdb.gimp_layer_new(dupe_image, original_width, original_height, RGB_IMAGE, "Layer1", 100, NORMAL_MODE)
       
        pdb.gimp_image_insert_layer(dupe_image, new_layer, None, 0)
       

        pdb.gimp_edit_copy(i)
        floating_sel = pdb.gimp_edit_paste(new_layer, False)
        pdb.gimp_floating_sel_anchor(floating_sel)

        pdb.gimp_layer_scale(new_layer, width, height, False)

        layer_file_name_ext = pdb.gimp_item_get_name(i)
        layer_file_name = os.path.splitext(layer_file_name_ext)[0]
        adj_file_name = layer_file_name + "_" + target_res_str

        if str(layer_file_name).find("8k") > 0:
            adj_file_name = layer_file_name.replace("8k", target_res_str)
        if str(layer_file_name).find("8K") > 0:
            adj_file_name = layer_file_name.replace("8K", target_res_str)
        if str(layer_file_name).find("4k") > 0:
            adj_file_name = layer_file_name.replace("4k", target_res_str)
        if str(layer_file_name).find("4K") > 0:
            adj_file_name = layer_file_name.replace("4K", target_res_str)
        if str(layer_file_name).find("2k") > 0:
            adj_file_name = layer_file_name.replace("2k", target_res_str)
        if str(layer_file_name).find("2K") > 0:
            adj_file_name = layer_file_name.replace("2K", target_res_str)
        if str(layer_file_name).find("1k") > 0:
            adj_file_name = layer_file_name.replace("1k", target_res_str)
        if str(layer_file_name).find("1K") > 0:
            adj_file_name = layer_file_name.replace("1K", target_res_str)

        export_fp = os.path.join(new_dir, adj_file_name + export_file_type)

        pdb.file_png_save(dupe_image, dupe_image.layers[0], export_fp, export_fp, 0, 9, 0, 0, 0, 0, 0)
        pdb.gimp_image_delete(dupe_image)
        pdb.gimp_message("Done image" + str(counter) + ".")


    pdb.gimp_message("Done all.")
    pdb.gimp_progress_end()


# Register the script in GIMP
register(
    "python_fu_export_layers_1k_to_png",
    "Export Layers 1k to PNG",
    "Export Layers 1k to PNG",
    "Brohd",
    "Brohd",
    "2024",
    "<Image>/Filters/MyScripts/Export Layers 1k to PNG",
    "*",
    [],
    [],
    python_fu_export_layers_1k_to_png
)

main()
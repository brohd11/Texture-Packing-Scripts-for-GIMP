import os
from gimpfu import *

def python_fu_pack_textures_rgba_to_png(image, drawable):

    export_file_type = "_packed.png"
    
    file_path_ext = pdb.gimp_image_get_filename(image)
    file_path = os.path.splitext(file_path_ext)[0]
    file_name_ext = pdb.gimp_item_get_name(image.layers[0])
    file_name = os.path.splitext(file_name_ext)[0]

    if not file_path:
        gimp.message("No file path associated with the image.")
    else:
        gimp.message("File path: " + str(file_path))

    layers = image.layers
   
    if not len(layers) == 2:
	gimp.message("Need 2 layers.")
	return
        
    red2 = layers[1]
	
  
    decomposed_id = pdb.plug_in_decompose(image, layers[0], "RGB", TRUE)
    
    decomposed = decomposed_id[0]
    decomposed_layers =  decomposed.layers
    
    if decomposed:

        # Get the width and height of the original image
        width = image.width
        height = image.height

	#insert new layers in decomposed and copy 2nd layer to it
	layer_red2 = pdb.gimp_layer_new(decomposed, width, height, GRAY_IMAGE, "Layer 4", 100, NORMAL_MODE)
	pdb.gimp_image_insert_layer(decomposed, layer_red2, None, 3)

	pdb.gimp_edit_copy(red2)
        floating_sel = pdb.gimp_edit_paste(layer_red2, False)
        pdb.gimp_floating_sel_anchor(floating_sel)
	
        decomposed_layers =  decomposed.layers
	
        # Compose the new RGBA image
        composed_image = pdb.plug_in_drawable_compose(decomposed, decomposed_layers[0], decomposed_layers[1], decomposed_layers[2], decomposed_layers[3], "RGBA")
        
    else:
        pdb.gimp_message("Error: Unable to decompose layers.")

    export_fp = file_path + export_file_type

    pdb.file_png_save(composed_image, composed_image.layers[0], export_fp, export_fp, 0, 9, 0, 0, 0, 0, 0)

    pdb.gimp_message("Done.")

    pdb.gimp_progress_end()
    pdb.gimp_image_delete(decomposed)
    pdb.gimp_image_delete(composed_image)

# Register the script in GIMP
register(
    "python_fu_pack_textures_rgba_to_png",
    "Pack Textures RGBA to PNG",
    "Pack Textures RGBA to PNG",
    "Brohd",
    "Brohd",
    "2024",
    "<Image>/Filters/MyScripts/Pack Textures RGBA to PNG",
    "*",
    [],
    [],
    python_fu_pack_textures_rgba_to_png
)

main()
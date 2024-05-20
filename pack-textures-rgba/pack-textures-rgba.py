from gimpfu import *

def python_fu_pack_textures_rgba(image, drawable):

    layers = image.layers
      
    if not len(layers) == 2:
	gimp.message("Need 2 layers.")
	return
  
    decomposed_id = pdb.plug_in_decompose(image, layers[0], "RGB", TRUE)
    
    decomposed = decomposed_id[0]
    decomposed_layers =  decomposed.layers
    
    if decomposed:

        # Get the width and height of the original image
        width = image.width
        height = image.height
	
    
        # Get the second layer from the original image
        red2 = layers[1]

	#insert new layers in decomposed and copy 2nd layer to it
	layer_red2 = pdb.gimp_layer_new(decomposed, width, height, GRAY_IMAGE, "Layer 4", 100, NORMAL_MODE)
	pdb.gimp_image_insert_layer(decomposed, layer_red2, None, 3)

	pdb.gimp_edit_copy(red2)
        floating_sel = pdb.gimp_edit_paste(layer_red2, False)
        pdb.gimp_floating_sel_anchor(floating_sel)
	
        decomposed_layers =  decomposed.layers

	
        # Compose the new RGBA image
        composed_image = pdb.plug_in_drawable_compose(decomposed, decomposed_layers[0], decomposed_layers[1], decomposed_layers[2], decomposed_layers[3], "RGBA")


        if composed_image != -1:

            gimp.Display(composed_image)

            pdb.gimp_message("Done.")

        else:
            pdb.gimp_message("Error: Compose failed.")
    else:
        pdb.gimp_message("Error: Unable to decompose layers.")

    pdb.gimp_progress_end()
    pdb.gimp_image_delete(decomposed)
    


# Register the script in GIMP
register(
    "python_fu_pack_textures_rgba",
    "Pack Textures RGBA",
    "Pack Textures RGBA",
    "Brohd",
    "Brohd",
    "2024",
    "<Image>/Filters/MyScripts/Pack Textures RGBA",
    "*",
    [],
    [],
    python_fu_pack_textures_rgba
)

main()
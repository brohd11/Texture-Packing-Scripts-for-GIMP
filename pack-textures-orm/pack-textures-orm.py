import os
from gimpfu import *

def python_fu_pack_textures_orm(image, drawable):
    
    #file_path_ext = pdb.gimp_image_get_filename(image)
    #file_path = os.path.splitext(file_path_ext)[0]
    #file_name_ext = pdb.gimp_item_get_name(image.layers[0])
    #file_name = os.path.splitext(file_name_ext)[0]

    #if not file_path:
        #gimp.message("No file path associated with the image.")
    #else:
        #gimp.message("File path: " + str(file_path))

    layer_check = image.layers
    if not len(layer_check) == 3:
	gimp.message("Need 3 layers.")
	return
	
    # Get the width and height of the original image
    width = image.width
    height = image.height

    dupe_image = pdb.gimp_image_duplicate(image)
    pdb.gimp_convert_grayscale(dupe_image)

    white_layer = pdb.gimp_layer_new(dupe_image, width, height, GRAY_IMAGE, "Layer 4", 100, NORMAL_MODE)
    pdb.gimp_image_insert_layer(dupe_image, white_layer, None, 3)

    layers = dupe_image.layers

    # Compose the new RGB image
    composed_image = pdb.plug_in_drawable_compose(dupe_image, layers[0], layers[1], layers[2], layers[3], "RGB")

    gimp.Display(composed_image)

    gimp.message("Done.")

    pdb.gimp_progress_end()
    pdb.gimp_image_delete(dupe_image)

# Register the script in GIMP
register(
    "python_fu_pack_textures_orm",
    "Pack Textures ORM",
    "Pack Textures ORM",
    "Brohd",
    "Brohd",
    "2024",
    "<Image>/Filters/MyScripts/Pack Textures ORM",
    "*",
    [],
    [],
    python_fu_pack_textures_orm
)

main()
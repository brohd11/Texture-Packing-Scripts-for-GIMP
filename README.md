# Texture-Packing-Scripts-for-GIMP

Scripts to speed up/ simplify texture packing. My main use cases Terrain3D textures with Godot and ORM packing.

Copy to (default install) C:\Users\User\AppData\Roaming\GIMP\2.10\plug-ins

Restart GIMP, after copying files.

Filters/MyScripts to run the scripts.

The scripts that output files will write to the folder that the first image was copied in from.

Quick runthrough on youtube: https://youtu.be/yfUFvIKG4tA

Note:
I have PNG compression set to 9, which is default for GIMP. It is pretty slow but saves alot of space. Can be changed anywhere from 0-9 in this line:

    pdb.file_png_save(composed_image, composed_image.layers[0], export_fp, export_fp, 0, 9, 0, 0, 0, 0, 0)




**Script functions:**

**Pack Textures RGBA** - Decomposes layer 1 and recomposes with layer 2 in alpha. Returns composed image.

**Pack Textures RGBA to PNG** - Continues the script to export to PNG and then delete stray files(composed image in GIMP). Exports to folder where the first image was imported from.

**Pack Textures RGBA to DDS** - Same as PNG, except using the settings specified for Terrain3D plug-in by TokisanGames

**Pack Textures ORM** - Duplicates image, sets to gray scale and then composes the 3 layers. Returns composed image.

**Pack Textures ORM to PNG** - Continues script to export to PNG and then delete stray files(duped imag and composed image in GIMP). Exports to folder where the first image was imported from.

**Pack Textures OR to PNG** - In case where no metalness map is available, it will insert a black layer(non-metallic) and follow the same export procedure.


**Export Layers Xk to PNG** - These scripts will export all layers in an image at the new resolution, into a new folder where the first image was exported from.
I use it by dragging in the first image into GIMP and then selecting the rest of the images and dragging all into the layers menu. Good for resizing all the textures for a given material at once.
Will also rename if it has a resolution in the filename(1k-8k).



I may make a 4 channel pack in the near future, the ORM already has a 4th layer added due to how compose works through script. It would be a small modification to create Pack "4 Channel to RGBA"

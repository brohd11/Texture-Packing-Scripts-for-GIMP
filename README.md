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

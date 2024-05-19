(define (script-fu-pack-textures-or-to-orm image drawable)
  (let* (
	 (gimp-image-convert-grayscale image)
         (layers (cadr (gimp-image-get-layers image)))
         (red1 (aref layers 0))
         (red2 (aref layers 1))
         (width (car (gimp-image-width image)))
         (height (car (gimp-image-height image)))
         (red1-image (car (gimp-image-new width height GRAY)))
         (layer (car (gimp-layer-new red1-image width height GRAY-IMAGE "Layer 1" 100 NORMAL-MODE)))
         (red2-image (car (gimp-image-new width height GRAY)))
         (layer2 (car (gimp-layer-new red2-image width height GRAY-IMAGE "Layer 2" 100 NORMAL-MODE)))
	 (black-image (car (gimp-image-new width height GRAY)))
	 (layer3 (car (gimp-layer-new black-image width height GRAY-IMAGE "Layer 3" 100 NORMAL-MODE)))
	)
	     
            
        (gimp-image-insert-layer red1-image layer 0 0)
        (gimp-edit-copy red1)
        (let ((floating-sel (car (gimp-edit-paste layer FALSE))))
          (gimp-floating-sel-anchor floating-sel))
	(gimp-image-insert-layer red2-image layer2 0 0)
        (gimp-edit-copy red2)
        (let ((floating-sel (car (gimp-edit-paste layer2 FALSE))))
          (gimp-floating-sel-anchor floating-sel))

	(gimp-context-set-foreground '(0 0 0))
	(gimp-image-insert-layer black-image layer3 0 0)
	(gimp-drawable-fill layer3 FILL-FOREGROUND)

	(let ((composed-image (car (plug-in-compose RUN-NONINTERACTIVE red1-image 0 red2-image black-image 0 "RGB"))))
	
	(if (not (= -1 composed-image))
	  
	    (gimp-display-new composed-image)
	    
	  )
	(gimp-message "Error: Compose failed."))
	
    )
)


(script-fu-register
  "script-fu-pack-textures-or-to-orm"
  "<Image>/Filters/MyScripts/Pack Textures OR to ORM"
  "Pack Textures OR to ORM"
  "Brohd"
  "Brohd"
  "2024"
  "*"
  SF-IMAGE "Image" 0
  SF-DRAWABLE "Drawable" 0
)

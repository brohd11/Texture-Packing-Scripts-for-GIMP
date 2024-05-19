(define (script-fu-pack-textures-rgba image drawable)
  (let* (
         (layers (cadr (gimp-image-get-layers image)))
         (layer1 (aref layers 0))
         (decomposed1 (car (plug-in-decompose RUN-NONINTERACTIVE image layer1 "RGB" TRUE)))
        )
    (if (and (not (= -1 decomposed1)))
      (let* (
             (red1 (car (gimp-image-get-layer-by-name decomposed1 "red")))
             (green1 (car (gimp-image-get-layer-by-name decomposed1 "green")))
             (blue1 (car (gimp-image-get-layer-by-name decomposed1 "blue")))
      	     (layers (cadr (gimp-image-get-layers image)))
             (red2 (aref layers 1))
             (width (car (gimp-image-width image)))
             (height (car (gimp-image-height image)))
             (red1-image (car (gimp-image-new width height GRAY)))
             (layer (car (gimp-layer-new red1-image width height GRAY-IMAGE "Layer 1" 100 NORMAL-MODE)))
             (green1-image (car (gimp-image-new width height GRAY)))
	     (layer2 (car (gimp-layer-new green1-image width height GRAY-IMAGE "Layer 2" 100 NORMAL-MODE)))
             (blue1-image (car (gimp-image-new width height GRAY)))
	     (layer3 (car (gimp-layer-new blue1-image width height GRAY-IMAGE "Layer 3" 100 NORMAL-MODE)))
             (red2-image (car (gimp-image-new width height GRAY)))
	     (layer4 (car (gimp-layer-new red2-image width height GRAY-IMAGE "Layer 4" 100 NORMAL-MODE)))
	     
            )
        (gimp-image-insert-layer red1-image layer 0 0)
        (gimp-edit-copy red1)
        (let ((floating-sel (car (gimp-edit-paste layer FALSE))))
          (gimp-floating-sel-anchor floating-sel))
	(gimp-image-insert-layer green1-image layer2 0 0)
        (gimp-edit-copy green1)
        (let ((floating-sel (car (gimp-edit-paste layer2 FALSE))))
          (gimp-floating-sel-anchor floating-sel))
	(gimp-image-insert-layer blue1-image layer3 0 0)
        (gimp-edit-copy blue1)
        (let ((floating-sel (car (gimp-edit-paste layer3 FALSE))))
          (gimp-floating-sel-anchor floating-sel))
	(gimp-image-insert-layer red2-image layer4 0 0)
        (gimp-edit-copy red2)
        (let ((floating-sel (car (gimp-edit-paste layer4 FALSE))))
          (gimp-floating-sel-anchor floating-sel))

	(let ((composed-image (car (plug-in-compose RUN-NONINTERACTIVE red1-image 0 green1-image blue1-image red2-image "RGBA"))))
	
	(if (not (= -1 composed-image))
	  
	    (gimp-display-new composed-image)
	    
	  )
	(gimp-message "Error: Compose failed."))

        )
      (gimp-message "Error: Unable to decompose layers.")
      )

	
    )
)


(script-fu-register
  "script-fu-pack-textures-rgba"
  "<Image>/Filters/MyScripts/Pack Textures RGBA"
  "Pack Textures RGBA"
  "Brohd"
  "Brohd"
  "2024"
  "*"
  SF-IMAGE "Image" 0
  SF-DRAWABLE "Drawable" 0
)
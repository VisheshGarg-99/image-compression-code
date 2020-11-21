#-----------------------------------multiple-image compression code----------------------------

import PIL            #-----------------------------------Pillow library
from PIL import Image
import os

mywidth = 2000        #-------------------------------------default image width
source_dir = r'<enter the source path>'                 #--------source directory path 
destination_dir = r'<enter the destination path>'	     #-------------destination directory path




#--------------------------compression code--------------------------------------------------- 
def resize_image(old_pic, new_pic, mywidth):
	
	img = Image.open(old_pic)     #-----------------------------original image 

	wpercent = (mywidth/float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)

	img.save(new_pic)    #-------------------------------------save compressed image



#------------------------directory loop code-----------------------------------------
def entire_dir(source_dir, destination_dir, mywidth):
	files = os.listdir(source_dir)
	i = 0 
	for file in files:
		i+=1
		filename, fileext = os.path.splitext(file)
		old_pic = source_dir + '\\' + file    #-----------------source image file path  
		
		if fileext == ".jpg":
			source_path = old_pic
		elif fileext == ".jpeg":
			source_path = old_pic
		else:
			continue

		new_pic = destination_dir + '\\' + file  #-compressed image file path
		
		resize_image(old_pic , new_pic, mywidth)
		print(i,"done") 	#-----------------------------------number of files done




entire_dir(source_dir, destination_dir , mywidth)


#--------------------------------------code end------------------------------------------------

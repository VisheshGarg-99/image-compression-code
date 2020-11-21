#-----------------------------------single-image compression code-----------------------------


import PIL 					#-----------------------------------Pillow library
from PIL import Image

mywidth = <enter image width>				#-------------------------------------image width


#--------------------------compression code--------------------------------------------------- 


img = Image.open(r'<enter the image path>') #------------original image path

wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)

img.save(r'<enter the path were you want to save the image>')  #-------------------------compressed image path



'''-------------------------------------code end-------------------------------------------'''

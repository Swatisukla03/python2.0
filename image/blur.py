from PIL import Image,ImageFilter
img=Image.open("image\wallpaper1.jpg")
img1=img.filter(ImageFilter.BLUR)
img1.show()
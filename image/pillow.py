from PIL import Image
img=Image.open("image\wallpaper2.jpg")
# img.show() 
print(img.mode) 
print(img.size) 
print(img.format)
rotate_img=img.rotate(50)
# rotate_img.show(90)
# pass it as a tuple
resized_img=img.resize((200,300))
# resized_img.show()
resized_img.save("resized.jpg")
img2=img.copy()
img2.show()

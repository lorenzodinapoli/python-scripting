from PIL import Image, ImageFilter

img = Image.open("Image Path")

# Reducing size of file - Tries to keep ratio
img.thumbnail(400, 400)

# Sharpening image
filtered_img = img.filter(ImageFilter.SHARPEN)

# Black and white image
convert_img = img.convert('L')

# Resize image
resized_img = img.resize((300, 300))

# Crop an image
box = (100, 100, 400, 400)
cropped_img = img.crop(box)

img.save("file name", "png")
img.show()


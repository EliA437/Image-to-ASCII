from PIL import Image

image_name = "stang.png"

img = Image.open(image_name)

# Resize image
width, height = img.size
aspect_ratio = height/width
new_width = 100
new_height = aspect_ratio * new_width * 0.5
img = img.resize((new_width, int(new_height)))

# Convert to grayscale
img = img.convert('L')

# Get all the pixels of the image
pixels = img.getdata()

# Replace pixels with intesity in a defined range of characters from list
characters = ["B", "s", "#", "&", "@", "$", "%", "*", "!", ":", "."]
new_pixels = [characters[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# Split string of characters into multiple strings of length equal to new width
new_pixels_count = len(new_pixels)
ascii_img = [new_pixels[index: index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_img = "\n".join(ascii_img)

with open("ascii_image.txt", "w") as f: # Opens ascii_image.txt file in write mode
    f.write(ascii_img)
from PIL import Image

# Converts a file from RGB to greyscale
img = Image.open('image.png').convert('LA')
img.save('greyscale.png')



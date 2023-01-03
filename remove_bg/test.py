from rembg import remove

from PIL import Image


input_image = Image.open("dada.png")
output = remove(input_image)
output.save("dada_new.png")

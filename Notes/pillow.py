import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costume.gif", save_all=True, append_images=[images[1]], duration=200, loop=0

)


# give images file names you want to make gif of in CLA.

# we can also explore audios and videos.

# pillow lib functionalities:

from PIL import Image
from PIL import ImageFilter


def main():
    img = Image.open("in.jpeg")           # opens the image into the program. Inside the bracket write file name.
    img.close()                           # its good practice to close the img as soon as you are done

    with Image.open("in.jpeg") as img:    # alternate way to open the image, through this there is no need to explicitly close the file.
        print(img.size)                    # it will print size of the image
        print(img.format)                  # tells the file type

        img = img.rotate(90)                # rotate the image by 90 degree and store it in img variable
        img.save("out.jpeg")                # the updated image will be saved in this file

        # applying filters
        blur = img.filter(ImageFilter.BLUR)
        blur.save("blur.jpeg")
        edge = img.filter(ImageFilter.FIND_EDGES)
        edge.save("edge.jpeg")

main()
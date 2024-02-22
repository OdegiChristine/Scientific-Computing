import PIL.Image

# ASCII characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


# Resize image according to new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image


# Convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image


# Convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def main():
    # Attempt to open an image from user input
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except Exception as e:
        print(f"Error: {e}\n{path} is not a valid pathname or an image.")
        return

    # convert image to ASCII
    resized_image = resize_image(image)
    grayscale_image = grayify(resized_image)
    ascii_characters = pixels_to_ascii(grayscale_image)

    # format
    width = resized_image.width
    # pixel_count = len(new_image_data)
    ascii_image = "\n".join(ascii_characters[i:(i + width)] for i in range(0, len(ascii_characters), width))

    # print result
    print(ascii_image)

    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


main()

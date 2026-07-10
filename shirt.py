import sys
from os import path
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_ext = path.splitext(input_file)[1].lower()
    output_ext = path.splitext(output_file)[1].lower()

    valid_extensions = [".jpg", ".jpeg", ".png"]

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    # Crop/resize the photo to match the shirt template's size,
    # centering the crop (fills the frame without stretching)
    fitted = ImageOps.fit(image, shirt.size)

    # Paste the shirt design on top, using its own transparency as a mask
    fitted.paste(shirt, shirt)

    fitted.save(output_file)


if __name__ == "__main__":
    main()
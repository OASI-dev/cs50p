from PIL import Image, ImageDraw, ImageFont


def main():
    name = input("Name: ")

    image = Image.open("shirtificate.png").convert("RGB")
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 48)
    text = f"{name} took CS50"

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    image_width, image_height = image.size
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2

    draw.text((x, y), text, font=font, fill="white")

    image.save("shirtificate.pdf")


if __name__ == "__main__":
    main()
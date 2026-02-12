from PIL import Image
def main():
    image_path=input("Enter valid image path:")

    try:
        image=Image.open(image_path)
    except:
        print(f"{image_path} is not a valid path!")
        return 0
    print(image.size)
    image_width=image.width
    image_height=image.height
    new_width=100
    new_height=((image_height/image_width)*new_width)*0.5
    resized_image=image.resize((new_width,int(new_height)))
    print(resized_image.size)
    grayscale_image=resized_image.convert("L")
    print(grayscale_image)
    ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']
    ascii_image = ""
    for y in range(int(new_height)):
        row = "" 
        for x in range(new_width):
            pixel_value = grayscale_image.getpixel((x, y))
            index = pixel_value * (len(ASCII_CHARS) - 1) / 255
            index=int(index)
            char = ASCII_CHARS[index]
            row += char

        ascii_image += row + "\n"
    print(ascii_image)
main()
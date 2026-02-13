from PIL import Image

#Resizing image into required dimensions.
def resize(image):
    image_width=image.width
    image_height=image.height
    new_width=100
    new_height=((image_height/image_width)*new_width)*0.5
    new_height=int(new_height)
    resized_image=image.resize((new_width,new_height))
    return resized_image
    
# Converting the resized image into grayscale.
def grayscale(image):
    grayscale_image=image.convert("L")
    return grayscale_image

# Main program responsible for loading image through image path and mainly doing ASCII operations.
def main():
    image_path=input("Enter valid image path:")

    try:
        image=Image.open(image_path)
    except:
        print(f"{image_path} is not a valid path!")
        return 0
    
    #Resizing and grayscaling the image
    resized_image=resize(image)
    grayscale_image=grayscale(resized_image)

    #Defining the ASCII characters
    ASCII_CHARS = ['.',',','^',':',';','+','*','?','%','$','#','@']
    ascii_image = ""

    width, height = grayscale_image.size

    for y in range(height):
        row = "" 
        for x in range(width):
            pixel_value = grayscale_image.getpixel((x, y))
            index = pixel_value * (len(ASCII_CHARS) - 1) / 255
            index=int(index)
            char = ASCII_CHARS[index]
            row += char

        ascii_image += row + "\n"
    print(ascii_image)
main()
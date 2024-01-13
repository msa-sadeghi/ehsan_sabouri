from PIL import Image

imagePath = 'assets/exit_btn.png'
newImagePath = 'assets/exit_btn2.png'

image = Image.open(imagePath).convert("RGB")

# print(list(im.getdata()))


def change_color (image):
    new_image_data = []
    orange_color = (230,97,29)
    red_color = (255,0,0)
    for color in image.getdata():
        if color == orange_color:
            new_image_data.append( red_color )
        elif color in [(82,48,6), (85,48,6)]:
            new_image_data.append((0,255,0))
        else:
            new_image_data.append( color )
    new_image = Image.new(image.mode,image.size)
    new_image.putdata(new_image_data)
    return new_image

change_color(image).save(newImagePath)
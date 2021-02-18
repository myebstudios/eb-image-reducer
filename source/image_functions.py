from PIL import Image

def resize_image(source, percentage, show=True):
    im = Image.open(source)
    new_height = int((im.height/100)*percentage)
    new_width = int(new_height / im.height * im.width)
    new_image = im.resize((new_width, new_height))
    
    if show == True:
        new_image.show()
    else:
        print("saved Image at .....")
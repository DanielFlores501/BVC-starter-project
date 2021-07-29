import random
import glob
from PIL import Image, ImageDraw, ImageFilter

# Open dataset of images, apply wheelchair symbol to all images (locations? translations?), save new images in destination

def main():
    paste_symbol_location = '..\wheelchair_symbol2.png' #symbol to apply to images
    image_location = '..\stanford-background-dataset\images' #images to use as backgrounds #715 
    new_image_destination = '..\stanford-background-dataset\marked_images' #location for images with pasted symbol
    labels_destination = '..\stanford-background-dataset\marked_images_labels.txt' #location to save labels of images  
    labels_string = ''
    symbol = Image.open(paste_symbol_location)
    
    symbol = symbol.resize((20, 22)).convert("RGBA")
    #Consider resizing image randomly as well???????????????

    symbol_width, symbol_height = symbol.size

    one_count = 0
    zero_count = 0

    for f in glob.iglob(image_location + '\*.jpg'):
        im = Image.open(f)
        im_copy = im.copy() #make copy to paste image to
        w, h = im_copy.size
        im_copy = im_copy.crop((0, 0, 200, 200))

        #randomly determine if this one should get a sign added
        if(random.randint(0,99) > 50):
            labels_string+= '0' #0, no sign
            im_copy.save(new_image_destination + '\\' + im.filename[-11:], quality=95)
            zero_count+=1
            continue
        else:
            labels_string+= '1' #1, add sign! 
            one_count+=1
            #get unique x and y location for image paste
            width, height = im_copy.size
            
            random_width = random.randint(0, width - symbol_width - 1)
            random_height = random.randint(0, height - symbol_height - 1)

            im_copy.paste(symbol, (random_width, random_height), symbol)
            im_copy.save(new_image_destination + '\\' + im.filename[-11:], quality=95)
    print("labels_string ", labels_string)
    print("zero_count: ", zero_count, " one_count: ", one_count)
    with open(labels_destination, 'w') as labels_file:
        labels_file.write(labels_string)
    
if __name__ == '__main__':
    main()

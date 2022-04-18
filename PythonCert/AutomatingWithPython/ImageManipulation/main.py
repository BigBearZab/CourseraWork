import re

def transform_image(original_image):
    from PIL import Image as im
    og_im = im.open('/home/student-02-f2f2f0d89f65/images/'+original_image)
    new_im = og_im.resize((128,128)).rotate(90).convert('RGB')
    new_im.save('/opt/icons/'+ original_image, 'JPEG')


def get_list_of_images(original_images_path):
    import os
    return [f for f in os.listdir(original_images_path) if re.match(r'ic_\w+',f)]

path = './images/'

def main():
    for image in get_list_of_images(path):
        transform_image(image)

if __name__ == "__main__":
    main()

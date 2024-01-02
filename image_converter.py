from PIL import Image
import fire

image_format_to_extension={
    'jpeg' : 'jpeg',
    'png' : 'png',
    'jpeg2000' : 'jp2',
    'gif' : 'GIF',
    'bmp' : 'BMP',
}

def convert_image_to_grayscale(filepath, image_format):
    try:
        jpeg_image = Image.open(open(filepath,'rb')).convert('L')
        new_filename = f'{filepath}_new.{image_format_to_extension[image_format.lower()]}'
        jpeg_image.save(new_filename, image_format)
        print(f'Succesfully converted image to grayscale {image_format}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    fire.Fire(convert_image_to_grayscale)

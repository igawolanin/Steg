ETX = 3

def string_to_bin(text):
    bin_text = ''.join(format(ord(x), '08b') for x in text)
    return bin_text

def int_to_bin(number):
    bin_number = format(number, '08b')
    return bin_number

def bin_to_int(bin_number):
    return int(bin_number, 2)

def change_last_bit(number, last_bit):
    return (number & ~1) | int(last_bit)

def new_path(path):
    path_list = path.rsplit('.', 1)
    return f"{path_list[0]}_steg.png"

def msg_fits_in_img(msg_bin, width, height):
    # maximum message size in bits (3 bits in each pixel)
    if len(msg_bin) > width * height * 3:
        print(f"message too long, max length is {width*height*3 // 8 -1}")
        return False
    else:
        return True

def prepare_image(image):
    if image.mode != 'RGB':
        return image.convert(mode='RGB')
    return image

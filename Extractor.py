from PIL import Image
import utils

class Extractor:
    """
   Extract hidden messages from an image using LSB steganography.

   The message is reconstructed by reading the least significant bits of each
   RGB channel in sequence and converting them back to ASCII characters.
   Extraction stops when the ETX (ASCII=3) marker is encountered.
   """
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def extract(self):
        with Image.open(self.path_to_file) as image:
            image = utils.prepare_image(image)
            width, height = image.size

            decoded_msg = ''
            buffer = ''
            pixels = image.load()

            for y in range(height):
                for x in range(width):
                    rgb = pixels[x, y]
                    for pixel in rgb:
                        buffer += str(pixel & 1)
                        if len(buffer) == 8:
                            decoded = utils.bin_to_int(buffer)
                            if decoded == utils.ETX: #eof
                                return decoded_msg
                            else:
                                decoded_msg += chr(decoded)
                                buffer = ''

            return decoded_msg
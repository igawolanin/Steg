from PIL import Image
import utils

class Embedder:
    """
    Embed a secret message into an image using LSB steganography.

    The message is converted into binary and embedded into the least significant bits
    of the image's RGB pixel values. An ETX (ASCII=3) marker is appended to signal
    the end of the message during extraction.
    """
    def __init__(self, secret_message, path_to_file):
        self.secret_message = secret_message
        self.path_to_file = path_to_file

    def _prepare_message(self):
        msg_bin = utils.string_to_bin(self.secret_message)  # message in binary
        msg_bin += utils.int_to_bin(utils.ETX)  # adding trailing ASCII End of Text to imply end of message
        return msg_bin

    def embed(self):
        with Image.open(self.path_to_file) as image:
            image = utils.prepare_image(image)

            width, height = image.size

            msg_bin = self._prepare_message()

            if not utils.msg_fits_in_img(msg_bin, width, height) :
                return

            pixels = image.load()

            bit_index = 0
            for y in range(height):
                for x in range(width):
                    if bit_index >= len(msg_bin):
                        break

                    rgb = list(pixels[x, y])
                    for idx in range(3):
                        if bit_index < len(msg_bin):
                            rgb[idx] = utils.change_last_bit(rgb[idx], msg_bin[bit_index])
                            bit_index += 1
                    pixels[x,y] = tuple(rgb)

                if bit_index >=len(msg_bin):
                    break

            image.save(utils.new_path(self.path_to_file))
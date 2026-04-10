# LSB Steganography Tool

### Overview

This project implements a simple command-line tool for hiding and extracting messages in images using **LSB (Least Significant Bit) steganography**.
The main goal of the project is to provide a **minimal, transparent, and easy-to-understand CLI tool** for steganography, without unnecessary complexity. It focuses on clarity of implementation and correctness of the underlying algorithm.
---

### How It Works

The message is converted into a binary representation and embedded into the least significant bits of RGB pixel channels.

To mark the end of the hidden message, a special **EOT (End of Text, ASCII = 3)** character is appended during embedding.

This allows the extractor to:
- know when the message ends  
- avoid decoding unnecessary image data
- 
After embedding, the modified image is saved automatically as a new file with the same name and the `_steg.png` suffix. The tool operates exclusively on PNG images, as the method relies on **lossless compression**. Formats such as JPEG use lossy compression, which alters pixel values and would corrupt the embedded data.

### Project Structure

- `main.py`: CLI entry point.
- `Embedder.py`: Embedding logic.
- `Extractor.py`: Extraction logic.
- `utils.py`: Helper functions.

### Usage

Steganography with LSB [-h] {embed,extract} …
- embed – hides a message inside an image
- extract – retrieves a hidden message from an image


#### Embed Mode

To embed a message, provide the input image and either a direct message or a file containing the message:

python main.py embed <image_path> -m “your secret message”

or

python main.py embed <image_path> -f <message_file>

#### Extract Mode

To extract a hidden message from an image:

python main.py extract <image_path>

### Future Improvements

The project is intended to be further developed in several directions.
First, support for **UTF-8 and arbitrary byte encoding** will be introduced, allowing the tool to handle a wider range of characters beyond the current ASCII limitation.
Second, the extraction process will be extended to optionally **read the entire embedded bitstream beyond the EOT marker**, enabling deeper analysis and more flexible decoding strategies.
Additionally, the tool may be enhanced with **optional encryption mechanisms**, allowing messages to be secured before embedding.

### License

This project is released under the GNU GPL v3 license. More information can be found in the `LICENSE.txt` file.

### Contact

If you have any questions or feedback, feel free to reach out via GitHub or email: igatwolanin@gmail.com.
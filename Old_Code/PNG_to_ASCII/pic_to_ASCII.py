import ascii_magic  # pip install ascii_magic

input_path = 'C:/Users/vojte/Desktop/PNG_to_ASCII/input.png'
output_path = 'C:/Users/vojte/Desktop/PNG_to_ASCII/output.txt'

ASCII_image = ascii_magic.from_image_file(input_path)
ascii_magic.to_terminal(ASCII_image)
ascii_magic.to_file(output_path, ASCII_image)

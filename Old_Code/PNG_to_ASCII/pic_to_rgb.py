import numpy as np
from PIL import Image

image = Image.open(r'C:/Users/Student/Documents/PNG_to_ASCII/input.png').convert('RGB')
image = np.asarray(image)
image2 = image.reshape(image.shape[0], -1)
np.set_printoptions(suppress=True, precision= 1)
image3 = np.array(image2)
np.savetxt('C:/Users/Student/Documents/PNG_to_ASCII/output3.txt', image3, delimiter=', ', newline= '\n')
#print(image)
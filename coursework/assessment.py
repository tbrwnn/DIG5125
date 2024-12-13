# fundamental image processing task 
import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sci
from tkinter import filedialog


def conovolution(img_dir, effect=None):

    # reads image
    image = cv2.imread(img_dir, cv2.IMREAD_COLOR)

    # checks for effects
    if effect == '1':
        image_output = cv2.GaussianBlur(image, (55, 55),9) #Blur function taken from cv
    elif effect == '2':
        image_output = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Converts image to gray scale
    elif effect == '3':
        kernel = np.ones((dimsx,dimsy),np.float32)/(dimsx*dimsy)
        image_output = cv2.filter2D(image,-1,kernel)
    else:
        image_output = image


    # Normal image, procsessed image
    image_listing = [image, image_output]
    titles = ['Input', 'Output']


    # Simple for loop to place 2 plots with input and output 
    for i, (image, title) in enumerate(zip(image_listing, titles), 1):
        plt.subplot(1,2,i) # Max 2
        if i == 1:
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        else:
            if effect == '2':
                plt.imshow(image_output, cmap='gray')
            else:
                plt.imshow(cv2.cvtColor(image_output, cv2.COLOR_BGR2RGB))


        plt.title(title)
        plt.axis('off')

    plt.tight_layout()
    plt.show()



# Ask for User Input
print('Image editing - 1: Blur, 2: Grayscale, 3: motion blur ')
user = input('Enter one of the numbers: ')

effect = None

if user == '1':
    effect = user
    print('Blur selected')
elif user == '2':
    effect = user
    print('Gray Scale Selected')
elif user == '3':
    effect = user
    print('Motion blur selected')
    
    dimsx = int(input('select motion dimentions y direction '))
    dimsy =int( input('select motion dimentions x direction '))
else:
    print('invalid')
    user = input('Enter one of the numbers: ')
img_dir = filedialog.askopenfilename()
conovolution(img_dir, effect)
# fundamental image processing task 
import cv2
import matplotlib.pyplot as plt
import numpy as np

def conovolution(img_dir, effect=None):

    # reads image
    image = cv2.imread(img_dir, cv2.IMREAD_COLOR)

    # checks for effects
    if effect == '1':
        image_output = cv2.GaussianBlur(image, (5, 5), 0) # Blur function taken from cv
    elif effect == '2':
        image_output = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Converts image to gray scale
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
print('Image editing - 1: Blur, 2: Grayscale')
user = input('Enter one of the numbers: ')

effect = None

if user == '1':
    effect = user
    print('Blur selected')
elif user == '2':
    effect = user
    print('Gray Scale Selected')
else:
    print('invalid')
    user = input('Enter one of the numbers: ')

conovolution('coursework/R.jpg', effect)
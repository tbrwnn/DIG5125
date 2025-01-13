import cv2
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog


def conovolution(img_dir, effect=None, dimsx=None, dimsy=None):
    # Read image
    image = cv2.imread(img_dir, cv2.IMREAD_COLOR)

    # Apply selected effect
    if effect == '1':
        image_output = cv2.GaussianBlur(image, (55, 55), 9)  # Gaussian blur
    elif effect == '2':
        image_output = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    elif effect == '3':
        kernel = np.ones((dimsx, dimsy), np.float32) / (dimsx * dimsy)
        image_output = cv2.filter2D(image, -1, kernel)  # Motion blur
    else:
        image_output = image  # No effect

    # Display images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    if effect == '2':
        plt.imshow(image_output, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image_output, cv2.COLOR_BGR2RGB))
    plt.title('processed')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


# Ask for User Input
print('Image editing - 1: Blur, 2: Grayscale, 3: Motion blur')
user_input = input('Enter one of the numbers: ')

effect = None
dimsx = None
dimsy = None

if user_input == '1':
    effect = user_input
    print('Blur selected')
elif user_input == '2':
    effect = user_input
    print('Grayscale selected')
elif user_input == '3':
    effect = user_input
    print('Motion blur selected')
    dimsx = int(input('Enter motion dimensions in y direction: '))
    dimsy = int(input('Enter motion dimensions in x direction: '))
else:
    print('Invalid input. Please enter one of the numbers: 1, 2, or 3')
    exit()

# Ask for image file
img_dir = 'coursework/R.jpg'

# Perform image processing and display results
conovolution(img_dir, effect, dimsx, dimsy)
 
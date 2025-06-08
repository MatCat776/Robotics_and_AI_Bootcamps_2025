# Open-CV with Python

## Installs 
opencv-python is usually the package name
For anaconda check out [this guide](https://sushant4191.medium.com/installing-opencv-on-windows-through-anaconda-how-to-fix-solving-environment-error-message-6760a1b07ba5) (I think often you use the conda-forge package)

## What is OpenCV? 

[OpenCV](https://opencv.org/) is the Open Computer Vision Library. It is a very popular library for a large variety of computer vision tasks and image processing. 

It is available in both Python and C++. We tend to use the Python version. [The Python Documentation is linked here](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html).  


## Basic Program 
First, we want to make sure that if you are planning to use a webcam, you can access it. If you don't have a webcam, or are planning to use Google Colab, we also want to make sure you are able to visualize the image. For most of the workshop, you should be able to pick whether you want to apply the operations on a static image, or a real-time feed. 

Code:

    import cv2 
    from matplotlib import pyplot as plt 

    #Test Webcam
    #Set up your webcam 
    webcam = cv2.VideoCapture(0)
    #Randomly init a 'key press'
    key = ord('r')
    #While the 's' key isn't pressed
    while key != ord("s"):
        #Get picture and success of operation
        success, still = webcam.read()
        cv2.imshow("Webcam Feed", still)
        #Sets frame rate
        key = cv2.waitKey(10)
    cv2.destroyAllWindows()

    #Test Matplotlib image visualization - create a function 
    def show_img(img_to_show):
        plt.imshow(cv2.cvtColor(img_to_show, cv2.COLOR_BGR2RGB))
        plt.show()
        plt.clf()

    #Read in an image
    img = cv2.imread('images/jellyfish.jpg')
    show_img(img)

Running this should pop up a webcam window with a live feed, and then a image window for matplotlib.

## Image Structure - basic_images.py
Code walkthrough 

## Processing Images - more_advanced_operations.py
Code walkthrough 


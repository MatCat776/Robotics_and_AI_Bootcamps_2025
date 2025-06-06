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
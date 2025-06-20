import cv2 
from matplotlib import pyplot as plt 

def run_program():
    #Set up your webcam 
    webcam = cv2.VideoCapture(0)
    #Randomly init a 'key press'
    key = ord('r')
    #While the 's' key isn't pressed
    while key != ord("s"):
        #Get picture and success of operation
        success, still = webcam.read()
        still = do_something(still)
        cv2.imshow("Webcam Feed", still)
        #Sets frame rate
        key = cv2.waitKey(10)
    cv2.destroyAllWindows()



#Test Matplotlib image visualization - create a function 
def show_img(img_to_show):
    plt.imshow(cv2.cvtColor(img_to_show, cv2.COLOR_BGR2RGB))
    plt.show()
    plt.clf()

def preprocess_img(img):
    #Grayscale
    gray_img = img.copy()
    gray_img = cv2.cvtColor(gray_img, cv2.COLOR_BGR2GRAY)
    #Blur
    blur_img = cv2.GaussianBlur(gray_img, (7,7), 0)
    return blur_img



# #Threshold
# def do_something(img):
#     #Preprocess img
#     img = preprocess_img(img)
#     #white is 255, black is 0
#     ret, thresh_img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
#     return thresh_img

# #Gradient
# def do_something(img):
#     #Preprocess img
#     img = preprocess_img(img)
#     #X direction
#     img = cv2.Sobel(img, -1, 1, 0)
#     #Y Direction 
#     #img = cv2.Sobel(img, -1, 0, 1)
#     return img


# #Edge Detection
# def do_something(img):
#     #Preprocess img
#     img = preprocess_img(img)
#     img = cv2.Canny(img, 50, 200)
#     return img


#Edge Detection and Contours
def do_something(img):
    #Preprocess img
    normal_img = img.copy()
    img = preprocess_img(img)
    img = cv2.Canny(img, 50, 200)
    #Contours
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for single_contour in contours:
        moments = cv2.moments(single_contour)
    og_img = normal_img.copy()
    cv2.drawContours(og_img, contours, -1, (0,0,255), 3)
    return og_img


run_program()
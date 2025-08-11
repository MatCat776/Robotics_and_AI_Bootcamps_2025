import cv2 
from matplotlib import pyplot as plt 
#Test Webcam


def run_program():
    # Set up your webcam
    webcam = cv2.VideoCapture(0)
    # Randomly init a 'key press'
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

def preprocess_img(img):
    gray_img = img.copy()
    gray_img = cv2.cvtColor(gray_img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    return blur_img
# def do_something(img):
#     img= preprocess_img(img)
#     ret, thresh_img = cv2.threshold(img,55,255, cv2.THRESH_BINARY)
#     return thresh_img

def do_something(img):
    img= preprocess_img(img)
    img = cv2.Sobel(img, -1, 1, 0)
    return img

#Test Matplotlib image visualization - create a function 
def show_img(img_to_show):
    plt.imshow(cv2.cvtColor(img_to_show, cv2.COLOR_BGR2RGB))
    plt.show()
    plt.clf()

#Read in an image
img = cv2.imread('images/jellyfish.jpg')
show_img(img)

text = "A photo of me"
origin = (50,100)
font=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
fontScale=1
color=(255,0,0)
thickness=2
line_type=cv2.LINE_4
new_img=still.copy()
new_img=cv2.putText(new_img,text,origin,font,fontScale,color,thickness,line_type)

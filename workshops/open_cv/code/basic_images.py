import cv2 
from matplotlib import pyplot as plt 

#Test Matplotlib image visualization - create a function 
def show_img(img_to_show):
    plt.imshow(cv2.cvtColor(img_to_show, cv2.COLOR_BGR2RGB))
    plt.show()
    plt.clf()

#Read in an image
img = cv2.imread('workshops/open_cv/code/images/jellyfish.jpg')

#Get the blue intensity of pixel 40,40
print(img[40, 40, 0])
#Rows, Columns, Channels
print(img.shape)
#Print datatype
print(img.dtype)

#Write text on an image
text = "A Jellyfish Picture!"
origin = (50, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale=1
color = (0, 255, 0)
thickness = 2
line_type = cv2.LINE_AA
new_img = img.copy()
new_img = cv2.putText(new_img, text, origin, font, fontScale, color, thickness, line_type)
show_img(new_img)

#Grayscale
gray_img = img.copy()
gray_img = cv2.cvtColor(gray_img, cv2.COLOR_BGR2GRAY)
show_img(gray_img)

#ColorMap
mapped_img = gray_img.copy()
mapped_img = cv2.applyColorMap(mapped_img, cv2.COLORMAP_TWILIGHT)
show_img(mapped_img)

#Blur
blur_img = gray_img.copy()
blur_img = cv2.GaussianBlur(blur_img, (7,7), 0)
show_img(blur_img)
plt.clf()


#Image Lumosity Histogram
histogram = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
plt.figure()
plt.title("Lumosity Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels in each bin")
plt.plot(histogram)
plt.xlim([0, 256])
plt.show()
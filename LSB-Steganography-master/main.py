from LSBSteg import *
message = input("Enter your message: ")
steg = LSBSteg(cv2.imread("up.jpg"))
img_encoded = steg.encode_text(message)
cv2.imwrite("my_new_image.png", img_encoded)
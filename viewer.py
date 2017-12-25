import cv2

def view(img,title='default'):
    cv2.imshow(title, img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
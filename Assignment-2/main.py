# Importing Libraries
import cv2
import numpy as np


if __name__ == "__main__":

    person_img = cv2.imread('Images/my_image.jpeg')

    # Resizing the Person image
    scale = 0.2
    width = int(person_img.shape[1]*scale)
    height = int(person_img.shape[0]*scale)
    dsize = (width, height)
    person_img = cv2.resize(person_img, dsize)

    # Selecting the Region of Interest of the image
    copy_of_person = person_img.copy()
    mask = np.zeros(person_img.shape[:2], np.uint8)

    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    x, y, w, h = cv2.selectROI("Select the Region of Interest", person_img)
    start = (x, y)
    end = (x+w, y+h)
    rect = (x, y, w, h)

    cv2.rectangle(copy_of_person, start, end, (0, 0, 255), 3)

    # Implementing GrabCut Algorithm for removing background

    cv2.grabCut(person_img, mask, rect, bgd_model, fgd_model, 100, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    no_bg_person = person_img * mask2[:, :, np.newaxis]
    cv2.imshow("Foreground Image", no_bg_person)
    cv2.imwrite('Images/my_image_no_bg.jpeg', no_bg_person)

    # Adding new Background
    background_img = cv2.imread('Images/Taj-Mahal.jpg')
    background_img = cv2.resize(background_img, dsize)
    background_img[mask2 != 0] = [0, 0, 0]

    final_img = no_bg_person + background_img
    cv2.imshow("Final Image", final_img)
    cv2.imwrite('Images/final_image.jpeg', final_img)

    # cv2.imshow("Background", background_img)

    # Displaying the results
    # cv2.imshow('My Image Original', resized_person_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

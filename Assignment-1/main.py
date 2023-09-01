import cv2
import numpy as np

def Marr_Hilderth(img):
    img_2 = cv2.Laplacian(img, cv2.CV_64F)
    edge_image = np.zeros((img_2.shape[0], img_2.shape[1]), dtype=np.uint8)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            if (img_2[i, j] == 0 and
                    ((img_2[i - 1, j] * img_2[i + 1, j] < 0) or
                     (img_2[i, j - 1] * img_2[i, j + 1] < 0) or
                     (img_2[i - 1, j - 1] * img_2[i + 1, j + 1] < 0) or
                     (img_2[i - 1, j + 1] * img_2[i + 1, j - 1] < 0))):
                edge_image[i, j] = 255
    return edge_image



if __name__ == "__main__":
    # Capture and Load the Face Image (f)
    f = cv2.imread('WhatsApp Image 2023-09-01 at 6.16.04 AM.jpeg')
    f = cv2.resize(f, (600, 900))
    # Covert to Grayscale Image
    gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Filter
    blurred_f = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny Algorithm
    canny_edge = cv2.Canny(blurred_f, 50, 150)

    # Apply Marr-Hildreth Edge Detection
    marr_hilderth_edge = Marr_Hilderth(blurred_f)

    # Sharpen the Image Using Edge Images
    c_canny = 30
    c_marr_hildreth = 10

    sharpened_canny = blurred_f + c_canny * canny_edge
    sharpened_marr_hilderth = blurred_f + c_marr_hildreth * marr_hilderth_edge

    # Display the Result
    cv2.imshow('Original Image', gray)
    cv2.imshow('Canny Edge', canny_edge)
    cv2.imshow('Marr Hilderth Edge', marr_hilderth_edge)
    cv2.imshow('Sharpened (Canny Edge)', sharpened_canny)
    cv2.imshow('Sharpened (Marr-Hildreth Edge)', sharpened_marr_hilderth)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# import cv2
# import numpy as np
#
# def Marr_Hilderth(img, sigma):
#     # Apply Gaussian blur to the input image
#     img_blurred = cv2.GaussianBlur(img, (5, 5), sigma)
#
#     # Apply Laplacian operator to the blurred image
#     laplacian = cv2.Laplacian(img_blurred, cv2.CV_64F)
#
#     # Calculate the absolute value of the Laplacian
#     laplacian_abs = np.abs(laplacian)
#
#     # Normalize the Laplacian result to 0-255
#     laplacian_normalized = cv2.normalize(laplacian_abs, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
#
#     # Create an empty edge image
#     edge_image = np.zeros_like(img, dtype=np.uint8)
#
#     # Define a threshold value to detect edges
#     threshold_value = 50  # You can adjust this threshold as needed
#
#     # Iterate through the image to detect edges based on the threshold
#     for i in range(img.shape[0]):
#         for j in range(img.shape[1]):
#             if laplacian_normalized[i, j] > threshold_value:
#                 edge_image[i, j] = 255  # Set edge pixel to white (255)
#
#     return edge_image
#
# if __name__ == "__main__":
#     # Load the input image
#     f = cv2.imread('WhatsApp Image 2023-09-01 at 6.16.04 AM.jpeg', cv2.IMREAD_GRAYSCALE)
#
#     # Apply Marr-Hildreth edge detection
#     sigma = 1
#     marr_hilderth_edge = Marr_Hilderth(f, sigma)
#
#     # Sharpen the image using the edge image
#     c_marr_hildreth = 10
#     sharpened_marr_hilderth = f + c_marr_hildreth * marr_hilderth_edge
#
#     # Display the results
#     cv2.imshow('Original Image', f)
#     cv2.imshow('Marr-Hildreth Edge', marr_hilderth_edge)
#     cv2.imshow('Sharpened (Marr-Hildreth Edge)', sharpened_marr_hilderth)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

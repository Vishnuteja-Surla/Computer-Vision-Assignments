import cv2

# Step 1: Capture and Load the Face Image (f)
f = cv2.imread('WhatsApp Image 2023-09-01 at 6.16.04 AM.jpeg', cv2.IMREAD_COLOR)

# Step 2: Apply Canny Edge Detection to f
gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
edges_canny = cv2.Canny(gray, 50, 150)  # Adjust threshold values as needed
edges_canny = cv2.cvtColor(edges_canny, cv2.COLOR_GRAY2BGR)  # Convert to 3 channels

# Step 3: Apply Marr-Hildreth Edge Detection to f
sigma = 1.0  # Adjust the Gaussian smoothing sigma as needed
edges_marr_hildreth = cv2.Laplacian(cv2.GaussianBlur(gray, (0, 0), sigma), cv2.CV_64F)
edges_marr_hildreth = cv2.convertScaleAbs(edges_marr_hildreth)
edges_marr_hildreth = cv2.cvtColor(edges_marr_hildreth, cv2.COLOR_GRAY2BGR)  # Convert to 3 channels

# Step 4: Sharpen the Image Using Edge Images
c_canny = 0.25
c_marr_hildreth = 2.0

sharpened_canny = cv2.addWeighted(f, 1, edges_canny, c_canny, 0)
sharpened_marr_hildreth = cv2.addWeighted(f, 1, edges_marr_hildreth, c_marr_hildreth, 0)

# Step 5: Display the Results
cv2.imshow('Original Image', f)
cv2.imshow('Sharpened (Canny Edge)', sharpened_canny)
cv2.imshow('Sharpened (Marr-Hildreth Edge)', sharpened_marr_hildreth)

cv2.waitKey(0)
cv2.destroyAllWindows()

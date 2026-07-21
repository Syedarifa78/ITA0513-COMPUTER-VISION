import cv2

# Read the image
image = cv2.imread("input.jpg")

# Enlarge the image (2 times bigger)
bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Shrink the image (half size)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Save the output images
cv2.imwrite("bigger_image.jpg", bigger)
cv2.imwrite("smaller_image.jpg", smaller)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()

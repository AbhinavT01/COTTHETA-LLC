import cv2

def crop_image(img):
    # Read the image
    # img = cv2.imread("./sample data/idcad10.jpg")
    img = cv2.resize(img, (700, 564))  # Resize the image for consistency
    if img.shape[0] > img.shape[1]:
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Adaptive thresholding to get a binary image
    threshold = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Apply morphological operations to enhance contours
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # Increase kernel size for better noise reduction
    threshold = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)

    # Find contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area and aspect ratio
    min_area = img.shape[0] * img.shape[1] * 0.05  # Adjust this threshold as needed for more noise tolerance
    min_aspect_ratio = 0.1  # Adjust this threshold as needed
    max_aspect_ratio = 10.0  # Adjust this threshold as needed
    detected_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_area:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.03 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            if min_aspect_ratio < aspect_ratio < max_aspect_ratio:
                detected_contours.append(contour)

    # Draw rectangle around the detected contour
    if detected_contours:
        contour = max(detected_contours, key=cv2.contourArea)
        # x, y, w, h = cv2.boundingRect(contour)
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Crop the detected area
        crop_img = img[y:y + h, x:x + w]

        # Save cropped image
        # cv2.imwrite("./cropped_image/Crop_Image.jpg", crop_img)

        # Display images
        # cv2.imshow("Selected Area", img)
        # cv2.imshow("Cropped Area", crop_img)
        return crop_img
    else:
        print("No contour found.")

    return img 

    # Wait for key press and close windows
    
# img = cv2.imread('./floridalicense/fl1.jpg')
# img = crop_image(img)
# cv2.imshow("pg",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows

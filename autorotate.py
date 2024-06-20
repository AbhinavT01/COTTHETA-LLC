import cv2
import numpy as np
def auto_rotate(image):
    if image.shape[0]<image.shape[1]:
        return image
    if image.shape[0]==0 or image.shape[1]==0 or image.shape == 0:
        return image
# Read the image
    # image = cv2.imread("./sample data/idcad8.jpg")
    image = cv2.resize(image, (1080, 800))  # Resize the image for consistency

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adaptive thresholding to get a binary image
    threshold = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Apply morphological operations to enhance contours
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    threshold = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)

    # Find contours
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area and aspect ratio
    min_area = image.shape[0] * image.shape[1] * 0.05
    min_aspect_ratio = 0.1
    max_aspect_ratio = 10.0
    min_solidity = 0.5
    detected_contours = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_area:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.03 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            if min_aspect_ratio < aspect_ratio < max_aspect_ratio:
                hull = cv2.convexHull(approx)
                hull_area = cv2.contourArea(hull)
                if hull_area > 0:
                    solidity = float(area) / hull_area
                    if solidity > min_solidity:
                        detected_contours.append(contour)

    # Function to rotate the image and ensure width > height
    def rotate_image_to_horizontal(image, rect):
        angle = rect[2]
        if angle < -45:
            angle += 90
        (height, width) = image.shape[:2]
        center = (width // 2, height // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (width, height))

        # Check if the resulting image is still vertical
        if rotated.shape[0] > rotated.shape[1]:
            rotated = cv2.rotate(rotated, cv2.ROTATE_90_CLOCKWISE)

        return rotated

    # Process detected contours
    if detected_contours:
        largest_contour = max(detected_contours, key=cv2.contourArea)
        rect = cv2.minAreaRect(largest_contour)
        box = cv2.boxPoints(rect)
        box = np.intp(box)
        # cv2.drawContours(image, [box], 0, (0, 0, 255), 2)

        rotated_image = rotate_image_to_horizontal(image, rect)

        # Crop the detected area
        M = cv2.getRotationMatrix2D((rect[0][0], rect[0][1]), rect[2], 1.0)
        rect_points = cv2.transform(np.array([box]), M)[0]
        x, y, w, h = cv2.boundingRect(rect_points)
        crop_img = rotated_image[y:y + h, x:x + w]

        # Save and display the images

        # cv2.imwrite("rotated_image.jpg", rotated_image)
        # cv2.imwrite("Crop_Image.jpg", crop_img)
        # cv2.imshow("Detected Area", image)
        # cv2.imshow("Rotated Image", rotated_image)
        # cv2.imshow("Cropped Area", crop_img)
    else:
        print("No suitable contour found, using the whole frame.")
        # Use the entire frame as bounding rectangle
        (height, width) = image.shape[:2]
        rect = ((width // 2, height // 2), (width, height), 0)
        rotated_image = rotate_image_to_horizontal(image, rect)


        # Save and display the images

        # cv2.imwrite("rotated_image.jpg", rotated_image)
        # cv2.imshow("Rotated Image", rotated_image)

    # Wait for key press and close windows
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return rotated_image
# image =  cv2.imread('./uploads/idcad1.jpg')
# image = cv2.resize(image, (1080, 800))
# image = auto_rotate(image)
# cv2.imshow("t",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
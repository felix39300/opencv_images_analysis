import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("CaptureWindow")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("Image", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC kex pressed => close everything
        print("ESC hit, closing ...")
        break
    elif k % 256 == 32:
        # Space pressed => capture one image
        img_name = "Capture_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

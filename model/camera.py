import cv2

def execute_camera():
    #Instance of the camera
    camera_capture = cv2.VideoCapture(0)

    if not camera_capture.isOpened():
        print('ERROR!: The camera does not work')
        return

    width, height = 640, 780 # Initial resolution
    camera_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    while True:
        ret, frame = camera_capture.read()

        if not ret:
            print('ERROR!: There is an error with the video frame')
            break

        resized_camera = cv2.resize(frame, (width, height))
        
        # Show the camera
        cv2.imshow('MeetMeNow (Camera)', resized_camera)

        # Frame to return
        yield resized_camera

        # Press 'q' to exit the camera
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera_capture.release()
    cv2.destroyAllWindows()

execute_camera()

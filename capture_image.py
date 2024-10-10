import cv2

def capture_image(filename="captured_image.jpg"):
    # Open the default camera (camera index 0)
    camera = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    # Read a frame from the camera
    ret, frame = camera.read()

    # If the frame was read correctly, save the image
    if ret:
        # Save the captured image to the file
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
    else:
        print("Error: Could not capture image.")

    # Release the camera
    camera.release()

    # Close any OpenCV windows if open
    cv2.destroyAllWindows()

# Call the function to capture and save the image
#capture_image()



def detect_and_draw_circle():
    # Load the pre-trained Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open the default camera (index 0)
    camera = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = camera.read()

        if not ret:
            print("Error: Couldn't capture image.")
            break

        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Loop through the detected faces and draw a circle around each
        for (x, y, w, h) in faces:
            # Calculate the center and radius for the circle
            center = (x + w // 2, y + h // 2)
            radius = w // 2
            # Draw the circle on the original colored frame
            cv2.circle(frame, center, radius, (255, 0, 0), 3)  # Blue color, thickness 3

        # Display the resulting frame
        cv2.imshow('Face Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the camera and close windows
    camera.release()
    cv2.destroyAllWindows()

# Call the function
#detect_and_draw_circle()

def capture_and_save_with_face_detection(output_filename="output_image.jpg"):
    # Load the pre-trained Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open the default camera (index 0)
    camera = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a single frame
    ret, frame = camera.read()

    if not ret:
        print("Error: Couldn't capture image.")
        return

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop through the detected faces and draw a blue circle around each
    for (x, y, w, h) in faces:
        # Calculate the center and radius for the circle
        center = (x + w // 2, y + h // 2)
        radius = w // 2
        # Draw the circle on the original colored frame
        cv2.circle(frame, center, radius, (255, 0, 0), 3)  # Blue color, thickness 3

    # Save the resulting image with the circle(s) drawn
    cv2.imwrite(output_filename, frame)
    print(f"Image with detected faces saved as {output_filename}")

    # Release the camera
    camera.release()

    # Close any OpenCV windows if open
    cv2.destroyAllWindows()

# Call the function to capture, detect faces, draw circles, and save the image
capture_and_save_with_face_detection()


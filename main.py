import cv2
import time
from model.camera import execute_camera
from model.genderRecognition import face_analyzer

if __name__ == "__main__":
    try:
        # setting the camera with the resolution
        camera_capture = cv2.VideoCapture(0)
        camera_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        camera_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 780)

        # Intervalue for the analysis and my camera dont break :(
        interval = 5  
        last_time = time.time()  

        # Variables para almacenar los últimos resultados
        last_gender = None
        last_age = None
        last_emotion = None

        # Ejecuta la cámara
        for frame in execute_camera():
            # Redimensiona la imagen para que se ajuste a la pantalla
            resized = cv2.resize(frame, (640, 780))

            # Verifica el tiempo transcurrido
            current_time = time.time()
            if current_time - last_time >= interval:
                # make  the analysis for the face (gender, age, emotion)
                gender, age, emotion = face_analyzer(resized)

                # If the face is detected, update the results
                if gender and age and emotion:

                    last_gender = gender
                    last_age = age
                    last_emotion = emotion

                else:
                    # Default values
                    last_gender = "Unknown"
                    last_age = "Unknown"
                    last_emotion = "Unknown"

                # refresh the last analysis time
                last_time = current_time

            # Show the data in the camera
            cv2.putText(resized, f"gender: {last_gender}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(resized, f"Age: {last_age}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(resized, f"Emotion: {last_emotion}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            cv2.imshow('MeetMeNow (Camera)', resized)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cv2.destroyAllWindows()

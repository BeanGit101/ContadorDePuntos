import cv2
import mediapipe as mp
import time
import threading
import tkinter as tk

Ventana = None
Habilitar = False
Puntuacion_1 = 0
Puntuacion_2 = 0
camera_open = True


def main():
 global camera_open
 Ventana = tk.Tk()
 Ventana.title("Ventana")
 Ventana.geometry("900x650+460+0")
 Ventana.mainloop()
 camera_open = False

def iniciar_main():
 main_thread = threading.Thread(target=main)
 main_thread.start()

iniciar_main()
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap = cv2.VideoCapture(0)
Ultimo_incremento = time.time()

Label_Puntuaje_1 = tk.Label(Ventana, 
    text= 0,
    font = ("arial", 48),
    bg="#800000", fg="#ECCD6A",
    relief="solid",bd=5,
    width= 3, pady=125)
Label_Puntuaje_1.place(x=165, y=130)  

Label_Puntuaje_2 = tk.Label(Ventana, 
    text= 0,
    font = ("arial", 48),
    bg="#800000", fg="#ECCD6A",
    relief="solid",bd=5,
    width= 3, pady=125)
Label_Puntuaje_2.place(x=610, y=130)  

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened() and camera_open == True:
            ret, frame = cap.read()
            if not ret:
                break

           
            # Devueleve el tiempo actual desde 1970
            Momento_Actual = time.time()

            # Convertir la imagen a RGB para mediapipe
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Procesar la imagen para obtener las poses
            results = pose.process(image)

            # Convertir la imagen de nuevo a BGR para OpenCV
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Dibujar las poses en la imagen
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Variables para almacenar coordenadas
            Nariz_x, Nariz_y = None, None
            Muñeca_Derecha_x, Muñeca_Derecha_y = None, None
            Muñeca_Izquierda_x, Muñeca_Izquierda_y = None, None
            Codo_Izquierdo_x, Codo_Izquierdo_y = None, None
            Codo_Derecho_x, Codo_Derecho_y = None, None


            if results.pose_landmarks:
                # Obtener coordenadas de la nariz
                Nariz_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image.shape[1])
                Nariz_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image.shape[0])

                # Obtener coordenadas de las muñecas
                Muñeca_Derecha_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * image.shape[1])
                Muñeca_Derecha_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * image.shape[0])
                Muñeca_Izquierda_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * image.shape[1])
                Muñeca_Izquierda_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * image.shape[0])

                # Obtener coordenadas de los codos
                Codo_Izquierdo_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x * image.shape[1])
                Codo_Izquierdo_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y * image.shape[0])
                Codo_Derecho_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x * image.shape[1])
                Codo_Derecho_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y * image.shape[0])    

                if Muñeca_Derecha_x < Nariz_x and Muñeca_Derecha_y < Nariz_y and Codo_Derecho_y > Nariz_y and Muñeca_Izquierda_y > Nariz_y:        
                 Puntuacion_1 += 1
                 Label_Puntuaje_1["text"] = Puntuacion_1

                if Muñeca_Izquierda_x > Nariz_x and Muñeca_Izquierda_y < Nariz_y and Codo_Izquierdo_y > Nariz_y and Muñeca_Derecha_y > Nariz_y:
                 Puntuacion_2 += 1
                 Label_Puntuaje_2["text"] = Puntuacion_2
                        
    
            # Crear una ventana con un nombre específico
            cv2.namedWindow('Video', cv2.WINDOW_NORMAL)

            # Mover la ventana a una posición específica
            cv2.moveWindow('Video', 0, 0)

            # Cambiar el tamaño de la ventana
            cv2.resizeWindow('Video', 500, 400)

            image = cv2.flip(image,1)

            # Mostrar la imagen procesada
            cv2.imshow('Video', image) 

            # Comprobar si se ha presionado la tecla 'q' para salir
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
# Liberar recursos de captura de video
cap.release()
cv2.destroyAllWindows()
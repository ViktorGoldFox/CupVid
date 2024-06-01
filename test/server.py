# from os import wait
from re import A
import socket 
import threading
from logzero import logger, logfile
import cv2

logfile("logs.log")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

now_connected = []

ip = '127.0.0.1'
port = 228

try:
    server.bind((ip, port))
    server.listen(5)
    logger.info(f"Сервер открыт: {ip}:{port}")
except Exception as error_code:
    logger.error(f"Ошибка в создании сокета: {error_code}")

def playvidio(cap):
    # cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Ошибка: Невозможно открыть видеофайл")
        exit()

    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        cv2.imshow('Video', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    
def applied_users():
    conn, addr = server.accept()
    
    now_connected.append(conn)
    now_connected.append(addr)
    
    data = conn.recv(5000)
    playvidio(data)
    
    logger.info(f"Applied user: {addr}")

applied_users()
# threading_applied = threading.Thread(target=applied_users)
# threading_applied.start()

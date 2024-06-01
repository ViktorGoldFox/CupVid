import cv2

video_path = 'video.mp4'

cap = cv2.VideoCapture(video_path)
print(cap)

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

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()

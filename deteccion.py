import cv2

classes = {0: "pelota", 1: "cancha"}
clasificacion = cv2.CascadeClassifier("./modelos/classifier/cascade.xml")

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    pelota = clasificacion.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=3)

    if ret == False:
        break

    for (x, y, w, h) in pelota:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("imagen", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

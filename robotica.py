from math import pi, sqrt, exp
import cv2
from cv2 import waitKey
from cv2 import minMaxLoc
import numpy as np
import time
cap = cv2.VideoCapture(0)


factorDimension = 100

cap.set(3, 3000)
cap.set(4, 3000)

while (True):

    ret, frame = cap.read()
    image_grande = frame

    if ret == True:
        image_grande = frame
        try:

            width = int(image_grande.shape[1] * factorDimension / 100)
            height = int(image_grande.shape[0] * factorDimension / 100)

            dim = (width, height)

            ancho = width/2
            largo = height/2

            cv2.line(frame, (0, int(largo)),
                     (width, int(largo)), (0, 255, 0), 4)
            cv2.line(frame, (int(ancho), 0),
                     (int(ancho), height), (0, 255, 0), 4)

            image = cv2.resize(image_grande, dim, interpolation=cv2.INTER_AREA)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.GaussianBlur(gray, (25, 25), 0)

            circles = cv2.HoughCircles(
                gray2, cv2.HOUGH_GRADIENT, 1, 150, param1=100, param2=30, minRadius=10, maxRadius=500)
            circles = np.uint16(np.around(circles))

            for i in circles[0, :]:
                cv2.circle(image,  (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 2)

                if (i[0] <= int(((ancho)*0.1)+ancho) and i[0] >= int(((ancho)*-0.1)+ancho)) and (i[1] <= int(((largo)*0.1)+largo) and i[1] >= int(((largo)*-0.1)+largo)):
                    #print("ancho pantalla", ancho)
                    #print("largo pantalla", largo)
                    #print("ancho pelota; ", i[0])
                    #print("largo pelota: ", i[1])
                    print("coincide")

                    cv2.line(image, (0, int(largo)),
                             (width, int(largo)), (255, 255, 0), 4)
                    cv2.line(image, (int(ancho), 0),
                             (int(ancho), height), (255, 255, 0), 4)

                else:
                    print("No coincide")

            circulos = np.uint16(np.around(circles))

            circulos = (sorted(circles[0], key=lambda x: x[2], reverse=True))
            cir = np.array(circulos)

            error = 0
            dato = []
            xi = []
            yi = []
            for i in cir:
                dato.append(i[2])
                xi.append(i[0])
                yi.append(i[1])

            areas = []
            for j in range(len(dato)):
                areas.append(round(dato[j]*2*pi, 2))

            base = [1280, 720]
            margen = []
            for x in range(len(dato)-1):
                margen.append(round((areas[x]-areas[x+1])/2, 2))
                error = ((max(dato)-min(dato))/(sqrt((len(base)*1.1))))

            total = 0
            y = 0
            ar = dato[0]*2*pi
            # print("areas",ar)
            distancia = exp(((-0.0022*ar)+5))
            distancia = round(distancia, 2)
            # print(distancia)

            for x in range(len(dato)):
                cv2.putText(image, str(distancia), (int(xi[x]), int(
                    yi[x])), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)

            cv2.imshow("Houghcircles", image)
            #print("circles", circles)

        except:
            width = int(image_grande.shape[1] * factorDimension / 100)
            height = int(image_grande.shape[0] * factorDimension / 100)

            dim = (width, height)
            frame = cv2.resize(image_grande, dim, interpolation=cv2.INTER_AREA)
            cv2.line(frame, (0, int(height/2)),
                     (width, int(height/2)), (0, 0, 255), 4)
            cv2.line(frame, (int(width/2), 0),
                     (int(width/2), height), (0, 0, 255), 4)

            cv2.imshow("Houghcircles", frame)
            time.sleep(0.05)

    else:
        break

cap.release()
cv2.destroyAllWindows()

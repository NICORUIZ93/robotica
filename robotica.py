from cgitb import grey
from math import pi, sqrt
import cv2
from cv2 import waitKey
from cv2 import minMaxLoc
import numpy as np
import time
import gc
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_EXPOSURE, 1)
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


cap.set(3, 3000)
cap.set(4, 3000)

#print(cap.get(3))
#print(cap.get(4))

while (True):

    ret, frame = cap.read()
    image_grande = frame

    if ret == True:
        image_grande = frame
        try:

            width = int(image_grande.shape[1] * 50 / 100)
            height = int(image_grande.shape[0] * 50 / 100)

            dim = (width, height)

            ancho = width/2
            largo = height/2

            image = cv2.resize(image_grande, dim, interpolation=cv2.INTER_AREA)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.GaussianBlur(gray, (27, 27), 0)

            circles = cv2.HoughCircles(
                gray2, cv2.HOUGH_GRADIENT, 1, 150, param1=100, param2=30, minRadius=10, maxRadius=500)
            circles = np.uint16(np.around(circles))

            for i in circles[0, :]:
                cv2.circle(image,  (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 2)
                #cv2.line(image,ancho,largo,(0,255,0),2)

            circulos = np.uint16(np.around(circles))
            #print("cirulos", circulos)
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

            #base=[691, 650, 615, 525, 440]
            base = [1280, 720]
            margen = []
            for x in range(len(dato)-1):
                margen.append(round((areas[x]-areas[x+1])/2, 2))
                error = ((max(dato)-min(dato))/(sqrt((len(base)*1.1))))
            #print("error: ",error)

            total = 0
            y = 0
            distancia = ((-12*areas[0]+7253)/61)
            distancia = round(distancia, 2)
            #print("areas: ", areas)
            #print("dist: ", distancia)
            for x in range(len(dato)):
                #print("x :", x)
                # if base[0] > areas[x]+error: #and areas[x] > base[0]-error:
                #total += 1000
                cv2.putText(image, str(distancia), (int(xi[x]), int(yi[x])), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
                #cv2.line(image,0,1280,(0,255,0),2)
                #print("esta a: ", distancia)
                # else:
                #   ("no hay monedas")

            #print("Pelota encontrada")
            cv2.imshow("Houghcircles", image)
            cv2.waitKey(1)
            cv2.destroyAllWindows()
            time.sleep(0.05)
     

        except:
            width = int(image_grande.shape[1] * 100 / 100)
            height = int(image_grande.shape[0] * 100 / 100)

            dim = (width, height)

            frame = cv2.resize(image_grande, dim, interpolation=cv2.INTER_AREA)
            cv2.imshow("Houghcircles", frame)
            cv2.waitKey(1)
            cv2.destroyAllWindows()
            #print("no se encontro pelota")
            time.sleep(0.05)
           
        
    else:
        break

cap.release()
cv2.destroyAllWindows()
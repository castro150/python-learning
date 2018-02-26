import cv2
import pandas
from datetime import datetime

# o primeiro frame é guardado, para ser comparado aos outros e ver
# se algo mudou, ou seja, movimento
first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=['Start', 'End'])

# o parametro é um número para os índices das webcams, se tiver mais
# de uma, ou pode ser o nove de um arquivo de vídeo (.mp4 por ex)
# video = cv2.VideoCapture(index=0)
video = cv2.VideoCapture('face.mp4')

while True:

    # check é um boolean que fala se está rodando ou não
    # frame é o frame atual do video
    check, frame = video.read()
    status = 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # removendo ruído e adicionando precisão na diferença
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue # volta pro início do loop

    delta_frame = cv2.absdiff(first_frame, gray)
    # valores maiores que 30 serão considerados brancos (255)
    # retorna uma tupla, o primeiro item não é útil aqui
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # remove os buracos pretos entre os brancos na imagem
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # encontrar os contornos, é boa prática usar cópia do frame
    (_, cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # para cada contorno encontrado:
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            # sai do for se for uma area pequena
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    status_list.append(status)
    status_list = status_list[-2:]
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow('Gray Frame', gray)
    cv2.imshow('Delta Frame', delta_frame)
    cv2.imshow('Threshold Frame', thresh_frame)
    cv2.imshow('Color Frame', frame)

    key = cv2.waitKey(1)
    # sai do loop se apertar Q
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

for i in range(0, len(times), 2):
    df = df.append({'Start': times[i], 'End': times[i + 1]}, ignore_index=True)
df.to_csv('times.csv')

# libera a camera
video.release()
cv2.destroyAllWindows()

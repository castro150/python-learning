import cv2
import skvideo.io as skv

# o parametro é um número para os índices das webcams, se tiver mais
# de uma, ou pode ser o nove de um arquivo de vídeo (.mp4 por ex)
# video = cv2.VideoCapture(index=0)
teste = skv.vread('face.mp4')
cv2.VideoCapture(filename='face.mp4').open()
video = cv2.VideoCapture('face.mp4')

frames_qnt = 0
while True:
    frames_qnt = frames_qnt + 1

    # check é um boolean que fala se está rodando ou não
    # frame é o frame atual do video
    check, frame = video.read()

    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capturing', gray)

    key = cv2.waitKey(1)
    # sai do loop se apertar Q
    if key == ord('q'):
        break

print(frames_qnt)
# libera a camera
video.release()
cv2.destroyAllWindows()

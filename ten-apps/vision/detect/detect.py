import cv2

# os arquivos haarcascade das diferentes perspectivas podem se achados
# no git do opencv
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('photo.jpg')
img = cv2.imread('news.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# scaleFactor é o tanto que a imagem vai ser diminuida na próxima iteração
# em busca de uma nova face; quanto menor, mais o algoritmo demora, mas é mais preciso
#faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

# cada face encontrada vai ter estes parâmetros
for x, y, width, height in faces:
    # as 2 primeiras tuplas sao os cantos superior esquerdo e inferior
    # direito do retangulo que será desenhado
    # depois vem a cor do retangulo e a largura da borda
    # a imagem original é redefinida como sendo a com o novo desenho
    img = cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 3)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[1]/2)))

print(faces)
cv2.imshow('Faces', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

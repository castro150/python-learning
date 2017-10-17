import glob
import cv2

file_names = glob.glob('*.jpg')
for file_name in file_names:
    img = cv2.imread(file_name, 1)
    resized = cv2.resize(img, (100, 100))
    new_name = file_name.split('.')[0] + '-resized.jpg'
    cv2.imwrite(new_name, resized)

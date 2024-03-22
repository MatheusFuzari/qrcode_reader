import cv2
from pyzbar.pyzbar import decode
import json
import locale
import time
from datetime import datetime

locale.setlocale(locale.LC_ALL, "pt_BR")
today = datetime.now().strftime('%a')


camera_id = 1
delay = 1
window_name = 'OpenCV pyzbar'

alunos = {
    "Julia Meneses":["seg","ter","qua","qui","sex"],
    "Roberto Carlos":["seg","sex"]
}
print(alunos)
cap = cv2.VideoCapture(camera_id)
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 600)
img = cv2.imread('gatinho.jpeg')
img_heigth, img_width, _ = img.shape

print(img_heigth, img_width)
print('/n caralho /n')
print(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
x = 50
y = 50
while True:
    ret, frame = cap.read()
    if ret:
        for d in decode(frame):
                s = d.data.decode()
                json_data = json.loads(s)
                nome_aluno = json_data['nome']
                dias_almoco = json_data['comida']
                almoco = f'{nome_aluno} Nao liberado'
                if nome_aluno in alunos.keys() and today in dias_almoco and dias_almoco in alunos.values():
                    print(f"{nome_aluno} PODE ALMOÇAR")
                    almoco = f'{nome_aluno} Liberado'
                else:
                    print(f"{nome_aluno} NÃO PODE ALMOÇAR")
                    almoco = f'{nome_aluno} Nao liberado'
                frame = cv2.rectangle(frame, (d.rect.left, d.rect.top),
                                      (d.rect.left + d.rect.width, d.rect.top + d.rect.height), (0, 255, 0), 3)
                frame = cv2.putText(frame, almoco, (d.rect.left, d.rect.top + d.rect.height),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        frame[ y:y+img_heigth, x:x+img_width] = img
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)

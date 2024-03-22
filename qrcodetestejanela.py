import cv2
from pyzbar.pyzbar import decode
import json
import locale
import time
from datetime import datetime
import tkinter as ttk

locale.setlocale(locale.LC_ALL, "pt_BR")
today = datetime.now().strftime('%a')

camera_id = 1
delay = 1
window_name = 'OpenCV pyzbar'

alunos = {
    "Julia Meneses": ["seg", "ter", "qua", "qui", "sex"],
    "Roberto Carlos": ["seg", "sex"]
}


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
root = ttk.Tk()
root.title("Informações do Aluno")
root.geometry("400x100")

label = ttk.Label(root, text="", font=("Arial", 16))
label.pack()

def update_label(text):
    label.config(text=text)

while True:
    ret, frame = cap.read()
    if ret:
        for d in decode(frame):
            try:
                s = d.data.decode()
                json_data = json.loads(s)
                nome_aluno = json_data['nome']
                dias_almoco = json_data['comida']
                almoco = f'{nome_aluno} Nao liberado'
                if nome_aluno in alunos.keys() and today in dias_almoco and dias_almoco in alunos.values():
                    print(f"{nome_aluno} PODE ALMOÇAR")
                    almoco = f'{nome_aluno} Liberado'
                    frame[ y:y+img_heigth, x:x+img_width] = img
                    
                else:
                    print(f"{nome_aluno} NÃO PODE ALMOÇAR")
                    almoco = f'{nome_aluno} Nao liberado'
                
                update_label(almoco)
            except Exception as e:
                pass
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
root.mainloop()

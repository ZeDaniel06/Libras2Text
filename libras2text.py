import cv2

from ultralytics import YOLO

# Carrega o modelo YOLO
model = YOLO("./best.pt")

cap = cv2.VideoCapture(0)

quadro_consecutivo=0
letra=''
modoUso = 'manual' #pode ser manual ou auto

texto=''
letras=['A','B','C','D','E','F','G','I','L','M','N','O','P','Q','R','S','T','U','V','W','Y']
print('Modo manual ativado: Faça um gesto e pressione Enter para memorizar a letra representada.\nAperte A no teclado se quiser mudar para o modo Automático, que consiste em escrever automaticamente a letra que for realizada por alguns segundos na câmera.\n')
# Loop pelos frames do vídeo
while cap.isOpened():
    # Lê um frame de um vídeo
    success, frame = cap.read()

    if success:
        # Faz inferência YOLO sobre o frame
        results = model(frame,verbose=False,conf=0.1)

        # Visualize os resultados no frame
        annotated_frame = results[0].plot()

        # Exiba o frame anotado
        cv2.imshow("YOLO Inference", annotated_frame)

        botao=cv2.waitKey(1) & 0xFF
        if modoUso == 'auto':
            if len(results[0].boxes.cls)>0:
                if letras[int(results[0].boxes.cls[0].item())] == letra:
                    quadro_consecutivo+=1
                else:
                    quadro_consecutivo=1
                    letra = letras[int(results[0].boxes.cls[0].item())]
                
                if quadro_consecutivo==80:
                    quadro_consecutivo=0
                    texto += letra
                    print(texto)

        if modoUso == 'manual':
            if botao == 13:
                if len(results[0].boxes.cls)>0:
                    texto+=letras[int(results[0].boxes.cls[0].item())]
                    print(texto)

        if botao == 8:
            texto=texto[0:len(texto)-1:1]
            print(texto)
        
        if botao==ord("l"):
            texto=''

        if botao==ord(' '):
            texto += ' '

        if botao == ord('a'):
            print('Modo de uso alterado para automático. Aperte M no teclado se quiser voltar ao modo manual')
            modoUso = 'auto'
        if botao == ord('m'):
            print('Modo de uso alterado para manual. Aperte A no teclado se quiser usar o modo automático')
            modoUso = 'manual'

        # Quebra o loop se 'q' for pressionado
        if botao == ord("q"):
            break

    else:
        # Quebra o loop se o vídeo chegar ao fim
        break

# Libera a janela de captura de vídeo

cap.release()
cv2.destroyAllWindows()
print(texto)
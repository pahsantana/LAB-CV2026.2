import numpy as np
import cv2
import time

print("Checking the right and left camera IDs:")
print("Press (y) if IDs are correct and (n) to swap the IDs")
print("Press enter to start the process >> ")
input()

# Check for left and right camera IDs
CamL_id = 0
CamR_id = 2

CamL = cv2.VideoCapture(CamL_id)
CamR = cv2.VideoCapture(CamR_id)

for i in range(100):
    retL, frameL = CamL.read()
    retR, frameR = CamR.read()

cv2.imshow('imgL', frameL)
cv2.imshow('imgR', frameR)

# Captura a tecla uma única vez para validação
key = cv2.waitKey(0) & 0xFF
if key == ord('y') or key == ord('Y'):
    CamL_id = 0
    CamR_id = 2
    print("Camera IDs maintained")
elif key == ord('n') or key == ord('N'):
    CamL_id = 2
    CamR_id = 0
    print("Camera IDs swapped")
else:
    print("Wrong input response")
    exit(-1)

CamR.release()
CamL.release()

CamL = cv2.VideoCapture(CamL_id)
CamR = cv2.VideoCapture(CamR_id)
output_path = "./data/"

# Contador de fotos salvas
count = 0

print("\n--- Pronto para capturar! ---")
print("Pressione 's' para salvar o par de fotos coloridas.")
print("Pressione 'ESC' para sair.")

while True:
    retR, frameR = CamR.read()
    retL, frameL = CamL.read()
    
    if not retR or not retL:
        print("Erro ao ler as câmeras.")
        break

    # Criando cópias para exibição (para o texto do contador não sair na foto salva)
    viewL = frameL.copy()
    viewR = frameR.copy()
    
    # Mostra o contador de fotos atual na tela de exibição
    cv2.putText(viewL, f"Fotos: {count}/15", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('imgR', viewR)
    cv2.imshow('imgL', viewL)

    # Captura o teclado
    k = cv2.waitKey(1) & 0xFF
    
    # Se pressionar 's', salva os frames coloridos originais
    if k == ord('s'):
        # Salvando os frames originais (Coloridos)
        cv2.imwrite(f"{output_path}stereoL/frm_{count}_Duda.jpg", frameL)
        cv2.imwrite(f"{output_path}stereoR/frm_{count}_Duda.jpg", frameR)
        
        print(f"Foto colorida par {count} salva com sucesso!")
        count += 1
        
        # Limite máximo de fotos (15)
        if count >= 15:
            print("Limite de 15 fotos atingido!")
            break
            
    # Se pressionar ESC, fecha o programa
    elif k == 27:
        print("Fechando as câmeras pelo usuário!")
        break

# Libera as Câmeras e fecha janelas
CamR.release()
CamL.release()
cv2.destroyAllWindows()
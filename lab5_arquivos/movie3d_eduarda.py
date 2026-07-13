import numpy as np 
import cv2
import os
import time

# IDs das webcams físicas (0 e 2 conforme os testes)
CamL_id = 0
CamR_id = 2

CamL = cv2.VideoCapture(CamL_id)
CamR = cv2.VideoCapture(CamR_id)

# Captura um frame inicial para descobrir a resolução real das câmeras
retL, imgL_init = CamL.read()
if not retL:
    print("Erro crítico: Não foi possível acessar as câmeras. Verifique os cabos USB.")
    exit(-1)

h_live, w_live = imgL_init.shape[:2]
print(f"Câmeras prontas. Resolução de gravação: {w_live}x{h_live}")

# Garante que a pasta data existe
if not os.path.exists('data'):
    os.makedirs('data')

# --- CONFIGURAÇÃO DOS GRAVADORES DUPLOS ---
# 1. Gravador MP4
fourcc_mp4 = cv2.VideoWriter_fourcc(*'mp4v')
filename_mp4 = 'data/video_3d_analifo_garrafa.mp4'
writer_mp4 = cv2.VideoWriter(filename_mp4, fourcc_mp4, 20.0, (w_live, h_live))

# 2. Gravador AVI
fourcc_avi = cv2.VideoWriter_fourcc(*'XVID')
filename_avi = 'data/video_3d_analifo_garrafa.avi'
writer_avi = cv2.VideoWriter(filename_avi, fourcc_avi, 20.0, (w_live, h_live))

if not writer_mp4.isOpened() or not writer_avi.isOpened():
    print("Erro: O OpenCV não conseguiu inicializar um dos gravadores de vídeo.")
    exit(-1)

print("\n--- INICIANDO GRAVAÇÃO DUPLA REVERTIDA/CORRIGIDA ---")
print("-> O efeito 3D agora está alinhado corretamente com os óculos.")
print(f"-> Gravando MP4 em: {filename_mp4}")
print(f"-> Gravando AVI em: {filename_avi}")
print("A gravação vai durar exatamente 15 segundos...")

start_time = time.time()
duracao_segundos = 15 

while True:
    retR, imgR = CamR.read()
    retL, imgL = CamL.read()
    
    if not retL or not retR:
        print("Erro de sinal no meio da gravação.")
        break

    # Calcula o cronômetro
    tempo_passado = time.time() - start_time
    tempo_restante = int(duracao_segundos - tempo_passado)

    # Condição de parada automática (15 segundos)
    if tempo_passado >= duracao_segundos:
        print("\nTempo limite de 15 segundos atingido!")
        break

    # === ALGORITMO DE MONTAGEM DO ANÁGLIFO CORRIGIDO ===
    output = np.zeros_like(imgR)
    
    # Inversão correta para óculos Vermelho/Azul padrão no OpenCV (BGR):
    output[:,:,0] = imgL[:,:,0] # Canal Azul (Blue) vem da câmera ESQUERDA
    output[:,:,1] = imgL[:,:,1] # Canal Verde (Green) vem da câmera ESQUERDA
    output[:,:,2] = imgR[:,:,2] # Canal Vermelho (Red) vem da câmera DIREITA

    # Grava o frame corrigido nos dois arquivos de forma simultânea
    writer_mp4.write(output)
    writer_avi.write(output)
    
    # Cria uma cópia limpa para a janela de exibição com o texto do cronômetro
    tela_exibicao = output.copy()
    cv2.putText(tela_exibicao, f"Gravando 3D Correto: {tempo_restante}s restantes", (30, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    # Mostra o resultado final na tela
    cv2.imshow("Gravador Duplo 3D - Canais Corrigidos", tela_exibicao)

    # Permite interromper a gravação antes se pressionar 'q'
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        print("\nGravação interrompida manualmente.")
        break

# Desliga as câmeras e fecha os arquivos de vídeo com segurança
CamR.release()
CamL.release()
writer_mp4.release()
writer_avi.release()
cv2.destroyAllWindows()

print("\n--- PROCESSAMENTO FINALIZADO ---")
print(f"1. Arquivo salvo: {filename_avi}")
print(f"2. Arquivo salvo: {filename_mp4}")
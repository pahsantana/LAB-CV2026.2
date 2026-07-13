import numpy as np 
import cv2
from tqdm import tqdm

# Caminho das imagens salvas pelo script anterior
pathL = "./data/stereoL/"
pathR = "./data/stereoR/"

print("Extracting image coordinates of respective 3D pattern ....\n")

# Critério de parada para o refinamento dos cantos
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# IMPORTANTE: Ajustado para o padrão (8,6) do seu primeiro script.
# Se o seu tabuleiro for diferente, mude aqui e no findChessboardCorners.
board_size = (8, 6)

objp = np.zeros((board_size[0] * board_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:board_size[0], 0:board_size[1]].T.reshape(-1, 2)

img_ptsL = []
img_ptsR = []
obj_pts = []

# Loop ajustado de 0 a 14 (para as 15 fotos tiradas)
# Se você tirou uma quantidade diferente (ex: 12), mude o 15 para o total de fotos.
total_fotos = 15

for i in tqdm(range(total_fotos)):
    # Lendo os arquivos com a nomenclatura exata do primeiro script
    filename = f"frm_{i}_Duda.jpg"
    
    imgL = cv2.imread(pathL + filename)
    imgR = cv2.imread(pathR + filename)
    
    # Validação caso alguma foto esteja faltando ou com problemas
    if imgL is None or imgR is None:
        print(f"\n[Aviso] Arquivo {filename} não encontrado. Pulando...")
        continue

    imgL_gray = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    imgR_gray = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    outputL = imgL.copy()
    outputR = imgR.copy()

    # Encontrando os cantos do tabuleiro (ajustado para board_size)
    retR, cornersR = cv2.findChessboardCorners(outputR, board_size, None)
    retL, cornersL = cv2.findChessboardCorners(outputL, board_size, None)

    if retR and retL:
        obj_pts.append(objp)
        cv2.cornerSubPix(imgR_gray, cornersR, (11, 11), (-1, -1), criteria)
        cv2.cornerSubPix(imgL_gray, cornersL, (11, 11), (-1, -1), criteria)
        
        cv2.drawChessboardCorners(outputR, board_size, cornersR, retR)
        cv2.drawChessboardCorners(outputL, board_size, cornersL, retL)
        
        cv2.imshow('cornersR', outputR)
        cv2.imshow('cornersL', outputL)
        
        # Pressione qualquer tecla para ir para a próxima foto do loop
        cv2.waitKey(100)  # Mudei para 100ms para passar mais rápido, se quiser manual mude para 0

        img_ptsL.append(cornersL)
        img_ptsR.append(cornersR)

cv2.destroyAllWindows()

# Garante que pelo menos algumas fotos foram detectadas antes de calibrar
if len(obj_pts) == 0:
    print("Erro: Nenhum padrão de xadrez foi encontrado nas imagens. Verifique a iluminação ou o tamanho do grid.")
    exit(-1)

print(f"\nImagens processadas com sucesso para calibração: {len(obj_pts)}/{total_fotos}")

print("Calculating left camera parameters ... ")
# Calibrating left camera
retL, mtxL, distL, rvecsL, tvecsL = cv2.calibrateCamera(obj_pts, img_ptsL, imgL_gray.shape[::-1], None, None)
hL, wL = imgL_gray.shape[:2]
new_mtxL, roiL = cv2.getOptimalNewCameraMatrix(mtxL, distL, (wL, hL), 1, (wL, hL))

print("Calculating right camera parameters ... ")
# Calibrating right camera
retR, mtxR, distR, rvecsR, tvecsR = cv2.calibrateCamera(obj_pts, img_ptsR, imgR_gray.shape[::-1], None, None)
hR, wR = imgR_gray.shape[:2]
new_mtxR, roiR = cv2.getOptimalNewCameraMatrix(mtxR, distR, (wR, hR), 1, (wR, hR))

print("Stereo calibration .....")
flags = 0
flags |= cv2.CALIB_FIX_INTRINSIC

criteria_stereo = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Calibração estéreo
retS, new_mtxL, distL, new_mtxR, distR, Rot, Trns, Emat, Fmat = cv2.stereoCalibrate(
    obj_pts, img_ptsL, img_ptsR, new_mtxL, distL, new_mtxR, distR,
    imgL_gray.shape[::-1], criteria_stereo, flags
)

# Retificação Estéreo
rectify_scale = 1 
rect_l, rect_r, proj_mat_l, proj_mat_r, Q, roiL, roiR = cv2.stereoRectify(
    new_mtxL, distL, new_mtxR, distR, imgL_gray.shape[::-1], Rot, Trns, rectify_scale, (0, 0)
)

# Mapeamento de Retificação e Remoção de Distorção
Left_Stereo_Map = cv2.initUndistortRectifyMap(new_mtxL, distL, rect_l, proj_mat_l, imgL_gray.shape[::-1], cv2.CV_16SC2)
Right_Stereo_Map = cv2.initUndistortRectifyMap(new_mtxR, distR, rect_r, proj_mat_r, imgR_gray.shape[::-1], cv2.CV_16SC2)

print("Saving parameters ......")
cv_file = cv2.FileStorage("data/params_py.xml", cv2.FILE_STORAGE_WRITE)
cv_file.write("Left_Stereo_Map_x", Left_Stereo_Map[0])
cv_file.write("Left_Stereo_Map_y", Left_Stereo_Map[1])
cv_file.write("Right_Stereo_Map_x", Right_Stereo_Map[0])
cv_file.write("Right_Stereo_Map_y", Right_Stereo_Map[1])
cv_file.release()

print("Parâmetros salvos com sucesso em data/params_py.xml!")
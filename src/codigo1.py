import cv2
import numpy as np
import pandas as pd
from PIL import Image
import torchvision
import torchvision.transforms as T
import torch

def is_nature(image_path):

    # Cargar el modelo preentrenado de resnet50
    model = torchvision.models.resnet50(pretrained=True)
    model.eval()

    # Clases de elementos naturales en ImageNet (árboles, montañas, ríos, etc.)
    nature_classes = [388, 589, 561, 562, 563, 564, 565, 566, 567]

    # Preprocesar la imagen
    preprocess = T.Compose([
        T.Resize(256),
        T.CenterCrop(224),
        T.ToTensor(),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    img = Image.open(image_path)
    input_tensor = preprocess(img)
    input_batch = input_tensor.unsqueeze(0)

    # Pasar la imagen preprocesada a través de la red
    with torch.no_grad():
        output = model(input_batch)

    # Calcular la probabilidad de las clases de elementos naturales
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    nature_probabilities = probabilities[nature_classes].sum()

    # Verificar si la probabilidad de elementos naturales supera el umbral
    return nature_probabilities >= 0.75


def image_entropy(image_path):
    image = cv2.imread(image_path)
    if len(image.shape) == 2:
        # Imagen en escala de grises
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])
        max_entropy = np.log2(256)
    else:
        # Imagen a color
        hist_r = cv2.calcHist([image], [0], None, [256], [0, 256])
        hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
        hist_b = cv2.calcHist([image], [2], None, [256], [0, 256])
        hist = hist_r + hist_g + hist_b
        max_entropy = np.log2(256**3)

    hist /= hist.sum()
    entropy = -np.sum(hist * np.log2(hist + np.finfo(float).eps))
    normalized_entropy = entropy / max_entropy

    return normalized_entropy


def image_energy(image_path):
    image = cv2.imread(image_path)
    if len(image.shape) == 2:
        # Imagen en escala de grises
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    else:
        # Imagen a color
        hist_r = cv2.calcHist([image], [0], None, [256], [0, 256])
        hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
        hist_b = cv2.calcHist([image], [2], None, [256], [0, 256])
        hist = hist_r + hist_g + hist_b

    hist /= hist.sum()
    energy = np.sum(hist**2)

    return energy


def image_focus(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    focus = np.var(laplacian)
    return focus


cont = 1
while cont <= 11:
    if cont == 8:
        cont += 1
        pass
    else:
        df = pd.read_csv(f'../data/datos{cont}_cleanRGB.csv')
        df["ph_entropia"] = 0.0
        df["ph_energia"] = 0.0
        df["ph_foco"] = 0.0

        for i in df.ph_nombre:
            imagen = '../images/'+i
            try:
                if is_nature(imagen):
                    df.loc[df.ph_nombre == i, 'ph_naturaleza'] = 1
                df.loc[df.ph_nombre == i, 'ph_entropia'] = image_entropy(imagen)
                df.loc[df.ph_nombre == i, 'ph_energia'] = image_energy(imagen)
                df.loc[df.ph_nombre == i, 'ph_foco'] = image_focus(imagen)
            except:
                pass

        df.to_csv(f'../data/datos{cont}_cleanRGBCV3.csv', index=False)
        cont += 1

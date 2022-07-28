import os
import shutil
from tkinter import *
from tkinter import filedialog
from shutil import *
import cv2

root = Tk()
root.title("Taş Kağıt Makas")
root.geometry("800x600")

global filepath1
global filepath2

width = 600
height = 400

tekGorselButonu = Button(None, text='Tek Görsel')
IkiliGorselButonu = Button(None, text='Oyunu Oyna')

tekCanvas = Canvas(root, width=width, height=height, bg="dark slate gray", )
ikiliCanvas = Canvas(root, width=width, height=height, bg="dark slate gray", )

tekButon = Button(tekCanvas, text='Yükle', fg='white', bg='green')
tekButon.config(height=5, width=8)
tekButon.pack()
tekCanvas.create_window(100, 30, window=tekButon)

tekCalistir = Button(tekCanvas, text='Çalıştır', fg='white', bg='gray')
tekCalistir.config(height=3, width=10)
tekCalistir.pack()
tekCanvas.create_window(500, 100, window=tekCalistir)

birinciFotoYukle = Button(ikiliCanvas, text='1.Yükle', fg='white', bg='green')
birinciFotoYukle.config(height=5, width=8)
birinciFotoYukle.pack()
ikiliCanvas.create_window(50, 30, window=birinciFotoYukle)

ikinciFotoYukle = Button(ikiliCanvas, text='2.Yükle', fg='white', bg='green')
ikinciFotoYukle.config(height=5, width=8)
ikinciFotoYukle.pack()
ikiliCanvas.create_window(550, 30, window=ikinciFotoYukle)

ikiliCalistir = Button(ikiliCanvas, text='Çalıştır', fg='white', bg='gray')
ikiliCalistir.config(height=3, width=10)  # yüzdelik oranında veriyor
ikiliCalistir.pack()
ikiliCanvas.create_window(500, 110, window=ikiliCalistir)

tekGorselButonu.pack()
IkiliGorselButonu.pack()


def tek(event):
    IkiliGorselButonu.destroy()
    tekCanvas.pack()


def ikili(event):
    tekGorselButonu.destroy()
    ikiliCanvas.pack()


def tekButonGorselSec(event):
    files = os.listdir('VeriSeti/')

    for f in files:
        try:
            os.remove(os.getcwd() + "/" + f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

    filepath1 = filedialog.askopenfilename()
    copy2(filepath1, "VeriSeti")


def ciftButonSagSec(event):
    filepath1 = filedialog.askopenfilename()
    copy2(filepath1, "VeriSeti")


def ciftButonSolSec(event):
    filepath2 = filedialog.askopenfilename()
    copy2(filepath2, "VeriSeti")


def tekFotografCalistir(event):
    shutil.rmtree(r'runs\detect')
    path = r"runs\detect"
    os.mkdir(path)
    os.system(
        'cmd /c "python yolov5/detect.py --weights agirliklar/last.pt --img 704 --conf 0.25 --source VeriSeti --save-crop --name exp"')

    baslikYolu = os.listdir("runs\\detect\\exp\\crops")
    baslik = baslikYolu[0]

    path2 = r"runs\detect\exp"
    arr = os.listdir(r"runs\detect\exp")
    foto = []
    x = len(arr)

    for i in range(0, x):
        if os.path.isfile(os.path.join(path2, arr[i])):
            foto.append(arr[i])

    cv2.namedWindow(baslik, cv2.WINDOW_NORMAL)
    im = cv2.imread(os.path.join(r"runs\detect\exp", foto[0]))
    imS = cv2.resize(im, (700, 700))
    cv2.imshow(baslik, imS)

    files = os.listdir('VeriSeti\\')

    for f in files:
        try:
            os.remove(os.getcwd() + "\\VeriSeti\\" + f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


def ciftFotografCalistir(event):


    shutil.rmtree(r'runs\detect')
    path = r"runs\detect"
    os.mkdir(path)
    os.system(
        'cmd /c "python yolov5/detect.py --weights agirliklar/last.pt --img 704 --conf 0.25 --source VeriSeti --save-crop --name exp"')
    path2 = r"runs\detect\exp\crops"
    arr = os.listdir(r"runs\detect\exp\crops")
    labels = []
    x = len(arr)

    for i in range(0, x):
        if os.path.isdir(os.path.join(path2, arr[i])):
            labels.append(arr[i])

    if labels[0] == "kagit":

        if len(labels) == 1:
            berabere = os.listdir("runs\detect\exp\crops\kagit")

            cv2.namedWindow("BERABERE1", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
            im1 = cv2.imread(os.path.join(r"runs\detect\exp", berabere[0]))  # Read image
            imS1 = cv2.resize(im1, (500, 500))  # Resize image
            cv2.imshow("BERABERE1", imS1)  # Show image

            cv2.namedWindow("BERABERE", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
            im = cv2.imread(os.path.join(r"runs\detect\exp", berabere[1]))  # Read image
            imS = cv2.resize(im, (500, 500))  # Resize image
            cv2.imshow("BERABERE", imS)  # Show image


        elif labels[1] == "makas":
            kazanan = os.listdir("runs\detect\exp\crops\\makas")
            kaybeden = os.listdir(r"runs\detect\exp\crops\kagit")

            cv2.namedWindow("KAZANAN", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
            im1 = cv2.imread(os.path.join(r"runs\detect\exp", kazanan[0]))  # Read image
            imS1 = cv2.resize(im1, (500, 500))  # Resize image
            cv2.imshow("KAZANAN", imS1)  # Show image

            cv2.namedWindow("KAYBEDEN", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
            im = cv2.imread(os.path.join(r"runs\detect\exp", kaybeden[0]))  # Read image
            imS = cv2.resize(im, (500, 500))  # Resize image
            cv2.imshow("KAYBEDEN", imS)  # Show image


        elif labels[1] == "tas":
            kazanan = os.listdir("runs\detect\exp\crops\kagit")
            kaybeden = os.listdir(r"runs\detect\exp\crops\tas")

            cv2.namedWindow("KAZANAN", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
            im1 = cv2.imread(os.path.join(r"runs\detect\exp", kazanan[0]))  # Read image
            imS1 = cv2.resize(im1, (500, 500))  # Resize image
            cv2.imshow("KAZANAN", imS1)  # Show image

            cv2.namedWindow("KAYBEDEN", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
            im = cv2.imread(os.path.join(r"runs\detect\exp", kaybeden[0]))  # Read image
            imS = cv2.resize(im, (500, 500))  # Resize image
            cv2.imshow("KAYBEDEN", imS)  # Show image

    if labels[0] == "makas":
        if len(labels) == 1:
            berabere = os.listdir("runs\detect\exp\crops\\makas")

            cv2.namedWindow("BERABERE1", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
            im1 = cv2.imread(os.path.join(r"runs\detect\exp", berabere[0]))  # Read image
            imS1 = cv2.resize(im1, (500, 500))  # Resize image
            cv2.imshow("BERABERE1", imS1)  # Show image

            cv2.namedWindow("BERABERE", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
            im = cv2.imread(os.path.join(r"runs\detect\exp", berabere[1]))  # Read image
            imS = cv2.resize(im, (500, 500))  # Resize image
            cv2.imshow("BERABERE", imS)  # Show image

        elif labels[1] == "tas":
            kazanan = os.listdir(r"runs\detect\exp\crops\tas")
            kaybeden = os.listdir(r"runs\detect\exp\crops\makas")

            cv2.namedWindow("KAZANAN", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
            im1 = cv2.imread(os.path.join(r"runs\detect\exp", kazanan[0]))  # Read image
            imS1 = cv2.resize(im1, (500, 500))  # Resize image
            cv2.imshow("KAZANAN", imS1)  # Show image

            cv2.namedWindow("KAYBEDEN", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
            im = cv2.imread(os.path.join(r"runs\detect\exp", kaybeden[0]))  # Read image
            imS = cv2.resize(im, (500, 500))  # Resize image
            cv2.imshow("KAYBEDEN", imS)  # Show image

    if labels[0] == "tas" and labels[0] == "tas":
        berabere = os.listdir("runs\detect\exp\crops\\tas")

        cv2.namedWindow("BERABERE1", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
        im1 = cv2.imread(os.path.join(r"runs\detect\exp", berabere[0]))  # Read image
        imS1 = cv2.resize(im1, (500, 500))  # Resize image
        cv2.imshow("BERABERE1", imS1)  # Show image

        cv2.namedWindow("BERABERE", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
        im = cv2.imread(os.path.join(r"runs\detect\exp", berabere[1]))  # Read image
        imS = cv2.resize(im, (500, 500))  # Resize image
        cv2.imshow("BERABERE", imS)  # Show image

    files = os.listdir('VeriSeti\\')

    for f in files:
        try:
            os.remove(os.getcwd() + "\\VeriSeti\\" + f)

        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


tekGorselButonu.bind('<Button-1>', tek)
IkiliGorselButonu.bind('<Button-1>', ikili)
tekButon.bind('<Button-1>', tekButonGorselSec)
birinciFotoYukle.bind('<Button-1>', ciftButonSolSec)
ikinciFotoYukle.bind('<Button-1>', ciftButonSagSec)
tekCalistir.bind('<Button-1>', tekFotografCalistir)
ikiliCalistir.bind('<Button-1>', ciftFotografCalistir)

root.mainloop()

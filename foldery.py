import sys, glob, os, shutil, string
from tkinter import Tk, filedialog
import ctypes  # An included library with Python install.   


directory = filedialog.askdirectory()
print(directory)
folder = directory.split("/")
folder_nazwa = folder[-1]

nfolder = folder_nazwa+'_doc'

if not os.path.isdir(folder_nazwa):
    ctypes.windll.user32.MessageBoxW(
        0, "Katalog początkowy nie istnieje", "Status")
else:
    os.chdir(folder_nazwa)
    base_folder = os.getcwd() #katalog początkowy
    print(base_folder)
    lista = list(os.listdir()) #lista plików wewnątrz obecnego katalogu
    print(len(lista))
    try:
        os.makedirs(nfolder)
    except FileExistsError:
        sys.exit('Katalog '+nfolder+' już istnieje')
    for l in lista:
        os.makedirs(nfolder+'/'+l) #tworzy puste katalogi o nazwach z listy folderów
        os.chdir(l) #przejscie do folderu z listy
        katras = os.getcwd()
        print(katras) #wypisuje obecny katalog
        lp = os.listdir('.')
        print(lp) #printuje wszystkie pliki wewnątrz katalogu
        for l in lp:
            folder = os.getcwd()
            folder1 = folder.split("\\")
            np = os.path.splitext(l)
            if np[1] == '.docx':
                start = katras+"\\"+l
                end = base_folder+"\\"+nfolder+"\\"+folder1[-1]+"\\"+l
                shutil.move(start, end)
            else:
                pass
            
        os.chdir(base_folder)
    ctypes.windll.user32.MessageBoxW(0, "Pliki zostały przekopiowane", "Status")

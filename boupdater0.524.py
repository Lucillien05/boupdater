import os
import sys
import tkinter as tk
from colorama import Fore, init
import wget
import shutil
from PIL import ImageTk, Image
os.chdir(os.path.dirname(os.path.dirname(sys.argv[0])))
print(f'Working with directory: {os.path.dirname(os.path.dirname(sys.argv[0]))}')

def capital():
    global alpha
    init(convert=True)
    print(Fore.WHITE + f'\nStarting to download patch-{alpha}:\n')
    if os.path.exists(f'Data\patch-{alpha}.MPQ'):
        os.remove(f'Data\patch-{alpha}.MPQ')
    remote_url = f'https://bradavice-online.cz/patches/patch-{alpha}.MPQ'
    local_file = f'Data\patch-{alpha}.MPQ'
    wget.download(remote_url, local_file)
    if os.path.exists(f'Data\patch-{alpha}.MPQ'):
        print(Fore.GREEN + '\nDONE!')
    else:
        print(Fore.RED + '\nFAILED!')
def small():
    global alpha
    init(convert=True)
    print(Fore.WHITE + f'\nStarting to download patch-{alpha}:\n')
    if os.path.exists(f'Data\patch-{alpha}.mpq'):
        os.remove(f'Data\patch-{alpha}.mpq')
    remote_url = f'https://bradavice-online.cz/patches/patch-{alpha}.mpq'
    local_file = f'Data\patch-{alpha}.mpq'
    wget.download(remote_url, local_file)
    if os.path.exists(f'Data\patch-{alpha}.mpq'):
        print(Fore.GREEN + '\nDONE!')
    else:
        print(Fore.RED + '\nFAILED!')
def patchall():
    patchh()
    patchp()
    patchs()
    patcht()
    patchm()
def patchh():
    global alpha
    alpha = 'H'
    capital()
def patchp():
    global alpha
    alpha = 'P'
    capital()
def patchs():
    global alpha
    alpha = 'S'
    capital()
def patcht():
    global alpha
    alpha = 'T'
    small()
def patchm():
    global alpha
    alpha = 'M'
    small()    
def boop():
    init(convert=True)
    if os.path.exists('Cache'):
        print (Fore.WHITE + '\nDeleting cache:')
        shutil.rmtree('Cache')
    else:
        print (Fore.WHITE + 'Cache not found, skipping...')
    print(Fore.WHITE + 'Starting game:')
    os.startfile('bradavice.exe')
    print(Fore.WHITE + 'Shutting down starter...:')
    sys.exit()
root = tk.Tk()
root.title('Bradavice-online Updater')
frame = tk.Frame(root)
root.geometry("375x25")
frame.pack()
alpha = ''
canvas = tk.Canvas(root, width=500, height=250)
canvas.pack(side=tk.LEFT)
img = ImageTk.PhotoImage(Image.open("0opener/logo.ppm"))
canvas.create_image(10,10, image=img)
pH = tk.Button(frame, text ="Patch-H", command = patchh, bg = 'red')
pH.pack(side=tk.LEFT)
pP = tk.Button(frame, text ="Patch-P", command = patchp, bg = 'orange')
pP.pack(side=tk.LEFT)
pS = tk.Button(frame, text ="Patch-S", command = patchs, bg = 'yellow')
pS.pack(side=tk.LEFT)
pT = tk.Button(frame, text ="Patch-T", command = patcht, bg = 'green')
pT.pack(side=tk.LEFT)
pT = tk.Button(frame, text ="Patch-M", command = patchm, bg = 'cyan')
pT.pack(side=tk.LEFT)
pT = tk.Button(frame, text ="UpdateALL", command = patchall, bg = 'blue')
pT.pack(side=tk.LEFT)
op = tk.Button(frame, text ="Open", command = boop, bg = 'magenta')
op.pack(side=tk.LEFT)
root.mainloop()

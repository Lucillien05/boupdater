import os
import tkinter as tk
from colorama import Fore, init
import wget
import shutil
def Notdone():
    init(convert=True)
    print(Fore.RED + '\nFAILED!')
def Done():
    init(convert=True)
    print(Fore.GREEN + '\nDONE!')
def patchh():
    init(convert=True)
    print(Fore.WHITE + '\nStarting to download patch-H:\n')
    if os.path.exists('Data\patch-H.MPQ'):
        os.remove('Data\patch-H.MPQ')
    remote_url = 'https://bradavice-online.cz/patches/patch-H.MPQ'
    local_file = 'Data\patch-H.MPQ'
    wget.download(remote_url, local_file)
    if os.path.exists('Data\patch-H.MPQ'):
        Done()
    else:
        NotDone()
def patchp():
    init(convert=True)
    print(Fore.WHITE + '\nStarting to download patch-P:\n')
    if os.path.exists('Data\patch-P.MPQ'):
        os.remove('Data\patch-P.MPQ')
    remote_url = 'https://bradavice-online.cz/patches/patch-P.MPQ'
    local_file = 'Data\patch-P.MPQ'
    wget.download(remote_url, local_file)
    if os.path.exists('Data\patch-P.MPQ'):
        Done()
    else:
        NotDone()
def patchs():
    init(convert=True)
    print(Fore.WHITE + '\nStarting to download patch-S:\n')
    if os.path.exists('Data\patch-S.MPQ'):
        os.remove('Data\patch-S.MPQ')
    remote_url = 'https://bradavice-online.cz/patches/patch-S.MPQ'
    local_file = 'Data\patch-S.MPQ'
    wget.download(remote_url, local_file)
    if os.path.exists('Data\patch-S.MPQ'):
        Done()
    else:
        NotDone()
def patcht():
    init(convert=True)
    print(Fore.WHITE + '\nStarting to download patch-T:\n')
    if os.path.exists('Data\patch-T.MPQ'):
        os.remove('Data\patch-T.MPQ')
    remote_url = 'https://bradavice-online.cz/patches/patch-T.mpq'
    local_file = 'Data\patch-T.mpq'
    wget.download(remote_url, local_file)
    if os.path.exists('Data\patch-T.MPQ'):
        Done() 
    else:
        NotDone()
def patchm():
    init(convert=True)
    print(Fore.WHITE + '\nStarting to download patch-M:\n')
    if os.path.exists('Data\patch-M.MPQ'):
        os.remove('Data\patch-M.MPQ')
    remote_url = 'https://bradavice-online.cz/patches/Patch-M.mpq'
    local_file = 'Data\patch-M.MPQ'
    wget.download(remote_url, local_file)
    if os.path.exists('Data\patch-M.MPQ'):
        Done()
    else:
        NotDone()
def patchall():
    patchh()
    patchp()
    patchs()
    patcht()
    patchm()
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
    quit()
root = tk.Tk()
root.title('Bradavice-online Updater')
frame = tk.Frame(root)
root.geometry("375x25")
frame.pack()
print(shutil.which('bradavice.exe'))
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

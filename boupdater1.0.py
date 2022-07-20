import urllib.request
import os
import sys
import wget
import shutil
os.chdir(os.path.dirname(os.path.dirname(sys.argv[0])))
fail = 0
patches = ['H','P','S','T']
mpqs = ['mpq','MPQ','Mpq']
patchs = ['patch', 'PATCH', 'Patch']
for patch in patches:
    for mpq in mpqs:
        for patchurl in patchs:
            try:
                if os.path.exists(f'Data\{patchurl}-{patch}.{mpq}'):
                    if int(urllib.request.urlopen(f'https://bradavice-online.cz/patches/{patchurl}-{patch}.{mpq}').length) != int(os.path.getsize(f'Data/{patchurl}-{patch}.{mpq}')):
                        print(f'Patch-{patch} is outdated. Updating...')
                        os.remove(f'Data\{patchurl}-{patch}.{mpq}')
                        wget.download(f'https://bradavice-online.cz/patches/{patchurl}-{patch}.{mpq}', f'Data\{patchurl}-{patch}.{mpq}')
                        print('Patch-{patch} successfully updated!')
                else:
                    if int(urllib.request.urlopen(f'https://bradavice-online.cz/patches/{patchurl}-{patch}.{mpq}').length) == 0:
                        print('Error')
                    print(f'No Patch-{patch} detected. Downloading new...')
                    wget.download(f'https://bradavice-online.cz/patches/{patchurl}-{patch}.{mpq}', f'Data\{patchurl}-{patch}.{mpq}')
                    print('Done')
            except:
                fail += 1
if os.path.exists('Data\Patch-M.mpq') and int(os.path.getsize('Data/Patch-M.mpq')) == 8707764965:
    if os.path.exists('Cache'):
        shutil.rmtree('Cache')
    os.startfile('bradavice.exe')
    sys.exit()
else:
    print('You have not updated OR installed Patch-M, cancelled opening.')

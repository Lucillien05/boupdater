import urllib.request
import os
import sys
import wget
import shutil
import time
os.chdir(os.path.dirname(os.path.dirname(sys.argv[0])))
fail = 0
noupt = 0
done = 0
patches = ['H','P','S','T']
mpqs = ['mpq','MPQ','Mpq']
patchs = ['patch', 'PATCH', 'Patch']
for patch in patches:
    for mpq in mpqs:
        for patchurl in patchs:
            try:
                if os.path.exists(f'Data\{patchurl}-{patch}.{mpq}'):
                    if int(urllib.request.urlopen(f'https://bradavice-online.cz/patches/{patchurl}-{patch}.{mpq}').length) != int(os.path.getsize(f'Data/{patchurl}-{patch}.{mpq}')):
                        print(f'\nPatch-{patch} is outdated. Updating...')
                        os.remove(f'Data\{patchurl}-{patch}.{mpq}')
                        wget.download(f'https://bradavice-online.cz/patches/{patchurl}-{patch}.{mpq}', f'Data\{patchurl}-{patch}.{mpq}')
                        done += 1
                    elif int(urllib.request.urlopen(f'https://bradavice-online.cz/patches/{patchurl}-{patch}.{mpq}').length) == int(os.path.getsize(f'Data/{patchurl}-{patch}.{mpq}')):
                        noupt += 1
                else:
                    if int(urllib.request.urlopen(f'https://bradavice-online.cz/patches/{patchurl}-{patch}.{mpq}').length) == 0:
                        print('Error')
                    print(f'\nNo Patch-{patch} detected. Downloading new...')
                    wget.download(f'https://bradavice-online.cz/patches/{patchurl}-{patch}.{mpq}', f'Data\{patchurl}-{patch}.{mpq}')
                    done += 1
            except:
                fail += 1
if done != 0:
    print('\n')
if os.path.exists('Data\Patch-M.mpq') and int(os.path.getsize('Data/Patch-M.mpq')) == 8707764965:
    if noupt == 4:
        print('All patches are already updated.')
else:
    print('Patch-M is not updated or installed properly.')
    m = input('Proceed? (y/n): ')
    if m == 'y' or m == '1':
        pass
    else:
        sys.exit()
if os.path.exists('Cache'):
    shutil.rmtree('Cache')
    print('Deleting Cache.')
print('Opening Bradavice-Online:')
os.startfile('bradavice.exe')
sys.exit()

import os
import shutil

c = 'pbrt.exe'
objfiles = []
for file in os.listdir('.'):
    if os.path.splitext(file)[1]==".pbrt":
        objfiles.append(file)

spp = 2
for i in range(1,6):
    spp = spp * 2
    strspp = str(spp)
    for i in range(0, len(objfiles)):
        c0 = objfiles[i]
        c1 = c+' '+c0+' --spp ' + strspp
        os.system(c1)

        print c0
        print i

   

    for file in os.listdir('.'):
        if os.path.splitext(file)[1] == ".exr":
            shutil.move(file, strspp + "spp")

    for file in os.listdir('.'):
        if os.path.splitext(file)[1] == ".mat":
            shutil.move(file, strspp + "spp")

    for file in os.listdir('.'):
        if os.path.splitext(file)[1] == ".txt":
            shutil.move(file, strspp + "spp")




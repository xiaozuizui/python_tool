import os
import shutil

spp = '32768'
c = 'pbrt.exe'
sample = 'pixelsamples" ['
objfiles = []
for file in os.listdir('.'):
    if os.path.splitext(file)[1]==".pbrt":
        objfiles.append(file)

for i in range(0, len(objfiles)):
     pbrt = open(objfiles[i],'r')
     str = pbrt.read()
     start_index = str.find(sample)
     start_index = str.find('[',start_index)+1
     end_index = str.find(']',start_index)
     pbrt1 = str[0:start_index]
     pbrt2 = str[end_index:]
     newpbrt = pbrt1+spp+pbrt2
     pbrt.close()
     pbrt = open(objfiles[i], 'w')
     pbrt.write(newpbrt)
     pbrt.close()
     print i

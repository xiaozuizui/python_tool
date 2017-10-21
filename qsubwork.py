import os
import shutil

for i in range(0,246,2):
    c1 = 'qsub task'+str(i)
    print (c1)
    os.system(c1)
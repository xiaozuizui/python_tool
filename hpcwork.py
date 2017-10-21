import os
import shutil

c = 'pbrt'
head = "#PBS -l nodes=5:ppn=20 \ncd $PBS_O_WORKDIR \ncat $PBS_NODEFILE > $PBS_O_WORKDIR/hosts.${PBS_JOBID}\n"
objfiles = []
for file in os.listdir('.'):
    if os.path.splitext(file)[1]==".pbrt":
        objfiles.append(file)

for i in range(0, len(objfiles),2):
        c1 =head+'./'+c+ ' $HOME/crisFolder/pbrt-allscene/'+ objfiles[i]+'\n'
        c1 = c1+ './'+c+' $HOME/crisFolder/pbrt-allscene/'+ objfiles[i+1]+'\n'
        print (c1)
        taskname = 'task'+str(i)
        pbrt = open(taskname, 'w')
        pbrt.write(c1)
        pbrt.close()
        print i
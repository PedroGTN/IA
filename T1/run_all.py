import os
import sys

if len(sys.argv) == 1:
    num_instâncias = 50
    tam_instâncias = 6
else:
    num_instâncias = sys.argv[1]
    tam_instâncias = sys.argv[2]


inst_folder = "instancias/"
insts = os.listdir(inst_folder)
res = os.listdir('resultados/')
for i in insts:
    inst = inst_folder + i
    os.remove(inst)
for r in res:
    resp = 'resultados/' + r
    os.remove(resp)


os.system("python3 gerador_instancias.py " + str(num_instâncias) + " " + str(tam_instâncias) + ' ' + inst_folder)



insts = os.listdir(inst_folder)
for i in insts:
    inst = inst_folder + i
    exec = "python3 main.py 0 200 " + inst + " resultados/"
    os.system(exec)
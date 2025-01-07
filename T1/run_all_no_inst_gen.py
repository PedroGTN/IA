import os

num_instâncias = 50
tam_instâncias = 6

inst_folder = "instancias/"
insts = os.listdir(inst_folder)

for i in insts:
    inst = inst_folder + i
    exec = "python3 main.py 0 200 " + inst + " resultados/"
    os.system(exec)
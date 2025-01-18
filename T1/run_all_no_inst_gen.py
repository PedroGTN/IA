import os

inst_folder = "instancias/"
insts = os.listdir(inst_folder)

for i in insts:
    inst = inst_folder + i
    exec = "python3 main.py 0 0 " + inst + " resultados/ 1234"
    os.system(exec)
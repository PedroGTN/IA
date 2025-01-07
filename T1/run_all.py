import os

num_instâncias = 50
tam_instâncias = 6

os.system("python3 gerador_instancias.py " + str(num_instâncias) + " " + str(tam_instâncias) + " instancias/")

inst_folder = "instancias/"
insts = os.listdir(inst_folder)

for i in insts:
    inst = inst_folder + i
    exec = "python3 main.py 0 200 " + inst + " resultados/"
    os.system(exec)
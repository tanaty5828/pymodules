import os

def MakeAnalyDir(dir_name = 'Analy'):
    os.makedirs(f'./{dir_name}/', exist_ok = True)

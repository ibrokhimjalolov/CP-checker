import subprocess
from conf import *


def compile():
    command = 'g++ -o ' + os.path.join(LAB_DIR, 'a.exe') + ' ' + SOURCE_FILE
    result = subprocess.run(command, shell=True)
    print(result)
    return result.returncode == 0


def get_testcases() -> dict:
    ios = set()
    from os import listdir
    from os.path import isfile, join
    files = [f for f in listdir(IO_DIR_NAME) if isfile(join(IO_DIR_NAME, f))]
    for f in files:
        ios.add(f.split('.')[0])
    return list(ios)


def generate_input_file_name(s: str) -> str:
    return os.path.join(IO_DIR_NAME, f'{s}.in.txt')


def generate_output_file_name(s: str) -> str:
    return os.path.join(IO_DIR_NAME, f'{s}.out.txt')

def diff(a, b):
    cmd = f'FC /w {a} {b}'
    res = 0
    with open(os.path.join(LAB_DIR, 'gar.txt'), 'w') as f:
        res = subprocess.run(cmd, stdout=f, shell=False)
        return res.returncode
    return res

def run_on_test(stdin, stdout):
    exe_file = os.path.join(LAB_DIR, 'a.exe')
    user_output = os.path.join(LAB_DIR, 'user_output', 'out.txt')
    user_err = os.path.join(LAB_DIR, 'user_output', 'err.txt')
    result = 0
    with open(stdin, 'r') as _in, open(user_output, 'w') as _out, open(user_err, 'w') as err:
        result = subprocess.run(exe_file, stdin=_in, stdout=_out, stderr=err, shell=False)

    if result.returncode:
        return 're'
    
    if int(diff(stdout, user_output)):
        return 'wa'
    return 'ok'




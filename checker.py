from utils import (compile, 
                   generate_input_file_name, 
                   get_testcases, 
                   generate_output_file_name,
                   run_on_test)
from conf import (IO_DIR_NAME, 
                  LAB_DIR, 
                  SOURCE_FILE, 
                  LOG_FILE)
import logging


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

logging.info('Compiling ' + SOURCE_FILE)
return_code = compile()
print(return_code)
if return_code == False:
    logging.info('CompilationError ')
    exit(0)

testcases = get_testcases()

testcases.sort()

for test in range(1, len(testcases)+1):
    stdin = generate_input_file_name(testcases[test-1])
    stdout = generate_output_file_name(testcases[test-1])

    status = run_on_test(stdin, stdout)
    if status != 'ok':
        logging.warning(f'Testcase #{testcases[test-1]} {status}')
        logging.warning(f'Solution incorrect STATUS={status} ' + SOURCE_FILE)
        exit(0)

    logging.info(f'Testcase #{test} ok')


logging.warning(f'Solution correct STATUS=OK' + SOURCE_FILE)
    



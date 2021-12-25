from environs import Env
import os


env = Env()
env.read_env()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IO_DIR_NAME = env.str("IO_DIR_NAME") 
SOURCE_FILE = env.list("SOURCE_FILE") 
LOG_FILE = env.str("LOG_FILE")
LAB_DIR = os.path.join(BASE_DIR, 'lab')


if isinstance(IO_DIR_NAME, list):
    IO_DIR_NAME = IO_DIR_NAME[0]

if isinstance(SOURCE_FILE, list):
    SOURCE_FILE = SOURCE_FILE[0]

if isinstance(LOG_FILE, list):
    LOG_FILE = LOG_FILE[0]
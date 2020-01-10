import sys
import subprocess

from todo.main.rpc_client import app
from todo.main.rpc_server import serve


def run():
    if(sys.argv[1] == 'start' and sys.argv[2] == 'server'):
        # print(subprocess.run(['python', 'code_gen.py']))
        print('Running Server \n')
        # subprocess.run(['python', './todo/main/rpc_server.py'])
        serve()

    elif(sys.argv[1] == 'start' and sys.argv[2] == 'client'):
        # print(subprocess.run(['python', 'code_gen.py']))
        print('Running Client \n')
        # subprocess.run(['python', './todo/main/rpc_client.py'])
        app()

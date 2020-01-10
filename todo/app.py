import sys
import subprocess


def run():
    if(sys.argv[1] == 'start' and sys.argv[2] == 'server'):
        # print(subprocess.run(['python', 'code_gen.py']))
        print('Running Server \n')
        subprocess.run(['python', './todo/main/rpc_server.py'])

    elif(sys.argv[1] == 'start' and sys.argv[2] == 'client'):
        # print(subprocess.run(['python', 'code_gen.py']))
        print('Running Client \n')
        subprocess.run(['python', './todo/main/rpc_client.py'])

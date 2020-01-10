import sys
import subprocess

print(sys.path)

if(sys.argv[1] == 'start' and sys.argv[2] == 'server'):
    # print(subprocess.run(['python', 'code_gen.py']))
    print(subprocess.run(['python', './main/rpc_server.py']))

elif(sys.argv[1] == 'start' and sys.argv[2] == 'client'):
    # print(subprocess.run(['python', 'code_gen.py']))
    print(subprocess.run(['python', './main/rpc_client.py']))

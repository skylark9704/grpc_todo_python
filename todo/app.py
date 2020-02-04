import sys
# import subprocess

from todo.main.client.app import client
from todo.main.server.app import server


def run():
    if(sys.argv[1] == 'start' and sys.argv[2] == 'server'):
        print('Running Server \n')
        server()

    elif(sys.argv[1] == 'start' and sys.argv[2] == 'client'):
        print('Running Client \n')
        client()

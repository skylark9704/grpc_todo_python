from setuptools import setup, find_packages

setup(
    name='my_grpc',
    version='0.1.0',
    description='Simple Todo App made with gRPC',
    author='Sushant Vangapandu',
    author_email='sushant@beautifulcode.in',
    url='https://github.com/skylark9704/grpc_todo_python',
    packages=['main', 'db', 'alembic']
)

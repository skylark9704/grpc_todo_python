from grpc_tools import protoc

protoc.main((
    '',
    '-I./protos',
    '--python_out=./main',
    '--grpc_python_out=./main',
    './protos/todos.proto',
))

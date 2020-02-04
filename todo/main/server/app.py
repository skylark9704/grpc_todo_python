from todo.rpcs import todos_pb2_grpc
from todo.main.server.service import TodoService
import grpc
from concurrent import futures


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todos_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

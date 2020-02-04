from todo.rpcs import todos_pb2_grpc
from todo.main.server import Server


class TodoService(todos_pb2_grpc.TodoServiceServicer):

    def __init__(self):
        pass

    def AddTodo(self, request, context):
        return Server.add(data=request)

    def GetTodo(self, request, context):
        return Server.get(data=request)

    def ListAllTodo(self, request, context):
        responses = Server.list_all()

        for response in responses:
            yield response

    def EditTodo(self, request, context):
        return Server.edit(data=request)

    def DeleteTodo(self, request, context):
        return Server.delete(data=request)

    def ToggleStatus(self, request, context):
        return Server.toggle_status(data=request)

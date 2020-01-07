from concurrent import futures
from collections import namedtuple, OrderedDict

import json
from datetime import datetime

import grpc
import todos_pb2
import todos_pb2_grpc

todos = OrderedDict()


class TodoService(todos_pb2_grpc.TodoServicer):

    def __init__(self):
        pass

    def SaveTodo(self, request, context):
        date = datetime.now()
        index = len(todos)+1
        todo = {
            'id': index,
            'title': request.title,
            'description': request.description,
            'date': date.strftime("%B %d, %Y"),
            'status': 'Incomplete'
        }
        todos[index] = todo
        print(todos)
        return todos_pb2.TodoResponse(message="Saved")

    def ListTodo(self, request, context):
        index = int(request.id)
        if index in todos:
            todo = todos[index]
            return todos_pb2.ListTodoResponse(
                data=json.dumps(todo).encode('utf-8')
            )
        else:
            return todos_pb2.ListTodoResponse(message='No Todo Found')

    def ListAllTodo(self, request, context):
        res = not todos
        print(res)
        if not todos:
            yield todos_pb2.ListAllTodoResponse(message="No Todos found")
        for key in todos:
            yield todos_pb2.ListAllTodoResponse(
                data=json.dumps(todos[key]).encode('utf-8')
            )

    def EditTodo(self, request, context):
        index = int(request.id)

        if index in todos:
            todo = todos[index]
            todo['title'] = request.title
            todo['description'] = request.description
            return todos_pb2.TodoResponse(message='Update Successful')

        return todos_pb2.TodoResponse(message="No Todo found with that ID")

    def DeleteTodo(self, request, context):
        print("Deleting Todo")
        index = int(request.id)
        if index in todos:
            del todos[index]
            return todos_pb2.TodoResponse(message="Deleted")
        else:
            return todos_pb2.TodoResponse(message="Todo Does Not Exist")

    def ToggleStatus(self, request, context):
        print('Toggling Status')
        index = int(request.id)
        if index in todos:
            status = todos[index]["status"]
            if status == 'Incomplete':
                todos[index]["status"] = 'Complete'
                return todos_pb2.TodoResponse(
                    message="Status Changed to [COMPLETE]"
                )

            todos[index]["status"] = 'Incomplete'
            return todos_pb2.TodoResponse(
                message="Status Changed to [INCOMPLETE]"
            )

        return todos_pb2.TodoResponse(
            message="No Todo with specified ID found"
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todos_pb2_grpc.add_TodoServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

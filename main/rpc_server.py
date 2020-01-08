import sys
import os
sys.path.insert(0, os.curdir)
import todos_pb2_grpc
import todos_pb2
import grpc
from datetime import datetime
import json
from db.db import Session, engine
from db.models.Todo import Todo
from collections import namedtuple, OrderedDict
from concurrent import futures
from contextlib import contextmanager


class TodoService(todos_pb2_grpc.TodoServicer):

    def __init__(self):
        self.session = Session()

    def SaveTodo(self, request, context):
        todo = Todo(
            title=request.title,
            description=request.description
        )
        with session_scope() as session:
            session.add(todo)
            session.commit()
            return todos_pb2.TodoResponse(message="Saved")

    def ListTodo(self, request, context):
        id = int(request.id)

        with session_scope() as session:
            row = session.query(Todo).get(id)
            if row:
                print(row2dict(row))
                return todos_pb2.ListTodoResponse(
                    data=json.dumps(row2dict(row)).encode('utf-8')
                )
            else:
                return todos_pb2.ListTodoResponse(message='No Todo Found')

    def ListAllTodo(self, request, context):
        with session_scope() as session:
            todos = session.query(Todo).order_by(Todo.id)
            if not todos:
                yield todos_pb2.ListAllTodoResponse(message="No Todos found")
            for todo in todos:
                yield todos_pb2.ListAllTodoResponse(
                    data=json.dumps(row2dict(todo)).encode('utf-8')
                )

    def EditTodo(self, request, context):
        id = int(request.id)

        with session_scope() as session:
            todo = session.query(Todo).get(id)
            if todo:
                todo.title = todo.title if request.title == "" else request.title
                todo.description = todo.description if request.description == "" else request.description
                session.commit()
                return todos_pb2.TodoResponse(message='Update Successful')

        return todos_pb2.TodoResponse(message="No Todo found with that ID")

    def DeleteTodo(self, request, context):
        id = int(request.id)

        with session_scope() as session:
            todo = session.query(Todo).get(id)
            if todo:
                session.delete(todo)
                session.commit()
                return todos_pb2.TodoResponse(message="Deleted")
            else:
                return todos_pb2.TodoResponse(message="Todo Does Not Exist")

    def ToggleStatus(self, request, context):
        id = int(request.id)

        with session_scope() as session:
            todo = session.query(Todo).get(id)
            if todo:
                if todo.status:
                    todo.status = 0
                    session.commit()
                    return todos_pb2.TodoResponse(
                        message="Status Changed to [INCOMPLETE]"
                    )

                todo.status = 1
                session.commit()
                return todos_pb2.TodoResponse(
                    message="Status Changed to [COMPLETE]"
                )

        return todos_pb2.TodoResponse(
            message="No Todo with specified ID found"
        )


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except(e):
        print(e)
        session.rollback()
        raise
    finally:
        session.close()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todos_pb2_grpc.add_TodoServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

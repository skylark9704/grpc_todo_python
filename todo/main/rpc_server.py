from contextlib import contextmanager
from concurrent import futures
from todo.db.models.Todo import Todo
from todo.db.db import Session
import grpc

from todo.rpcs import todos_pb2
from todo.rpcs import todos_pb2_grpc


class TodoService(todos_pb2_grpc.TodoServiceServicer):

    def __init__(self):
        pass

    def SaveTodo(self, request, context):
        todo = Todo(
            title=request.todo.title,
            description=request.todo.description,
        )

        status = todos_pb2.OperationErrors()

        with session_scope() as session:
            session.add(todo)
            status.code = todos_pb2.Status.Value('OK')
            return todos_pb2.TodoResponse(status=status)

    def ListTodo(self, request, context):
        id = request.id

        with session_scope() as session:
            row = session.query(Todo).get(id)
            status = todos_pb2.OperationErrors()
            if row:
                todo = todos_pb2.Todo()
                todo.id = row.id
                todo.title = row.title
                todo.description = row.description
                todo.status = row.status
                todo.created_at.FromDatetime(row.created),
                todo.updated_at.FromDatetime(row.updated)

                status.code = todos_pb2.Status.Value('OK')
                status.errors.extend(["OK"])

                return todos_pb2.TodoResponse(
                    todo=todo, status=status
                )
            else:
                status.code = todos_pb2.Status.Value('NOT_FOUND')
                status.errors.extend(
                    ["Specified ID does not Exist in the Database"]
                )
                return todos_pb2.TodoResponse(
                    status=status
                )

    def ListAllTodo(self, request, context):
        with session_scope() as session:
            todos = session.query(Todo).order_by(Todo.id)

            if not todos:
                status = todos_pb2.OperationErrors()
                status.code = todos_pb2.Status.Value('NOT_FOUND')
                status.errors.extend(
                    ["No Todo entries found in the Database"]
                )
                yield todos_pb2.ListAllTodoResponse(
                    status=status
                )

            else:
                for _todo in todos:
                    todo = todos_pb2.Todo()
                    todo.id = _todo.id
                    todo.title = _todo.title
                    todo.description = _todo.description
                    todo.status = _todo.status
                    todo.created_at.FromDatetime(_todo.created),
                    todo.updated_at.FromDatetime(_todo.updated)

                    yield todos_pb2.ListAllTodoResponse(
                        todo=todo
                    )

    def EditTodo(self, request, context):
        id = request.todo.id

        with session_scope() as session:
            todo = session.query(Todo).get(id)
            status = todos_pb2.OperationErrors()
            if todo:
                description, title = request.todo
                todo.title = todo.title if title == "" else title
                todo.description = todo.description if description == "" \
                    else description

                status.code = todos_pb2.Status.Value('UPDATED')
                status.errors.extend(
                    ["Successfully Updated Entry"]
                )

                return todos_pb2.TodoResponse(
                    status=status
                )
            status.code = todos_pb2.Status.Value('NOT_FOUND')
            status.errors.extend(
                ["Specified ID does not Exist in the Database"]
            )
            return todos_pb2.TodoResponse(
                status=status
            )

    def DeleteTodo(self, request, context):
        id = request.id

        with session_scope() as session:
            todo = session.query(Todo).get(id)
            status = todos_pb2.OperationErrors()
            if todo:
                session.delete(todo)
                status.code = todos_pb2.Status.Value('DELETED')
                return todos_pb2.TodoResponse(
                    status=status
                )
            else:
                status.code = todos_pb2.Status.Value('NOT_FOUND')
                status.errors.extend(
                    ["Specified ID does not Exist in the Database"]
                )
                return todos_pb2.TodoResponse(
                    status=status
                )

    def ToggleStatus(self, request, context):
        id = request.id
        with session_scope() as session:
            todo = session.query(Todo).get(id)
            status = todos_pb2.OperationErrors()
            if todo:
                status.code = todos_pb2.Status.Value('UPDATED')
                if todo.status:
                    todo.status = 0

                    return todos_pb2.TodoResponse(
                        status=status
                    )

                todo.status = 1

                return todos_pb2.TodoResponse(
                    status=status
                )
        status.code = todos_pb2.Status.Value('NOT_FOUND')
        status.errors.extend(
                    ["Specified ID does not Exist in the Database"]
                )
        return todos_pb2.TodoResponse(
            status=status
        )


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todos_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

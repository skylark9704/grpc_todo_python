from todo.rpcs import todos_pb2
from todo.database.models.Todo import Todo
from todo.database.connection import session_scope


class Server():

    def add(data):
        todo = Todo(
            title=data.title,
            description=data.description)

        status = todos_pb2.OperationErrors()

        with session_scope() as session:
            session.add(todo)
            status.code = todos_pb2.OK
            return todos_pb2.TodoResponse(status=status)

    def get(data):
        id = data.id

        with session_scope() as session:
            row = session.query(Todo).get(id)
            status = todos_pb2.OperationErrors()
            if row:
                todo = todos_pb2.Todo()
                todo.id = row.id
                todo.title = row.title
                todo.description = row.description
                todo.status = row.status
                todo.created_at.FromDatetime(row.created_at),
                todo.updated_at.FromDatetime(row.updated_at)
                status.code = todos_pb2.OK

                return todos_pb2.TodoResponse(
                    todo=todo, status=status
                )
            else:
                status.code = todos_pb2.NOT_FOUND
                status.errors.extend(
                    ["Specified ID does not Exist in the Database"]
                )
                return todos_pb2.TodoResponse(
                    status=status
                )

    def list_all():
        with session_scope() as session:
            count = session.query(Todo.id).count()

            if not count:
                status = todos_pb2.OperationErrors()
                status.code = todos_pb2.NOT_FOUND
                status.errors.extend(
                    ["No Todo entries found in the Database"]
                )

                yield todos_pb2.ListAllTodoResponse(
                    status=status
                )

            else:
                todos = session.query(Todo).order_by(Todo.id)

                for _todo in todos:
                    todo = todos_pb2.Todo()
                    todo.id = _todo.id
                    todo.title = _todo.title
                    todo.description = _todo.description
                    todo.status = _todo.status
                    todo.created_at.FromDatetime(_todo.created_at)
                    todo.updated_at.FromDatetime(_todo.updated_at)

                    yield todos_pb2.ListAllTodoResponse(
                        todo=todo
                    )

    def toggle_status(data):
        id = data.id
        with session_scope() as session:
            todo = session.query(Todo).get(id)
            status = todos_pb2.OperationErrors()
            if todo:
                status.code = todos_pb2.UPDATED
                status_options = {
                    0: todos_pb2.NEW,
                    1: todos_pb2.PROGRESS,
                    2: todos_pb2.COMPLETED
                }

                todo.status = status_options[data.status]

                return todos_pb2.TodoResponse(
                    status=status
                )

        status.code = todos_pb2.NOT_FOUND
        status.errors.extend(
            ["Specified ID does not Exist in the Database"]
        )
        return todos_pb2.TodoResponse(
            status=status
        )

    def edit(data):
        id = data.id

        with session_scope() as session:
            todo = session.query(Todo).get(id)
            status = todos_pb2.OperationErrors()
            if todo:
                description, title = data.description, data.title
                todo.title = todo.title if title == "" else title
                todo.description = todo.description if description == "" \
                    else description

                status.code = todos_pb2.UPDATED

                return todos_pb2.TodoResponse(
                    status=status
                )
            status.code = todos_pb2.NOT_FOUND
            status.errors.extend(
                ["Specified ID does not Exist in the Database"]
            )
            return todos_pb2.TodoResponse(
                status=status
            )

    def delete(data):
        id = data.id

        with session_scope() as session:
            todo = session.query(Todo).get(id)
            status = todos_pb2.OperationErrors()
            if todo:
                session.delete(todo)
                status.code = todos_pb2.DELETED
                return todos_pb2.TodoResponse(
                    status=status
                )
            else:
                status.code = todos_pb2.NOT_FOUND
                status.errors.extend(
                    ["Specified ID does not Exist in the Database"]
                )
                return todos_pb2.TodoResponse(
                    status=status
                )

    def test():
        pass

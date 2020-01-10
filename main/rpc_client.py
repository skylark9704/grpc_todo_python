import grpc
import todos_pb2
import todos_pb2_grpc


def app():

    print("""
    Todo Application [MENU]:
        1 - Create Todo
        2 - Get Todo By ID
        3 - List All Todos
        4 - Toggle Status of Todo [Input : id]
        5 - Edit Todo
        6 - Delete Todo By ID
    """)

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = todos_pb2_grpc.TodoServiceStub(channel)

        while True:
            choice = int(input('Choice : '))

            if choice == 0:
                break

            elif choice == 1:
                title = input("Enter Title : ")
                description = input("Enter Description : ")
                todo = todos_pb2.Todo()
                todo.title = title
                todo.description = description
                response = stub.SaveTodo(todos_pb2.SaveTodoRequest(
                    todo=todo
                ))
                print(response.status)

            elif choice == 2:
                id = int(input('Enter ID : '))
                response = stub.ListTodo(todos_pb2.ListTodoRequest(id=id))

                if response.status.code == todos_pb2.Status.Value('OK'):
                    print(format_todo(response.todo))

                elif response.status.code == todos_pb2.Status.Value(
                    'NOT_FOUND'
                ):
                    print(response.status.code, response.status.errors)

            elif choice == 3:
                todos = stub.ListAllTodo(todos_pb2.ListAllTodoRequest())
                for todo in todos:
                    if todo.todo:
                        print(format_todo(todo.todo))
                    else:
                        print(todo.status.code)
                        print(todo.status.errors)

            elif choice == 4:
                id = int(input('Enter ID : '))
                response = stub.ToggleStatus(
                    todos_pb2.ToggleStatusRequest(id=id))
                print(response.status)

            elif choice == 5:
                id = int(input('Enter ID : '))
                title = input('Title : ')
                description = input('Description : ')
                todo = todos_pb2.Todo()
                todo.id = id
                todo.title = title
                todo.description = description
                response = stub.EditTodo(
                    todos_pb2.EditTodoRequest(
                        todo=todo
                    )
                )
                print(response.status)

            elif choice == 6:
                id = int(input('Enter ID : '))
                response = stub.DeleteTodo(todos_pb2.DeleteTodoRequest(id=id))
                print(response.status)


def format_todo(todo):
    return """
    {}. {}, [{}] | Date : {} | Last Updt : {}
    _______________________________

    {}
    """.format(
        todo.id,
        todo.title,
        "Completed" if todo.status == 1 else "Incomplete",
        todo.created_at.ToDatetime(),
        todo.updated_at.ToDatetime(),
        todo.description
    )


if __name__ == '__main__':
    app()

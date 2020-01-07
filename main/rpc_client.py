import grpc
import json
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
        stub = todos_pb2_grpc.TodoStub(channel)

        while True:
            choice = int(input('Choice : '))

            if choice == 0:
                break

            elif choice == 1:
                title = input("Enter Title : ")
                description = input("Enter Description : ")
                response = stub.SaveTodo(todos_pb2.SaveTodoRequest(
                    title=title,
                    description=description
                ))
                print(response.message)

            elif choice == 2:
                _id = input('Enter ID : ')
                response = stub.ListTodo(todos_pb2.ListTodoRequest(id=_id))

                if response.data:
                    print(format_todo(response.data))
                else:
                    print(response.message)

            elif choice == 3:
                todos = stub.ListAllTodo(todos_pb2.ListAllTodoRequest())
                for todo in todos:
                    if todo.data:
                        print(format_todo(todo.data))
                    else:
                        print(todo.message)

            elif choice == 4:
                _id = input('Enter ID : ')
                response = stub.ToggleStatus(
                    todos_pb2.ToggleStatusRequest(id=_id))
                print(response.message)

            elif choice == 5:
                _id = input('Enter ID : ')
                title = input('Title : ')
                description = input('Description : ')
                response = stub.EditTodo(
                    todos_pb2.EditTodoRequest(
                        id=_id,
                        title=title,
                        description=description
                    )
                )
                print(response.message)

            elif choice == 6:
                _id = input('Enter ID : ')
                response = stub.DeleteTodo(todos_pb2.DeleteTodoRequest(id=_id))
                print(response.message)


def format_todo(todo):
    formatted_todo = json.loads(todo)
    print('Format TODO')
    return """
    {}. {}, [{}] | Date : {}
    _______________________________

    {}
    """.format(
        formatted_todo["id"],
        formatted_todo["title"],
        formatted_todo["status"],
        formatted_todo["date"],
        formatted_todo["description"]
    )


if __name__ == '__main__':
    app()

from todo.rpcs import todos_pb2
from todo.lib.helpers import format_todo
from google.protobuf.json_format import MessageToDict


class Client():

    def __init__(self, stub):
        self.stub = stub

    def display_menu(self):
        print("""
        Todo Application [MENU]:
            1 - Create Todo
            2 - Get Todo By ID
            3 - List All Todos
            4 - Toggle Status of Todo [Input : id]
            5 - Edit Todo
            6 - Delete Todo By ID
        """)

    def add(self):
        todo = todos_pb2.Todo()
        todo.title = input("Enter Title : ")
        todo.description = input("Enter Description : ")
        response = self.stub.AddTodo(todo)
        print(response)

    def get(self):
        todo = todos_pb2.Todo()
        todo.id = int(input('Enter ID : '))
        response = self.stub.GetTodo(todo)

        if response.status.code == todos_pb2.OK:
            print(format_todo(response.todo), response.status)

        elif response.status.code == todos_pb2.NOT_FOUND:
            print(response.status)

    def list_all(self):
        response = self.stub.ListAllTodo(todos_pb2.EmptyRequest())
        for todo in response:
            todoDict = MessageToDict(todo.todo)
            if todoDict:
                print(format_todo(todo.todo))
            else:
                print(todo.status)

    def toggle_status(self):
        todo = todos_pb2.Todo()
        todo.id = int(input('Enter ID : '))
        status_options = {
            0: todos_pb2.NEW,
            1: todos_pb2.PROGRESS,
            2: todos_pb2.COMPLETED
        }

        print("0 - NEW | 1 - PROGRESS | 2 - COMPLETED")
        try:
            todo.status = status_options[int(input('Status : '))]
        except KeyError as e:
            print(f'Invalid Status : {e}, Use options defined in menu')
            return

        response = self.stub.ToggleStatus(todo)
        print(response.status)

    def edit(self):
        id = int(input('Enter ID : '))
        title = input('Title : ')
        description = input('Description : ')
        todo = todos_pb2.Todo()
        todo.id = id
        todo.title = title
        todo.description = description
        response = self.stub.EditTodo(todo)
        print(response.status)

    def delete(self):
        todo = todos_pb2.Todo()
        todo.id = int(input('Enter ID : '))
        response = self.stub.DeleteTodo(todo)
        print(response.status)

    def test(self):
        pass

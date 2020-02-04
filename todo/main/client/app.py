import grpc
from todo.rpcs import todos_pb2_grpc
from todo.main.client import Client


def client():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = todos_pb2_grpc.TodoServiceStub(channel)
        Todo = Client(stub)
        Todo.display_menu()

        while True:

            choice = int(input('Choice : '))

            options = {
                1: Todo.add,
                2: Todo.get,
                3: Todo.list_all,
                4: Todo.toggle_status,
                5: Todo.edit,
                6: Todo.delete,
                99: Todo.test
            }

            try:
                options[choice]()
            except KeyError as e:
                print(f'Invalid Option : {e}, Use options defined in menu')


if __name__ == '__main__':
    client()

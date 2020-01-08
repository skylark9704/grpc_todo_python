# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todos.proto',
  package='todo',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0btodos.proto\x12\x04todo\"E\n\x0fSaveTodoRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\"\x1d\n\x0fListTodoRequest\x12\n\n\x02id\x18\x01 \x01(\t\"1\n\x10ListTodoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"\x14\n\x12ListAllTodoRequest\"4\n\x13ListAllTodoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"\x1f\n\x11\x44\x65leteTodoRequest\x12\n\n\x02id\x18\x01 \x01(\t\"A\n\x0f\x45\x64itTodoRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"!\n\x13ToggleStatusRequest\x12\n\n\x02id\x18\x01 \x01(\t\"-\n\x0cTodoResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t2\xfb\x02\n\x04Todo\x12\x37\n\x08SaveTodo\x12\x15.todo.SaveTodoRequest\x1a\x12.todo.TodoResponse\"\x00\x12;\n\x08ListTodo\x12\x15.todo.ListTodoRequest\x1a\x16.todo.ListTodoResponse\"\x00\x12\x46\n\x0bListAllTodo\x12\x18.todo.ListAllTodoRequest\x1a\x19.todo.ListAllTodoResponse\"\x00\x30\x01\x12;\n\nDeleteTodo\x12\x17.todo.DeleteTodoRequest\x1a\x12.todo.TodoResponse\"\x00\x12\x37\n\x08\x45\x64itTodo\x12\x15.todo.EditTodoRequest\x1a\x12.todo.TodoResponse\"\x00\x12?\n\x0cToggleStatus\x12\x19.todo.ToggleStatusRequest\x1a\x12.todo.TodoResponse\"\x00\x62\x06proto3')
)




_SAVETODOREQUEST = _descriptor.Descriptor(
  name='SaveTodoRequest',
  full_name='todo.SaveTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='todo.SaveTodoRequest.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='todo.SaveTodoRequest.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='todo.SaveTodoRequest.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=90,
)


_LISTTODOREQUEST = _descriptor.Descriptor(
  name='ListTodoRequest',
  full_name='todo.ListTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.ListTodoRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=121,
)


_LISTTODORESPONSE = _descriptor.Descriptor(
  name='ListTodoResponse',
  full_name='todo.ListTodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='todo.ListTodoResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='todo.ListTodoResponse.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=172,
)


_LISTALLTODOREQUEST = _descriptor.Descriptor(
  name='ListAllTodoRequest',
  full_name='todo.ListAllTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=194,
)


_LISTALLTODORESPONSE = _descriptor.Descriptor(
  name='ListAllTodoResponse',
  full_name='todo.ListAllTodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='todo.ListAllTodoResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='todo.ListAllTodoResponse.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=248,
)


_DELETETODOREQUEST = _descriptor.Descriptor(
  name='DeleteTodoRequest',
  full_name='todo.DeleteTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.DeleteTodoRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=281,
)


_EDITTODOREQUEST = _descriptor.Descriptor(
  name='EditTodoRequest',
  full_name='todo.EditTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.EditTodoRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='todo.EditTodoRequest.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='todo.EditTodoRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=348,
)


_TOGGLESTATUSREQUEST = _descriptor.Descriptor(
  name='ToggleStatusRequest',
  full_name='todo.ToggleStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='todo.ToggleStatusRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=383,
)


_TODORESPONSE = _descriptor.Descriptor(
  name='TodoResponse',
  full_name='todo.TodoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='todo.TodoResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='todo.TodoResponse.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=430,
)

DESCRIPTOR.message_types_by_name['SaveTodoRequest'] = _SAVETODOREQUEST
DESCRIPTOR.message_types_by_name['ListTodoRequest'] = _LISTTODOREQUEST
DESCRIPTOR.message_types_by_name['ListTodoResponse'] = _LISTTODORESPONSE
DESCRIPTOR.message_types_by_name['ListAllTodoRequest'] = _LISTALLTODOREQUEST
DESCRIPTOR.message_types_by_name['ListAllTodoResponse'] = _LISTALLTODORESPONSE
DESCRIPTOR.message_types_by_name['DeleteTodoRequest'] = _DELETETODOREQUEST
DESCRIPTOR.message_types_by_name['EditTodoRequest'] = _EDITTODOREQUEST
DESCRIPTOR.message_types_by_name['ToggleStatusRequest'] = _TOGGLESTATUSREQUEST
DESCRIPTOR.message_types_by_name['TodoResponse'] = _TODORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SaveTodoRequest = _reflection.GeneratedProtocolMessageType('SaveTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAVETODOREQUEST,
  '__module__' : 'todos_pb2'
  # @@protoc_insertion_point(class_scope:todo.SaveTodoRequest)
  })
_sym_db.RegisterMessage(SaveTodoRequest)

ListTodoRequest = _reflection.GeneratedProtocolMessageType('ListTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTODOREQUEST,
  '__module__' : 'todos_pb2'
  # @@protoc_insertion_point(class_scope:todo.ListTodoRequest)
  })
_sym_db.RegisterMessage(ListTodoRequest)

ListTodoResponse = _reflection.GeneratedProtocolMessageType('ListTodoResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTODORESPONSE,
  '__module__' : 'todos_pb2'
  # @@protoc_insertion_point(class_scope:todo.ListTodoResponse)
  })
_sym_db.RegisterMessage(ListTodoResponse)

ListAllTodoRequest = _reflection.GeneratedProtocolMessageType('ListAllTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTALLTODOREQUEST,
  '__module__' : 'todos_pb2'
  # @@protoc_insertion_point(class_scope:todo.ListAllTodoRequest)
  })
_sym_db.RegisterMessage(ListAllTodoRequest)

ListAllTodoResponse = _reflection.GeneratedProtocolMessageType('ListAllTodoResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTALLTODORESPONSE,
  '__module__' : 'todos_pb2'
  # @@protoc_insertion_point(class_scope:todo.ListAllTodoResponse)
  })
_sym_db.RegisterMessage(ListAllTodoResponse)

DeleteTodoRequest = _reflection.GeneratedProtocolMessageType('DeleteTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETODOREQUEST,
  '__module__' : 'todos_pb2'
  # @@protoc_insertion_point(class_scope:todo.DeleteTodoRequest)
  })
_sym_db.RegisterMessage(DeleteTodoRequest)

EditTodoRequest = _reflection.GeneratedProtocolMessageType('EditTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _EDITTODOREQUEST,
  '__module__' : 'todos_pb2'
  # @@protoc_insertion_point(class_scope:todo.EditTodoRequest)
  })
_sym_db.RegisterMessage(EditTodoRequest)

ToggleStatusRequest = _reflection.GeneratedProtocolMessageType('ToggleStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOGGLESTATUSREQUEST,
  '__module__' : 'todos_pb2'
  # @@protoc_insertion_point(class_scope:todo.ToggleStatusRequest)
  })
_sym_db.RegisterMessage(ToggleStatusRequest)

TodoResponse = _reflection.GeneratedProtocolMessageType('TodoResponse', (_message.Message,), {
  'DESCRIPTOR' : _TODORESPONSE,
  '__module__' : 'todos_pb2'
  # @@protoc_insertion_point(class_scope:todo.TodoResponse)
  })
_sym_db.RegisterMessage(TodoResponse)



_TODO = _descriptor.ServiceDescriptor(
  name='Todo',
  full_name='todo.Todo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=433,
  serialized_end=812,
  methods=[
  _descriptor.MethodDescriptor(
    name='SaveTodo',
    full_name='todo.Todo.SaveTodo',
    index=0,
    containing_service=None,
    input_type=_SAVETODOREQUEST,
    output_type=_TODORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListTodo',
    full_name='todo.Todo.ListTodo',
    index=1,
    containing_service=None,
    input_type=_LISTTODOREQUEST,
    output_type=_LISTTODORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListAllTodo',
    full_name='todo.Todo.ListAllTodo',
    index=2,
    containing_service=None,
    input_type=_LISTALLTODOREQUEST,
    output_type=_LISTALLTODORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTodo',
    full_name='todo.Todo.DeleteTodo',
    index=3,
    containing_service=None,
    input_type=_DELETETODOREQUEST,
    output_type=_TODORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EditTodo',
    full_name='todo.Todo.EditTodo',
    index=4,
    containing_service=None,
    input_type=_EDITTODOREQUEST,
    output_type=_TODORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ToggleStatus',
    full_name='todo.Todo.ToggleStatus',
    index=5,
    containing_service=None,
    input_type=_TOGGLESTATUSREQUEST,
    output_type=_TODORESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODO)

DESCRIPTOR.services_by_name['Todo'] = _TODO

# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logging.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='logging.proto',
  package='logging',
  syntax='proto3',
  serialized_pb=_b('\n\rlogging.proto\x12\x07logging\"?\n\x07\x46\x61ilure\x12\x10\n\x08latitude\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\tb\x06proto3')
)




_FAILURE = _descriptor.Descriptor(
  name='Failure',
  full_name='logging.Failure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='logging.Failure.latitude', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='logging.Failure.longitude', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='logging.Failure.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['Failure'] = _FAILURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Failure = _reflection.GeneratedProtocolMessageType('Failure', (_message.Message,), dict(
  DESCRIPTOR = _FAILURE,
  __module__ = 'logging_pb2'
  # @@protoc_insertion_point(class_scope:logging.Failure)
  ))
_sym_db.RegisterMessage(Failure)


# @@protoc_insertion_point(module_scope)
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/transport/internet/http/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/transport/internet/http/config.proto',
  package='v2ray.core.transport.internet.http',
  syntax='proto3',
  serialized_options=_b('\n&com.v2ray.core.transport.internet.httpP\001Z\004http\252\002\"V2Ray.Core.Transport.Internet.Http'),
  serialized_pb=_b('\n3v2ray.com/core/transport/internet/http/config.proto\x12\"v2ray.core.transport.internet.http\"$\n\x06\x43onfig\x12\x0c\n\x04host\x18\x01 \x03(\t\x12\x0c\n\x04path\x18\x02 \x01(\tBU\n&com.v2ray.core.transport.internet.httpP\x01Z\x04http\xaa\x02\"V2Ray.Core.Transport.Internet.Httpb\x06proto3')
)




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.transport.internet.http.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='v2ray.core.transport.internet.http.Config.host', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='v2ray.core.transport.internet.http.Config.path', index=1,
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
  serialized_start=91,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'v2ray.com.core.transport.internet.http.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.http.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

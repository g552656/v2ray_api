# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/app/proxyman/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray.com.core.common.net import address_pb2 as v2ray_dot_com_dot_core_dot_common_dot_net_dot_address__pb2
from v2ray.com.core.common.net import port_pb2 as v2ray_dot_com_dot_core_dot_common_dot_net_dot_port__pb2
from v2ray.com.core.transport.internet import config_pb2 as v2ray_dot_com_dot_core_dot_transport_dot_internet_dot_config__pb2
from v2ray.com.core.common.serial import typed_message_pb2 as v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/app/proxyman/config.proto',
  package='v2ray.core.app.proxyman',
  syntax='proto3',
  serialized_options=_b('\n\033com.v2ray.core.app.proxymanP\001Z\010proxyman\252\002\027V2Ray.Core.App.Proxyman'),
  serialized_pb=_b('\n(v2ray.com/core/app/proxyman/config.proto\x12\x17v2ray.core.app.proxyman\x1a\'v2ray.com/core/common/net/address.proto\x1a$v2ray.com/core/common/net/port.proto\x1a.v2ray.com/core/transport/internet/config.proto\x1a\x30v2ray.com/core/common/serial/typed_message.proto\"\x0f\n\rInboundConfig\"\x96\x03\n\x12\x41llocationStrategy\x12>\n\x04type\x18\x01 \x01(\x0e\x32\x30.v2ray.core.app.proxyman.AllocationStrategy.Type\x12^\n\x0b\x63oncurrency\x18\x02 \x01(\x0b\x32I.v2ray.core.app.proxyman.AllocationStrategy.AllocationStrategyConcurrency\x12V\n\x07refresh\x18\x03 \x01(\x0b\x32\x45.v2ray.core.app.proxyman.AllocationStrategy.AllocationStrategyRefresh\x1a.\n\x1d\x41llocationStrategyConcurrency\x12\r\n\x05value\x18\x01 \x01(\r\x1a*\n\x19\x41llocationStrategyRefresh\x12\r\n\x05value\x18\x01 \x01(\r\",\n\x04Type\x12\n\n\x06\x41lways\x10\x00\x12\n\n\x06Random\x10\x01\x12\x0c\n\x08\x45xternal\x10\x02\"?\n\x0eSniffingConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x1c\n\x14\x64\x65stination_override\x18\x02 \x03(\t\"\xbf\x03\n\x0eReceiverConfig\x12\x34\n\nport_range\x18\x01 \x01(\x0b\x32 .v2ray.core.common.net.PortRange\x12\x31\n\x06listen\x18\x02 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12H\n\x13\x61llocation_strategy\x18\x03 \x01(\x0b\x32+.v2ray.core.app.proxyman.AllocationStrategy\x12\x44\n\x0fstream_settings\x18\x04 \x01(\x0b\x32+.v2ray.core.transport.internet.StreamConfig\x12$\n\x1creceive_original_destination\x18\x05 \x01(\x08\x12\x44\n\x0f\x64omain_override\x18\x07 \x03(\x0e\x32\'.v2ray.core.app.proxyman.KnownProtocolsB\x02\x18\x01\x12\x42\n\x11sniffing_settings\x18\x08 \x01(\x0b\x32\'.v2ray.core.app.proxyman.SniffingConfigJ\x04\x08\x06\x10\x07\"\xa6\x01\n\x14InboundHandlerConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x41\n\x11receiver_settings\x18\x02 \x01(\x0b\x32&.v2ray.core.common.serial.TypedMessage\x12>\n\x0eproxy_settings\x18\x03 \x01(\x0b\x32&.v2ray.core.common.serial.TypedMessage\"\x10\n\x0eOutboundConfig\"\x91\x02\n\x0cSenderConfig\x12.\n\x03via\x18\x01 \x01(\x0b\x32!.v2ray.core.common.net.IPOrDomain\x12\x44\n\x0fstream_settings\x18\x02 \x01(\x0b\x32+.v2ray.core.transport.internet.StreamConfig\x12\x42\n\x0eproxy_settings\x18\x03 \x01(\x0b\x32*.v2ray.core.transport.internet.ProxyConfig\x12G\n\x12multiplex_settings\x18\x04 \x01(\x0b\x32+.v2ray.core.app.proxyman.MultiplexingConfig\":\n\x12MultiplexingConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x13\n\x0b\x63oncurrency\x18\x02 \x01(\r*#\n\x0eKnownProtocols\x12\x08\n\x04HTTP\x10\x00\x12\x07\n\x03TLS\x10\x01\x42\x43\n\x1b\x63om.v2ray.core.app.proxymanP\x01Z\x08proxyman\xaa\x02\x17V2Ray.Core.App.Proxymanb\x06proto3')
  ,
  dependencies=[v2ray_dot_com_dot_core_dot_common_dot_net_dot_address__pb2.DESCRIPTOR,v2ray_dot_com_dot_core_dot_common_dot_net_dot_port__pb2.DESCRIPTOR,v2ray_dot_com_dot_core_dot_transport_dot_internet_dot_config__pb2.DESCRIPTOR,v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2.DESCRIPTOR,])

_KNOWNPROTOCOLS = _descriptor.EnumDescriptor(
  name='KnownProtocols',
  full_name='v2ray.core.app.proxyman.KnownProtocols',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HTTP', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TLS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1710,
  serialized_end=1745,
)
_sym_db.RegisterEnumDescriptor(_KNOWNPROTOCOLS)

KnownProtocols = enum_type_wrapper.EnumTypeWrapper(_KNOWNPROTOCOLS)
HTTP = 0
TLS = 1


_ALLOCATIONSTRATEGY_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='v2ray.core.app.proxyman.AllocationStrategy.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Always', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Random', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='External', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=626,
  serialized_end=670,
)
_sym_db.RegisterEnumDescriptor(_ALLOCATIONSTRATEGY_TYPE)


_INBOUNDCONFIG = _descriptor.Descriptor(
  name='InboundConfig',
  full_name='v2ray.core.app.proxyman.InboundConfig',
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
  serialized_start=246,
  serialized_end=261,
)


_ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYCONCURRENCY = _descriptor.Descriptor(
  name='AllocationStrategyConcurrency',
  full_name='v2ray.core.app.proxyman.AllocationStrategy.AllocationStrategyConcurrency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v2ray.core.app.proxyman.AllocationStrategy.AllocationStrategyConcurrency.value', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=534,
  serialized_end=580,
)

_ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYREFRESH = _descriptor.Descriptor(
  name='AllocationStrategyRefresh',
  full_name='v2ray.core.app.proxyman.AllocationStrategy.AllocationStrategyRefresh',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v2ray.core.app.proxyman.AllocationStrategy.AllocationStrategyRefresh.value', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=582,
  serialized_end=624,
)

_ALLOCATIONSTRATEGY = _descriptor.Descriptor(
  name='AllocationStrategy',
  full_name='v2ray.core.app.proxyman.AllocationStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='v2ray.core.app.proxyman.AllocationStrategy.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concurrency', full_name='v2ray.core.app.proxyman.AllocationStrategy.concurrency', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refresh', full_name='v2ray.core.app.proxyman.AllocationStrategy.refresh', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYCONCURRENCY, _ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYREFRESH, ],
  enum_types=[
    _ALLOCATIONSTRATEGY_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=670,
)


_SNIFFINGCONFIG = _descriptor.Descriptor(
  name='SniffingConfig',
  full_name='v2ray.core.app.proxyman.SniffingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='v2ray.core.app.proxyman.SniffingConfig.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_override', full_name='v2ray.core.app.proxyman.SniffingConfig.destination_override', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=672,
  serialized_end=735,
)


_RECEIVERCONFIG = _descriptor.Descriptor(
  name='ReceiverConfig',
  full_name='v2ray.core.app.proxyman.ReceiverConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port_range', full_name='v2ray.core.app.proxyman.ReceiverConfig.port_range', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='listen', full_name='v2ray.core.app.proxyman.ReceiverConfig.listen', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allocation_strategy', full_name='v2ray.core.app.proxyman.ReceiverConfig.allocation_strategy', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream_settings', full_name='v2ray.core.app.proxyman.ReceiverConfig.stream_settings', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receive_original_destination', full_name='v2ray.core.app.proxyman.ReceiverConfig.receive_original_destination', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_override', full_name='v2ray.core.app.proxyman.ReceiverConfig.domain_override', index=5,
      number=7, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sniffing_settings', full_name='v2ray.core.app.proxyman.ReceiverConfig.sniffing_settings', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=738,
  serialized_end=1185,
)


_INBOUNDHANDLERCONFIG = _descriptor.Descriptor(
  name='InboundHandlerConfig',
  full_name='v2ray.core.app.proxyman.InboundHandlerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='v2ray.core.app.proxyman.InboundHandlerConfig.tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver_settings', full_name='v2ray.core.app.proxyman.InboundHandlerConfig.receiver_settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proxy_settings', full_name='v2ray.core.app.proxyman.InboundHandlerConfig.proxy_settings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1188,
  serialized_end=1354,
)


_OUTBOUNDCONFIG = _descriptor.Descriptor(
  name='OutboundConfig',
  full_name='v2ray.core.app.proxyman.OutboundConfig',
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
  serialized_start=1356,
  serialized_end=1372,
)


_SENDERCONFIG = _descriptor.Descriptor(
  name='SenderConfig',
  full_name='v2ray.core.app.proxyman.SenderConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='via', full_name='v2ray.core.app.proxyman.SenderConfig.via', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream_settings', full_name='v2ray.core.app.proxyman.SenderConfig.stream_settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proxy_settings', full_name='v2ray.core.app.proxyman.SenderConfig.proxy_settings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiplex_settings', full_name='v2ray.core.app.proxyman.SenderConfig.multiplex_settings', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1375,
  serialized_end=1648,
)


_MULTIPLEXINGCONFIG = _descriptor.Descriptor(
  name='MultiplexingConfig',
  full_name='v2ray.core.app.proxyman.MultiplexingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='v2ray.core.app.proxyman.MultiplexingConfig.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concurrency', full_name='v2ray.core.app.proxyman.MultiplexingConfig.concurrency', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1650,
  serialized_end=1708,
)

_ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYCONCURRENCY.containing_type = _ALLOCATIONSTRATEGY
_ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYREFRESH.containing_type = _ALLOCATIONSTRATEGY
_ALLOCATIONSTRATEGY.fields_by_name['type'].enum_type = _ALLOCATIONSTRATEGY_TYPE
_ALLOCATIONSTRATEGY.fields_by_name['concurrency'].message_type = _ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYCONCURRENCY
_ALLOCATIONSTRATEGY.fields_by_name['refresh'].message_type = _ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYREFRESH
_ALLOCATIONSTRATEGY_TYPE.containing_type = _ALLOCATIONSTRATEGY
_RECEIVERCONFIG.fields_by_name['port_range'].message_type = v2ray_dot_com_dot_core_dot_common_dot_net_dot_port__pb2._PORTRANGE
_RECEIVERCONFIG.fields_by_name['listen'].message_type = v2ray_dot_com_dot_core_dot_common_dot_net_dot_address__pb2._IPORDOMAIN
_RECEIVERCONFIG.fields_by_name['allocation_strategy'].message_type = _ALLOCATIONSTRATEGY
_RECEIVERCONFIG.fields_by_name['stream_settings'].message_type = v2ray_dot_com_dot_core_dot_transport_dot_internet_dot_config__pb2._STREAMCONFIG
_RECEIVERCONFIG.fields_by_name['domain_override'].enum_type = _KNOWNPROTOCOLS
_RECEIVERCONFIG.fields_by_name['sniffing_settings'].message_type = _SNIFFINGCONFIG
_INBOUNDHANDLERCONFIG.fields_by_name['receiver_settings'].message_type = v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2._TYPEDMESSAGE
_INBOUNDHANDLERCONFIG.fields_by_name['proxy_settings'].message_type = v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2._TYPEDMESSAGE
_SENDERCONFIG.fields_by_name['via'].message_type = v2ray_dot_com_dot_core_dot_common_dot_net_dot_address__pb2._IPORDOMAIN
_SENDERCONFIG.fields_by_name['stream_settings'].message_type = v2ray_dot_com_dot_core_dot_transport_dot_internet_dot_config__pb2._STREAMCONFIG
_SENDERCONFIG.fields_by_name['proxy_settings'].message_type = v2ray_dot_com_dot_core_dot_transport_dot_internet_dot_config__pb2._PROXYCONFIG
_SENDERCONFIG.fields_by_name['multiplex_settings'].message_type = _MULTIPLEXINGCONFIG
DESCRIPTOR.message_types_by_name['InboundConfig'] = _INBOUNDCONFIG
DESCRIPTOR.message_types_by_name['AllocationStrategy'] = _ALLOCATIONSTRATEGY
DESCRIPTOR.message_types_by_name['SniffingConfig'] = _SNIFFINGCONFIG
DESCRIPTOR.message_types_by_name['ReceiverConfig'] = _RECEIVERCONFIG
DESCRIPTOR.message_types_by_name['InboundHandlerConfig'] = _INBOUNDHANDLERCONFIG
DESCRIPTOR.message_types_by_name['OutboundConfig'] = _OUTBOUNDCONFIG
DESCRIPTOR.message_types_by_name['SenderConfig'] = _SENDERCONFIG
DESCRIPTOR.message_types_by_name['MultiplexingConfig'] = _MULTIPLEXINGCONFIG
DESCRIPTOR.enum_types_by_name['KnownProtocols'] = _KNOWNPROTOCOLS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InboundConfig = _reflection.GeneratedProtocolMessageType('InboundConfig', (_message.Message,), {
  'DESCRIPTOR' : _INBOUNDCONFIG,
  '__module__' : 'v2ray.com.core.app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.InboundConfig)
  })
_sym_db.RegisterMessage(InboundConfig)

AllocationStrategy = _reflection.GeneratedProtocolMessageType('AllocationStrategy', (_message.Message,), {

  'AllocationStrategyConcurrency' : _reflection.GeneratedProtocolMessageType('AllocationStrategyConcurrency', (_message.Message,), {
    'DESCRIPTOR' : _ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYCONCURRENCY,
    '__module__' : 'v2ray.com.core.app.proxyman.config_pb2'
    # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.AllocationStrategy.AllocationStrategyConcurrency)
    })
  ,

  'AllocationStrategyRefresh' : _reflection.GeneratedProtocolMessageType('AllocationStrategyRefresh', (_message.Message,), {
    'DESCRIPTOR' : _ALLOCATIONSTRATEGY_ALLOCATIONSTRATEGYREFRESH,
    '__module__' : 'v2ray.com.core.app.proxyman.config_pb2'
    # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.AllocationStrategy.AllocationStrategyRefresh)
    })
  ,
  'DESCRIPTOR' : _ALLOCATIONSTRATEGY,
  '__module__' : 'v2ray.com.core.app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.AllocationStrategy)
  })
_sym_db.RegisterMessage(AllocationStrategy)
_sym_db.RegisterMessage(AllocationStrategy.AllocationStrategyConcurrency)
_sym_db.RegisterMessage(AllocationStrategy.AllocationStrategyRefresh)

SniffingConfig = _reflection.GeneratedProtocolMessageType('SniffingConfig', (_message.Message,), {
  'DESCRIPTOR' : _SNIFFINGCONFIG,
  '__module__' : 'v2ray.com.core.app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.SniffingConfig)
  })
_sym_db.RegisterMessage(SniffingConfig)

ReceiverConfig = _reflection.GeneratedProtocolMessageType('ReceiverConfig', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVERCONFIG,
  '__module__' : 'v2ray.com.core.app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.ReceiverConfig)
  })
_sym_db.RegisterMessage(ReceiverConfig)

InboundHandlerConfig = _reflection.GeneratedProtocolMessageType('InboundHandlerConfig', (_message.Message,), {
  'DESCRIPTOR' : _INBOUNDHANDLERCONFIG,
  '__module__' : 'v2ray.com.core.app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.InboundHandlerConfig)
  })
_sym_db.RegisterMessage(InboundHandlerConfig)

OutboundConfig = _reflection.GeneratedProtocolMessageType('OutboundConfig', (_message.Message,), {
  'DESCRIPTOR' : _OUTBOUNDCONFIG,
  '__module__' : 'v2ray.com.core.app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.OutboundConfig)
  })
_sym_db.RegisterMessage(OutboundConfig)

SenderConfig = _reflection.GeneratedProtocolMessageType('SenderConfig', (_message.Message,), {
  'DESCRIPTOR' : _SENDERCONFIG,
  '__module__' : 'v2ray.com.core.app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.SenderConfig)
  })
_sym_db.RegisterMessage(SenderConfig)

MultiplexingConfig = _reflection.GeneratedProtocolMessageType('MultiplexingConfig', (_message.Message,), {
  'DESCRIPTOR' : _MULTIPLEXINGCONFIG,
  '__module__' : 'v2ray.com.core.app.proxyman.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.proxyman.MultiplexingConfig)
  })
_sym_db.RegisterMessage(MultiplexingConfig)


DESCRIPTOR._options = None
_RECEIVERCONFIG.fields_by_name['domain_override']._options = None
# @@protoc_insertion_point(module_scope)

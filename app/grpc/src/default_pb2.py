# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: default.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rdefault.proto\"\x1f\n\x0eIsAliveRequest\x12\r\n\x05\x63heck\x18\x01 \x01(\x08\"!\n\x0fIsAliveResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x62\x06proto3')



_ISALIVEREQUEST = DESCRIPTOR.message_types_by_name['IsAliveRequest']
_ISALIVERESPONSE = DESCRIPTOR.message_types_by_name['IsAliveResponse']
IsAliveRequest = _reflection.GeneratedProtocolMessageType('IsAliveRequest', (_message.Message,), {
  'DESCRIPTOR' : _ISALIVEREQUEST,
  '__module__' : 'default_pb2'
  # @@protoc_insertion_point(class_scope:IsAliveRequest)
  })
_sym_db.RegisterMessage(IsAliveRequest)

IsAliveResponse = _reflection.GeneratedProtocolMessageType('IsAliveResponse', (_message.Message,), {
  'DESCRIPTOR' : _ISALIVERESPONSE,
  '__module__' : 'default_pb2'
  # @@protoc_insertion_point(class_scope:IsAliveResponse)
  })
_sym_db.RegisterMessage(IsAliveResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ISALIVEREQUEST._serialized_start=17
  _ISALIVEREQUEST._serialized_end=48
  _ISALIVERESPONSE._serialized_start=50
  _ISALIVERESPONSE._serialized_end=83
# @@protoc_insertion_point(module_scope)

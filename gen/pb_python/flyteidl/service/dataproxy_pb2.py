# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/service/dataproxy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2
from flyteidl.core import literals_pb2 as flyteidl_dot_core_dot_literals__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/service/dataproxy.proto',
  package='flyteidl.service',
  syntax='proto3',
  serialized_options=_b('Z7github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/service'),
  serialized_pb=_b('\n flyteidl/service/dataproxy.proto\x12\x10\x66lyteidl.service\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1e\x66lyteidl/core/identifier.proto\x1a\x1c\x66lyteidl/core/literals.proto\"v\n\x1c\x43reateUploadLocationResponse\x12\x12\n\nsigned_url\x18\x01 \x01(\t\x12\x12\n\nnative_url\x18\x02 \x01(\t\x12.\n\nexpires_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x94\x01\n\x1b\x43reateUploadLocationRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x10\n\x08\x66ilename\x18\x03 \x01(\t\x12-\n\nexpires_in\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x13\n\x0b\x63ontent_md5\x18\x05 \x01(\x0c\"f\n\x1d\x43reateDownloadLocationRequest\x12\x12\n\nnative_url\x18\x01 \x01(\t\x12-\n\nexpires_in\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration:\x02\x18\x01\"h\n\x1e\x43reateDownloadLocationResponse\x12\x12\n\nsigned_url\x18\x01 \x01(\t\x12.\n\nexpires_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp:\x02\x18\x01\"\xd0\x01\n\x19\x43reateDownloadLinkRequest\x12\x35\n\rartifact_type\x18\x01 \x01(\x0e\x32\x1e.flyteidl.service.ArtifactType\x12-\n\nexpires_in\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x43\n\x11node_execution_id\x18\x03 \x01(\x0b\x32&.flyteidl.core.NodeExecutionIdentifierH\x00\x42\x08\n\x06source\"\xa2\x01\n\x1a\x43reateDownloadLinkResponse\x12\x16\n\nsigned_url\x18\x01 \x03(\tB\x02\x18\x01\x12\x32\n\nexpires_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01\x12\x38\n\x0fpre_signed_urls\x18\x03 \x01(\x0b\x32\x1f.flyteidl.service.PreSignedURLs\"S\n\rPreSignedURLs\x12\x12\n\nsigned_url\x18\x01 \x03(\t\x12.\n\nexpires_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"#\n\x0eGetDataRequest\x12\x11\n\tflyte_url\x18\x01 \x01(\t\"\x87\x01\n\x0fGetDataResponse\x12\x30\n\x0bliteral_map\x18\x01 \x01(\x0b\x32\x19.flyteidl.core.LiteralMapH\x00\x12:\n\x0fpre_signed_urls\x18\x02 \x01(\x0b\x32\x1f.flyteidl.service.PreSignedURLsH\x00\x42\x06\n\x04\x64\x61ta*C\n\x0c\x41rtifactType\x12\x1b\n\x17\x41RTIFACT_TYPE_UNDEFINED\x10\x00\x12\x16\n\x12\x41RTIFACT_TYPE_DECK\x10\x01\x32\xe2\x04\n\x10\x44\x61taProxyService\x12\xa0\x01\n\x14\x43reateUploadLocation\x12-.flyteidl.service.CreateUploadLocationRequest\x1a..flyteidl.service.CreateUploadLocationResponse\")\x82\xd3\xe4\x93\x02#\"\x1e/api/v1/dataproxy/artifact_urn:\x01*\x12\xa6\x01\n\x16\x43reateDownloadLocation\x12/.flyteidl.service.CreateDownloadLocationRequest\x1a\x30.flyteidl.service.CreateDownloadLocationResponse\")\x88\x02\x01\x82\xd3\xe4\x93\x02 \x12\x1e/api/v1/dataproxy/artifact_urn\x12\x9b\x01\n\x12\x43reateDownloadLink\x12+.flyteidl.service.CreateDownloadLinkRequest\x1a,.flyteidl.service.CreateDownloadLinkResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/api/v1/dataproxy/artifact_link:\x01*\x12\x64\n\x07GetData\x12 .flyteidl.service.GetDataRequest\x1a!.flyteidl.service.GetDataResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/api/v1/dataB9Z7github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/serviceb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,flyteidl_dot_core_dot_identifier__pb2.DESCRIPTOR,flyteidl_dot_core_dot_literals__pb2.DESCRIPTOR,])

_ARTIFACTTYPE = _descriptor.EnumDescriptor(
  name='ArtifactType',
  full_name='flyteidl.service.ArtifactType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ARTIFACT_TYPE_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARTIFACT_TYPE_DECK', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1328,
  serialized_end=1395,
)
_sym_db.RegisterEnumDescriptor(_ARTIFACTTYPE)

ArtifactType = enum_type_wrapper.EnumTypeWrapper(_ARTIFACTTYPE)
ARTIFACT_TYPE_UNDEFINED = 0
ARTIFACT_TYPE_DECK = 1



_CREATEUPLOADLOCATIONRESPONSE = _descriptor.Descriptor(
  name='CreateUploadLocationResponse',
  full_name='flyteidl.service.CreateUploadLocationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signed_url', full_name='flyteidl.service.CreateUploadLocationResponse.signed_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='native_url', full_name='flyteidl.service.CreateUploadLocationResponse.native_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires_at', full_name='flyteidl.service.CreateUploadLocationResponse.expires_at', index=2,
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
  serialized_start=211,
  serialized_end=329,
)


_CREATEUPLOADLOCATIONREQUEST = _descriptor.Descriptor(
  name='CreateUploadLocationRequest',
  full_name='flyteidl.service.CreateUploadLocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='flyteidl.service.CreateUploadLocationRequest.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='flyteidl.service.CreateUploadLocationRequest.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='flyteidl.service.CreateUploadLocationRequest.filename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires_in', full_name='flyteidl.service.CreateUploadLocationRequest.expires_in', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_md5', full_name='flyteidl.service.CreateUploadLocationRequest.content_md5', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=332,
  serialized_end=480,
)


_CREATEDOWNLOADLOCATIONREQUEST = _descriptor.Descriptor(
  name='CreateDownloadLocationRequest',
  full_name='flyteidl.service.CreateDownloadLocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='native_url', full_name='flyteidl.service.CreateDownloadLocationRequest.native_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires_in', full_name='flyteidl.service.CreateDownloadLocationRequest.expires_in', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('\030\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=482,
  serialized_end=584,
)


_CREATEDOWNLOADLOCATIONRESPONSE = _descriptor.Descriptor(
  name='CreateDownloadLocationResponse',
  full_name='flyteidl.service.CreateDownloadLocationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signed_url', full_name='flyteidl.service.CreateDownloadLocationResponse.signed_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires_at', full_name='flyteidl.service.CreateDownloadLocationResponse.expires_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=_b('\030\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=586,
  serialized_end=690,
)


_CREATEDOWNLOADLINKREQUEST = _descriptor.Descriptor(
  name='CreateDownloadLinkRequest',
  full_name='flyteidl.service.CreateDownloadLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='artifact_type', full_name='flyteidl.service.CreateDownloadLinkRequest.artifact_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires_in', full_name='flyteidl.service.CreateDownloadLinkRequest.expires_in', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_execution_id', full_name='flyteidl.service.CreateDownloadLinkRequest.node_execution_id', index=2,
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
    _descriptor.OneofDescriptor(
      name='source', full_name='flyteidl.service.CreateDownloadLinkRequest.source',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=693,
  serialized_end=901,
)


_CREATEDOWNLOADLINKRESPONSE = _descriptor.Descriptor(
  name='CreateDownloadLinkResponse',
  full_name='flyteidl.service.CreateDownloadLinkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signed_url', full_name='flyteidl.service.CreateDownloadLinkResponse.signed_url', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires_at', full_name='flyteidl.service.CreateDownloadLinkResponse.expires_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pre_signed_urls', full_name='flyteidl.service.CreateDownloadLinkResponse.pre_signed_urls', index=2,
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
  serialized_start=904,
  serialized_end=1066,
)


_PRESIGNEDURLS = _descriptor.Descriptor(
  name='PreSignedURLs',
  full_name='flyteidl.service.PreSignedURLs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signed_url', full_name='flyteidl.service.PreSignedURLs.signed_url', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires_at', full_name='flyteidl.service.PreSignedURLs.expires_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1068,
  serialized_end=1151,
)


_GETDATAREQUEST = _descriptor.Descriptor(
  name='GetDataRequest',
  full_name='flyteidl.service.GetDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flyte_url', full_name='flyteidl.service.GetDataRequest.flyte_url', index=0,
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
  serialized_start=1153,
  serialized_end=1188,
)


_GETDATARESPONSE = _descriptor.Descriptor(
  name='GetDataResponse',
  full_name='flyteidl.service.GetDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='literal_map', full_name='flyteidl.service.GetDataResponse.literal_map', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pre_signed_urls', full_name='flyteidl.service.GetDataResponse.pre_signed_urls', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='data', full_name='flyteidl.service.GetDataResponse.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1191,
  serialized_end=1326,
)

_CREATEUPLOADLOCATIONRESPONSE.fields_by_name['expires_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CREATEUPLOADLOCATIONREQUEST.fields_by_name['expires_in'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CREATEDOWNLOADLOCATIONREQUEST.fields_by_name['expires_in'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CREATEDOWNLOADLOCATIONRESPONSE.fields_by_name['expires_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CREATEDOWNLOADLINKREQUEST.fields_by_name['artifact_type'].enum_type = _ARTIFACTTYPE
_CREATEDOWNLOADLINKREQUEST.fields_by_name['expires_in'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CREATEDOWNLOADLINKREQUEST.fields_by_name['node_execution_id'].message_type = flyteidl_dot_core_dot_identifier__pb2._NODEEXECUTIONIDENTIFIER
_CREATEDOWNLOADLINKREQUEST.oneofs_by_name['source'].fields.append(
  _CREATEDOWNLOADLINKREQUEST.fields_by_name['node_execution_id'])
_CREATEDOWNLOADLINKREQUEST.fields_by_name['node_execution_id'].containing_oneof = _CREATEDOWNLOADLINKREQUEST.oneofs_by_name['source']
_CREATEDOWNLOADLINKRESPONSE.fields_by_name['expires_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CREATEDOWNLOADLINKRESPONSE.fields_by_name['pre_signed_urls'].message_type = _PRESIGNEDURLS
_PRESIGNEDURLS.fields_by_name['expires_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETDATARESPONSE.fields_by_name['literal_map'].message_type = flyteidl_dot_core_dot_literals__pb2._LITERALMAP
_GETDATARESPONSE.fields_by_name['pre_signed_urls'].message_type = _PRESIGNEDURLS
_GETDATARESPONSE.oneofs_by_name['data'].fields.append(
  _GETDATARESPONSE.fields_by_name['literal_map'])
_GETDATARESPONSE.fields_by_name['literal_map'].containing_oneof = _GETDATARESPONSE.oneofs_by_name['data']
_GETDATARESPONSE.oneofs_by_name['data'].fields.append(
  _GETDATARESPONSE.fields_by_name['pre_signed_urls'])
_GETDATARESPONSE.fields_by_name['pre_signed_urls'].containing_oneof = _GETDATARESPONSE.oneofs_by_name['data']
DESCRIPTOR.message_types_by_name['CreateUploadLocationResponse'] = _CREATEUPLOADLOCATIONRESPONSE
DESCRIPTOR.message_types_by_name['CreateUploadLocationRequest'] = _CREATEUPLOADLOCATIONREQUEST
DESCRIPTOR.message_types_by_name['CreateDownloadLocationRequest'] = _CREATEDOWNLOADLOCATIONREQUEST
DESCRIPTOR.message_types_by_name['CreateDownloadLocationResponse'] = _CREATEDOWNLOADLOCATIONRESPONSE
DESCRIPTOR.message_types_by_name['CreateDownloadLinkRequest'] = _CREATEDOWNLOADLINKREQUEST
DESCRIPTOR.message_types_by_name['CreateDownloadLinkResponse'] = _CREATEDOWNLOADLINKRESPONSE
DESCRIPTOR.message_types_by_name['PreSignedURLs'] = _PRESIGNEDURLS
DESCRIPTOR.message_types_by_name['GetDataRequest'] = _GETDATAREQUEST
DESCRIPTOR.message_types_by_name['GetDataResponse'] = _GETDATARESPONSE
DESCRIPTOR.enum_types_by_name['ArtifactType'] = _ARTIFACTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateUploadLocationResponse = _reflection.GeneratedProtocolMessageType('CreateUploadLocationResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUPLOADLOCATIONRESPONSE,
  __module__ = 'flyteidl.service.dataproxy_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.service.CreateUploadLocationResponse)
  ))
_sym_db.RegisterMessage(CreateUploadLocationResponse)

CreateUploadLocationRequest = _reflection.GeneratedProtocolMessageType('CreateUploadLocationRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUPLOADLOCATIONREQUEST,
  __module__ = 'flyteidl.service.dataproxy_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.service.CreateUploadLocationRequest)
  ))
_sym_db.RegisterMessage(CreateUploadLocationRequest)

CreateDownloadLocationRequest = _reflection.GeneratedProtocolMessageType('CreateDownloadLocationRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEDOWNLOADLOCATIONREQUEST,
  __module__ = 'flyteidl.service.dataproxy_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.service.CreateDownloadLocationRequest)
  ))
_sym_db.RegisterMessage(CreateDownloadLocationRequest)

CreateDownloadLocationResponse = _reflection.GeneratedProtocolMessageType('CreateDownloadLocationResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEDOWNLOADLOCATIONRESPONSE,
  __module__ = 'flyteidl.service.dataproxy_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.service.CreateDownloadLocationResponse)
  ))
_sym_db.RegisterMessage(CreateDownloadLocationResponse)

CreateDownloadLinkRequest = _reflection.GeneratedProtocolMessageType('CreateDownloadLinkRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEDOWNLOADLINKREQUEST,
  __module__ = 'flyteidl.service.dataproxy_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.service.CreateDownloadLinkRequest)
  ))
_sym_db.RegisterMessage(CreateDownloadLinkRequest)

CreateDownloadLinkResponse = _reflection.GeneratedProtocolMessageType('CreateDownloadLinkResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEDOWNLOADLINKRESPONSE,
  __module__ = 'flyteidl.service.dataproxy_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.service.CreateDownloadLinkResponse)
  ))
_sym_db.RegisterMessage(CreateDownloadLinkResponse)

PreSignedURLs = _reflection.GeneratedProtocolMessageType('PreSignedURLs', (_message.Message,), dict(
  DESCRIPTOR = _PRESIGNEDURLS,
  __module__ = 'flyteidl.service.dataproxy_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.service.PreSignedURLs)
  ))
_sym_db.RegisterMessage(PreSignedURLs)

GetDataRequest = _reflection.GeneratedProtocolMessageType('GetDataRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETDATAREQUEST,
  __module__ = 'flyteidl.service.dataproxy_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.service.GetDataRequest)
  ))
_sym_db.RegisterMessage(GetDataRequest)

GetDataResponse = _reflection.GeneratedProtocolMessageType('GetDataResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETDATARESPONSE,
  __module__ = 'flyteidl.service.dataproxy_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.service.GetDataResponse)
  ))
_sym_db.RegisterMessage(GetDataResponse)


DESCRIPTOR._options = None
_CREATEDOWNLOADLOCATIONREQUEST._options = None
_CREATEDOWNLOADLOCATIONRESPONSE._options = None
_CREATEDOWNLOADLINKRESPONSE.fields_by_name['signed_url']._options = None
_CREATEDOWNLOADLINKRESPONSE.fields_by_name['expires_at']._options = None

_DATAPROXYSERVICE = _descriptor.ServiceDescriptor(
  name='DataProxyService',
  full_name='flyteidl.service.DataProxyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1398,
  serialized_end=2008,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUploadLocation',
    full_name='flyteidl.service.DataProxyService.CreateUploadLocation',
    index=0,
    containing_service=None,
    input_type=_CREATEUPLOADLOCATIONREQUEST,
    output_type=_CREATEUPLOADLOCATIONRESPONSE,
    serialized_options=_b('\202\323\344\223\002#\"\036/api/v1/dataproxy/artifact_urn:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateDownloadLocation',
    full_name='flyteidl.service.DataProxyService.CreateDownloadLocation',
    index=1,
    containing_service=None,
    input_type=_CREATEDOWNLOADLOCATIONREQUEST,
    output_type=_CREATEDOWNLOADLOCATIONRESPONSE,
    serialized_options=_b('\210\002\001\202\323\344\223\002 \022\036/api/v1/dataproxy/artifact_urn'),
  ),
  _descriptor.MethodDescriptor(
    name='CreateDownloadLink',
    full_name='flyteidl.service.DataProxyService.CreateDownloadLink',
    index=2,
    containing_service=None,
    input_type=_CREATEDOWNLOADLINKREQUEST,
    output_type=_CREATEDOWNLOADLINKRESPONSE,
    serialized_options=_b('\202\323\344\223\002$\"\037/api/v1/dataproxy/artifact_link:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetData',
    full_name='flyteidl.service.DataProxyService.GetData',
    index=3,
    containing_service=None,
    input_type=_GETDATAREQUEST,
    output_type=_GETDATARESPONSE,
    serialized_options=_b('\202\323\344\223\002\016\022\014/api/v1/data'),
  ),
])
_sym_db.RegisterServiceDescriptor(_DATAPROXYSERVICE)

DESCRIPTOR.services_by_name['DataProxyService'] = _DATAPROXYSERVICE

# @@protoc_insertion_point(module_scope)

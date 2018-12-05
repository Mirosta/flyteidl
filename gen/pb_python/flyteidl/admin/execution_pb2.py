# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/execution.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.admin import common_pb2 as flyteidl_dot_admin_dot_common__pb2
from flyteidl.core import literals_pb2 as flyteidl_dot_core_dot_literals__pb2
from flyteidl.core import execution_pb2 as flyteidl_dot_core_dot_execution__pb2
from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/admin/execution.proto',
  package='flyteidl.admin',
  syntax='proto3',
  serialized_pb=_b('\n\x1e\x66lyteidl/admin/execution.proto\x12\x0e\x66lyteidl.admin\x1a\x1b\x66lyteidl/admin/common.proto\x1a\x1c\x66lyteidl/core/literals.proto\x1a\x1d\x66lyteidl/core/execution.proto\x1a\x1e\x66lyteidl/core/identifier.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"t\n\x16\x45xecutionCreateRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12+\n\x04spec\x18\x04 \x01(\x0b\x32\x1d.flyteidl.admin.ExecutionSpec\"Q\n\x17\x45xecutionCreateResponse\x12\x36\n\x02id\x18\x01 \x01(\x0b\x32*.flyteidl.core.WorkflowExecutionIdentifier\"U\n\x1bWorkflowExecutionGetRequest\x12\x36\n\x02id\x18\x01 \x01(\x0b\x32*.flyteidl.core.WorkflowExecutionIdentifier\"\xa3\x01\n\tExecution\x12\x36\n\x02id\x18\x01 \x01(\x0b\x32*.flyteidl.core.WorkflowExecutionIdentifier\x12+\n\x04spec\x18\x02 \x01(\x0b\x32\x1d.flyteidl.admin.ExecutionSpec\x12\x31\n\x07\x63losure\x18\x03 \x01(\x0b\x32 .flyteidl.admin.ExecutionClosure\">\n\rExecutionList\x12-\n\nexecutions\x18\x01 \x03(\x0b\x32\x19.flyteidl.admin.Execution\"T\n\x0eLiteralMapBlob\x12+\n\x06values\x18\x01 \x01(\x0b\x32\x19.flyteidl.core.LiteralMapH\x00\x12\r\n\x03uri\x18\x02 \x01(\tH\x00\x42\x06\n\x04\x64\x61ta\"\xe2\x03\n\x10\x45xecutionClosure\x12\x31\n\x07outputs\x18\x01 \x01(\x0b\x32\x1e.flyteidl.admin.LiteralMapBlobH\x00\x12.\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.flyteidl.core.ExecutionErrorH\x00\x12\x32\n\x0f\x63omputed_inputs\x18\x03 \x01(\x0b\x32\x19.flyteidl.core.LiteralMap\x12\x34\n\x05phase\x18\x04 \x01(\x0e\x32%.flyteidl.core.WorkflowExecutionPhase\x12.\n\nstarted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x08\x64uration\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\rnotifications\x18\t \x03(\x0b\x32\x1c.flyteidl.admin.NotificationB\x0f\n\routput_result\"\xae\x01\n\x11\x45xecutionMetadata\x12=\n\x04mode\x18\x01 \x01(\x0e\x32/.flyteidl.admin.ExecutionMetadata.ExecutionMode\x12\x11\n\tprincipal\x18\x02 \x01(\t\x12\x0f\n\x07nesting\x18\x03 \x01(\x05\"6\n\rExecutionMode\x12\n\n\x06MANUAL\x10\x00\x12\r\n\tSCHEDULED\x10\x01\x12\n\n\x06SYSTEM\x10\x02\"\xd4\x01\n\rExecutionSpec\x12.\n\x0blaunch_plan\x18\x01 \x01(\x0b\x32\x19.flyteidl.core.Identifier\x12)\n\x06inputs\x18\x02 \x01(\x0b\x32\x19.flyteidl.core.LiteralMap\x12\x33\n\x08metadata\x18\x03 \x01(\x0b\x32!.flyteidl.admin.ExecutionMetadata\x12\x33\n\rnotifications\x18\x04 \x03(\x0b\x32\x1c.flyteidl.admin.NotificationB3Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/adminb\x06proto3')
  ,
  dependencies=[flyteidl_dot_admin_dot_common__pb2.DESCRIPTOR,flyteidl_dot_core_dot_literals__pb2.DESCRIPTOR,flyteidl_dot_core_dot_execution__pb2.DESCRIPTOR,flyteidl_dot_core_dot_identifier__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_EXECUTIONMETADATA_EXECUTIONMODE = _descriptor.EnumDescriptor(
  name='ExecutionMode',
  full_name='flyteidl.admin.ExecutionMetadata.ExecutionMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MANUAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCHEDULED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1447,
  serialized_end=1501,
)
_sym_db.RegisterEnumDescriptor(_EXECUTIONMETADATA_EXECUTIONMODE)


_EXECUTIONCREATEREQUEST = _descriptor.Descriptor(
  name='ExecutionCreateRequest',
  full_name='flyteidl.admin.ExecutionCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='flyteidl.admin.ExecutionCreateRequest.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='flyteidl.admin.ExecutionCreateRequest.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='flyteidl.admin.ExecutionCreateRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='flyteidl.admin.ExecutionCreateRequest.spec', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=237,
  serialized_end=353,
)


_EXECUTIONCREATERESPONSE = _descriptor.Descriptor(
  name='ExecutionCreateResponse',
  full_name='flyteidl.admin.ExecutionCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.ExecutionCreateResponse.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=355,
  serialized_end=436,
)


_WORKFLOWEXECUTIONGETREQUEST = _descriptor.Descriptor(
  name='WorkflowExecutionGetRequest',
  full_name='flyteidl.admin.WorkflowExecutionGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.WorkflowExecutionGetRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=438,
  serialized_end=523,
)


_EXECUTION = _descriptor.Descriptor(
  name='Execution',
  full_name='flyteidl.admin.Execution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.Execution.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spec', full_name='flyteidl.admin.Execution.spec', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closure', full_name='flyteidl.admin.Execution.closure', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=526,
  serialized_end=689,
)


_EXECUTIONLIST = _descriptor.Descriptor(
  name='ExecutionList',
  full_name='flyteidl.admin.ExecutionList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='executions', full_name='flyteidl.admin.ExecutionList.executions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=691,
  serialized_end=753,
)


_LITERALMAPBLOB = _descriptor.Descriptor(
  name='LiteralMapBlob',
  full_name='flyteidl.admin.LiteralMapBlob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='flyteidl.admin.LiteralMapBlob.values', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='flyteidl.admin.LiteralMapBlob.uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='data', full_name='flyteidl.admin.LiteralMapBlob.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=755,
  serialized_end=839,
)


_EXECUTIONCLOSURE = _descriptor.Descriptor(
  name='ExecutionClosure',
  full_name='flyteidl.admin.ExecutionClosure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputs', full_name='flyteidl.admin.ExecutionClosure.outputs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='flyteidl.admin.ExecutionClosure.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='computed_inputs', full_name='flyteidl.admin.ExecutionClosure.computed_inputs', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phase', full_name='flyteidl.admin.ExecutionClosure.phase', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='flyteidl.admin.ExecutionClosure.started_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='flyteidl.admin.ExecutionClosure.duration', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='flyteidl.admin.ExecutionClosure.created_at', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='flyteidl.admin.ExecutionClosure.updated_at', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notifications', full_name='flyteidl.admin.ExecutionClosure.notifications', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='output_result', full_name='flyteidl.admin.ExecutionClosure.output_result',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=842,
  serialized_end=1324,
)


_EXECUTIONMETADATA = _descriptor.Descriptor(
  name='ExecutionMetadata',
  full_name='flyteidl.admin.ExecutionMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='flyteidl.admin.ExecutionMetadata.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='principal', full_name='flyteidl.admin.ExecutionMetadata.principal', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nesting', full_name='flyteidl.admin.ExecutionMetadata.nesting', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXECUTIONMETADATA_EXECUTIONMODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1327,
  serialized_end=1501,
)


_EXECUTIONSPEC = _descriptor.Descriptor(
  name='ExecutionSpec',
  full_name='flyteidl.admin.ExecutionSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='launch_plan', full_name='flyteidl.admin.ExecutionSpec.launch_plan', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='flyteidl.admin.ExecutionSpec.inputs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='flyteidl.admin.ExecutionSpec.metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notifications', full_name='flyteidl.admin.ExecutionSpec.notifications', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1504,
  serialized_end=1716,
)

_EXECUTIONCREATEREQUEST.fields_by_name['spec'].message_type = _EXECUTIONSPEC
_EXECUTIONCREATERESPONSE.fields_by_name['id'].message_type = flyteidl_dot_core_dot_identifier__pb2._WORKFLOWEXECUTIONIDENTIFIER
_WORKFLOWEXECUTIONGETREQUEST.fields_by_name['id'].message_type = flyteidl_dot_core_dot_identifier__pb2._WORKFLOWEXECUTIONIDENTIFIER
_EXECUTION.fields_by_name['id'].message_type = flyteidl_dot_core_dot_identifier__pb2._WORKFLOWEXECUTIONIDENTIFIER
_EXECUTION.fields_by_name['spec'].message_type = _EXECUTIONSPEC
_EXECUTION.fields_by_name['closure'].message_type = _EXECUTIONCLOSURE
_EXECUTIONLIST.fields_by_name['executions'].message_type = _EXECUTION
_LITERALMAPBLOB.fields_by_name['values'].message_type = flyteidl_dot_core_dot_literals__pb2._LITERALMAP
_LITERALMAPBLOB.oneofs_by_name['data'].fields.append(
  _LITERALMAPBLOB.fields_by_name['values'])
_LITERALMAPBLOB.fields_by_name['values'].containing_oneof = _LITERALMAPBLOB.oneofs_by_name['data']
_LITERALMAPBLOB.oneofs_by_name['data'].fields.append(
  _LITERALMAPBLOB.fields_by_name['uri'])
_LITERALMAPBLOB.fields_by_name['uri'].containing_oneof = _LITERALMAPBLOB.oneofs_by_name['data']
_EXECUTIONCLOSURE.fields_by_name['outputs'].message_type = _LITERALMAPBLOB
_EXECUTIONCLOSURE.fields_by_name['error'].message_type = flyteidl_dot_core_dot_execution__pb2._EXECUTIONERROR
_EXECUTIONCLOSURE.fields_by_name['computed_inputs'].message_type = flyteidl_dot_core_dot_literals__pb2._LITERALMAP
_EXECUTIONCLOSURE.fields_by_name['phase'].enum_type = flyteidl_dot_core_dot_execution__pb2._WORKFLOWEXECUTIONPHASE
_EXECUTIONCLOSURE.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EXECUTIONCLOSURE.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_EXECUTIONCLOSURE.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EXECUTIONCLOSURE.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EXECUTIONCLOSURE.fields_by_name['notifications'].message_type = flyteidl_dot_admin_dot_common__pb2._NOTIFICATION
_EXECUTIONCLOSURE.oneofs_by_name['output_result'].fields.append(
  _EXECUTIONCLOSURE.fields_by_name['outputs'])
_EXECUTIONCLOSURE.fields_by_name['outputs'].containing_oneof = _EXECUTIONCLOSURE.oneofs_by_name['output_result']
_EXECUTIONCLOSURE.oneofs_by_name['output_result'].fields.append(
  _EXECUTIONCLOSURE.fields_by_name['error'])
_EXECUTIONCLOSURE.fields_by_name['error'].containing_oneof = _EXECUTIONCLOSURE.oneofs_by_name['output_result']
_EXECUTIONMETADATA.fields_by_name['mode'].enum_type = _EXECUTIONMETADATA_EXECUTIONMODE
_EXECUTIONMETADATA_EXECUTIONMODE.containing_type = _EXECUTIONMETADATA
_EXECUTIONSPEC.fields_by_name['launch_plan'].message_type = flyteidl_dot_core_dot_identifier__pb2._IDENTIFIER
_EXECUTIONSPEC.fields_by_name['inputs'].message_type = flyteidl_dot_core_dot_literals__pb2._LITERALMAP
_EXECUTIONSPEC.fields_by_name['metadata'].message_type = _EXECUTIONMETADATA
_EXECUTIONSPEC.fields_by_name['notifications'].message_type = flyteidl_dot_admin_dot_common__pb2._NOTIFICATION
DESCRIPTOR.message_types_by_name['ExecutionCreateRequest'] = _EXECUTIONCREATEREQUEST
DESCRIPTOR.message_types_by_name['ExecutionCreateResponse'] = _EXECUTIONCREATERESPONSE
DESCRIPTOR.message_types_by_name['WorkflowExecutionGetRequest'] = _WORKFLOWEXECUTIONGETREQUEST
DESCRIPTOR.message_types_by_name['Execution'] = _EXECUTION
DESCRIPTOR.message_types_by_name['ExecutionList'] = _EXECUTIONLIST
DESCRIPTOR.message_types_by_name['LiteralMapBlob'] = _LITERALMAPBLOB
DESCRIPTOR.message_types_by_name['ExecutionClosure'] = _EXECUTIONCLOSURE
DESCRIPTOR.message_types_by_name['ExecutionMetadata'] = _EXECUTIONMETADATA
DESCRIPTOR.message_types_by_name['ExecutionSpec'] = _EXECUTIONSPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExecutionCreateRequest = _reflection.GeneratedProtocolMessageType('ExecutionCreateRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTIONCREATEREQUEST,
  __module__ = 'flyteidl.admin.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ExecutionCreateRequest)
  ))
_sym_db.RegisterMessage(ExecutionCreateRequest)

ExecutionCreateResponse = _reflection.GeneratedProtocolMessageType('ExecutionCreateResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTIONCREATERESPONSE,
  __module__ = 'flyteidl.admin.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ExecutionCreateResponse)
  ))
_sym_db.RegisterMessage(ExecutionCreateResponse)

WorkflowExecutionGetRequest = _reflection.GeneratedProtocolMessageType('WorkflowExecutionGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _WORKFLOWEXECUTIONGETREQUEST,
  __module__ = 'flyteidl.admin.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.WorkflowExecutionGetRequest)
  ))
_sym_db.RegisterMessage(WorkflowExecutionGetRequest)

Execution = _reflection.GeneratedProtocolMessageType('Execution', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTION,
  __module__ = 'flyteidl.admin.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.Execution)
  ))
_sym_db.RegisterMessage(Execution)

ExecutionList = _reflection.GeneratedProtocolMessageType('ExecutionList', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTIONLIST,
  __module__ = 'flyteidl.admin.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ExecutionList)
  ))
_sym_db.RegisterMessage(ExecutionList)

LiteralMapBlob = _reflection.GeneratedProtocolMessageType('LiteralMapBlob', (_message.Message,), dict(
  DESCRIPTOR = _LITERALMAPBLOB,
  __module__ = 'flyteidl.admin.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.LiteralMapBlob)
  ))
_sym_db.RegisterMessage(LiteralMapBlob)

ExecutionClosure = _reflection.GeneratedProtocolMessageType('ExecutionClosure', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTIONCLOSURE,
  __module__ = 'flyteidl.admin.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ExecutionClosure)
  ))
_sym_db.RegisterMessage(ExecutionClosure)

ExecutionMetadata = _reflection.GeneratedProtocolMessageType('ExecutionMetadata', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTIONMETADATA,
  __module__ = 'flyteidl.admin.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ExecutionMetadata)
  ))
_sym_db.RegisterMessage(ExecutionMetadata)

ExecutionSpec = _reflection.GeneratedProtocolMessageType('ExecutionSpec', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTIONSPEC,
  __module__ = 'flyteidl.admin.execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.ExecutionSpec)
  ))
_sym_db.RegisterMessage(ExecutionSpec)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/admin'))
# @@protoc_insertion_point(module_scope)

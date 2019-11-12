# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/workflow_attributes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.core import tasks_pb2 as flyteidl_dot_core_dot_tasks__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/admin/workflow_attributes.proto',
  package='flyteidl.admin',
  syntax='proto3',
  serialized_options=_b('Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/admin'),
  serialized_pb=_b('\n(flyteidl/admin/workflow_attributes.proto\x12\x0e\x66lyteidl.admin\x1a\x19\x66lyteidl/core/tasks.proto\"\x8c\x02\n\x12WorkflowAttributes\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x10\n\x08workflow\x18\x03 \x01(\t\x12\x46\n\nattributes\x18\x04 \x03(\x0b\x32\x32.flyteidl.admin.WorkflowAttributes.AttributesEntry\x12:\n\x18task_resource_attributes\x18\x05 \x01(\x0b\x32\x18.flyteidl.core.Resources\x12\x0c\n\x04tags\x18\x06 \x03(\t\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"Y\n\x1fWorkflowAttributesUpdateRequest\x12\x36\n\nattributes\x18\x01 \x01(\x0b\x32\".flyteidl.admin.WorkflowAttributes\"\"\n WorkflowAttributesUpdateResponseB3Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/adminb\x06proto3')
  ,
  dependencies=[flyteidl_dot_core_dot_tasks__pb2.DESCRIPTOR,])




_WORKFLOWATTRIBUTES_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='flyteidl.admin.WorkflowAttributes.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='flyteidl.admin.WorkflowAttributes.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='flyteidl.admin.WorkflowAttributes.AttributesEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=356,
)

_WORKFLOWATTRIBUTES = _descriptor.Descriptor(
  name='WorkflowAttributes',
  full_name='flyteidl.admin.WorkflowAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='flyteidl.admin.WorkflowAttributes.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='flyteidl.admin.WorkflowAttributes.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow', full_name='flyteidl.admin.WorkflowAttributes.workflow', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='flyteidl.admin.WorkflowAttributes.attributes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_resource_attributes', full_name='flyteidl.admin.WorkflowAttributes.task_resource_attributes', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='flyteidl.admin.WorkflowAttributes.tags', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WORKFLOWATTRIBUTES_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=356,
)


_WORKFLOWATTRIBUTESUPDATEREQUEST = _descriptor.Descriptor(
  name='WorkflowAttributesUpdateRequest',
  full_name='flyteidl.admin.WorkflowAttributesUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attributes', full_name='flyteidl.admin.WorkflowAttributesUpdateRequest.attributes', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=358,
  serialized_end=447,
)


_WORKFLOWATTRIBUTESUPDATERESPONSE = _descriptor.Descriptor(
  name='WorkflowAttributesUpdateResponse',
  full_name='flyteidl.admin.WorkflowAttributesUpdateResponse',
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
  serialized_start=449,
  serialized_end=483,
)

_WORKFLOWATTRIBUTES_ATTRIBUTESENTRY.containing_type = _WORKFLOWATTRIBUTES
_WORKFLOWATTRIBUTES.fields_by_name['attributes'].message_type = _WORKFLOWATTRIBUTES_ATTRIBUTESENTRY
_WORKFLOWATTRIBUTES.fields_by_name['task_resource_attributes'].message_type = flyteidl_dot_core_dot_tasks__pb2._RESOURCES
_WORKFLOWATTRIBUTESUPDATEREQUEST.fields_by_name['attributes'].message_type = _WORKFLOWATTRIBUTES
DESCRIPTOR.message_types_by_name['WorkflowAttributes'] = _WORKFLOWATTRIBUTES
DESCRIPTOR.message_types_by_name['WorkflowAttributesUpdateRequest'] = _WORKFLOWATTRIBUTESUPDATEREQUEST
DESCRIPTOR.message_types_by_name['WorkflowAttributesUpdateResponse'] = _WORKFLOWATTRIBUTESUPDATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkflowAttributes = _reflection.GeneratedProtocolMessageType('WorkflowAttributes', (_message.Message,), dict(

  AttributesEntry = _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), dict(
    DESCRIPTOR = _WORKFLOWATTRIBUTES_ATTRIBUTESENTRY,
    __module__ = 'flyteidl.admin.workflow_attributes_pb2'
    # @@protoc_insertion_point(class_scope:flyteidl.admin.WorkflowAttributes.AttributesEntry)
    ))
  ,
  DESCRIPTOR = _WORKFLOWATTRIBUTES,
  __module__ = 'flyteidl.admin.workflow_attributes_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.WorkflowAttributes)
  ))
_sym_db.RegisterMessage(WorkflowAttributes)
_sym_db.RegisterMessage(WorkflowAttributes.AttributesEntry)

WorkflowAttributesUpdateRequest = _reflection.GeneratedProtocolMessageType('WorkflowAttributesUpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _WORKFLOWATTRIBUTESUPDATEREQUEST,
  __module__ = 'flyteidl.admin.workflow_attributes_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.WorkflowAttributesUpdateRequest)
  ))
_sym_db.RegisterMessage(WorkflowAttributesUpdateRequest)

WorkflowAttributesUpdateResponse = _reflection.GeneratedProtocolMessageType('WorkflowAttributesUpdateResponse', (_message.Message,), dict(
  DESCRIPTOR = _WORKFLOWATTRIBUTESUPDATERESPONSE,
  __module__ = 'flyteidl.admin.workflow_attributes_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.WorkflowAttributesUpdateResponse)
  ))
_sym_db.RegisterMessage(WorkflowAttributesUpdateResponse)


DESCRIPTOR._options = None
_WORKFLOWATTRIBUTES_ATTRIBUTESENTRY._options = None
# @@protoc_insertion_point(module_scope)
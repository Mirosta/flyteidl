# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/workflow_attributes.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.admin import matchable_resource_pb2 as flyteidl_dot_admin_dot_matchable__resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(flyteidl/admin/workflow_attributes.proto\x12\x0e\x66lyteidl.admin\x1a\'flyteidl/admin/matchable_resource.proto\"\xb7\x01\n\x12WorkflowAttributes\x12\x18\n\x07project\x18\x01 \x01(\tR\x07project\x12\x16\n\x06\x64omain\x18\x02 \x01(\tR\x06\x64omain\x12\x1a\n\x08workflow\x18\x03 \x01(\tR\x08workflow\x12S\n\x13matching_attributes\x18\x04 \x01(\x0b\x32\".flyteidl.admin.MatchingAttributesR\x12matchingAttributes\"e\n\x1fWorkflowAttributesUpdateRequest\x12\x42\n\nattributes\x18\x01 \x01(\x0b\x32\".flyteidl.admin.WorkflowAttributesR\nattributes\"\"\n WorkflowAttributesUpdateResponse\"\xb4\x01\n\x1cWorkflowAttributesGetRequest\x12\x18\n\x07project\x18\x01 \x01(\tR\x07project\x12\x16\n\x06\x64omain\x18\x02 \x01(\tR\x06\x64omain\x12\x1a\n\x08workflow\x18\x03 \x01(\tR\x08workflow\x12\x46\n\rresource_type\x18\x04 \x01(\x0e\x32!.flyteidl.admin.MatchableResourceR\x0cresourceType\"c\n\x1dWorkflowAttributesGetResponse\x12\x42\n\nattributes\x18\x01 \x01(\x0b\x32\".flyteidl.admin.WorkflowAttributesR\nattributes\"\xb7\x01\n\x1fWorkflowAttributesDeleteRequest\x12\x18\n\x07project\x18\x01 \x01(\tR\x07project\x12\x16\n\x06\x64omain\x18\x02 \x01(\tR\x06\x64omain\x12\x1a\n\x08workflow\x18\x03 \x01(\tR\x08workflow\x12\x46\n\rresource_type\x18\x04 \x01(\x0e\x32!.flyteidl.admin.MatchableResourceR\x0cresourceType\"\"\n WorkflowAttributesDeleteResponseB\xbd\x01\n\x12\x63om.flyteidl.adminB\x17WorkflowAttributesProtoP\x01Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/admin\xa2\x02\x03\x46\x41X\xaa\x02\x0e\x46lyteidl.Admin\xca\x02\x0e\x46lyteidl\\Admin\xe2\x02\x1a\x46lyteidl\\Admin\\GPBMetadata\xea\x02\x0f\x46lyteidl::Adminb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flyteidl.admin.workflow_attributes_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.flyteidl.adminB\027WorkflowAttributesProtoP\001Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/admin\242\002\003FAX\252\002\016Flyteidl.Admin\312\002\016Flyteidl\\Admin\342\002\032Flyteidl\\Admin\\GPBMetadata\352\002\017Flyteidl::Admin'
  _globals['_WORKFLOWATTRIBUTES']._serialized_start=102
  _globals['_WORKFLOWATTRIBUTES']._serialized_end=285
  _globals['_WORKFLOWATTRIBUTESUPDATEREQUEST']._serialized_start=287
  _globals['_WORKFLOWATTRIBUTESUPDATEREQUEST']._serialized_end=388
  _globals['_WORKFLOWATTRIBUTESUPDATERESPONSE']._serialized_start=390
  _globals['_WORKFLOWATTRIBUTESUPDATERESPONSE']._serialized_end=424
  _globals['_WORKFLOWATTRIBUTESGETREQUEST']._serialized_start=427
  _globals['_WORKFLOWATTRIBUTESGETREQUEST']._serialized_end=607
  _globals['_WORKFLOWATTRIBUTESGETRESPONSE']._serialized_start=609
  _globals['_WORKFLOWATTRIBUTESGETRESPONSE']._serialized_end=708
  _globals['_WORKFLOWATTRIBUTESDELETEREQUEST']._serialized_start=711
  _globals['_WORKFLOWATTRIBUTESDELETEREQUEST']._serialized_end=894
  _globals['_WORKFLOWATTRIBUTESDELETERESPONSE']._serialized_start=896
  _globals['_WORKFLOWATTRIBUTESDELETERESPONSE']._serialized_end=930
# @@protoc_insertion_point(module_scope)

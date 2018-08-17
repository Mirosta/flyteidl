# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/service/admin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from flyteidl.admin import task_pb2 as flyteidl_dot_admin_dot_task__pb2
from flyteidl.admin import workflow_pb2 as flyteidl_dot_admin_dot_workflow__pb2
from flyteidl.admin import launch_plan_pb2 as flyteidl_dot_admin_dot_launch__plan__pb2
from flyteidl.admin import execution_pb2 as flyteidl_dot_admin_dot_execution__pb2
from flyteidl.admin import common_pb2 as flyteidl_dot_admin_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/service/admin.proto',
  package='flyteidl.service',
  syntax='proto3',
  serialized_pb=_b('\n\x1c\x66lyteidl/service/admin.proto\x12\x10\x66lyteidl.service\x1a\x1cgoogle/api/annotations.proto\x1a\x19\x66lyteidl/admin/task.proto\x1a\x1d\x66lyteidl/admin/workflow.proto\x1a flyteidl/admin/launch_plan.proto\x1a\x1e\x66lyteidl/admin/execution.proto\x1a\x1b\x66lyteidl/admin/common.proto2\xa7\x0c\n\x0c\x41\x64minService\x12m\n\nCreateTask\x12!.flyteidl.admin.TaskCreateRequest\x1a\".flyteidl.admin.TaskCreateResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/api/v1/tasks:\x01*\x12^\n\x07GetTask\x12 .flyteidl.admin.ObjectGetRequest\x1a\x14.flyteidl.admin.Task\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/api/v1/tasks/{urn}\x12\x90\x01\n\x0bListTaskIds\x12%.flyteidl.admin.IdentifierListRequest\x1a\x1e.flyteidl.admin.IdentifierList\":\x82\xd3\xe4\x93\x02\x34\x12\x32/api/v1/project/{project}/domain/{domain}/task_ids\x12\xcd\x01\n\tListTasks\x12#.flyteidl.admin.ResourceListRequest\x1a\x18.flyteidl.admin.TaskList\"\x80\x01\x82\xd3\xe4\x93\x02z\x12\x35/api/v1/project/{id.project}/domain/{id.domain}/tasksZA\x12?/api/v1/project/{id.project}/domain/{id.domain}/tasks/{id.name}\x12}\n\x0e\x43reateWorkflow\x12%.flyteidl.admin.WorkflowCreateRequest\x1a&.flyteidl.admin.WorkflowCreateResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/api/v1/workflows:\x01*\x12j\n\x0bGetWorkflow\x12 .flyteidl.admin.ObjectGetRequest\x1a\x18.flyteidl.admin.Workflow\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/api/v1/workflows/{urn}\x12\x98\x01\n\x0fListWorkflowIds\x12%.flyteidl.admin.IdentifierListRequest\x1a\x1e.flyteidl.admin.IdentifierList\">\x82\xd3\xe4\x93\x02\x38\x12\x36/api/v1/project/{project}/domain/{domain}/workflow_ids\x12\xde\x01\n\rListWorkflows\x12#.flyteidl.admin.ResourceListRequest\x1a\x1c.flyteidl.admin.WorkflowList\"\x89\x01\x82\xd3\xe4\x93\x02\x82\x01\x12\x39/api/v1/project/{id.project}/domain/{id.domain}/workflowsZE\x12\x43/api/v1/project/{id.project}/domain/{id.domain}/workflows/{id.name}\x12\x86\x01\n\x10\x43reateLaunchPlan\x12\'.flyteidl.admin.LaunchPlanCreateRequest\x1a(.flyteidl.admin.LaunchPlanCreateResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/api/v1/launch_plans:\x01*\x12q\n\rGetLaunchPlan\x12 .flyteidl.admin.ObjectGetRequest\x1a\x1a.flyteidl.admin.LaunchPlan\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/api/v1/launch_plans/{urn}\x12\x81\x01\n\x0f\x43reateExecution\x12&.flyteidl.admin.ExecutionCreateRequest\x1a\'.flyteidl.admin.ExecutionCreateResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/api/v1/executions:\x01*B5Z3github.com/lyft/flyteidl/gen/pb-go/flyteidl/serviceb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,flyteidl_dot_admin_dot_task__pb2.DESCRIPTOR,flyteidl_dot_admin_dot_workflow__pb2.DESCRIPTOR,flyteidl_dot_admin_dot_launch__plan__pb2.DESCRIPTOR,flyteidl_dot_admin_dot_execution__pb2.DESCRIPTOR,flyteidl_dot_admin_dot_common__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z3github.com/lyft/flyteidl/gen/pb-go/flyteidl/service'))

_ADMINSERVICE = _descriptor.ServiceDescriptor(
  name='AdminService',
  full_name='flyteidl.service.AdminService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=234,
  serialized_end=1809,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateTask',
    full_name='flyteidl.service.AdminService.CreateTask',
    index=0,
    containing_service=None,
    input_type=flyteidl_dot_admin_dot_task__pb2._TASKCREATEREQUEST,
    output_type=flyteidl_dot_admin_dot_task__pb2._TASKCREATERESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\022\"\r/api/v1/tasks:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='GetTask',
    full_name='flyteidl.service.AdminService.GetTask',
    index=1,
    containing_service=None,
    input_type=flyteidl_dot_admin_dot_common__pb2._OBJECTGETREQUEST,
    output_type=flyteidl_dot_admin_dot_task__pb2._TASK,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\025\022\023/api/v1/tasks/{urn}')),
  ),
  _descriptor.MethodDescriptor(
    name='ListTaskIds',
    full_name='flyteidl.service.AdminService.ListTaskIds',
    index=2,
    containing_service=None,
    input_type=flyteidl_dot_admin_dot_common__pb2._IDENTIFIERLISTREQUEST,
    output_type=flyteidl_dot_admin_dot_common__pb2._IDENTIFIERLIST,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0024\0222/api/v1/project/{project}/domain/{domain}/task_ids')),
  ),
  _descriptor.MethodDescriptor(
    name='ListTasks',
    full_name='flyteidl.service.AdminService.ListTasks',
    index=3,
    containing_service=None,
    input_type=flyteidl_dot_admin_dot_common__pb2._RESOURCELISTREQUEST,
    output_type=flyteidl_dot_admin_dot_task__pb2._TASKLIST,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002z\0225/api/v1/project/{id.project}/domain/{id.domain}/tasksZA\022?/api/v1/project/{id.project}/domain/{id.domain}/tasks/{id.name}')),
  ),
  _descriptor.MethodDescriptor(
    name='CreateWorkflow',
    full_name='flyteidl.service.AdminService.CreateWorkflow',
    index=4,
    containing_service=None,
    input_type=flyteidl_dot_admin_dot_workflow__pb2._WORKFLOWCREATEREQUEST,
    output_type=flyteidl_dot_admin_dot_workflow__pb2._WORKFLOWCREATERESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\026\"\021/api/v1/workflows:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='GetWorkflow',
    full_name='flyteidl.service.AdminService.GetWorkflow',
    index=5,
    containing_service=None,
    input_type=flyteidl_dot_admin_dot_common__pb2._OBJECTGETREQUEST,
    output_type=flyteidl_dot_admin_dot_workflow__pb2._WORKFLOW,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\031\022\027/api/v1/workflows/{urn}')),
  ),
  _descriptor.MethodDescriptor(
    name='ListWorkflowIds',
    full_name='flyteidl.service.AdminService.ListWorkflowIds',
    index=6,
    containing_service=None,
    input_type=flyteidl_dot_admin_dot_common__pb2._IDENTIFIERLISTREQUEST,
    output_type=flyteidl_dot_admin_dot_common__pb2._IDENTIFIERLIST,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0028\0226/api/v1/project/{project}/domain/{domain}/workflow_ids')),
  ),
  _descriptor.MethodDescriptor(
    name='ListWorkflows',
    full_name='flyteidl.service.AdminService.ListWorkflows',
    index=7,
    containing_service=None,
    input_type=flyteidl_dot_admin_dot_common__pb2._RESOURCELISTREQUEST,
    output_type=flyteidl_dot_admin_dot_workflow__pb2._WORKFLOWLIST,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\202\001\0229/api/v1/project/{id.project}/domain/{id.domain}/workflowsZE\022C/api/v1/project/{id.project}/domain/{id.domain}/workflows/{id.name}')),
  ),
  _descriptor.MethodDescriptor(
    name='CreateLaunchPlan',
    full_name='flyteidl.service.AdminService.CreateLaunchPlan',
    index=8,
    containing_service=None,
    input_type=flyteidl_dot_admin_dot_launch__plan__pb2._LAUNCHPLANCREATEREQUEST,
    output_type=flyteidl_dot_admin_dot_launch__plan__pb2._LAUNCHPLANCREATERESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\031\"\024/api/v1/launch_plans:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='GetLaunchPlan',
    full_name='flyteidl.service.AdminService.GetLaunchPlan',
    index=9,
    containing_service=None,
    input_type=flyteidl_dot_admin_dot_common__pb2._OBJECTGETREQUEST,
    output_type=flyteidl_dot_admin_dot_launch__plan__pb2._LAUNCHPLAN,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\034\022\032/api/v1/launch_plans/{urn}')),
  ),
  _descriptor.MethodDescriptor(
    name='CreateExecution',
    full_name='flyteidl.service.AdminService.CreateExecution',
    index=10,
    containing_service=None,
    input_type=flyteidl_dot_admin_dot_execution__pb2._EXECUTIONCREATEREQUEST,
    output_type=flyteidl_dot_admin_dot_execution__pb2._EXECUTIONCREATERESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\027\"\022/api/v1/executions:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_ADMINSERVICE)

DESCRIPTOR.services_by_name['AdminService'] = _ADMINSERVICE

# @@protoc_insertion_point(module_scope)
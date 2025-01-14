// Code generated by protoc-gen-go. DO NOT EDIT.
// source: flyteidl/plugins/ray.proto

package plugins

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

// RayJobSpec defines the desired state of RayJob
type RayJob struct {
	// RayClusterSpec is the cluster template to run the job
	RayCluster *RayCluster `protobuf:"bytes,1,opt,name=ray_cluster,json=rayCluster,proto3" json:"ray_cluster,omitempty"`
	// runtime_env is base64 encoded.
	// Ray runtime environments: https://docs.ray.io/en/latest/ray-core/handling-dependencies.html#runtime-environments
	RuntimeEnv           string   `protobuf:"bytes,2,opt,name=runtime_env,json=runtimeEnv,proto3" json:"runtime_env,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *RayJob) Reset()         { *m = RayJob{} }
func (m *RayJob) String() string { return proto.CompactTextString(m) }
func (*RayJob) ProtoMessage()    {}
func (*RayJob) Descriptor() ([]byte, []int) {
	return fileDescriptor_b980f6d58c7489d7, []int{0}
}

func (m *RayJob) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_RayJob.Unmarshal(m, b)
}
func (m *RayJob) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_RayJob.Marshal(b, m, deterministic)
}
func (m *RayJob) XXX_Merge(src proto.Message) {
	xxx_messageInfo_RayJob.Merge(m, src)
}
func (m *RayJob) XXX_Size() int {
	return xxx_messageInfo_RayJob.Size(m)
}
func (m *RayJob) XXX_DiscardUnknown() {
	xxx_messageInfo_RayJob.DiscardUnknown(m)
}

var xxx_messageInfo_RayJob proto.InternalMessageInfo

func (m *RayJob) GetRayCluster() *RayCluster {
	if m != nil {
		return m.RayCluster
	}
	return nil
}

func (m *RayJob) GetRuntimeEnv() string {
	if m != nil {
		return m.RuntimeEnv
	}
	return ""
}

// Define Ray cluster defines the desired state of RayCluster
type RayCluster struct {
	// HeadGroupSpecs are the spec for the head pod
	HeadGroupSpec *HeadGroupSpec `protobuf:"bytes,1,opt,name=head_group_spec,json=headGroupSpec,proto3" json:"head_group_spec,omitempty"`
	// WorkerGroupSpecs are the specs for the worker pods
	WorkerGroupSpec      []*WorkerGroupSpec `protobuf:"bytes,2,rep,name=worker_group_spec,json=workerGroupSpec,proto3" json:"worker_group_spec,omitempty"`
	XXX_NoUnkeyedLiteral struct{}           `json:"-"`
	XXX_unrecognized     []byte             `json:"-"`
	XXX_sizecache        int32              `json:"-"`
}

func (m *RayCluster) Reset()         { *m = RayCluster{} }
func (m *RayCluster) String() string { return proto.CompactTextString(m) }
func (*RayCluster) ProtoMessage()    {}
func (*RayCluster) Descriptor() ([]byte, []int) {
	return fileDescriptor_b980f6d58c7489d7, []int{1}
}

func (m *RayCluster) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_RayCluster.Unmarshal(m, b)
}
func (m *RayCluster) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_RayCluster.Marshal(b, m, deterministic)
}
func (m *RayCluster) XXX_Merge(src proto.Message) {
	xxx_messageInfo_RayCluster.Merge(m, src)
}
func (m *RayCluster) XXX_Size() int {
	return xxx_messageInfo_RayCluster.Size(m)
}
func (m *RayCluster) XXX_DiscardUnknown() {
	xxx_messageInfo_RayCluster.DiscardUnknown(m)
}

var xxx_messageInfo_RayCluster proto.InternalMessageInfo

func (m *RayCluster) GetHeadGroupSpec() *HeadGroupSpec {
	if m != nil {
		return m.HeadGroupSpec
	}
	return nil
}

func (m *RayCluster) GetWorkerGroupSpec() []*WorkerGroupSpec {
	if m != nil {
		return m.WorkerGroupSpec
	}
	return nil
}

// HeadGroupSpec are the spec for the head pod
type HeadGroupSpec struct {
	// Optional. RayStartParams are the params of the start command: address, object-store-memory.
	// Refer to https://docs.ray.io/en/latest/ray-core/package-ref.html#ray-start
	RayStartParams       map[string]string `protobuf:"bytes,1,rep,name=ray_start_params,json=rayStartParams,proto3" json:"ray_start_params,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *HeadGroupSpec) Reset()         { *m = HeadGroupSpec{} }
func (m *HeadGroupSpec) String() string { return proto.CompactTextString(m) }
func (*HeadGroupSpec) ProtoMessage()    {}
func (*HeadGroupSpec) Descriptor() ([]byte, []int) {
	return fileDescriptor_b980f6d58c7489d7, []int{2}
}

func (m *HeadGroupSpec) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_HeadGroupSpec.Unmarshal(m, b)
}
func (m *HeadGroupSpec) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_HeadGroupSpec.Marshal(b, m, deterministic)
}
func (m *HeadGroupSpec) XXX_Merge(src proto.Message) {
	xxx_messageInfo_HeadGroupSpec.Merge(m, src)
}
func (m *HeadGroupSpec) XXX_Size() int {
	return xxx_messageInfo_HeadGroupSpec.Size(m)
}
func (m *HeadGroupSpec) XXX_DiscardUnknown() {
	xxx_messageInfo_HeadGroupSpec.DiscardUnknown(m)
}

var xxx_messageInfo_HeadGroupSpec proto.InternalMessageInfo

func (m *HeadGroupSpec) GetRayStartParams() map[string]string {
	if m != nil {
		return m.RayStartParams
	}
	return nil
}

// WorkerGroupSpec are the specs for the worker pods
type WorkerGroupSpec struct {
	// Required. RayCluster can have multiple worker groups, and it distinguishes them by name
	GroupName string `protobuf:"bytes,1,opt,name=group_name,json=groupName,proto3" json:"group_name,omitempty"`
	// Required. Desired replicas of the worker group. Defaults to 1.
	Replicas int32 `protobuf:"varint,2,opt,name=replicas,proto3" json:"replicas,omitempty"`
	// Optional. Min replicas of the worker group. MinReplicas defaults to 1.
	MinReplicas int32 `protobuf:"varint,3,opt,name=min_replicas,json=minReplicas,proto3" json:"min_replicas,omitempty"`
	// Optional. Max replicas of the worker group. MaxReplicas defaults to maxInt32
	MaxReplicas int32 `protobuf:"varint,4,opt,name=max_replicas,json=maxReplicas,proto3" json:"max_replicas,omitempty"`
	// Optional. RayStartParams are the params of the start command: address, object-store-memory.
	// Refer to https://docs.ray.io/en/latest/ray-core/package-ref.html#ray-start
	RayStartParams       map[string]string `protobuf:"bytes,5,rep,name=ray_start_params,json=rayStartParams,proto3" json:"ray_start_params,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *WorkerGroupSpec) Reset()         { *m = WorkerGroupSpec{} }
func (m *WorkerGroupSpec) String() string { return proto.CompactTextString(m) }
func (*WorkerGroupSpec) ProtoMessage()    {}
func (*WorkerGroupSpec) Descriptor() ([]byte, []int) {
	return fileDescriptor_b980f6d58c7489d7, []int{3}
}

func (m *WorkerGroupSpec) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_WorkerGroupSpec.Unmarshal(m, b)
}
func (m *WorkerGroupSpec) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_WorkerGroupSpec.Marshal(b, m, deterministic)
}
func (m *WorkerGroupSpec) XXX_Merge(src proto.Message) {
	xxx_messageInfo_WorkerGroupSpec.Merge(m, src)
}
func (m *WorkerGroupSpec) XXX_Size() int {
	return xxx_messageInfo_WorkerGroupSpec.Size(m)
}
func (m *WorkerGroupSpec) XXX_DiscardUnknown() {
	xxx_messageInfo_WorkerGroupSpec.DiscardUnknown(m)
}

var xxx_messageInfo_WorkerGroupSpec proto.InternalMessageInfo

func (m *WorkerGroupSpec) GetGroupName() string {
	if m != nil {
		return m.GroupName
	}
	return ""
}

func (m *WorkerGroupSpec) GetReplicas() int32 {
	if m != nil {
		return m.Replicas
	}
	return 0
}

func (m *WorkerGroupSpec) GetMinReplicas() int32 {
	if m != nil {
		return m.MinReplicas
	}
	return 0
}

func (m *WorkerGroupSpec) GetMaxReplicas() int32 {
	if m != nil {
		return m.MaxReplicas
	}
	return 0
}

func (m *WorkerGroupSpec) GetRayStartParams() map[string]string {
	if m != nil {
		return m.RayStartParams
	}
	return nil
}

func init() {
	proto.RegisterType((*RayJob)(nil), "flyteidl.plugins.RayJob")
	proto.RegisterType((*RayCluster)(nil), "flyteidl.plugins.RayCluster")
	proto.RegisterType((*HeadGroupSpec)(nil), "flyteidl.plugins.HeadGroupSpec")
	proto.RegisterMapType((map[string]string)(nil), "flyteidl.plugins.HeadGroupSpec.RayStartParamsEntry")
	proto.RegisterType((*WorkerGroupSpec)(nil), "flyteidl.plugins.WorkerGroupSpec")
	proto.RegisterMapType((map[string]string)(nil), "flyteidl.plugins.WorkerGroupSpec.RayStartParamsEntry")
}

func init() { proto.RegisterFile("flyteidl/plugins/ray.proto", fileDescriptor_b980f6d58c7489d7) }

var fileDescriptor_b980f6d58c7489d7 = []byte{
	// 412 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xbc, 0x93, 0x4d, 0xcb, 0xd3, 0x40,
	0x10, 0xc7, 0x49, 0x6a, 0x8b, 0x9d, 0x58, 0x5b, 0x57, 0x0f, 0xa5, 0x28, 0x6d, 0x73, 0xea, 0xc5,
	0x04, 0x5a, 0xc4, 0x17, 0xf0, 0xa0, 0x52, 0x2a, 0x82, 0x22, 0xdb, 0x83, 0x20, 0x48, 0xd8, 0xa4,
	0x6b, 0x12, 0x9a, 0xec, 0x2e, 0x9b, 0x4d, 0xdb, 0x7c, 0x1f, 0xbf, 0x80, 0x17, 0x3f, 0x9f, 0x64,
	0x9b, 0x27, 0x7d, 0x85, 0xde, 0x9e, 0xdb, 0xce, 0xcc, 0x7f, 0xfe, 0x33, 0xf9, 0x85, 0x81, 0xc1,
	0xef, 0xa4, 0x50, 0x34, 0x5e, 0x25, 0xae, 0x48, 0xf2, 0x30, 0x66, 0x99, 0x2b, 0x49, 0xe1, 0x08,
	0xc9, 0x15, 0x47, 0xbd, 0xbb, 0x9a, 0x53, 0xd5, 0xec, 0x08, 0x5a, 0x98, 0x14, 0x5f, 0xb8, 0x8f,
	0xde, 0x83, 0x25, 0x49, 0xe1, 0x05, 0x49, 0x9e, 0x29, 0x2a, 0xfb, 0xc6, 0xc8, 0x98, 0x58, 0xd3,
	0xe7, 0xce, 0x79, 0x87, 0x83, 0x49, 0xf1, 0x69, 0xaf, 0xc1, 0x20, 0xeb, 0x37, 0x1a, 0x82, 0x25,
	0x73, 0xa6, 0xe2, 0x94, 0x7a, 0x94, 0x6d, 0xfa, 0xe6, 0xc8, 0x98, 0xb4, 0x31, 0x54, 0xa9, 0x39,
	0xdb, 0xd8, 0x7f, 0x0c, 0x80, 0x43, 0x2f, 0x5a, 0x40, 0x37, 0xa2, 0x64, 0xe5, 0x85, 0x92, 0xe7,
	0xc2, 0xcb, 0x04, 0x0d, 0xaa, 0x91, 0xc3, 0xcb, 0x91, 0x9f, 0x29, 0x59, 0x2d, 0x4a, 0xdd, 0x52,
	0xd0, 0x00, 0x77, 0xa2, 0xe3, 0x10, 0x7d, 0x85, 0x27, 0x5b, 0x2e, 0xd7, 0x54, 0x1e, 0x5b, 0x99,
	0xa3, 0xc6, 0xc4, 0x9a, 0x8e, 0x2f, 0xad, 0x7e, 0x68, 0xe9, 0xc1, 0xac, 0xbb, 0x3d, 0x4d, 0xd8,
	0x7f, 0x0d, 0xe8, 0x9c, 0xcc, 0x43, 0xbf, 0xa0, 0x57, 0x82, 0xc9, 0x14, 0x91, 0xca, 0x13, 0x44,
	0x92, 0x34, 0xeb, 0x1b, 0xda, 0x7f, 0x76, 0x63, 0xd5, 0x92, 0xd5, 0xb2, 0x6c, 0xfb, 0xae, 0xbb,
	0xe6, 0x4c, 0xc9, 0x02, 0x3f, 0x96, 0x27, 0xc9, 0xc1, 0x07, 0x78, 0x7a, 0x45, 0x86, 0x7a, 0xd0,
	0x58, 0xd3, 0x42, 0x33, 0x69, 0xe3, 0xf2, 0x89, 0x9e, 0x41, 0x73, 0x43, 0x92, 0x9c, 0x56, 0x6c,
	0xf7, 0xc1, 0x3b, 0xf3, 0x8d, 0x61, 0xff, 0x33, 0xa1, 0x7b, 0xf6, 0x61, 0xe8, 0x05, 0xc0, 0x9e,
	0x07, 0x23, 0x29, 0xad, 0x6c, 0xda, 0x3a, 0xf3, 0x8d, 0xa4, 0x14, 0x0d, 0xe0, 0xa1, 0xa4, 0x22,
	0x89, 0x03, 0x92, 0x69, 0xbf, 0x26, 0xae, 0x63, 0x34, 0x86, 0x47, 0x69, 0xcc, 0xbc, 0xba, 0xde,
	0xd0, 0x75, 0x2b, 0x8d, 0x19, 0x3e, 0x96, 0x90, 0xdd, 0x41, 0xf2, 0xa0, 0x92, 0x90, 0x5d, 0x2d,
	0xf1, 0xae, 0x60, 0x6b, 0x6a, 0x6c, 0xaf, 0x6e, 0xfe, 0x96, 0x7b, 0x02, 0xf7, 0xf1, 0xed, 0xcf,
	0xd7, 0x61, 0xac, 0xa2, 0xdc, 0x77, 0x02, 0x9e, 0xba, 0x7a, 0x2b, 0x2e, 0x43, 0xb7, 0xbe, 0xa0,
	0x90, 0x32, 0x57, 0xf8, 0x2f, 0x43, 0xee, 0x9e, 0x1f, 0x95, 0xdf, 0xd2, 0x17, 0x35, 0xfb, 0x1f,
	0x00, 0x00, 0xff, 0xff, 0xfb, 0xc2, 0x9c, 0xe6, 0x6f, 0x03, 0x00, 0x00,
}

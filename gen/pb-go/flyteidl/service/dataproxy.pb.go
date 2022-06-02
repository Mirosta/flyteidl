// Code generated by protoc-gen-go. DO NOT EDIT.
// source: flyteidl/service/dataproxy.proto

package service

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	duration "github.com/golang/protobuf/ptypes/duration"
	timestamp "github.com/golang/protobuf/ptypes/timestamp"
	_ "github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/options"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
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

type CreateUploadLocationResponse struct {
	// SignedUrl specifies the url to use to upload content to (e.g. https://my-bucket.s3.amazonaws.com/randomstring/suffix.tar?X-...)
	SignedUrl string `protobuf:"bytes,1,opt,name=signed_url,json=signedUrl,proto3" json:"signed_url,omitempty"`
	// NativeUrl specifies the url in the format of the configured storage provider (e.g. s3://my-bucket/randomstring/suffix.tar)
	NativeUrl string `protobuf:"bytes,2,opt,name=native_url,json=nativeUrl,proto3" json:"native_url,omitempty"`
	// ExpiresAt defines when will the signed URL expires.
	ExpiresAt            *timestamp.Timestamp `protobuf:"bytes,3,opt,name=expires_at,json=expiresAt,proto3" json:"expires_at,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *CreateUploadLocationResponse) Reset()         { *m = CreateUploadLocationResponse{} }
func (m *CreateUploadLocationResponse) String() string { return proto.CompactTextString(m) }
func (*CreateUploadLocationResponse) ProtoMessage()    {}
func (*CreateUploadLocationResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_bffb71366d75dab0, []int{0}
}

func (m *CreateUploadLocationResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CreateUploadLocationResponse.Unmarshal(m, b)
}
func (m *CreateUploadLocationResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CreateUploadLocationResponse.Marshal(b, m, deterministic)
}
func (m *CreateUploadLocationResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CreateUploadLocationResponse.Merge(m, src)
}
func (m *CreateUploadLocationResponse) XXX_Size() int {
	return xxx_messageInfo_CreateUploadLocationResponse.Size(m)
}
func (m *CreateUploadLocationResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_CreateUploadLocationResponse.DiscardUnknown(m)
}

var xxx_messageInfo_CreateUploadLocationResponse proto.InternalMessageInfo

func (m *CreateUploadLocationResponse) GetSignedUrl() string {
	if m != nil {
		return m.SignedUrl
	}
	return ""
}

func (m *CreateUploadLocationResponse) GetNativeUrl() string {
	if m != nil {
		return m.NativeUrl
	}
	return ""
}

func (m *CreateUploadLocationResponse) GetExpiresAt() *timestamp.Timestamp {
	if m != nil {
		return m.ExpiresAt
	}
	return nil
}

// CreateUploadLocationRequest specified request for the CreateUploadLocation API.
type CreateUploadLocationRequest struct {
	// Project to create the upload location for
	// +required
	Project string `protobuf:"bytes,1,opt,name=project,proto3" json:"project,omitempty"`
	// Domain to create the upload location for.
	// +required
	Domain string `protobuf:"bytes,2,opt,name=domain,proto3" json:"domain,omitempty"`
	// Filename specifies a desired suffix for the generated location. E.g. `file.py` or `pre/fix/file.zip`.
	// +optional. By default, the service will generate a consistent name based on the provided parameters.
	Filename string `protobuf:"bytes,3,opt,name=filename,proto3" json:"filename,omitempty"`
	// ExpiresIn defines a requested expiration duration for the generated url. The request will be rejected if this
	// exceeds the platform allowed max.
	// +optional. The default value comes from a global config.
	ExpiresIn *duration.Duration `protobuf:"bytes,4,opt,name=expires_in,json=expiresIn,proto3" json:"expires_in,omitempty"`
	// ContentMD5 restricts the upload location to the specific MD5 provided. The ContentMD5 will also appear in the
	// generated path.
	// +required
	ContentMd5           []byte   `protobuf:"bytes,5,opt,name=content_md5,json=contentMd5,proto3" json:"content_md5,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *CreateUploadLocationRequest) Reset()         { *m = CreateUploadLocationRequest{} }
func (m *CreateUploadLocationRequest) String() string { return proto.CompactTextString(m) }
func (*CreateUploadLocationRequest) ProtoMessage()    {}
func (*CreateUploadLocationRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_bffb71366d75dab0, []int{1}
}

func (m *CreateUploadLocationRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CreateUploadLocationRequest.Unmarshal(m, b)
}
func (m *CreateUploadLocationRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CreateUploadLocationRequest.Marshal(b, m, deterministic)
}
func (m *CreateUploadLocationRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CreateUploadLocationRequest.Merge(m, src)
}
func (m *CreateUploadLocationRequest) XXX_Size() int {
	return xxx_messageInfo_CreateUploadLocationRequest.Size(m)
}
func (m *CreateUploadLocationRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_CreateUploadLocationRequest.DiscardUnknown(m)
}

var xxx_messageInfo_CreateUploadLocationRequest proto.InternalMessageInfo

func (m *CreateUploadLocationRequest) GetProject() string {
	if m != nil {
		return m.Project
	}
	return ""
}

func (m *CreateUploadLocationRequest) GetDomain() string {
	if m != nil {
		return m.Domain
	}
	return ""
}

func (m *CreateUploadLocationRequest) GetFilename() string {
	if m != nil {
		return m.Filename
	}
	return ""
}

func (m *CreateUploadLocationRequest) GetExpiresIn() *duration.Duration {
	if m != nil {
		return m.ExpiresIn
	}
	return nil
}

func (m *CreateUploadLocationRequest) GetContentMd5() []byte {
	if m != nil {
		return m.ContentMd5
	}
	return nil
}

// CreateDownloadLocationRequest specified request for the CreateDownloadLocation API.
type CreateDownloadLocationRequest struct {
	// NativeUrl specifies the url in the format of the configured storage provider (e.g. s3://my-bucket/randomstring/suffix.tar)
	NativeUrl string `protobuf:"bytes,1,opt,name=native_url,json=nativeUrl,proto3" json:"native_url,omitempty"`
	// ExpiresIn defines a requested expiration duration for the generated url. The request will be rejected if this
	// exceeds the platform allowed max.
	// +optional. The default value comes from a global config.
	ExpiresIn            *duration.Duration `protobuf:"bytes,2,opt,name=expires_in,json=expiresIn,proto3" json:"expires_in,omitempty"`
	XXX_NoUnkeyedLiteral struct{}           `json:"-"`
	XXX_unrecognized     []byte             `json:"-"`
	XXX_sizecache        int32              `json:"-"`
}

func (m *CreateDownloadLocationRequest) Reset()         { *m = CreateDownloadLocationRequest{} }
func (m *CreateDownloadLocationRequest) String() string { return proto.CompactTextString(m) }
func (*CreateDownloadLocationRequest) ProtoMessage()    {}
func (*CreateDownloadLocationRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_bffb71366d75dab0, []int{2}
}

func (m *CreateDownloadLocationRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CreateDownloadLocationRequest.Unmarshal(m, b)
}
func (m *CreateDownloadLocationRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CreateDownloadLocationRequest.Marshal(b, m, deterministic)
}
func (m *CreateDownloadLocationRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CreateDownloadLocationRequest.Merge(m, src)
}
func (m *CreateDownloadLocationRequest) XXX_Size() int {
	return xxx_messageInfo_CreateDownloadLocationRequest.Size(m)
}
func (m *CreateDownloadLocationRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_CreateDownloadLocationRequest.DiscardUnknown(m)
}

var xxx_messageInfo_CreateDownloadLocationRequest proto.InternalMessageInfo

func (m *CreateDownloadLocationRequest) GetNativeUrl() string {
	if m != nil {
		return m.NativeUrl
	}
	return ""
}

func (m *CreateDownloadLocationRequest) GetExpiresIn() *duration.Duration {
	if m != nil {
		return m.ExpiresIn
	}
	return nil
}

type CreateDownloadLocationResponse struct {
	// SignedUrl specifies the url to use to download content from (e.g. https://my-bucket.s3.amazonaws.com/randomstring/suffix.tar?X-...)
	SignedUrl string `protobuf:"bytes,1,opt,name=signed_url,json=signedUrl,proto3" json:"signed_url,omitempty"`
	// ExpiresAt defines when will the signed URL expires.
	ExpiresAt            *timestamp.Timestamp `protobuf:"bytes,2,opt,name=expires_at,json=expiresAt,proto3" json:"expires_at,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *CreateDownloadLocationResponse) Reset()         { *m = CreateDownloadLocationResponse{} }
func (m *CreateDownloadLocationResponse) String() string { return proto.CompactTextString(m) }
func (*CreateDownloadLocationResponse) ProtoMessage()    {}
func (*CreateDownloadLocationResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_bffb71366d75dab0, []int{3}
}

func (m *CreateDownloadLocationResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_CreateDownloadLocationResponse.Unmarshal(m, b)
}
func (m *CreateDownloadLocationResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_CreateDownloadLocationResponse.Marshal(b, m, deterministic)
}
func (m *CreateDownloadLocationResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_CreateDownloadLocationResponse.Merge(m, src)
}
func (m *CreateDownloadLocationResponse) XXX_Size() int {
	return xxx_messageInfo_CreateDownloadLocationResponse.Size(m)
}
func (m *CreateDownloadLocationResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_CreateDownloadLocationResponse.DiscardUnknown(m)
}

var xxx_messageInfo_CreateDownloadLocationResponse proto.InternalMessageInfo

func (m *CreateDownloadLocationResponse) GetSignedUrl() string {
	if m != nil {
		return m.SignedUrl
	}
	return ""
}

func (m *CreateDownloadLocationResponse) GetExpiresAt() *timestamp.Timestamp {
	if m != nil {
		return m.ExpiresAt
	}
	return nil
}

func init() {
	proto.RegisterType((*CreateUploadLocationResponse)(nil), "flyteidl.service.CreateUploadLocationResponse")
	proto.RegisterType((*CreateUploadLocationRequest)(nil), "flyteidl.service.CreateUploadLocationRequest")
	proto.RegisterType((*CreateDownloadLocationRequest)(nil), "flyteidl.service.CreateDownloadLocationRequest")
	proto.RegisterType((*CreateDownloadLocationResponse)(nil), "flyteidl.service.CreateDownloadLocationResponse")
}

func init() { proto.RegisterFile("flyteidl/service/dataproxy.proto", fileDescriptor_bffb71366d75dab0) }

var fileDescriptor_bffb71366d75dab0 = []byte{
	// 583 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xa4, 0x94, 0xcd, 0x6e, 0xd3, 0x40,
	0x14, 0x85, 0xe5, 0x14, 0x0a, 0x99, 0xb2, 0xa8, 0x46, 0xa8, 0x0a, 0xa6, 0x3f, 0x23, 0x57, 0x48,
	0x15, 0x22, 0x1e, 0x28, 0xaa, 0xa0, 0xec, 0x0a, 0xd9, 0x00, 0xad, 0x84, 0x02, 0xdd, 0xb0, 0x89,
	0x26, 0xf6, 0x8d, 0x33, 0x60, 0xcf, 0x98, 0x99, 0xeb, 0xfc, 0x74, 0xc9, 0x23, 0x94, 0x05, 0x6f,
	0xc4, 0x0b, 0xf0, 0x0a, 0x3c, 0x00, 0x3b, 0x96, 0xa0, 0xd8, 0x4e, 0xa2, 0x84, 0xa4, 0x0a, 0x62,
	0x15, 0xdd, 0xb9, 0x67, 0xe2, 0xef, 0xcc, 0x99, 0x3b, 0x84, 0x75, 0xe2, 0x21, 0x82, 0x0c, 0x63,
	0x6e, 0xc1, 0xf4, 0x64, 0x00, 0x3c, 0x14, 0x28, 0x52, 0xa3, 0x07, 0x43, 0x3f, 0x35, 0x1a, 0x35,
	0xdd, 0x1c, 0x2b, 0xfc, 0x52, 0xe1, 0x6e, 0x47, 0x5a, 0x47, 0x31, 0x70, 0x91, 0x4a, 0x2e, 0x94,
	0xd2, 0x28, 0x50, 0x6a, 0x65, 0x0b, 0xbd, 0xfb, 0x20, 0xff, 0x09, 0xea, 0x11, 0xa8, 0xba, 0xed,
	0x8b, 0x28, 0x02, 0xc3, 0x75, 0x9a, 0x2b, 0x16, 0xa8, 0x77, 0xcb, 0xff, 0xca, 0xab, 0x76, 0xd6,
	0xe1, 0x61, 0x66, 0x72, 0x41, 0xd9, 0xdf, 0x9b, 0xef, 0xa3, 0x4c, 0xc0, 0xa2, 0x48, 0xd2, 0x42,
	0xe0, 0x7d, 0x75, 0xc8, 0xf6, 0x0b, 0x03, 0x02, 0xe1, 0x3c, 0x8d, 0xb5, 0x08, 0x4f, 0x75, 0x90,
	0xef, 0x6f, 0x82, 0x4d, 0xb5, 0xb2, 0x40, 0x77, 0x08, 0xb1, 0x32, 0x52, 0x10, 0xb6, 0x32, 0x13,
	0xd7, 0x1c, 0xe6, 0x1c, 0x54, 0x9b, 0xd5, 0x62, 0xe5, 0xdc, 0xc4, 0xa3, 0xb6, 0x12, 0x28, 0x7b,
	0x90, 0xb7, 0x2b, 0x45, 0xbb, 0x58, 0x19, 0xb5, 0x8f, 0x09, 0x81, 0x41, 0x2a, 0x0d, 0xd8, 0x96,
	0xc0, 0xda, 0x1a, 0x73, 0x0e, 0x36, 0x0e, 0x5d, 0xbf, 0x80, 0xf2, 0xc7, 0x50, 0xfe, 0xbb, 0x31,
	0x54, 0xb3, 0x5a, 0xaa, 0x4f, 0xd0, 0xfb, 0xe6, 0x90, 0xbb, 0x8b, 0xc9, 0x3e, 0x65, 0x60, 0x91,
	0xd6, 0xc8, 0x8d, 0xd4, 0xe8, 0x0f, 0x10, 0x60, 0x49, 0x35, 0x2e, 0xe9, 0x16, 0x59, 0x0f, 0x75,
	0x22, 0xa4, 0x2a, 0x79, 0xca, 0x8a, 0xba, 0xe4, 0x66, 0x47, 0xc6, 0xa0, 0x44, 0x02, 0x39, 0x4a,
	0xb5, 0x39, 0xa9, 0xe9, 0xd3, 0x29, 0xa8, 0x54, 0xb5, 0x6b, 0x39, 0xe8, 0x9d, 0xbf, 0x40, 0x1b,
	0xe5, 0xe9, 0x4e, 0x38, 0x5f, 0x2a, 0xba, 0x47, 0x36, 0x02, 0xad, 0x10, 0x14, 0xb6, 0x92, 0xf0,
	0xa8, 0x76, 0x9d, 0x39, 0x07, 0xb7, 0x9a, 0xa4, 0x5c, 0x3a, 0x0b, 0x8f, 0xbc, 0x01, 0xd9, 0x29,
	0x7c, 0x34, 0x74, 0x5f, 0x2d, 0x72, 0x32, 0x7b, 0x86, 0xce, 0xfc, 0x19, 0xce, 0xa2, 0x55, 0x56,
	0x47, 0xf3, 0x2e, 0xc8, 0xee, 0xb2, 0x2f, 0xaf, 0x96, 0xee, 0x6c, 0x7c, 0x95, 0x7f, 0x88, 0xef,
	0xf0, 0xf7, 0x1a, 0xd9, 0x6c, 0x08, 0x14, 0x6f, 0x46, 0xb3, 0xf0, 0xb6, 0xb8, 0xfa, 0xf4, 0xa7,
	0x43, 0x6e, 0x2f, 0xca, 0x94, 0xd6, 0xfd, 0xf9, 0x31, 0xf1, 0xaf, 0xc8, 0xde, 0xf5, 0x57, 0x95,
	0x17, 0x36, 0xbd, 0xe1, 0xe5, 0xc9, 0x99, 0xfb, 0xba, 0x90, 0x58, 0x26, 0x58, 0xdf, 0x48, 0x84,
	0xba, 0x56, 0xf1, 0x90, 0x75, 0x11, 0x53, 0x16, 0x97, 0x1b, 0x18, 0x76, 0x05, 0x32, 0x69, 0x99,
	0x08, 0x02, 0xb0, 0x56, 0xb6, 0x63, 0x60, 0x1d, 0x6d, 0x18, 0x0a, 0xfb, 0xd1, 0x32, 0x81, 0xcc,
	0x64, 0x6a, 0x34, 0x41, 0xfe, 0xe7, 0xef, 0x3f, 0xbe, 0x54, 0xf6, 0xbd, 0xdd, 0x7c, 0x88, 0x7b,
	0x8f, 0xa6, 0x53, 0xcf, 0x85, 0x41, 0xd9, 0x11, 0x01, 0xb6, 0x32, 0xa3, 0x9e, 0x39, 0xf7, 0xe9,
	0x2f, 0x87, 0x6c, 0x2d, 0x0e, 0x81, 0xf2, 0x65, 0x2e, 0x96, 0x5c, 0x14, 0xf7, 0xe1, 0xea, 0x1b,
	0x4a, 0xe3, 0x17, 0x97, 0x27, 0xa7, 0xee, 0xab, 0xa9, 0x71, 0x03, 0x22, 0xfc, 0x6f, 0xdf, 0xf7,
	0xe8, 0xfe, 0xd5, 0xbe, 0x5b, 0x08, 0x16, 0x9f, 0x1f, 0xbf, 0x7f, 0x12, 0x49, 0xec, 0x66, 0x6d,
	0x3f, 0xd0, 0x09, 0xcf, 0xc9, 0xb5, 0x89, 0xf8, 0xe4, 0xc5, 0x8c, 0x40, 0xf1, 0xb4, 0x5d, 0x8f,
	0x34, 0x9f, 0x7f, 0x44, 0xdb, 0xeb, 0xf9, 0xdd, 0x7a, 0xfc, 0x27, 0x00, 0x00, 0xff, 0xff, 0x24,
	0x80, 0x11, 0x55, 0x5f, 0x05, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// DataProxyServiceClient is the client API for DataProxyService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type DataProxyServiceClient interface {
	// CreateUploadLocation creates a signed url to upload artifacts to for a given project/domain.
	CreateUploadLocation(ctx context.Context, in *CreateUploadLocationRequest, opts ...grpc.CallOption) (*CreateUploadLocationResponse, error)
	// CreateDownloadLocation creates a signed url to download artifacts.
	CreateDownloadLocation(ctx context.Context, in *CreateDownloadLocationRequest, opts ...grpc.CallOption) (*CreateDownloadLocationResponse, error)
}

type dataProxyServiceClient struct {
	cc *grpc.ClientConn
}

func NewDataProxyServiceClient(cc *grpc.ClientConn) DataProxyServiceClient {
	return &dataProxyServiceClient{cc}
}

func (c *dataProxyServiceClient) CreateUploadLocation(ctx context.Context, in *CreateUploadLocationRequest, opts ...grpc.CallOption) (*CreateUploadLocationResponse, error) {
	out := new(CreateUploadLocationResponse)
	err := c.cc.Invoke(ctx, "/flyteidl.service.DataProxyService/CreateUploadLocation", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *dataProxyServiceClient) CreateDownloadLocation(ctx context.Context, in *CreateDownloadLocationRequest, opts ...grpc.CallOption) (*CreateDownloadLocationResponse, error) {
	out := new(CreateDownloadLocationResponse)
	err := c.cc.Invoke(ctx, "/flyteidl.service.DataProxyService/CreateDownloadLocation", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DataProxyServiceServer is the server API for DataProxyService service.
type DataProxyServiceServer interface {
	// CreateUploadLocation creates a signed url to upload artifacts to for a given project/domain.
	CreateUploadLocation(context.Context, *CreateUploadLocationRequest) (*CreateUploadLocationResponse, error)
	// CreateDownloadLocation creates a signed url to download artifacts.
	CreateDownloadLocation(context.Context, *CreateDownloadLocationRequest) (*CreateDownloadLocationResponse, error)
}

// UnimplementedDataProxyServiceServer can be embedded to have forward compatible implementations.
type UnimplementedDataProxyServiceServer struct {
}

func (*UnimplementedDataProxyServiceServer) CreateUploadLocation(ctx context.Context, req *CreateUploadLocationRequest) (*CreateUploadLocationResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateUploadLocation not implemented")
}
func (*UnimplementedDataProxyServiceServer) CreateDownloadLocation(ctx context.Context, req *CreateDownloadLocationRequest) (*CreateDownloadLocationResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateDownloadLocation not implemented")
}

func RegisterDataProxyServiceServer(s *grpc.Server, srv DataProxyServiceServer) {
	s.RegisterService(&_DataProxyService_serviceDesc, srv)
}

func _DataProxyService_CreateUploadLocation_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateUploadLocationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DataProxyServiceServer).CreateUploadLocation(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/flyteidl.service.DataProxyService/CreateUploadLocation",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DataProxyServiceServer).CreateUploadLocation(ctx, req.(*CreateUploadLocationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DataProxyService_CreateDownloadLocation_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateDownloadLocationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DataProxyServiceServer).CreateDownloadLocation(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/flyteidl.service.DataProxyService/CreateDownloadLocation",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DataProxyServiceServer).CreateDownloadLocation(ctx, req.(*CreateDownloadLocationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _DataProxyService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "flyteidl.service.DataProxyService",
	HandlerType: (*DataProxyServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CreateUploadLocation",
			Handler:    _DataProxyService_CreateUploadLocation_Handler,
		},
		{
			MethodName: "CreateDownloadLocation",
			Handler:    _DataProxyService_CreateDownloadLocation_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "flyteidl/service/dataproxy.proto",
}

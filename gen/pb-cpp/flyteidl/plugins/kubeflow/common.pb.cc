// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: flyteidl/plugins/kubeflow/common.proto

#include "flyteidl/plugins/kubeflow/common.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>

namespace flyteidl {
namespace plugins {
namespace kubeflow {
class RunPolicyDefaultTypeInternal {
 public:
  ::google::protobuf::internal::ExplicitlyConstructed<RunPolicy> _instance;
} _RunPolicy_default_instance_;
}  // namespace kubeflow
}  // namespace plugins
}  // namespace flyteidl
static void InitDefaultsRunPolicy_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::flyteidl::plugins::kubeflow::_RunPolicy_default_instance_;
    new (ptr) ::flyteidl::plugins::kubeflow::RunPolicy();
    ::google::protobuf::internal::OnShutdownDestroyMessage(ptr);
  }
  ::flyteidl::plugins::kubeflow::RunPolicy::InitAsDefaultInstance();
}

::google::protobuf::internal::SCCInfo<0> scc_info_RunPolicy_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto =
    {{ATOMIC_VAR_INIT(::google::protobuf::internal::SCCInfoBase::kUninitialized), 0, InitDefaultsRunPolicy_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto}, {}};

void InitDefaults_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto() {
  ::google::protobuf::internal::InitSCC(&scc_info_RunPolicy_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto.base);
}

::google::protobuf::Metadata file_level_metadata_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto[1];
const ::google::protobuf::EnumDescriptor* file_level_enum_descriptors_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto[3];
constexpr ::google::protobuf::ServiceDescriptor const** file_level_service_descriptors_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto = nullptr;

const ::google::protobuf::uint32 TableStruct_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::kubeflow::RunPolicy, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::kubeflow::RunPolicy, clean_pod_policy_),
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::kubeflow::RunPolicy, ttl_seconds_after_finished_),
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::kubeflow::RunPolicy, activedeadlineseconds_),
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::kubeflow::RunPolicy, backoff_limit_),
};
static const ::google::protobuf::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, sizeof(::flyteidl::plugins::kubeflow::RunPolicy)},
};

static ::google::protobuf::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::google::protobuf::Message*>(&::flyteidl::plugins::kubeflow::_RunPolicy_default_instance_),
};

::google::protobuf::internal::AssignDescriptorsTable assign_descriptors_table_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto = {
  {}, AddDescriptors_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto, "flyteidl/plugins/kubeflow/common.proto", schemas,
  file_default_instances, TableStruct_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto::offsets,
  file_level_metadata_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto, 1, file_level_enum_descriptors_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto, file_level_service_descriptors_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto,
};

const char descriptor_table_protodef_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto[] =
  "\n&flyteidl/plugins/kubeflow/common.proto"
  "\022\031flyteidl.plugins.kubeflow\"\252\001\n\tRunPolic"
  "y\022C\n\020clean_pod_policy\030\001 \001(\0162).flyteidl.p"
  "lugins.kubeflow.CleanPodPolicy\022\"\n\032ttl_se"
  "conds_after_finished\030\002 \001(\005\022\035\n\025activeDead"
  "lineSeconds\030\003 \001(\005\022\025\n\rbackoff_limit\030\004 \001(\005"
  "*K\n\rSuccessPolicy\022\032\n\026SUCCESS_POLICY_DEFA"
  "ULT\020\000\022\036\n\032SUCCESS_POLICY_ALL_WORKERS\020\001*\177\n"
  "\016CleanPodPolicy\022\035\n\031CLEANPOD_POLICY_UNDEF"
  "INED\020\000\022\027\n\023CLEANPOD_POLICY_ALL\020\001\022\033\n\027CLEAN"
  "POD_POLICY_RUNNING\020\002\022\030\n\024CLEANPOD_POLICY_"
  "NONE\020\003*c\n\rRestartPolicy\022\031\n\025RESTART_POLIC"
  "Y_ALWAYS\020\000\022\035\n\031RESTART_POLICY_ON_FAILURE\020"
  "\001\022\030\n\024RESTART_POLICY_NEVER\020\002B9Z7github.co"
  "m/flyteorg/flyteidl/gen/pb-go/flyteidl/p"
  "luginsb\006proto3"
  ;
::google::protobuf::internal::DescriptorTable descriptor_table_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto = {
  false, InitDefaults_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto, 
  descriptor_table_protodef_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto,
  "flyteidl/plugins/kubeflow/common.proto", &assign_descriptors_table_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto, 614,
};

void AddDescriptors_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto() {
  static constexpr ::google::protobuf::internal::InitFunc deps[1] =
  {
  };
 ::google::protobuf::internal::AddDescriptors(&descriptor_table_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto, deps, 0);
}

// Force running AddDescriptors() at dynamic initialization time.
static bool dynamic_init_dummy_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto = []() { AddDescriptors_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto(); return true; }();
namespace flyteidl {
namespace plugins {
namespace kubeflow {
const ::google::protobuf::EnumDescriptor* SuccessPolicy_descriptor() {
  ::google::protobuf::internal::AssignDescriptors(&assign_descriptors_table_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto);
  return file_level_enum_descriptors_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto[0];
}
bool SuccessPolicy_IsValid(int value) {
  switch (value) {
    case 0:
    case 1:
      return true;
    default:
      return false;
  }
}

const ::google::protobuf::EnumDescriptor* CleanPodPolicy_descriptor() {
  ::google::protobuf::internal::AssignDescriptors(&assign_descriptors_table_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto);
  return file_level_enum_descriptors_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto[1];
}
bool CleanPodPolicy_IsValid(int value) {
  switch (value) {
    case 0:
    case 1:
    case 2:
    case 3:
      return true;
    default:
      return false;
  }
}

const ::google::protobuf::EnumDescriptor* RestartPolicy_descriptor() {
  ::google::protobuf::internal::AssignDescriptors(&assign_descriptors_table_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto);
  return file_level_enum_descriptors_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto[2];
}
bool RestartPolicy_IsValid(int value) {
  switch (value) {
    case 0:
    case 1:
    case 2:
      return true;
    default:
      return false;
  }
}


// ===================================================================

void RunPolicy::InitAsDefaultInstance() {
}
class RunPolicy::HasBitSetters {
 public:
};

#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int RunPolicy::kCleanPodPolicyFieldNumber;
const int RunPolicy::kTtlSecondsAfterFinishedFieldNumber;
const int RunPolicy::kActiveDeadlineSecondsFieldNumber;
const int RunPolicy::kBackoffLimitFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

RunPolicy::RunPolicy()
  : ::google::protobuf::Message(), _internal_metadata_(nullptr) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:flyteidl.plugins.kubeflow.RunPolicy)
}
RunPolicy::RunPolicy(const RunPolicy& from)
  : ::google::protobuf::Message(),
      _internal_metadata_(nullptr) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::memcpy(&clean_pod_policy_, &from.clean_pod_policy_,
    static_cast<size_t>(reinterpret_cast<char*>(&backoff_limit_) -
    reinterpret_cast<char*>(&clean_pod_policy_)) + sizeof(backoff_limit_));
  // @@protoc_insertion_point(copy_constructor:flyteidl.plugins.kubeflow.RunPolicy)
}

void RunPolicy::SharedCtor() {
  ::memset(&clean_pod_policy_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&backoff_limit_) -
      reinterpret_cast<char*>(&clean_pod_policy_)) + sizeof(backoff_limit_));
}

RunPolicy::~RunPolicy() {
  // @@protoc_insertion_point(destructor:flyteidl.plugins.kubeflow.RunPolicy)
  SharedDtor();
}

void RunPolicy::SharedDtor() {
}

void RunPolicy::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const RunPolicy& RunPolicy::default_instance() {
  ::google::protobuf::internal::InitSCC(&::scc_info_RunPolicy_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto.base);
  return *internal_default_instance();
}


void RunPolicy::Clear() {
// @@protoc_insertion_point(message_clear_start:flyteidl.plugins.kubeflow.RunPolicy)
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  ::memset(&clean_pod_policy_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&backoff_limit_) -
      reinterpret_cast<char*>(&clean_pod_policy_)) + sizeof(backoff_limit_));
  _internal_metadata_.Clear();
}

#if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
const char* RunPolicy::_InternalParse(const char* begin, const char* end, void* object,
                  ::google::protobuf::internal::ParseContext* ctx) {
  auto msg = static_cast<RunPolicy*>(object);
  ::google::protobuf::int32 size; (void)size;
  int depth; (void)depth;
  ::google::protobuf::uint32 tag;
  ::google::protobuf::internal::ParseFunc parser_till_end; (void)parser_till_end;
  auto ptr = begin;
  while (ptr < end) {
    ptr = ::google::protobuf::io::Parse32(ptr, &tag);
    GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
    switch (tag >> 3) {
      // .flyteidl.plugins.kubeflow.CleanPodPolicy clean_pod_policy = 1;
      case 1: {
        if (static_cast<::google::protobuf::uint8>(tag) != 8) goto handle_unusual;
        ::google::protobuf::uint64 val = ::google::protobuf::internal::ReadVarint(&ptr);
        msg->set_clean_pod_policy(static_cast<::flyteidl::plugins::kubeflow::CleanPodPolicy>(val));
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        break;
      }
      // int32 ttl_seconds_after_finished = 2;
      case 2: {
        if (static_cast<::google::protobuf::uint8>(tag) != 16) goto handle_unusual;
        msg->set_ttl_seconds_after_finished(::google::protobuf::internal::ReadVarint(&ptr));
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        break;
      }
      // int32 activeDeadlineSeconds = 3;
      case 3: {
        if (static_cast<::google::protobuf::uint8>(tag) != 24) goto handle_unusual;
        msg->set_activedeadlineseconds(::google::protobuf::internal::ReadVarint(&ptr));
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        break;
      }
      // int32 backoff_limit = 4;
      case 4: {
        if (static_cast<::google::protobuf::uint8>(tag) != 32) goto handle_unusual;
        msg->set_backoff_limit(::google::protobuf::internal::ReadVarint(&ptr));
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        break;
      }
      default: {
      handle_unusual:
        if ((tag & 7) == 4 || tag == 0) {
          ctx->EndGroup(tag);
          return ptr;
        }
        auto res = UnknownFieldParse(tag, {_InternalParse, msg},
          ptr, end, msg->_internal_metadata_.mutable_unknown_fields(), ctx);
        ptr = res.first;
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr != nullptr);
        if (res.second) return ptr;
      }
    }  // switch
  }  // while
  return ptr;
}
#else  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
bool RunPolicy::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!PROTOBUF_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:flyteidl.plugins.kubeflow.RunPolicy)
  for (;;) {
    ::std::pair<::google::protobuf::uint32, bool> p = input->ReadTagWithCutoffNoLastTag(127u);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // .flyteidl.plugins.kubeflow.CleanPodPolicy clean_pod_policy = 1;
      case 1: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (8 & 0xFF)) {
          int value = 0;
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   int, ::google::protobuf::internal::WireFormatLite::TYPE_ENUM>(
                 input, &value)));
          set_clean_pod_policy(static_cast< ::flyteidl::plugins::kubeflow::CleanPodPolicy >(value));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // int32 ttl_seconds_after_finished = 2;
      case 2: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (16 & 0xFF)) {

          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int32, ::google::protobuf::internal::WireFormatLite::TYPE_INT32>(
                 input, &ttl_seconds_after_finished_)));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // int32 activeDeadlineSeconds = 3;
      case 3: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (24 & 0xFF)) {

          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int32, ::google::protobuf::internal::WireFormatLite::TYPE_INT32>(
                 input, &activedeadlineseconds_)));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // int32 backoff_limit = 4;
      case 4: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (32 & 0xFF)) {

          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int32, ::google::protobuf::internal::WireFormatLite::TYPE_INT32>(
                 input, &backoff_limit_)));
        } else {
          goto handle_unusual;
        }
        break;
      }

      default: {
      handle_unusual:
        if (tag == 0) {
          goto success;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, _internal_metadata_.mutable_unknown_fields()));
        break;
      }
    }
  }
success:
  // @@protoc_insertion_point(parse_success:flyteidl.plugins.kubeflow.RunPolicy)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:flyteidl.plugins.kubeflow.RunPolicy)
  return false;
#undef DO_
}
#endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER

void RunPolicy::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:flyteidl.plugins.kubeflow.RunPolicy)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // .flyteidl.plugins.kubeflow.CleanPodPolicy clean_pod_policy = 1;
  if (this->clean_pod_policy() != 0) {
    ::google::protobuf::internal::WireFormatLite::WriteEnum(
      1, this->clean_pod_policy(), output);
  }

  // int32 ttl_seconds_after_finished = 2;
  if (this->ttl_seconds_after_finished() != 0) {
    ::google::protobuf::internal::WireFormatLite::WriteInt32(2, this->ttl_seconds_after_finished(), output);
  }

  // int32 activeDeadlineSeconds = 3;
  if (this->activedeadlineseconds() != 0) {
    ::google::protobuf::internal::WireFormatLite::WriteInt32(3, this->activedeadlineseconds(), output);
  }

  // int32 backoff_limit = 4;
  if (this->backoff_limit() != 0) {
    ::google::protobuf::internal::WireFormatLite::WriteInt32(4, this->backoff_limit(), output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        _internal_metadata_.unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:flyteidl.plugins.kubeflow.RunPolicy)
}

::google::protobuf::uint8* RunPolicy::InternalSerializeWithCachedSizesToArray(
    ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:flyteidl.plugins.kubeflow.RunPolicy)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // .flyteidl.plugins.kubeflow.CleanPodPolicy clean_pod_policy = 1;
  if (this->clean_pod_policy() != 0) {
    target = ::google::protobuf::internal::WireFormatLite::WriteEnumToArray(
      1, this->clean_pod_policy(), target);
  }

  // int32 ttl_seconds_after_finished = 2;
  if (this->ttl_seconds_after_finished() != 0) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt32ToArray(2, this->ttl_seconds_after_finished(), target);
  }

  // int32 activeDeadlineSeconds = 3;
  if (this->activedeadlineseconds() != 0) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt32ToArray(3, this->activedeadlineseconds(), target);
  }

  // int32 backoff_limit = 4;
  if (this->backoff_limit() != 0) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt32ToArray(4, this->backoff_limit(), target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:flyteidl.plugins.kubeflow.RunPolicy)
  return target;
}

size_t RunPolicy::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:flyteidl.plugins.kubeflow.RunPolicy)
  size_t total_size = 0;

  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        _internal_metadata_.unknown_fields());
  }
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // .flyteidl.plugins.kubeflow.CleanPodPolicy clean_pod_policy = 1;
  if (this->clean_pod_policy() != 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::EnumSize(this->clean_pod_policy());
  }

  // int32 ttl_seconds_after_finished = 2;
  if (this->ttl_seconds_after_finished() != 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::Int32Size(
        this->ttl_seconds_after_finished());
  }

  // int32 activeDeadlineSeconds = 3;
  if (this->activedeadlineseconds() != 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::Int32Size(
        this->activedeadlineseconds());
  }

  // int32 backoff_limit = 4;
  if (this->backoff_limit() != 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::Int32Size(
        this->backoff_limit());
  }

  int cached_size = ::google::protobuf::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void RunPolicy::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:flyteidl.plugins.kubeflow.RunPolicy)
  GOOGLE_DCHECK_NE(&from, this);
  const RunPolicy* source =
      ::google::protobuf::DynamicCastToGenerated<RunPolicy>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:flyteidl.plugins.kubeflow.RunPolicy)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:flyteidl.plugins.kubeflow.RunPolicy)
    MergeFrom(*source);
  }
}

void RunPolicy::MergeFrom(const RunPolicy& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:flyteidl.plugins.kubeflow.RunPolicy)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.clean_pod_policy() != 0) {
    set_clean_pod_policy(from.clean_pod_policy());
  }
  if (from.ttl_seconds_after_finished() != 0) {
    set_ttl_seconds_after_finished(from.ttl_seconds_after_finished());
  }
  if (from.activedeadlineseconds() != 0) {
    set_activedeadlineseconds(from.activedeadlineseconds());
  }
  if (from.backoff_limit() != 0) {
    set_backoff_limit(from.backoff_limit());
  }
}

void RunPolicy::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:flyteidl.plugins.kubeflow.RunPolicy)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void RunPolicy::CopyFrom(const RunPolicy& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:flyteidl.plugins.kubeflow.RunPolicy)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool RunPolicy::IsInitialized() const {
  return true;
}

void RunPolicy::Swap(RunPolicy* other) {
  if (other == this) return;
  InternalSwap(other);
}
void RunPolicy::InternalSwap(RunPolicy* other) {
  using std::swap;
  _internal_metadata_.Swap(&other->_internal_metadata_);
  swap(clean_pod_policy_, other->clean_pod_policy_);
  swap(ttl_seconds_after_finished_, other->ttl_seconds_after_finished_);
  swap(activedeadlineseconds_, other->activedeadlineseconds_);
  swap(backoff_limit_, other->backoff_limit_);
}

::google::protobuf::Metadata RunPolicy::GetMetadata() const {
  ::google::protobuf::internal::AssignDescriptors(&::assign_descriptors_table_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto);
  return ::file_level_metadata_flyteidl_2fplugins_2fkubeflow_2fcommon_2eproto[kIndexInFileMessages];
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace kubeflow
}  // namespace plugins
}  // namespace flyteidl
namespace google {
namespace protobuf {
template<> PROTOBUF_NOINLINE ::flyteidl::plugins::kubeflow::RunPolicy* Arena::CreateMaybeMessage< ::flyteidl::plugins::kubeflow::RunPolicy >(Arena* arena) {
  return Arena::CreateInternal< ::flyteidl::plugins::kubeflow::RunPolicy >(arena);
}
}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>

// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: flyteidl/plugins/sagemaker/hpojob.proto

#include "flyteidl/plugins/sagemaker/hpojob.pb.h"

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

extern PROTOBUF_INTERNAL_EXPORT_flyteidl_2fplugins_2fsagemaker_2ftrainingjob_2eproto ::google::protobuf::internal::SCCInfo<4> scc_info_TrainingJob_flyteidl_2fplugins_2fsagemaker_2ftrainingjob_2eproto;
namespace flyteidl {
namespace plugins {
namespace sagemaker {
class HPOJobObjectiveDefaultTypeInternal {
 public:
  ::google::protobuf::internal::ExplicitlyConstructed<HPOJobObjective> _instance;
} _HPOJobObjective_default_instance_;
class HPOJobDefaultTypeInternal {
 public:
  ::google::protobuf::internal::ExplicitlyConstructed<HPOJob> _instance;
} _HPOJob_default_instance_;
}  // namespace sagemaker
}  // namespace plugins
}  // namespace flyteidl
static void InitDefaultsHPOJobObjective_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::flyteidl::plugins::sagemaker::_HPOJobObjective_default_instance_;
    new (ptr) ::flyteidl::plugins::sagemaker::HPOJobObjective();
    ::google::protobuf::internal::OnShutdownDestroyMessage(ptr);
  }
  ::flyteidl::plugins::sagemaker::HPOJobObjective::InitAsDefaultInstance();
}

::google::protobuf::internal::SCCInfo<0> scc_info_HPOJobObjective_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto =
    {{ATOMIC_VAR_INIT(::google::protobuf::internal::SCCInfoBase::kUninitialized), 0, InitDefaultsHPOJobObjective_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto}, {}};

static void InitDefaultsHPOJob_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::flyteidl::plugins::sagemaker::_HPOJob_default_instance_;
    new (ptr) ::flyteidl::plugins::sagemaker::HPOJob();
    ::google::protobuf::internal::OnShutdownDestroyMessage(ptr);
  }
  ::flyteidl::plugins::sagemaker::HPOJob::InitAsDefaultInstance();
}

::google::protobuf::internal::SCCInfo<1> scc_info_HPOJob_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto =
    {{ATOMIC_VAR_INIT(::google::protobuf::internal::SCCInfoBase::kUninitialized), 1, InitDefaultsHPOJob_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto}, {
      &scc_info_TrainingJob_flyteidl_2fplugins_2fsagemaker_2ftrainingjob_2eproto.base,}};

void InitDefaults_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto() {
  ::google::protobuf::internal::InitSCC(&scc_info_HPOJobObjective_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto.base);
  ::google::protobuf::internal::InitSCC(&scc_info_HPOJob_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto.base);
}

::google::protobuf::Metadata file_level_metadata_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto[2];
const ::google::protobuf::EnumDescriptor* file_level_enum_descriptors_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto[1];
constexpr ::google::protobuf::ServiceDescriptor const** file_level_service_descriptors_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto = nullptr;

const ::google::protobuf::uint32 TableStruct_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::sagemaker::HPOJobObjective, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::sagemaker::HPOJobObjective, type_),
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::sagemaker::HPOJobObjective, metric_name_),
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::sagemaker::HPOJob, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::sagemaker::HPOJob, max_number_of_training_jobs_),
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::sagemaker::HPOJob, max_parallel_training_jobs_),
  PROTOBUF_FIELD_OFFSET(::flyteidl::plugins::sagemaker::HPOJob, training_job_),
};
static const ::google::protobuf::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, sizeof(::flyteidl::plugins::sagemaker::HPOJobObjective)},
  { 7, -1, sizeof(::flyteidl::plugins::sagemaker::HPOJob)},
};

static ::google::protobuf::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::google::protobuf::Message*>(&::flyteidl::plugins::sagemaker::_HPOJobObjective_default_instance_),
  reinterpret_cast<const ::google::protobuf::Message*>(&::flyteidl::plugins::sagemaker::_HPOJob_default_instance_),
};

::google::protobuf::internal::AssignDescriptorsTable assign_descriptors_table_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto = {
  {}, AddDescriptors_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto, "flyteidl/plugins/sagemaker/hpojob.proto", schemas,
  file_default_instances, TableStruct_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto::offsets,
  file_level_metadata_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto, 2, file_level_enum_descriptors_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto, file_level_service_descriptors_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto,
};

const char descriptor_table_protodef_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto[] =
  "\n\'flyteidl/plugins/sagemaker/hpojob.prot"
  "o\022\032flyteidl.plugins.sagemaker\0320flyteidl/"
  "plugins/sagemaker/parameterranges.proto\032"
  ",flyteidl/plugins/sagemaker/trainingjob."
  "proto\"\250\001\n\017HPOJobObjective\022M\n\004type\030\001 \001(\0162"
  "\?.flyteidl.plugins.sagemaker.HPOJobObjec"
  "tive.HPOJobObjectiveType\022\023\n\013metric_name\030"
  "\002 \001(\t\"1\n\023HPOJobObjectiveType\022\014\n\010MINIMIZE"
  "\020\000\022\014\n\010MAXIMIZE\020\001\"\220\001\n\006HPOJob\022#\n\033max_numbe"
  "r_of_training_jobs\030\001 \001(\003\022\"\n\032max_parallel"
  "_training_jobs\030\002 \001(\003\022=\n\014training_job\030\003 \001"
  "(\0132\'.flyteidl.plugins.sagemaker.Training"
  "JobB5Z3github.com/lyft/flyteidl/gen/pb-g"
  "o/flyteidl/pluginsb\006proto3"
  ;
::google::protobuf::internal::DescriptorTable descriptor_table_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto = {
  false, InitDefaults_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto, 
  descriptor_table_protodef_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto,
  "flyteidl/plugins/sagemaker/hpojob.proto", &assign_descriptors_table_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto, 546,
};

void AddDescriptors_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto() {
  static constexpr ::google::protobuf::internal::InitFunc deps[2] =
  {
    ::AddDescriptors_flyteidl_2fplugins_2fsagemaker_2fparameterranges_2eproto,
    ::AddDescriptors_flyteidl_2fplugins_2fsagemaker_2ftrainingjob_2eproto,
  };
 ::google::protobuf::internal::AddDescriptors(&descriptor_table_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto, deps, 2);
}

// Force running AddDescriptors() at dynamic initialization time.
static bool dynamic_init_dummy_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto = []() { AddDescriptors_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto(); return true; }();
namespace flyteidl {
namespace plugins {
namespace sagemaker {
const ::google::protobuf::EnumDescriptor* HPOJobObjective_HPOJobObjectiveType_descriptor() {
  ::google::protobuf::internal::AssignDescriptors(&assign_descriptors_table_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto);
  return file_level_enum_descriptors_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto[0];
}
bool HPOJobObjective_HPOJobObjectiveType_IsValid(int value) {
  switch (value) {
    case 0:
    case 1:
      return true;
    default:
      return false;
  }
}

#if !defined(_MSC_VER) || _MSC_VER >= 1900
const HPOJobObjective_HPOJobObjectiveType HPOJobObjective::MINIMIZE;
const HPOJobObjective_HPOJobObjectiveType HPOJobObjective::MAXIMIZE;
const HPOJobObjective_HPOJobObjectiveType HPOJobObjective::HPOJobObjectiveType_MIN;
const HPOJobObjective_HPOJobObjectiveType HPOJobObjective::HPOJobObjectiveType_MAX;
const int HPOJobObjective::HPOJobObjectiveType_ARRAYSIZE;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

// ===================================================================

void HPOJobObjective::InitAsDefaultInstance() {
}
class HPOJobObjective::HasBitSetters {
 public:
};

#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int HPOJobObjective::kTypeFieldNumber;
const int HPOJobObjective::kMetricNameFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

HPOJobObjective::HPOJobObjective()
  : ::google::protobuf::Message(), _internal_metadata_(nullptr) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:flyteidl.plugins.sagemaker.HPOJobObjective)
}
HPOJobObjective::HPOJobObjective(const HPOJobObjective& from)
  : ::google::protobuf::Message(),
      _internal_metadata_(nullptr) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  metric_name_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  if (from.metric_name().size() > 0) {
    metric_name_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.metric_name_);
  }
  type_ = from.type_;
  // @@protoc_insertion_point(copy_constructor:flyteidl.plugins.sagemaker.HPOJobObjective)
}

void HPOJobObjective::SharedCtor() {
  ::google::protobuf::internal::InitSCC(
      &scc_info_HPOJobObjective_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto.base);
  metric_name_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  type_ = 0;
}

HPOJobObjective::~HPOJobObjective() {
  // @@protoc_insertion_point(destructor:flyteidl.plugins.sagemaker.HPOJobObjective)
  SharedDtor();
}

void HPOJobObjective::SharedDtor() {
  metric_name_.DestroyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}

void HPOJobObjective::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const HPOJobObjective& HPOJobObjective::default_instance() {
  ::google::protobuf::internal::InitSCC(&::scc_info_HPOJobObjective_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto.base);
  return *internal_default_instance();
}


void HPOJobObjective::Clear() {
// @@protoc_insertion_point(message_clear_start:flyteidl.plugins.sagemaker.HPOJobObjective)
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  metric_name_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  type_ = 0;
  _internal_metadata_.Clear();
}

#if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
const char* HPOJobObjective::_InternalParse(const char* begin, const char* end, void* object,
                  ::google::protobuf::internal::ParseContext* ctx) {
  auto msg = static_cast<HPOJobObjective*>(object);
  ::google::protobuf::int32 size; (void)size;
  int depth; (void)depth;
  ::google::protobuf::uint32 tag;
  ::google::protobuf::internal::ParseFunc parser_till_end; (void)parser_till_end;
  auto ptr = begin;
  while (ptr < end) {
    ptr = ::google::protobuf::io::Parse32(ptr, &tag);
    GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
    switch (tag >> 3) {
      // .flyteidl.plugins.sagemaker.HPOJobObjective.HPOJobObjectiveType type = 1;
      case 1: {
        if (static_cast<::google::protobuf::uint8>(tag) != 8) goto handle_unusual;
        ::google::protobuf::uint64 val = ::google::protobuf::internal::ReadVarint(&ptr);
        msg->set_type(static_cast<::flyteidl::plugins::sagemaker::HPOJobObjective_HPOJobObjectiveType>(val));
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        break;
      }
      // string metric_name = 2;
      case 2: {
        if (static_cast<::google::protobuf::uint8>(tag) != 18) goto handle_unusual;
        ptr = ::google::protobuf::io::ReadSize(ptr, &size);
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        ctx->extra_parse_data().SetFieldName("flyteidl.plugins.sagemaker.HPOJobObjective.metric_name");
        object = msg->mutable_metric_name();
        if (size > end - ptr + ::google::protobuf::internal::ParseContext::kSlopBytes) {
          parser_till_end = ::google::protobuf::internal::GreedyStringParserUTF8;
          goto string_till_end;
        }
        GOOGLE_PROTOBUF_PARSER_ASSERT(::google::protobuf::internal::StringCheckUTF8(ptr, size, ctx));
        ::google::protobuf::internal::InlineGreedyStringParser(object, ptr, size, ctx);
        ptr += size;
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
string_till_end:
  static_cast<::std::string*>(object)->clear();
  static_cast<::std::string*>(object)->reserve(size);
  goto len_delim_till_end;
len_delim_till_end:
  return ctx->StoreAndTailCall(ptr, end, {_InternalParse, msg},
                               {parser_till_end, object}, size);
}
#else  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
bool HPOJobObjective::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!PROTOBUF_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:flyteidl.plugins.sagemaker.HPOJobObjective)
  for (;;) {
    ::std::pair<::google::protobuf::uint32, bool> p = input->ReadTagWithCutoffNoLastTag(127u);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // .flyteidl.plugins.sagemaker.HPOJobObjective.HPOJobObjectiveType type = 1;
      case 1: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (8 & 0xFF)) {
          int value = 0;
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   int, ::google::protobuf::internal::WireFormatLite::TYPE_ENUM>(
                 input, &value)));
          set_type(static_cast< ::flyteidl::plugins::sagemaker::HPOJobObjective_HPOJobObjectiveType >(value));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // string metric_name = 2;
      case 2: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (18 & 0xFF)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_metric_name()));
          DO_(::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
            this->metric_name().data(), static_cast<int>(this->metric_name().length()),
            ::google::protobuf::internal::WireFormatLite::PARSE,
            "flyteidl.plugins.sagemaker.HPOJobObjective.metric_name"));
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
  // @@protoc_insertion_point(parse_success:flyteidl.plugins.sagemaker.HPOJobObjective)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:flyteidl.plugins.sagemaker.HPOJobObjective)
  return false;
#undef DO_
}
#endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER

void HPOJobObjective::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:flyteidl.plugins.sagemaker.HPOJobObjective)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // .flyteidl.plugins.sagemaker.HPOJobObjective.HPOJobObjectiveType type = 1;
  if (this->type() != 0) {
    ::google::protobuf::internal::WireFormatLite::WriteEnum(
      1, this->type(), output);
  }

  // string metric_name = 2;
  if (this->metric_name().size() > 0) {
    ::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
      this->metric_name().data(), static_cast<int>(this->metric_name().length()),
      ::google::protobuf::internal::WireFormatLite::SERIALIZE,
      "flyteidl.plugins.sagemaker.HPOJobObjective.metric_name");
    ::google::protobuf::internal::WireFormatLite::WriteStringMaybeAliased(
      2, this->metric_name(), output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        _internal_metadata_.unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:flyteidl.plugins.sagemaker.HPOJobObjective)
}

::google::protobuf::uint8* HPOJobObjective::InternalSerializeWithCachedSizesToArray(
    ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:flyteidl.plugins.sagemaker.HPOJobObjective)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // .flyteidl.plugins.sagemaker.HPOJobObjective.HPOJobObjectiveType type = 1;
  if (this->type() != 0) {
    target = ::google::protobuf::internal::WireFormatLite::WriteEnumToArray(
      1, this->type(), target);
  }

  // string metric_name = 2;
  if (this->metric_name().size() > 0) {
    ::google::protobuf::internal::WireFormatLite::VerifyUtf8String(
      this->metric_name().data(), static_cast<int>(this->metric_name().length()),
      ::google::protobuf::internal::WireFormatLite::SERIALIZE,
      "flyteidl.plugins.sagemaker.HPOJobObjective.metric_name");
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        2, this->metric_name(), target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:flyteidl.plugins.sagemaker.HPOJobObjective)
  return target;
}

size_t HPOJobObjective::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:flyteidl.plugins.sagemaker.HPOJobObjective)
  size_t total_size = 0;

  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        _internal_metadata_.unknown_fields());
  }
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // string metric_name = 2;
  if (this->metric_name().size() > 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::StringSize(
        this->metric_name());
  }

  // .flyteidl.plugins.sagemaker.HPOJobObjective.HPOJobObjectiveType type = 1;
  if (this->type() != 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::EnumSize(this->type());
  }

  int cached_size = ::google::protobuf::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void HPOJobObjective::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:flyteidl.plugins.sagemaker.HPOJobObjective)
  GOOGLE_DCHECK_NE(&from, this);
  const HPOJobObjective* source =
      ::google::protobuf::DynamicCastToGenerated<HPOJobObjective>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:flyteidl.plugins.sagemaker.HPOJobObjective)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:flyteidl.plugins.sagemaker.HPOJobObjective)
    MergeFrom(*source);
  }
}

void HPOJobObjective::MergeFrom(const HPOJobObjective& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:flyteidl.plugins.sagemaker.HPOJobObjective)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.metric_name().size() > 0) {

    metric_name_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.metric_name_);
  }
  if (from.type() != 0) {
    set_type(from.type());
  }
}

void HPOJobObjective::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:flyteidl.plugins.sagemaker.HPOJobObjective)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void HPOJobObjective::CopyFrom(const HPOJobObjective& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:flyteidl.plugins.sagemaker.HPOJobObjective)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool HPOJobObjective::IsInitialized() const {
  return true;
}

void HPOJobObjective::Swap(HPOJobObjective* other) {
  if (other == this) return;
  InternalSwap(other);
}
void HPOJobObjective::InternalSwap(HPOJobObjective* other) {
  using std::swap;
  _internal_metadata_.Swap(&other->_internal_metadata_);
  metric_name_.Swap(&other->metric_name_, &::google::protobuf::internal::GetEmptyStringAlreadyInited(),
    GetArenaNoVirtual());
  swap(type_, other->type_);
}

::google::protobuf::Metadata HPOJobObjective::GetMetadata() const {
  ::google::protobuf::internal::AssignDescriptors(&::assign_descriptors_table_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto);
  return ::file_level_metadata_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto[kIndexInFileMessages];
}


// ===================================================================

void HPOJob::InitAsDefaultInstance() {
  ::flyteidl::plugins::sagemaker::_HPOJob_default_instance_._instance.get_mutable()->training_job_ = const_cast< ::flyteidl::plugins::sagemaker::TrainingJob*>(
      ::flyteidl::plugins::sagemaker::TrainingJob::internal_default_instance());
}
class HPOJob::HasBitSetters {
 public:
  static const ::flyteidl::plugins::sagemaker::TrainingJob& training_job(const HPOJob* msg);
};

const ::flyteidl::plugins::sagemaker::TrainingJob&
HPOJob::HasBitSetters::training_job(const HPOJob* msg) {
  return *msg->training_job_;
}
void HPOJob::clear_training_job() {
  if (GetArenaNoVirtual() == nullptr && training_job_ != nullptr) {
    delete training_job_;
  }
  training_job_ = nullptr;
}
#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int HPOJob::kMaxNumberOfTrainingJobsFieldNumber;
const int HPOJob::kMaxParallelTrainingJobsFieldNumber;
const int HPOJob::kTrainingJobFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

HPOJob::HPOJob()
  : ::google::protobuf::Message(), _internal_metadata_(nullptr) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:flyteidl.plugins.sagemaker.HPOJob)
}
HPOJob::HPOJob(const HPOJob& from)
  : ::google::protobuf::Message(),
      _internal_metadata_(nullptr) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  if (from.has_training_job()) {
    training_job_ = new ::flyteidl::plugins::sagemaker::TrainingJob(*from.training_job_);
  } else {
    training_job_ = nullptr;
  }
  ::memcpy(&max_number_of_training_jobs_, &from.max_number_of_training_jobs_,
    static_cast<size_t>(reinterpret_cast<char*>(&max_parallel_training_jobs_) -
    reinterpret_cast<char*>(&max_number_of_training_jobs_)) + sizeof(max_parallel_training_jobs_));
  // @@protoc_insertion_point(copy_constructor:flyteidl.plugins.sagemaker.HPOJob)
}

void HPOJob::SharedCtor() {
  ::google::protobuf::internal::InitSCC(
      &scc_info_HPOJob_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto.base);
  ::memset(&training_job_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&max_parallel_training_jobs_) -
      reinterpret_cast<char*>(&training_job_)) + sizeof(max_parallel_training_jobs_));
}

HPOJob::~HPOJob() {
  // @@protoc_insertion_point(destructor:flyteidl.plugins.sagemaker.HPOJob)
  SharedDtor();
}

void HPOJob::SharedDtor() {
  if (this != internal_default_instance()) delete training_job_;
}

void HPOJob::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const HPOJob& HPOJob::default_instance() {
  ::google::protobuf::internal::InitSCC(&::scc_info_HPOJob_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto.base);
  return *internal_default_instance();
}


void HPOJob::Clear() {
// @@protoc_insertion_point(message_clear_start:flyteidl.plugins.sagemaker.HPOJob)
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  if (GetArenaNoVirtual() == nullptr && training_job_ != nullptr) {
    delete training_job_;
  }
  training_job_ = nullptr;
  ::memset(&max_number_of_training_jobs_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&max_parallel_training_jobs_) -
      reinterpret_cast<char*>(&max_number_of_training_jobs_)) + sizeof(max_parallel_training_jobs_));
  _internal_metadata_.Clear();
}

#if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
const char* HPOJob::_InternalParse(const char* begin, const char* end, void* object,
                  ::google::protobuf::internal::ParseContext* ctx) {
  auto msg = static_cast<HPOJob*>(object);
  ::google::protobuf::int32 size; (void)size;
  int depth; (void)depth;
  ::google::protobuf::uint32 tag;
  ::google::protobuf::internal::ParseFunc parser_till_end; (void)parser_till_end;
  auto ptr = begin;
  while (ptr < end) {
    ptr = ::google::protobuf::io::Parse32(ptr, &tag);
    GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
    switch (tag >> 3) {
      // int64 max_number_of_training_jobs = 1;
      case 1: {
        if (static_cast<::google::protobuf::uint8>(tag) != 8) goto handle_unusual;
        msg->set_max_number_of_training_jobs(::google::protobuf::internal::ReadVarint(&ptr));
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        break;
      }
      // int64 max_parallel_training_jobs = 2;
      case 2: {
        if (static_cast<::google::protobuf::uint8>(tag) != 16) goto handle_unusual;
        msg->set_max_parallel_training_jobs(::google::protobuf::internal::ReadVarint(&ptr));
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        break;
      }
      // .flyteidl.plugins.sagemaker.TrainingJob training_job = 3;
      case 3: {
        if (static_cast<::google::protobuf::uint8>(tag) != 26) goto handle_unusual;
        ptr = ::google::protobuf::io::ReadSize(ptr, &size);
        GOOGLE_PROTOBUF_PARSER_ASSERT(ptr);
        parser_till_end = ::flyteidl::plugins::sagemaker::TrainingJob::_InternalParse;
        object = msg->mutable_training_job();
        if (size > end - ptr) goto len_delim_till_end;
        ptr += size;
        GOOGLE_PROTOBUF_PARSER_ASSERT(ctx->ParseExactRange(
            {parser_till_end, object}, ptr - size, ptr));
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
len_delim_till_end:
  return ctx->StoreAndTailCall(ptr, end, {_InternalParse, msg},
                               {parser_till_end, object}, size);
}
#else  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
bool HPOJob::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!PROTOBUF_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:flyteidl.plugins.sagemaker.HPOJob)
  for (;;) {
    ::std::pair<::google::protobuf::uint32, bool> p = input->ReadTagWithCutoffNoLastTag(127u);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // int64 max_number_of_training_jobs = 1;
      case 1: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (8 & 0xFF)) {

          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int64, ::google::protobuf::internal::WireFormatLite::TYPE_INT64>(
                 input, &max_number_of_training_jobs_)));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // int64 max_parallel_training_jobs = 2;
      case 2: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (16 & 0xFF)) {

          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   ::google::protobuf::int64, ::google::protobuf::internal::WireFormatLite::TYPE_INT64>(
                 input, &max_parallel_training_jobs_)));
        } else {
          goto handle_unusual;
        }
        break;
      }

      // .flyteidl.plugins.sagemaker.TrainingJob training_job = 3;
      case 3: {
        if (static_cast< ::google::protobuf::uint8>(tag) == (26 & 0xFF)) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessage(
               input, mutable_training_job()));
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
  // @@protoc_insertion_point(parse_success:flyteidl.plugins.sagemaker.HPOJob)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:flyteidl.plugins.sagemaker.HPOJob)
  return false;
#undef DO_
}
#endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER

void HPOJob::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:flyteidl.plugins.sagemaker.HPOJob)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // int64 max_number_of_training_jobs = 1;
  if (this->max_number_of_training_jobs() != 0) {
    ::google::protobuf::internal::WireFormatLite::WriteInt64(1, this->max_number_of_training_jobs(), output);
  }

  // int64 max_parallel_training_jobs = 2;
  if (this->max_parallel_training_jobs() != 0) {
    ::google::protobuf::internal::WireFormatLite::WriteInt64(2, this->max_parallel_training_jobs(), output);
  }

  // .flyteidl.plugins.sagemaker.TrainingJob training_job = 3;
  if (this->has_training_job()) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      3, HasBitSetters::training_job(this), output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        _internal_metadata_.unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:flyteidl.plugins.sagemaker.HPOJob)
}

::google::protobuf::uint8* HPOJob::InternalSerializeWithCachedSizesToArray(
    ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:flyteidl.plugins.sagemaker.HPOJob)
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // int64 max_number_of_training_jobs = 1;
  if (this->max_number_of_training_jobs() != 0) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt64ToArray(1, this->max_number_of_training_jobs(), target);
  }

  // int64 max_parallel_training_jobs = 2;
  if (this->max_parallel_training_jobs() != 0) {
    target = ::google::protobuf::internal::WireFormatLite::WriteInt64ToArray(2, this->max_parallel_training_jobs(), target);
  }

  // .flyteidl.plugins.sagemaker.TrainingJob training_job = 3;
  if (this->has_training_job()) {
    target = ::google::protobuf::internal::WireFormatLite::
      InternalWriteMessageToArray(
        3, HasBitSetters::training_job(this), target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:flyteidl.plugins.sagemaker.HPOJob)
  return target;
}

size_t HPOJob::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:flyteidl.plugins.sagemaker.HPOJob)
  size_t total_size = 0;

  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        _internal_metadata_.unknown_fields());
  }
  ::google::protobuf::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // .flyteidl.plugins.sagemaker.TrainingJob training_job = 3;
  if (this->has_training_job()) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::MessageSize(
        *training_job_);
  }

  // int64 max_number_of_training_jobs = 1;
  if (this->max_number_of_training_jobs() != 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::Int64Size(
        this->max_number_of_training_jobs());
  }

  // int64 max_parallel_training_jobs = 2;
  if (this->max_parallel_training_jobs() != 0) {
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::Int64Size(
        this->max_parallel_training_jobs());
  }

  int cached_size = ::google::protobuf::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void HPOJob::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:flyteidl.plugins.sagemaker.HPOJob)
  GOOGLE_DCHECK_NE(&from, this);
  const HPOJob* source =
      ::google::protobuf::DynamicCastToGenerated<HPOJob>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:flyteidl.plugins.sagemaker.HPOJob)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:flyteidl.plugins.sagemaker.HPOJob)
    MergeFrom(*source);
  }
}

void HPOJob::MergeFrom(const HPOJob& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:flyteidl.plugins.sagemaker.HPOJob)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::google::protobuf::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.has_training_job()) {
    mutable_training_job()->::flyteidl::plugins::sagemaker::TrainingJob::MergeFrom(from.training_job());
  }
  if (from.max_number_of_training_jobs() != 0) {
    set_max_number_of_training_jobs(from.max_number_of_training_jobs());
  }
  if (from.max_parallel_training_jobs() != 0) {
    set_max_parallel_training_jobs(from.max_parallel_training_jobs());
  }
}

void HPOJob::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:flyteidl.plugins.sagemaker.HPOJob)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void HPOJob::CopyFrom(const HPOJob& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:flyteidl.plugins.sagemaker.HPOJob)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool HPOJob::IsInitialized() const {
  return true;
}

void HPOJob::Swap(HPOJob* other) {
  if (other == this) return;
  InternalSwap(other);
}
void HPOJob::InternalSwap(HPOJob* other) {
  using std::swap;
  _internal_metadata_.Swap(&other->_internal_metadata_);
  swap(training_job_, other->training_job_);
  swap(max_number_of_training_jobs_, other->max_number_of_training_jobs_);
  swap(max_parallel_training_jobs_, other->max_parallel_training_jobs_);
}

::google::protobuf::Metadata HPOJob::GetMetadata() const {
  ::google::protobuf::internal::AssignDescriptors(&::assign_descriptors_table_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto);
  return ::file_level_metadata_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto[kIndexInFileMessages];
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace sagemaker
}  // namespace plugins
}  // namespace flyteidl
namespace google {
namespace protobuf {
template<> PROTOBUF_NOINLINE ::flyteidl::plugins::sagemaker::HPOJobObjective* Arena::CreateMaybeMessage< ::flyteidl::plugins::sagemaker::HPOJobObjective >(Arena* arena) {
  return Arena::CreateInternal< ::flyteidl::plugins::sagemaker::HPOJobObjective >(arena);
}
template<> PROTOBUF_NOINLINE ::flyteidl::plugins::sagemaker::HPOJob* Arena::CreateMaybeMessage< ::flyteidl::plugins::sagemaker::HPOJob >(Arena* arena) {
  return Arena::CreateInternal< ::flyteidl::plugins::sagemaker::HPOJob >(arena);
}
}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>

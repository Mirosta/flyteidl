// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: flyteidl/plugins/sagemaker/hpojob.proto

#ifndef PROTOBUF_INCLUDED_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto
#define PROTOBUF_INCLUDED_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3007000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3007000 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/generated_enum_reflection.h>
#include <google/protobuf/unknown_field_set.h>
#include "flyteidl/plugins/sagemaker/parameterranges.pb.h"
#include "flyteidl/plugins/sagemaker/trainingjob.pb.h"
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto

// Internal implementation detail -- do not use these members.
struct TableStruct_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto {
  static const ::google::protobuf::internal::ParseTableField entries[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::google::protobuf::internal::AuxillaryParseTableField aux[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::google::protobuf::internal::ParseTable schema[2]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::google::protobuf::internal::FieldMetadata field_metadata[];
  static const ::google::protobuf::internal::SerializationTable serialization_table[];
  static const ::google::protobuf::uint32 offsets[];
};
void AddDescriptors_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto();
namespace flyteidl {
namespace plugins {
namespace sagemaker {
class HPOJob;
class HPOJobDefaultTypeInternal;
extern HPOJobDefaultTypeInternal _HPOJob_default_instance_;
class HPOJobObjective;
class HPOJobObjectiveDefaultTypeInternal;
extern HPOJobObjectiveDefaultTypeInternal _HPOJobObjective_default_instance_;
}  // namespace sagemaker
}  // namespace plugins
}  // namespace flyteidl
namespace google {
namespace protobuf {
template<> ::flyteidl::plugins::sagemaker::HPOJob* Arena::CreateMaybeMessage<::flyteidl::plugins::sagemaker::HPOJob>(Arena*);
template<> ::flyteidl::plugins::sagemaker::HPOJobObjective* Arena::CreateMaybeMessage<::flyteidl::plugins::sagemaker::HPOJobObjective>(Arena*);
}  // namespace protobuf
}  // namespace google
namespace flyteidl {
namespace plugins {
namespace sagemaker {

enum HPOJobObjective_HPOJobObjectiveType {
  HPOJobObjective_HPOJobObjectiveType_MINIMIZE = 0,
  HPOJobObjective_HPOJobObjectiveType_MAXIMIZE = 1,
  HPOJobObjective_HPOJobObjectiveType_HPOJobObjective_HPOJobObjectiveType_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<::google::protobuf::int32>::min(),
  HPOJobObjective_HPOJobObjectiveType_HPOJobObjective_HPOJobObjectiveType_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<::google::protobuf::int32>::max()
};
bool HPOJobObjective_HPOJobObjectiveType_IsValid(int value);
const HPOJobObjective_HPOJobObjectiveType HPOJobObjective_HPOJobObjectiveType_HPOJobObjectiveType_MIN = HPOJobObjective_HPOJobObjectiveType_MINIMIZE;
const HPOJobObjective_HPOJobObjectiveType HPOJobObjective_HPOJobObjectiveType_HPOJobObjectiveType_MAX = HPOJobObjective_HPOJobObjectiveType_MAXIMIZE;
const int HPOJobObjective_HPOJobObjectiveType_HPOJobObjectiveType_ARRAYSIZE = HPOJobObjective_HPOJobObjectiveType_HPOJobObjectiveType_MAX + 1;

const ::google::protobuf::EnumDescriptor* HPOJobObjective_HPOJobObjectiveType_descriptor();
inline const ::std::string& HPOJobObjective_HPOJobObjectiveType_Name(HPOJobObjective_HPOJobObjectiveType value) {
  return ::google::protobuf::internal::NameOfEnum(
    HPOJobObjective_HPOJobObjectiveType_descriptor(), value);
}
inline bool HPOJobObjective_HPOJobObjectiveType_Parse(
    const ::std::string& name, HPOJobObjective_HPOJobObjectiveType* value) {
  return ::google::protobuf::internal::ParseNamedEnum<HPOJobObjective_HPOJobObjectiveType>(
    HPOJobObjective_HPOJobObjectiveType_descriptor(), name, value);
}
// ===================================================================

class HPOJobObjective final :
    public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:flyteidl.plugins.sagemaker.HPOJobObjective) */ {
 public:
  HPOJobObjective();
  virtual ~HPOJobObjective();

  HPOJobObjective(const HPOJobObjective& from);

  inline HPOJobObjective& operator=(const HPOJobObjective& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  HPOJobObjective(HPOJobObjective&& from) noexcept
    : HPOJobObjective() {
    *this = ::std::move(from);
  }

  inline HPOJobObjective& operator=(HPOJobObjective&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor() {
    return default_instance().GetDescriptor();
  }
  static const HPOJobObjective& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const HPOJobObjective* internal_default_instance() {
    return reinterpret_cast<const HPOJobObjective*>(
               &_HPOJobObjective_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  void Swap(HPOJobObjective* other);
  friend void swap(HPOJobObjective& a, HPOJobObjective& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline HPOJobObjective* New() const final {
    return CreateMaybeMessage<HPOJobObjective>(nullptr);
  }

  HPOJobObjective* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<HPOJobObjective>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const HPOJobObjective& from);
  void MergeFrom(const HPOJobObjective& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  static const char* _InternalParse(const char* begin, const char* end, void* object, ::google::protobuf::internal::ParseContext* ctx);
  ::google::protobuf::internal::ParseFunc _ParseFunc() const final { return _InternalParse; }
  #else
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(HPOJobObjective* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  typedef HPOJobObjective_HPOJobObjectiveType HPOJobObjectiveType;
  static const HPOJobObjectiveType MINIMIZE =
    HPOJobObjective_HPOJobObjectiveType_MINIMIZE;
  static const HPOJobObjectiveType MAXIMIZE =
    HPOJobObjective_HPOJobObjectiveType_MAXIMIZE;
  static inline bool HPOJobObjectiveType_IsValid(int value) {
    return HPOJobObjective_HPOJobObjectiveType_IsValid(value);
  }
  static const HPOJobObjectiveType HPOJobObjectiveType_MIN =
    HPOJobObjective_HPOJobObjectiveType_HPOJobObjectiveType_MIN;
  static const HPOJobObjectiveType HPOJobObjectiveType_MAX =
    HPOJobObjective_HPOJobObjectiveType_HPOJobObjectiveType_MAX;
  static const int HPOJobObjectiveType_ARRAYSIZE =
    HPOJobObjective_HPOJobObjectiveType_HPOJobObjectiveType_ARRAYSIZE;
  static inline const ::google::protobuf::EnumDescriptor*
  HPOJobObjectiveType_descriptor() {
    return HPOJobObjective_HPOJobObjectiveType_descriptor();
  }
  static inline const ::std::string& HPOJobObjectiveType_Name(HPOJobObjectiveType value) {
    return HPOJobObjective_HPOJobObjectiveType_Name(value);
  }
  static inline bool HPOJobObjectiveType_Parse(const ::std::string& name,
      HPOJobObjectiveType* value) {
    return HPOJobObjective_HPOJobObjectiveType_Parse(name, value);
  }

  // accessors -------------------------------------------------------

  // string metric_name = 2;
  void clear_metric_name();
  static const int kMetricNameFieldNumber = 2;
  const ::std::string& metric_name() const;
  void set_metric_name(const ::std::string& value);
  #if LANG_CXX11
  void set_metric_name(::std::string&& value);
  #endif
  void set_metric_name(const char* value);
  void set_metric_name(const char* value, size_t size);
  ::std::string* mutable_metric_name();
  ::std::string* release_metric_name();
  void set_allocated_metric_name(::std::string* metric_name);

  // .flyteidl.plugins.sagemaker.HPOJobObjective.HPOJobObjectiveType type = 1;
  void clear_type();
  static const int kTypeFieldNumber = 1;
  ::flyteidl::plugins::sagemaker::HPOJobObjective_HPOJobObjectiveType type() const;
  void set_type(::flyteidl::plugins::sagemaker::HPOJobObjective_HPOJobObjectiveType value);

  // @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.HPOJobObjective)
 private:
  class HasBitSetters;

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::google::protobuf::internal::ArenaStringPtr metric_name_;
  int type_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto;
};
// -------------------------------------------------------------------

class HPOJob final :
    public ::google::protobuf::Message /* @@protoc_insertion_point(class_definition:flyteidl.plugins.sagemaker.HPOJob) */ {
 public:
  HPOJob();
  virtual ~HPOJob();

  HPOJob(const HPOJob& from);

  inline HPOJob& operator=(const HPOJob& from) {
    CopyFrom(from);
    return *this;
  }
  #if LANG_CXX11
  HPOJob(HPOJob&& from) noexcept
    : HPOJob() {
    *this = ::std::move(from);
  }

  inline HPOJob& operator=(HPOJob&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }
  #endif
  static const ::google::protobuf::Descriptor* descriptor() {
    return default_instance().GetDescriptor();
  }
  static const HPOJob& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const HPOJob* internal_default_instance() {
    return reinterpret_cast<const HPOJob*>(
               &_HPOJob_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  void Swap(HPOJob* other);
  friend void swap(HPOJob& a, HPOJob& b) {
    a.Swap(&b);
  }

  // implements Message ----------------------------------------------

  inline HPOJob* New() const final {
    return CreateMaybeMessage<HPOJob>(nullptr);
  }

  HPOJob* New(::google::protobuf::Arena* arena) const final {
    return CreateMaybeMessage<HPOJob>(arena);
  }
  void CopyFrom(const ::google::protobuf::Message& from) final;
  void MergeFrom(const ::google::protobuf::Message& from) final;
  void CopyFrom(const HPOJob& from);
  void MergeFrom(const HPOJob& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  static const char* _InternalParse(const char* begin, const char* end, void* object, ::google::protobuf::internal::ParseContext* ctx);
  ::google::protobuf::internal::ParseFunc _ParseFunc() const final { return _InternalParse; }
  #else
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const final;
  ::google::protobuf::uint8* InternalSerializeWithCachedSizesToArray(
      ::google::protobuf::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(HPOJob* other);
  private:
  inline ::google::protobuf::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::google::protobuf::Metadata GetMetadata() const final;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // .flyteidl.plugins.sagemaker.TrainingJob training_job = 3;
  bool has_training_job() const;
  void clear_training_job();
  static const int kTrainingJobFieldNumber = 3;
  const ::flyteidl::plugins::sagemaker::TrainingJob& training_job() const;
  ::flyteidl::plugins::sagemaker::TrainingJob* release_training_job();
  ::flyteidl::plugins::sagemaker::TrainingJob* mutable_training_job();
  void set_allocated_training_job(::flyteidl::plugins::sagemaker::TrainingJob* training_job);

  // int64 max_number_of_training_jobs = 1;
  void clear_max_number_of_training_jobs();
  static const int kMaxNumberOfTrainingJobsFieldNumber = 1;
  ::google::protobuf::int64 max_number_of_training_jobs() const;
  void set_max_number_of_training_jobs(::google::protobuf::int64 value);

  // int64 max_parallel_training_jobs = 2;
  void clear_max_parallel_training_jobs();
  static const int kMaxParallelTrainingJobsFieldNumber = 2;
  ::google::protobuf::int64 max_parallel_training_jobs() const;
  void set_max_parallel_training_jobs(::google::protobuf::int64 value);

  // @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.HPOJob)
 private:
  class HasBitSetters;

  ::google::protobuf::internal::InternalMetadataWithArena _internal_metadata_;
  ::flyteidl::plugins::sagemaker::TrainingJob* training_job_;
  ::google::protobuf::int64 max_number_of_training_jobs_;
  ::google::protobuf::int64 max_parallel_training_jobs_;
  mutable ::google::protobuf::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// HPOJobObjective

// .flyteidl.plugins.sagemaker.HPOJobObjective.HPOJobObjectiveType type = 1;
inline void HPOJobObjective::clear_type() {
  type_ = 0;
}
inline ::flyteidl::plugins::sagemaker::HPOJobObjective_HPOJobObjectiveType HPOJobObjective::type() const {
  // @@protoc_insertion_point(field_get:flyteidl.plugins.sagemaker.HPOJobObjective.type)
  return static_cast< ::flyteidl::plugins::sagemaker::HPOJobObjective_HPOJobObjectiveType >(type_);
}
inline void HPOJobObjective::set_type(::flyteidl::plugins::sagemaker::HPOJobObjective_HPOJobObjectiveType value) {
  
  type_ = value;
  // @@protoc_insertion_point(field_set:flyteidl.plugins.sagemaker.HPOJobObjective.type)
}

// string metric_name = 2;
inline void HPOJobObjective::clear_metric_name() {
  metric_name_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline const ::std::string& HPOJobObjective::metric_name() const {
  // @@protoc_insertion_point(field_get:flyteidl.plugins.sagemaker.HPOJobObjective.metric_name)
  return metric_name_.GetNoArena();
}
inline void HPOJobObjective::set_metric_name(const ::std::string& value) {
  
  metric_name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:flyteidl.plugins.sagemaker.HPOJobObjective.metric_name)
}
#if LANG_CXX11
inline void HPOJobObjective::set_metric_name(::std::string&& value) {
  
  metric_name_.SetNoArena(
    &::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::move(value));
  // @@protoc_insertion_point(field_set_rvalue:flyteidl.plugins.sagemaker.HPOJobObjective.metric_name)
}
#endif
inline void HPOJobObjective::set_metric_name(const char* value) {
  GOOGLE_DCHECK(value != nullptr);
  
  metric_name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:flyteidl.plugins.sagemaker.HPOJobObjective.metric_name)
}
inline void HPOJobObjective::set_metric_name(const char* value, size_t size) {
  
  metric_name_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:flyteidl.plugins.sagemaker.HPOJobObjective.metric_name)
}
inline ::std::string* HPOJobObjective::mutable_metric_name() {
  
  // @@protoc_insertion_point(field_mutable:flyteidl.plugins.sagemaker.HPOJobObjective.metric_name)
  return metric_name_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline ::std::string* HPOJobObjective::release_metric_name() {
  // @@protoc_insertion_point(field_release:flyteidl.plugins.sagemaker.HPOJobObjective.metric_name)
  
  return metric_name_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
inline void HPOJobObjective::set_allocated_metric_name(::std::string* metric_name) {
  if (metric_name != nullptr) {
    
  } else {
    
  }
  metric_name_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), metric_name);
  // @@protoc_insertion_point(field_set_allocated:flyteidl.plugins.sagemaker.HPOJobObjective.metric_name)
}

// -------------------------------------------------------------------

// HPOJob

// int64 max_number_of_training_jobs = 1;
inline void HPOJob::clear_max_number_of_training_jobs() {
  max_number_of_training_jobs_ = PROTOBUF_LONGLONG(0);
}
inline ::google::protobuf::int64 HPOJob::max_number_of_training_jobs() const {
  // @@protoc_insertion_point(field_get:flyteidl.plugins.sagemaker.HPOJob.max_number_of_training_jobs)
  return max_number_of_training_jobs_;
}
inline void HPOJob::set_max_number_of_training_jobs(::google::protobuf::int64 value) {
  
  max_number_of_training_jobs_ = value;
  // @@protoc_insertion_point(field_set:flyteidl.plugins.sagemaker.HPOJob.max_number_of_training_jobs)
}

// int64 max_parallel_training_jobs = 2;
inline void HPOJob::clear_max_parallel_training_jobs() {
  max_parallel_training_jobs_ = PROTOBUF_LONGLONG(0);
}
inline ::google::protobuf::int64 HPOJob::max_parallel_training_jobs() const {
  // @@protoc_insertion_point(field_get:flyteidl.plugins.sagemaker.HPOJob.max_parallel_training_jobs)
  return max_parallel_training_jobs_;
}
inline void HPOJob::set_max_parallel_training_jobs(::google::protobuf::int64 value) {
  
  max_parallel_training_jobs_ = value;
  // @@protoc_insertion_point(field_set:flyteidl.plugins.sagemaker.HPOJob.max_parallel_training_jobs)
}

// .flyteidl.plugins.sagemaker.TrainingJob training_job = 3;
inline bool HPOJob::has_training_job() const {
  return this != internal_default_instance() && training_job_ != nullptr;
}
inline const ::flyteidl::plugins::sagemaker::TrainingJob& HPOJob::training_job() const {
  const ::flyteidl::plugins::sagemaker::TrainingJob* p = training_job_;
  // @@protoc_insertion_point(field_get:flyteidl.plugins.sagemaker.HPOJob.training_job)
  return p != nullptr ? *p : *reinterpret_cast<const ::flyteidl::plugins::sagemaker::TrainingJob*>(
      &::flyteidl::plugins::sagemaker::_TrainingJob_default_instance_);
}
inline ::flyteidl::plugins::sagemaker::TrainingJob* HPOJob::release_training_job() {
  // @@protoc_insertion_point(field_release:flyteidl.plugins.sagemaker.HPOJob.training_job)
  
  ::flyteidl::plugins::sagemaker::TrainingJob* temp = training_job_;
  training_job_ = nullptr;
  return temp;
}
inline ::flyteidl::plugins::sagemaker::TrainingJob* HPOJob::mutable_training_job() {
  
  if (training_job_ == nullptr) {
    auto* p = CreateMaybeMessage<::flyteidl::plugins::sagemaker::TrainingJob>(GetArenaNoVirtual());
    training_job_ = p;
  }
  // @@protoc_insertion_point(field_mutable:flyteidl.plugins.sagemaker.HPOJob.training_job)
  return training_job_;
}
inline void HPOJob::set_allocated_training_job(::flyteidl::plugins::sagemaker::TrainingJob* training_job) {
  ::google::protobuf::Arena* message_arena = GetArenaNoVirtual();
  if (message_arena == nullptr) {
    delete reinterpret_cast< ::google::protobuf::MessageLite*>(training_job_);
  }
  if (training_job) {
    ::google::protobuf::Arena* submessage_arena = nullptr;
    if (message_arena != submessage_arena) {
      training_job = ::google::protobuf::internal::GetOwnedMessage(
          message_arena, training_job, submessage_arena);
    }
    
  } else {
    
  }
  training_job_ = training_job;
  // @@protoc_insertion_point(field_set_allocated:flyteidl.plugins.sagemaker.HPOJob.training_job)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace sagemaker
}  // namespace plugins
}  // namespace flyteidl

namespace google {
namespace protobuf {

template <> struct is_proto_enum< ::flyteidl::plugins::sagemaker::HPOJobObjective_HPOJobObjectiveType> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::flyteidl::plugins::sagemaker::HPOJobObjective_HPOJobObjectiveType>() {
  return ::flyteidl::plugins::sagemaker::HPOJobObjective_HPOJobObjectiveType_descriptor();
}

}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // PROTOBUF_INCLUDED_flyteidl_2fplugins_2fsagemaker_2fhpojob_2eproto

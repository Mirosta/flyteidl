/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

// A Task structure that uniquely identifies a task in the system Tasks are registered as a first step in the system.
type CoreTaskTemplate struct {
	// Auto generated taskId by the system. Task Id uniquely identifies this task globally.
	Id *CoreIdentifier `json:"id,omitempty"`
	// A predefined yet extensible Task type identifier. This can be used to customize any of the components. If no extensions are provided in the system, Flyte will resolve the this task to its TaskCategory and default the implementation registered for the TaskCategory.
	Type_ string `json:"type,omitempty"`
	// Extra metadata about the task.
	Metadata *CoreTaskMetadata `json:"metadata,omitempty"`
	// A strongly typed interface for the task. This enables others to use this task within a workflow and gauarantees compile-time validation of the workflow to avoid costly runtime failures.
	Interface_ *CoreTypedInterface `json:"interface,omitempty"`
	// Custom data about the task. This is extensible to allow various plugins in the system.
	Custom *ProtobufStruct `json:"custom,omitempty"`
	Container *CoreContainer `json:"container,omitempty"`
	// This can be used to customize task handling at execution time for the same task type.
	Version int32 `json:"version,omitempty"`
}

/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

import (
	"time"
)

// Represents attributes about an execution which are not required to launch the execution but are useful to record. These attributes are assigned at launch time and do not change.
type AdminExecutionMetadata struct {
	Mode *ExecutionMetadataExecutionMode `json:"mode,omitempty"`
	// Identifier of the entity that triggered this execution. For systems using back-end authentication any value set here will be discarded in favor of the authenticated user context.
	Principal string `json:"principal,omitempty"`
	// Indicates the nestedness of this execution. If a user launches a workflow execution, the default nesting is 0. If this execution further launches a workflow (child workflow), the nesting level is incremented by 0 => 1 Generally, if workflow at nesting level k launches a workflow then the child workflow will have nesting = k + 1.
	Nesting int64 `json:"nesting,omitempty"`
	// For scheduled executions, the requested time for execution for this specific schedule invocation.
	ScheduledAt time.Time `json:"scheduled_at,omitempty"`
	ParentNodeExecution *CoreNodeExecutionIdentifier `json:"parent_node_execution,omitempty"`
	// Optional, a reference workflow execution related to this execution. In the case of a relaunch, this references the original workflow execution.
	ReferenceExecution *CoreWorkflowExecutionIdentifier `json:"reference_execution,omitempty"`
	// Optional, platform-specific metadata about the execution. In this the future this may be gated behind an ACL or some sort of authorization.
	SystemMetadata *AdminSystemMetadata `json:"system_metadata,omitempty"`
	ArtifactIds map[string]CoreArtifactId `json:"artifact_ids,omitempty"`
}

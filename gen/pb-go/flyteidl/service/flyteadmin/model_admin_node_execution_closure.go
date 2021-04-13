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

// Container for node execution details and results.
type AdminNodeExecutionClosure struct {
	OutputUri string `json:"output_uri,omitempty"`
	Error_ *CoreExecutionError `json:"error,omitempty"`
	// The last recorded phase for this node execution.
	Phase *CoreNodeExecutionPhase `json:"phase,omitempty"`
	// Time at which the node execution began running.
	StartedAt time.Time `json:"started_at,omitempty"`
	// The amount of time the node execution spent running.
	Duration string `json:"duration,omitempty"`
	// Time at which the node execution was created.
	CreatedAt time.Time `json:"created_at,omitempty"`
	// Time at which the node execution was last updated.
	UpdatedAt time.Time `json:"updated_at,omitempty"`
	WorkflowNodeMetadata *FlyteidladminWorkflowNodeMetadata `json:"workflow_node_metadata,omitempty"`
	TaskNodeMetadata *FlyteidladminTaskNodeMetadata `json:"task_node_metadata,omitempty"`
	DynamicWorkflowNodeMetadata *FlyteidladminDynamicWorkflowNodeMetadata `json:"dynamic_workflow_node_metadata,omitempty"`
}

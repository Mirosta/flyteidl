/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

// This message contains various identifiers for resources used for a specific task execution.
type EventResourceIdentifiers struct {
	// Unique, generated name for this task execution used by the backend.
	GeneratedName string `json:"generated_name,omitempty"`
	// Identifiers for external resources created by this task execution, for exaple Qubole query ID or presto query ids.
	ExternalIds []string `json:"external_ids,omitempty"`
}

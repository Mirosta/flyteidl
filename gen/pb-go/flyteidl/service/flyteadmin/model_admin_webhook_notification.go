/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

// Defines a webhook notification specification.
type AdminWebhookNotification struct {
	Url string `json:"url,omitempty"`
	// The secret name to use to trigger the webhook.
	SecretName string `json:"secret_name,omitempty"`
	Payload string `json:"payload,omitempty"`
}

/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin
// PluginOverrideMissingPluginBehavior :  - OVERRIDE_FALLBACK: Use the in-order list of fallback_plugin_ids as supported fallbacks for this task type.  - USE_DEFAULT: Uses the system-configured default implementation.
type PluginOverrideMissingPluginBehavior string

// List of PluginOverrideMissingPluginBehavior
const (
	PluginOverrideMissingPluginBehaviorFAIL PluginOverrideMissingPluginBehavior = "FAIL"
	PluginOverrideMissingPluginBehaviorOVERRIDE_FALLBACK PluginOverrideMissingPluginBehavior = "OVERRIDE_FALLBACK"
	PluginOverrideMissingPluginBehaviorUSE_DEFAULT PluginOverrideMissingPluginBehavior = "USE_DEFAULT"
)
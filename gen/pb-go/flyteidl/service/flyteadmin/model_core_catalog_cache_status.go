/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin
// CoreCatalogCacheStatus : - CACHE_DISABLED: Used to indicate that caching was disabled  - CACHE_MISS: Used to indicate that the cache lookup resulted in no matches  - CACHE_HIT: used to indicate that the associated artifact was a result of a previous execution  - CACHE_POPULATED: used to indicate that the resultant artifact was added to the cache  - CACHE_LOOKUP_FAILURE: Used to indicate that cache lookup failed because of an error  - CACHE_PUT_FAILURE: Used to indicate that cache lookup failed because of an error  - CACHE_SKIPPED: Used to indicate the cache lookup was skipped
type CoreCatalogCacheStatus string

// List of coreCatalogCacheStatus
const (
	CoreCatalogCacheStatusDISABLED CoreCatalogCacheStatus = "CACHE_DISABLED"
	CoreCatalogCacheStatusMISS CoreCatalogCacheStatus = "CACHE_MISS"
	CoreCatalogCacheStatusHIT CoreCatalogCacheStatus = "CACHE_HIT"
	CoreCatalogCacheStatusPOPULATED CoreCatalogCacheStatus = "CACHE_POPULATED"
	CoreCatalogCacheStatusLOOKUP_FAILURE CoreCatalogCacheStatus = "CACHE_LOOKUP_FAILURE"
	CoreCatalogCacheStatusPUT_FAILURE CoreCatalogCacheStatus = "CACHE_PUT_FAILURE"
	CoreCatalogCacheStatusSKIPPED CoreCatalogCacheStatus = "CACHE_SKIPPED"
)

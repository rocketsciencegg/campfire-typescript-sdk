# CompanyObjectsApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**caApiV1CustomFieldsCreate**](#caapiv1customfieldscreate) | **POST** /ca/api/v1/custom-fields | Create Custom Field|
|[**caApiV1CustomFieldsDestroy**](#caapiv1customfieldsdestroy) | **DELETE** /ca/api/v1/custom-fields/{id} | Delete Custom Field|
|[**caApiV1CustomFieldsList**](#caapiv1customfieldslist) | **GET** /ca/api/v1/custom-fields | List Custom Fields|
|[**caApiV1CustomFieldsPartialUpdate**](#caapiv1customfieldspartialupdate) | **PATCH** /ca/api/v1/custom-fields/{id} | Partial Update Custom Field|
|[**caApiV1CustomFieldsRetrieve**](#caapiv1customfieldsretrieve) | **GET** /ca/api/v1/custom-fields/{id} | Retrieve Custom Field|
|[**caApiV1CustomFieldsUpdate**](#caapiv1customfieldsupdate) | **PUT** /ca/api/v1/custom-fields/{id} | Update Custom Field|
|[**coaApiAccountBalanceSheetCreate**](#coaapiaccountbalancesheetcreate) | **POST** /coa/api/account/balance-sheet | Create Chart Account|
|[**coaApiAccountBalanceSheetList**](#coaapiaccountbalancesheetlist) | **GET** /coa/api/account/balance-sheet | List Chart Accounts|
|[**coaApiAccountCreate**](#coaapiaccountcreate) | **POST** /coa/api/account | Create Chart Account|
|[**coaApiAccountDestroy**](#coaapiaccountdestroy) | **DELETE** /coa/api/account/{id} | Delete Chart Account|
|[**coaApiAccountIncomeStatementCreate**](#coaapiaccountincomestatementcreate) | **POST** /coa/api/account/income-statement | Create Chart Account|
|[**coaApiAccountIncomeStatementList**](#coaapiaccountincomestatementlist) | **GET** /coa/api/account/income-statement | List Chart of Accounts|
|[**coaApiAccountList**](#coaapiaccountlist) | **GET** /coa/api/account | List Chart of Accounts|
|[**coaApiAccountPartialUpdate**](#coaapiaccountpartialupdate) | **PATCH** /coa/api/account/{id} | Partial Update Chart Account|
|[**coaApiAccountRetrieve**](#coaapiaccountretrieve) | **GET** /coa/api/account/{id} | Retrieve Chart Account|
|[**coaApiAccountUpdate**](#coaapiaccountupdate) | **PUT** /coa/api/account/{id} | Update Chart Account|
|[**coaApiCostAllocationsCatchUpCreate**](#coaapicostallocationscatchupcreate) | **POST** /coa/api/cost-allocations/{id}/catch-up | Catch Up Closed Period Allocation|
|[**coaApiCostAllocationsCreate**](#coaapicostallocationscreate) | **POST** /coa/api/cost-allocations | Create Cost Allocation|
|[**coaApiCostAllocationsDestroy**](#coaapicostallocationsdestroy) | **DELETE** /coa/api/cost-allocations/{id} | Delete Cost Allocation|
|[**coaApiCostAllocationsList**](#coaapicostallocationslist) | **GET** /coa/api/cost-allocations | List Cost Allocation|
|[**coaApiCostAllocationsPartialUpdate**](#coaapicostallocationspartialupdate) | **PATCH** /coa/api/cost-allocations/{id} | Partial Update Cost Allocation|
|[**coaApiCostAllocationsPreviewRetrieve**](#coaapicostallocationspreviewretrieve) | **GET** /coa/api/cost-allocations/{id}/preview | Preview Cost Allocation Split|
|[**coaApiCostAllocationsRetrieve**](#coaapicostallocationsretrieve) | **GET** /coa/api/cost-allocations/{id} | Get Cost Allocation|
|[**coaApiCostAllocationsSyncCreate**](#coaapicostallocationssynccreate) | **POST** /coa/api/cost-allocations/{id}/sync | Recalculate Cost Allocation|
|[**coaApiCostAllocationsSyncRunsList**](#coaapicostallocationssyncrunslist) | **GET** /coa/api/cost-allocations/{id}/sync-runs | List Allocation Sync Runs|
|[**coaApiCostAllocationsSyncRunsRetrieve**](#coaapicostallocationssyncrunsretrieve) | **GET** /coa/api/cost-allocations/{id}/sync-runs/{run_pk} | Retrieve Allocation Sync Run|
|[**coaApiCostAllocationsUpdate**](#coaapicostallocationsupdate) | **PUT** /coa/api/cost-allocations/{id} | Update Cost Allocation|
|[**coaApiDepartmentCreate**](#coaapidepartmentcreate) | **POST** /coa/api/department | Create Department|
|[**coaApiDepartmentDeleteCreate**](#coaapidepartmentdeletecreate) | **POST** /coa/api/department/{id}/delete | Delete Department|
|[**coaApiDepartmentDestroy**](#coaapidepartmentdestroy) | **DELETE** /coa/api/department/{id} | Delete Department (deprecated)|
|[**coaApiDepartmentList**](#coaapidepartmentlist) | **GET** /coa/api/department | List Departments|
|[**coaApiDepartmentPartialUpdate**](#coaapidepartmentpartialupdate) | **PATCH** /coa/api/department/{id} | Partial Update Department|
|[**coaApiDepartmentRetrieve**](#coaapidepartmentretrieve) | **GET** /coa/api/department/{id} | Retrieve Department|
|[**coaApiDepartmentUpdate**](#coaapidepartmentupdate) | **PUT** /coa/api/department/{id} | Update Department|
|[**coaApiFixedAssetClassCreate**](#coaapifixedassetclasscreate) | **POST** /coa/api/fixed-asset-class | Create Fixed Asset Class|
|[**coaApiFixedAssetClassDestroy**](#coaapifixedassetclassdestroy) | **DELETE** /coa/api/fixed-asset-class/{id} | Delete Fixed Asset Class|
|[**coaApiFixedAssetClassList**](#coaapifixedassetclasslist) | **GET** /coa/api/fixed-asset-class | List Fixed Asset Classes|
|[**coaApiFixedAssetClassPartialUpdate**](#coaapifixedassetclasspartialupdate) | **PATCH** /coa/api/fixed-asset-class/{id} | Partial Fixed Asset Class|
|[**coaApiFixedAssetClassRetrieve**](#coaapifixedassetclassretrieve) | **GET** /coa/api/fixed-asset-class/{id} | Retrieve Fixed Asset Class|
|[**coaApiFixedAssetClassUpdate**](#coaapifixedassetclassupdate) | **PUT** /coa/api/fixed-asset-class/{id} | Update Fixed Asset Class|
|[**coaApiTagCreate**](#coaapitagcreate) | **POST** /coa/api/tag | Create Custom Dimension|
|[**coaApiTagDeleteCreate**](#coaapitagdeletecreate) | **POST** /coa/api/tag/{id}/delete | Delete Custom Dimension|
|[**coaApiTagDestroy**](#coaapitagdestroy) | **DELETE** /coa/api/tag/{id} | Delete Custom Dimension (deprecated)|
|[**coaApiTagGroupCreate**](#coaapitaggroupcreate) | **POST** /coa/api/tag-group | Create Custom Dimension Group|
|[**coaApiTagGroupDestroy**](#coaapitaggroupdestroy) | **DELETE** /coa/api/tag-group/{id} | Delete Custom Dimension Group|
|[**coaApiTagGroupList**](#coaapitaggrouplist) | **GET** /coa/api/tag-group | List Custom Dimension Groups|
|[**coaApiTagGroupPartialUpdate**](#coaapitaggrouppartialupdate) | **PATCH** /coa/api/tag-group/{id} | Partial Update Custom Dimension Group|
|[**coaApiTagGroupRetrieve**](#coaapitaggroupretrieve) | **GET** /coa/api/tag-group/{id} | Retrieve Custom Dimension Group|
|[**coaApiTagGroupUpdate**](#coaapitaggroupupdate) | **PUT** /coa/api/tag-group/{id} | Update Custom Dimension Group|
|[**coaApiTagList**](#coaapitaglist) | **GET** /coa/api/tag | List Custom Dimensions|
|[**coaApiTagPartialUpdate**](#coaapitagpartialupdate) | **PATCH** /coa/api/tag/{id} | Partial Update Custom Dimension|
|[**coaApiTagRetrieve**](#coaapitagretrieve) | **GET** /coa/api/tag/{id} | Retrieve Custom Dimension|
|[**coaApiTagUpdate**](#coaapitagupdate) | **PUT** /coa/api/tag/{id} | Update Custom Dimension|
|[**coaApiVendorContactTitleCreate**](#coaapivendorcontacttitlecreate) | **POST** /coa/api/vendor-contact-title | Create Vendor Contact Title|
|[**coaApiVendorContactTitleDestroy**](#coaapivendorcontacttitledestroy) | **DELETE** /coa/api/vendor-contact-title/{id} | Delete Vendor Contact Title|
|[**coaApiVendorContactTitleList**](#coaapivendorcontacttitlelist) | **GET** /coa/api/vendor-contact-title | List Vendor Contact Titles|
|[**coaApiVendorContactTitlePartialUpdate**](#coaapivendorcontacttitlepartialupdate) | **PATCH** /coa/api/vendor-contact-title/{id} | Partial Update Vendor Contact Title|
|[**coaApiVendorContactTitleRetrieve**](#coaapivendorcontacttitleretrieve) | **GET** /coa/api/vendor-contact-title/{id} | Retrieve Vendor Contact Title|
|[**coaApiVendorContactTitleUpdate**](#coaapivendorcontacttitleupdate) | **PUT** /coa/api/vendor-contact-title/{id} | Update Vendor Contact Title|
|[**coaApiVendorCreate**](#coaapivendorcreate) | **POST** /coa/api/vendor | Create Vendor|
|[**coaApiVendorDestroy**](#coaapivendordestroy) | **DELETE** /coa/api/vendor/{id} | Delete Vendor|
|[**coaApiVendorList**](#coaapivendorlist) | **GET** /coa/api/vendor | List Vendors|
|[**coaApiVendorPartialUpdate**](#coaapivendorpartialupdate) | **PATCH** /coa/api/vendor/{id} | Partial Update Vendor|
|[**coaApiVendorRetrieve**](#coaapivendorretrieve) | **GET** /coa/api/vendor/{id} | Retrieve Vendor|
|[**coaApiVendorUpdate**](#coaapivendorupdate) | **PUT** /coa/api/vendor/{id} | Update Vendor|
|[**createVendorCustomField**](#createvendorcustomfield) | **POST** /coa/api/vendor_custom_field_1 | Create Vendor Custom Field|
|[**deleteVendorCustomField**](#deletevendorcustomfield) | **DELETE** /coa/api/vendor_custom_field_1/{id} | Delete Vendor Custom Field|
|[**getVendorCustomField**](#getvendorcustomfield) | **GET** /coa/api/vendor_custom_field_1/{id} | Retrieve Vendor Custom Field|
|[**listVendorCustomFields**](#listvendorcustomfields) | **GET** /coa/api/vendor_custom_field_1 | List Vendor Custom Fields|
|[**listVendorSummaries**](#listvendorsummaries) | **GET** /coa/api/vendor/summary | List Vendor Summaries|
|[**partialUpdateVendorCustomField**](#partialupdatevendorcustomfield) | **PATCH** /coa/api/vendor_custom_field_1/{id} | Partial Update Vendor Custom Field|
|[**updateVendorCustomField**](#updatevendorcustomfield) | **PUT** /coa/api/vendor_custom_field_1/{id} | Update Vendor Custom Field|

# **caApiV1CustomFieldsCreate**
> CustomField caApiV1CustomFieldsCreate(customField)

Create a new custom field for a given app and model

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    CustomField
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let customField: CustomField; //

const { status, data } = await apiInstance.caApiV1CustomFieldsCreate(
    customField
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customField** | **CustomField**|  | |


### Return type

**CustomField**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiV1CustomFieldsDestroy**
> caApiV1CustomFieldsDestroy()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.caApiV1CustomFieldsDestroy(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiV1CustomFieldsList**
> PaginatedCustomFieldList caApiV1CustomFieldsList()

         List all custom fields for a given app and model.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let app: string; //App name (optional) (default to undefined)
let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let isActive: boolean; //Filter by active status (optional) (default to undefined)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let model: string; //Model name (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.caApiV1CustomFieldsList(
    app,
    includeDeleted,
    isActive,
    lastModifiedAtGte,
    lastModifiedAtLte,
    limit,
    model,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **app** | [**string**] | App name | (optional) defaults to undefined|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **isActive** | [**boolean**] | Filter by active status | (optional) defaults to undefined|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **model** | [**string**] | Model name | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedCustomFieldList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiV1CustomFieldsPartialUpdate**
> CustomField caApiV1CustomFieldsPartialUpdate()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    PatchedCustomField
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let patchedCustomField: PatchedCustomField; // (optional)

const { status, data } = await apiInstance.caApiV1CustomFieldsPartialUpdate(
    id,
    patchedCustomField
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedCustomField** | **PatchedCustomField**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**CustomField**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiV1CustomFieldsRetrieve**
> CustomField caApiV1CustomFieldsRetrieve()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.caApiV1CustomFieldsRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**CustomField**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiV1CustomFieldsUpdate**
> CustomField caApiV1CustomFieldsUpdate(customField)


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    CustomField
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let customField: CustomField; //

const { status, data } = await apiInstance.caApiV1CustomFieldsUpdate(
    id,
    customField
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customField** | **CustomField**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**CustomField**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiAccountBalanceSheetCreate**
> ChartAccount coaApiAccountBalanceSheetCreate(chartAccount)

Lists the chart of accounts (GL accounts). Each account includes metadata about its parent account and its full lineage (the ordered chain of ancestor accounts), so parent/child account relationships can be reconstructed from the response.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    ChartAccount
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let chartAccount: ChartAccount; //

const { status, data } = await apiInstance.coaApiAccountBalanceSheetCreate(
    chartAccount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **chartAccount** | **ChartAccount**|  | |


### Return type

**ChartAccount**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiAccountBalanceSheetList**
> PaginatedChartAccountList coaApiAccountBalanceSheetList()

Retrieve a list of chart accounts with optional filtering and sorting

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let account: number; //Filter by account ID. Can be specified multiple times for multiple accounts (optional) (default to undefined)
let accountSubtype: string; //Filter by account subtype. Can be specified multiple times for multiple subtypes (optional) (default to undefined)
let accountType: string; //Filter by account type. Can be specified multiple times for multiple types (optional) (default to undefined)
let includeCostAllocation: boolean; //Include accounts with cost allocation (optional) (default to false)
let includeInactive: boolean; //Include inactive accounts in results (optional) (default to true)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let q: string; //Search query - searches by account name or number (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiAccountBalanceSheetList(
    account,
    accountSubtype,
    accountType,
    includeCostAllocation,
    includeInactive,
    limit,
    offset,
    q
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **account** | [**number**] | Filter by account ID. Can be specified multiple times for multiple accounts | (optional) defaults to undefined|
| **accountSubtype** | [**string**] | Filter by account subtype. Can be specified multiple times for multiple subtypes | (optional) defaults to undefined|
| **accountType** | [**string**] | Filter by account type. Can be specified multiple times for multiple types | (optional) defaults to undefined|
| **includeCostAllocation** | [**boolean**] | Include accounts with cost allocation | (optional) defaults to false|
| **includeInactive** | [**boolean**] | Include inactive accounts in results | (optional) defaults to true|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **q** | [**string**] | Search query - searches by account name or number | (optional) defaults to undefined|


### Return type

**PaginatedChartAccountList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiAccountCreate**
> ChartAccount coaApiAccountCreate(chartAccount)

Lists the chart of accounts (GL accounts). Each account includes metadata about its parent account and its full lineage (the ordered chain of ancestor accounts), so parent/child account relationships can be reconstructed from the response.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    ChartAccount
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let chartAccount: ChartAccount; //

const { status, data } = await apiInstance.coaApiAccountCreate(
    chartAccount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **chartAccount** | **ChartAccount**|  | |


### Return type

**ChartAccount**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiAccountDestroy**
> coaApiAccountDestroy()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiAccountDestroy(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiAccountIncomeStatementCreate**
> ChartAccount coaApiAccountIncomeStatementCreate(chartAccount)

Lists the chart of accounts (GL accounts). Each account includes metadata about its parent account and its full lineage (the ordered chain of ancestor accounts), so parent/child account relationships can be reconstructed from the response.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    ChartAccount
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let chartAccount: ChartAccount; //

const { status, data } = await apiInstance.coaApiAccountIncomeStatementCreate(
    chartAccount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **chartAccount** | **ChartAccount**|  | |


### Return type

**ChartAccount**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiAccountIncomeStatementList**
> PaginatedChartAccountList coaApiAccountIncomeStatementList()

Lists the chart of accounts (GL accounts). Each account includes metadata about its parent account and its full lineage (the ordered chain of ancestor accounts), so parent/child account relationships can be reconstructed from the response.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiAccountIncomeStatementList(
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedChartAccountList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiAccountList**
> PaginatedChartAccountList coaApiAccountList()

Lists the chart of accounts (GL accounts). Each account includes metadata about its parent account and its full lineage (the ordered chain of ancestor accounts), so parent/child account relationships can be reconstructed from the response.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiAccountList(
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedChartAccountList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiAccountPartialUpdate**
> ChartAccount coaApiAccountPartialUpdate()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    PatchedChartAccount
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let patchedChartAccount: PatchedChartAccount; // (optional)

const { status, data } = await apiInstance.coaApiAccountPartialUpdate(
    id,
    patchedChartAccount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedChartAccount** | **PatchedChartAccount**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ChartAccount**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiAccountRetrieve**
> ChartAccount coaApiAccountRetrieve()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiAccountRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ChartAccount**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiAccountUpdate**
> ChartAccount coaApiAccountUpdate(chartAccount)


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    ChartAccount
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let chartAccount: ChartAccount; //

const { status, data } = await apiInstance.coaApiAccountUpdate(
    id,
    chartAccount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **chartAccount** | **ChartAccount**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ChartAccount**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiCostAllocationsCatchUpCreate**
> CostAllocationCatchUp coaApiCostAllocationsCatchUpCreate(costAllocationCatchUp)

Post a closed entity-period\'s remaining allocation delta into the next open period.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    CostAllocationCatchUp
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let costAllocationCatchUp: CostAllocationCatchUp; //

const { status, data } = await apiInstance.coaApiCostAllocationsCatchUpCreate(
    id,
    costAllocationCatchUp
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **costAllocationCatchUp** | **CostAllocationCatchUp**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**CostAllocationCatchUp**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiCostAllocationsCreate**
> CostAllocation coaApiCostAllocationsCreate(costAllocation)

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    CostAllocation
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let costAllocation: CostAllocation; //

const { status, data } = await apiInstance.coaApiCostAllocationsCreate(
    costAllocation
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **costAllocation** | **CostAllocation**|  | |


### Return type

**CostAllocation**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiCostAllocationsDestroy**
> coaApiCostAllocationsDestroy()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiCostAllocationsDestroy(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiCostAllocationsList**
> PaginatedCostAllocationList coaApiCostAllocationsList()

         Retrieve a list of cost allocations with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiCostAllocationsList(
    includeDeleted,
    lastModifiedAtGte,
    lastModifiedAtLte,
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedCostAllocationList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiCostAllocationsPartialUpdate**
> CostAllocation coaApiCostAllocationsPartialUpdate()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    PatchedCostAllocation
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let patchedCostAllocation: PatchedCostAllocation; // (optional)

const { status, data } = await apiInstance.coaApiCostAllocationsPartialUpdate(
    id,
    patchedCostAllocation
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedCostAllocation** | **PatchedCostAllocation**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**CostAllocation**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiCostAllocationsPreviewRetrieve**
> CostAllocationPreviewQuery coaApiCostAllocationsPreviewRetrieve()

Fan-out lines the posting path would produce for an amount, period, and entity. Writes nothing.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let amount: number; // (default to undefined)
let id: number; // (default to undefined)
let period: string; // (default to undefined)
let entity: number; // (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiCostAllocationsPreviewRetrieve(
    amount,
    id,
    period,
    entity
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **amount** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|
| **period** | [**string**] |  | defaults to undefined|
| **entity** | [**number**] |  | (optional) defaults to undefined|


### Return type

**CostAllocationPreviewQuery**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiCostAllocationsRetrieve**
> CostAllocation coaApiCostAllocationsRetrieve()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiCostAllocationsRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**CostAllocation**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiCostAllocationsSyncCreate**
> CostAllocationSync coaApiCostAllocationsSyncCreate(costAllocationSync)

Queue sync runs for an allocation\'s open entity-periods in the requested period, optionally for one entity.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    CostAllocationSync
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let costAllocationSync: CostAllocationSync; //

const { status, data } = await apiInstance.coaApiCostAllocationsSyncCreate(
    id,
    costAllocationSync
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **costAllocationSync** | **CostAllocationSync**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**CostAllocationSync**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiCostAllocationsSyncRunsList**
> PaginatedAllocationSyncRunList coaApiCostAllocationsSyncRunsList()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiCostAllocationsSyncRunsList(
    id,
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedAllocationSyncRunList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiCostAllocationsSyncRunsRetrieve**
> AllocationSyncRun coaApiCostAllocationsSyncRunsRetrieve()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let runPk: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiCostAllocationsSyncRunsRetrieve(
    id,
    runPk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|
| **runPk** | [**number**] |  | defaults to undefined|


### Return type

**AllocationSyncRun**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiCostAllocationsUpdate**
> CostAllocation coaApiCostAllocationsUpdate(costAllocation)


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    CostAllocation
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let costAllocation: CostAllocation; //

const { status, data } = await apiInstance.coaApiCostAllocationsUpdate(
    id,
    costAllocation
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **costAllocation** | **CostAllocation**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**CostAllocation**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiDepartmentCreate**
> Department coaApiDepartmentCreate(department)

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    Department
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let department: Department; //

const { status, data } = await apiInstance.coaApiDepartmentCreate(
    department
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **department** | **Department**|  | |


### Return type

**Department**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiDepartmentDeleteCreate**
> coaApiDepartmentDeleteCreate()

Delete a department and optionally reassign all related records to another department

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    DeleteRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let newDepartment: number; //ID of the department to reassign all related records to before deletion (optional) (default to undefined)
let deleteRequest: DeleteRequest; // (optional)

const { status, data } = await apiInstance.coaApiDepartmentDeleteCreate(
    id,
    newDepartment,
    deleteRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deleteRequest** | **DeleteRequest**|  | |
| **id** | [**number**] |  | defaults to undefined|
| **newDepartment** | [**number**] | ID of the department to reassign all related records to before deletion | (optional) defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | Deleted. |  -  |
|**202** | Sent for approval; the record is deleted once a reviewer approves. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiDepartmentDestroy**
> coaApiDepartmentDestroy()

Deprecated: use `POST /coa/api/department/{id}/delete`, which also takes an optional reason for the audit log.  Delete a department and optionally reassign all related records to another department

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let newDepartment: number; //ID of the department to reassign all related records to before deletion (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiDepartmentDestroy(
    id,
    newDepartment
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|
| **newDepartment** | [**number**] | ID of the department to reassign all related records to before deletion | (optional) defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | Deleted. |  -  |
|**202** | Sent for approval; the record is deleted once a reviewer approves. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiDepartmentList**
> PaginatedDepartmentList coaApiDepartmentList()

         Retrieve a list of departments with optional filtering and sorting.          Each department includes metadata about its parent department (`parent`, `parent_name`),         so parent/child department relationships can be reconstructed from the response.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let includeInactive: boolean; //Include inactive departments in results (optional) (default to true)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let q: string; //Search query - searches by department name or code (optional) (default to undefined)
let sort: string; //Sort order. Use field name for ascending, -field for descending. Supports multiple fields separated by comma. Default: name (optional) (default to 'name')

const { status, data } = await apiInstance.coaApiDepartmentList(
    includeDeleted,
    includeInactive,
    lastModifiedAtGte,
    lastModifiedAtLte,
    limit,
    offset,
    q,
    sort
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **includeInactive** | [**boolean**] | Include inactive departments in results | (optional) defaults to true|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **q** | [**string**] | Search query - searches by department name or code | (optional) defaults to undefined|
| **sort** | [**string**] | Sort order. Use field name for ascending, -field for descending. Supports multiple fields separated by comma. Default: name | (optional) defaults to 'name'|


### Return type

**PaginatedDepartmentList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiDepartmentPartialUpdate**
> Department coaApiDepartmentPartialUpdate()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    PatchedDepartment
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let patchedDepartment: PatchedDepartment; // (optional)

const { status, data } = await apiInstance.coaApiDepartmentPartialUpdate(
    id,
    patchedDepartment
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedDepartment** | **PatchedDepartment**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Department**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiDepartmentRetrieve**
> Department coaApiDepartmentRetrieve()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiDepartmentRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Department**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiDepartmentUpdate**
> Department coaApiDepartmentUpdate(department)


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    Department
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let department: Department; //

const { status, data } = await apiInstance.coaApiDepartmentUpdate(
    id,
    department
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **department** | **Department**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Department**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetClassCreate**
> FixedAssetClass coaApiFixedAssetClassCreate(fixedAssetClass)

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    FixedAssetClass
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let fixedAssetClass: FixedAssetClass; //

const { status, data } = await apiInstance.coaApiFixedAssetClassCreate(
    fixedAssetClass
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **fixedAssetClass** | **FixedAssetClass**|  | |


### Return type

**FixedAssetClass**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetClassDestroy**
> coaApiFixedAssetClassDestroy()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiFixedAssetClassDestroy(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetClassList**
> PaginatedFixedAssetClassList coaApiFixedAssetClassList()

         Retrieve a list of fixed asset classes with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiFixedAssetClassList(
    includeDeleted,
    lastModifiedAtGte,
    lastModifiedAtLte,
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedFixedAssetClassList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetClassPartialUpdate**
> FixedAssetClass coaApiFixedAssetClassPartialUpdate()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    PatchedFixedAssetClass
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let patchedFixedAssetClass: PatchedFixedAssetClass; // (optional)

const { status, data } = await apiInstance.coaApiFixedAssetClassPartialUpdate(
    id,
    patchedFixedAssetClass
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedFixedAssetClass** | **PatchedFixedAssetClass**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**FixedAssetClass**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetClassRetrieve**
> FixedAssetClass coaApiFixedAssetClassRetrieve()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiFixedAssetClassRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**FixedAssetClass**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetClassUpdate**
> FixedAssetClass coaApiFixedAssetClassUpdate(fixedAssetClass)


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    FixedAssetClass
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let fixedAssetClass: FixedAssetClass; //

const { status, data } = await apiInstance.coaApiFixedAssetClassUpdate(
    id,
    fixedAssetClass
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **fixedAssetClass** | **FixedAssetClass**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**FixedAssetClass**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagCreate**
> TransactionTag coaApiTagCreate(transactionTag)

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    TransactionTag
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let transactionTag: TransactionTag; //

const { status, data } = await apiInstance.coaApiTagCreate(
    transactionTag
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transactionTag** | **TransactionTag**|  | |


### Return type

**TransactionTag**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagDeleteCreate**
> coaApiTagDeleteCreate()

Delete a transaction tag and optionally merge it with another tag

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    DeleteRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let newTag: number; //ID of the tag to merge with before deletion (optional) (default to undefined)
let deleteRequest: DeleteRequest; // (optional)

const { status, data } = await apiInstance.coaApiTagDeleteCreate(
    id,
    newTag,
    deleteRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deleteRequest** | **DeleteRequest**|  | |
| **id** | [**number**] |  | defaults to undefined|
| **newTag** | [**number**] | ID of the tag to merge with before deletion | (optional) defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | Deleted. |  -  |
|**202** | Sent for approval; the record is deleted once a reviewer approves. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagDestroy**
> coaApiTagDestroy()

Deprecated: use `POST /coa/api/tag/{id}/delete`, which also takes an optional reason for the audit log.  Delete a transaction tag and optionally merge it with another tag

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let newTag: number; //ID of the tag to merge with before deletion (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiTagDestroy(
    id,
    newTag
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|
| **newTag** | [**number**] | ID of the tag to merge with before deletion | (optional) defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | Deleted. |  -  |
|**202** | Sent for approval; the record is deleted once a reviewer approves. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagGroupCreate**
> TransactionTagGroup coaApiTagGroupCreate(transactionTagGroup)

Mixin to provide consistent last_modified_at filtering and sorting functionality for List APIs with comprehensive timestamp computation.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    TransactionTagGroup
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let transactionTagGroup: TransactionTagGroup; //

const { status, data } = await apiInstance.coaApiTagGroupCreate(
    transactionTagGroup
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transactionTagGroup** | **TransactionTagGroup**|  | |


### Return type

**TransactionTagGroup**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagGroupDestroy**
> coaApiTagGroupDestroy()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTagGroupDestroy(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagGroupList**
> PaginatedTransactionTagGroupList coaApiTagGroupList()

         Retrieve a list of transaction tag groups with optional filtering and sorting.          Supports timestamp-based filtering for synchronization and audit purposes.         

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let q: string; //Search query - searches by group name (optional) (default to undefined)
let sort: string; //Sort order. Use field name for ascending, -field for descending. Default: name (optional) (default to 'name')

const { status, data } = await apiInstance.coaApiTagGroupList(
    lastModifiedAtGte,
    lastModifiedAtLte,
    limit,
    offset,
    q,
    sort
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **q** | [**string**] | Search query - searches by group name | (optional) defaults to undefined|
| **sort** | [**string**] | Sort order. Use field name for ascending, -field for descending. Default: name | (optional) defaults to 'name'|


### Return type

**PaginatedTransactionTagGroupList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagGroupPartialUpdate**
> TransactionTagGroup coaApiTagGroupPartialUpdate()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    PatchedTransactionTagGroup
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let patchedTransactionTagGroup: PatchedTransactionTagGroup; // (optional)

const { status, data } = await apiInstance.coaApiTagGroupPartialUpdate(
    id,
    patchedTransactionTagGroup
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedTransactionTagGroup** | **PatchedTransactionTagGroup**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**TransactionTagGroup**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagGroupRetrieve**
> TransactionTagGroup coaApiTagGroupRetrieve()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTagGroupRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**TransactionTagGroup**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagGroupUpdate**
> TransactionTagGroup coaApiTagGroupUpdate(transactionTagGroup)


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    TransactionTagGroup
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let transactionTagGroup: TransactionTagGroup; //

const { status, data } = await apiInstance.coaApiTagGroupUpdate(
    id,
    transactionTagGroup
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transactionTagGroup** | **TransactionTagGroup**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**TransactionTagGroup**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagList**
> PaginatedTransactionTagList coaApiTagList()

         Retrieve a list of transaction tags (custom dimensions) with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let excludeTags: string; //Comma-separated list of tag IDs to exclude (optional) (default to undefined)
let group: number; //Filter by tag group ID (optional) (default to undefined)
let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let includeInactive: boolean; //If true, include inactive tags (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let noGroup: boolean; //If true, only return tags without a group (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let parent: number; //Filter by parent tag ID (optional) (default to undefined)
let q: string; //Search query - searches by tag name or group name (optional) (default to undefined)
let sort: string; //Sort order. Use field name for ascending, -field for descending. Special field: group_name. Default: name (optional) (default to 'name')

const { status, data } = await apiInstance.coaApiTagList(
    excludeTags,
    group,
    includeDeleted,
    includeInactive,
    lastModifiedAtGte,
    lastModifiedAtLte,
    limit,
    noGroup,
    offset,
    parent,
    q,
    sort
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **excludeTags** | [**string**] | Comma-separated list of tag IDs to exclude | (optional) defaults to undefined|
| **group** | [**number**] | Filter by tag group ID | (optional) defaults to undefined|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **includeInactive** | [**boolean**] | If true, include inactive tags | (optional) defaults to false|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **noGroup** | [**boolean**] | If true, only return tags without a group | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **parent** | [**number**] | Filter by parent tag ID | (optional) defaults to undefined|
| **q** | [**string**] | Search query - searches by tag name or group name | (optional) defaults to undefined|
| **sort** | [**string**] | Sort order. Use field name for ascending, -field for descending. Special field: group_name. Default: name | (optional) defaults to 'name'|


### Return type

**PaginatedTransactionTagList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagPartialUpdate**
> TransactionTag coaApiTagPartialUpdate()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    PatchedTransactionTag
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let patchedTransactionTag: PatchedTransactionTag; // (optional)

const { status, data } = await apiInstance.coaApiTagPartialUpdate(
    id,
    patchedTransactionTag
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedTransactionTag** | **PatchedTransactionTag**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**TransactionTag**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagRetrieve**
> TransactionTag coaApiTagRetrieve()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTagRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**TransactionTag**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTagUpdate**
> TransactionTag coaApiTagUpdate(transactionTag)


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    TransactionTag
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let transactionTag: TransactionTag; //

const { status, data } = await apiInstance.coaApiTagUpdate(
    id,
    transactionTag
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transactionTag** | **TransactionTag**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**TransactionTag**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorContactTitleCreate**
> VendorContactTitle coaApiVendorContactTitleCreate(vendorContactTitle)

Mixin to provide consistent last_modified_at filtering and sorting functionality for List APIs with comprehensive timestamp computation.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    VendorContactTitle
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let vendorContactTitle: VendorContactTitle; //

const { status, data } = await apiInstance.coaApiVendorContactTitleCreate(
    vendorContactTitle
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **vendorContactTitle** | **VendorContactTitle**|  | |


### Return type

**VendorContactTitle**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorContactTitleDestroy**
> coaApiVendorContactTitleDestroy()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiVendorContactTitleDestroy(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorContactTitleList**
> PaginatedVendorContactTitleList coaApiVendorContactTitleList()

         Retrieve a list of vendor contact titles with optional filtering and sorting.          Supports timestamp-based filtering for synchronization and audit purposes.         

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let q: string; //Search query - searches by title name (optional) (default to undefined)
let sort: string; //Sort order. Use field name for ascending, -field for descending. Default: name (optional) (default to 'name')

const { status, data } = await apiInstance.coaApiVendorContactTitleList(
    lastModifiedAtGte,
    lastModifiedAtLte,
    limit,
    offset,
    q,
    sort
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **q** | [**string**] | Search query - searches by title name | (optional) defaults to undefined|
| **sort** | [**string**] | Sort order. Use field name for ascending, -field for descending. Default: name | (optional) defaults to 'name'|


### Return type

**PaginatedVendorContactTitleList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorContactTitlePartialUpdate**
> VendorContactTitle coaApiVendorContactTitlePartialUpdate()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    PatchedVendorContactTitle
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let patchedVendorContactTitle: PatchedVendorContactTitle; // (optional)

const { status, data } = await apiInstance.coaApiVendorContactTitlePartialUpdate(
    id,
    patchedVendorContactTitle
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedVendorContactTitle** | **PatchedVendorContactTitle**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**VendorContactTitle**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorContactTitleRetrieve**
> VendorContactTitle coaApiVendorContactTitleRetrieve()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiVendorContactTitleRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**VendorContactTitle**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorContactTitleUpdate**
> VendorContactTitle coaApiVendorContactTitleUpdate(vendorContactTitle)


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    VendorContactTitle
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let vendorContactTitle: VendorContactTitle; //

const { status, data } = await apiInstance.coaApiVendorContactTitleUpdate(
    id,
    vendorContactTitle
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **vendorContactTitle** | **VendorContactTitle**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**VendorContactTitle**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorCreate**
> Vendor coaApiVendorCreate(vendor)

Create a new vendor or customer in the system

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    Vendor
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let vendor: Vendor; //

const { status, data } = await apiInstance.coaApiVendorCreate(
    vendor
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **vendor** | **Vendor**|  | |


### Return type

**Vendor**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorDestroy**
> coaApiVendorDestroy()

Delete a vendor and optionally reassign all related records to another vendor. Returns 202 Accepted as deletion is processed asynchronously.

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let newVendor: string; //Identifier of the vendor to reassign all related records to before deletion. Accepts a Campfire ID (e.g. VEN-0000001) or the legacy internal integer id. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiVendorDestroy(
    id,
    newVendor
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|
| **newVendor** | [**string**] | Identifier of the vendor to reassign all related records to before deletion. Accepts a Campfire ID (e.g. VEN-0000001) or the legacy internal integer id. | (optional) defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorList**
> PaginatedVendorList coaApiVendorList()

         Retrieve a list of vendors/customers with optional filtering and sorting.          Each vendor includes metadata about its parent vendor (`parent`, `parent_name`) and its         full `lineage` (the ordered chain of ancestor vendors), so parent/child vendor         relationships can be reconstructed from the response.          Supports retrieving deleted records for audit purposes. When include_deleted=true,         returns ONLY deleted records with minimal data (id, is_deleted, deleted_at, last_modified_at).         When false or omitted, returns ONLY active records.         

### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let externalId: string; //Filter by external ID (optional) (default to undefined)
let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let includeInactive: boolean; //Include inactive vendors in results (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let q: string; //Search query - searches by name, DBA, email, or company name. If numeric, also searches by ID (optional) (default to undefined)
let sort: string; //Sort order. Use field name for ascending, -field for descending. Supports multiple fields separated by comma. Default: name (optional) (default to 'name')
let stripeCustomerId: string; //Filter by Stripe customer ID (exact match, e.g. cus_ABC123) (optional) (default to undefined)
let vendorType: 'customer' | 'vendor'; //Filter by vendor type. Can be specified multiple times for multiple types (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiVendorList(
    externalId,
    includeDeleted,
    includeInactive,
    lastModifiedAtGte,
    lastModifiedAtLte,
    limit,
    offset,
    q,
    sort,
    stripeCustomerId,
    vendorType
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **externalId** | [**string**] | Filter by external ID | (optional) defaults to undefined|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **includeInactive** | [**boolean**] | Include inactive vendors in results | (optional) defaults to false|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **q** | [**string**] | Search query - searches by name, DBA, email, or company name. If numeric, also searches by ID | (optional) defaults to undefined|
| **sort** | [**string**] | Sort order. Use field name for ascending, -field for descending. Supports multiple fields separated by comma. Default: name | (optional) defaults to 'name'|
| **stripeCustomerId** | [**string**] | Filter by Stripe customer ID (exact match, e.g. cus_ABC123) | (optional) defaults to undefined|
| **vendorType** | [**&#39;customer&#39; | &#39;vendor&#39;**]**Array<&#39;customer&#39; &#124; &#39;vendor&#39;>** | Filter by vendor type. Can be specified multiple times for multiple types | (optional) defaults to undefined|


### Return type

**PaginatedVendorList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorPartialUpdate**
> Vendor coaApiVendorPartialUpdate()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    PatchedVendor
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let patchedVendor: PatchedVendor; // (optional)

const { status, data } = await apiInstance.coaApiVendorPartialUpdate(
    id,
    patchedVendor
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedVendor** | **PatchedVendor**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Vendor**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorRetrieve**
> Vendor coaApiVendorRetrieve()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiVendorRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Vendor**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorUpdate**
> Vendor coaApiVendorUpdate(vendor)


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    Vendor
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let vendor: Vendor; //

const { status, data } = await apiInstance.coaApiVendorUpdate(
    id,
    vendor
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **vendor** | **Vendor**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Vendor**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createVendorCustomField**
> VendorCustomField1 createVendorCustomField(vendorCustomField1)


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    VendorCustomField1
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let vendorCustomField1: VendorCustomField1; //

const { status, data } = await apiInstance.createVendorCustomField(
    vendorCustomField1
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **vendorCustomField1** | **VendorCustomField1**|  | |


### Return type

**VendorCustomField1**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteVendorCustomField**
> deleteVendorCustomField()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.deleteVendorCustomField(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getVendorCustomField**
> VendorCustomField1 getVendorCustomField()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.getVendorCustomField(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**VendorCustomField1**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listVendorCustomFields**
> Array<VendorCustomField1> listVendorCustomFields()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

const { status, data } = await apiInstance.listVendorCustomFields();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<VendorCustomField1>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listVendorSummaries**
> PaginatedVendorSummaryList listVendorSummaries()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listVendorSummaries(
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedVendorSummaryList**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partialUpdateVendorCustomField**
> VendorCustomField1 partialUpdateVendorCustomField()


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    PatchedVendorCustomField1
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let patchedVendorCustomField1: PatchedVendorCustomField1; // (optional)

const { status, data } = await apiInstance.partialUpdateVendorCustomField(
    id,
    patchedVendorCustomField1
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedVendorCustomField1** | **PatchedVendorCustomField1**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**VendorCustomField1**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateVendorCustomField**
> VendorCustomField1 updateVendorCustomField(vendorCustomField1)


### Example

```typescript
import {
    CompanyObjectsApi,
    Configuration,
    VendorCustomField1
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CompanyObjectsApi(configuration);

let id: number; // (default to undefined)
let vendorCustomField1: VendorCustomField1; //

const { status, data } = await apiInstance.updateVendorCustomField(
    id,
    vendorCustomField1
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **vendorCustomField1** | **VendorCustomField1**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**VendorCustomField1**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


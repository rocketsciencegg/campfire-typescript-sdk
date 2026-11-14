# SettingsApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**caApiFileDestroy**](#caapifiledestroy) | **DELETE** /ca/api/file/{id} | Delete File|
|[**caApiFileList**](#caapifilelist) | **GET** /ca/api/file | List Files|
|[**caApiFilePartialUpdate**](#caapifilepartialupdate) | **PATCH** /ca/api/file/{id} | Patch File|
|[**caApiFileRetrieve**](#caapifileretrieve) | **GET** /ca/api/file/{id} | Get File|
|[**caApiFileUpdate**](#caapifileupdate) | **PUT** /ca/api/file/{id} | Update File|
|[**caApiFileUploadCreate**](#caapifileuploadcreate) | **POST** /ca/api/file/upload | Upload File|
|[**caApiUserCurrencyCreate**](#caapiusercurrencycreate) | **POST** /ca/api/user_currency | Create Customer Currencies|
|[**caApiUserCurrencyDestroy**](#caapiusercurrencydestroy) | **DELETE** /ca/api/user_currency/{id} | Delete Customer Currencies|
|[**caApiUserCurrencyList**](#caapiusercurrencylist) | **GET** /ca/api/user_currency | List Customer Currencies|
|[**caApiUserCurrencyPartialUpdate**](#caapiusercurrencypartialupdate) | **PATCH** /ca/api/user_currency/{id} | Partial Update Customer Currencies|
|[**caApiUserCurrencyRateRetrieve**](#caapiusercurrencyrateretrieve) | **GET** /ca/api/user_currency/rate | Get Currency Exchange Rate|
|[**caApiUserCurrencyRetrieve**](#caapiusercurrencyretrieve) | **GET** /ca/api/user_currency/{id} | Retrieve Customer Currencies|
|[**caApiUserCurrencyUpdate**](#caapiusercurrencyupdate) | **PUT** /ca/api/user_currency/{id} | Update Customer Currencies|
|[**caApiUserCurrencyWithRateRetrieve**](#caapiusercurrencywithrateretrieve) | **GET** /ca/api/user_currency/with_rate | Get Currencies Exchange Rates for Currency|
|[**caApiV1AuditLogList**](#caapiv1auditloglist) | **GET** /ca/api/v1/audit-log | List audit log entries|
|[**caApiV1AuditLogRetrieve**](#caapiv1auditlogretrieve) | **GET** /ca/api/v1/audit-log/{id} | Get one audit log entry, with readable payloads|
|[**coaApiEntityAttachmentCreate**](#coaapientityattachmentcreate) | **POST** /coa/api/entity/{entity_id}/attachment | Upload Entity Invoice Email Attachment|
|[**coaApiEntityCreate**](#coaapientitycreate) | **POST** /coa/api/entity | Create Chart Entity|
|[**coaApiEntityDestroy**](#coaapientitydestroy) | **DELETE** /coa/api/entity/{id} | Delete Chart Entity|
|[**coaApiEntityForIntercompanyList**](#coaapientityforintercompanylist) | **GET** /coa/api/entity/for-intercompany | List All Entities for Intercompany JE|
|[**coaApiEntityList**](#coaapientitylist) | **GET** /coa/api/entity | List Chart Entities|
|[**coaApiEntityLogoCreate**](#coaapientitylogocreate) | **POST** /coa/api/entity/{id}/logo | Upload Chart Entity Logo|
|[**coaApiEntityPartialUpdate**](#coaapientitypartialupdate) | **PATCH** /coa/api/entity/{id} | Partial Update Chart Entity|
|[**coaApiEntityRetrieve**](#coaapientityretrieve) | **GET** /coa/api/entity/{id} | Retrieve Chart Entity|
|[**coaApiEntityUpdate**](#coaapientityupdate) | **PUT** /coa/api/entity/{id} | Update Chart Entity|
|[**getFileTempDownloadUrl**](#getfiletempdownloadurl) | **GET** /ca/api/file/{id}/temp-download-url | Get File Temporary Download URL|
|[**settingsPartialUpdateChartAccountSettings**](#settingspartialupdatechartaccountsettings) | **PATCH** /coa/api/chart-account-settings | Partially Update Chart Account Settings|
|[**settingsRetrieveChartAccountSettings**](#settingsretrievechartaccountsettings) | **GET** /coa/api/chart-account-settings | Retrieve Chart Account Settings|
|[**settingsUpdateChartAccountSettings**](#settingsupdatechartaccountsettings) | **PUT** /coa/api/chart-account-settings | Update Chart Account Settings|

# **caApiFileDestroy**
> caApiFileDestroy()


### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.caApiFileDestroy(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiFileList**
> PaginatedFileList caApiFileList()

         Retrieve a list of files with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.caApiFileList(
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

**PaginatedFileList**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiFilePartialUpdate**
> any caApiFilePartialUpdate()


### Example

```typescript
import {
    SettingsApi,
    Configuration,
    PatchedFile
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)
let patchedFile: PatchedFile; // (optional)

const { status, data } = await apiInstance.caApiFilePartialUpdate(
    id,
    patchedFile
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedFile** | **PatchedFile**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**any**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiFileRetrieve**
> any caApiFileRetrieve()


### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.caApiFileRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**any**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiFileUpdate**
> any caApiFileUpdate(modelFile)


### Example

```typescript
import {
    SettingsApi,
    Configuration,
    ModelFile
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)
let modelFile: ModelFile; //

const { status, data } = await apiInstance.caApiFileUpdate(
    id,
    modelFile
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **modelFile** | **ModelFile**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**any**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiFileUploadCreate**
> caApiFileUploadCreate()

         Upload a file directly to Campfire. This is the primary way to upload files.          **Supported Models:**         bill, chat, close_task, closecheckitem, contract, credit_memo, customer, debit_memo, draft_queue, fixed_asset, forecast, intercompany_journal, invoice, journal_entry, journalentry, lease_v2, migration_record, policy, reconciliation, reconciliation_report, revenue_contract          **Supported Content Types:**         application/msword, application/pdf, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/vnd.openxmlformats-officedocument.presentationml.presentation, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.openxmlformats-officedocument.wordprocessingml.document, image/gif, image/jpeg, image/jpg, image/png, image/webp, text/csv, text/markdown, text/plain, text/x-markdown          **Maximum File Size:** 100MB          **Example:**         ```bash         curl -X POST \"https://api.meetcampfire.com/ca/api/file/upload?model=bill&object_id=12345\" \\           -H \"Authorization: Token YOUR_TOKEN\" \\           -F \"file=@receipt.pdf\"         ```          **OAuth Apps:** attaching a file changes the record, so an app token needs the write scope for         that record type (e.g. `journal_entries:write` for `model=journal_entry`), and the person who         connected the app must hold the same permission. Apps pass `model` alone, never `app`.          **Query Parameters:**         - `model` (required): Model type (e.g., \"bill\", \"invoice\", \"contract\")         - `object_id` (optional): ID of the object to attach the file to          **Request Body:**         - `file` (required): The file to upload (multipart/form-data)         

### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

const { status, data } = await apiInstance.caApiFileUploadCreate();
```

### Parameters
This endpoint does not have any parameters.


### Return type

void (empty response body)

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiUserCurrencyCreate**
> CustomerCurrency caApiUserCurrencyCreate(customerCurrency)

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    SettingsApi,
    Configuration,
    CustomerCurrency
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let customerCurrency: CustomerCurrency; //

const { status, data } = await apiInstance.caApiUserCurrencyCreate(
    customerCurrency
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customerCurrency** | **CustomerCurrency**|  | |


### Return type

**CustomerCurrency**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiUserCurrencyDestroy**
> caApiUserCurrencyDestroy()


### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.caApiUserCurrencyDestroy(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiUserCurrencyList**
> PaginatedCustomerCurrencyList caApiUserCurrencyList()

         Retrieve a list of customer currencies with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.caApiUserCurrencyList(
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

**PaginatedCustomerCurrencyList**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiUserCurrencyPartialUpdate**
> CustomerCurrency caApiUserCurrencyPartialUpdate()


### Example

```typescript
import {
    SettingsApi,
    Configuration,
    PatchedCustomerCurrency
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)
let patchedCustomerCurrency: PatchedCustomerCurrency; // (optional)

const { status, data } = await apiInstance.caApiUserCurrencyPartialUpdate(
    id,
    patchedCustomerCurrency
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedCustomerCurrency** | **PatchedCustomerCurrency**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**CustomerCurrency**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiUserCurrencyRateRetrieve**
> caApiUserCurrencyRateRetrieve()


### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

const { status, data } = await apiInstance.caApiUserCurrencyRateRetrieve();
```

### Parameters
This endpoint does not have any parameters.


### Return type

void (empty response body)

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiUserCurrencyRetrieve**
> CustomerCurrency caApiUserCurrencyRetrieve()


### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.caApiUserCurrencyRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**CustomerCurrency**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiUserCurrencyUpdate**
> CustomerCurrency caApiUserCurrencyUpdate(customerCurrency)


### Example

```typescript
import {
    SettingsApi,
    Configuration,
    CustomerCurrency
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)
let customerCurrency: CustomerCurrency; //

const { status, data } = await apiInstance.caApiUserCurrencyUpdate(
    id,
    customerCurrency
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **customerCurrency** | **CustomerCurrency**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**CustomerCurrency**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiUserCurrencyWithRateRetrieve**
> caApiUserCurrencyWithRateRetrieve()


### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

const { status, data } = await apiInstance.caApiUserCurrencyWithRateRetrieve();
```

### Parameters
This endpoint does not have any parameters.


### Return type

void (empty response body)

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiV1AuditLogList**
> PaginatedAuditLogEntrySchemaList caApiV1AuditLogList()

         Retrieve approved audit log entries: each change to a record, with who made it, who approved it,         and the record\'s payload before and after. Entries are ordered newest first by (created_at, id).          **Access:** customer admins, or users with the \"View audit logs\" permission. OAuth apps also need         the `audit_logs:read` scope. Users restricted to some entities see only entries whose every entity         they can access.          **Filtering:**         - `created_at__gte` (inclusive) and `created_at__lt` (exclusive) take an ISO 8601 date, read as           00:00 UTC, or a datetime with a UTC offset. URL-encode the `+` in an offset as `%2B`.         - `model` (as `app_label.model`) returns that object type; with `object_id` it returns that           object\'s entries and the entries of records under it, such as a bill\'s payments.         - Unknown parameters are rejected with a 400.          **Paging:**         - For a complete export, pass an empty cursor (`cursor=`) on the first request and follow the           `next` URL until it is null. Entries written while you page don\'t shift later pages.         - Pass `skip_count=true` when you don\'t need the total; `count` stops at 10,000.          **Notes:**         - The entry\'s `approved_by` is who gave final approval. Inside `approvers`, `approved_by` is the           step\'s approver type and `approved_by_user` is who approved that step; it can be empty for           steps approved before step approvers were recorded.         - Entries recorded when data was first imported can appear later with historical `created_at` dates.         - Payload fields that hold secrets are stored hashed.         

### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let actionType: Array<string>; //created, updated or deleted. Repeat or comma-separate. (optional) (default to undefined)
let approvedBy: number; //User who gave final approval. (optional) (default to undefined)
let createdAtGte: string; //Start, inclusive. Use an ISO 8601 date or a datetime with a UTC offset, such as 2026-03-10T11:00:00-04:00. (optional) (default to undefined)
let createdAtLt: string; //End, exclusive. Use an ISO 8601 date or a datetime with a UTC offset, such as 2026-03-10T11:00:00-04:00. (optional) (default to undefined)
let createdBy: number; //User who made the change. (optional) (default to undefined)
let cursor: string; //Opts into cursor pagination. Pass an empty value (cursor=) on the first request, then follow the next URL until it is null. Recommended for complete exports: rows written while paging don\'t shift pages, so none are skipped or repeated. (optional) (default to undefined)
let limit: number; //Page size. Default 100, maximum 10000. (optional) (default to undefined)
let model: string; //Object type as app_label.model. Open set. (optional) (default to undefined)
let objectId: number; //Rows for this object, or whose parent is this object. Needs model. (optional) (default to undefined)
let offset: number; //Number of records to skip. Use with limit to paginate. (optional) (default to undefined)
let operation: string; //Raw operation, such as add or delete. Open set. (optional) (default to undefined)
let parentDraftQueue: number; //Rows written as part of this audit entry. (optional) (default to undefined)
let skipCount: boolean; //When true, skips the total count. Recommended for large exports. (optional) (default to undefined)

const { status, data } = await apiInstance.caApiV1AuditLogList(
    actionType,
    approvedBy,
    createdAtGte,
    createdAtLt,
    createdBy,
    cursor,
    limit,
    model,
    objectId,
    offset,
    operation,
    parentDraftQueue,
    skipCount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **actionType** | **Array&lt;string&gt;** | created, updated or deleted. Repeat or comma-separate. | (optional) defaults to undefined|
| **approvedBy** | [**number**] | User who gave final approval. | (optional) defaults to undefined|
| **createdAtGte** | [**string**] | Start, inclusive. Use an ISO 8601 date or a datetime with a UTC offset, such as 2026-03-10T11:00:00-04:00. | (optional) defaults to undefined|
| **createdAtLt** | [**string**] | End, exclusive. Use an ISO 8601 date or a datetime with a UTC offset, such as 2026-03-10T11:00:00-04:00. | (optional) defaults to undefined|
| **createdBy** | [**number**] | User who made the change. | (optional) defaults to undefined|
| **cursor** | [**string**] | Opts into cursor pagination. Pass an empty value (cursor&#x3D;) on the first request, then follow the next URL until it is null. Recommended for complete exports: rows written while paging don\&#39;t shift pages, so none are skipped or repeated. | (optional) defaults to undefined|
| **limit** | [**number**] | Page size. Default 100, maximum 10000. | (optional) defaults to undefined|
| **model** | [**string**] | Object type as app_label.model. Open set. | (optional) defaults to undefined|
| **objectId** | [**number**] | Rows for this object, or whose parent is this object. Needs model. | (optional) defaults to undefined|
| **offset** | [**number**] | Number of records to skip. Use with limit to paginate. | (optional) defaults to undefined|
| **operation** | [**string**] | Raw operation, such as add or delete. Open set. | (optional) defaults to undefined|
| **parentDraftQueue** | [**number**] | Rows written as part of this audit entry. | (optional) defaults to undefined|
| **skipCount** | [**boolean**] | When true, skips the total count. Recommended for large exports. | (optional) defaults to undefined|


### Return type

**PaginatedAuditLogEntrySchemaList**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**400** | An unknown parameter or an invalid filter value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiV1AuditLogRetrieve**
> AuditLogEntrySchema caApiV1AuditLogRetrieve()

         Retrieve one approved audit log entry by id, with its payloads expanded into readable values.         Access is the same as for the list: an entry the list hides is a 404 here.         

### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.caApiV1AuditLogRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**AuditLogEntrySchema**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**404** | No approved entry with this id that you can access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiEntityAttachmentCreate**
> coaApiEntityAttachmentCreate()

Upload invoice email attachment with proper permissions

### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let entityId: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiEntityAttachmentCreate(
    entityId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **entityId** | [**number**] |  | defaults to undefined|


### Return type

void (empty response body)

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiEntityCreate**
> ChartEntity coaApiEntityCreate(chartEntity)

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    SettingsApi,
    Configuration,
    ChartEntity
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let chartEntity: ChartEntity; //

const { status, data } = await apiInstance.coaApiEntityCreate(
    chartEntity
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **chartEntity** | **ChartEntity**|  | |


### Return type

**ChartEntity**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiEntityDestroy**
> coaApiEntityDestroy()


### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiEntityDestroy(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiEntityForIntercompanyList**
> Array<ChartEntityMinimal> coaApiEntityForIntercompanyList()

Returns every operating entity for intercompany journal entry creation. Adjusting entities are left out: they are never an intercompany leg or counterparty.  This endpoint bypasses entity-scoped filtering because users need to select entities they don\'t normally have access to when creating intercompany journal entries (per the entity-scoped-user-access spec).  Uses minimal serializer to only expose id, name, and currency - preventing data leakage of sensitive entity details to users who may not have full access to all entities.

### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

const { status, data } = await apiInstance.coaApiEntityForIntercompanyList();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<ChartEntityMinimal>**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiEntityList**
> Array<ChartEntity> coaApiEntityList()

Retrieve a list of chart entities with optional filtering

### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let excludeAdjusting: boolean; //Exclude adjusting entities (those with a primary_entity set) from results. Defaults to false for backwards compatibility. (optional) (default to false)
let includeInactive: boolean; //Include inactive entities in results (optional) (default to true)

const { status, data } = await apiInstance.coaApiEntityList(
    excludeAdjusting,
    includeInactive
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **excludeAdjusting** | [**boolean**] | Exclude adjusting entities (those with a primary_entity set) from results. Defaults to false for backwards compatibility. | (optional) defaults to false|
| **includeInactive** | [**boolean**] | Include inactive entities in results | (optional) defaults to true|


### Return type

**Array<ChartEntity>**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiEntityLogoCreate**
> coaApiEntityLogoCreate()


### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiEntityLogoCreate(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiEntityPartialUpdate**
> ChartEntity coaApiEntityPartialUpdate()


### Example

```typescript
import {
    SettingsApi,
    Configuration,
    PatchedChartEntity
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)
let patchedChartEntity: PatchedChartEntity; // (optional)

const { status, data } = await apiInstance.coaApiEntityPartialUpdate(
    id,
    patchedChartEntity
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedChartEntity** | **PatchedChartEntity**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ChartEntity**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiEntityRetrieve**
> ChartEntity coaApiEntityRetrieve()


### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiEntityRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ChartEntity**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiEntityUpdate**
> ChartEntity coaApiEntityUpdate(chartEntity)


### Example

```typescript
import {
    SettingsApi,
    Configuration,
    ChartEntity
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)
let chartEntity: ChartEntity; //

const { status, data } = await apiInstance.coaApiEntityUpdate(
    id,
    chartEntity
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **chartEntity** | **ChartEntity**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ChartEntity**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getFileTempDownloadUrl**
> getFileTempDownloadUrl()

Return a short-lived presigned S3 URL for downloading a file.  Pass ``?disposition=inline`` to render preview-safe types (PDF, images) in the browser instead of forcing a download.  :param request: The incoming DRF request (must be authenticated). :return: JSON response with ``url`` key or an error.

### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.getFileTempDownloadUrl(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settingsPartialUpdateChartAccountSettings**
> ChartAccountSettings settingsPartialUpdateChartAccountSettings()

Partially update the default chart accounts to be used across the platform. Each input is the id to an existing chart account.

### Example

```typescript
import {
    SettingsApi,
    Configuration,
    PatchedChartAccountSettings
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let patchedChartAccountSettings: PatchedChartAccountSettings; // (optional)

const { status, data } = await apiInstance.settingsPartialUpdateChartAccountSettings(
    patchedChartAccountSettings
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedChartAccountSettings** | **PatchedChartAccountSettings**|  | |


### Return type

**ChartAccountSettings**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settingsRetrieveChartAccountSettings**
> ChartAccountSettings settingsRetrieveChartAccountSettings()

These are the defaults chart accounts to be used across the platform. Each input is the id to an existing chart account.

### Example

```typescript
import {
    SettingsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

const { status, data } = await apiInstance.settingsRetrieveChartAccountSettings();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**ChartAccountSettings**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settingsUpdateChartAccountSettings**
> ChartAccountSettings settingsUpdateChartAccountSettings(chartAccountSettings)

These are the defaults chart accounts to be used across the platform. Each input is the id to an existing chart account.

### Example

```typescript
import {
    SettingsApi,
    Configuration,
    ChartAccountSettings
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new SettingsApi(configuration);

let chartAccountSettings: ChartAccountSettings; //

const { status, data } = await apiInstance.settingsUpdateChartAccountSettings(
    chartAccountSettings
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **chartAccountSettings** | **ChartAccountSettings**|  | |


### Return type

**ChartAccountSettings**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


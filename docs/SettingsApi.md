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
|[**caApiUserCurrencyRetrieve**](#caapiusercurrencyretrieve) | **GET** /ca/api/user_currency/{id} | Retrieve Customer Currencies|
|[**caApiUserCurrencyUpdate**](#caapiusercurrencyupdate) | **PUT** /ca/api/user_currency/{id} | Update Customer Currencies|
|[**caApiUserCurrencyWithRateRetrieve**](#caapiusercurrencywithrateretrieve) | **GET** /ca/api/user_currency/with_rate | Get Currencies Exchange Rates for Currency|
|[**coaApiEntityCreate**](#coaapientitycreate) | **POST** /coa/api/entity | Create Chart Entity|
|[**coaApiEntityDestroy**](#coaapientitydestroy) | **DELETE** /coa/api/entity/{id} | Delete Chart Entity|
|[**coaApiEntityForIntercompanyList**](#coaapientityforintercompanylist) | **GET** /coa/api/entity/for-intercompany | List All Entities for Intercompany JE|
|[**coaApiEntityList**](#coaapientitylist) | **GET** /coa/api/entity | List Chart Entities|
|[**coaApiEntityLogoCreate**](#coaapientitylogocreate) | **POST** /coa/api/entity/{id}/logo | Upload Chart Entity Logo|
|[**coaApiEntityPartialUpdate**](#coaapientitypartialupdate) | **PATCH** /coa/api/entity/{id} | Partial Update Chart Entity|
|[**coaApiEntityRetrieve**](#coaapientityretrieve) | **GET** /coa/api/entity/{id} | Retrieve Chart Entity|
|[**coaApiEntityUpdate**](#coaapientityupdate) | **PUT** /coa/api/entity/{id} | Update Chart Entity|
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
|**200** | Successful response |  -  |

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
|**200** | Successful response |  -  |

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
|**200** | Successful response |  -  |

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
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiFileUploadCreate**
> caApiFileUploadCreate()

         Upload a file directly to Campfire. This is the primary way to upload files.          **Supported Models:**         bill, chat, close_task, closecheckitem, contract, credit_memo, customer, debit_memo, draft_queue, fixed_asset, intercompany_journal, invoice, journal_entry, journalentry, reconciliation, reconciliation_report          **Supported Content Types:**         application/msword, application/pdf, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/vnd.openxmlformats-officedocument.presentationml.presentation, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.openxmlformats-officedocument.wordprocessingml.document, image/gif, image/jpeg, image/jpg, image/png, image/webp, text/csv, text/plain          **Maximum File Size:** 100MB          **Example:**         ```bash         curl -X POST \"https://api.meetcampfire.com/ca/api/file/upload?model=bill&object_id=12345\" \\           -H \"Authorization: Token YOUR_TOKEN\" \\           -F \"file=@receipt.pdf\"         ```          **Query Parameters:**         - `model` (required): Model type (e.g., \"bill\", \"invoice\", \"contract\")         - `object_id` (optional): ID of the object to attach the file to          **Request Body:**         - `file` (required): The file to upload (multipart/form-data)         

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
> CustomerCurrency caApiUserCurrencyCreate()

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

let customerCurrency: CustomerCurrency; // (optional)

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
|**200** | Successful response |  -  |

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
|**200** | Successful response |  -  |

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
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiUserCurrencyUpdate**
> CustomerCurrency caApiUserCurrencyUpdate()


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
let customerCurrency: CustomerCurrency; // (optional)

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
|**200** | Successful response |  -  |

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

# **coaApiEntityCreate**
> ChartEntity coaApiEntityCreate()

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

let chartEntity: ChartEntity; // (optional)

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

Returns ALL entities for intercompany journal entry creation.  This endpoint bypasses entity-scoped filtering because users need to select entities they don\'t normally have access to when creating intercompany journal entries (per the entity-scoped-user-access spec).  Uses minimal serializer to only expose id, name, and currency - preventing data leakage of sensitive entity details to users who may not have full access to all entities.

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
|**200** | Successful response |  -  |

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

let includeInactive: boolean; //Include inactive entities in results (optional) (default to true)

const { status, data } = await apiInstance.coaApiEntityList(
    includeInactive
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
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
|**200** | Successful response |  -  |

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
|**200** | Successful response |  -  |

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
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiEntityUpdate**
> ChartEntity coaApiEntityUpdate()


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
let chartEntity: ChartEntity; // (optional)

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
|**200** | Successful response |  -  |

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
|**200** | Successful response |  -  |

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
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settingsUpdateChartAccountSettings**
> ChartAccountSettings settingsUpdateChartAccountSettings()

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

let chartAccountSettings: ChartAccountSettings; // (optional)

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
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


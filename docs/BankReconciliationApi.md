# BankReconciliationApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**coaApiV2ReconciliationCreate**](#coaapiv2reconciliationcreate) | **POST** /coa/api/v2/reconciliation | Create Bank Reconciliation Report|
|[**coaApiV2ReconciliationDestroy**](#coaapiv2reconciliationdestroy) | **DELETE** /coa/api/v2/reconciliation/{id} | Delete Bank Reconciliation Report|
|[**coaApiV2ReconciliationList**](#coaapiv2reconciliationlist) | **GET** /coa/api/v2/reconciliation | List Bank Reconciliation Reports|
|[**coaApiV2ReconciliationPartialUpdate**](#coaapiv2reconciliationpartialupdate) | **PATCH** /coa/api/v2/reconciliation/{id} | Partial Update Bank Reconciliation Report|
|[**coaApiV2ReconciliationRetrieve**](#coaapiv2reconciliationretrieve) | **GET** /coa/api/v2/reconciliation/{id} | Get Bank Reconciliation Report|
|[**coaApiV2ReconciliationSourceTransactionsList**](#coaapiv2reconciliationsourcetransactionslist) | **GET** /coa/api/v2/reconciliation/{id}/source-transactions | List GL Transactions for Reconciliation|
|[**coaApiV2ReconciliationTransactionsConfirmCreate**](#coaapiv2reconciliationtransactionsconfirmcreate) | **POST** /coa/api/v2/reconciliation/{id}/transactions/confirm | Confirm Selection of Transactions to Reconcile|
|[**coaApiV2ReconciliationUpdate**](#coaapiv2reconciliationupdate) | **PUT** /coa/api/v2/reconciliation/{id} | Update Bank Reconciliation Report|

# **coaApiV2ReconciliationCreate**
> ReconciliationReportV2 coaApiV2ReconciliationCreate(reconciliationReportV2)

Create a new bank reconciliation report for a specific account and date range. Cannot create overlapping date ranges for the same account and entity.

### Example

```typescript
import {
    BankReconciliationApi,
    Configuration,
    ReconciliationReportV2
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new BankReconciliationApi(configuration);

let reconciliationReportV2: ReconciliationReportV2; //

const { status, data } = await apiInstance.coaApiV2ReconciliationCreate(
    reconciliationReportV2
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **reconciliationReportV2** | **ReconciliationReportV2**|  | |


### Return type

**ReconciliationReportV2**

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

# **coaApiV2ReconciliationDestroy**
> coaApiV2ReconciliationDestroy()

Delete a bank reconciliation report and all associated data.

### Example

```typescript
import {
    BankReconciliationApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new BankReconciliationApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV2ReconciliationDestroy(
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

# **coaApiV2ReconciliationList**
> PaginatedReconciliationReportV2List coaApiV2ReconciliationList()

Retrieve a paginated list of bank reconciliation reports. Supports filtering by start_date, end_date, entity, account, and search query (q). Default sort is by statement_ending_date descending.

### Example

```typescript
import {
    BankReconciliationApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new BankReconciliationApi(configuration);

let account: number; //Filter by account ID (optional) (default to undefined)
let endDate: string; //Filter by maximum statement ending date (YYYY-MM-DD) (optional) (default to undefined)
let entity: number; //Filter by entity ID (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let q: string; //Search term for account name, number, or reconciled_by name (optional) (default to undefined)
let sort: string; //Sort field (prefix with - for descending) (optional) (default to undefined)
let startDate: string; //Filter by minimum statement ending date (YYYY-MM-DD) (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiV2ReconciliationList(
    account,
    endDate,
    entity,
    limit,
    offset,
    q,
    sort,
    startDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **account** | [**number**] | Filter by account ID | (optional) defaults to undefined|
| **endDate** | [**string**] | Filter by maximum statement ending date (YYYY-MM-DD) | (optional) defaults to undefined|
| **entity** | [**number**] | Filter by entity ID | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **q** | [**string**] | Search term for account name, number, or reconciled_by name | (optional) defaults to undefined|
| **sort** | [**string**] | Sort field (prefix with - for descending) | (optional) defaults to undefined|
| **startDate** | [**string**] | Filter by minimum statement ending date (YYYY-MM-DD) | (optional) defaults to undefined|


### Return type

**PaginatedReconciliationReportV2List**

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

# **coaApiV2ReconciliationPartialUpdate**
> ReconciliationReportV2 coaApiV2ReconciliationPartialUpdate()

Partially update a bank reconciliation report. Only provided fields are modified.

### Example

```typescript
import {
    BankReconciliationApi,
    Configuration,
    PatchedReconciliationReportV2
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new BankReconciliationApi(configuration);

let id: number; // (default to undefined)
let patchedReconciliationReportV2: PatchedReconciliationReportV2; // (optional)

const { status, data } = await apiInstance.coaApiV2ReconciliationPartialUpdate(
    id,
    patchedReconciliationReportV2
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedReconciliationReportV2** | **PatchedReconciliationReportV2**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ReconciliationReportV2**

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

# **coaApiV2ReconciliationRetrieve**
> ReconciliationReportV2 coaApiV2ReconciliationRetrieve()

Retrieve a specific bank reconciliation report by ID. Includes report metadata, status, async task status for PDF processing, and attached files/CSV statements.

### Example

```typescript
import {
    BankReconciliationApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new BankReconciliationApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV2ReconciliationRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ReconciliationReportV2**

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

# **coaApiV2ReconciliationSourceTransactionsList**
> PaginatedReconciliationReportV2SourceTransactionList coaApiV2ReconciliationSourceTransactionsList()

List source (GL) transactions available for reconciliation. Supports filtering by date range, bank, vendor, department, tag, currency, and reconciliation status.

### Example

```typescript
import {
    BankReconciliationApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new BankReconciliationApi(configuration);

let id: number; // (default to undefined)
let bank: number; //Filter by bank account ID (optional) (default to undefined)
let currency: string; //Filter by currency code (e.g., USD, EUR) (optional) (default to undefined)
let department: number; //Filter by department ID (optional) (default to undefined)
let endDate: string; //Filter by maximum posted date (YYYY-MM-DD) (optional) (default to undefined)
let group: number; //Filter by tag group ID (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let q: string; //Search term for bank description, journal memo, journal order, or amount (optional) (default to undefined)
let reconciledOnly: string; //Set to \'true\' to show only reconciled transactions for this report (optional) (default to undefined)
let sort: string; //Sort field(s), comma-separated (prefix with - for descending). Default: posted_at (optional) (default to undefined)
let startDate: string; //Filter by minimum posted date (YYYY-MM-DD) (optional) (default to undefined)
let tag: number; //Filter by tag ID (optional) (default to undefined)
let unreconciled: string; //Set to \'true\' to show only unreconciled transactions (optional) (default to undefined)
let vendor: number; //Filter by vendor/payee ID (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiV2ReconciliationSourceTransactionsList(
    id,
    bank,
    currency,
    department,
    endDate,
    group,
    limit,
    offset,
    q,
    reconciledOnly,
    sort,
    startDate,
    tag,
    unreconciled,
    vendor
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|
| **bank** | [**number**] | Filter by bank account ID | (optional) defaults to undefined|
| **currency** | [**string**] | Filter by currency code (e.g., USD, EUR) | (optional) defaults to undefined|
| **department** | [**number**] | Filter by department ID | (optional) defaults to undefined|
| **endDate** | [**string**] | Filter by maximum posted date (YYYY-MM-DD) | (optional) defaults to undefined|
| **group** | [**number**] | Filter by tag group ID | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **q** | [**string**] | Search term for bank description, journal memo, journal order, or amount | (optional) defaults to undefined|
| **reconciledOnly** | [**string**] | Set to \&#39;true\&#39; to show only reconciled transactions for this report | (optional) defaults to undefined|
| **sort** | [**string**] | Sort field(s), comma-separated (prefix with - for descending). Default: posted_at | (optional) defaults to undefined|
| **startDate** | [**string**] | Filter by minimum posted date (YYYY-MM-DD) | (optional) defaults to undefined|
| **tag** | [**number**] | Filter by tag ID | (optional) defaults to undefined|
| **unreconciled** | [**string**] | Set to \&#39;true\&#39; to show only unreconciled transactions | (optional) defaults to undefined|
| **vendor** | [**number**] | Filter by vendor/payee ID | (optional) defaults to undefined|


### Return type

**PaginatedReconciliationReportV2SourceTransactionList**

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

# **coaApiV2ReconciliationTransactionsConfirmCreate**
> coaApiV2ReconciliationTransactionsConfirmCreate(confirmTransactionSelectionRequest)

Confirm the selection of GL transactions for reconciliation. Pass selected transaction IDs in the request body. Selected transactions are marked as RECONCILED; deselected transactions have their status as suggested matches to this reconciliation report cleared.

### Example

```typescript
import {
    BankReconciliationApi,
    Configuration,
    ConfirmTransactionSelectionRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new BankReconciliationApi(configuration);

let id: number; // (default to undefined)
let confirmTransactionSelectionRequest: ConfirmTransactionSelectionRequest; //

const { status, data } = await apiInstance.coaApiV2ReconciliationTransactionsConfirmCreate(
    id,
    confirmTransactionSelectionRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **confirmTransactionSelectionRequest** | **ConfirmTransactionSelectionRequest**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

void (empty response body)

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |
|**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV2ReconciliationUpdate**
> ReconciliationReportV2 coaApiV2ReconciliationUpdate(reconciliationReportV2)

Update a bank reconciliation report. Supports partial updates via PATCH.

### Example

```typescript
import {
    BankReconciliationApi,
    Configuration,
    ReconciliationReportV2
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new BankReconciliationApi(configuration);

let id: number; // (default to undefined)
let reconciliationReportV2: ReconciliationReportV2; //

const { status, data } = await apiInstance.coaApiV2ReconciliationUpdate(
    id,
    reconciliationReportV2
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **reconciliationReportV2** | **ReconciliationReportV2**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ReconciliationReportV2**

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


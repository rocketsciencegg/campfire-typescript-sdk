# CashManagementApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**caApiAccountDestroy**](#caapiaccountdestroy) | **DELETE** /ca/api/account/{id} | Delete Bank Account|
|[**caApiAccountPartialUpdate**](#caapiaccountpartialupdate) | **PATCH** /ca/api/account/{id} | Partial Update Bank Account|
|[**caApiAccountRetrieve**](#caapiaccountretrieve) | **GET** /ca/api/account/{id} | Retrieve Bank Account|
|[**caApiAccountUpdate**](#caapiaccountupdate) | **PUT** /ca/api/account/{id} | Update Bank Account|
|[**caApiTransactionDestroy**](#caapitransactiondestroy) | **DELETE** /ca/api/transaction/{id} | Delete Bank Transaction|
|[**caApiTransactionPartialUpdate**](#caapitransactionpartialupdate) | **PATCH** /ca/api/transaction/{id} | Partial Update Bank Transaction|
|[**caApiTransactionRetrieve**](#caapitransactionretrieve) | **GET** /ca/api/transaction/{id} | Retrieve Bank Transaction|
|[**caApiTransactionUpdate**](#caapitransactionupdate) | **PUT** /ca/api/transaction/{id} | Update Bank Transaction|
|[**createAccount**](#createaccount) | **POST** /ca/api/account | Create Bank Account|
|[**createBankTransaction**](#createbanktransaction) | **POST** /ca/api/transaction | Create Bank Transaction|
|[**listAccounts**](#listaccounts) | **GET** /ca/api/account | List Bank Accounts|
|[**listBankTransactions**](#listbanktransactions) | **GET** /ca/api/transaction | List Bank Transactions|

# **caApiAccountDestroy**
> caApiAccountDestroy()


### Example

```typescript
import {
    CashManagementApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CashManagementApi(configuration);

let id: number; // (default to undefined)
let newAccount: number; //ID of the bank account to reassign transactions to before deletion (optional) (default to undefined)

const { status, data } = await apiInstance.caApiAccountDestroy(
    id,
    newAccount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|
| **newAccount** | [**number**] | ID of the bank account to reassign transactions to before deletion | (optional) defaults to undefined|


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

# **caApiAccountPartialUpdate**
> BankAccount caApiAccountPartialUpdate()


### Example

```typescript
import {
    CashManagementApi,
    Configuration,
    PatchedBankAccount
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CashManagementApi(configuration);

let id: number; // (default to undefined)
let patchedBankAccount: PatchedBankAccount; // (optional)

const { status, data } = await apiInstance.caApiAccountPartialUpdate(
    id,
    patchedBankAccount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedBankAccount** | **PatchedBankAccount**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**BankAccount**

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

# **caApiAccountRetrieve**
> BankAccount caApiAccountRetrieve()


### Example

```typescript
import {
    CashManagementApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CashManagementApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.caApiAccountRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**BankAccount**

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

# **caApiAccountUpdate**
> BankAccount caApiAccountUpdate(bankAccount)


### Example

```typescript
import {
    CashManagementApi,
    Configuration,
    BankAccount
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CashManagementApi(configuration);

let id: number; // (default to undefined)
let bankAccount: BankAccount; //

const { status, data } = await apiInstance.caApiAccountUpdate(
    id,
    bankAccount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bankAccount** | **BankAccount**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**BankAccount**

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

# **caApiTransactionDestroy**
> caApiTransactionDestroy()


### Example

```typescript
import {
    CashManagementApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CashManagementApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.caApiTransactionDestroy(
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

# **caApiTransactionPartialUpdate**
> BankTransaction caApiTransactionPartialUpdate()


### Example

```typescript
import {
    CashManagementApi,
    Configuration,
    PatchedBankTransaction
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CashManagementApi(configuration);

let id: number; // (default to undefined)
let patchedBankTransaction: PatchedBankTransaction; // (optional)

const { status, data } = await apiInstance.caApiTransactionPartialUpdate(
    id,
    patchedBankTransaction
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedBankTransaction** | **PatchedBankTransaction**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**BankTransaction**

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

# **caApiTransactionRetrieve**
> BankTransaction caApiTransactionRetrieve()


### Example

```typescript
import {
    CashManagementApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CashManagementApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.caApiTransactionRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**BankTransaction**

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

# **caApiTransactionUpdate**
> BankTransaction caApiTransactionUpdate(bankTransaction)


### Example

```typescript
import {
    CashManagementApi,
    Configuration,
    BankTransaction
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CashManagementApi(configuration);

let id: number; // (default to undefined)
let bankTransaction: BankTransaction; //

const { status, data } = await apiInstance.caApiTransactionUpdate(
    id,
    bankTransaction
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bankTransaction** | **BankTransaction**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**BankTransaction**

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

# **createAccount**
> BankAccount createAccount(bankAccount)

Create a new bank account

### Example

```typescript
import {
    CashManagementApi,
    Configuration,
    BankAccount
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CashManagementApi(configuration);

let bankAccount: BankAccount; //

const { status, data } = await apiInstance.createAccount(
    bankAccount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bankAccount** | **BankAccount**|  | |


### Return type

**BankAccount**

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

# **createBankTransaction**
> BankTransaction createBankTransaction(bankTransaction)

Create a new bank transaction

### Example

```typescript
import {
    CashManagementApi,
    Configuration,
    BankTransaction
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CashManagementApi(configuration);

let bankTransaction: BankTransaction; //

const { status, data } = await apiInstance.createBankTransaction(
    bankTransaction
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bankTransaction** | **BankTransaction**|  | |


### Return type

**BankTransaction**

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

# **listAccounts**
> PaginatedBankAccountList listAccounts()

         Retrieve a paginated list of bank accounts.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, deleted records will have is_deleted=true         and include deletion metadata (deleted_at timestamp).          Supports sorting by all returned fields:         - name, -name (account name)         - nickname, -nickname (account nickname)         - type, -type (account type)         - status, -status (account status)         - currency, -currency (account currency)         - external_account_id, -external_account_id (external account ID)         - institution_id, -institution_id (institution ID)         - source, -source (account source)         - current_balance, -current_balance (current balance)         - available_balance, -available_balance (available balance)         - created_at, -created_at (creation date)         - last_modified_at, -last_modified_at (last modified date)         - account_type, -account_type (chart account type)         - account_subtype, -account_subtype (chart account subtype)         - account_cashflow_classification, -account_cashflow_classification (cashflow classification)         - type_name, -type_name (human-readable account type)         - subtype_name, -subtype_name (human-readable account subtype)         - cashflow_classification_name, -cashflow_classification_name (human-readable cashflow classification)         - entity_name, -entity_name (entity name)         - department, -department (department name)         - id, -id (account ID)         - account_id, -account_id (UUID account ID)         

### Example

```typescript
import {
    CashManagementApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CashManagementApi(configuration);

let chartOfAccountsAccount: number; //Filter bank accounts by their linked chart of accounts account ID (optional) (default to undefined)
let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listAccounts(
    chartOfAccountsAccount,
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
| **chartOfAccountsAccount** | [**number**] | Filter bank accounts by their linked chart of accounts account ID | (optional) defaults to undefined|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedBankAccountList**

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

# **listBankTransactions**
> PaginatedBankTransactionList listBankTransactions()

         Retrieve a paginated list of bank transactions with optional filtering.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, deleted records will have is_deleted=true         and include deletion metadata (deleted_at timestamp).         

### Example

```typescript
import {
    CashManagementApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CashManagementApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listBankTransactions(
    includeDeleted,
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedBankTransactionList**

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


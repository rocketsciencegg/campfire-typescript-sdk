# CoreAccountingApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**coaApiBudgetsAccountsCreate**](#coaapibudgetsaccountscreate) | **POST** /coa/api/budgets/{budget_pk}/accounts | Create Budget|
|[**coaApiBudgetsAccountsDestroy**](#coaapibudgetsaccountsdestroy) | **DELETE** /coa/api/budgets/{budget_pk}/accounts/{id} | Delete Budget Account|
|[**coaApiBudgetsAccountsList**](#coaapibudgetsaccountslist) | **GET** /coa/api/budgets/{budget_pk}/accounts | List Budget Accounts|
|[**coaApiBudgetsAccountsPartialUpdate**](#coaapibudgetsaccountspartialupdate) | **PATCH** /coa/api/budgets/{budget_pk}/accounts/{id} | Partial Update Budget Account|
|[**coaApiBudgetsAccountsRetrieve**](#coaapibudgetsaccountsretrieve) | **GET** /coa/api/budgets/{budget_pk}/accounts/{id} | Retrieve Budget Account|
|[**coaApiBudgetsAccountsUpdate**](#coaapibudgetsaccountsupdate) | **PUT** /coa/api/budgets/{budget_pk}/accounts/{id} | Update Budget Account|
|[**coaApiBudgetsCreate**](#coaapibudgetscreate) | **POST** /coa/api/budgets | Create Budget|
|[**coaApiBudgetsDestroy**](#coaapibudgetsdestroy) | **DELETE** /coa/api/budgets/{id} | Delete Budget|
|[**coaApiBudgetsList**](#coaapibudgetslist) | **GET** /coa/api/budgets | List Budgets|
|[**coaApiBudgetsPartialUpdate**](#coaapibudgetspartialupdate) | **PATCH** /coa/api/budgets/{id} | Partial Update Budget|
|[**coaApiBudgetsRetrieve**](#coaapibudgetsretrieve) | **GET** /coa/api/budgets/{id} | Retrieve Budget|
|[**coaApiBudgetsUpdate**](#coaapibudgetsupdate) | **PUT** /coa/api/budgets/{id} | Update Budget|
|[**coaApiDepartmentBulkSearchCreate**](#coaapidepartmentbulksearchcreate) | **POST** /coa/api/department/bulk-search | Bulk Search Departments by Name|
|[**coaApiFixedAssetCreate**](#coaapifixedassetcreate) | **POST** /coa/api/fixed-asset | Create Fixed Asset|
|[**coaApiFixedAssetDestroy**](#coaapifixedassetdestroy) | **DELETE** /coa/api/fixed-asset/{id} | Delete Fixed Asset|
|[**coaApiFixedAssetList**](#coaapifixedassetlist) | **GET** /coa/api/fixed-asset | List Fixed Assets|
|[**coaApiFixedAssetPartialUpdate**](#coaapifixedassetpartialupdate) | **PATCH** /coa/api/fixed-asset/{id} | Partial Update Fixed Asset|
|[**coaApiFixedAssetRetrieve**](#coaapifixedassetretrieve) | **GET** /coa/api/fixed-asset/{id} | Retrieve Fixed Asset|
|[**coaApiFixedAssetUpdate**](#coaapifixedassetupdate) | **PUT** /coa/api/fixed-asset/{id} | Update Fixed Asset|
|[**coaApiIntercompanyJournalEntryCreate**](#coaapiintercompanyjournalentrycreate) | **POST** /coa/api/intercompany-journal-entry | Create Intercompany Journal Entry|
|[**coaApiIntercompanyJournalEntryDestroy**](#coaapiintercompanyjournalentrydestroy) | **DELETE** /coa/api/intercompany-journal-entry/{id} | Delete Intercompany Journal Entry|
|[**coaApiIntercompanyJournalEntryList**](#coaapiintercompanyjournalentrylist) | **GET** /coa/api/intercompany-journal-entry | List Intercompany Journal Entries|
|[**coaApiIntercompanyJournalEntryPartialUpdate**](#coaapiintercompanyjournalentrypartialupdate) | **PATCH** /coa/api/intercompany-journal-entry/{id} | Partial Update Intercompany Journal Entry|
|[**coaApiIntercompanyJournalEntryRetrieve**](#coaapiintercompanyjournalentryretrieve) | **GET** /coa/api/intercompany-journal-entry/{id} | Get Intercompany Journal Entry|
|[**coaApiIntercompanyJournalEntryUpdate**](#coaapiintercompanyjournalentryupdate) | **PUT** /coa/api/intercompany-journal-entry/{id} | Update Intercompany Journal Entry|
|[**coaApiJournalEntryCreate**](#coaapijournalentrycreate) | **POST** /coa/api/journal_entry | Create Journal Entry|
|[**coaApiJournalEntryDestroy**](#coaapijournalentrydestroy) | **DELETE** /coa/api/journal_entry/{id} | Delete Journal Entry|
|[**coaApiJournalEntryList**](#coaapijournalentrylist) | **GET** /coa/api/journal_entry | List Journal Entries|
|[**coaApiJournalEntryPartialUpdate**](#coaapijournalentrypartialupdate) | **PATCH** /coa/api/journal_entry/{id} | Partial Update Journal Entry|
|[**coaApiJournalEntryRetrieve**](#coaapijournalentryretrieve) | **GET** /coa/api/journal_entry/{id} | Retrieve Journal Entry|
|[**coaApiJournalEntryUpdate**](#coaapijournalentryupdate) | **PUT** /coa/api/journal_entry/{id} | Update Journal Entry|
|[**coaApiTagBulkSearchCreate**](#coaapitagbulksearchcreate) | **POST** /coa/api/tag/bulk-search | Bulk Search Custom Dimensions by Name|
|[**coaApiTransactionBillPaymentsCreate**](#coaapitransactionbillpaymentscreate) | **POST** /coa/api/transaction/{transaction_id}/bill_payments | Apply Bill Payments to Transaction|
|[**coaApiTransactionCreditMemoPaymentsCreate**](#coaapitransactioncreditmemopaymentscreate) | **POST** /coa/api/transaction/{transaction_id}/credit_memo_payments | Apply Credit Memo Payments to Transaction|
|[**coaApiTransactionDebitMemoPaymentsCreate**](#coaapitransactiondebitmemopaymentscreate) | **POST** /coa/api/transaction/{transaction_id}/debit_memo_payments | Apply Debit Memo Payments to Transaction|
|[**coaApiTransactionDestroy**](#coaapitransactiondestroy) | **DELETE** /coa/api/transaction/{id} | Delete Chart Transaction|
|[**coaApiTransactionInvoicePaymentsCreate**](#coaapitransactioninvoicepaymentscreate) | **POST** /coa/api/transaction/{transaction_id}/invoice_payments | Apply Invoice Payments to Transaction|
|[**coaApiTransactionPartialUpdate**](#coaapitransactionpartialupdate) | **PATCH** /coa/api/transaction/{id} | Partial Update Chart Transaction|
|[**coaApiTransactionRetrieve**](#coaapitransactionretrieve) | **GET** /coa/api/transaction | List Chart Transactions|
|[**coaApiTransactionRetrieve2**](#coaapitransactionretrieve2) | **GET** /coa/api/transaction/{id} | Retrieve Chart Transaction|
|[**coaApiTransactionUpdate**](#coaapitransactionupdate) | **PUT** /coa/api/transaction/{id} | Update Chart Transaction|
|[**coaApiVendorBulkSearchCreate**](#coaapivendorbulksearchcreate) | **POST** /coa/api/vendor/bulk-search | Bulk Search Vendors by External ID or Name|
|[**coaApiVendorContactsCreate**](#coaapivendorcontactscreate) | **POST** /coa/api/vendor/{id}/contacts | Create Vendor Contact|
|[**coaApiVendorContactsList**](#coaapivendorcontactslist) | **GET** /coa/api/vendor/{id}/contacts | List Vendor Contacts|

# **coaApiBudgetsAccountsCreate**
> BudgetAccount coaApiBudgetsAccountsCreate()

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    BudgetAccount
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let budgetPk: number; // (default to undefined)
let budgetAccount: BudgetAccount; // (optional)

const { status, data } = await apiInstance.coaApiBudgetsAccountsCreate(
    budgetPk,
    budgetAccount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **budgetAccount** | **BudgetAccount**|  | |
| **budgetPk** | [**number**] |  | defaults to undefined|


### Return type

**BudgetAccount**

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

# **coaApiBudgetsAccountsDestroy**
> coaApiBudgetsAccountsDestroy()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let budgetPk: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiBudgetsAccountsDestroy(
    budgetPk,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **budgetPk** | [**number**] |  | defaults to undefined|
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

# **coaApiBudgetsAccountsList**
> Array<BudgetAccount> coaApiBudgetsAccountsList()

         Retrieve a list of budget accounts with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let budgetPk: number; // (default to undefined)
let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiBudgetsAccountsList(
    budgetPk,
    includeDeleted,
    lastModifiedAtGte,
    lastModifiedAtLte
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **budgetPk** | [**number**] |  | defaults to undefined|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|


### Return type

**Array<BudgetAccount>**

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

# **coaApiBudgetsAccountsPartialUpdate**
> BudgetAccount coaApiBudgetsAccountsPartialUpdate()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    PatchedBudgetAccount
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let budgetPk: number; // (default to undefined)
let id: number; // (default to undefined)
let patchedBudgetAccount: PatchedBudgetAccount; // (optional)

const { status, data } = await apiInstance.coaApiBudgetsAccountsPartialUpdate(
    budgetPk,
    id,
    patchedBudgetAccount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedBudgetAccount** | **PatchedBudgetAccount**|  | |
| **budgetPk** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**BudgetAccount**

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

# **coaApiBudgetsAccountsRetrieve**
> BudgetAccount coaApiBudgetsAccountsRetrieve()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let budgetPk: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiBudgetsAccountsRetrieve(
    budgetPk,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **budgetPk** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**BudgetAccount**

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

# **coaApiBudgetsAccountsUpdate**
> BudgetAccount coaApiBudgetsAccountsUpdate()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    BudgetAccount
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let budgetPk: number; // (default to undefined)
let id: number; // (default to undefined)
let budgetAccount: BudgetAccount; // (optional)

const { status, data } = await apiInstance.coaApiBudgetsAccountsUpdate(
    budgetPk,
    id,
    budgetAccount
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **budgetAccount** | **BudgetAccount**|  | |
| **budgetPk** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**BudgetAccount**

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

# **coaApiBudgetsCreate**
> Budget coaApiBudgetsCreate(budget)

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    Budget
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let budget: Budget; //

const { status, data } = await apiInstance.coaApiBudgetsCreate(
    budget
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **budget** | **Budget**|  | |


### Return type

**Budget**

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

# **coaApiBudgetsDestroy**
> coaApiBudgetsDestroy()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiBudgetsDestroy(
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

# **coaApiBudgetsList**
> PaginatedBudgetList coaApiBudgetsList()

         Retrieve a list of budgets with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let entity: number; //Filter by entity ID (optional) (default to undefined)
let entityName: string; //Filter by entity name (partial match) (optional) (default to undefined)
let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let q: string; //Search query - searches by budget name (optional) (default to undefined)
let sort: string; //Sort order. Use field name for ascending, -field for descending. Supports multiple fields separated by comma. Default: name (optional) (default to 'name')

const { status, data } = await apiInstance.coaApiBudgetsList(
    entity,
    entityName,
    includeDeleted,
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
| **entity** | [**number**] | Filter by entity ID | (optional) defaults to undefined|
| **entityName** | [**string**] | Filter by entity name (partial match) | (optional) defaults to undefined|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **q** | [**string**] | Search query - searches by budget name | (optional) defaults to undefined|
| **sort** | [**string**] | Sort order. Use field name for ascending, -field for descending. Supports multiple fields separated by comma. Default: name | (optional) defaults to 'name'|


### Return type

**PaginatedBudgetList**

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

# **coaApiBudgetsPartialUpdate**
> Budget coaApiBudgetsPartialUpdate()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    PatchedBudget
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let patchedBudget: PatchedBudget; // (optional)

const { status, data } = await apiInstance.coaApiBudgetsPartialUpdate(
    id,
    patchedBudget
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedBudget** | **PatchedBudget**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Budget**

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

# **coaApiBudgetsRetrieve**
> Budget coaApiBudgetsRetrieve()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiBudgetsRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Budget**

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

# **coaApiBudgetsUpdate**
> Budget coaApiBudgetsUpdate(budget)


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    Budget
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let budget: Budget; //

const { status, data } = await apiInstance.coaApiBudgetsUpdate(
    id,
    budget
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **budget** | **Budget**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Budget**

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

# **coaApiDepartmentBulkSearchCreate**
> Array<Department> coaApiDepartmentBulkSearchCreate(bulkDepartmentSearch)

Search for thousands of departments by exact name match in a single request. Optimized for performance. Supports upsert to create missing departments.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    BulkDepartmentSearch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let bulkDepartmentSearch: BulkDepartmentSearch; //

const { status, data } = await apiInstance.coaApiDepartmentBulkSearchCreate(
    bulkDepartmentSearch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulkDepartmentSearch** | **BulkDepartmentSearch**|  | |


### Return type

**Array<Department>**

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

# **coaApiFixedAssetCreate**
> FixedAsset coaApiFixedAssetCreate(fixedAsset)

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    FixedAsset
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let fixedAsset: FixedAsset; //

const { status, data } = await apiInstance.coaApiFixedAssetCreate(
    fixedAsset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **fixedAsset** | **FixedAsset**|  | |


### Return type

**FixedAsset**

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

# **coaApiFixedAssetDestroy**
> coaApiFixedAssetDestroy()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiFixedAssetDestroy(
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

# **coaApiFixedAssetList**
> PaginatedFixedAssetList coaApiFixedAssetList()

         Retrieve a list of fixed assets with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiFixedAssetList(
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

**PaginatedFixedAssetList**

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

# **coaApiFixedAssetPartialUpdate**
> FixedAsset coaApiFixedAssetPartialUpdate()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    PatchedFixedAsset
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let patchedFixedAsset: PatchedFixedAsset; // (optional)

const { status, data } = await apiInstance.coaApiFixedAssetPartialUpdate(
    id,
    patchedFixedAsset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedFixedAsset** | **PatchedFixedAsset**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**FixedAsset**

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

# **coaApiFixedAssetRetrieve**
> FixedAsset coaApiFixedAssetRetrieve()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiFixedAssetRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**FixedAsset**

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

# **coaApiFixedAssetUpdate**
> FixedAsset coaApiFixedAssetUpdate(fixedAsset)


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    FixedAsset
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let fixedAsset: FixedAsset; //

const { status, data } = await apiInstance.coaApiFixedAssetUpdate(
    id,
    fixedAsset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **fixedAsset** | **FixedAsset**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**FixedAsset**

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

# **coaApiIntercompanyJournalEntryCreate**
> IntercompanyJournalEntry coaApiIntercompanyJournalEntryCreate()

         Creates a new intercompany journal entry          This endpoint allows for complex multi-entity transactions where:         - Transactions are balanced across different entities         - Exchange rates are handled for multi-currency transactions          Key requirements:         - Total debits must equal total credits for each entity (debit_amount_native must equal credit_amount_native)         - Cannot create entries before closed book dates         - All referenced accounts must be active         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    IntercompanyJournalEntry
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let intercompanyJournalEntry: IntercompanyJournalEntry; // (optional)

const { status, data } = await apiInstance.coaApiIntercompanyJournalEntryCreate(
    intercompanyJournalEntry
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **intercompanyJournalEntry** | **IntercompanyJournalEntry**|  | |


### Return type

**IntercompanyJournalEntry**

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

# **coaApiIntercompanyJournalEntryDestroy**
> coaApiIntercompanyJournalEntryDestroy()

         Permanently deletes an intercompany journal entry and all related transactions.          This endpoint performs a comprehensive cleanup when deleting an intercompany journal entry:         - Validates that the entry can be deleted (not in closed period)         - Removes all associated journal entries across entities         - Updates summary tables and account balances         - Handles cascade deletion of related transactions         - Ensures data integrity across the accounting system          Deletion restrictions:         - Cannot delete entries in closed accounting periods          Error conditions:         - 400 Bad Request: Entry date is in a closed period         - 409 Conflict: Entry has protected relationships (e.g., close checklist tasks)         - 404 Not Found: Entry does not exist or user lacks access          On successful deletion, all related journal entries are removed and accounting summaries are recalculated.         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiIntercompanyJournalEntryDestroy(
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

# **coaApiIntercompanyJournalEntryList**
> PaginatedIntercompanyJournalEntryList coaApiIntercompanyJournalEntryList()

         Retrieves a paginated list of intercompany journal entries for the authenticated user\'s customer.          This endpoint returns:         - Summary information for each intercompany journal entry         - Basic transaction details (simplified view for list performance)         - Entity and exchange rate information         - Pagination metadata (count, next, previous)         - Reversal relationships and attachment counts          The response includes:         - Intercompany journal entry metadata         - Associated transaction summaries         - Entity exchange rate information         - Links to related reversals         - Attachment information          Results can be sorted using the \'sort\' query parameter with field names like \'date\', \'id\', etc.         Prefix with \'-\' for descending order (e.g., \'-date\').         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiIntercompanyJournalEntryList(
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

**PaginatedIntercompanyJournalEntryList**

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

# **coaApiIntercompanyJournalEntryPartialUpdate**
> IntercompanyJournalEntry coaApiIntercompanyJournalEntryPartialUpdate()

         Performs a partial update of an intercompany journal entry, allowing modification of specific fields without replacing the entire entry.          This endpoint supports partial updates to:         - Journal entry metadata (memo, date, currency, reference number)         - Individual transaction modifications         - Entity exchange rate adjustments         - Vendor, department, and tag assignments         - Account categorizations and amounts          Key differences from PUT:         - Only specified fields are updated (vs. full replacement)         - Maintains existing data for unspecified fields         - Supports granular transaction modifications         - Preserves audit trail and timestamps         - Allows incremental changes without full transaction rebuilds          Validation requirements:         - Modified transactions must maintain entity balance (debits = credits)         - Cannot modify entries in closed accounting periods         - All referenced accounts, vendors, departments must be active         - Exchange rates must be valid for multi-currency transactions         - Account assignments must be appropriate for transaction types         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    PatchedIntercompanyJournalEntry
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let patchedIntercompanyJournalEntry: PatchedIntercompanyJournalEntry; // (optional)

const { status, data } = await apiInstance.coaApiIntercompanyJournalEntryPartialUpdate(
    id,
    patchedIntercompanyJournalEntry
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedIntercompanyJournalEntry** | **PatchedIntercompanyJournalEntry**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**IntercompanyJournalEntry**

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

# **coaApiIntercompanyJournalEntryRetrieve**
> IntercompanyJournalEntry coaApiIntercompanyJournalEntryRetrieve()

         Retrieves a single intercompany journal entry by its ID with complete details.          This endpoint returns:         - Complete intercompany journal entry information         - Full transaction details with all accounting fields         - Entity information and exchange rates         - Attachment and reversal information         - Comprehensive transaction metadata          The response includes:         - All transaction details with account information         - Entity exchange rate data         - Vendor, department, and tag information         - Balance calculations and transaction history         - File attachments and reversal relationships         - Complete audit trail information          This is the detailed view used for editing and complete transaction analysis.         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiIntercompanyJournalEntryRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**IntercompanyJournalEntry**

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

# **coaApiIntercompanyJournalEntryUpdate**
> IntercompanyJournalEntry coaApiIntercompanyJournalEntryUpdate()

         Updates an existing intercompany journal entry with new transaction details.          This endpoint allows for:         - Modifying transaction amounts and details         - Updating entity assignments and exchange rates         - Changing account assignments and categorizations         - Updating vendor, department, and tag information         - Maintaining balance validation across all entities          Key requirements:         - Total debits must equal total credits for each entity         - All account balances must be valid in all currencies         - Cannot modify entries in closed periods         - All referenced accounts must be active         - Existing transactions are replaced with new transaction set          The update process atomically replaces all transactions while preserving the journal entry ID and audit trail.         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    IntercompanyJournalEntry
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let intercompanyJournalEntry: IntercompanyJournalEntry; // (optional)

const { status, data } = await apiInstance.coaApiIntercompanyJournalEntryUpdate(
    id,
    intercompanyJournalEntry
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **intercompanyJournalEntry** | **IntercompanyJournalEntry**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**IntercompanyJournalEntry**

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

# **coaApiJournalEntryCreate**
> JournalEntryPostResponse coaApiJournalEntryCreate()

         Create a new journal entry with transactions. Journal entries must balance - total debits must equal total credits.          **Key Features:**         - Automatic currency conversion using exchange rates         - Vendor, Department and Custom Dimension assignment         - Optional reversal date for automatic reversal entries         - Validation against closed book periods          **Validation Rules:**         - Debits must equal credits in transaction currency (debit_native and credit_native)         - Cannot create entries before closed book dates         - Accounts must be active         - Exchange rates are auto-calculated if not provided         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    JournalEntryPostResponse
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let journalEntryPostResponse: JournalEntryPostResponse; // (optional)

const { status, data } = await apiInstance.coaApiJournalEntryCreate(
    journalEntryPostResponse
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **journalEntryPostResponse** | **JournalEntryPostResponse**|  | |


### Return type

**JournalEntryPostResponse**

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

# **coaApiJournalEntryDestroy**
> coaApiJournalEntryDestroy()

         Delete a journal entry and all its associated transactions.          **Restrictions:**         - Cannot delete entries before closed book dates          **Response Codes:**         - 204: Successfully deleted         - 400: Cannot delete (books closed for this date)         - 409: Cannot delete (associated with other objects)         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiJournalEntryDestroy(
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
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |
|**400** | Bad request |  -  |
|**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiJournalEntryList**
> PaginatedJournalEntryList coaApiJournalEntryList()

         Retrieve a paginated list of journal entries with optional filtering and sorting.          **Query Parameters:**         - `start_date`, `end_date`: Filter by date range (defaults to last 6 months)         - `account`: Filter by account ID(s) - supports multiple values         - `source`: Filter by journal entry source         - `journal_id`: Filter by specific journal ID         - `all_time`: Include all entries regardless of date (true/false)         - `sort`: Sort field (default: \"date\")          **Response includes:**         - Complete journal entry details with all transactions         - Account information with names and numbers         - Vendor and department details         - Tag associations with groups         - Attachment information         - Exchange rate data for multi-currency entries         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let account: string; //Filter by account ID(s). Can specify multiple values. (optional) (default to undefined)
let allTime: boolean; //Include all entries regardless of date range (optional) (default to false)
let endDate: string; //End date for filtering (YYYY-MM-DD format) (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let source: string; //Filter by journal entry source (e.g., \'manual\', \'CSV Upload\') (optional) (default to undefined)
let startDate: string; //Start date for filtering (YYYY-MM-DD format) (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiJournalEntryList(
    account,
    allTime,
    endDate,
    limit,
    offset,
    source,
    startDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **account** | [**string**] | Filter by account ID(s). Can specify multiple values. | (optional) defaults to undefined|
| **allTime** | [**boolean**] | Include all entries regardless of date range | (optional) defaults to false|
| **endDate** | [**string**] | End date for filtering (YYYY-MM-DD format) | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **source** | [**string**] | Filter by journal entry source (e.g., \&#39;manual\&#39;, \&#39;CSV Upload\&#39;) | (optional) defaults to undefined|
| **startDate** | [**string**] | Start date for filtering (YYYY-MM-DD format) | (optional) defaults to undefined|


### Return type

**PaginatedJournalEntryList**

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

# **coaApiJournalEntryPartialUpdate**
> JournalEntryPostResponse coaApiJournalEntryPartialUpdate()

         Partially update a journal entry. Only provided fields will be updated.          **Common Use Cases:**         - Update memo or reference number         - Change journal entry date         - Modify specific transaction amounts         - Add or remove tags from transactions          **Validation Rules:**         - Journal entry must still balance after updates         - Cannot modify entries in closed periods         - Account changes must maintain chart of accounts rules         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    PatchedJournalEntryPostResponse
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let patchedJournalEntryPostResponse: PatchedJournalEntryPostResponse; // (optional)

const { status, data } = await apiInstance.coaApiJournalEntryPartialUpdate(
    id,
    patchedJournalEntryPostResponse
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedJournalEntryPostResponse** | **PatchedJournalEntryPostResponse**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**JournalEntryPostResponse**

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

# **coaApiJournalEntryRetrieve**
> JournalEntry coaApiJournalEntryRetrieve()

         Retrieve a specific journal entry by ID with all transaction details.          **Response includes:**         - Complete journal entry with all transactions         - Account names, numbers, and types         - Vendor and department information         - Tag associations with groups         - Exchange rate data for multi-currency entries         - Attachment information         - Reversal information if applicable         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiJournalEntryRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**JournalEntry**

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

# **coaApiJournalEntryUpdate**
> JournalEntryPostResponse coaApiJournalEntryUpdate()

         Update a journal entry completely. All transactions will be replaced with the new ones provided.          **Important Notes:**         - Cannot update entries before closed book dates         - Must maintain double-entry bookkeeping (debits = credits)         - All existing transactions will be replaced         - Exchange rates will be recalculated if not provided          **Validation Rules:**         - Journal entry must balance in all currencies         - Accounts must be active         - Cannot modify entries in closed periods         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    JournalEntryPostResponse
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let journalEntryPostResponse: JournalEntryPostResponse; // (optional)

const { status, data } = await apiInstance.coaApiJournalEntryUpdate(
    id,
    journalEntryPostResponse
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **journalEntryPostResponse** | **JournalEntryPostResponse**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**JournalEntryPostResponse**

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

# **coaApiTagBulkSearchCreate**
> Array<TransactionTag> coaApiTagBulkSearchCreate(bulkTagSearch)

Search for tags by exact name match in a single request. Supports upsert to create missing tags.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    BulkTagSearch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let bulkTagSearch: BulkTagSearch; //

const { status, data } = await apiInstance.coaApiTagBulkSearchCreate(
    bulkTagSearch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulkTagSearch** | **BulkTagSearch**|  | |


### Return type

**Array<TransactionTag>**

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

# **coaApiTransactionBillPaymentsCreate**
> coaApiTransactionBillPaymentsCreate()

Apply bill payments to a bank transaction, linking the transaction to one or more bills.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let transactionId: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionBillPaymentsCreate(
    transactionId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transactionId** | [**number**] |  | defaults to undefined|


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
|**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTransactionCreditMemoPaymentsCreate**
> coaApiTransactionCreditMemoPaymentsCreate()

Apply credit memo payments to a bank transaction.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let transactionId: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionCreditMemoPaymentsCreate(
    transactionId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transactionId** | [**number**] |  | defaults to undefined|


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
|**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTransactionDebitMemoPaymentsCreate**
> coaApiTransactionDebitMemoPaymentsCreate()

Apply debit memo payments to a bank transaction.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let transactionId: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionDebitMemoPaymentsCreate(
    transactionId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transactionId** | [**number**] |  | defaults to undefined|


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
|**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTransactionDestroy**
> coaApiTransactionDestroy()

Delete a chart transaction. Cannot delete transactions in closed accounting periods.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionDestroy(
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

# **coaApiTransactionInvoicePaymentsCreate**
> coaApiTransactionInvoicePaymentsCreate()

Apply invoice payments to a bank transaction, linking the transaction to one or more invoices.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let transactionId: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionInvoicePaymentsCreate(
    transactionId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transactionId** | [**number**] |  | defaults to undefined|


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
|**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTransactionPartialUpdate**
> ChartTransaction coaApiTransactionPartialUpdate()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    PatchedChartTransaction
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let patchedChartTransaction: PatchedChartTransaction; // (optional)

const { status, data } = await apiInstance.coaApiTransactionPartialUpdate(
    id,
    patchedChartTransaction
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedChartTransaction** | **PatchedChartTransaction**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ChartTransaction**

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

# **coaApiTransactionRetrieve**
> coaApiTransactionRetrieve()

Retrieve chart transactions with advanced filtering options

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

const { status, data } = await apiInstance.coaApiTransactionRetrieve();
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

# **coaApiTransactionRetrieve2**
> ChartTransaction coaApiTransactionRetrieve2()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionRetrieve2(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ChartTransaction**

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

# **coaApiTransactionUpdate**
> ChartTransaction coaApiTransactionUpdate(chartTransaction)


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    ChartTransaction
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let chartTransaction: ChartTransaction; //

const { status, data } = await apiInstance.coaApiTransactionUpdate(
    id,
    chartTransaction
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **chartTransaction** | **ChartTransaction**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ChartTransaction**

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

# **coaApiVendorBulkSearchCreate**
> Array<Vendor> coaApiVendorBulkSearchCreate(bulkVendorSearch)

Search for thousands of vendors by external_id (priority) or name in a single request. Optimized for performance. Supports upsert to create missing vendors.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    BulkVendorSearch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let bulkVendorSearch: BulkVendorSearch; //

const { status, data } = await apiInstance.coaApiVendorBulkSearchCreate(
    bulkVendorSearch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulkVendorSearch** | **BulkVendorSearch**|  | |


### Return type

**Array<Vendor>**

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

# **coaApiVendorContactsCreate**
> VendorContact coaApiVendorContactsCreate()

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    VendorContact
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let vendorContact: VendorContact; // (optional)

const { status, data } = await apiInstance.coaApiVendorContactsCreate(
    id,
    vendorContact
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **vendorContact** | **VendorContact**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**VendorContact**

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

# **coaApiVendorContactsList**
> PaginatedVendorContactList coaApiVendorContactsList()

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiVendorContactsList(
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

**PaginatedVendorContactList**

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


# AccountsPayableApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**coaApiV1BillBulkSearchCreate**](#coaapiv1billbulksearchcreate) | **POST** /coa/api/v1/bill/bulk-search | Bulk Search Bills by Number|
|[**coaApiV1BillBulkSyncToRampCreate**](#coaapiv1billbulksynctorampcreate) | **POST** /coa/api/v1/bill/bulk-sync-to-ramp/ | |
|[**coaApiV1BillCreate**](#coaapiv1billcreate) | **POST** /coa/api/v1/bill/ | Create Accounting Bill|
|[**coaApiV1BillDestroy**](#coaapiv1billdestroy) | **DELETE** /coa/api/v1/bill/{id}/ | Delete Accounting Bill|
|[**coaApiV1BillEmptyTransactionDefaultDepartmentTagsRetrieve**](#coaapiv1billemptytransactiondefaultdepartmenttagsretrieve) | **GET** /coa/api/v1/bill/{bill_id}/empty-transaction-default-department-tags | Get Default Department and Tags for Empty Transaction|
|[**coaApiV1BillPartialUpdate**](#coaapiv1billpartialupdate) | **PATCH** /coa/api/v1/bill/{id}/ | Partial Update Accounting Bill|
|[**coaApiV1BillPayCreate**](#coaapiv1billpaycreate) | **POST** /coa/api/v1/bill/{bill_id}/pay/ | Mark Bill as Paid|
|[**coaApiV1BillPaymentVoidCreate**](#coaapiv1billpaymentvoidcreate) | **POST** /coa/api/v1/bill/{bill_id}/payment/{payment_id}/void/ | Void Bill Payment|
|[**coaApiV1BillPaymentVoidDestroy**](#coaapiv1billpaymentvoiddestroy) | **DELETE** /coa/api/v1/bill/{bill_id}/payment/{payment_id}/void/ | Delete Bill Payment|
|[**coaApiV1BillReopenCreate**](#coaapiv1billreopencreate) | **POST** /coa/api/v1/bill/{bill_id}/reopen/ | Reopen Voided Bill|
|[**coaApiV1BillRetrieve**](#coaapiv1billretrieve) | **GET** /coa/api/v1/bill/ | List Accounting Bills|
|[**coaApiV1BillRetrieve2**](#coaapiv1billretrieve2) | **GET** /coa/api/v1/bill/{id}/ | Retrieve Accounting Bill|
|[**coaApiV1BillSyncToRampCreate**](#coaapiv1billsynctorampcreate) | **POST** /coa/api/v1/bill/{bill_id}/sync-to-ramp/ | Sync Bill to Ramp|
|[**coaApiV1BillUpdate**](#coaapiv1billupdate) | **PUT** /coa/api/v1/bill/{id}/ | Update Accounting Bill|
|[**coaApiV1BillVoidCreate**](#coaapiv1billvoidcreate) | **POST** /coa/api/v1/bill/{bill_id}/void/ | Void Bill|
|[**coaApiV1DebitMemoBulkSearchCreate**](#coaapiv1debitmemobulksearchcreate) | **POST** /coa/api/v1/debit-memo/bulk-search | Bulk Search Debit Memos by Number|
|[**coaApiV1DebitMemoCreate**](#coaapiv1debitmemocreate) | **POST** /coa/api/v1/debit-memo | Create Debit Memo|
|[**coaApiV1DebitMemoDestroy**](#coaapiv1debitmemodestroy) | **DELETE** /coa/api/v1/debit-memo/{id} | Delete Debit Memo|
|[**coaApiV1DebitMemoList**](#coaapiv1debitmemolist) | **GET** /coa/api/v1/debit-memo | List Debit Memos|
|[**coaApiV1DebitMemoMarkUsedCreate**](#coaapiv1debitmemomarkusedcreate) | **POST** /coa/api/v1/debit-memo/{debit_memo_id}/mark-used | Mark Debit Memo as Used|
|[**coaApiV1DebitMemoNextDebitMemoNumberRetrieve**](#coaapiv1debitmemonextdebitmemonumberretrieve) | **GET** /coa/api/v1/debit-memo/next-debit-memo-number | Get Next Debit Memo Number|
|[**coaApiV1DebitMemoPartialUpdate**](#coaapiv1debitmemopartialupdate) | **PATCH** /coa/api/v1/debit-memo/{id} | Partial Update Debit Memo|
|[**coaApiV1DebitMemoReopenCreate**](#coaapiv1debitmemoreopencreate) | **POST** /coa/api/v1/debit-memo/{debit_memo_id}/reopen/ | Reopen Voided Debit Memo|
|[**coaApiV1DebitMemoRetrieve**](#coaapiv1debitmemoretrieve) | **GET** /coa/api/v1/debit-memo/{id} | Retrieve Debit Memo|
|[**coaApiV1DebitMemoUpdate**](#coaapiv1debitmemoupdate) | **PUT** /coa/api/v1/debit-memo/{id} | Update Debit Memo|
|[**coaApiV1DebitMemoVoidCreate**](#coaapiv1debitmemovoidcreate) | **POST** /coa/api/v1/debit-memo/{debit_memo_id}/void/ | Void Debit Memo|

# **coaApiV1BillBulkSearchCreate**
> { [key: string]: any; } coaApiV1BillBulkSearchCreate(bulkBillSearch)

Search for thousands of bills by exact bill number match in a single request. Optimized for performance.

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration,
    BulkBillSearch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let bulkBillSearch: BulkBillSearch; //

const { status, data } = await apiInstance.coaApiV1BillBulkSearchCreate(
    bulkBillSearch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulkBillSearch** | **BulkBillSearch**|  | |


### Return type

**{ [key: string]: any; }**

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

# **coaApiV1BillBulkSyncToRampCreate**
> coaApiV1BillBulkSyncToRampCreate()

Sync multiple bills to Ramp

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

const { status, data } = await apiInstance.coaApiV1BillBulkSyncToRampCreate();
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

# **coaApiV1BillCreate**
> coaApiV1BillCreate()

         Creates a new accounting bill with line items and automatic journal entry generation.          This endpoint allows for complex bill creation with:         - Multiple line items with different accounts, departments, and vendor assignments         - Automatic accounts payable journal entry creation         - Tax calculations and tax account handling         - Exchange rate support for multi-currency transactions         - Custom field support for additional bill metadata          Requirements:         - All referenced accounts must exist and be active         - Vendor must exist         - Entity must exist         - Line items must have valid amounts and descriptions         - Currency must be valid for the entity         - Accounting date must be before closed book date         

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

const { status, data } = await apiInstance.coaApiV1BillCreate();
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
|**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1BillDestroy**
> coaApiV1BillDestroy()

         Permanently deletes an accounting bill and its associated journal entry.          This endpoint performs a complete deletion of the bill including:         - Removal of all bill line items and associated data         - Deletion of the corresponding accounts payable journal entry         - Cleanup of any tax calculations and allocations         - Removal of vendor payment allocations if applicable          **Important Notes:**         - This operation is irreversible and permanently removes the bill from the system         - The associated journal entry will be automatically deleted to maintain accounting integrity         - All double-entry bookkeeping records related to this bill will be removed         - Any payments allocated to this bill should be handled separately before deletion         - Deletion may affect financial reports and account balances          **Restrictions:**         - Bills with allocated payments may require payment reallocation first         - Consider the impact on historical financial reporting         - Bills cannot be deleted in a closed period         

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let id: string; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1BillDestroy(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] |  | defaults to undefined|


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

# **coaApiV1BillEmptyTransactionDefaultDepartmentTagsRetrieve**
> CoaApiV1BillEmptyTransactionDefaultDepartmentTagsRetrieve200Response coaApiV1BillEmptyTransactionDefaultDepartmentTagsRetrieve()

Get the default department and tags from the bill line with the largest total amount.          This endpoint is used to provide default values when creating empty transactions (marking as paid without a transaction).         The total amount is calculated as: amount + tax.         If multiple lines have the same total amount, the line with the lowest ID (first created) is selected.         The department and tags are retrieved directly from the bill line.

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let billId: number; //ID of the bill (default to undefined)

const { status, data } = await apiInstance.coaApiV1BillEmptyTransactionDefaultDepartmentTagsRetrieve(
    billId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **billId** | [**number**] | ID of the bill | defaults to undefined|


### Return type

**CoaApiV1BillEmptyTransactionDefaultDepartmentTagsRetrieve200Response**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |
|**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1BillPartialUpdate**
> AccountingBill coaApiV1BillPartialUpdate()

         Performs a partial update of an existing accounting bill using PATCH semantics.          This endpoint allows selective modification of bill fields without requiring         a complete bill replacement. You can update specific aspects of the bill while         leaving other fields unchanged.          **Updatable Fields:**         - Bill metadata (number, dates, descriptions, vendor, entity)         - Line items (amounts, accounts, descriptions, departments)         - Payment terms and due dates         - Tax calculations and allocations         - Custom fields and tags         - Currency and exchange rates         

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration,
    PatchedAccountingBill
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let id: string; // (default to undefined)
let patchedAccountingBill: PatchedAccountingBill; // (optional)

const { status, data } = await apiInstance.coaApiV1BillPartialUpdate(
    id,
    patchedAccountingBill
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedAccountingBill** | **PatchedAccountingBill**|  | |
| **id** | [**string**] |  | defaults to undefined|


### Return type

**AccountingBill**

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

# **coaApiV1BillPayCreate**
> AccountingBill coaApiV1BillPayCreate()

Mark a bill as paid, allowing partial payments.          This endpoint supports multiple payment methods:         - Apply existing transactions as payments         - Apply debit memos to reduce the bill balance         - Create manual payments without a transaction          The request body should contain at least one of:         - transactions: List of transaction payments to apply         - debit_memos: List of debit memos to apply         - empty_transactions: List of manual payments without transactions

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration,
    MarkPaid
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let billId: number; //ID of the bill to mark as paid (default to undefined)
let markPaid: MarkPaid; // (optional)

const { status, data } = await apiInstance.coaApiV1BillPayCreate(
    billId,
    markPaid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **markPaid** | **MarkPaid**|  | |
| **billId** | [**number**] | ID of the bill to mark as paid | defaults to undefined|


### Return type

**AccountingBill**

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

# **coaApiV1BillPaymentVoidCreate**
> AccountingBillPayment coaApiV1BillPaymentVoidCreate()

Void an existing bill payment.          This creates a reversing journal entry to void the payment and updates the bill status.          Optionally accepts a void_date in the request body to specify when the payment should be voided.         If not provided, defaults to today\'s date.

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration,
    VoidPayment
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let billId: number; //ID of the bill (default to undefined)
let paymentId: number; //ID of the payment to void (default to undefined)
let voidPayment: VoidPayment; // (optional)

const { status, data } = await apiInstance.coaApiV1BillPaymentVoidCreate(
    billId,
    paymentId,
    voidPayment
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **voidPayment** | **VoidPayment**|  | |
| **billId** | [**number**] | ID of the bill | defaults to undefined|
| **paymentId** | [**number**] | ID of the payment to void | defaults to undefined|


### Return type

**AccountingBillPayment**

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

# **coaApiV1BillPaymentVoidDestroy**
> coaApiV1BillPaymentVoidDestroy()

Delete a bill payment.          This removes the payment record and updates the transaction to uncategorized.

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let billId: number; //ID of the bill (default to undefined)
let paymentId: number; //ID of the payment to delete (default to undefined)

const { status, data } = await apiInstance.coaApiV1BillPaymentVoidDestroy(
    billId,
    paymentId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **billId** | [**number**] | ID of the bill | defaults to undefined|
| **paymentId** | [**number**] | ID of the payment to delete | defaults to undefined|


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

# **coaApiV1BillReopenCreate**
> AccountingBill coaApiV1BillReopenCreate()

Reopen a voided bill.          This removes the void date and void journal entry, and sets the bill status back to open.         The voiding journal entry will be deleted to reverse the void operation.

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let billId: number; //ID of the voided bill to reopen (default to undefined)

const { status, data } = await apiInstance.coaApiV1BillReopenCreate(
    billId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **billId** | [**number**] | ID of the voided bill to reopen | defaults to undefined|


### Return type

**AccountingBill**

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

# **coaApiV1BillRetrieve**
> coaApiV1BillRetrieve()

         Retrieve a paginated list of accounting bills with comprehensive filtering, search, and sorting capabilities.          This endpoint provides complete access to your bills data with:         - Advanced filtering by date ranges, payment status, vendors, entities, and currency         - Full-text search across bill numbers, vendor names, addresses, and bill messages         - Flexible sorting by any field including calculated fields (totals, amounts due, etc.)         - Comprehensive pagination with customizable page sizes         - Aging calculations and payment status categorization         - Automatic calculation of totals, amounts paid, and amounts due          **Deleted Records Support:**         - When include_deleted=true: Returns ONLY deleted bills with minimal data (id, is_deleted, deleted_at, last_modified_at)         - When include_deleted=false or omitted: Returns ONLY active bills with full data         - Timestamp filtering (last_modified_at__gte/lte) works with both active and deleted records         

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let currency: string; //Filter by currency code (e.g., USD, EUR) (optional) (default to undefined)
let download: boolean; //If true, triggers async download workflow and sends bills via email (optional) (default to false)
let endDate: string; //Filter bills with bill_date on or before this date (YYYY-MM-DD) (optional) (default to undefined)
let entity: number; //Filter by entity ID. Can be specified multiple times for multiple entities (optional) (default to undefined)
let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page (default: 50, max: 1000) (optional) (default to 50)
let offset: number; //The initial index from which to return the results (optional) (default to 0)
let q: string; //Search query - searches by mailing address, bill number, message on bill, or vendor name (optional) (default to undefined)
let sort: string; //Sort order. Use field name for ascending, -field for descending. Special fields: vendor_name, total_amount, amount_paid, amount_due, payment. Default: -bill_date (optional) (default to '-bill_date')
let startDate: string; //Filter bills with bill_date on or after this date (YYYY-MM-DD) (optional) (default to undefined)
let status: '1_30' | '31_60' | '61_90' | '91_120' | 'current' | 'open' | 'over_120' | 'paid' | 'partially_paid' | 'past_due' | 'payment_not_found' | 'payment_pending' | 'unpaid' | 'voided'; //Filter by payment status (optional) (default to undefined)
let vendor: number; //Filter by vendor ID. Can be specified multiple times for multiple vendors (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiV1BillRetrieve(
    currency,
    download,
    endDate,
    entity,
    includeDeleted,
    lastModifiedAtGte,
    lastModifiedAtLte,
    limit,
    offset,
    q,
    sort,
    startDate,
    status,
    vendor
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **currency** | [**string**] | Filter by currency code (e.g., USD, EUR) | (optional) defaults to undefined|
| **download** | [**boolean**] | If true, triggers async download workflow and sends bills via email | (optional) defaults to false|
| **endDate** | [**string**] | Filter bills with bill_date on or before this date (YYYY-MM-DD) | (optional) defaults to undefined|
| **entity** | [**number**] | Filter by entity ID. Can be specified multiple times for multiple entities | (optional) defaults to undefined|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page (default: 50, max: 1000) | (optional) defaults to 50|
| **offset** | [**number**] | The initial index from which to return the results | (optional) defaults to 0|
| **q** | [**string**] | Search query - searches by mailing address, bill number, message on bill, or vendor name | (optional) defaults to undefined|
| **sort** | [**string**] | Sort order. Use field name for ascending, -field for descending. Special fields: vendor_name, total_amount, amount_paid, amount_due, payment. Default: -bill_date | (optional) defaults to '-bill_date'|
| **startDate** | [**string**] | Filter bills with bill_date on or after this date (YYYY-MM-DD) | (optional) defaults to undefined|
| **status** | [**&#39;1_30&#39; | &#39;31_60&#39; | &#39;61_90&#39; | &#39;91_120&#39; | &#39;current&#39; | &#39;open&#39; | &#39;over_120&#39; | &#39;paid&#39; | &#39;partially_paid&#39; | &#39;past_due&#39; | &#39;payment_not_found&#39; | &#39;payment_pending&#39; | &#39;unpaid&#39; | &#39;voided&#39;**]**Array<&#39;1_30&#39; &#124; &#39;31_60&#39; &#124; &#39;61_90&#39; &#124; &#39;91_120&#39; &#124; &#39;current&#39; &#124; &#39;open&#39; &#124; &#39;over_120&#39; &#124; &#39;paid&#39; &#124; &#39;partially_paid&#39; &#124; &#39;past_due&#39; &#124; &#39;payment_not_found&#39; &#124; &#39;payment_pending&#39; &#124; &#39;unpaid&#39; &#124; &#39;voided&#39;>** | Filter by payment status | (optional) defaults to undefined|
| **vendor** | [**number**] | Filter by vendor ID. Can be specified multiple times for multiple vendors | (optional) defaults to undefined|


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

# **coaApiV1BillRetrieve2**
> AccountingBill coaApiV1BillRetrieve2()

         Retrieve a single accounting bill by ID with complete detail including all line items, payments, and related data.          This endpoint returns comprehensive bill information including:         - Full bill details with vendor, entity, and customer information         - All line items with account details, departments, tags, and amortization schedules         - Complete payment history with journal entry references         - Calculated fields including total amounts, amounts paid, amounts due, and payment status         - Journal entry references for accounting integration         - Exchange rate information for multi-currency bills         

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let id: string; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1BillRetrieve2(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] |  | defaults to undefined|


### Return type

**AccountingBill**

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

# **coaApiV1BillSyncToRampCreate**
> coaApiV1BillSyncToRampCreate()

Sync a bill without a source to Ramp using the enabled Ramp connection

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let billId: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1BillSyncToRampCreate(
    billId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **billId** | [**number**] |  | defaults to undefined|


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
|**400** | No response body |  -  |
|**404** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1BillUpdate**
> AccountingBill coaApiV1BillUpdate(accountingBill)

         Update an existing accounting bill with complete replacement of all data including line items and metadata.          This endpoint performs a full update (PUT) of an accounting bill with:         - Complete replacement of all bill data including vendor, entity, dates, and terms         - Full replacement of all line items with new account assignments, amounts, and descriptions         - Automatic recalculation of journal entries and accounting transactions         - Preservation of payment history while updating balances and amounts due         - Validation of all referenced accounts, vendors, entities, and departments         - Automatic exchange rate updates for multi-currency bills         - Custom field updates and attachment management         

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration,
    AccountingBill
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let id: string; // (default to undefined)
let accountingBill: AccountingBill; //

const { status, data } = await apiInstance.coaApiV1BillUpdate(
    id,
    accountingBill
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountingBill** | **AccountingBill**|  | |
| **id** | [**string**] |  | defaults to undefined|


### Return type

**AccountingBill**

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

# **coaApiV1BillVoidCreate**
> AccountingBill coaApiV1BillVoidCreate(voidBillRequest)

Void an existing bill.          This creates a reversing journal entry to void the bill by reversing all debit and credit amounts.         The bill status will be updated to reflect the void.

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration,
    VoidBillRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let billId: number; //ID of the bill to void (default to undefined)
let voidBillRequest: VoidBillRequest; //

const { status, data } = await apiInstance.coaApiV1BillVoidCreate(
    billId,
    voidBillRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **voidBillRequest** | **VoidBillRequest**|  | |
| **billId** | [**number**] | ID of the bill to void | defaults to undefined|


### Return type

**AccountingBill**

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

# **coaApiV1DebitMemoBulkSearchCreate**
> { [key: string]: any; } coaApiV1DebitMemoBulkSearchCreate(bulkDebitMemoSearch)

Search for thousands of debit memos by exact debit memo number match in a single request. Optimized for performance.

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration,
    BulkDebitMemoSearch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let bulkDebitMemoSearch: BulkDebitMemoSearch; //

const { status, data } = await apiInstance.coaApiV1DebitMemoBulkSearchCreate(
    bulkDebitMemoSearch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulkDebitMemoSearch** | **BulkDebitMemoSearch**|  | |


### Return type

**{ [key: string]: any; }**

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

# **coaApiV1DebitMemoCreate**
> AccountingDebitMemo coaApiV1DebitMemoCreate(accountingDebitMemo)

         Creates a new accounting debit memo with line items and automatic journal entry generation.          Debit memos are used to record amounts owed to vendors or to adjust vendor account balances.         This endpoint handles multi-currency transactions, departmental allocations, and automatic         double-entry bookkeeping.         

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration,
    AccountingDebitMemo
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let accountingDebitMemo: AccountingDebitMemo; //

const { status, data } = await apiInstance.coaApiV1DebitMemoCreate(
    accountingDebitMemo
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountingDebitMemo** | **AccountingDebitMemo**|  | |


### Return type

**AccountingDebitMemo**

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

# **coaApiV1DebitMemoDestroy**
> coaApiV1DebitMemoDestroy()


### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1DebitMemoDestroy(
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

# **coaApiV1DebitMemoList**
> PaginatedAccountingDebitMemoList coaApiV1DebitMemoList()

         Retrieves a paginated list of accounting debit memos with filtering and sorting capabilities.          Supports filtering by date ranges, status, vendors, entities, and full-text search.         

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiV1DebitMemoList(
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

**PaginatedAccountingDebitMemoList**

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

# **coaApiV1DebitMemoMarkUsedCreate**
> any coaApiV1DebitMemoMarkUsedCreate(markDebitMemoUsed)

Mark a debit memo as used by linking to an existing transaction.          The transaction\'s debit amount will be recategorized to A/P to clear the debit memo.         The debit memo\'s status will be updated to \"used\" or \"partially_used\" based on         the amount applied vs the total amount.

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration,
    MarkDebitMemoUsed
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let debitMemoId: number; //ID of the debit memo to mark as used (default to undefined)
let markDebitMemoUsed: MarkDebitMemoUsed; //

const { status, data } = await apiInstance.coaApiV1DebitMemoMarkUsedCreate(
    debitMemoId,
    markDebitMemoUsed
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **markDebitMemoUsed** | **MarkDebitMemoUsed**|  | |
| **debitMemoId** | [**number**] | ID of the debit memo to mark as used | defaults to undefined|


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

# **coaApiV1DebitMemoNextDebitMemoNumberRetrieve**
> coaApiV1DebitMemoNextDebitMemoNumberRetrieve()


### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

const { status, data } = await apiInstance.coaApiV1DebitMemoNextDebitMemoNumberRetrieve();
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

# **coaApiV1DebitMemoPartialUpdate**
> AccountingDebitMemo coaApiV1DebitMemoPartialUpdate()

         Performs a partial update of an existing accounting debit memo using PATCH semantics.          This endpoint allows selective modification of debit memo fields without requiring         a complete replacement.         

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration,
    PatchedAccountingDebitMemo
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let id: number; // (default to undefined)
let patchedAccountingDebitMemo: PatchedAccountingDebitMemo; // (optional)

const { status, data } = await apiInstance.coaApiV1DebitMemoPartialUpdate(
    id,
    patchedAccountingDebitMemo
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedAccountingDebitMemo** | **PatchedAccountingDebitMemo**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**AccountingDebitMemo**

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

# **coaApiV1DebitMemoReopenCreate**
> AccountingDebitMemo coaApiV1DebitMemoReopenCreate()

Reopen a voided debit memo.          This removes the void date and void journal entry, and sets the debit memo status back to open.         The voiding journal entry will be deleted to reverse the void operation.

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let debitMemoId: number; //ID of the voided debit memo to reopen (default to undefined)

const { status, data } = await apiInstance.coaApiV1DebitMemoReopenCreate(
    debitMemoId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **debitMemoId** | [**number**] | ID of the voided debit memo to reopen | defaults to undefined|


### Return type

**AccountingDebitMemo**

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

# **coaApiV1DebitMemoRetrieve**
> AccountingDebitMemo coaApiV1DebitMemoRetrieve()

         Retrieves a single accounting debit memo with complete details including line items,         payments, and accounting relationships.         

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1DebitMemoRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**AccountingDebitMemo**

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

# **coaApiV1DebitMemoUpdate**
> AccountingDebitMemo coaApiV1DebitMemoUpdate(accountingDebitMemo)

         Performs a complete update of an existing accounting debit memo using PUT semantics.          This endpoint allows full replacement of debit memo data including line items         and journal entry recalculation.         

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration,
    AccountingDebitMemo
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let id: number; // (default to undefined)
let accountingDebitMemo: AccountingDebitMemo; //

const { status, data } = await apiInstance.coaApiV1DebitMemoUpdate(
    id,
    accountingDebitMemo
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountingDebitMemo** | **AccountingDebitMemo**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**AccountingDebitMemo**

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

# **coaApiV1DebitMemoVoidCreate**
> AccountingDebitMemo coaApiV1DebitMemoVoidCreate(voidDebitMemoRequest)

Void an existing debit memo.          This creates a reversing journal entry to void the debit memo by reversing all debit and credit amounts.         The debit memo status will be updated to reflect the void.

### Example

```typescript
import {
    AccountsPayableApi,
    Configuration,
    VoidDebitMemoRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsPayableApi(configuration);

let debitMemoId: number; //ID of the debit memo to void (default to undefined)
let voidDebitMemoRequest: VoidDebitMemoRequest; //

const { status, data } = await apiInstance.coaApiV1DebitMemoVoidCreate(
    debitMemoId,
    voidDebitMemoRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **voidDebitMemoRequest** | **VoidDebitMemoRequest**|  | |
| **debitMemoId** | [**number**] | ID of the debit memo to void | defaults to undefined|


### Return type

**AccountingDebitMemo**

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


# AccountsReceivableApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**bulkCreateInvoices**](#bulkcreateinvoices) | **POST** /coa/api/v1/invoice/bulk-create | Bulk Create Invoices|
|[**coaApiV1CreditMemoBulkSearchCreate**](#coaapiv1creditmemobulksearchcreate) | **POST** /coa/api/v1/credit-memo/bulk-search | Bulk Search Credit Memos by Number|
|[**coaApiV1CreditMemoCreate**](#coaapiv1creditmemocreate) | **POST** /coa/api/v1/credit-memo | Create Credit Memo|
|[**coaApiV1CreditMemoDestroy**](#coaapiv1creditmemodestroy) | **DELETE** /coa/api/v1/credit-memo/{id} | Delete Credit Memo|
|[**coaApiV1CreditMemoList**](#coaapiv1creditmemolist) | **GET** /coa/api/v1/credit-memo | List Credit Memos|
|[**coaApiV1CreditMemoMarkUsedCreate**](#coaapiv1creditmemomarkusedcreate) | **POST** /coa/api/v1/credit-memo/{credit_memo_id}/mark-used | Mark Credit Memo as Used|
|[**coaApiV1CreditMemoNextCreditMemoNumberRetrieve**](#coaapiv1creditmemonextcreditmemonumberretrieve) | **GET** /coa/api/v1/credit-memo/next-credit-memo-number | Get Next Credit Memo Number|
|[**coaApiV1CreditMemoPartialUpdate**](#coaapiv1creditmemopartialupdate) | **PATCH** /coa/api/v1/credit-memo/{id} | Partial Update Credit Memo|
|[**coaApiV1CreditMemoPaymentVoidCreate**](#coaapiv1creditmemopaymentvoidcreate) | **POST** /coa/api/v1/credit-memo/{credit_memo_id}/payment/{payment_id}/void | Void Credit Memo Used Payment|
|[**coaApiV1CreditMemoPaymentVoidDestroy**](#coaapiv1creditmemopaymentvoiddestroy) | **DELETE** /coa/api/v1/credit-memo/{credit_memo_id}/payment/{payment_id}/void | Delete Credit Memo Used Payment|
|[**coaApiV1CreditMemoReopenCreate**](#coaapiv1creditmemoreopencreate) | **POST** /coa/api/v1/credit-memo/{credit_memo_id}/reopen | Reopen Voided Credit Memo|
|[**coaApiV1CreditMemoRetrieve**](#coaapiv1creditmemoretrieve) | **GET** /coa/api/v1/credit-memo/{id} | Retrieve Credit Memo|
|[**coaApiV1CreditMemoUpdate**](#coaapiv1creditmemoupdate) | **PUT** /coa/api/v1/credit-memo/{id} | Update Credit Memo|
|[**coaApiV1CreditMemoVoidCreate**](#coaapiv1creditmemovoidcreate) | **POST** /coa/api/v1/credit-memo/{credit_memo_id}/void | Void Credit Memo|
|[**coaApiV1InvoiceBulkApplyPaymentCreate**](#coaapiv1invoicebulkapplypaymentcreate) | **POST** /coa/api/v1/invoice/bulk-apply-payment | Bulk Apply Transaction Payment to Selected Invoices|
|[**coaApiV1InvoiceBulkSearchCreate**](#coaapiv1invoicebulksearchcreate) | **POST** /coa/api/v1/invoice/bulk-search | Bulk Search Invoices by Number|
|[**coaApiV1InvoiceCalculatePaymentCreate**](#coaapiv1invoicecalculatepaymentcreate) | **POST** /coa/api/v1/invoice/{invoice_id}/calculate-payment | Calculate Invoice Payment|
|[**coaApiV1InvoiceCreate**](#coaapiv1invoicecreate) | **POST** /coa/api/v1/invoice | Create Invoice|
|[**coaApiV1InvoiceDefaultPaymentCreate**](#coaapiv1invoicedefaultpaymentcreate) | **POST** /coa/api/v1/invoice/{invoice_id}/default-payment | Get Default Payment Amount|
|[**coaApiV1InvoiceDestroy**](#coaapiv1invoicedestroy) | **DELETE** /coa/api/v1/invoice/{id} | Delete Invoice|
|[**coaApiV1InvoiceList**](#coaapiv1invoicelist) | **GET** /coa/api/v1/invoice | List Invoices|
|[**coaApiV1InvoicePartialUpdate**](#coaapiv1invoicepartialupdate) | **PATCH** /coa/api/v1/invoice/{id} | Partial Update Invoice|
|[**coaApiV1InvoicePayCreate**](#coaapiv1invoicepaycreate) | **POST** /coa/api/v1/invoice/{invoice_id}/pay | Mark Invoice as Paid|
|[**coaApiV1InvoicePaymentVoidCreate**](#coaapiv1invoicepaymentvoidcreate) | **POST** /coa/api/v1/invoice/{invoice_id}/payment/{payment_id}/void | Void Invoice Payment|
|[**coaApiV1InvoicePaymentVoidDestroy**](#coaapiv1invoicepaymentvoiddestroy) | **DELETE** /coa/api/v1/invoice/{invoice_id}/payment/{payment_id}/void | Delete Invoice Payment|
|[**coaApiV1InvoicePaymentsList**](#coaapiv1invoicepaymentslist) | **GET** /coa/api/v1/invoice-payments | List Invoice Payments|
|[**coaApiV1InvoiceReopenCreate**](#coaapiv1invoicereopencreate) | **POST** /coa/api/v1/invoice/{invoice_id}/reopen | Reopen Voided Invoice|
|[**coaApiV1InvoiceReportDataRetrieve**](#coaapiv1invoicereportdataretrieve) | **GET** /coa/api/v1/invoice/report/{id}/data | Execute invoice report|
|[**coaApiV1InvoiceReportPreviewRetrieve**](#coaapiv1invoicereportpreviewretrieve) | **GET** /coa/api/v1/invoice/report/preview | Preview invoice report|
|[**coaApiV1InvoiceRetrieve**](#coaapiv1invoiceretrieve) | **GET** /coa/api/v1/invoice/{id} | Retrieve Invoice|
|[**coaApiV1InvoiceStatsRetrieve**](#coaapiv1invoicestatsretrieve) | **GET** /coa/api/v1/invoice/stats | Invoice Stat Card Aggregates|
|[**coaApiV1InvoiceUpdate**](#coaapiv1invoiceupdate) | **PUT** /coa/api/v1/invoice/{id} | Update Invoice|
|[**coaApiV1InvoiceVoidCreate**](#coaapiv1invoicevoidcreate) | **POST** /coa/api/v1/invoice/{invoice_id}/void | Void Invoice|
|[**createProduct**](#createproduct) | **POST** /rr/api/v1/product | Create Contract Product|
|[**getClientInvoiceStatementPdf**](#getclientinvoicestatementpdf) | **GET** /coa/api/v1/invoice/statement/client/{client_id}/pdf | Get Client Invoice Statement PDF|
|[**getCreditMemoPdf**](#getcreditmemopdf) | **GET** /coa/api/v1/credit-memo/{id}/pdf | Get Credit Memo PDF|
|[**listProducts**](#listproducts) | **GET** /rr/api/v1/product | List Contract Products|
|[**rrApiV1ProductBulkSearchCreate**](#rrapiv1productbulksearchcreate) | **POST** /rr/api/v1/product/bulk-search | Bulk Search Products|
|[**rrApiV1ProductDeleteCreate**](#rrapiv1productdeletecreate) | **POST** /rr/api/v1/product/{id}/delete | Delete Product|
|[**rrApiV1ProductDestroy**](#rrapiv1productdestroy) | **DELETE** /rr/api/v1/product/{id} | Delete Product (deprecated)|
|[**rrApiV1ProductPartialUpdate**](#rrapiv1productpartialupdate) | **PATCH** /rr/api/v1/product/{id} | Partial Update Product|
|[**rrApiV1ProductRetrieve**](#rrapiv1productretrieve) | **GET** /rr/api/v1/product/{id} | Retrieve Product|
|[**rrApiV1ProductUpdate**](#rrapiv1productupdate) | **PUT** /rr/api/v1/product/{id} | Update Product|
|[**sendCreditMemo**](#sendcreditmemo) | **PUT** /coa/api/v1/credit-memo/{id}/send | Send Credit Memo|

# **bulkCreateInvoices**
> Array<AccountingInvoice> bulkCreateInvoices(bulkCreateInvoices)

     Create multiple invoices atomically in a single transaction.      All invoices are created within a single database transaction. If any invoice creation fails,     all invoices are rolled back and no invoices are created.      This endpoint validates all invoices before creating any of them, ensuring data integrity.     

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    BulkCreateInvoices
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let bulkCreateInvoices: BulkCreateInvoices; //

const { status, data } = await apiInstance.bulkCreateInvoices(
    bulkCreateInvoices
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulkCreateInvoices** | **BulkCreateInvoices**|  | |


### Return type

**Array<AccountingInvoice>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |
|**400** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1CreditMemoBulkSearchCreate**
> { [key: string]: any; } coaApiV1CreditMemoBulkSearchCreate(bulkCreditMemoSearch)

Search for thousands of credit memos by exact credit memo number match in a single request. Optimized for performance.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    BulkCreditMemoSearch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let bulkCreditMemoSearch: BulkCreditMemoSearch; //

const { status, data } = await apiInstance.coaApiV1CreditMemoBulkSearchCreate(
    bulkCreditMemoSearch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulkCreditMemoSearch** | **BulkCreditMemoSearch**|  | |


### Return type

**{ [key: string]: any; }**

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

# **coaApiV1CreditMemoCreate**
> AccountingCreditMemo coaApiV1CreditMemoCreate(accountingCreditMemo)

         Creates a new accounting credit memo with line items and automatic journal entry generation.          This endpoint allows for comprehensive credit memo creation with:         - Multiple line items with different products, accounts, amounts, and departmental allocations         - Automatic journal entry creation following double-entry bookkeeping principles         - Multi-currency support with exchange rate handling         - Client and entity relationship management         - Contract associations for revenue recognition tracking         - Product-based line item categorization with tax handling         - Tag-based transaction categorization and reporting         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    AccountingCreditMemo
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let accountingCreditMemo: AccountingCreditMemo; //

const { status, data } = await apiInstance.coaApiV1CreditMemoCreate(
    accountingCreditMemo
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountingCreditMemo** | **AccountingCreditMemo**|  | |


### Return type

**AccountingCreditMemo**

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

# **coaApiV1CreditMemoDestroy**
> coaApiV1CreditMemoDestroy()

         Permanently deletes an accounting credit memo and all associated data from the system.          This endpoint performs a complete removal of the credit memo including:         - Complete credit memo record deletion with all line items         - Automatic journal entry removal and accounting transaction cleanup          **Accounting Impact:**         - Associated journal entries are automatically deleted to maintain accounting integrity         - Exchange rate records and multi-currency data are cleaned up          **Restrictions:**         - Credit memos that have been applied to invoices cannot be deleted         - Credit memos in closed accounting periods may have deletion restrictions         - Consider the impact on historical financial reporting         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1CreditMemoDestroy(
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

# **coaApiV1CreditMemoList**
> PaginatedAccountingCreditMemoList coaApiV1CreditMemoList()

         Retrieves a paginated list of accounting credit memos with comprehensive filtering and sorting capabilities.          This endpoint provides a powerful interface for browsing and searching credit memos with:         - Advanced filtering by date ranges, status, clients, entities, and contracts         - Full-text search across credit memo numbers, messages, and client names         - Flexible sorting by multiple fields including amounts and relationships         - Optimized performance with efficient database queries and pagination         - Complete credit memo details including line items, payment status, and accounting relationships          **Key Features:**         - Date range filtering for credit memo creation and application dates         - Status-based filtering (open, partially_used, used, voided)         - Client and entity-based filtering with hierarchical client support         - Contract association filtering for revenue recognition workflows         - Full-text search capabilities across key fields          **Query Parameters:**         - `start_date`, `end_date`: Filter by credit memo date range         - `status`: Filter by application status (open, partially_used, used, voided)         - `q`: Full-text search across credit memo number, message, and client name         - `client`: Filter by specific client IDs (supports multiple values)         - `entity`: Filter by specific entity IDs (supports multiple values)         - `contract`: Filter by specific contract IDs (supports multiple values)         - `sort`: Sort by various fields (credit_memo_date, client_name, total_amount, etc.)         - `limit`, `offset`: Pagination controls for large result sets         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let client: Array<number>; //Filter by client IDs (can specify multiple) (optional) (default to undefined)
let contract: Array<number>; //Filter by contract IDs (can specify multiple) (optional) (default to undefined)
let endDate: string; //Filter credit memos created on or before this date (YYYY-MM-DD format) (optional) (default to undefined)
let entity: Array<number>; //Filter by entity IDs (can specify multiple) (optional) (default to undefined)
let limit: number; //Number of results to return per page (optional) (default to undefined)
let offset: number; //Number of results to skip for pagination (optional) (default to undefined)
let q: string; //Search credit memo numbers, messages, and client names (optional) (default to undefined)
let sort: '-amount_used' | '-client_name' | '-credit_memo_date' | '-credit_memo_number' | '-total_amount' | 'amount_used' | 'client_name' | 'credit_memo_date' | 'credit_memo_number' | 'total_amount'; //Sort results by field (prefix with - for descending) (optional) (default to undefined)
let startDate: string; //Filter credit memos created on or after this date (YYYY-MM-DD format) (optional) (default to undefined)
let status: 'open' | 'partially_used' | 'used' | 'voided'; //Filter by application status (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiV1CreditMemoList(
    client,
    contract,
    endDate,
    entity,
    limit,
    offset,
    q,
    sort,
    startDate,
    status
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client** | **Array&lt;number&gt;** | Filter by client IDs (can specify multiple) | (optional) defaults to undefined|
| **contract** | **Array&lt;number&gt;** | Filter by contract IDs (can specify multiple) | (optional) defaults to undefined|
| **endDate** | [**string**] | Filter credit memos created on or before this date (YYYY-MM-DD format) | (optional) defaults to undefined|
| **entity** | **Array&lt;number&gt;** | Filter by entity IDs (can specify multiple) | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page | (optional) defaults to undefined|
| **offset** | [**number**] | Number of results to skip for pagination | (optional) defaults to undefined|
| **q** | [**string**] | Search credit memo numbers, messages, and client names | (optional) defaults to undefined|
| **sort** | [**&#39;-amount_used&#39; | &#39;-client_name&#39; | &#39;-credit_memo_date&#39; | &#39;-credit_memo_number&#39; | &#39;-total_amount&#39; | &#39;amount_used&#39; | &#39;client_name&#39; | &#39;credit_memo_date&#39; | &#39;credit_memo_number&#39; | &#39;total_amount&#39;**]**Array<&#39;-amount_used&#39; &#124; &#39;-client_name&#39; &#124; &#39;-credit_memo_date&#39; &#124; &#39;-credit_memo_number&#39; &#124; &#39;-total_amount&#39; &#124; &#39;amount_used&#39; &#124; &#39;client_name&#39; &#124; &#39;credit_memo_date&#39; &#124; &#39;credit_memo_number&#39; &#124; &#39;total_amount&#39;>** | Sort results by field (prefix with - for descending) | (optional) defaults to undefined|
| **startDate** | [**string**] | Filter credit memos created on or after this date (YYYY-MM-DD format) | (optional) defaults to undefined|
| **status** | [**&#39;open&#39; | &#39;partially_used&#39; | &#39;used&#39; | &#39;voided&#39;**]**Array<&#39;open&#39; &#124; &#39;partially_used&#39; &#124; &#39;used&#39; &#124; &#39;voided&#39;>** | Filter by application status | (optional) defaults to undefined|


### Return type

**PaginatedAccountingCreditMemoList**

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

# **coaApiV1CreditMemoMarkUsedCreate**
> object coaApiV1CreditMemoMarkUsedCreate(markCreditMemoUsed)

Mark a credit memo as used by linking to an existing transaction.          The transaction\'s debit amount will be recategorized to A/R to clear the credit memo.         The credit memo\'s status will be updated to \"used\" or \"partially_used\" based on         the amount applied vs the total amount.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    MarkCreditMemoUsed
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let creditMemoId: number; //ID of the credit memo to mark as used (default to undefined)
let markCreditMemoUsed: MarkCreditMemoUsed; //

const { status, data } = await apiInstance.coaApiV1CreditMemoMarkUsedCreate(
    creditMemoId,
    markCreditMemoUsed
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **markCreditMemoUsed** | **MarkCreditMemoUsed**|  | |
| **creditMemoId** | [**number**] | ID of the credit memo to mark as used | defaults to undefined|


### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Credit memo marked as used successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1CreditMemoNextCreditMemoNumberRetrieve**
> coaApiV1CreditMemoNextCreditMemoNumberRetrieve()


### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

const { status, data } = await apiInstance.coaApiV1CreditMemoNextCreditMemoNumberRetrieve();
```

### Parameters
This endpoint does not have any parameters.


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
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1CreditMemoPartialUpdate**
> AccountingCreditMemo coaApiV1CreditMemoPartialUpdate()

         Performs a partial update of an existing accounting credit memo using PATCH semantics.          This endpoint allows selective modification of credit memo fields without requiring         a complete credit memo replacement. You can update specific aspects of the credit memo while         leaving other fields unchanged.          **Updatable Fields:**         - Credit memo metadata (dates, messages, descriptions, client, entity, currency)         - Line items (amounts, accounts, descriptions, departments, products)         - Reference numbers and contract associations         - Exchange rates and currency information         - Custom fields and additional metadata         - Application status and tracking information         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    PatchedAccountingCreditMemo
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)
let patchedAccountingCreditMemo: PatchedAccountingCreditMemo; // (optional)

const { status, data } = await apiInstance.coaApiV1CreditMemoPartialUpdate(
    id,
    patchedAccountingCreditMemo
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedAccountingCreditMemo** | **PatchedAccountingCreditMemo**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**AccountingCreditMemo**

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

# **coaApiV1CreditMemoPaymentVoidCreate**
> AccountingCreditMemoPayment coaApiV1CreditMemoPaymentVoidCreate()

Void a credit memo \'mark used\' payment by creating a reversing journal entry.          This creates a reversing JE that credits the A/R account and debits Uncategorized,         then marks the payment as voided.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    VoidPayment
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let creditMemoId: number; //ID of the credit memo (default to undefined)
let paymentId: number; //ID of the payment to void (default to undefined)
let voidPayment: VoidPayment; // (optional)

const { status, data } = await apiInstance.coaApiV1CreditMemoPaymentVoidCreate(
    creditMemoId,
    paymentId,
    voidPayment
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **voidPayment** | **VoidPayment**|  | |
| **creditMemoId** | [**number**] | ID of the credit memo | defaults to undefined|
| **paymentId** | [**number**] | ID of the payment to void | defaults to undefined|


### Return type

**AccountingCreditMemoPayment**

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

# **coaApiV1CreditMemoPaymentVoidDestroy**
> coaApiV1CreditMemoPaymentVoidDestroy()

Remove a credit memo \'mark used\' payment application.          This recategorizes the transaction back to Uncategorized and deletes the payment record.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let creditMemoId: number; //ID of the credit memo (default to undefined)
let paymentId: number; //ID of the payment to delete (default to undefined)

const { status, data } = await apiInstance.coaApiV1CreditMemoPaymentVoidDestroy(
    creditMemoId,
    paymentId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **creditMemoId** | [**number**] | ID of the credit memo | defaults to undefined|
| **paymentId** | [**number**] | ID of the payment to delete | defaults to undefined|


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

# **coaApiV1CreditMemoReopenCreate**
> AccountingCreditMemo coaApiV1CreditMemoReopenCreate()

Reopen a voided credit memo.          This removes the void date and void journal entry, and sets the credit memo status back to open.         The voiding journal entry will be deleted to reverse the void operation.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let creditMemoId: number; //ID of the voided credit memo to reopen (default to undefined)

const { status, data } = await apiInstance.coaApiV1CreditMemoReopenCreate(
    creditMemoId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **creditMemoId** | [**number**] | ID of the voided credit memo to reopen | defaults to undefined|


### Return type

**AccountingCreditMemo**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1CreditMemoRetrieve**
> AccountingCreditMemo coaApiV1CreditMemoRetrieve()

         Retrieves a single accounting credit memo with complete details including line items, payments, and accounting relationships.          This endpoint provides comprehensive credit memo information with:         - Complete credit memo metadata (dates, amounts, status, currency, terms)         - All associated line items with product details, account information, and departmental allocations         - Payment application history with journal entry references and transaction details         - Client and entity information with relationship details         - Contract associations for revenue recognition and reporting         - File attachments and supporting documentation         - Journal entry references for accounting audit trails and compliance         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1CreditMemoRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**AccountingCreditMemo**

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

# **coaApiV1CreditMemoUpdate**
> AccountingCreditMemo coaApiV1CreditMemoUpdate(accountingCreditMemo)

         Performs a complete update of an existing accounting credit memo using PUT semantics.          This endpoint allows full replacement of credit memo data including:         - Complete credit memo metadata update (dates, amounts, client, entity, currency)         - Full line item replacement with new products, accounts, amounts, and departmental allocations         - Journal entry recalculation and update with new accounting transactions         - Exchange rate updates for multi-currency credit memos         - Contract and reference number association updates         - Custom field updates and modifications          **Important Notes:**         - This is a full replacement operation - all credit memo data will be updated         - Missing fields in the request will be set to null or default values         - Existing line items will be completely replaced with the new line items         - Journal entries will be updated to reflect all changes         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    AccountingCreditMemo
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)
let accountingCreditMemo: AccountingCreditMemo; //

const { status, data } = await apiInstance.coaApiV1CreditMemoUpdate(
    id,
    accountingCreditMemo
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountingCreditMemo** | **AccountingCreditMemo**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**AccountingCreditMemo**

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

# **coaApiV1CreditMemoVoidCreate**
> AccountingCreditMemo coaApiV1CreditMemoVoidCreate(voidCreditMemoRequest)

Void an existing credit memo.          This creates a reversing journal entry to void the credit memo by reversing all debit and credit amounts.         The credit memo status will be updated to reflect the void.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    VoidCreditMemoRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let creditMemoId: number; //ID of the credit memo to void (default to undefined)
let voidCreditMemoRequest: VoidCreditMemoRequest; //

const { status, data } = await apiInstance.coaApiV1CreditMemoVoidCreate(
    creditMemoId,
    voidCreditMemoRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **voidCreditMemoRequest** | **VoidCreditMemoRequest**|  | |
| **creditMemoId** | [**number**] | ID of the credit memo to void | defaults to undefined|


### Return type

**AccountingCreditMemo**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1InvoiceBulkApplyPaymentCreate**
> { [key: string]: any; } coaApiV1InvoiceBulkApplyPaymentCreate(bulkApplyInvoicePayment)

Apply a single transaction payment to multiple selected invoices.  Supports two selection modes: - Explicit invoice IDs (``invoice_ids``) - Filter-based selection (``filters``) for \"select all matching\" behaviour  Reuses :meth:`MarkInvoicePaidView.apply_transaction_payment` so that line-level payment splitting, FX gain/loss realisation, and transaction cleanup are all respected.  A single ``DraftQueue`` is created when approval is required.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    BulkApplyInvoicePayment
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let bulkApplyInvoicePayment: BulkApplyInvoicePayment; //

const { status, data } = await apiInstance.coaApiV1InvoiceBulkApplyPaymentCreate(
    bulkApplyInvoicePayment
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulkApplyInvoicePayment** | **BulkApplyInvoicePayment**|  | |


### Return type

**{ [key: string]: any; }**

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

# **coaApiV1InvoiceBulkSearchCreate**
> { [key: string]: any; } coaApiV1InvoiceBulkSearchCreate(bulkInvoiceSearch)

Search for thousands of invoices by exact invoice number match in a single request. Optimized for performance.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    BulkInvoiceSearch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let bulkInvoiceSearch: BulkInvoiceSearch; //

const { status, data } = await apiInstance.coaApiV1InvoiceBulkSearchCreate(
    bulkInvoiceSearch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulkInvoiceSearch** | **BulkInvoiceSearch**|  | |


### Return type

**{ [key: string]: any; }**

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

# **coaApiV1InvoiceCalculatePaymentCreate**
> CalculatePaymentOutput coaApiV1InvoiceCalculatePaymentCreate()

Calculate the payment details for an invoice.          This endpoint calculates:         - Total amount due on the invoice         - Applied payments (existing + proposed)         - Applied credits (existing + proposed credit memos)         - Payment term discounts (based on payment dates) - ALL OR NOTHING: discount only applies if paying full invoice         - Remaining balance due          Supports payment terms with early payment discounts (all-or-nothing).         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    CalculatePaymentInput
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let invoiceId: number; //ID of the invoice (default to undefined)
let calculatePaymentInput: CalculatePaymentInput; // (optional)

const { status, data } = await apiInstance.coaApiV1InvoiceCalculatePaymentCreate(
    invoiceId,
    calculatePaymentInput
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **calculatePaymentInput** | **CalculatePaymentInput**|  | |
| **invoiceId** | [**number**] | ID of the invoice | defaults to undefined|


### Return type

**CalculatePaymentOutput**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**400** | Bad Request |  -  |
|**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1InvoiceCreate**
> AccountingInvoice coaApiV1InvoiceCreate(accountingInvoice)

         Creates a new accounting invoice with line items and automatic journal entry generation.          This endpoint allows for comprehensive invoice creation with:         - Multiple line items with different products, rates, quantities, and tax handling         - Automatic accounts receivable journal entry creation         - Tax calculations and tax account handling         - Multi-currency support with exchange rate handling         - Product-based taxation rules         - Service date tracking for revenue recognition         - Contract and purchase order integration         - Stripe payment integration support          Key features:         - Credits revenue accounts for each line item amount         - Debits accounts receivable for the total amount         - Handles tax calculations with appropriate tax accounts         - Supports entity-specific currency conversions         - Creates proper double-entry accounting transactions         - Validates client, entity, and product relationships         - Integrates with Stripe for payment processing          Requirements:         - All referenced products, clients, and entities must exist and be active         - Client must be of type \'customer\'         - Line items must have valid amounts, quantities, and rates         - Currency must be valid for the entity         - Tax calculations must comply with configured tax rules         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    AccountingInvoice
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let accountingInvoice: AccountingInvoice; //

const { status, data } = await apiInstance.coaApiV1InvoiceCreate(
    accountingInvoice
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountingInvoice** | **AccountingInvoice**|  | |


### Return type

**AccountingInvoice**

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

# **coaApiV1InvoiceDefaultPaymentCreate**
> GetDefaultPaymentOutput coaApiV1InvoiceDefaultPaymentCreate(getDefaultPaymentInput)

Get the default payment amount for an invoice based on when payment is posted.          If the invoice has discount terms and the posted date is within the discount period,         the discounted amount is returned. Otherwise, the full amount is returned.         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    GetDefaultPaymentInput
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let invoiceId: number; //ID of the invoice (default to undefined)
let getDefaultPaymentInput: GetDefaultPaymentInput; //

const { status, data } = await apiInstance.coaApiV1InvoiceDefaultPaymentCreate(
    invoiceId,
    getDefaultPaymentInput
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **getDefaultPaymentInput** | **GetDefaultPaymentInput**|  | |
| **invoiceId** | [**number**] | ID of the invoice | defaults to undefined|


### Return type

**GetDefaultPaymentOutput**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**400** | Bad Request |  -  |
|**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1InvoiceDestroy**
> coaApiV1InvoiceDestroy()

         Permanently deletes an accounting invoice and its associated journal entry and related data.          This endpoint performs a complete deletion of the invoice including:         - Removal of all invoice line items and associated product data         - Deletion of the corresponding accounts receivable journal entry         - Removal of payment records and journal entries          **Important Notes:**         - This operation is irreversible and permanently removes the invoice from the system         - The associated journal entry will be automatically deleted to maintain accounting integrity          **Restrictions:**         - Invoices in closed accounting periods cannot be deleted         - Consider the impact on historical financial reporting         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1InvoiceDestroy(
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

# **coaApiV1InvoiceList**
> PaginatedAccountingInvoiceListList coaApiV1InvoiceList()

         Retrieve a paginated list of invoices with comprehensive filtering, sorting, and download capabilities.          This endpoint provides powerful invoice listing with:         - Advanced filtering by date ranges, status, clients, and entities         - Full-text search across multiple fields         - Flexible sorting options including custom calculated fields         - Async CSV export functionality via email         - Optimized queries with prefetched relationships          **Filtering Options:**         - Date-based filtering (invoice_date, due_date ranges)         - Status-based filtering (payment status, sent status, aging buckets)         - Entity and client-based filtering (supports multiple selections)         - Contract and currency filtering         - Full-text search across invoice numbers, addresses, messages, and client names          **Sorting Capabilities:**         - Standard field sorting (invoice_date, total_amount, due_date, etc.)         - Custom calculated field sorting (amount_due, client_name, contract_name)         - Ascending/descending order with null handling          **Performance Features:**         - Efficient database queries with proper indexing         - Prefetched related objects (lines, payments, clients, entities)         - Pagination support for large datasets         - Optimized for high-volume invoice management          **Export Functionality:**         - Async CSV generation and email delivery         - Filtered export based on current query parameters         - Background processing to handle large datasets         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let client: number; //Filter by client ID. Can be specified multiple times (optional) (default to undefined)
let contract: number; //Filter by contract ID (optional) (default to undefined)
let currency: string; //Filter by currency code (e.g., USD, EUR) (optional) (default to undefined)
let download: boolean; //If true, triggers async CSV download workflow and sends result via email (optional) (default to false)
let endDate: string; //Filter invoices with invoice_date on or before this date (YYYY-MM-DD) (optional) (default to undefined)
let entity: number; //Filter by entity ID. Can be specified multiple times (optional) (default to undefined)
let invoiceNumber: string; //Filter by exact invoice number (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let lineTagGroupId: number; //Filter invoices with at least one line item assigned a tag from this tag group ID (optional) (default to undefined)
let lineTagId: number; //Filter invoices with at least one line item assigned this tag ID (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let paidDateFrom: string; //Filter invoices with paid_date on or after this date (YYYY-MM-DD) (optional) (default to undefined)
let paidDateTo: string; //Filter invoices with paid_date on or before this date (YYYY-MM-DD) (optional) (default to undefined)
let parentClient: number; //Filter by parent client (Vendor) ID. Returns invoices for the specified client and all of its descendants via vendor lineage. (optional) (default to undefined)
let q: string; //Search query - searches shipping address, invoice number, message, or client name (optional) (default to undefined)
let refNumber: string; //Filter by exact ref number (optional) (default to undefined)
let sentStatus: 'not_sent' | 'sent'; //Filter by sent status (optional) (default to undefined)
let sort: string; //Sort order. Use field name for ascending, -field for descending. Special fields: client_name, amount_due. Default: -invoice_date (optional) (default to '-invoice_date')
let startDate: string; //Filter invoices with invoice_date on or after this date (YYYY-MM-DD) (optional) (default to undefined)
let status: '1_30' | '31_60' | '61_90' | '91_120' | 'current' | 'open' | 'over_120' | 'paid' | 'partially_paid' | 'past_due' | 'scheduled' | 'sent' | 'uncollectible' | 'unpaid' | 'voided'; //Filter by payment status (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiV1InvoiceList(
    client,
    contract,
    currency,
    download,
    endDate,
    entity,
    invoiceNumber,
    limit,
    lineTagGroupId,
    lineTagId,
    offset,
    paidDateFrom,
    paidDateTo,
    parentClient,
    q,
    refNumber,
    sentStatus,
    sort,
    startDate,
    status
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **client** | [**number**] | Filter by client ID. Can be specified multiple times | (optional) defaults to undefined|
| **contract** | [**number**] | Filter by contract ID | (optional) defaults to undefined|
| **currency** | [**string**] | Filter by currency code (e.g., USD, EUR) | (optional) defaults to undefined|
| **download** | [**boolean**] | If true, triggers async CSV download workflow and sends result via email | (optional) defaults to false|
| **endDate** | [**string**] | Filter invoices with invoice_date on or before this date (YYYY-MM-DD) | (optional) defaults to undefined|
| **entity** | [**number**] | Filter by entity ID. Can be specified multiple times | (optional) defaults to undefined|
| **invoiceNumber** | [**string**] | Filter by exact invoice number | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **lineTagGroupId** | [**number**] | Filter invoices with at least one line item assigned a tag from this tag group ID | (optional) defaults to undefined|
| **lineTagId** | [**number**] | Filter invoices with at least one line item assigned this tag ID | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **paidDateFrom** | [**string**] | Filter invoices with paid_date on or after this date (YYYY-MM-DD) | (optional) defaults to undefined|
| **paidDateTo** | [**string**] | Filter invoices with paid_date on or before this date (YYYY-MM-DD) | (optional) defaults to undefined|
| **parentClient** | [**number**] | Filter by parent client (Vendor) ID. Returns invoices for the specified client and all of its descendants via vendor lineage. | (optional) defaults to undefined|
| **q** | [**string**] | Search query - searches shipping address, invoice number, message, or client name | (optional) defaults to undefined|
| **refNumber** | [**string**] | Filter by exact ref number | (optional) defaults to undefined|
| **sentStatus** | [**&#39;not_sent&#39; | &#39;sent&#39;**]**Array<&#39;not_sent&#39; &#124; &#39;sent&#39;>** | Filter by sent status | (optional) defaults to undefined|
| **sort** | [**string**] | Sort order. Use field name for ascending, -field for descending. Special fields: client_name, amount_due. Default: -invoice_date | (optional) defaults to '-invoice_date'|
| **startDate** | [**string**] | Filter invoices with invoice_date on or after this date (YYYY-MM-DD) | (optional) defaults to undefined|
| **status** | [**&#39;1_30&#39; | &#39;31_60&#39; | &#39;61_90&#39; | &#39;91_120&#39; | &#39;current&#39; | &#39;open&#39; | &#39;over_120&#39; | &#39;paid&#39; | &#39;partially_paid&#39; | &#39;past_due&#39; | &#39;scheduled&#39; | &#39;sent&#39; | &#39;uncollectible&#39; | &#39;unpaid&#39; | &#39;voided&#39;**]**Array<&#39;1_30&#39; &#124; &#39;31_60&#39; &#124; &#39;61_90&#39; &#124; &#39;91_120&#39; &#124; &#39;current&#39; &#124; &#39;open&#39; &#124; &#39;over_120&#39; &#124; &#39;paid&#39; &#124; &#39;partially_paid&#39; &#124; &#39;past_due&#39; &#124; &#39;scheduled&#39; &#124; &#39;sent&#39; &#124; &#39;uncollectible&#39; &#124; &#39;unpaid&#39; &#124; &#39;voided&#39;>** | Filter by payment status | (optional) defaults to undefined|


### Return type

**PaginatedAccountingInvoiceListList**

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

# **coaApiV1InvoicePartialUpdate**
> AccountingInvoice coaApiV1InvoicePartialUpdate()

         Performs a partial update of an existing accounting invoice using PATCH semantics.          This endpoint allows selective modification of invoice fields without requiring         a complete invoice replacement. You can update specific aspects of the invoice while         leaving other fields unchanged.          **Updatable Fields:**         - Invoice metadata (dates, terms, descriptions, client, entity, currency)         - Line items (amounts, accounts, descriptions, departments, products)         - Payment terms and due dates         - Tax calculations and allocations         - Custom fields and tags         - Contract and purchase order associations         - Exchange rates and currency information         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    PatchedAccountingInvoice
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)
let patchedAccountingInvoice: PatchedAccountingInvoice; // (optional)

const { status, data } = await apiInstance.coaApiV1InvoicePartialUpdate(
    id,
    patchedAccountingInvoice
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedAccountingInvoice** | **PatchedAccountingInvoice**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**AccountingInvoice**

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

# **coaApiV1InvoicePayCreate**
> MarkInvoicePaidResponse coaApiV1InvoicePayCreate()

Mark an invoice as paid, allowing partial payments.          This endpoint supports multiple payment methods:         - Apply existing transactions as payments         - Apply credit memos to reduce the invoice balance         - Create manual payments without a transaction          The request body should contain at least one of:         - transactions: List of transaction payments to apply         - credit_memos: List of credit memos to apply         - empty_transactions: List of manual payments without transactions

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    MarkPaid
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let invoiceId: number; //ID of the invoice to mark as paid (default to undefined)
let markPaid: MarkPaid; // (optional)

const { status, data } = await apiInstance.coaApiV1InvoicePayCreate(
    invoiceId,
    markPaid
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **markPaid** | **MarkPaid**|  | |
| **invoiceId** | [**number**] | ID of the invoice to mark as paid | defaults to undefined|


### Return type

**MarkInvoicePaidResponse**

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

# **coaApiV1InvoicePaymentVoidCreate**
> AccountingInvoicePayment coaApiV1InvoicePaymentVoidCreate()

Void an existing invoice payment.          This creates a reversing journal entry to void the payment and updates the invoice status.         For Stripe payments, this will also process a refund through Stripe.          Optionally accepts a void_date in the request body to specify when the payment should be voided.         If not provided, defaults to today\'s date.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    VoidPayment
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let invoiceId: number; //ID of the invoice (default to undefined)
let paymentId: number; //ID of the payment to void (default to undefined)
let voidPayment: VoidPayment; // (optional)

const { status, data } = await apiInstance.coaApiV1InvoicePaymentVoidCreate(
    invoiceId,
    paymentId,
    voidPayment
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **voidPayment** | **VoidPayment**|  | |
| **invoiceId** | [**number**] | ID of the invoice | defaults to undefined|
| **paymentId** | [**number**] | ID of the payment to void | defaults to undefined|


### Return type

**AccountingInvoicePayment**

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

# **coaApiV1InvoicePaymentVoidDestroy**
> coaApiV1InvoicePaymentVoidDestroy()

Delete an invoice payment.          This removes the payment record and updates the transaction to uncategorized.         For Stripe payments, this will also process a refund through Stripe.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let invoiceId: number; //ID of the invoice (default to undefined)
let paymentId: number; //ID of the payment to delete (default to undefined)

const { status, data } = await apiInstance.coaApiV1InvoicePaymentVoidDestroy(
    invoiceId,
    paymentId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **invoiceId** | [**number**] | ID of the invoice | defaults to undefined|
| **paymentId** | [**number**] | ID of the payment to delete | defaults to undefined|


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

# **coaApiV1InvoicePaymentsList**
> PaginatedInvoicePaymentSyncList coaApiV1InvoicePaymentsList()

         Retrieve a paginated list of invoice payments (payments applied against accounts         receivable invoices), designed for syncing payment data into external systems.          Results are ordered by (last_modified_at, id) ascending, so pages are stable and         a sync can resume from where it left off.          **Full sync (cursor pagination):**         - Pass an empty cursor parameter (cursor=) on the first request         - Follow the \'next\' URL from each response until it is null          **Incremental sync (time-based):**         - Store the highest last_modified_at value you have processed         - On the next run, pass it as last_modified_at__gte to fetch only new and updated payments          **Voids:**         - Voided payments are included by default with voided_date set, so integrators can           detect payments that were reversed after a previous sync         - Filter with voided=true or voided=false to fetch only one kind         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let cursor: string; //Opts into cursor pagination. Pass an empty value (cursor=) on the first request, then follow the \'next\' URL from each response until it is null. The cursor value is opaque - do not parse or construct it. Cursor pagination is recommended for full syncs as it avoids the performance penalty of deep offsets on large result sets. (optional) (default to undefined)
let externalId: string; //Filter for the payment carrying this upstream external_id. Use it to reconcile a payment you created via the invoice pay endpoint back to your source-system record. An empty value is ignored and returns all payments. (optional) (default to undefined)
let invoiceId: number; //Filter for payments applied to this invoice id. (optional) (default to undefined)
let lastModifiedAtGte: string; //Filter for payments modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Use this for incremental syncs: store the highest last_modified_at you have processed and pass it on the next sync run. (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for payments modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Date-only values are inclusive of the entire day. (optional) (default to undefined)
let limit: number; //Maximum number of records to return per page. Default 100, maximum 10000. Use with offset to paginate (optional) (default to 100)
let offset: number; //Number of records to skip before collecting the result page. Use with limit to paginate (optional) (default to 0)
let skipCount: boolean; //When \'true\', skips the total COUNT query and returns a lower-bound \'count\' instead. Recommended for large syncs where the exact total is not needed. (optional) (default to false)
let voided: boolean; //Filter by void status. When \'true\', returns only voided payments (voided_date is set). When \'false\', returns only active payments. When omitted, returns both so integrators can detect and propagate voids. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiV1InvoicePaymentsList(
    cursor,
    externalId,
    invoiceId,
    lastModifiedAtGte,
    lastModifiedAtLte,
    limit,
    offset,
    skipCount,
    voided
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **cursor** | [**string**] | Opts into cursor pagination. Pass an empty value (cursor&#x3D;) on the first request, then follow the \&#39;next\&#39; URL from each response until it is null. The cursor value is opaque - do not parse or construct it. Cursor pagination is recommended for full syncs as it avoids the performance penalty of deep offsets on large result sets. | (optional) defaults to undefined|
| **externalId** | [**string**] | Filter for the payment carrying this upstream external_id. Use it to reconcile a payment you created via the invoice pay endpoint back to your source-system record. An empty value is ignored and returns all payments. | (optional) defaults to undefined|
| **invoiceId** | [**number**] | Filter for payments applied to this invoice id. | (optional) defaults to undefined|
| **lastModifiedAtGte** | [**string**] | Filter for payments modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Use this for incremental syncs: store the highest last_modified_at you have processed and pass it on the next sync run. | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for payments modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Date-only values are inclusive of the entire day. | (optional) defaults to undefined|
| **limit** | [**number**] | Maximum number of records to return per page. Default 100, maximum 10000. Use with offset to paginate | (optional) defaults to 100|
| **offset** | [**number**] | Number of records to skip before collecting the result page. Use with limit to paginate | (optional) defaults to 0|
| **skipCount** | [**boolean**] | When \&#39;true\&#39;, skips the total COUNT query and returns a lower-bound \&#39;count\&#39; instead. Recommended for large syncs where the exact total is not needed. | (optional) defaults to false|
| **voided** | [**boolean**] | Filter by void status. When \&#39;true\&#39;, returns only voided payments (voided_date is set). When \&#39;false\&#39;, returns only active payments. When omitted, returns both so integrators can detect and propagate voids. | (optional) defaults to undefined|


### Return type

**PaginatedInvoicePaymentSyncList**

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

# **coaApiV1InvoiceReopenCreate**
> AccountingInvoice coaApiV1InvoiceReopenCreate()

Reopen a voided invoice.          This removes the void date and void journal entry, and sets the invoice status back to open.         The voiding journal entry will be deleted to reverse the void operation.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let invoiceId: number; //ID of the voided invoice to reopen (default to undefined)

const { status, data } = await apiInstance.coaApiV1InvoiceReopenCreate(
    invoiceId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **invoiceId** | [**number**] | ID of the voided invoice to reopen | defaults to undefined|


### Return type

**AccountingInvoice**

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

# **coaApiV1InvoiceReportDataRetrieve**
> InvoiceReportResponse coaApiV1InvoiceReportDataRetrieve()

Execute saved invoice report and return DataTable-compatible response.  :param request: HTTP request with query params :param pk: Custom report ID :return: Paginated, sparse-formatted response

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)
let aggregationFields: string; //Aggregates: sum:amount, sum:amount_paid, sum:amount_due, etc. (optional) (default to undefined)
let clientId: string; //Filter by client ID(s) (optional) (default to undefined)
let contractId: string; //Filter by contract ID(s) (optional) (default to undefined)
let currency: string; //Filter by currency code (optional) (default to undefined)
let departmentId: string; //Filter by department ID(s) (optional) (default to undefined)
let endDate: string; //End date (YYYY-MM-DD) (optional) (default to undefined)
let entityId: string; //Entity ID(s), comma-separated (optional) (default to undefined)
let groupFields: string; //Row dimensions: client_id, invoice_id, invoice_date_month, product_id, etc. (optional) (default to undefined)
let groupKeys: string; //Drilldown parent keys (optional) (default to undefined)
let includeTotals: boolean; //Include grand totals row (optional) (default to undefined)
let limit: number; //Page size (max 10000) (optional) (default to undefined)
let mode: string; //paginated | full | csv (optional) (default to undefined)
let offset: number; //Pagination offset (optional) (default to undefined)
let paymentStatus: string; //Filter by status: draft,open,sent,partial,paid,uncollectible (optional) (default to undefined)
let pivotFields: string; //Column dimensions: product_id, client_id, etc. (optional) (default to undefined)
let productId: string; //Filter by product ID(s) (optional) (default to undefined)
let shouldPivot: boolean; //Enable pivot columns (optional) (default to undefined)
let startDate: string; //Start date (YYYY-MM-DD) (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiV1InvoiceReportDataRetrieve(
    id,
    aggregationFields,
    clientId,
    contractId,
    currency,
    departmentId,
    endDate,
    entityId,
    groupFields,
    groupKeys,
    includeTotals,
    limit,
    mode,
    offset,
    paymentStatus,
    pivotFields,
    productId,
    shouldPivot,
    startDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|
| **aggregationFields** | [**string**] | Aggregates: sum:amount, sum:amount_paid, sum:amount_due, etc. | (optional) defaults to undefined|
| **clientId** | [**string**] | Filter by client ID(s) | (optional) defaults to undefined|
| **contractId** | [**string**] | Filter by contract ID(s) | (optional) defaults to undefined|
| **currency** | [**string**] | Filter by currency code | (optional) defaults to undefined|
| **departmentId** | [**string**] | Filter by department ID(s) | (optional) defaults to undefined|
| **endDate** | [**string**] | End date (YYYY-MM-DD) | (optional) defaults to undefined|
| **entityId** | [**string**] | Entity ID(s), comma-separated | (optional) defaults to undefined|
| **groupFields** | [**string**] | Row dimensions: client_id, invoice_id, invoice_date_month, product_id, etc. | (optional) defaults to undefined|
| **groupKeys** | [**string**] | Drilldown parent keys | (optional) defaults to undefined|
| **includeTotals** | [**boolean**] | Include grand totals row | (optional) defaults to undefined|
| **limit** | [**number**] | Page size (max 10000) | (optional) defaults to undefined|
| **mode** | [**string**] | paginated | full | csv | (optional) defaults to undefined|
| **offset** | [**number**] | Pagination offset | (optional) defaults to undefined|
| **paymentStatus** | [**string**] | Filter by status: draft,open,sent,partial,paid,uncollectible | (optional) defaults to undefined|
| **pivotFields** | [**string**] | Column dimensions: product_id, client_id, etc. | (optional) defaults to undefined|
| **productId** | [**string**] | Filter by product ID(s) | (optional) defaults to undefined|
| **shouldPivot** | [**boolean**] | Enable pivot columns | (optional) defaults to undefined|
| **startDate** | [**string**] | Start date (YYYY-MM-DD) | (optional) defaults to undefined|


### Return type

**InvoiceReportResponse**

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

# **coaApiV1InvoiceReportPreviewRetrieve**
> InvoiceReportResponse coaApiV1InvoiceReportPreviewRetrieve()

Execute invoice report preview from query params.  :param request: HTTP request with report configuration :return: Paginated response or CSV stream

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let aggregationFields: string; //Aggregates: sum:amount, sum:amount_paid, sum:amount_due, etc. (optional) (default to undefined)
let clientId: string; //Filter by client ID(s) (optional) (default to undefined)
let contractId: string; //Filter by contract ID(s) (optional) (default to undefined)
let currency: string; //Filter by currency code (optional) (default to undefined)
let departmentId: string; //Filter by department ID(s) (optional) (default to undefined)
let endDate: string; //End date (YYYY-MM-DD) (optional) (default to undefined)
let entityId: string; //Entity ID(s), comma-separated (optional) (default to undefined)
let groupFields: string; //Row dimensions: client_id, invoice_id, invoice_date_month, product_id, etc. (optional) (default to undefined)
let groupKeys: string; //Drilldown parent keys (optional) (default to undefined)
let includeTotals: boolean; //Include grand totals row (optional) (default to undefined)
let limit: number; //Page size (max 10000) (optional) (default to undefined)
let mode: string; //paginated | full | csv (optional) (default to undefined)
let offset: number; //Pagination offset (optional) (default to undefined)
let paymentStatus: string; //Filter by status: draft,open,sent,partial,paid,uncollectible (optional) (default to undefined)
let pivotFields: string; //Column dimensions: product_id, client_id, etc. (optional) (default to undefined)
let productId: string; //Filter by product ID(s) (optional) (default to undefined)
let shouldPivot: boolean; //Enable pivot columns (optional) (default to undefined)
let startDate: string; //Start date (YYYY-MM-DD) (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiV1InvoiceReportPreviewRetrieve(
    aggregationFields,
    clientId,
    contractId,
    currency,
    departmentId,
    endDate,
    entityId,
    groupFields,
    groupKeys,
    includeTotals,
    limit,
    mode,
    offset,
    paymentStatus,
    pivotFields,
    productId,
    shouldPivot,
    startDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **aggregationFields** | [**string**] | Aggregates: sum:amount, sum:amount_paid, sum:amount_due, etc. | (optional) defaults to undefined|
| **clientId** | [**string**] | Filter by client ID(s) | (optional) defaults to undefined|
| **contractId** | [**string**] | Filter by contract ID(s) | (optional) defaults to undefined|
| **currency** | [**string**] | Filter by currency code | (optional) defaults to undefined|
| **departmentId** | [**string**] | Filter by department ID(s) | (optional) defaults to undefined|
| **endDate** | [**string**] | End date (YYYY-MM-DD) | (optional) defaults to undefined|
| **entityId** | [**string**] | Entity ID(s), comma-separated | (optional) defaults to undefined|
| **groupFields** | [**string**] | Row dimensions: client_id, invoice_id, invoice_date_month, product_id, etc. | (optional) defaults to undefined|
| **groupKeys** | [**string**] | Drilldown parent keys | (optional) defaults to undefined|
| **includeTotals** | [**boolean**] | Include grand totals row | (optional) defaults to undefined|
| **limit** | [**number**] | Page size (max 10000) | (optional) defaults to undefined|
| **mode** | [**string**] | paginated | full | csv | (optional) defaults to undefined|
| **offset** | [**number**] | Pagination offset | (optional) defaults to undefined|
| **paymentStatus** | [**string**] | Filter by status: draft,open,sent,partial,paid,uncollectible | (optional) defaults to undefined|
| **pivotFields** | [**string**] | Column dimensions: product_id, client_id, etc. | (optional) defaults to undefined|
| **productId** | [**string**] | Filter by product ID(s) | (optional) defaults to undefined|
| **shouldPivot** | [**boolean**] | Enable pivot columns | (optional) defaults to undefined|
| **startDate** | [**string**] | Start date (YYYY-MM-DD) | (optional) defaults to undefined|


### Return type

**InvoiceReportResponse**

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

# **coaApiV1InvoiceRetrieve**
> AccountingInvoice coaApiV1InvoiceRetrieve()

         Retrieves a single accounting invoice with complete details including line items, payments, and accounting relationships.          This endpoint provides comprehensive invoice information with:         - Complete invoice metadata (dates, amounts, status, terms)         - All associated line items with product details and tax information         - Payment history with journal entry references and transaction details         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1InvoiceRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**AccountingInvoice**

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

# **coaApiV1InvoiceStatsRetrieve**
> { [key: string]: any; } coaApiV1InvoiceStatsRetrieve()

Customer-scoped counts and outstanding amounts for the Invoices page Open / Sent / Overdue stat cards.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

const { status, data } = await apiInstance.coaApiV1InvoiceStatsRetrieve();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**{ [key: string]: any; }**

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

# **coaApiV1InvoiceUpdate**
> AccountingInvoice coaApiV1InvoiceUpdate(accountingInvoice)

         Performs a complete update of an existing accounting invoice using PUT semantics.          This endpoint allows full replacement of invoice data including:         - Complete invoice metadata update (dates, amounts, terms, client, entity)         - Full line item replacement with new products, quantities, rates, and tax calculations         - Journal entry recalculation and update with new accounting transactions         - Exchange rate updates for multi-currency invoices          **Important Notes:**         - This is a full replacement operation - all invoice data will be updated         - Missing fields in the request will be set to null or default values         - Existing line items will be completely replaced with the new line items         - Journal entries will be updated to reflect all changes         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    AccountingInvoice
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)
let accountingInvoice: AccountingInvoice; //

const { status, data } = await apiInstance.coaApiV1InvoiceUpdate(
    id,
    accountingInvoice
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **accountingInvoice** | **AccountingInvoice**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**AccountingInvoice**

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

# **coaApiV1InvoiceVoidCreate**
> AccountingInvoice coaApiV1InvoiceVoidCreate()

Void an existing invoice.          This creates a reversing journal entry to void the invoice by reversing all debit and credit amounts.         The invoice status will be updated to reflect the void.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    VoidInvoiceRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let invoiceId: number; //ID of the invoice to void (default to undefined)
let voidInvoiceRequest: VoidInvoiceRequest; // (optional)

const { status, data } = await apiInstance.coaApiV1InvoiceVoidCreate(
    invoiceId,
    voidInvoiceRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **voidInvoiceRequest** | **VoidInvoiceRequest**|  | |
| **invoiceId** | [**number**] | ID of the invoice to void | defaults to undefined|


### Return type

**AccountingInvoice**

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

# **createProduct**
> Product createProduct(product)

Create a new product

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    Product
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let product: Product; //

const { status, data } = await apiInstance.createProduct(
    product
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **product** | **Product**|  | |


### Return type

**Product**

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

# **getClientInvoiceStatementPdf**
> getClientInvoiceStatementPdf()

Generate a customer statement PDF for a specific client.  This creates a professional, customer-facing statement showing: - All outstanding invoices as of the specified date - Running balance - Total balance due - Payment advice slip

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let clientId: number; // (default to undefined)

const { status, data } = await apiInstance.getClientInvoiceStatementPdf(
    clientId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **clientId** | [**number**] |  | defaults to undefined|


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
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getCreditMemoPdf**
> getCreditMemoPdf()


### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.getCreditMemoPdf(
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
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listProducts**
> PaginatedProductList listProducts()

         Retrieve a list of contract products with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listProducts(
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

**PaginatedProductList**

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

# **rrApiV1ProductBulkSearchCreate**
> BulkProductSearchResponse rrApiV1ProductBulkSearchCreate(bulkProductSearch)

Resolve many product cells in a single request. Each term is matched against product_id, display_name, product_uuid, id, then product_name, in that order. A term matching more than one product is returned in the ambiguous list instead of being resolved.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    BulkProductSearch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let bulkProductSearch: BulkProductSearch; //

const { status, data } = await apiInstance.rrApiV1ProductBulkSearchCreate(
    bulkProductSearch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulkProductSearch** | **BulkProductSearch**|  | |


### Return type

**BulkProductSearchResponse**

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

# **rrApiV1ProductDeleteCreate**
> rrApiV1ProductDeleteCreate()

Delete a product.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    DeleteRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)
let deleteRequest: DeleteRequest; // (optional)

const { status, data } = await apiInstance.rrApiV1ProductDeleteCreate(
    id,
    deleteRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **deleteRequest** | **DeleteRequest**|  | |
| **id** | [**number**] |  | defaults to undefined|


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

# **rrApiV1ProductDestroy**
> rrApiV1ProductDestroy()

Deprecated: use `POST /rr/api/v1/product/{id}/delete`, which also takes an optional reason for the audit log.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ProductDestroy(
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
|**204** | Deleted. |  -  |
|**202** | Sent for approval; the record is deleted once a reviewer approves. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rrApiV1ProductPartialUpdate**
> Product rrApiV1ProductPartialUpdate()


### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    PatchedProduct
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)
let patchedProduct: PatchedProduct; // (optional)

const { status, data } = await apiInstance.rrApiV1ProductPartialUpdate(
    id,
    patchedProduct
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedProduct** | **PatchedProduct**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Product**

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

# **rrApiV1ProductRetrieve**
> Product rrApiV1ProductRetrieve()


### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ProductRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Product**

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

# **rrApiV1ProductUpdate**
> Product rrApiV1ProductUpdate(product)


### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration,
    Product
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)
let product: Product; //

const { status, data } = await apiInstance.rrApiV1ProductUpdate(
    id,
    product
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **product** | **Product**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Product**

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

# **sendCreditMemo**
> sendCreditMemo()

Send a single credit memo via email.

### Example

```typescript
import {
    AccountsReceivableApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new AccountsReceivableApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.sendCreditMemo(
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
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


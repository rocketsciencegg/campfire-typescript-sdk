# CoreAccountingApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**bulkUpdateChartTransactions**](#bulkupdatecharttransactions) | **POST** /coa/api/transaction/bulk-update | Bulk Update Chart Transactions|
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
|[**coaApiFixedAssetAutomationDeleteCreate**](#coaapifixedassetautomationdeletecreate) | **POST** /coa/api/fixed-asset-automation/{id}/delete | Delete Fixed Asset Automation|
|[**coaApiFixedAssetCreate**](#coaapifixedassetcreate) | **POST** /coa/api/fixed-asset | Create Fixed Asset|
|[**coaApiFixedAssetDestroy**](#coaapifixedassetdestroy) | **DELETE** /coa/api/fixed-asset/{id} | Delete Fixed Asset|
|[**coaApiFixedAssetList**](#coaapifixedassetlist) | **GET** /coa/api/fixed-asset | List Fixed Assets|
|[**coaApiFixedAssetPartialUpdate**](#coaapifixedassetpartialupdate) | **PATCH** /coa/api/fixed-asset/{id} | Partial Update Fixed Asset|
|[**coaApiFixedAssetRetrieve**](#coaapifixedassetretrieve) | **GET** /coa/api/fixed-asset/{id} | Retrieve Fixed Asset|
|[**coaApiFixedAssetUpdate**](#coaapifixedassetupdate) | **PUT** /coa/api/fixed-asset/{id} | Update Fixed Asset|
|[**coaApiIntercompanyJournalEntryBalanceCreate**](#coaapiintercompanyjournalentrybalancecreate) | **POST** /coa/api/intercompany-journal-entry/balance | Balance Intercompany Journal Entry|
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
|[**coaApiTransactionList**](#coaapitransactionlist) | **GET** /coa/api/transaction | List Chart Transactions|
|[**coaApiTransactionMatchesBulkAcceptCreate**](#coaapitransactionmatchesbulkacceptcreate) | **POST** /coa/api/transaction-matches/bulk-accept | Bulk Accept Suggestions|
|[**coaApiTransactionPartialUpdate**](#coaapitransactionpartialupdate) | **PATCH** /coa/api/transaction/{id} | Partial Update Chart Transaction|
|[**coaApiTransactionRetrieve**](#coaapitransactionretrieve) | **GET** /coa/api/transaction/{id} | Retrieve Chart Transaction|
|[**coaApiTransactionUpdate**](#coaapitransactionupdate) | **PUT** /coa/api/transaction/{id} | Update Chart Transaction|
|[**coaApiVendorBulkSearchCreate**](#coaapivendorbulksearchcreate) | **POST** /coa/api/vendor/bulk-search | Bulk Search Vendors by External ID or Name|
|[**coaApiVendorContactDestroy**](#coaapivendorcontactdestroy) | **DELETE** /coa/api/vendor-contact/{id} | Delete Vendor Contact|
|[**coaApiVendorContactPartialUpdate**](#coaapivendorcontactpartialupdate) | **PATCH** /coa/api/vendor-contact/{id} | Partial Update Vendor Contact|
|[**coaApiVendorContactRetrieve**](#coaapivendorcontactretrieve) | **GET** /coa/api/vendor-contact/{id} | Retrieve Vendor Contact|
|[**coaApiVendorContactUpdate**](#coaapivendorcontactupdate) | **PUT** /coa/api/vendor-contact/{id} | Update Vendor Contact|
|[**coaApiVendorContactsCreate**](#coaapivendorcontactscreate) | **POST** /coa/api/vendor/{id}/contacts | Create Vendor Contact|
|[**coaApiVendorContactsList**](#coaapivendorcontactslist) | **GET** /coa/api/vendor/{id}/contacts | List Vendor Contacts|
|[**createFixedAssetAutomation**](#createfixedassetautomation) | **POST** /coa/api/fixed-asset-automation | Create Fixed Asset Automation|
|[**createTransactionBillPayments**](#createtransactionbillpayments) | **POST** /coa/api/transaction/{transaction_id}/bill_payments | Create Bill Payments for Transaction|
|[**createTransactionCreditMemoPayments**](#createtransactioncreditmemopayments) | **POST** /coa/api/transaction/{transaction_id}/credit_memo_payments | Create Credit Memo Payments for Transaction|
|[**createTransactionDebitMemoPayments**](#createtransactiondebitmemopayments) | **POST** /coa/api/transaction/{transaction_id}/debit_memo_payments | Create Debit Memo Payments for Transaction|
|[**createTransactionInvoicePayments**](#createtransactioninvoicepayments) | **POST** /coa/api/transaction/{transaction_id}/invoice_payments | Create Invoice Payments for Transaction|
|[**deleteChartTransaction**](#deletecharttransaction) | **DELETE** /coa/api/transaction/{id} | Delete Chart Transaction|
|[**deleteFixedAssetAutomation**](#deletefixedassetautomation) | **DELETE** /coa/api/fixed-asset-automation/{id} | Delete Fixed Asset Automation (deprecated)|
|[**deleteTransactionMatch**](#deletetransactionmatch) | **DELETE** /coa/api/transaction-matches/{id} | Delete Transaction Match|
|[**discoverTransactionMatchCandidates**](#discovertransactionmatchcandidates) | **GET** /coa/api/transaction-matches/candidates | Discover bill or invoice match candidates for a bank transaction|
|[**getChartTransactionTotals**](#getcharttransactiontotals) | **GET** /coa/api/transaction/totals | Get Chart Transaction Totals|
|[**getFixedAssetAutomation**](#getfixedassetautomation) | **GET** /coa/api/fixed-asset-automation/{id} | Retrieve Fixed Asset Automation|
|[**getFixedAssetAutomationMatch**](#getfixedassetautomationmatch) | **GET** /coa/api/fixed-asset-automation-match/{id} | Retrieve Fixed Asset Automation Match|
|[**getTransactionMatch**](#gettransactionmatch) | **GET** /coa/api/transaction-matches/{id} | Retrieve Transaction Match|
|[**getTransactionMatchesCount**](#gettransactionmatchescount) | **GET** /coa/api/transaction-matches-count | Get Transaction Matches Count|
|[**listFixedAssetAutomationAccounts**](#listfixedassetautomationaccounts) | **GET** /coa/api/fixed-asset-automation/accounts | List Fixed Asset Automation Accounts|
|[**listFixedAssetAutomationAssetClasses**](#listfixedassetautomationassetclasses) | **GET** /coa/api/fixed-asset-automation/asset-classes | List Fixed Asset Automation Asset Classes|
|[**listFixedAssetAutomationMatches**](#listfixedassetautomationmatches) | **GET** /coa/api/fixed-asset-automation/matches | List Fixed Asset Automation Matches|
|[**listFixedAssetAutomations**](#listfixedassetautomations) | **GET** /coa/api/fixed-asset-automation | List Fixed Asset Automations|
|[**listFixedAssetReconciliationUnmatchedGl**](#listfixedassetreconciliationunmatchedgl) | **GET** /coa/api/fixed-asset/reconciliation/unmatched-gl | List Unmatched GL Transactions for Fixed Asset Reconciliation|
|[**listTransactionMatches**](#listtransactionmatches) | **GET** /coa/api/transaction-matches | List Transaction Matches|
|[**mergeChartTransactions**](#mergecharttransactions) | **POST** /coa/api/transaction/merge | Merge Chart Transactions|
|[**partialUpdateFixedAssetAutomation**](#partialupdatefixedassetautomation) | **PATCH** /coa/api/fixed-asset-automation/{id} | Partial Update Fixed Asset Automation|
|[**partialUpdateFixedAssetAutomationMatch**](#partialupdatefixedassetautomationmatch) | **PATCH** /coa/api/fixed-asset-automation-match/{id} | Partial Update Fixed Asset Automation Match|
|[**partialUpdateTransactionMatch**](#partialupdatetransactionmatch) | **PATCH** /coa/api/transaction-matches/{id} | Partial Update Transaction Match|
|[**previewChartTransactionMerge**](#previewcharttransactionmerge) | **GET** /coa/api/transaction/merge | Preview Chart Transaction Merge|
|[**processTransactionMatch**](#processtransactionmatch) | **POST** /coa/api/transaction-match-process | Process Transaction Match|
|[**proposeTransactionGlCoding**](#proposetransactionglcoding) | **POST** /coa/api/transaction-gl-codings/propose | Create a pending GL coding suggestion|
|[**proposeTransactionMatches**](#proposetransactionmatches) | **POST** /coa/api/transaction-matches/propose | Create pending transaction matches|
|[**proposeTransactionMerge**](#proposetransactionmerge) | **POST** /coa/api/transaction-merges/propose | Create a pending transaction merge|
|[**rejectTransactionMatch**](#rejecttransactionmatch) | **POST** /coa/api/transaction-matches/{id}/reject | Reject Transaction Match|
|[**runFixedAssetAutomation**](#runfixedassetautomation) | **POST** /coa/api/fixed-asset-automation/run | Run Fixed Asset Automation|
|[**setTransactionMatchStatus**](#settransactionmatchstatus) | **POST** /coa/api/transaction-matches/{id}/status | Set Transaction Match Status|
|[**updateFixedAssetAutomation**](#updatefixedassetautomation) | **PUT** /coa/api/fixed-asset-automation/{id} | Update Fixed Asset Automation|
|[**updateFixedAssetAutomationMatch**](#updatefixedassetautomationmatch) | **PUT** /coa/api/fixed-asset-automation-match/{id} | Update Fixed Asset Automation Match|
|[**updateTransactionMatch**](#updatetransactionmatch) | **PUT** /coa/api/transaction-matches/{id} | Update Transaction Match|
|[**updateTransactionMatchStatus**](#updatetransactionmatchstatus) | **PUT** /coa/api/transaction-matches/{id}/status | Update Transaction Match Status|

# **bulkUpdateChartTransactions**
> bulkUpdateChartTransactions()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

const { status, data } = await apiInstance.bulkUpdateChartTransactions();
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

# **coaApiBudgetsAccountsCreate**
> BudgetAccount coaApiBudgetsAccountsCreate(budgetAccount)

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
let budgetAccount: BudgetAccount; //

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiBudgetsAccountsUpdate**
> BudgetAccount coaApiBudgetsAccountsUpdate(budgetAccount)


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
let budgetAccount: BudgetAccount; //

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetAutomationDeleteCreate**
> coaApiFixedAssetAutomationDeleteCreate()

Delete a fixed asset automation. Replaces the deprecated DELETE /coa/api/fixed-asset-automation/{id}/.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    DeleteRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let deleteRequest: DeleteRequest; // (optional)

const { status, data } = await apiInstance.coaApiFixedAssetAutomationDeleteCreate(
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

# **coaApiFixedAssetCreate**
> FixedAsset coaApiFixedAssetCreate(fixedAsset)

Wraps ``CreateModelMixin.create`` (or any method named ``create``) with ``Idempotency-Key`` handling.  Place this mixin **before** the view\'s other base classes so its ``create`` overrides the inherited one::      class JournalEntryListCreate(         IdempotentCreateMixin,         HistoryFilteringMixin,         ListCreateAPIView,     ):         ...

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

No authorization required

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiIntercompanyJournalEntryBalanceCreate**
> coaApiIntercompanyJournalEntryBalanceCreate(coaApiIntercompanyJournalEntryBalanceCreateRequest)

         Balances an intercompany journal entry by entity and currency.          This endpoint performs the same balancing logic as the frontend, applying:         1. Auto-fetching of exchange rates if not provided (requires date field)         2. Exchange rate roll-forward from native to book to consolidation currencies         3. Exchange rate plugging to ensure consolidation amounts match across currencies within an entity         4. Automatic creation of balancing transactions when debits != credits at any currency level          The endpoint accepts a partial intercompany journal entry with transactions and optionally exchange rates,         and returns the balanced version with:         - Auto-fetched exchange rates (if exchange_rates is empty and date is provided)         - Updated transactions with calculated book and consolidation amounts         - New balancing transactions added where needed         - Plugged exchange rates to maintain consolidation consistency          This is useful for:         - Validating journal entries before submission         - Understanding what balancing entries will be created         - Testing multi-currency and multi-entity scenarios         - Auto-fetching exchange rates for the journal date         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    CoaApiIntercompanyJournalEntryBalanceCreateRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let coaApiIntercompanyJournalEntryBalanceCreateRequest: CoaApiIntercompanyJournalEntryBalanceCreateRequest; //

const { status, data } = await apiInstance.coaApiIntercompanyJournalEntryBalanceCreate(
    coaApiIntercompanyJournalEntryBalanceCreateRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **coaApiIntercompanyJournalEntryBalanceCreateRequest** | **CoaApiIntercompanyJournalEntryBalanceCreateRequest**|  | |


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiIntercompanyJournalEntryCreate**
> IntercompanyJournalEntry coaApiIntercompanyJournalEntryCreate(intercompanyJournalEntry)

         Creates a new intercompany journal entry          This endpoint allows for complex multi-entity transactions where:         - Transactions are balanced across different entities         - Exchange rates are handled for multi-currency transactions          Key requirements:         - Total debits must equal total credits for each entity (debit_amount_native must equal credit_amount_native)         - Cannot create entries before closed book dates         - All referenced accounts must be active         - Exchange rates must be provided for all currency conversions (native to book, book to consolidation)         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    IntercompanyJournalEntry
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let intercompanyJournalEntry: IntercompanyJournalEntry; //

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

No authorization required

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

No authorization required

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

         Retrieves a paginated list of intercompany journal entries for the authenticated user\'s customer.          This endpoint returns:         - Summary information for each intercompany journal entry         - Basic transaction details (simplified view for list performance)         - Entity and exchange rate information         - Pagination metadata (count, next, previous)         - Reversal relationships and attachment counts          The response includes:         - Intercompany journal entry metadata         - Associated transaction summaries         - Exchange rate information for currency conversions         - Links to related reversals         - Attachment information          Results can be sorted using the \'sort\' query parameter with field names like \'date\', \'id\', etc.         Prefix with \'-\' for descending order (e.g., \'-date\').         

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiIntercompanyJournalEntryRetrieve**
> IntercompanyJournalEntry coaApiIntercompanyJournalEntryRetrieve()

         Retrieves a single intercompany journal entry by its ID with complete details.          This endpoint returns:         - Complete intercompany journal entry information         - Full transaction details with all accounting fields         - Entity information and exchange rates         - Attachment and reversal information         - Comprehensive transaction metadata          The response includes:         - All transaction details with account information         - Exchange rate data for all currency conversions (native to book, book to consolidation)         - Vendor, department, and tag information         - Balance calculations and transaction history         - File attachments and reversal relationships         - Complete audit trail information          This is the detailed view used for editing and complete transaction analysis.         

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiIntercompanyJournalEntryUpdate**
> IntercompanyJournalEntry coaApiIntercompanyJournalEntryUpdate(intercompanyJournalEntry)

         Updates an existing intercompany journal entry with new transaction details.          This endpoint allows for:         - Modifying transaction amounts and details         - Updating entity assignments and exchange rates         - Changing account assignments and categorizations         - Updating vendor, department, and tag information         - Maintaining balance validation across all entities          Key requirements:         - Total debits must equal total credits for each entity         - All account balances must be valid in all currencies         - Cannot modify entries in closed periods         - All referenced accounts must be active         - Existing transactions are replaced with new transaction set         - Exchange rates must be provided for all currency conversions          The update process atomically replaces all transactions while preserving the journal entry ID and audit trail.         

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
let intercompanyJournalEntry: IntercompanyJournalEntry; //

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiJournalEntryCreate**
> JournalEntry coaApiJournalEntryCreate(journalEntryWrite)

         Create a new journal entry with transactions. Journal entries must balance - total debits must equal total credits.          **Key Features:**         - Automatic currency conversion using exchange rates         - Vendor, Department and Custom Dimension assignment         - Optional reversal date for automatic reversal entries         - Validation against closed book periods          **Validation Rules:**         - Debits must equal credits in transaction currency (debit_native and credit_native)         - Cannot create entries before closed book dates         - Accounts must be active         - Exchange rates are auto-calculated if not provided         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    JournalEntryWrite
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let journalEntryWrite: JournalEntryWrite; //

const { status, data } = await apiInstance.coaApiJournalEntryCreate(
    journalEntryWrite
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **journalEntryWrite** | **JournalEntryWrite**|  | |


### Return type

**JournalEntry**

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |
|**400** | Books are closed for this date |  -  |
|**409** | Journal entry is associated with other objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiJournalEntryList**
> PaginatedJournalEntryList coaApiJournalEntryList()

         Retrieve a paginated list of journal entries with optional filtering and sorting.          **Query Parameters:**         - `start_date`, `end_date`: Filter by date range (defaults to last 6 months)         - `account`: Filter by account ID(s) - supports multiple values         - `source`: Filter by journal entry source. Payroll auto-sync sources           (`rippling_payroll_auto`, `finch_payroll_auto`, `deel_payroll_auto`, `adp_workforce_now_payroll_auto`) are exempt from the default           window, since they page on `last_modified_at` and re-post back-dated corrections.         - `journal_id`: Filter by specific journal ID         - `all_time`: Include all entries regardless of date (true/false)         - `sort`: Sort field (default: \"date\")          **Response includes:**         - Complete journal entry details with all transactions         - Account information with names and numbers         - Vendor and department details         - Tag associations with groups         - Attachment information         - Exchange rate data for multi-currency entries         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let account: string; //Filter by account ID(s). Can specify multiple values. (optional) (default to undefined)
let allTime: boolean; //Return entries across the full history instead of the default 6-month window. Ignored when both start_date and end_date are supplied. (optional) (default to false)
let endDate: string; //End date, YYYY-MM-DD. Omit both dates and the range defaults to the last 6 months; pass all_time=true for the full history. (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let source: string; //Filter by journal entry source (e.g., \'manual\', \'CSV Upload\') (optional) (default to undefined)
let startDate: string; //Start date, YYYY-MM-DD. Omit both dates and the range defaults to the last 6 months; pass all_time=true for the full history. (optional) (default to undefined)

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
| **allTime** | [**boolean**] | Return entries across the full history instead of the default 6-month window. Ignored when both start_date and end_date are supplied. | (optional) defaults to false|
| **endDate** | [**string**] | End date, YYYY-MM-DD. Omit both dates and the range defaults to the last 6 months; pass all_time&#x3D;true for the full history. | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **source** | [**string**] | Filter by journal entry source (e.g., \&#39;manual\&#39;, \&#39;CSV Upload\&#39;) | (optional) defaults to undefined|
| **startDate** | [**string**] | Start date, YYYY-MM-DD. Omit both dates and the range defaults to the last 6 months; pass all_time&#x3D;true for the full history. | (optional) defaults to undefined|


### Return type

**PaginatedJournalEntryList**

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

# **coaApiJournalEntryPartialUpdate**
> JournalEntry coaApiJournalEntryPartialUpdate()

         Partially update a journal entry. Only provided fields will be updated.          **Common Use Cases:**         - Update memo or reference number         - Change journal entry date         - Modify specific transaction amounts         - Add or remove tags from transactions          **Validation Rules:**         - Journal entry must still balance after updates         - Cannot modify entries in closed periods         - Account changes must maintain chart of accounts rules         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    PatchedJournalEntryWrite
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let patchedJournalEntryWrite: PatchedJournalEntryWrite; // (optional)

const { status, data } = await apiInstance.coaApiJournalEntryPartialUpdate(
    id,
    patchedJournalEntryWrite
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedJournalEntryWrite** | **PatchedJournalEntryWrite**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**JournalEntry**

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiJournalEntryUpdate**
> JournalEntry coaApiJournalEntryUpdate(journalEntryWrite)

         Update a journal entry completely. All transactions will be replaced with the new ones provided.          **Important Notes:**         - Cannot update entries before closed book dates         - Must maintain double-entry bookkeeping (debits = credits)         - All existing transactions will be replaced         - Exchange rates will be recalculated if not provided          **Validation Rules:**         - Journal entry must balance in all currencies         - Accounts must be active         - Cannot modify entries in closed periods         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    JournalEntryWrite
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let journalEntryWrite: JournalEntryWrite; //

const { status, data } = await apiInstance.coaApiJournalEntryUpdate(
    id,
    journalEntryWrite
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **journalEntryWrite** | **JournalEntryWrite**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**JournalEntry**

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTransactionList**
> PaginatedChartTransactionList coaApiTransactionList()

Lists general-ledger transactions (`ChartTransaction` records) - Campfire\'s GL transaction log, and the recommended endpoint for retrieving GL transaction data.  Each transaction carries account, department, vendor, entity, journal/date metadata, and tags (where applicable). Product metadata is not stored directly on a transaction; it is reached through relations with other Campfire objects.  **Date range:** filter with `start_date` and `end_date` (both `YYYY-MM-DD`, inclusive); `date_from` and `date_to` are aliases, and `start_date`/`end_date` win when both are sent. The bounds match on transaction date (the journal entry date, which `posted_at` mirrors).  **Pagination:** results are paginated via `limit` (default 100, max 10000) and `offset`. To retrieve more than 10000 records, page through with `offset`, or use cursor pagination by passing an empty `cursor=` parameter and following the `next` link.  **Key response fields:** - `amount` - amount in consolidated currency (the root entity\'s currency). - `amount_book` - amount in the currency of the entity the transaction belongs to. - `amount_native` - amount in the currency the transaction was originally created in. Example: for a transaction made in GBP where the entity uses EUR and the root entity uses USD, `amount_native` is GBP, `amount_book` is EUR, and `amount` is USD. - `posted_at` - the transaction date; determines which period the transaction falls in. `date_year` and `date_month` are derived from it. - `vendor` / `vendor_name` - the linked Campfire `Vendor` object\'s ID and name. - `merchant_name` - a free-text field stored directly on the transaction; not linked to any Campfire object. - `account` - the Campfire `ChartAccount` (GL account) the transaction is posted to. - `entity` - the Campfire `ChartEntity` ID. - `tags` - the transaction\'s tags; each tag\'s `group`/`group_name` identify the tag group (dimension) it belongs to. List a customer\'s tag groups via `/coa/api/tag-group` and tags via `/coa/api/tag`.  **Dynamic tag-group columns:** in addition to `tags`, each row carries flattened per-dimension columns `tag_group_<id>` (tag ID) and `tag_group_<id>_name` (tag name), one pair per tag group defined by the customer, plus `tag_group_none` / `tag_group_none_name` for ungrouped tags. Journal-level custom fields are merged in as `custom_field_<name>` keys. These columns are customer-specific, so they cannot appear in this static schema - discover tag groups via `/coa/api/tag-group` and custom fields via `/ca/api/v1/custom-fields`.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let account: number; // (optional) (default to undefined)
let accountId: number; // (optional) (default to undefined)
let accountRollup: boolean; // (optional) (default to false)
let accountSubtype: string; // (optional) (default to undefined)
let accountType: string; // (optional) (default to undefined)
let accounts: number; // (optional) (default to undefined)
let aggregationFields: string; //Comma-separated aggregations, e.g. sum:amount,count:id (optional) (default to undefined)
let allTime: boolean; //If true, uses full transaction date range for the customer; start_date and end_date are ignored (optional) (default to false)
let bank: number; // (optional) (default to undefined)
let bankDescription: string; // (optional) (default to undefined)
let bankId: number; // (optional) (default to undefined)
let categorized: string; //Filter by categorization state (true/false) (optional) (default to undefined)
let counterparty: number; //Intercompany counterparty entity id; matches lines whose balance is against that entity (optional) (default to undefined)
let counterpartyId: number; //Alias of counterparty; do not combine the two (optional) (default to undefined)
let creditAmountEqual: number; // (optional) (default to undefined)
let creditAmountGte: number; // (optional) (default to undefined)
let creditAmountLte: number; // (optional) (default to undefined)
let creditAmountNull: boolean; // (optional) (default to false)
let currency: string; // (optional) (default to undefined)
let dateFrom: string; //Alias of `start_date`; `start_date` wins when both are sent (optional) (default to undefined)
let dateTo: string; //Alias of `end_date`; `end_date` wins when both are sent (optional) (default to undefined)
let debitAmountEqual: number; // (optional) (default to undefined)
let debitAmountGte: number; // (optional) (default to undefined)
let debitAmountLte: number; // (optional) (default to undefined)
let debitAmountNull: boolean; // (optional) (default to false)
let department: number; // (optional) (default to undefined)
let departmentId: number; // (optional) (default to undefined)
let departmentOrUnassigned: boolean; // (optional) (default to false)
let download: boolean; //If true, dispatch async CSV/Excel email export instead of returning rows (optional) (default to false)
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to end of current month (optional) (default to undefined)
let entity: number; // (optional) (default to undefined)
let entityId: number; // (optional) (default to undefined)
let entityRollup: boolean; // (optional) (default to false)
let excludeEntity: number; // (optional) (default to undefined)
let excludeEntityId: number; // (optional) (default to undefined)
let excludeId: number; // (optional) (default to undefined)
let excludeJournal: number; // (optional) (default to undefined)
let excludeReconciliationReport: number; // (optional) (default to undefined)
let excludeUncategorizedAccounts: boolean; // (optional) (default to false)
let expenseOrAp: boolean; // (optional) (default to undefined)
let fields: string; //Comma-separated list of columns to return, e.g. \'posted_at,debit_amount,account\'. Omit to receive the full payload. \'id\' is always included. Narrowing the column list also skips the derived values behind the omitted columns, so it is the recommended way to pull large pages: a 1000-row page returns roughly 90% less data and responds materially faster when only a few columns are needed. Unrecognized names are ignored. (optional) (default to undefined)
let group: number; // (optional) (default to undefined)
let groupFields: string; //Comma-separated list of fields to group by (e.g. account,vendor,tag_group_<id>) (optional) (default to undefined)
let groupId: number; // (optional) (default to undefined)
let groupKeys: string; //Comma-separated values matched positionally to group_fields for drill-down (optional) (default to undefined)
let hasLinkedFixedAsset: string; // (optional) (default to undefined)
let hasParentBankTransaction: string; // (optional) (default to undefined)
let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let includeMatches: boolean; //If true, include match metadata (has_matches, primary_action_type) in serialized rows (optional) (default to false)
let isNotReconciled: boolean; // (optional) (default to false)
let isReconciled: boolean; // (optional) (default to false)
let journal: number; //Only transactions on these journal entry ids (repeat the param for several) (optional) (default to undefined)
let journalType: string; // (optional) (default to undefined)
let journalTypeNin: string; // (optional) (default to undefined)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Maximum number of records to return per page. Default 100, maximum 10000. Use with offset to paginate (optional) (default to 100)
let matchType: 'all' | 'any'; // (optional) (default to 'all')
let needsReview: boolean; // (optional) (default to false)
let noCounterparty: boolean; //If true, only lines with no intercompany counterparty (optional) (default to undefined)
let noDepartment: boolean; // (optional) (default to undefined)
let noTag: boolean; // (optional) (default to undefined)
let noVendor: boolean; // (optional) (default to undefined)
let offset: number; //Number of records to skip before collecting the result page. Use with limit to paginate (optional) (default to 0)
let opposingAccount: number; // (optional) (default to undefined)
let opposingAccountSubtype: string; // (optional) (default to undefined)
let ordering: string; // (optional) (default to undefined)
let payee: string; //Integer payee id or Campfire ID (VEN-/CUST-/EMP-) (optional) (default to undefined)
let payeeId: string; //Integer payee id or Campfire ID (VEN-/CUST-/EMP-) (optional) (default to undefined)
let pivotFields: string; //Comma-separated list of pivot dimensions (optional) (default to undefined)
let q: string; //Free-text search across journal memo, bank description, and related fields (optional) (default to undefined)
let reconciliationReport: number; // (optional) (default to undefined)
let revenueOrReceivables: boolean; // (optional) (default to undefined)
let shouldPivot: boolean; // (optional) (default to false)
let sort: string; //Sort field; prefix with - for descending. Default: -posted_at (optional) (default to undefined)
let startDate: string; //Earliest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)
let tag: number; // (optional) (default to undefined)
let tagGroups: number; // (optional) (default to undefined)
let tagId: number; // (optional) (default to undefined)
let vendor: string; //Integer payee id or Campfire ID (VEN-/CUST-/EMP-) (optional) (default to undefined)
let vendorId: string; //Integer payee id or Campfire ID (VEN-/CUST-/EMP-) (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionList(
    account,
    accountId,
    accountRollup,
    accountSubtype,
    accountType,
    accounts,
    aggregationFields,
    allTime,
    bank,
    bankDescription,
    bankId,
    categorized,
    counterparty,
    counterpartyId,
    creditAmountEqual,
    creditAmountGte,
    creditAmountLte,
    creditAmountNull,
    currency,
    dateFrom,
    dateTo,
    debitAmountEqual,
    debitAmountGte,
    debitAmountLte,
    debitAmountNull,
    department,
    departmentId,
    departmentOrUnassigned,
    download,
    endDate,
    entity,
    entityId,
    entityRollup,
    excludeEntity,
    excludeEntityId,
    excludeId,
    excludeJournal,
    excludeReconciliationReport,
    excludeUncategorizedAccounts,
    expenseOrAp,
    fields,
    group,
    groupFields,
    groupId,
    groupKeys,
    hasLinkedFixedAsset,
    hasParentBankTransaction,
    includeDeleted,
    includeMatches,
    isNotReconciled,
    isReconciled,
    journal,
    journalType,
    journalTypeNin,
    lastModifiedAtGte,
    lastModifiedAtLte,
    limit,
    matchType,
    needsReview,
    noCounterparty,
    noDepartment,
    noTag,
    noVendor,
    offset,
    opposingAccount,
    opposingAccountSubtype,
    ordering,
    payee,
    payeeId,
    pivotFields,
    q,
    reconciliationReport,
    revenueOrReceivables,
    shouldPivot,
    sort,
    startDate,
    tag,
    tagGroups,
    tagId,
    vendor,
    vendorId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **account** | [**number**] |  | (optional) defaults to undefined|
| **accountId** | [**number**] |  | (optional) defaults to undefined|
| **accountRollup** | [**boolean**] |  | (optional) defaults to false|
| **accountSubtype** | [**string**] |  | (optional) defaults to undefined|
| **accountType** | [**string**] |  | (optional) defaults to undefined|
| **accounts** | [**number**] |  | (optional) defaults to undefined|
| **aggregationFields** | [**string**] | Comma-separated aggregations, e.g. sum:amount,count:id | (optional) defaults to undefined|
| **allTime** | [**boolean**] | If true, uses full transaction date range for the customer; start_date and end_date are ignored | (optional) defaults to false|
| **bank** | [**number**] |  | (optional) defaults to undefined|
| **bankDescription** | [**string**] |  | (optional) defaults to undefined|
| **bankId** | [**number**] |  | (optional) defaults to undefined|
| **categorized** | [**string**] | Filter by categorization state (true/false) | (optional) defaults to undefined|
| **counterparty** | [**number**] | Intercompany counterparty entity id; matches lines whose balance is against that entity | (optional) defaults to undefined|
| **counterpartyId** | [**number**] | Alias of counterparty; do not combine the two | (optional) defaults to undefined|
| **creditAmountEqual** | [**number**] |  | (optional) defaults to undefined|
| **creditAmountGte** | [**number**] |  | (optional) defaults to undefined|
| **creditAmountLte** | [**number**] |  | (optional) defaults to undefined|
| **creditAmountNull** | [**boolean**] |  | (optional) defaults to false|
| **currency** | [**string**] |  | (optional) defaults to undefined|
| **dateFrom** | [**string**] | Alias of &#x60;start_date&#x60;; &#x60;start_date&#x60; wins when both are sent | (optional) defaults to undefined|
| **dateTo** | [**string**] | Alias of &#x60;end_date&#x60;; &#x60;end_date&#x60; wins when both are sent | (optional) defaults to undefined|
| **debitAmountEqual** | [**number**] |  | (optional) defaults to undefined|
| **debitAmountGte** | [**number**] |  | (optional) defaults to undefined|
| **debitAmountLte** | [**number**] |  | (optional) defaults to undefined|
| **debitAmountNull** | [**boolean**] |  | (optional) defaults to false|
| **department** | [**number**] |  | (optional) defaults to undefined|
| **departmentId** | [**number**] |  | (optional) defaults to undefined|
| **departmentOrUnassigned** | [**boolean**] |  | (optional) defaults to false|
| **download** | [**boolean**] | If true, dispatch async CSV/Excel email export instead of returning rows | (optional) defaults to false|
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to end of current month | (optional) defaults to undefined|
| **entity** | [**number**] |  | (optional) defaults to undefined|
| **entityId** | [**number**] |  | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] |  | (optional) defaults to false|
| **excludeEntity** | [**number**] |  | (optional) defaults to undefined|
| **excludeEntityId** | [**number**] |  | (optional) defaults to undefined|
| **excludeId** | [**number**] |  | (optional) defaults to undefined|
| **excludeJournal** | [**number**] |  | (optional) defaults to undefined|
| **excludeReconciliationReport** | [**number**] |  | (optional) defaults to undefined|
| **excludeUncategorizedAccounts** | [**boolean**] |  | (optional) defaults to false|
| **expenseOrAp** | [**boolean**] |  | (optional) defaults to undefined|
| **fields** | [**string**] | Comma-separated list of columns to return, e.g. \&#39;posted_at,debit_amount,account\&#39;. Omit to receive the full payload. \&#39;id\&#39; is always included. Narrowing the column list also skips the derived values behind the omitted columns, so it is the recommended way to pull large pages: a 1000-row page returns roughly 90% less data and responds materially faster when only a few columns are needed. Unrecognized names are ignored. | (optional) defaults to undefined|
| **group** | [**number**] |  | (optional) defaults to undefined|
| **groupFields** | [**string**] | Comma-separated list of fields to group by (e.g. account,vendor,tag_group_&lt;id&gt;) | (optional) defaults to undefined|
| **groupId** | [**number**] |  | (optional) defaults to undefined|
| **groupKeys** | [**string**] | Comma-separated values matched positionally to group_fields for drill-down | (optional) defaults to undefined|
| **hasLinkedFixedAsset** | [**string**] |  | (optional) defaults to undefined|
| **hasParentBankTransaction** | [**string**] |  | (optional) defaults to undefined|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **includeMatches** | [**boolean**] | If true, include match metadata (has_matches, primary_action_type) in serialized rows | (optional) defaults to false|
| **isNotReconciled** | [**boolean**] |  | (optional) defaults to false|
| **isReconciled** | [**boolean**] |  | (optional) defaults to false|
| **journal** | [**number**] | Only transactions on these journal entry ids (repeat the param for several) | (optional) defaults to undefined|
| **journalType** | [**string**] |  | (optional) defaults to undefined|
| **journalTypeNin** | [**string**] |  | (optional) defaults to undefined|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Maximum number of records to return per page. Default 100, maximum 10000. Use with offset to paginate | (optional) defaults to 100|
| **matchType** | [**&#39;all&#39; | &#39;any&#39;**]**Array<&#39;all&#39; &#124; &#39;any&#39;>** |  | (optional) defaults to 'all'|
| **needsReview** | [**boolean**] |  | (optional) defaults to false|
| **noCounterparty** | [**boolean**] | If true, only lines with no intercompany counterparty | (optional) defaults to undefined|
| **noDepartment** | [**boolean**] |  | (optional) defaults to undefined|
| **noTag** | [**boolean**] |  | (optional) defaults to undefined|
| **noVendor** | [**boolean**] |  | (optional) defaults to undefined|
| **offset** | [**number**] | Number of records to skip before collecting the result page. Use with limit to paginate | (optional) defaults to 0|
| **opposingAccount** | [**number**] |  | (optional) defaults to undefined|
| **opposingAccountSubtype** | [**string**] |  | (optional) defaults to undefined|
| **ordering** | [**string**] |  | (optional) defaults to undefined|
| **payee** | [**string**] | Integer payee id or Campfire ID (VEN-/CUST-/EMP-) | (optional) defaults to undefined|
| **payeeId** | [**string**] | Integer payee id or Campfire ID (VEN-/CUST-/EMP-) | (optional) defaults to undefined|
| **pivotFields** | [**string**] | Comma-separated list of pivot dimensions | (optional) defaults to undefined|
| **q** | [**string**] | Free-text search across journal memo, bank description, and related fields | (optional) defaults to undefined|
| **reconciliationReport** | [**number**] |  | (optional) defaults to undefined|
| **revenueOrReceivables** | [**boolean**] |  | (optional) defaults to undefined|
| **shouldPivot** | [**boolean**] |  | (optional) defaults to false|
| **sort** | [**string**] | Sort field; prefix with - for descending. Default: -posted_at | (optional) defaults to undefined|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|
| **tag** | [**number**] |  | (optional) defaults to undefined|
| **tagGroups** | [**number**] |  | (optional) defaults to undefined|
| **tagId** | [**number**] |  | (optional) defaults to undefined|
| **vendor** | [**string**] | Integer payee id or Campfire ID (VEN-/CUST-/EMP-) | (optional) defaults to undefined|
| **vendorId** | [**string**] | Integer payee id or Campfire ID (VEN-/CUST-/EMP-) | (optional) defaults to undefined|


### Return type

**PaginatedChartTransactionList**

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

# **coaApiTransactionMatchesBulkAcceptCreate**
> coaApiTransactionMatchesBulkAcceptCreate(bulkAcceptSuggestions)

Apply one class of pending suggestions (match | rule | merge | ai) across an explicit or filter-implicit transaction selection, each through its existing single-item flow. Per-item outcomes; capped per call — drain until \'truncated\' is false, excluding blocked transaction ids on subsequent calls.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    BulkAcceptSuggestions
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let bulkAcceptSuggestions: BulkAcceptSuggestions; //

const { status, data } = await apiInstance.coaApiTransactionMatchesBulkAcceptCreate(
    bulkAcceptSuggestions
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulkAcceptSuggestions** | **BulkAcceptSuggestions**|  | |


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
|**200** | No response body |  -  |

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTransactionRetrieve**
> ChartTransaction coaApiTransactionRetrieve()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionRetrieve(
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorBulkSearchCreate**
> BulkVendorSearchResult coaApiVendorBulkSearchCreate(bulkVendorSearch)

Search for thousands of vendors in a single request, resolving each cell by external_id, then a Campfire ID or internal pk parsed from the cell, then name. Optimized for performance. Supports upsert to create missing vendors.  A row that supplies an external_id matching no payee is reported rather than failing the request: the body becomes `{vendors, errors}` instead of the payee list, still a 200, so the payees that did resolve are not discarded along with it. A name-only row that matches nothing is not reported — with `upsert` it is created, and without it the row is simply absent from `vendors`.

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

**BulkVendorSearchResult**

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

# **coaApiVendorContactDestroy**
> coaApiVendorContactDestroy()

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

const { status, data } = await apiInstance.coaApiVendorContactDestroy(
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

# **coaApiVendorContactPartialUpdate**
> VendorContact coaApiVendorContactPartialUpdate()

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    PatchedVendorContact
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let patchedVendorContact: PatchedVendorContact; // (optional)

const { status, data } = await apiInstance.coaApiVendorContactPartialUpdate(
    id,
    patchedVendorContact
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedVendorContact** | **PatchedVendorContact**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**VendorContact**

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

# **coaApiVendorContactRetrieve**
> VendorContact coaApiVendorContactRetrieve()

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

const { status, data } = await apiInstance.coaApiVendorContactRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**VendorContact**

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

# **coaApiVendorContactUpdate**
> VendorContact coaApiVendorContactUpdate(vendorContact)

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
let vendorContact: VendorContact; //

const { status, data } = await apiInstance.coaApiVendorContactUpdate(
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorContactsCreate**
> VendorContact coaApiVendorContactsCreate(vendorContact)

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
let vendorContact: VendorContact; //

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

No authorization required

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createFixedAssetAutomation**
> FixedAssetAutomationRule createFixedAssetAutomation(fixedAssetAutomationRule)

List all automation rules or create a new one. GET /api/fixed-asset-automation/ POST /api/fixed-asset-automation/

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    FixedAssetAutomationRule
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let fixedAssetAutomationRule: FixedAssetAutomationRule; //

const { status, data } = await apiInstance.createFixedAssetAutomation(
    fixedAssetAutomationRule
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **fixedAssetAutomationRule** | **FixedAssetAutomationRule**|  | |


### Return type

**FixedAssetAutomationRule**

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

# **createTransactionBillPayments**
> createTransactionBillPayments()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let transactionId: number; // (default to undefined)

const { status, data } = await apiInstance.createTransactionBillPayments(
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createTransactionCreditMemoPayments**
> createTransactionCreditMemoPayments()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let transactionId: number; // (default to undefined)

const { status, data } = await apiInstance.createTransactionCreditMemoPayments(
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createTransactionDebitMemoPayments**
> createTransactionDebitMemoPayments()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let transactionId: number; // (default to undefined)

const { status, data } = await apiInstance.createTransactionDebitMemoPayments(
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createTransactionInvoicePayments**
> createTransactionInvoicePayments()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let transactionId: number; // (default to undefined)

const { status, data } = await apiInstance.createTransactionInvoicePayments(
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteChartTransaction**
> deleteChartTransaction()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.deleteChartTransaction(
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

# **deleteFixedAssetAutomation**
> deleteFixedAssetAutomation()

Deprecated: use `POST /coa/api/fixed-asset-automation/{id}/delete`, which also takes an optional reason for the audit log.  Retrieve, update, or delete an automation rule. GET/PUT/PATCH/DELETE /api/fixed-asset-automation/<id>/

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.deleteFixedAssetAutomation(
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

# **deleteTransactionMatch**
> deleteTransactionMatch()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.deleteTransactionMatch(
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

# **discoverTransactionMatchCandidates**
> discoverTransactionMatchCandidates()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

const { status, data } = await apiInstance.discoverTransactionMatchCandidates();
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

# **getChartTransactionTotals**
> Array<ChartTransaction> getChartTransactionTotals()

Complete mixin for history filtering with pagination support. Returns either active OR deleted records based on include_deleted parameter.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let fields: string; //Comma-separated list of columns to return, e.g. \'posted_at,debit_amount,account\'. Omit to receive the full payload. \'id\' is always included. Narrowing the column list also skips the derived values behind the omitted columns, so it is the recommended way to pull large pages: a 1000-row page returns roughly 90% less data and responds materially faster when only a few columns are needed. Unrecognized names are ignored. (optional) (default to undefined)

const { status, data } = await apiInstance.getChartTransactionTotals(
    fields
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **fields** | [**string**] | Comma-separated list of columns to return, e.g. \&#39;posted_at,debit_amount,account\&#39;. Omit to receive the full payload. \&#39;id\&#39; is always included. Narrowing the column list also skips the derived values behind the omitted columns, so it is the recommended way to pull large pages: a 1000-row page returns roughly 90% less data and responds materially faster when only a few columns are needed. Unrecognized names are ignored. | (optional) defaults to undefined|


### Return type

**Array<ChartTransaction>**

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

# **getFixedAssetAutomation**
> FixedAssetAutomationRule getFixedAssetAutomation()

Retrieve, update, or delete an automation rule. GET/PUT/PATCH/DELETE /api/fixed-asset-automation/<id>/

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.getFixedAssetAutomation(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**FixedAssetAutomationRule**

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

# **getFixedAssetAutomationMatch**
> FixedAssetAutomationMatch getFixedAssetAutomationMatch()

Retrieve or update an automation match (for editing proposed values before acceptance). GET/PATCH /api/fixed-asset-automation-match/<id>/

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.getFixedAssetAutomationMatch(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**FixedAssetAutomationMatch**

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

# **getTransactionMatch**
> TransactionMatch getTransactionMatch()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.getTransactionMatch(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**TransactionMatch**

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

# **getTransactionMatchesCount**
> getTransactionMatchesCount()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

const { status, data } = await apiInstance.getTransactionMatchesCount();
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

# **listFixedAssetAutomationAccounts**
> listFixedAssetAutomationAccounts()

List accounts that are of type FIXED_ASSET for use in automation rule creation. GET /api/fixed-asset-automation/accounts  This endpoint returns only accounts with account_subtype=\'FIXED_ASSET\' to ensure automation rules are created with appropriate accounts.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

const { status, data } = await apiInstance.listFixedAssetAutomationAccounts();
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

# **listFixedAssetAutomationAssetClasses**
> listFixedAssetAutomationAssetClasses()

List fixed asset classes that match a specific account. GET /api/fixed-asset-automation/asset-classes?account_id=<id>  Filters asset classes to only those where asset_account matches the provided account_id. This ensures users can only select compatible asset classes for the chosen account.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

const { status, data } = await apiInstance.listFixedAssetAutomationAssetClasses();
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

# **listFixedAssetAutomationMatches**
> PaginatedFixedAssetAutomationMatchList listFixedAssetAutomationMatches()

List pending asset matches for review. GET /api/fixed-asset-automation/matches

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let ordering: string; //Which field to use when ordering the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listFixedAssetAutomationMatches(
    limit,
    offset,
    ordering
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **ordering** | [**string**] | Which field to use when ordering the results. | (optional) defaults to undefined|


### Return type

**PaginatedFixedAssetAutomationMatchList**

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

# **listFixedAssetAutomations**
> PaginatedFixedAssetAutomationRuleList listFixedAssetAutomations()

List all automation rules or create a new one. GET /api/fixed-asset-automation/ POST /api/fixed-asset-automation/

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let ordering: string; //Which field to use when ordering the results. (optional) (default to undefined)
let search: string; //A search term. (optional) (default to undefined)

const { status, data } = await apiInstance.listFixedAssetAutomations(
    limit,
    offset,
    ordering,
    search
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|
| **ordering** | [**string**] | Which field to use when ordering the results. | (optional) defaults to undefined|
| **search** | [**string**] | A search term. | (optional) defaults to undefined|


### Return type

**PaginatedFixedAssetAutomationRuleList**

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

# **listFixedAssetReconciliationUnmatchedGl**
> listFixedAssetReconciliationUnmatchedGl()

Drilldown showing GL transactions NOT linked to any fixed asset.  Returns the journal entries on a control account that cannot be traced back to a specific asset\'s purchase, depreciation, or disposal entries. These are the transactions that make up the \"Unmatched GL\" amount in the reconciliation report.

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

const { status, data } = await apiInstance.listFixedAssetReconciliationUnmatchedGl();
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

# **listTransactionMatches**
> PaginatedTransactionMatchList listTransactionMatches()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listTransactionMatches(
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

**PaginatedTransactionMatchList**

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

# **mergeChartTransactions**
> JournalEntry mergeChartTransactions(mergeChartTransactionsRequest)

         Merge two offsetting chart transactions from different journals.          This endpoint consolidates journals containing offsetting transactions by removing         the specified transactions and combining the remaining transactions into a single journal entry.          **Request Body:**         - `transaction_ids` (array, required): Array of exactly two transaction IDs to merge         - `transaction_match_id` (integer, optional): The AutoMergeSuggestion TransactionMatch           the user explicitly accepted; when it names a suggestion over exactly this pair, the           merge is recorded as a suggestion accept rather than a manual merge          **Returns:**         The merged journal entry with all remaining transactions.          **Requirements:**         - Must provide exactly two transaction IDs         - Transactions must be from different journals         - Transactions must have matching amounts         - Transactions must belong to the same entity          **Result:**         - The two specified transactions are deleted         - Other transactions from both journals are consolidated into a single journal         - A draft queue record is created for audit purposes and auto-approved         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    MergeChartTransactionsRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let mergeChartTransactionsRequest: MergeChartTransactionsRequest; //

const { status, data } = await apiInstance.mergeChartTransactions(
    mergeChartTransactionsRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **mergeChartTransactionsRequest** | **MergeChartTransactionsRequest**|  | |


### Return type

**JournalEntry**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**400** | Validation error - invalid transaction count, draft queue not found, same journal, mismatched amounts, or mismatched entities |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partialUpdateFixedAssetAutomation**
> FixedAssetAutomationRule partialUpdateFixedAssetAutomation()

Retrieve, update, or delete an automation rule. GET/PUT/PATCH/DELETE /api/fixed-asset-automation/<id>/

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    PatchedFixedAssetAutomationRule
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let patchedFixedAssetAutomationRule: PatchedFixedAssetAutomationRule; // (optional)

const { status, data } = await apiInstance.partialUpdateFixedAssetAutomation(
    id,
    patchedFixedAssetAutomationRule
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedFixedAssetAutomationRule** | **PatchedFixedAssetAutomationRule**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**FixedAssetAutomationRule**

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

# **partialUpdateFixedAssetAutomationMatch**
> FixedAssetAutomationMatch partialUpdateFixedAssetAutomationMatch()

Retrieve or update an automation match (for editing proposed values before acceptance). GET/PATCH /api/fixed-asset-automation-match/<id>/

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    PatchedFixedAssetAutomationMatch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let patchedFixedAssetAutomationMatch: PatchedFixedAssetAutomationMatch; // (optional)

const { status, data } = await apiInstance.partialUpdateFixedAssetAutomationMatch(
    id,
    patchedFixedAssetAutomationMatch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedFixedAssetAutomationMatch** | **PatchedFixedAssetAutomationMatch**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**FixedAssetAutomationMatch**

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

# **partialUpdateTransactionMatch**
> TransactionMatch partialUpdateTransactionMatch()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    PatchedTransactionMatch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let patchedTransactionMatch: PatchedTransactionMatch; // (optional)

const { status, data } = await apiInstance.partialUpdateTransactionMatch(
    id,
    patchedTransactionMatch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedTransactionMatch** | **PatchedTransactionMatch**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**TransactionMatch**

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

# **previewChartTransactionMerge**
> JournalEntry previewChartTransactionMerge()

         Preview the result of merging two chart transactions.          This endpoint shows what the merged journal entry will look like, allowing you to verify         the merge before committing. The preview includes the journal that will be retained and         the transactions that will remain after the merge.          **Parameters:**         - `transaction_ids` (query, required): Comma-separated list of exactly two transaction IDs          **Returns:**         A journal entry object containing the merged result with all remaining transactions.          **Requirements:**         - Must provide exactly two transaction IDs         - Transactions must be from different journals         - Transactions must have matching amounts         - Transactions must belong to the same entity         

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

const { status, data } = await apiInstance.previewChartTransactionMerge();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**JournalEntry**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**400** | Validation error - invalid transaction count, same journal, mismatched amounts, or mismatched entities |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **processTransactionMatch**
> processTransactionMatch()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

const { status, data } = await apiInstance.processTransactionMatch();
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

# **proposeTransactionGlCoding**
> proposeTransactionGlCoding(proposeGlCoding)

Wraps ``CreateModelMixin.create`` (or any method named ``create``) with ``Idempotency-Key`` handling.  Place this mixin **before** the view\'s other base classes so its ``create`` overrides the inherited one::      class JournalEntryListCreate(         IdempotentCreateMixin,         HistoryFilteringMixin,         ListCreateAPIView,     ):         ...

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    ProposeGlCoding
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let proposeGlCoding: ProposeGlCoding; //

const { status, data } = await apiInstance.proposeTransactionGlCoding(
    proposeGlCoding
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **proposeGlCoding** | **ProposeGlCoding**|  | |


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
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposeTransactionMatches**
> proposeTransactionMatches()

Wraps ``CreateModelMixin.create`` (or any method named ``create``) with ``Idempotency-Key`` handling.  Place this mixin **before** the view\'s other base classes so its ``create`` overrides the inherited one::      class JournalEntryListCreate(         IdempotentCreateMixin,         HistoryFilteringMixin,         ListCreateAPIView,     ):         ...

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    ProposeMatches
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let proposeMatches: ProposeMatches; // (optional)

const { status, data } = await apiInstance.proposeTransactionMatches(
    proposeMatches
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **proposeMatches** | **ProposeMatches**|  | |


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
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proposeTransactionMerge**
> proposeTransactionMerge(proposeMerge)

Wraps ``CreateModelMixin.create`` (or any method named ``create``) with ``Idempotency-Key`` handling.  Place this mixin **before** the view\'s other base classes so its ``create`` overrides the inherited one::      class JournalEntryListCreate(         IdempotentCreateMixin,         HistoryFilteringMixin,         ListCreateAPIView,     ):         ...

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    ProposeMerge
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let proposeMerge: ProposeMerge; //

const { status, data } = await apiInstance.proposeTransactionMerge(
    proposeMerge
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **proposeMerge** | **ProposeMerge**|  | |


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
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rejectTransactionMatch**
> rejectTransactionMatch()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rejectTransactionMatch(
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

# **runFixedAssetAutomation**
> runFixedAssetAutomation()

Trigger automation processing. POST /api/fixed-asset-automation/run  Optional body: {\"rule_id\": 123}

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

const { status, data } = await apiInstance.runFixedAssetAutomation();
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

# **setTransactionMatchStatus**
> setTransactionMatchStatus()

Handle POST requests with \'action\' parameter (accept/reject)

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.setTransactionMatchStatus(
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

# **updateFixedAssetAutomation**
> FixedAssetAutomationRule updateFixedAssetAutomation(fixedAssetAutomationRule)

Retrieve, update, or delete an automation rule. GET/PUT/PATCH/DELETE /api/fixed-asset-automation/<id>/

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    FixedAssetAutomationRule
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let fixedAssetAutomationRule: FixedAssetAutomationRule; //

const { status, data } = await apiInstance.updateFixedAssetAutomation(
    id,
    fixedAssetAutomationRule
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **fixedAssetAutomationRule** | **FixedAssetAutomationRule**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**FixedAssetAutomationRule**

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

# **updateFixedAssetAutomationMatch**
> FixedAssetAutomationMatch updateFixedAssetAutomationMatch(fixedAssetAutomationMatch)

Retrieve or update an automation match (for editing proposed values before acceptance). GET/PATCH /api/fixed-asset-automation-match/<id>/

### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    FixedAssetAutomationMatch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let fixedAssetAutomationMatch: FixedAssetAutomationMatch; //

const { status, data } = await apiInstance.updateFixedAssetAutomationMatch(
    id,
    fixedAssetAutomationMatch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **fixedAssetAutomationMatch** | **FixedAssetAutomationMatch**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**FixedAssetAutomationMatch**

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

# **updateTransactionMatch**
> TransactionMatch updateTransactionMatch(transactionMatch)


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration,
    TransactionMatch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)
let transactionMatch: TransactionMatch; //

const { status, data } = await apiInstance.updateTransactionMatch(
    id,
    transactionMatch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **transactionMatch** | **TransactionMatch**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**TransactionMatch**

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

# **updateTransactionMatchStatus**
> updateTransactionMatchStatus()


### Example

```typescript
import {
    CoreAccountingApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoreAccountingApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.updateTransactionMatchStatus(
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


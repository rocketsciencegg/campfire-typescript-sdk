# FinancialStatementsApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**caApiBalanceSheetComparativeRetrieve**](#caapibalancesheetcomparativeretrieve) | **GET** /ca/api/balance-sheet/comparative | Get Comparative Balance Sheet|
|[**caApiCashBasisOperatingStatementRetrieve**](#caapicashbasisoperatingstatementretrieve) | **GET** /ca/api/cash-basis-operating-statement | Get Cash Basis Operating Statement|
|[**caApiCashBasisRetrieve**](#caapicashbasisretrieve) | **GET** /ca/api/cash-basis | Get Cash Basis Income Statement|
|[**caApiCashOperatingStatementTransactionsRetrieve**](#caapicashoperatingstatementtransactionsretrieve) | **GET** /ca/api/cash-operating-statement/transactions | Get Cash Operating Transactions with Projected Transactions|
|[**caApiCustomReportsDataRetrieve**](#caapicustomreportsdataretrieve) | **GET** /ca/api/custom-reports/{id}/data | Execute Custom Report|
|[**caApiCustomReportsList**](#caapicustomreportslist) | **GET** /ca/api/custom-reports | List Custom Reports|
|[**caApiCustomReportsRetrieve**](#caapicustomreportsretrieve) | **GET** /ca/api/custom-reports/{id} | Retrieve Custom Report|
|[**caApiGetBalanceSheetRetrieve**](#caapigetbalancesheetretrieve) | **GET** /ca/api/get_balance_sheet | Get Balance Sheet|
|[**caApiGetCashFlowActivityRetrieve**](#caapigetcashflowactivityretrieve) | **GET** /ca/api/get_cash_flow_activity | Get Cash Flow Activity|
|[**caApiGetCashFlowRetrieve**](#caapigetcashflowretrieve) | **GET** /ca/api/get_cash_flow | Get Cash Flow|
|[**caApiGetCashFlowV2Retrieve**](#caapigetcashflowv2retrieve) | **GET** /ca/api/get_cash_flow_v2 | Get Cash Flow Statement|
|[**caApiGetIncomeStatementRetrieve**](#caapigetincomestatementretrieve) | **GET** /ca/api/get_income_statement | Get Income Statement|
|[**caApiGetTrialBalanceRetrieve**](#caapigettrialbalanceretrieve) | **GET** /ca/api/get_trial_balance | Get Trial Balance|
|[**caApiIncomeStatementComparativeRetrieve**](#caapiincomestatementcomparativeretrieve) | **GET** /ca/api/income-statement/comparative | Get Comparative Income Statement|
|[**coaApiGeneralLedgerRetrieve**](#coaapigeneralledgerretrieve) | **GET** /coa/api/general-ledger | Get General Ledger|

# **caApiBalanceSheetComparativeRetrieve**
> CaApiBalanceSheetComparativeRetrieve200Response caApiBalanceSheetComparativeRetrieve()

API view for comparative balance sheet that handles budget vs actual comparisons

### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let cadence: 'daily' | 'monthly' | 'quarterly' | 'weekly' | 'yearly'; // (optional) (default to 'monthly')
let entity: number; //Entity ID(s) to scope the report. Can be repeated (?entity=1&entity=2) or JSON array (optional) (default to undefined)
let entityRollup: boolean; //If true, includes all data of children entities in consolidation (optional) (default to false)
let groupBy: string; // (optional) (default to undefined)

const { status, data } = await apiInstance.caApiBalanceSheetComparativeRetrieve(
    cadence,
    entity,
    entityRollup,
    groupBy
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **cadence** | [**&#39;daily&#39; | &#39;monthly&#39; | &#39;quarterly&#39; | &#39;weekly&#39; | &#39;yearly&#39;**]**Array<&#39;daily&#39; &#124; &#39;monthly&#39; &#124; &#39;quarterly&#39; &#124; &#39;weekly&#39; &#124; &#39;yearly&#39;>** |  | (optional) defaults to 'monthly'|
| **entity** | [**number**] | Entity ID(s) to scope the report. Can be repeated (?entity&#x3D;1&amp;entity&#x3D;2) or JSON array | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **groupBy** | [**string**] |  | (optional) defaults to undefined|


### Return type

**CaApiBalanceSheetComparativeRetrieve200Response**

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

# **caApiCashBasisOperatingStatementRetrieve**
> caApiCashBasisOperatingStatementRetrieve()


### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let allTime: boolean; //If true, uses full transaction date range for the customer; start_date and end_date are ignored (optional) (default to false)
let cadence: 'daily' | 'monthly' | 'quarterly' | 'weekly' | 'yearly'; // (optional) (default to 'monthly')
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to end of current month (optional) (default to undefined)
let entity: number; //Entity ID(s) to scope the report. Can be repeated (?entity=1&entity=2) or JSON array (optional) (default to undefined)
let entityRollup: boolean; //If true, includes all data of children entities in consolidation (optional) (default to false)
let _export: 'xlsx'; //If xlsx, returns Excel file (income_statement.xlsx) instead of JSON (optional) (default to undefined)
let group: number; //Tag group ID. Required when group_by=tag (optional) (default to undefined)
let groupBy: string; //Breakdown dimension: vendor, department, tag, currency, entity. For tag, also pass group (tag group ID). For cash-basis, department_row_children, department_row_parents, department_only normalize to department (optional) (default to undefined)
let rollupTotals: boolean; //If true, roll up child account totals to parent accounts. Set to false for export (optional) (default to true)
let startDate: string; //Earliest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)

const { status, data } = await apiInstance.caApiCashBasisOperatingStatementRetrieve(
    allTime,
    cadence,
    endDate,
    entity,
    entityRollup,
    _export,
    group,
    groupBy,
    rollupTotals,
    startDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **allTime** | [**boolean**] | If true, uses full transaction date range for the customer; start_date and end_date are ignored | (optional) defaults to false|
| **cadence** | [**&#39;daily&#39; | &#39;monthly&#39; | &#39;quarterly&#39; | &#39;weekly&#39; | &#39;yearly&#39;**]**Array<&#39;daily&#39; &#124; &#39;monthly&#39; &#124; &#39;quarterly&#39; &#124; &#39;weekly&#39; &#124; &#39;yearly&#39;>** |  | (optional) defaults to 'monthly'|
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to end of current month | (optional) defaults to undefined|
| **entity** | [**number**] | Entity ID(s) to scope the report. Can be repeated (?entity&#x3D;1&amp;entity&#x3D;2) or JSON array | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **_export** | [**&#39;xlsx&#39;**]**Array<&#39;xlsx&#39;>** | If xlsx, returns Excel file (income_statement.xlsx) instead of JSON | (optional) defaults to undefined|
| **group** | [**number**] | Tag group ID. Required when group_by&#x3D;tag | (optional) defaults to undefined|
| **groupBy** | [**string**] | Breakdown dimension: vendor, department, tag, currency, entity. For tag, also pass group (tag group ID). For cash-basis, department_row_children, department_row_parents, department_only normalize to department | (optional) defaults to undefined|
| **rollupTotals** | [**boolean**] | If true, roll up child account totals to parent accounts. Set to false for export | (optional) defaults to true|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|


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

# **caApiCashBasisRetrieve**
> caApiCashBasisRetrieve()


### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let allTime: boolean; //If true, uses full transaction date range for the customer; start_date and end_date are ignored (optional) (default to false)
let cadence: 'daily' | 'monthly' | 'quarterly' | 'weekly' | 'yearly'; // (optional) (default to 'monthly')
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to end of current month (optional) (default to undefined)
let entity: number; //Entity ID(s) to scope the report. Can be repeated (?entity=1&entity=2) or JSON array (optional) (default to undefined)
let entityRollup: boolean; //If true, includes all data of children entities in consolidation (optional) (default to false)
let _export: 'xlsx'; //If xlsx, returns Excel file (income_statement.xlsx) instead of JSON (optional) (default to undefined)
let group: number; //Tag group ID. Required when group_by=tag (optional) (default to undefined)
let groupBy: string; //Breakdown dimension: vendor, department, tag, currency, entity. For tag, also pass group (tag group ID). For cash-basis, department_row_children, department_row_parents, department_only normalize to department (optional) (default to undefined)
let rollupTotals: boolean; //If true, roll up child account totals to parent accounts. Set to false for export (optional) (default to true)
let startDate: string; //Earliest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)
let useBookValues: boolean; //If true, use book currency amounts instead of presentation currency (optional) (default to false)

const { status, data } = await apiInstance.caApiCashBasisRetrieve(
    allTime,
    cadence,
    endDate,
    entity,
    entityRollup,
    _export,
    group,
    groupBy,
    rollupTotals,
    startDate,
    useBookValues
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **allTime** | [**boolean**] | If true, uses full transaction date range for the customer; start_date and end_date are ignored | (optional) defaults to false|
| **cadence** | [**&#39;daily&#39; | &#39;monthly&#39; | &#39;quarterly&#39; | &#39;weekly&#39; | &#39;yearly&#39;**]**Array<&#39;daily&#39; &#124; &#39;monthly&#39; &#124; &#39;quarterly&#39; &#124; &#39;weekly&#39; &#124; &#39;yearly&#39;>** |  | (optional) defaults to 'monthly'|
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to end of current month | (optional) defaults to undefined|
| **entity** | [**number**] | Entity ID(s) to scope the report. Can be repeated (?entity&#x3D;1&amp;entity&#x3D;2) or JSON array | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **_export** | [**&#39;xlsx&#39;**]**Array<&#39;xlsx&#39;>** | If xlsx, returns Excel file (income_statement.xlsx) instead of JSON | (optional) defaults to undefined|
| **group** | [**number**] | Tag group ID. Required when group_by&#x3D;tag | (optional) defaults to undefined|
| **groupBy** | [**string**] | Breakdown dimension: vendor, department, tag, currency, entity. For tag, also pass group (tag group ID). For cash-basis, department_row_children, department_row_parents, department_only normalize to department | (optional) defaults to undefined|
| **rollupTotals** | [**boolean**] | If true, roll up child account totals to parent accounts. Set to false for export | (optional) defaults to true|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|
| **useBookValues** | [**boolean**] | If true, use book currency amounts instead of presentation currency | (optional) defaults to false|


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

# **caApiCashOperatingStatementTransactionsRetrieve**
> caApiCashOperatingStatementTransactionsRetrieve()


### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to end of current month (optional) (default to undefined)
let startDate: string; //Earliest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)

const { status, data } = await apiInstance.caApiCashOperatingStatementTransactionsRetrieve(
    endDate,
    startDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to end of current month | (optional) defaults to undefined|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|


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

# **caApiCustomReportsDataRetrieve**
> CustomReportDataTableResponse caApiCustomReportsDataRetrieve()

Execute custom report and return DataTable-compatible response.  :param request: HTTP request with query params :param pk: Custom report ID :return: Paginated, sparse-formatted response

### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let id: number; // (default to undefined)
let account: string; //Account ID(s), comma-separated (optional) (default to undefined)
let accountSubtype: string; //Account subtype(s) (optional) (default to undefined)
let accountType: string; //Account type(s), comma-separated (e.g. REVENUE,EXPENSE) (optional) (default to undefined)
let aggregationFields: string; //Override saved aggregates: comma-separated fn:field pairs (e.g. sum:net_debit,sum:net_credit) (optional) (default to undefined)
let bank: string; //Bank account ID(s), comma-separated (optional) (default to undefined)
let currency: string; //Currency code(s), comma-separated (optional) (default to undefined)
let department: string; //Department ID(s), comma-separated (optional) (default to undefined)
let endDate: string; //End date (YYYY-MM-DD) (optional) (default to undefined)
let entity: string; //Entity ID(s), comma-separated (optional) (default to undefined)
let groupFields: string; //Override saved row dimensions, comma-separated (e.g. vendor_id,account_id) (optional) (default to undefined)
let groupKeys: string; //Drilldown parent keys (optional) (default to undefined)
let includeTotals: boolean; //Include grand totals row (optional) (default to undefined)
let journalType: string; //Journal type(s), comma-separated (optional) (default to undefined)
let limit: number; //Page size (max 10000) (optional) (default to undefined)
let mode: string; //paginated | full | csv. full returns unpaginated JSON for grouped reports; reports without groupings/aggregations stay paginated in JSON — use csv, which streams the complete report as a CSV attachment, for a full flat export. (optional) (default to undefined)
let noDepartment: boolean; //Only rows without a department (optional) (default to undefined)
let noTag: boolean; //Only rows without tags (optional) (default to undefined)
let noVendor: boolean; //Only rows without a vendor (optional) (default to undefined)
let offset: number; //Pagination offset (optional) (default to undefined)
let pivotFields: string; //Override saved column dimensions, comma-separated (e.g. date_month) (optional) (default to undefined)
let shouldPivot: boolean; //Enable pivot columns (optional) (default to undefined)
let showEmptyLines: boolean; //Include zero-balance rows (defaults to the saved report\'s setting) (optional) (default to undefined)
let sort: string; //Sort by column id; prefix with \'-\' for descending (optional) (default to undefined)
let startDate: string; //Start date (YYYY-MM-DD) (optional) (default to undefined)
let tag: string; //Tag ID(s), comma-separated (optional) (default to undefined)
let tagGroups: string; //Tag group ID(s), comma-separated (optional) (default to undefined)
let vendor: string; //Vendor ID(s), comma-separated (optional) (default to undefined)

const { status, data } = await apiInstance.caApiCustomReportsDataRetrieve(
    id,
    account,
    accountSubtype,
    accountType,
    aggregationFields,
    bank,
    currency,
    department,
    endDate,
    entity,
    groupFields,
    groupKeys,
    includeTotals,
    journalType,
    limit,
    mode,
    noDepartment,
    noTag,
    noVendor,
    offset,
    pivotFields,
    shouldPivot,
    showEmptyLines,
    sort,
    startDate,
    tag,
    tagGroups,
    vendor
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|
| **account** | [**string**] | Account ID(s), comma-separated | (optional) defaults to undefined|
| **accountSubtype** | [**string**] | Account subtype(s) | (optional) defaults to undefined|
| **accountType** | [**string**] | Account type(s), comma-separated (e.g. REVENUE,EXPENSE) | (optional) defaults to undefined|
| **aggregationFields** | [**string**] | Override saved aggregates: comma-separated fn:field pairs (e.g. sum:net_debit,sum:net_credit) | (optional) defaults to undefined|
| **bank** | [**string**] | Bank account ID(s), comma-separated | (optional) defaults to undefined|
| **currency** | [**string**] | Currency code(s), comma-separated | (optional) defaults to undefined|
| **department** | [**string**] | Department ID(s), comma-separated | (optional) defaults to undefined|
| **endDate** | [**string**] | End date (YYYY-MM-DD) | (optional) defaults to undefined|
| **entity** | [**string**] | Entity ID(s), comma-separated | (optional) defaults to undefined|
| **groupFields** | [**string**] | Override saved row dimensions, comma-separated (e.g. vendor_id,account_id) | (optional) defaults to undefined|
| **groupKeys** | [**string**] | Drilldown parent keys | (optional) defaults to undefined|
| **includeTotals** | [**boolean**] | Include grand totals row | (optional) defaults to undefined|
| **journalType** | [**string**] | Journal type(s), comma-separated | (optional) defaults to undefined|
| **limit** | [**number**] | Page size (max 10000) | (optional) defaults to undefined|
| **mode** | [**string**] | paginated | full | csv. full returns unpaginated JSON for grouped reports; reports without groupings/aggregations stay paginated in JSON — use csv, which streams the complete report as a CSV attachment, for a full flat export. | (optional) defaults to undefined|
| **noDepartment** | [**boolean**] | Only rows without a department | (optional) defaults to undefined|
| **noTag** | [**boolean**] | Only rows without tags | (optional) defaults to undefined|
| **noVendor** | [**boolean**] | Only rows without a vendor | (optional) defaults to undefined|
| **offset** | [**number**] | Pagination offset | (optional) defaults to undefined|
| **pivotFields** | [**string**] | Override saved column dimensions, comma-separated (e.g. date_month) | (optional) defaults to undefined|
| **shouldPivot** | [**boolean**] | Enable pivot columns | (optional) defaults to undefined|
| **showEmptyLines** | [**boolean**] | Include zero-balance rows (defaults to the saved report\&#39;s setting) | (optional) defaults to undefined|
| **sort** | [**string**] | Sort by column id; prefix with \&#39;-\&#39; for descending | (optional) defaults to undefined|
| **startDate** | [**string**] | Start date (YYYY-MM-DD) | (optional) defaults to undefined|
| **tag** | [**string**] | Tag ID(s), comma-separated | (optional) defaults to undefined|
| **tagGroups** | [**string**] | Tag group ID(s), comma-separated | (optional) defaults to undefined|
| **vendor** | [**string**] | Vendor ID(s), comma-separated | (optional) defaults to undefined|


### Return type

**CustomReportDataTableResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiCustomReportsList**
> PaginatedCustomReportList caApiCustomReportsList()


### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let dataType: string; //Filter by report type(s), comma-separated: transaction, invoice, financial_statement. Only transaction reports can be executed via the custom report data endpoint; invoice reports use the invoice report data endpoint. (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.caApiCustomReportsList(
    dataType,
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **dataType** | [**string**] | Filter by report type(s), comma-separated: transaction, invoice, financial_statement. Only transaction reports can be executed via the custom report data endpoint; invoice reports use the invoice report data endpoint. | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedCustomReportList**

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

# **caApiCustomReportsRetrieve**
> CustomReport caApiCustomReportsRetrieve()


### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.caApiCustomReportsRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**CustomReport**

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

# **caApiGetBalanceSheetRetrieve**
> CaApiGetBalanceSheetRetrieve200Response caApiGetBalanceSheetRetrieve()

Returns ending account balances for each period between `start_date` and `end_date` (both inclusive), split by `cadence`. This is the recommended endpoint for balance sheet ending balances.  **How the date range works:** `start_date` is *not* the date balances are calculated *from*. Account balances are always accumulated from the beginning of time through each period end. `start_date`, `end_date`, and `cadence` only determine how the report is split into periods (columns).  **Retained earnings:** included as its own row.  **Breakdowns:** the report can be broken down or filtered by entity, department, and tag dimensions via `group_by` (pass `group` with a tag group ID when grouping by tag).

### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let cadence: 'daily' | 'monthly' | 'quarterly' | 'weekly' | 'yearly'; // (optional) (default to 'monthly')
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to end of current month (optional) (default to undefined)
let entity: number; //Entity ID(s) to scope the report. Can be repeated (?entity=1&entity=2) or JSON array (optional) (default to undefined)
let entityRollup: boolean; //If true, includes all data of children entities in consolidation (optional) (default to false)
let groupBy: string; // (optional) (default to undefined)
let startDate: string; //Earliest period (inclusive) shown in the report. NOTE: balances are NOT calculated starting from this date - account balances are always accumulated from the beginning of time through each period end. start_date, end_date, and cadence only control how the report is split into periods (columns). Defaults to six months ago. (optional) (default to undefined)

const { status, data } = await apiInstance.caApiGetBalanceSheetRetrieve(
    cadence,
    endDate,
    entity,
    entityRollup,
    groupBy,
    startDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **cadence** | [**&#39;daily&#39; | &#39;monthly&#39; | &#39;quarterly&#39; | &#39;weekly&#39; | &#39;yearly&#39;**]**Array<&#39;daily&#39; &#124; &#39;monthly&#39; &#124; &#39;quarterly&#39; &#124; &#39;weekly&#39; &#124; &#39;yearly&#39;>** |  | (optional) defaults to 'monthly'|
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to end of current month | (optional) defaults to undefined|
| **entity** | [**number**] | Entity ID(s) to scope the report. Can be repeated (?entity&#x3D;1&amp;entity&#x3D;2) or JSON array | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **groupBy** | [**string**] |  | (optional) defaults to undefined|
| **startDate** | [**string**] | Earliest period (inclusive) shown in the report. NOTE: balances are NOT calculated starting from this date - account balances are always accumulated from the beginning of time through each period end. start_date, end_date, and cadence only control how the report is split into periods (columns). Defaults to six months ago. | (optional) defaults to undefined|


### Return type

**CaApiGetBalanceSheetRetrieve200Response**

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

# **caApiGetCashFlowActivityRetrieve**
> CaApiGetCashFlowActivityRetrieve200Response caApiGetCashFlowActivityRetrieve()


### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let cadence: 'daily' | 'monthly' | 'quarterly' | 'weekly' | 'yearly'; // (optional) (default to 'monthly')
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to end of current month (optional) (default to undefined)
let entity: number; //Entity ID(s) to scope the report. Can be repeated (?entity=1&entity=2) or JSON array (optional) (default to undefined)
let entityRollup: boolean; //If true, includes all data of children entities in consolidation (optional) (default to false)
let startDate: string; //Earliest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)

const { status, data } = await apiInstance.caApiGetCashFlowActivityRetrieve(
    cadence,
    endDate,
    entity,
    entityRollup,
    startDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **cadence** | [**&#39;daily&#39; | &#39;monthly&#39; | &#39;quarterly&#39; | &#39;weekly&#39; | &#39;yearly&#39;**]**Array<&#39;daily&#39; &#124; &#39;monthly&#39; &#124; &#39;quarterly&#39; &#124; &#39;weekly&#39; &#124; &#39;yearly&#39;>** |  | (optional) defaults to 'monthly'|
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to end of current month | (optional) defaults to undefined|
| **entity** | [**number**] | Entity ID(s) to scope the report. Can be repeated (?entity&#x3D;1&amp;entity&#x3D;2) or JSON array | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|


### Return type

**CaApiGetCashFlowActivityRetrieve200Response**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **caApiGetCashFlowRetrieve**
> CaApiGetCashFlowRetrieve200Response caApiGetCashFlowRetrieve()


### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let cadence: 'daily' | 'monthly' | 'quarterly' | 'weekly' | 'yearly'; // (optional) (default to 'monthly')
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to end of current month (optional) (default to undefined)
let entity: number; //Entity ID(s) to scope the report. Can be repeated (?entity=1&entity=2) or JSON array (optional) (default to undefined)
let entityRollup: boolean; //If true, includes all data of children entities in consolidation (optional) (default to false)
let groupBy: string; // (optional) (default to undefined)
let startDate: string; //Earliest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)

const { status, data } = await apiInstance.caApiGetCashFlowRetrieve(
    cadence,
    endDate,
    entity,
    entityRollup,
    groupBy,
    startDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **cadence** | [**&#39;daily&#39; | &#39;monthly&#39; | &#39;quarterly&#39; | &#39;weekly&#39; | &#39;yearly&#39;**]**Array<&#39;daily&#39; &#124; &#39;monthly&#39; &#124; &#39;quarterly&#39; &#124; &#39;weekly&#39; &#124; &#39;yearly&#39;>** |  | (optional) defaults to 'monthly'|
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to end of current month | (optional) defaults to undefined|
| **entity** | [**number**] | Entity ID(s) to scope the report. Can be repeated (?entity&#x3D;1&amp;entity&#x3D;2) or JSON array | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **groupBy** | [**string**] |  | (optional) defaults to undefined|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|


### Return type

**CaApiGetCashFlowRetrieve200Response**

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

# **caApiGetCashFlowV2Retrieve**
> caApiGetCashFlowV2Retrieve()

Sectioned cash flow statement (indirect method): operating (net income, non-cash adjustments, working-capital deltas), transactional investing and financing lines, the effect of exchange-rate changes on cash, and non-cash disclosures. The statement reconciles beginning to ending cash with a zero plug or is not rendered: an unreconciled ledger returns HTTP 422 with the plug by period and the journal entries whose accounts need cashflow classification. Monetary amounts are decimal strings. Pass export=xlsx for a workbook download.

### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let cadence: 'daily' | 'monthly' | 'quarterly' | 'weekly' | 'yearly'; // (optional) (default to 'monthly')
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to end of current month (optional) (default to undefined)
let entity: number; //Entity ID(s) to scope the report. Can be repeated (?entity=1&entity=2) or JSON array (optional) (default to undefined)
let entityRollup: boolean; //If true, includes all data of children entities in consolidation (optional) (default to false)
let startDate: string; //Earliest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)

const { status, data } = await apiInstance.caApiGetCashFlowV2Retrieve(
    cadence,
    endDate,
    entity,
    entityRollup,
    startDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **cadence** | [**&#39;daily&#39; | &#39;monthly&#39; | &#39;quarterly&#39; | &#39;weekly&#39; | &#39;yearly&#39;**]**Array<&#39;daily&#39; &#124; &#39;monthly&#39; &#124; &#39;quarterly&#39; &#124; &#39;weekly&#39; &#124; &#39;yearly&#39;>** |  | (optional) defaults to 'monthly'|
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to end of current month | (optional) defaults to undefined|
| **entity** | [**number**] | Entity ID(s) to scope the report. Can be repeated (?entity&#x3D;1&amp;entity&#x3D;2) or JSON array | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|


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

# **caApiGetIncomeStatementRetrieve**
> CaApiGetIncomeStatementRetrieve200Response caApiGetIncomeStatementRetrieve()

Returns account activity (revenue and expense movement) within the `start_date`-`end_date` range, split by `cadence`.  Unlike the balance sheet, the income statement reflects only the activity that falls *inside* the requested date range - `start_date` is the true start of the activity window.  **Breakdowns:** supports entity, department, vendor, and tag breakdowns/filters via `group_by` (pass `group` with a tag group ID when grouping by tag).

### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let cadence: 'daily' | 'monthly' | 'quarterly' | 'weekly' | 'yearly'; // (optional) (default to 'monthly')
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to end of current month (optional) (default to undefined)
let entity: number; //Entity ID(s) to scope the report. Can be repeated (?entity=1&entity=2) or JSON array (optional) (default to undefined)
let entityRollup: boolean; //If true, includes all data of children entities in consolidation (optional) (default to false)
let groupBy: string; // (optional) (default to undefined)
let startDate: string; //Earliest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)

const { status, data } = await apiInstance.caApiGetIncomeStatementRetrieve(
    cadence,
    endDate,
    entity,
    entityRollup,
    groupBy,
    startDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **cadence** | [**&#39;daily&#39; | &#39;monthly&#39; | &#39;quarterly&#39; | &#39;weekly&#39; | &#39;yearly&#39;**]**Array<&#39;daily&#39; &#124; &#39;monthly&#39; &#124; &#39;quarterly&#39; &#124; &#39;weekly&#39; &#124; &#39;yearly&#39;>** |  | (optional) defaults to 'monthly'|
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to end of current month | (optional) defaults to undefined|
| **entity** | [**number**] | Entity ID(s) to scope the report. Can be repeated (?entity&#x3D;1&amp;entity&#x3D;2) or JSON array | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **groupBy** | [**string**] |  | (optional) defaults to undefined|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|


### Return type

**CaApiGetIncomeStatementRetrieve200Response**

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

# **caApiGetTrialBalanceRetrieve**
> TrialBalanceResponse caApiGetTrialBalanceRetrieve()

Returns debit and credit totals for each account over a date range.  **The summation window depends on the account type:** - **Balance sheet accounts** (assets, liabilities, equity): totals are summed from the beginning of time through `end_date`. - **Income statement accounts** (revenue, expenses): the window depends on `income_statement_basis`. With the default `period` basis, totals are summed from `start_date` through `end_date` and a synthetic Net Income (Prior Periods) row carries current-fiscal-year income earned before `start_date`. With `fiscal_ytd`, totals are summed from the fiscal-year start through `end_date` and no Net Income row is emitted.  The effective income-statement window start is returned as `income_statement_start`.  Each account also carries rollforward columns, all presented as one-sided debit/credit pairs: `beginning_balances` (balance as of the day before `start_date`; fiscal-window-scoped for income-statement accounts), `activity` (gross period debits and credits), and `ending_balances` (`beginning + activity`, the net one-sided presentation of the account\'s balance). Beginning and ending columns each foot to zero across the report and period debits equal period credits.  Retained earnings is included as its own row. For balance sheet ending balances specifically, prefer `GET /ca/api/get_balance_sheet`.

### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let basis: 'transaction_rates' | 'translated'; //Balances as stamped at transaction time (default) or translated at read time (flagged customers; closing and average rates, CTA derived). Gross activity stays on transaction rates. (optional) (default to undefined)
let department: number; //Filter by department ID. Can be specified multiple times for multiple departments (optional) (default to undefined)
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to end of current month (optional) (default to undefined)
let entity: number; //Entity ID(s) to scope the report. Can be repeated (?entity=1&entity=2) or JSON array (optional) (default to undefined)
let entityRollup: boolean; //If true, includes all data of children entities in consolidation (optional) (default to false)
let groupBy: string; // (optional) (default to undefined)
let incomeStatementBasis: 'fiscal_ytd' | 'period'; //Income-statement window: selected period (default) or fiscal year-to-date. (optional) (default to undefined)
let startDate: string; //Earliest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)

const { status, data } = await apiInstance.caApiGetTrialBalanceRetrieve(
    basis,
    department,
    endDate,
    entity,
    entityRollup,
    groupBy,
    incomeStatementBasis,
    startDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **basis** | [**&#39;transaction_rates&#39; | &#39;translated&#39;**]**Array<&#39;transaction_rates&#39; &#124; &#39;translated&#39;>** | Balances as stamped at transaction time (default) or translated at read time (flagged customers; closing and average rates, CTA derived). Gross activity stays on transaction rates. | (optional) defaults to undefined|
| **department** | [**number**] | Filter by department ID. Can be specified multiple times for multiple departments | (optional) defaults to undefined|
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to end of current month | (optional) defaults to undefined|
| **entity** | [**number**] | Entity ID(s) to scope the report. Can be repeated (?entity&#x3D;1&amp;entity&#x3D;2) or JSON array | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **groupBy** | [**string**] |  | (optional) defaults to undefined|
| **incomeStatementBasis** | [**&#39;fiscal_ytd&#39; | &#39;period&#39;**]**Array<&#39;fiscal_ytd&#39; &#124; &#39;period&#39;>** | Income-statement window: selected period (default) or fiscal year-to-date. | (optional) defaults to undefined|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|


### Return type

**TrialBalanceResponse**

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

# **caApiIncomeStatementComparativeRetrieve**
> CaApiIncomeStatementComparativeRetrieve200Response caApiIncomeStatementComparativeRetrieve()


### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let cadence: 'daily' | 'monthly' | 'quarterly' | 'weekly' | 'yearly'; // (optional) (default to 'monthly')
let entity: number; //Entity ID(s) to scope the report. Can be repeated (?entity=1&entity=2) or JSON array (optional) (default to undefined)
let entityRollup: boolean; //If true, includes all data of children entities in consolidation (optional) (default to false)
let groupBy: string; // (optional) (default to undefined)

const { status, data } = await apiInstance.caApiIncomeStatementComparativeRetrieve(
    cadence,
    entity,
    entityRollup,
    groupBy
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **cadence** | [**&#39;daily&#39; | &#39;monthly&#39; | &#39;quarterly&#39; | &#39;weekly&#39; | &#39;yearly&#39;**]**Array<&#39;daily&#39; &#124; &#39;monthly&#39; &#124; &#39;quarterly&#39; &#124; &#39;weekly&#39; &#124; &#39;yearly&#39;>** |  | (optional) defaults to 'monthly'|
| **entity** | [**number**] | Entity ID(s) to scope the report. Can be repeated (?entity&#x3D;1&amp;entity&#x3D;2) or JSON array | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **groupBy** | [**string**] |  | (optional) defaults to undefined|


### Return type

**CaApiIncomeStatementComparativeRetrieve200Response**

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

# **coaApiGeneralLedgerRetrieve**
> GeneralLedgerResponse coaApiGeneralLedgerRetrieve()

Returns general-ledger transactions with running balances.  Each row includes a `tags` array with the transaction\'s tags; a tag\'s `group`/`group_name` identify the tag group (dimension) it belongs to. List a customer\'s tag groups via `/coa/api/tag-group` and tags via `/coa/api/tag`.

### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

const { status, data } = await apiInstance.coaApiGeneralLedgerRetrieve();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**GeneralLedgerResponse**

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


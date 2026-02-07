# FinancialStatementsApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**caApiCashBasisOperatingStatementRetrieve**](#caapicashbasisoperatingstatementretrieve) | **GET** /ca/api/cash-basis-operating-statement | Get Cash Basis Operating Statement|
|[**caApiCashBasisRetrieve**](#caapicashbasisretrieve) | **GET** /ca/api/cash-basis | Get Cash Basis Income Statement|
|[**caApiGetBalanceSheetRetrieve**](#caapigetbalancesheetretrieve) | **GET** /ca/api/get_balance_sheet | Get Balance Sheet|
|[**caApiGetCashFlowRetrieve**](#caapigetcashflowretrieve) | **GET** /ca/api/get_cash_flow | Get Cash Flow|
|[**caApiGetIncomeStatementRetrieve**](#caapigetincomestatementretrieve) | **GET** /ca/api/get_income_statement | Get Income Statement|
|[**caApiGetTrialBalanceRetrieve**](#caapigettrialbalanceretrieve) | **GET** /ca/api/get_trial_balance | Get Trial Balance|
|[**coaApiGeneralLedgerRetrieve**](#coaapigeneralledgerretrieve) | **GET** /coa/api/general-ledger | Get General Ledger|

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

const { status, data } = await apiInstance.caApiCashBasisOperatingStatementRetrieve();
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

const { status, data } = await apiInstance.caApiCashBasisRetrieve();
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

# **caApiGetBalanceSheetRetrieve**
> CaApiGetBalanceSheetRetrieve200Response caApiGetBalanceSheetRetrieve()


### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let cadence: 'daily' | 'monthly' | 'quarterly' | 'weekly' | 'yearly'; // (optional) (default to 'monthly')
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)
let entity: number; // (optional) (default to undefined)
let entityRollup: boolean; //If true, includes all data of children entities in consolidation (optional) (default to false)
let groupBy: string; // (optional) (default to undefined)
let startDate: string; //Earliest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)

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
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|
| **entity** | [**number**] |  | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **groupBy** | [**string**] |  | (optional) defaults to undefined|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|


### Return type

**CaApiGetBalanceSheetRetrieve200Response**

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
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)
let entity: number; // (optional) (default to undefined)
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
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|
| **entity** | [**number**] |  | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **groupBy** | [**string**] |  | (optional) defaults to undefined|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|


### Return type

**CaApiGetCashFlowRetrieve200Response**

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

# **caApiGetIncomeStatementRetrieve**
> CaApiGetIncomeStatementRetrieve200Response caApiGetIncomeStatementRetrieve()


### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let cadence: 'daily' | 'monthly' | 'quarterly' | 'weekly' | 'yearly'; // (optional) (default to 'monthly')
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)
let entity: number; // (optional) (default to undefined)
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
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|
| **entity** | [**number**] |  | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **groupBy** | [**string**] |  | (optional) defaults to undefined|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|


### Return type

**CaApiGetIncomeStatementRetrieve200Response**

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

# **caApiGetTrialBalanceRetrieve**
> TrialBalanceResponse caApiGetTrialBalanceRetrieve()


### Example

```typescript
import {
    FinancialStatementsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new FinancialStatementsApi(configuration);

let department: number; //Filter by department ID. Can be specified multiple times for multiple departments (optional) (default to undefined)
let endDate: string; //Latest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)
let entity: number; // (optional) (default to undefined)
let entityRollup: boolean; //If true, includes all data of children entities in consolidation (optional) (default to false)
let groupBy: string; // (optional) (default to undefined)
let startDate: string; //Earliest date (inclusive) for which to retrieve data. Defaults to six months ago (optional) (default to undefined)

const { status, data } = await apiInstance.caApiGetTrialBalanceRetrieve(
    department,
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
| **department** | [**number**] | Filter by department ID. Can be specified multiple times for multiple departments | (optional) defaults to undefined|
| **endDate** | [**string**] | Latest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|
| **entity** | [**number**] |  | (optional) defaults to undefined|
| **entityRollup** | [**boolean**] | If true, includes all data of children entities in consolidation | (optional) defaults to false|
| **groupBy** | [**string**] |  | (optional) defaults to undefined|
| **startDate** | [**string**] | Earliest date (inclusive) for which to retrieve data. Defaults to six months ago | (optional) defaults to undefined|


### Return type

**TrialBalanceResponse**

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

# **coaApiGeneralLedgerRetrieve**
> coaApiGeneralLedgerRetrieve()


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


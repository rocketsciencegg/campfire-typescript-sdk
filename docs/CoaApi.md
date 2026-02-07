# CoaApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**coaApiEntityAttachmentCreate**](#coaapientityattachmentcreate) | **POST** /coa/api/entity/{entity_id}/attachment | Upload Entity Invoice Email Attachment|
|[**coaApiFixedAssetAutomationAccountsRetrieve**](#coaapifixedassetautomationaccountsretrieve) | **GET** /coa/api/fixed-asset-automation/accounts | |
|[**coaApiFixedAssetAutomationAssetClassesRetrieve**](#coaapifixedassetautomationassetclassesretrieve) | **GET** /coa/api/fixed-asset-automation/asset-classes | |
|[**coaApiFixedAssetAutomationCreate**](#coaapifixedassetautomationcreate) | **POST** /coa/api/fixed-asset-automation/ | |
|[**coaApiFixedAssetAutomationDestroy**](#coaapifixedassetautomationdestroy) | **DELETE** /coa/api/fixed-asset-automation/{id}/ | |
|[**coaApiFixedAssetAutomationList**](#coaapifixedassetautomationlist) | **GET** /coa/api/fixed-asset-automation/ | |
|[**coaApiFixedAssetAutomationMatchPartialUpdate**](#coaapifixedassetautomationmatchpartialupdate) | **PATCH** /coa/api/fixed-asset-automation-match/{id}/ | |
|[**coaApiFixedAssetAutomationMatchRetrieve**](#coaapifixedassetautomationmatchretrieve) | **GET** /coa/api/fixed-asset-automation-match/{id}/ | |
|[**coaApiFixedAssetAutomationMatchUpdate**](#coaapifixedassetautomationmatchupdate) | **PUT** /coa/api/fixed-asset-automation-match/{id}/ | |
|[**coaApiFixedAssetAutomationMatchesList**](#coaapifixedassetautomationmatcheslist) | **GET** /coa/api/fixed-asset-automation/matches | |
|[**coaApiFixedAssetAutomationPartialUpdate**](#coaapifixedassetautomationpartialupdate) | **PATCH** /coa/api/fixed-asset-automation/{id}/ | |
|[**coaApiFixedAssetAutomationRetrieve**](#coaapifixedassetautomationretrieve) | **GET** /coa/api/fixed-asset-automation/{id}/ | |
|[**coaApiFixedAssetAutomationRunCreate**](#coaapifixedassetautomationruncreate) | **POST** /coa/api/fixed-asset-automation/run | |
|[**coaApiFixedAssetAutomationUpdate**](#coaapifixedassetautomationupdate) | **PUT** /coa/api/fixed-asset-automation/{id}/ | |
|[**coaApiTransactionBulkUpdateCreate**](#coaapitransactionbulkupdatecreate) | **POST** /coa/api/transaction/bulk-update | |
|[**coaApiTransactionMatchProcessCreate**](#coaapitransactionmatchprocesscreate) | **POST** /coa/api/transaction-match-process | |
|[**coaApiTransactionMatchesCountRetrieve**](#coaapitransactionmatchescountretrieve) | **GET** /coa/api/transaction-matches-count | |
|[**coaApiTransactionMatchesDestroy**](#coaapitransactionmatchesdestroy) | **DELETE** /coa/api/transaction-matches/{id} | |
|[**coaApiTransactionMatchesList**](#coaapitransactionmatcheslist) | **GET** /coa/api/transaction-matches | |
|[**coaApiTransactionMatchesPartialUpdate**](#coaapitransactionmatchespartialupdate) | **PATCH** /coa/api/transaction-matches/{id} | |
|[**coaApiTransactionMatchesRejectCreate**](#coaapitransactionmatchesrejectcreate) | **POST** /coa/api/transaction-matches/{id}/reject | |
|[**coaApiTransactionMatchesRetrieve**](#coaapitransactionmatchesretrieve) | **GET** /coa/api/transaction-matches/{id} | |
|[**coaApiTransactionMatchesStatusCreate**](#coaapitransactionmatchesstatuscreate) | **POST** /coa/api/transaction-matches/{id}/status | |
|[**coaApiTransactionMatchesStatusUpdate**](#coaapitransactionmatchesstatusupdate) | **PUT** /coa/api/transaction-matches/{id}/status | |
|[**coaApiTransactionMatchesUpdate**](#coaapitransactionmatchesupdate) | **PUT** /coa/api/transaction-matches/{id} | |
|[**coaApiTransactionMergeCreate**](#coaapitransactionmergecreate) | **POST** /coa/api/transaction/merge | Merge Chart Transactions|
|[**coaApiTransactionMergeRetrieve**](#coaapitransactionmergeretrieve) | **GET** /coa/api/transaction/merge | Preview Chart Transaction Merge|
|[**coaApiV1BillAmortizationCreate**](#coaapiv1billamortizationcreate) | **POST** /coa/api/v1/bill/amortization | |
|[**coaApiV1BillAmortizationCreate2**](#coaapiv1billamortizationcreate2) | **POST** /coa/api/v1/bill/{bill_id}/amortization | |
|[**coaApiV1BillAmortizationDestroy**](#coaapiv1billamortizationdestroy) | **DELETE** /coa/api/v1/bill/amortization | |
|[**coaApiV1BillAmortizationDestroy2**](#coaapiv1billamortizationdestroy2) | **DELETE** /coa/api/v1/bill/{bill_id}/amortization | |
|[**coaApiV1BillAmortizationGenerateScheduleRetrieve**](#coaapiv1billamortizationgeneratescheduleretrieve) | **GET** /coa/api/v1/bill/amortization/generate-schedule | |
|[**coaApiV1BillAmortizationGenerateScheduleUpdate**](#coaapiv1billamortizationgeneratescheduleupdate) | **PUT** /coa/api/v1/bill/amortization/generate-schedule | |
|[**coaApiV1BillAmortizationRetrieve**](#coaapiv1billamortizationretrieve) | **GET** /coa/api/v1/bill/amortization | |
|[**coaApiV1BillAmortizationRetrieve2**](#coaapiv1billamortizationretrieve2) | **GET** /coa/api/v1/bill/{bill_id}/amortization | |
|[**coaApiV1CreditMemoPdfRetrieve**](#coaapiv1creditmemopdfretrieve) | **GET** /coa/api/v1/credit-memo/{id}/pdf/ | |
|[**coaApiV1CreditMemoSendUpdate**](#coaapiv1creditmemosendupdate) | **PUT** /coa/api/v1/credit-memo/{id}/send/ | |
|[**coaApiV1InvoiceStatementClientPdfRetrieve**](#coaapiv1invoicestatementclientpdfretrieve) | **GET** /coa/api/v1/invoice/statement/client/{client_id}/pdf/ | |
|[**coaApiVendorCustomField1Create**](#coaapivendorcustomfield1create) | **POST** /coa/api/vendor_custom_field_1/ | |
|[**coaApiVendorCustomField1Destroy**](#coaapivendorcustomfield1destroy) | **DELETE** /coa/api/vendor_custom_field_1/{id}/ | |
|[**coaApiVendorCustomField1List**](#coaapivendorcustomfield1list) | **GET** /coa/api/vendor_custom_field_1/ | |
|[**coaApiVendorCustomField1PartialUpdate**](#coaapivendorcustomfield1partialupdate) | **PATCH** /coa/api/vendor_custom_field_1/{id}/ | |
|[**coaApiVendorCustomField1Retrieve**](#coaapivendorcustomfield1retrieve) | **GET** /coa/api/vendor_custom_field_1/{id}/ | |
|[**coaApiVendorCustomField1Update**](#coaapivendorcustomfield1update) | **PUT** /coa/api/vendor_custom_field_1/{id}/ | |
|[**coaApiVendorSummaryList**](#coaapivendorsummarylist) | **GET** /coa/api/vendor/summary | |

# **coaApiEntityAttachmentCreate**
> coaApiEntityAttachmentCreate()

Upload invoice email attachment with proper permissions

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

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

# **coaApiFixedAssetAutomationAccountsRetrieve**
> coaApiFixedAssetAutomationAccountsRetrieve()

List accounts that are of type FIXED_ASSET for use in automation rule creation. GET /api/fixed-asset-automation/accounts  This endpoint returns only accounts with account_subtype=\'FIXED_ASSET\' to ensure automation rules are created with appropriate accounts.

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiFixedAssetAutomationAccountsRetrieve();
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

# **coaApiFixedAssetAutomationAssetClassesRetrieve**
> coaApiFixedAssetAutomationAssetClassesRetrieve()

List fixed asset classes that match a specific account. GET /api/fixed-asset-automation/asset-classes?account_id=<id>  Filters asset classes to only those where asset_account matches the provided account_id. This ensures users can only select compatible asset classes for the chosen account.

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiFixedAssetAutomationAssetClassesRetrieve();
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

# **coaApiFixedAssetAutomationCreate**
> FixedAssetAutomationRule coaApiFixedAssetAutomationCreate(fixedAssetAutomationRule)

List all automation rules or create a new one. GET /api/fixed-asset-automation/ POST /api/fixed-asset-automation/

### Example

```typescript
import {
    CoaApi,
    Configuration,
    FixedAssetAutomationRule
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let fixedAssetAutomationRule: FixedAssetAutomationRule; //

const { status, data } = await apiInstance.coaApiFixedAssetAutomationCreate(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetAutomationDestroy**
> coaApiFixedAssetAutomationDestroy()

Retrieve, update, or delete an automation rule. GET/PUT/PATCH/DELETE /api/fixed-asset-automation/<id>/

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiFixedAssetAutomationDestroy(
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

# **coaApiFixedAssetAutomationList**
> PaginatedFixedAssetAutomationRuleList coaApiFixedAssetAutomationList()

List all automation rules or create a new one. GET /api/fixed-asset-automation/ POST /api/fixed-asset-automation/

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let ordering: string; //Which field to use when ordering the results. (optional) (default to undefined)
let search: string; //A search term. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiFixedAssetAutomationList(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetAutomationMatchPartialUpdate**
> FixedAssetAutomationMatch coaApiFixedAssetAutomationMatchPartialUpdate()

Retrieve or update an automation match (for editing proposed values before acceptance). GET/PATCH /api/fixed-asset-automation-match/<id>/

### Example

```typescript
import {
    CoaApi,
    Configuration,
    PatchedFixedAssetAutomationMatch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)
let patchedFixedAssetAutomationMatch: PatchedFixedAssetAutomationMatch; // (optional)

const { status, data } = await apiInstance.coaApiFixedAssetAutomationMatchPartialUpdate(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetAutomationMatchRetrieve**
> FixedAssetAutomationMatch coaApiFixedAssetAutomationMatchRetrieve()

Retrieve or update an automation match (for editing proposed values before acceptance). GET/PATCH /api/fixed-asset-automation-match/<id>/

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiFixedAssetAutomationMatchRetrieve(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetAutomationMatchUpdate**
> FixedAssetAutomationMatch coaApiFixedAssetAutomationMatchUpdate(fixedAssetAutomationMatch)

Retrieve or update an automation match (for editing proposed values before acceptance). GET/PATCH /api/fixed-asset-automation-match/<id>/

### Example

```typescript
import {
    CoaApi,
    Configuration,
    FixedAssetAutomationMatch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)
let fixedAssetAutomationMatch: FixedAssetAutomationMatch; //

const { status, data } = await apiInstance.coaApiFixedAssetAutomationMatchUpdate(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetAutomationMatchesList**
> PaginatedFixedAssetAutomationMatchList coaApiFixedAssetAutomationMatchesList()

List pending asset matches for review. GET /api/fixed-asset-automation/matches

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)
let ordering: string; //Which field to use when ordering the results. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiFixedAssetAutomationMatchesList(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetAutomationPartialUpdate**
> FixedAssetAutomationRule coaApiFixedAssetAutomationPartialUpdate()

Retrieve, update, or delete an automation rule. GET/PUT/PATCH/DELETE /api/fixed-asset-automation/<id>/

### Example

```typescript
import {
    CoaApi,
    Configuration,
    PatchedFixedAssetAutomationRule
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)
let patchedFixedAssetAutomationRule: PatchedFixedAssetAutomationRule; // (optional)

const { status, data } = await apiInstance.coaApiFixedAssetAutomationPartialUpdate(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetAutomationRetrieve**
> FixedAssetAutomationRule coaApiFixedAssetAutomationRetrieve()

Retrieve, update, or delete an automation rule. GET/PUT/PATCH/DELETE /api/fixed-asset-automation/<id>/

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiFixedAssetAutomationRetrieve(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiFixedAssetAutomationRunCreate**
> coaApiFixedAssetAutomationRunCreate()

Trigger automation processing. POST /api/fixed-asset-automation/run  Optional body: {\"rule_id\": 123}

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiFixedAssetAutomationRunCreate();
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

# **coaApiFixedAssetAutomationUpdate**
> FixedAssetAutomationRule coaApiFixedAssetAutomationUpdate(fixedAssetAutomationRule)

Retrieve, update, or delete an automation rule. GET/PUT/PATCH/DELETE /api/fixed-asset-automation/<id>/

### Example

```typescript
import {
    CoaApi,
    Configuration,
    FixedAssetAutomationRule
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)
let fixedAssetAutomationRule: FixedAssetAutomationRule; //

const { status, data } = await apiInstance.coaApiFixedAssetAutomationUpdate(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTransactionBulkUpdateCreate**
> coaApiTransactionBulkUpdateCreate()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiTransactionBulkUpdateCreate();
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

# **coaApiTransactionMatchProcessCreate**
> coaApiTransactionMatchProcessCreate()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiTransactionMatchProcessCreate();
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

# **coaApiTransactionMatchesCountRetrieve**
> coaApiTransactionMatchesCountRetrieve()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiTransactionMatchesCountRetrieve();
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

# **coaApiTransactionMatchesDestroy**
> coaApiTransactionMatchesDestroy()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionMatchesDestroy(
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

# **coaApiTransactionMatchesList**
> PaginatedTransactionMatchList coaApiTransactionMatchesList()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionMatchesList(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTransactionMatchesPartialUpdate**
> TransactionMatch coaApiTransactionMatchesPartialUpdate()


### Example

```typescript
import {
    CoaApi,
    Configuration,
    PatchedTransactionMatch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)
let patchedTransactionMatch: PatchedTransactionMatch; // (optional)

const { status, data } = await apiInstance.coaApiTransactionMatchesPartialUpdate(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTransactionMatchesRejectCreate**
> coaApiTransactionMatchesRejectCreate()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionMatchesRejectCreate(
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

# **coaApiTransactionMatchesRetrieve**
> TransactionMatch coaApiTransactionMatchesRetrieve()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionMatchesRetrieve(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTransactionMatchesStatusCreate**
> coaApiTransactionMatchesStatusCreate()

Handle POST requests with \'action\' parameter (accept/reject)

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionMatchesStatusCreate(
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

# **coaApiTransactionMatchesStatusUpdate**
> coaApiTransactionMatchesStatusUpdate()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiTransactionMatchesStatusUpdate(
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

# **coaApiTransactionMatchesUpdate**
> TransactionMatch coaApiTransactionMatchesUpdate(transactionMatch)


### Example

```typescript
import {
    CoaApi,
    Configuration,
    TransactionMatch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)
let transactionMatch: TransactionMatch; //

const { status, data } = await apiInstance.coaApiTransactionMatchesUpdate(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTransactionMergeCreate**
> JournalEntry coaApiTransactionMergeCreate()

         Merge two offsetting chart transactions from different journals.          This endpoint consolidates journals containing offsetting transactions by removing         the specified transactions and combining the remaining transactions into a single journal entry.          **Request Body:**         - `transaction_ids` (array, required): Array of exactly two transaction IDs to merge          **Returns:**         The merged journal entry with all remaining transactions.          **Requirements:**         - Must provide exactly two transaction IDs         - Transactions must be from different journals         - Transactions must have matching amounts         - Transactions must belong to the same entity          **Result:**         - The two specified transactions are deleted         - Other transactions from both journals are consolidated into a single journal         - A draft queue record is created for audit purposes and auto-approved         

### Example

```typescript
import {
    CoaApi,
    Configuration,
    CoaApiTransactionMergeCreateRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let coaApiTransactionMergeCreateRequest: CoaApiTransactionMergeCreateRequest; // (optional)

const { status, data } = await apiInstance.coaApiTransactionMergeCreate(
    coaApiTransactionMergeCreateRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **coaApiTransactionMergeCreateRequest** | **CoaApiTransactionMergeCreateRequest**|  | |


### Return type

**JournalEntry**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |
|**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiTransactionMergeRetrieve**
> JournalEntry coaApiTransactionMergeRetrieve()

         Preview the result of merging two chart transactions.          This endpoint shows what the merged journal entry will look like, allowing you to verify         the merge before committing. The preview includes the journal that will be retained and         the transactions that will remain after the merge.          **Parameters:**         - `transaction_ids` (query, required): Comma-separated list of exactly two transaction IDs          **Returns:**         A journal entry object containing the merged result with all remaining transactions.          **Requirements:**         - Must provide exactly two transaction IDs         - Transactions must be from different journals         - Transactions must have matching amounts         - Transactions must belong to the same entity         

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiTransactionMergeRetrieve();
```

### Parameters
This endpoint does not have any parameters.


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
|**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1BillAmortizationCreate**
> coaApiV1BillAmortizationCreate()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiV1BillAmortizationCreate();
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

# **coaApiV1BillAmortizationCreate2**
> coaApiV1BillAmortizationCreate2()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let billId: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1BillAmortizationCreate2(
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1BillAmortizationDestroy**
> coaApiV1BillAmortizationDestroy()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiV1BillAmortizationDestroy();
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
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1BillAmortizationDestroy2**
> coaApiV1BillAmortizationDestroy2()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let billId: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1BillAmortizationDestroy2(
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
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1BillAmortizationGenerateScheduleRetrieve**
> coaApiV1BillAmortizationGenerateScheduleRetrieve()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiV1BillAmortizationGenerateScheduleRetrieve();
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

# **coaApiV1BillAmortizationGenerateScheduleUpdate**
> coaApiV1BillAmortizationGenerateScheduleUpdate()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiV1BillAmortizationGenerateScheduleUpdate();
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

# **coaApiV1BillAmortizationRetrieve**
> coaApiV1BillAmortizationRetrieve()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiV1BillAmortizationRetrieve();
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

# **coaApiV1BillAmortizationRetrieve2**
> coaApiV1BillAmortizationRetrieve2()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let billId: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1BillAmortizationRetrieve2(
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiV1CreditMemoPdfRetrieve**
> coaApiV1CreditMemoPdfRetrieve()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1CreditMemoPdfRetrieve(
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

# **coaApiV1CreditMemoSendUpdate**
> coaApiV1CreditMemoSendUpdate()

Send a single credit memo via email.

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1CreditMemoSendUpdate(
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

# **coaApiV1InvoiceStatementClientPdfRetrieve**
> coaApiV1InvoiceStatementClientPdfRetrieve()

Generate a customer statement PDF for a specific client.  This creates a professional, customer-facing statement showing: - All outstanding invoices as of the specified date - Running balance - Total balance due - Payment advice slip

### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let clientId: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiV1InvoiceStatementClientPdfRetrieve(
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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coaApiVendorCustomField1Create**
> VendorCustomField1 coaApiVendorCustomField1Create()


### Example

```typescript
import {
    CoaApi,
    Configuration,
    VendorCustomField1
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let vendorCustomField1: VendorCustomField1; // (optional)

const { status, data } = await apiInstance.coaApiVendorCustomField1Create(
    vendorCustomField1
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **vendorCustomField1** | **VendorCustomField1**|  | |


### Return type

**VendorCustomField1**

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

# **coaApiVendorCustomField1Destroy**
> coaApiVendorCustomField1Destroy()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiVendorCustomField1Destroy(
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

# **coaApiVendorCustomField1List**
> Array<VendorCustomField1> coaApiVendorCustomField1List()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

const { status, data } = await apiInstance.coaApiVendorCustomField1List();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<VendorCustomField1>**

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

# **coaApiVendorCustomField1PartialUpdate**
> VendorCustomField1 coaApiVendorCustomField1PartialUpdate()


### Example

```typescript
import {
    CoaApi,
    Configuration,
    PatchedVendorCustomField1
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)
let patchedVendorCustomField1: PatchedVendorCustomField1; // (optional)

const { status, data } = await apiInstance.coaApiVendorCustomField1PartialUpdate(
    id,
    patchedVendorCustomField1
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedVendorCustomField1** | **PatchedVendorCustomField1**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**VendorCustomField1**

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

# **coaApiVendorCustomField1Retrieve**
> VendorCustomField1 coaApiVendorCustomField1Retrieve()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.coaApiVendorCustomField1Retrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**VendorCustomField1**

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

# **coaApiVendorCustomField1Update**
> VendorCustomField1 coaApiVendorCustomField1Update()


### Example

```typescript
import {
    CoaApi,
    Configuration,
    VendorCustomField1
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let id: number; // (default to undefined)
let vendorCustomField1: VendorCustomField1; // (optional)

const { status, data } = await apiInstance.coaApiVendorCustomField1Update(
    id,
    vendorCustomField1
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **vendorCustomField1** | **VendorCustomField1**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**VendorCustomField1**

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

# **coaApiVendorSummaryList**
> PaginatedVendorSummaryList coaApiVendorSummaryList()


### Example

```typescript
import {
    CoaApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CoaApi(configuration);

let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.coaApiVendorSummaryList(
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

**PaginatedVendorSummaryList**

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


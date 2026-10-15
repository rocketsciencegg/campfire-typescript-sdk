# RevenueRecognitionApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**createContract**](#createcontract) | **POST** /rr/api/v1/contracts | Create Contract|
|[**createContractBundle**](#createcontractbundle) | **POST** /rr/api/v1/contracts/{contract_id}/bundles | Create Contract Bundle|
|[**createContractMilestone**](#createcontractmilestone) | **POST** /rr/api/v1/contracts/{contract_id}/milestones | Create Contract Milestone|
|[**createContractSubscription**](#createcontractsubscription) | **POST** /rr/api/v1/contracts/{contract_id}/subscriptions | Create Contract Subscription|
|[**createPrepaidCommit**](#createprepaidcommit) | **POST** /rr/api/v1/contracts/{contract_id}/prepaid-commits | Create Prepaid Commit|
|[**createPrepaidCommitConsumption**](#createprepaidcommitconsumption) | **POST** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{commit_id}/consumption | Create Prepaid Commit Consumption|
|[**createProduct**](#createproduct) | **POST** /rr/api/v1/product | Create Contract Product|
|[**createProductBundle**](#createproductbundle) | **POST** /rr/api/v1/product-bundles | Create Product Bundle|
|[**createRevenueTransaction**](#createrevenuetransaction) | **POST** /rr/api/v1/transactions | Create Revenue Transaction|
|[**deletePrepaidCommit**](#deleteprepaidcommit) | **DELETE** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{id} | Delete Prepaid Commit|
|[**deletePrepaidCommitConsumption**](#deleteprepaidcommitconsumption) | **DELETE** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{commit_id}/consumption/{id} | Delete Prepaid Commit Consumption|
|[**getPrepaidCommit**](#getprepaidcommit) | **GET** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{id} | Retrieve Prepaid Commit|
|[**getPrepaidCommitSummary**](#getprepaidcommitsummary) | **GET** /rr/api/v1/contracts/{contract_id}/prepaid-commit-summary | Get Prepaid Commit Summary|
|[**getPrepaidCommitUsageEventDistinctValues**](#getprepaidcommitusageeventdistinctvalues) | **GET** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{commit_id}/usage-events/distinct-values | Get Prepaid Commit Usage Event Distinct Values|
|[**getPrepaidCommitUsageEventsTemplate**](#getprepaidcommitusageeventstemplate) | **GET** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{commit_id}/usage-events/template | Get Prepaid Commit Usage Events Template|
|[**listContractBundles**](#listcontractbundles) | **GET** /rr/api/v1/contracts/{contract_id}/bundles | List Contract Bundles|
|[**listContractMilestones**](#listcontractmilestones) | **GET** /rr/api/v1/contracts/{contract_id}/milestones | List Contract Milestones|
|[**listContractSubscriptions**](#listcontractsubscriptions) | **GET** /rr/api/v1/contracts/{contract_id}/subscriptions | List Contract Subscriptions|
|[**listContracts**](#listcontracts) | **GET** /rr/api/v1/contracts | List Contracts|
|[**listPrepaidCommitConsumption**](#listprepaidcommitconsumption) | **GET** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{commit_id}/consumption | List Prepaid Commit Consumption|
|[**listPrepaidCommitUsageEvents**](#listprepaidcommitusageevents) | **GET** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{commit_id}/usage-events | List Prepaid Commit Usage Events|
|[**listPrepaidCommits**](#listprepaidcommits) | **GET** /rr/api/v1/contracts/{contract_id}/prepaid-commits | List Prepaid Commits|
|[**listProductBundles**](#listproductbundles) | **GET** /rr/api/v1/product-bundles | List Product Bundles|
|[**listProducts**](#listproducts) | **GET** /rr/api/v1/product | List Contract Products|
|[**listRevenueTransactions**](#listrevenuetransactions) | **GET** /rr/api/v1/transactions | List Revenue Transactions|
|[**modifySubscriptionSchedule**](#modifysubscriptionschedule) | **POST** /rr/api/v1/modify-subscription-schedule | Modify Subscription Schedule|
|[**parseContract**](#parsecontract) | **POST** /rr/api/v1/contracts/parse | Parse Contract|
|[**partialUpdatePrepaidCommit**](#partialupdateprepaidcommit) | **PATCH** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{id} | Partial Update Prepaid Commit|
|[**processPrepaidCommitAdjustments**](#processprepaidcommitadjustments) | **POST** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{commit_id}/process-adjustments | Process Prepaid Commit Adjustments|
|[**reverseContractSubscriptionFully**](#reversecontractsubscriptionfully) | **POST** /rr/api/v1/contracts/{contract_id}/subscriptions/{id}/full-reversal | Fully reverse a usage-relative subscription|
|[**rrApiV1ContractsBulkSearchCreate**](#rrapiv1contractsbulksearchcreate) | **POST** /rr/api/v1/contracts/bulk-search | Bulk Search Contracts|
|[**rrApiV1ContractsBundlesDestroy**](#rrapiv1contractsbundlesdestroy) | **DELETE** /rr/api/v1/contracts/{contract_id}/bundles/{id} | Delete Contract Bundle|
|[**rrApiV1ContractsBundlesPartialUpdate**](#rrapiv1contractsbundlespartialupdate) | **PATCH** /rr/api/v1/contracts/{contract_id}/bundles/{id} | Partial Update Contract Bundle|
|[**rrApiV1ContractsBundlesRetrieve**](#rrapiv1contractsbundlesretrieve) | **GET** /rr/api/v1/contracts/{contract_id}/bundles/{id} | Retrieve Contract Bundle|
|[**rrApiV1ContractsBundlesUpdate**](#rrapiv1contractsbundlesupdate) | **PUT** /rr/api/v1/contracts/{contract_id}/bundles/{id} | Update Contract Bundle|
|[**rrApiV1ContractsDestroy**](#rrapiv1contractsdestroy) | **DELETE** /rr/api/v1/contracts/{id} | Delete Contract|
|[**rrApiV1ContractsDuplicateCreate**](#rrapiv1contractsduplicatecreate) | **POST** /rr/api/v1/contracts/{id}/duplicate | Duplicate Contract|
|[**rrApiV1ContractsMilestonesAllocationsPartialUpdate**](#rrapiv1contractsmilestonesallocationspartialupdate) | **PATCH** /rr/api/v1/contracts/{contract_id}/milestones/{milestone_id}/allocations | Partial Update Bundle Allocations|
|[**rrApiV1ContractsMilestonesAllocationsRetrieve**](#rrapiv1contractsmilestonesallocationsretrieve) | **GET** /rr/api/v1/contracts/{contract_id}/milestones/{milestone_id}/allocations | Get Bundle Allocations|
|[**rrApiV1ContractsMilestonesAllocationsUpdate**](#rrapiv1contractsmilestonesallocationsupdate) | **PUT** /rr/api/v1/contracts/{contract_id}/milestones/{milestone_id}/allocations | Update Bundle Allocations|
|[**rrApiV1ContractsMilestonesDestroy**](#rrapiv1contractsmilestonesdestroy) | **DELETE** /rr/api/v1/contracts/{contract_id}/milestones/{id} | Delete Contract Milestone|
|[**rrApiV1ContractsMilestonesPartialUpdate**](#rrapiv1contractsmilestonespartialupdate) | **PATCH** /rr/api/v1/contracts/{contract_id}/milestones/{id} | Partial Update Contract Milestone|
|[**rrApiV1ContractsMilestonesRetrieve**](#rrapiv1contractsmilestonesretrieve) | **GET** /rr/api/v1/contracts/{contract_id}/milestones/{id} | Retrieve Contract Milestone|
|[**rrApiV1ContractsMilestonesUpdate**](#rrapiv1contractsmilestonesupdate) | **PUT** /rr/api/v1/contracts/{contract_id}/milestones/{id} | Update Contract Milestone|
|[**rrApiV1ContractsMinimumCommitPreviewRetrieve**](#rrapiv1contractsminimumcommitpreviewretrieve) | **GET** /rr/api/v1/contracts/{id}/minimum-commit-preview | Preview Contract Minimum Commit|
|[**rrApiV1ContractsPartialUpdate**](#rrapiv1contractspartialupdate) | **PATCH** /rr/api/v1/contracts/{id} | Partial Update Contract|
|[**rrApiV1ContractsRetrieve**](#rrapiv1contractsretrieve) | **GET** /rr/api/v1/contracts/{id} | Retrieve Contract|
|[**rrApiV1ContractsSubscriptionsAllocationsPartialUpdate**](#rrapiv1contractssubscriptionsallocationspartialupdate) | **PATCH** /rr/api/v1/contracts/{contract_id}/subscriptions/{subscription_id}/allocations | Partial Update Bundle Allocations|
|[**rrApiV1ContractsSubscriptionsAllocationsRetrieve**](#rrapiv1contractssubscriptionsallocationsretrieve) | **GET** /rr/api/v1/contracts/{contract_id}/subscriptions/{subscription_id}/allocations | Get Bundle Allocations|
|[**rrApiV1ContractsSubscriptionsAllocationsUpdate**](#rrapiv1contractssubscriptionsallocationsupdate) | **PUT** /rr/api/v1/contracts/{contract_id}/subscriptions/{subscription_id}/allocations | Update Bundle Allocations|
|[**rrApiV1ContractsSubscriptionsDestroy**](#rrapiv1contractssubscriptionsdestroy) | **DELETE** /rr/api/v1/contracts/{contract_id}/subscriptions/{id} | Delete Contract Subscription|
|[**rrApiV1ContractsSubscriptionsPartialUpdate**](#rrapiv1contractssubscriptionspartialupdate) | **PATCH** /rr/api/v1/contracts/{contract_id}/subscriptions/{id} | Partial Update Contract Subscription|
|[**rrApiV1ContractsSubscriptionsRetrieve**](#rrapiv1contractssubscriptionsretrieve) | **GET** /rr/api/v1/contracts/{contract_id}/subscriptions/{id} | Retrieve Contract Subscription|
|[**rrApiV1ContractsSubscriptionsUpdate**](#rrapiv1contractssubscriptionsupdate) | **PUT** /rr/api/v1/contracts/{contract_id}/subscriptions/{id} | Update Contract Subscription|
|[**rrApiV1ContractsTerminateCreate**](#rrapiv1contractsterminatecreate) | **POST** /rr/api/v1/contracts/{id}/terminate | Terminate Contract|
|[**rrApiV1ContractsTerminationSettlementPreviewRetrieve**](#rrapiv1contractsterminationsettlementpreviewretrieve) | **GET** /rr/api/v1/contracts/{id}/termination-settlement-preview | Preview Contract Termination Settlement|
|[**rrApiV1ContractsTierPriceOverridesCreate**](#rrapiv1contractstierpriceoverridescreate) | **POST** /rr/api/v1/contracts/{contract_id}/tier-price-overrides | Create Contract Tier Price Override|
|[**rrApiV1ContractsTierPriceOverridesList**](#rrapiv1contractstierpriceoverrideslist) | **GET** /rr/api/v1/contracts/{contract_id}/tier-price-overrides | List Contract Tier Price Overrides|
|[**rrApiV1ContractsUpdate**](#rrapiv1contractsupdate) | **PUT** /rr/api/v1/contracts/{id} | Update Contract|
|[**rrApiV1ContractsUsageAllocationsPartialUpdate**](#rrapiv1contractsusageallocationspartialupdate) | **PATCH** /rr/api/v1/contracts/{contract_id}/usage/{usage_id}/allocations | Partial Update Bundle Allocations|
|[**rrApiV1ContractsUsageAllocationsRetrieve**](#rrapiv1contractsusageallocationsretrieve) | **GET** /rr/api/v1/contracts/{contract_id}/usage/{usage_id}/allocations | Get Bundle Allocations|
|[**rrApiV1ContractsUsageAllocationsUpdate**](#rrapiv1contractsusageallocationsupdate) | **PUT** /rr/api/v1/contracts/{contract_id}/usage/{usage_id}/allocations | Update Bundle Allocations|
|[**rrApiV1ContractsUsageCreate**](#rrapiv1contractsusagecreate) | **POST** /rr/api/v1/contracts/{contract_id}/usage | Create Contract Usage Revenue|
|[**rrApiV1ContractsUsageDestroy**](#rrapiv1contractsusagedestroy) | **DELETE** /rr/api/v1/contracts/{contract_id}/usage/{id} | Delete Contract Usage Revenue|
|[**rrApiV1ContractsUsageList**](#rrapiv1contractsusagelist) | **GET** /rr/api/v1/contracts/{contract_id}/usage | List Contract Usage Revenue|
|[**rrApiV1ContractsUsagePartialUpdate**](#rrapiv1contractsusagepartialupdate) | **PATCH** /rr/api/v1/contracts/{contract_id}/usage/{id} | Partially Update Contract Usage Revenue|
|[**rrApiV1ContractsUsageRetrieve**](#rrapiv1contractsusageretrieve) | **GET** /rr/api/v1/contracts/{contract_id}/usage/{id} | Retrieve Contract Usage Revenue|
|[**rrApiV1ContractsUsageUpdate**](#rrapiv1contractsusageupdate) | **PUT** /rr/api/v1/contracts/{contract_id}/usage/{id} | Update Contract Usage Revenue|
|[**rrApiV1CustomersDestroy**](#rrapiv1customersdestroy) | **DELETE** /rr/api/v1/customers/{id} | Delete Contract Customer|
|[**rrApiV1CustomersList**](#rrapiv1customerslist) | **GET** /rr/api/v1/customers | List Contract Customers|
|[**rrApiV1CustomersPartialUpdate**](#rrapiv1customerspartialupdate) | **PATCH** /rr/api/v1/customers/{id} | Partial Update Contract Customer|
|[**rrApiV1CustomersRetrieve**](#rrapiv1customersretrieve) | **GET** /rr/api/v1/customers/{id} | Retrieve Contract Customer|
|[**rrApiV1CustomersUpdate**](#rrapiv1customersupdate) | **PUT** /rr/api/v1/customers/{id} | Update Contract Customer|
|[**rrApiV1ProductBulkSearchCreate**](#rrapiv1productbulksearchcreate) | **POST** /rr/api/v1/product/bulk-search | Bulk Search Products|
|[**rrApiV1ProductBundlesDestroy**](#rrapiv1productbundlesdestroy) | **DELETE** /rr/api/v1/product-bundles/{id} | Delete Product Bundle|
|[**rrApiV1ProductBundlesPartialUpdate**](#rrapiv1productbundlespartialupdate) | **PATCH** /rr/api/v1/product-bundles/{id} | Partial Update Product Bundle|
|[**rrApiV1ProductBundlesRetrieve**](#rrapiv1productbundlesretrieve) | **GET** /rr/api/v1/product-bundles/{id} | Retrieve Product Bundle|
|[**rrApiV1ProductBundlesUpdate**](#rrapiv1productbundlesupdate) | **PUT** /rr/api/v1/product-bundles/{id} | Update Product Bundle|
|[**rrApiV1ProductDeleteCreate**](#rrapiv1productdeletecreate) | **POST** /rr/api/v1/product/{id}/delete | Delete Product|
|[**rrApiV1ProductDestroy**](#rrapiv1productdestroy) | **DELETE** /rr/api/v1/product/{id} | Delete Product (deprecated)|
|[**rrApiV1ProductPartialUpdate**](#rrapiv1productpartialupdate) | **PATCH** /rr/api/v1/product/{id} | Partial Update Product|
|[**rrApiV1ProductRetrieve**](#rrapiv1productretrieve) | **GET** /rr/api/v1/product/{id} | Retrieve Product|
|[**rrApiV1ProductUpdate**](#rrapiv1productupdate) | **PUT** /rr/api/v1/product/{id} | Update Product|
|[**rrApiV1TransactionsDestroy**](#rrapiv1transactionsdestroy) | **DELETE** /rr/api/v1/transactions/{id} | Delete Revenue Transaction|
|[**rrApiV1TransactionsPartialUpdate**](#rrapiv1transactionspartialupdate) | **PATCH** /rr/api/v1/transactions/{id} | Partial Update Revenue Transaction|
|[**rrApiV1TransactionsRetrieve**](#rrapiv1transactionsretrieve) | **GET** /rr/api/v1/transactions/{id} | Retrieve Revenue Transaction|
|[**rrApiV1TransactionsUpdate**](#rrapiv1transactionsupdate) | **PUT** /rr/api/v1/transactions/{id} | Update Revenue Transaction|
|[**updatePrepaidCommit**](#updateprepaidcommit) | **PUT** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{id} | Update Prepaid Commit|
|[**updatePrepaidCommitConsumption**](#updateprepaidcommitconsumption) | **PUT** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{commit_id}/consumption/{id} | Update Prepaid Commit Consumption|
|[**uploadPrepaidCommitUsageEvents**](#uploadprepaidcommitusageevents) | **POST** /rr/api/v1/contracts/{contract_id}/prepaid-commits/{commit_id}/usage-events/upload | Upload Prepaid Commit Usage Events|

# **createContract**
> Contract createContract(contract)

     Create a new contract.      Evergreen vs standard:     - Standard contract: set is_evergreen=false and provide a fixed contract_end_date.     - Evergreen contract: set is_evergreen=true and leave contract_end_date as null.       The system manages a rolling effective_end_date, exposes working_end_date for downstream usage,       and returns evergreen_locked_date for immutable historical boundary rules.      Additional evergreen constraints:     - is_evergreen and auto_renew cannot both be true.     - billing_frequency is required for evergreen behavior.     - default_payment_term is not implemented yet for standard contracts. It can currently be set only for Evergreen       contracts and is applied to their automatically generated invoices. Other contract invoice flows retain their       existing payment-term selection behavior; support may be extended to additional contract types in the future.     - When default_payment_term is omitted or null, automatically generated Evergreen invoices retain the existing       Net 30 fallback.     - skip_evergreen_invoice_generation is creation-time only and cannot be changed on existing contracts.     - skip_evergreen_invoice_generation=true skips only Campfire\'s auto-generated evergreen invoices.       Revenue transactions still generate.     

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    Contract
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contract: Contract; //

const { status, data } = await apiInstance.createContract(
    contract
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contract** | **Contract**|  | |


### Return type

**Contract**

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

# **createContractBundle**
> ContractBundle createContractBundle(contractBundle)

     Create a new contract bundle.      Evergreen vs standard:     - Standard contracts require a fixed bundle end_date.     - Evergreen contracts allow end_date to be null (open-ended) or set to a billing-period end date.       Evergreen bundle start/end dates must align with billing period boundaries.      Evergreen-specific option:     - rebalance_journal_entries_indefinitely=true keeps invoice-journal rebalancing in sync as the evergreen       contract extends.     

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractBundle
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let contractBundle: ContractBundle; //

const { status, data } = await apiInstance.createContractBundle(
    contractId,
    contractBundle
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractBundle** | **ContractBundle**|  | |
| **contractId** | [**number**] |  | defaults to undefined|


### Return type

**ContractBundle**

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

# **createContractMilestone**
> ContractMilestone createContractMilestone(contractMilestone)

Create a new milestone for a contract. This will automatically create an associated revenue transaction.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractMilestone
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let contractMilestone: ContractMilestone; //

const { status, data } = await apiInstance.createContractMilestone(
    contractId,
    contractMilestone
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractMilestone** | **ContractMilestone**|  | |
| **contractId** | [**number**] |  | defaults to undefined|


### Return type

**ContractMilestone**

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

# **createContractSubscription**
> ContractSubscription createContractSubscription(contractSubscription)

     Create a new contract subscription.      Evergreen vs standard:     - Standard contract subscriptions generally provide explicit lines and fixed start/end dates.     - Evergreen contract subscriptions can provide period_amount to auto-generate lines. Their dates must align       to billing period boundaries and must not exceed the contract\'s current working_end_date.      Notes:     - Usage and milestone subscription flows are not supported for evergreen contracts.     - For evergreen contracts, period_amount is the source-of-truth amount per billing period.     - renewal_behavior:       - FOLLOW_CONTRACT: subscription follows evergreen contract extension windows.       - FIXED_END: subscription keeps its own fixed end_date and does not extend automatically.     

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractSubscription
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let contractSubscription: ContractSubscription; //

const { status, data } = await apiInstance.createContractSubscription(
    contractId,
    contractSubscription
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractSubscription** | **ContractSubscription**|  | |
| **contractId** | [**number**] |  | defaults to undefined|


### Return type

**ContractSubscription**

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

# **createPrepaidCommit**
> ContractPrepaidCommit createPrepaidCommit(contractPrepaidCommit)


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractPrepaidCommit
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let contractPrepaidCommit: ContractPrepaidCommit; //

const { status, data } = await apiInstance.createPrepaidCommit(
    contractId,
    contractPrepaidCommit
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractPrepaidCommit** | **ContractPrepaidCommit**|  | |
| **contractId** | [**number**] |  | defaults to undefined|


### Return type

**ContractPrepaidCommit**

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

# **createPrepaidCommitConsumption**
> RecordConsumptionInput createPrepaidCommitConsumption(recordConsumptionInput)


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    RecordConsumptionInput
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let commitId: number; // (default to undefined)
let contractId: number; // (default to undefined)
let recordConsumptionInput: RecordConsumptionInput; //

const { status, data } = await apiInstance.createPrepaidCommitConsumption(
    commitId,
    contractId,
    recordConsumptionInput
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **recordConsumptionInput** | **RecordConsumptionInput**|  | |
| **commitId** | [**number**] |  | defaults to undefined|
| **contractId** | [**number**] |  | defaults to undefined|


### Return type

**RecordConsumptionInput**

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

# **createProduct**
> Product createProduct(product)

Create a new product

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    Product
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

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

# **createProductBundle**
> ProductBundle createProductBundle(productBundle)

Create a new product bundle with products and percentage allocations. Total percentage must equal 100.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ProductBundle
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let productBundle: ProductBundle; //

const { status, data } = await apiInstance.createProductBundle(
    productBundle
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **productBundle** | **ProductBundle**|  | |


### Return type

**ProductBundle**

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

# **createRevenueTransaction**
> RevenueTransaction createRevenueTransaction(revenueTransaction)

Create a new revenue transaction

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    RevenueTransaction
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let revenueTransaction: RevenueTransaction; //

const { status, data } = await apiInstance.createRevenueTransaction(
    revenueTransaction
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **revenueTransaction** | **RevenueTransaction**|  | |


### Return type

**RevenueTransaction**

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

# **deletePrepaidCommit**
> deletePrepaidCommit()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.deletePrepaidCommit(
    contractId,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
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

# **deletePrepaidCommitConsumption**
> deletePrepaidCommitConsumption()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let commitId: number; // (default to undefined)
let contractId: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.deletePrepaidCommitConsumption(
    commitId,
    contractId,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **commitId** | [**number**] |  | defaults to undefined|
| **contractId** | [**number**] |  | defaults to undefined|
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

# **getPrepaidCommit**
> ContractPrepaidCommit getPrepaidCommit()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.getPrepaidCommit(
    contractId,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractPrepaidCommit**

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

# **getPrepaidCommitSummary**
> getPrepaidCommitSummary()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)

const { status, data } = await apiInstance.getPrepaidCommitSummary(
    contractId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|


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

# **getPrepaidCommitUsageEventDistinctValues**
> getPrepaidCommitUsageEventDistinctValues()

Return distinct values for a given JSONB data field, for filter dropdowns.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let commitId: number; // (default to undefined)
let contractId: number; // (default to undefined)

const { status, data } = await apiInstance.getPrepaidCommitUsageEventDistinctValues(
    commitId,
    contractId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **commitId** | [**number**] |  | defaults to undefined|
| **contractId** | [**number**] |  | defaults to undefined|


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

# **getPrepaidCommitUsageEventsTemplate**
> getPrepaidCommitUsageEventsTemplate()

Download a CSV template (commit-scoped).

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let commitId: number; // (default to undefined)
let contractId: number; // (default to undefined)

const { status, data } = await apiInstance.getPrepaidCommitUsageEventsTemplate(
    commitId,
    contractId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **commitId** | [**number**] |  | defaults to undefined|
| **contractId** | [**number**] |  | defaults to undefined|


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

# **listContractBundles**
> Array<ContractBundle> listContractBundles()

         Retrieve a list of contract bundles with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)

const { status, data } = await apiInstance.listContractBundles(
    contractId,
    includeDeleted,
    lastModifiedAtGte,
    lastModifiedAtLte
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|


### Return type

**Array<ContractBundle>**

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

# **listContractMilestones**
> PaginatedContractMilestoneList listContractMilestones()

         Retrieve a list of milestones for a specific contract with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listContractMilestones(
    contractId,
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
| **contractId** | [**number**] |  | defaults to undefined|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedContractMilestoneList**

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

# **listContractSubscriptions**
> Array<ContractSubscription> listContractSubscriptions()

         Retrieve a list of contract subscriptions with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)

const { status, data } = await apiInstance.listContractSubscriptions(
    contractId,
    includeDeleted,
    lastModifiedAtGte,
    lastModifiedAtLte
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **includeDeleted** | [**boolean**] | When set to \&#39;true\&#39;, returns ONLY deleted records instead of active records. Deleted records contain minimal data: \&#39;id\&#39;, \&#39;is_deleted&#x3D;true\&#39;, \&#39;deleted_at\&#39; timestamp, and \&#39;last_modified_at\&#39;. When \&#39;false\&#39; or omitted, returns ONLY active records. This provides clean separation between active and deleted data. | (optional) defaults to false|
| **lastModifiedAtGte** | [**string**] | Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \&#39;2024-01-01T00:00:00Z\&#39; or \&#39;2024-01-01\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|
| **lastModifiedAtLte** | [**string**] | Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \&#39;2024-12-31T23:59:59Z\&#39; or \&#39;2024-12-31\&#39;). Works with both active records and deleted records (filters by deletion time for deleted records). | (optional) defaults to undefined|


### Return type

**Array<ContractSubscription>**

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

# **listContracts**
> PaginatedContractList listContracts()

         Retrieve a list of contracts with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.          When download=true, triggers an async workflow that generates a ZIP file with         contracts_summary.csv and contracts_detail.csv, uploads to S3, and sends an email         with the download link.         

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listContracts(
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

**PaginatedContractList**

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

# **listPrepaidCommitConsumption**
> PaginatedContractPrepaidCommitConsumptionList listPrepaidCommitConsumption()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let commitId: number; // (default to undefined)
let contractId: number; // (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listPrepaidCommitConsumption(
    commitId,
    contractId,
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **commitId** | [**number**] |  | defaults to undefined|
| **contractId** | [**number**] |  | defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedContractPrepaidCommitConsumptionList**

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

# **listPrepaidCommitUsageEvents**
> PaginatedPrepaidUsageEventList listPrepaidCommitUsageEvents()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let commitId: number; // (default to undefined)
let contractId: number; // (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listPrepaidCommitUsageEvents(
    commitId,
    contractId,
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **commitId** | [**number**] |  | defaults to undefined|
| **contractId** | [**number**] |  | defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedPrepaidUsageEventList**

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

# **listPrepaidCommits**
> PaginatedContractPrepaidCommitList listPrepaidCommits()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listPrepaidCommits(
    contractId,
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedContractPrepaidCommitList**

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

# **listProductBundles**
> PaginatedProductBundleList listProductBundles()

         Retrieve a list of product bundles with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listProductBundles(
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

**PaginatedProductBundleList**

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

# **listProducts**
> PaginatedProductList listProducts()

         Retrieve a list of contract products with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

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

# **listRevenueTransactions**
> PaginatedRevenueTransactionList listRevenueTransactions()

         Retrieve a list of revenue transactions with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.listRevenueTransactions(
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

**PaginatedRevenueTransactionList**

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

# **modifySubscriptionSchedule**
> Array<ContractSubscriptionLine> modifySubscriptionSchedule(generageSubscriptionSchedule)

Generate a modified subscription schedule by comparing a new schedule against an existing subscription. Returns the delta between the original and modified schedules, with support for catch-up accounting and contract end date modifications.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    GenerageSubscriptionSchedule
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let generageSubscriptionSchedule: GenerageSubscriptionSchedule; //

const { status, data } = await apiInstance.modifySubscriptionSchedule(
    generageSubscriptionSchedule
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **generageSubscriptionSchedule** | **GenerageSubscriptionSchedule**|  | |


### Return type

**Array<ContractSubscriptionLine>**

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

# **parseContract**
> parseContract()

Parse contract details from uploaded PDF files using AI.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

const { status, data } = await apiInstance.parseContract();
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

# **partialUpdatePrepaidCommit**
> ContractPrepaidCommit partialUpdatePrepaidCommit()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    PatchedContractPrepaidCommit
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)
let patchedContractPrepaidCommit: PatchedContractPrepaidCommit; // (optional)

const { status, data } = await apiInstance.partialUpdatePrepaidCommit(
    contractId,
    id,
    patchedContractPrepaidCommit
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedContractPrepaidCommit** | **PatchedContractPrepaidCommit**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractPrepaidCommit**

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

# **processPrepaidCommitAdjustments**
> processPrepaidCommitAdjustments()

Process adjustment events for a prepaid commit and create credit memos.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let commitId: number; // (default to undefined)
let contractId: number; // (default to undefined)

const { status, data } = await apiInstance.processPrepaidCommitAdjustments(
    commitId,
    contractId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **commitId** | [**number**] |  | defaults to undefined|
| **contractId** | [**number**] |  | defaults to undefined|


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

# **reverseContractSubscriptionFully**
> ContractSubscriptionFullReversalResponse reverseContractSubscriptionFully(contractSubscriptionFullReversal)

Wraps ``CreateModelMixin.create`` (or any method named ``create``) with ``Idempotency-Key`` handling.  Place this mixin **before** the view\'s other base classes so its ``create`` overrides the inherited one::      class JournalEntryListCreate(         IdempotentCreateMixin,         HistoryFilteringMixin,         ListCreateAPIView,     ):         ...

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractSubscriptionFullReversal
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)
let contractSubscriptionFullReversal: ContractSubscriptionFullReversal; //

const { status, data } = await apiInstance.reverseContractSubscriptionFully(
    contractId,
    id,
    contractSubscriptionFullReversal
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractSubscriptionFullReversal** | **ContractSubscriptionFullReversal**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractSubscriptionFullReversalResponse**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Existing reversal replayed. |  -  |
|**201** | Created |  -  |
|**202** | Reversal submitted for approval; no accounting changes posted. |  -  |
|**400** | The subscription or funding cannot be reversed safely. |  -  |
|**403** | Missing contract or credit-memo permission. |  -  |
|**409** | Usage processing is in progress; retry after it completes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rrApiV1ContractsBulkSearchCreate**
> Array<Contract> rrApiV1ContractsBulkSearchCreate(bulkContractSearch)

Search for contracts by deal_name in a single request.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    BulkContractSearch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let bulkContractSearch: BulkContractSearch; //

const { status, data } = await apiInstance.rrApiV1ContractsBulkSearchCreate(
    bulkContractSearch
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bulkContractSearch** | **BulkContractSearch**|  | |


### Return type

**Array<Contract>**

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

# **rrApiV1ContractsBundlesDestroy**
> rrApiV1ContractsBundlesDestroy()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsBundlesDestroy(
    contractId,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
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

# **rrApiV1ContractsBundlesPartialUpdate**
> ContractBundle rrApiV1ContractsBundlesPartialUpdate()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    PatchedContractBundle
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)
let patchedContractBundle: PatchedContractBundle; // (optional)

const { status, data } = await apiInstance.rrApiV1ContractsBundlesPartialUpdate(
    contractId,
    id,
    patchedContractBundle
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedContractBundle** | **PatchedContractBundle**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractBundle**

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

# **rrApiV1ContractsBundlesRetrieve**
> ContractBundle rrApiV1ContractsBundlesRetrieve()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsBundlesRetrieve(
    contractId,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractBundle**

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

# **rrApiV1ContractsBundlesUpdate**
> ContractBundle rrApiV1ContractsBundlesUpdate(contractBundle)


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractBundle
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)
let contractBundle: ContractBundle; //

const { status, data } = await apiInstance.rrApiV1ContractsBundlesUpdate(
    contractId,
    id,
    contractBundle
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractBundle** | **ContractBundle**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractBundle**

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

# **rrApiV1ContractsDestroy**
> rrApiV1ContractsDestroy()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsDestroy(
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

# **rrApiV1ContractsDuplicateCreate**
> ContractDuplicateResponse rrApiV1ContractsDuplicateCreate()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsDuplicateCreate(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractDuplicateResponse**

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

# **rrApiV1ContractsMilestonesAllocationsPartialUpdate**
> ContractProductBundle rrApiV1ContractsMilestonesAllocationsPartialUpdate()

Partially update bundle allocations. Same behavior as PUT.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    PatchedContractProductBundleUpdate
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let milestoneId: number; // (default to undefined)
let patchedContractProductBundleUpdate: PatchedContractProductBundleUpdate; // (optional)

const { status, data } = await apiInstance.rrApiV1ContractsMilestonesAllocationsPartialUpdate(
    contractId,
    milestoneId,
    patchedContractProductBundleUpdate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedContractProductBundleUpdate** | **PatchedContractProductBundleUpdate**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **milestoneId** | [**number**] |  | defaults to undefined|


### Return type

**ContractProductBundle**

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

# **rrApiV1ContractsMilestonesAllocationsRetrieve**
> ContractProductBundle rrApiV1ContractsMilestonesAllocationsRetrieve()

Retrieve the current bundle allocation details for a contract subscription, milestone, or usage.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let milestoneId: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsMilestonesAllocationsRetrieve(
    contractId,
    milestoneId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **milestoneId** | [**number**] |  | defaults to undefined|


### Return type

**ContractProductBundle**

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

# **rrApiV1ContractsMilestonesAllocationsUpdate**
> ContractProductBundle rrApiV1ContractsMilestonesAllocationsUpdate(contractProductBundleUpdate)

         Update the bundle allocations for a contract item.          The sum of all line amounts must equal the bundle\'s total_amount.         Changes will cascade to related RevenueTransactions and JournalEntries.         

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractProductBundleUpdate
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let milestoneId: number; // (default to undefined)
let contractProductBundleUpdate: ContractProductBundleUpdate; //

const { status, data } = await apiInstance.rrApiV1ContractsMilestonesAllocationsUpdate(
    contractId,
    milestoneId,
    contractProductBundleUpdate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractProductBundleUpdate** | **ContractProductBundleUpdate**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **milestoneId** | [**number**] |  | defaults to undefined|


### Return type

**ContractProductBundle**

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

# **rrApiV1ContractsMilestonesDestroy**
> rrApiV1ContractsMilestonesDestroy()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsMilestonesDestroy(
    contractId,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
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

# **rrApiV1ContractsMilestonesPartialUpdate**
> ContractMilestone rrApiV1ContractsMilestonesPartialUpdate()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    PatchedContractMilestone
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)
let patchedContractMilestone: PatchedContractMilestone; // (optional)

const { status, data } = await apiInstance.rrApiV1ContractsMilestonesPartialUpdate(
    contractId,
    id,
    patchedContractMilestone
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedContractMilestone** | **PatchedContractMilestone**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractMilestone**

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

# **rrApiV1ContractsMilestonesRetrieve**
> ContractMilestone rrApiV1ContractsMilestonesRetrieve()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsMilestonesRetrieve(
    contractId,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractMilestone**

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

# **rrApiV1ContractsMilestonesUpdate**
> ContractMilestone rrApiV1ContractsMilestonesUpdate(contractMilestone)


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractMilestone
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)
let contractMilestone: ContractMilestone; //

const { status, data } = await apiInstance.rrApiV1ContractsMilestonesUpdate(
    contractId,
    id,
    contractMilestone
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractMilestone** | **ContractMilestone**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractMilestone**

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

# **rrApiV1ContractsMinimumCommitPreviewRetrieve**
> rrApiV1ContractsMinimumCommitPreviewRetrieve()

Projected monthly minimum commitment true-up for a contract.  Read-only. Returns the shortfall the month-end batch *would* post if it ran right now. Lets the contract detail screen show a live floor preview without triggering writes from the UI.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsMinimumCommitPreviewRetrieve(
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

# **rrApiV1ContractsPartialUpdate**
> Contract rrApiV1ContractsPartialUpdate()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    PatchedContract
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)
let patchedContract: PatchedContract; // (optional)

const { status, data } = await apiInstance.rrApiV1ContractsPartialUpdate(
    id,
    patchedContract
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedContract** | **PatchedContract**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Contract**

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

# **rrApiV1ContractsRetrieve**
> Contract rrApiV1ContractsRetrieve()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Contract**

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

# **rrApiV1ContractsSubscriptionsAllocationsPartialUpdate**
> ContractProductBundle rrApiV1ContractsSubscriptionsAllocationsPartialUpdate()

Partially update bundle allocations. Same behavior as PUT.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    PatchedContractProductBundleUpdate
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let subscriptionId: number; // (default to undefined)
let patchedContractProductBundleUpdate: PatchedContractProductBundleUpdate; // (optional)

const { status, data } = await apiInstance.rrApiV1ContractsSubscriptionsAllocationsPartialUpdate(
    contractId,
    subscriptionId,
    patchedContractProductBundleUpdate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedContractProductBundleUpdate** | **PatchedContractProductBundleUpdate**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **subscriptionId** | [**number**] |  | defaults to undefined|


### Return type

**ContractProductBundle**

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

# **rrApiV1ContractsSubscriptionsAllocationsRetrieve**
> ContractProductBundle rrApiV1ContractsSubscriptionsAllocationsRetrieve()

Retrieve the current bundle allocation details for a contract subscription, milestone, or usage.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let subscriptionId: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsSubscriptionsAllocationsRetrieve(
    contractId,
    subscriptionId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **subscriptionId** | [**number**] |  | defaults to undefined|


### Return type

**ContractProductBundle**

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

# **rrApiV1ContractsSubscriptionsAllocationsUpdate**
> ContractProductBundle rrApiV1ContractsSubscriptionsAllocationsUpdate(contractProductBundleUpdate)

         Update the bundle allocations for a contract item.          The sum of all line amounts must equal the bundle\'s total_amount.         Changes will cascade to related RevenueTransactions and JournalEntries.         

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractProductBundleUpdate
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let subscriptionId: number; // (default to undefined)
let contractProductBundleUpdate: ContractProductBundleUpdate; //

const { status, data } = await apiInstance.rrApiV1ContractsSubscriptionsAllocationsUpdate(
    contractId,
    subscriptionId,
    contractProductBundleUpdate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractProductBundleUpdate** | **ContractProductBundleUpdate**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **subscriptionId** | [**number**] |  | defaults to undefined|


### Return type

**ContractProductBundle**

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

# **rrApiV1ContractsSubscriptionsDestroy**
> rrApiV1ContractsSubscriptionsDestroy()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsSubscriptionsDestroy(
    contractId,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
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

# **rrApiV1ContractsSubscriptionsPartialUpdate**
> ContractSubscription rrApiV1ContractsSubscriptionsPartialUpdate()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    PatchedContractSubscription
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)
let patchedContractSubscription: PatchedContractSubscription; // (optional)

const { status, data } = await apiInstance.rrApiV1ContractsSubscriptionsPartialUpdate(
    contractId,
    id,
    patchedContractSubscription
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedContractSubscription** | **PatchedContractSubscription**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractSubscription**

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

# **rrApiV1ContractsSubscriptionsRetrieve**
> ContractSubscription rrApiV1ContractsSubscriptionsRetrieve()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsSubscriptionsRetrieve(
    contractId,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractSubscription**

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

# **rrApiV1ContractsSubscriptionsUpdate**
> ContractSubscription rrApiV1ContractsSubscriptionsUpdate(contractSubscription)


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractSubscription
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)
let contractSubscription: ContractSubscription; //

const { status, data } = await apiInstance.rrApiV1ContractsSubscriptionsUpdate(
    contractId,
    id,
    contractSubscription
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractSubscription** | **ContractSubscription**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractSubscription**

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

# **rrApiV1ContractsTerminateCreate**
> TerminateContractResponse rrApiV1ContractsTerminateCreate(terminateContract)

Terminate a contract and optionally void associated invoices.          If the user has permission to terminate contracts and void invoices, both operations         are performed atomically. If the user lacks permission for either operation, a draft         is created instead, and the response indicates which operations were drafted.          Returns 400 if any of the provided void_invoice_ids are invalid (not found, already voided,         has payments, void date is before the invoice date, or in a closed period).

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    TerminateContract
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)
let terminateContract: TerminateContract; //

const { status, data } = await apiInstance.rrApiV1ContractsTerminateCreate(
    id,
    terminateContract
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **terminateContract** | **TerminateContract**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**TerminateContractResponse**

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

# **rrApiV1ContractsTerminationSettlementPreviewRetrieve**
> TerminationSettlementPreviewResponse rrApiV1ContractsTerminationSettlementPreviewRetrieve()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)
let terminationDate: string; // (default to undefined)
let creditUnusedRevenue: boolean; // (optional) (default to true)

const { status, data } = await apiInstance.rrApiV1ContractsTerminationSettlementPreviewRetrieve(
    id,
    terminationDate,
    creditUnusedRevenue
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|
| **terminationDate** | [**string**] |  | defaults to undefined|
| **creditUnusedRevenue** | [**boolean**] |  | (optional) defaults to true|


### Return type

**TerminationSettlementPreviewResponse**

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

# **rrApiV1ContractsTierPriceOverridesCreate**
> TierPriceOverride rrApiV1ContractsTierPriceOverridesCreate(tierPriceOverride)


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    TierPriceOverride
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let tierPriceOverride: TierPriceOverride; //

const { status, data } = await apiInstance.rrApiV1ContractsTierPriceOverridesCreate(
    contractId,
    tierPriceOverride
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **tierPriceOverride** | **TierPriceOverride**|  | |
| **contractId** | [**number**] |  | defaults to undefined|


### Return type

**TierPriceOverride**

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

# **rrApiV1ContractsTierPriceOverridesList**
> PaginatedTierPriceOverrideList rrApiV1ContractsTierPriceOverridesList()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsTierPriceOverridesList(
    contractId,
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedTierPriceOverrideList**

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

# **rrApiV1ContractsUpdate**
> Contract rrApiV1ContractsUpdate(contract)


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    Contract
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)
let contract: Contract; //

const { status, data } = await apiInstance.rrApiV1ContractsUpdate(
    id,
    contract
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contract** | **Contract**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Contract**

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

# **rrApiV1ContractsUsageAllocationsPartialUpdate**
> ContractProductBundle rrApiV1ContractsUsageAllocationsPartialUpdate()

Partially update bundle allocations. Same behavior as PUT.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    PatchedContractProductBundleUpdate
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let usageId: number; // (default to undefined)
let patchedContractProductBundleUpdate: PatchedContractProductBundleUpdate; // (optional)

const { status, data } = await apiInstance.rrApiV1ContractsUsageAllocationsPartialUpdate(
    contractId,
    usageId,
    patchedContractProductBundleUpdate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedContractProductBundleUpdate** | **PatchedContractProductBundleUpdate**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **usageId** | [**number**] |  | defaults to undefined|


### Return type

**ContractProductBundle**

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

# **rrApiV1ContractsUsageAllocationsRetrieve**
> ContractProductBundle rrApiV1ContractsUsageAllocationsRetrieve()

Retrieve the current bundle allocation details for a contract subscription, milestone, or usage.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let usageId: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsUsageAllocationsRetrieve(
    contractId,
    usageId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **usageId** | [**number**] |  | defaults to undefined|


### Return type

**ContractProductBundle**

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

# **rrApiV1ContractsUsageAllocationsUpdate**
> ContractProductBundle rrApiV1ContractsUsageAllocationsUpdate(contractProductBundleUpdate)

         Update the bundle allocations for a contract item.          The sum of all line amounts must equal the bundle\'s total_amount.         Changes will cascade to related RevenueTransactions and JournalEntries.         

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractProductBundleUpdate
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let usageId: number; // (default to undefined)
let contractProductBundleUpdate: ContractProductBundleUpdate; //

const { status, data } = await apiInstance.rrApiV1ContractsUsageAllocationsUpdate(
    contractId,
    usageId,
    contractProductBundleUpdate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractProductBundleUpdate** | **ContractProductBundleUpdate**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **usageId** | [**number**] |  | defaults to undefined|


### Return type

**ContractProductBundle**

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

# **rrApiV1ContractsUsageCreate**
> ContractUsage rrApiV1ContractsUsageCreate(contractUsage)

List usage revenue records

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractUsage
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let contractUsage: ContractUsage; //

const { status, data } = await apiInstance.rrApiV1ContractsUsageCreate(
    contractId,
    contractUsage
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractUsage** | **ContractUsage**|  | |
| **contractId** | [**number**] |  | defaults to undefined|


### Return type

**ContractUsage**

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

# **rrApiV1ContractsUsageDestroy**
> rrApiV1ContractsUsageDestroy()

Retrieve, update, and delete contract usage revenue records

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsUsageDestroy(
    contractId,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
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

# **rrApiV1ContractsUsageList**
> PaginatedContractUsageList rrApiV1ContractsUsageList()

List usage revenue records

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsUsageList(
    contractId,
    limit,
    offset
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **limit** | [**number**] | Number of results to return per page. | (optional) defaults to undefined|
| **offset** | [**number**] | The initial index from which to return the results. | (optional) defaults to undefined|


### Return type

**PaginatedContractUsageList**

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

# **rrApiV1ContractsUsagePartialUpdate**
> ContractUsage rrApiV1ContractsUsagePartialUpdate()

Retrieve, update, and delete contract usage revenue records

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    PatchedContractUsage
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)
let patchedContractUsage: PatchedContractUsage; // (optional)

const { status, data } = await apiInstance.rrApiV1ContractsUsagePartialUpdate(
    contractId,
    id,
    patchedContractUsage
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedContractUsage** | **PatchedContractUsage**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractUsage**

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

# **rrApiV1ContractsUsageRetrieve**
> ContractUsage rrApiV1ContractsUsageRetrieve()

Retrieve, update, and delete contract usage revenue records

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ContractsUsageRetrieve(
    contractId,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractUsage**

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

# **rrApiV1ContractsUsageUpdate**
> ContractUsage rrApiV1ContractsUsageUpdate(contractUsage)

Retrieve, update, and delete contract usage revenue records

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractUsage
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)
let contractUsage: ContractUsage; //

const { status, data } = await apiInstance.rrApiV1ContractsUsageUpdate(
    contractId,
    id,
    contractUsage
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractUsage** | **ContractUsage**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractUsage**

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

# **rrApiV1CustomersDestroy**
> rrApiV1CustomersDestroy()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1CustomersDestroy(
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

# **rrApiV1CustomersList**
> PaginatedContractCustomerList rrApiV1CustomersList()

         Retrieve a list of contract customers with optional filtering and sorting.          Supports including soft-deleted records for audit and recovery purposes.         When include_deleted=true, returns ONLY deleted records instead of active records.         Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp,         and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records.         This provides clean separation between active and deleted data.         

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let includeDeleted: boolean; //When set to \'true\', returns ONLY deleted records instead of active records. Deleted records contain minimal data: \'id\', \'is_deleted=true\', \'deleted_at\' timestamp, and \'last_modified_at\'. When \'false\' or omitted, returns ONLY active records. This provides clean separation between active and deleted data. (optional) (default to false)
let lastModifiedAtGte: string; //Filter for records modified on or after this timestamp. Format: ISO 8601 (e.g., \'2024-01-01T00:00:00Z\' or \'2024-01-01\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let lastModifiedAtLte: string; //Filter for records modified on or before this timestamp. Format: ISO 8601 (e.g., \'2024-12-31T23:59:59Z\' or \'2024-12-31\'). Works with both active records and deleted records (filters by deletion time for deleted records). (optional) (default to undefined)
let limit: number; //Number of results to return per page. (optional) (default to undefined)
let offset: number; //The initial index from which to return the results. (optional) (default to undefined)

const { status, data } = await apiInstance.rrApiV1CustomersList(
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

**PaginatedContractCustomerList**

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

# **rrApiV1CustomersPartialUpdate**
> ContractCustomer rrApiV1CustomersPartialUpdate()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    PatchedContractCustomer
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)
let patchedContractCustomer: PatchedContractCustomer; // (optional)

const { status, data } = await apiInstance.rrApiV1CustomersPartialUpdate(
    id,
    patchedContractCustomer
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedContractCustomer** | **PatchedContractCustomer**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractCustomer**

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

# **rrApiV1CustomersRetrieve**
> ContractCustomer rrApiV1CustomersRetrieve()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1CustomersRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractCustomer**

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

# **rrApiV1CustomersUpdate**
> ContractCustomer rrApiV1CustomersUpdate(contractCustomer)


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractCustomer
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)
let contractCustomer: ContractCustomer; //

const { status, data } = await apiInstance.rrApiV1CustomersUpdate(
    id,
    contractCustomer
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractCustomer** | **ContractCustomer**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractCustomer**

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

# **rrApiV1ProductBulkSearchCreate**
> BulkProductSearchResponse rrApiV1ProductBulkSearchCreate(bulkProductSearch)

Resolve many product cells in a single request. Each term is matched against product_id, display_name, product_uuid, id, then product_name, in that order. A term matching more than one product is returned in the ambiguous list instead of being resolved.

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    BulkProductSearch
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

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

# **rrApiV1ProductBundlesDestroy**
> rrApiV1ProductBundlesDestroy()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ProductBundlesDestroy(
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

# **rrApiV1ProductBundlesPartialUpdate**
> ProductBundle rrApiV1ProductBundlesPartialUpdate()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    PatchedProductBundle
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)
let patchedProductBundle: PatchedProductBundle; // (optional)

const { status, data } = await apiInstance.rrApiV1ProductBundlesPartialUpdate(
    id,
    patchedProductBundle
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedProductBundle** | **PatchedProductBundle**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ProductBundle**

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

# **rrApiV1ProductBundlesRetrieve**
> ProductBundle rrApiV1ProductBundlesRetrieve()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1ProductBundlesRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ProductBundle**

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

# **rrApiV1ProductBundlesUpdate**
> ProductBundle rrApiV1ProductBundlesUpdate(productBundle)


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ProductBundle
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)
let productBundle: ProductBundle; //

const { status, data } = await apiInstance.rrApiV1ProductBundlesUpdate(
    id,
    productBundle
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **productBundle** | **ProductBundle**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ProductBundle**

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
    RevenueRecognitionApi,
    Configuration,
    DeleteRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

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
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

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
    RevenueRecognitionApi,
    Configuration,
    PatchedProduct
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

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
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

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
    RevenueRecognitionApi,
    Configuration,
    Product
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

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

# **rrApiV1TransactionsDestroy**
> rrApiV1TransactionsDestroy()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1TransactionsDestroy(
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

# **rrApiV1TransactionsPartialUpdate**
> RevenueTransaction rrApiV1TransactionsPartialUpdate()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    PatchedRevenueTransaction
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)
let patchedRevenueTransaction: PatchedRevenueTransaction; // (optional)

const { status, data } = await apiInstance.rrApiV1TransactionsPartialUpdate(
    id,
    patchedRevenueTransaction
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedRevenueTransaction** | **PatchedRevenueTransaction**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**RevenueTransaction**

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

# **rrApiV1TransactionsRetrieve**
> RevenueTransaction rrApiV1TransactionsRetrieve()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.rrApiV1TransactionsRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**RevenueTransaction**

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

# **rrApiV1TransactionsUpdate**
> RevenueTransaction rrApiV1TransactionsUpdate(revenueTransaction)


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    RevenueTransaction
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let id: number; // (default to undefined)
let revenueTransaction: RevenueTransaction; //

const { status, data } = await apiInstance.rrApiV1TransactionsUpdate(
    id,
    revenueTransaction
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **revenueTransaction** | **RevenueTransaction**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**RevenueTransaction**

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

# **updatePrepaidCommit**
> ContractPrepaidCommit updatePrepaidCommit(contractPrepaidCommit)


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    ContractPrepaidCommit
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contractId: number; // (default to undefined)
let id: number; // (default to undefined)
let contractPrepaidCommit: ContractPrepaidCommit; //

const { status, data } = await apiInstance.updatePrepaidCommit(
    contractId,
    id,
    contractPrepaidCommit
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **contractPrepaidCommit** | **ContractPrepaidCommit**|  | |
| **contractId** | [**number**] |  | defaults to undefined|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**ContractPrepaidCommit**

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

# **updatePrepaidCommitConsumption**
> updatePrepaidCommitConsumption()


### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let commitId: number; // (default to undefined)
let contractId: number; // (default to undefined)
let id: number; // (default to undefined)

const { status, data } = await apiInstance.updatePrepaidCommitConsumption(
    commitId,
    contractId,
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **commitId** | [**number**] |  | defaults to undefined|
| **contractId** | [**number**] |  | defaults to undefined|
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

# **uploadPrepaidCommitUsageEvents**
> uploadPrepaidCommitUsageEvents()

Upload a CSV of usage events for a specific prepaid commit (commit-scoped).

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let commitId: number; // (default to undefined)
let contractId: number; // (default to undefined)

const { status, data } = await apiInstance.uploadPrepaidCommitUsageEvents(
    commitId,
    contractId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **commitId** | [**number**] |  | defaults to undefined|
| **contractId** | [**number**] |  | defaults to undefined|


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


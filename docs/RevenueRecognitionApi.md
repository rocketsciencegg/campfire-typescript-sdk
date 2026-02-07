# RevenueRecognitionApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**createContract**](#createcontract) | **POST** /rr/api/v1/contracts | Create Contract|
|[**createContractBundle**](#createcontractbundle) | **POST** /rr/api/v1/contracts/{contract_id}/bundles | Create Contract Bundle|
|[**createContractMilestone**](#createcontractmilestone) | **POST** /rr/api/v1/contracts/{contract_id}/milestones | Create Contract Milestone|
|[**createContractSubscription**](#createcontractsubscription) | **POST** /rr/api/v1/contracts/{contract_id}/subscriptions | Create Contract Subscription|
|[**createProduct**](#createproduct) | **POST** /rr/api/v1/product | Create Contract Product|
|[**createProductBundle**](#createproductbundle) | **POST** /rr/api/v1/product-bundles | Create Product Bundle|
|[**createRevenueTransaction**](#createrevenuetransaction) | **POST** /rr/api/v1/transactions | Create Revenue Transaction|
|[**listContractBundles**](#listcontractbundles) | **GET** /rr/api/v1/contracts/{contract_id}/bundles | List Contract Bundles|
|[**listContractMilestones**](#listcontractmilestones) | **GET** /rr/api/v1/contracts/{contract_id}/milestones | List Contract Milestones|
|[**listContractSubscriptions**](#listcontractsubscriptions) | **GET** /rr/api/v1/contracts/{contract_id}/subscriptions | List Contract Subscriptions|
|[**listContracts**](#listcontracts) | **GET** /rr/api/v1/contracts | List Contracts|
|[**listProductBundles**](#listproductbundles) | **GET** /rr/api/v1/product-bundles | List Product Bundles|
|[**listProducts**](#listproducts) | **GET** /rr/api/v1/product | List Contract Products|
|[**listRevenueTransactions**](#listrevenuetransactions) | **GET** /rr/api/v1/transactions | List Revenue Transactions|
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
|[**rrApiV1ProductBundlesDestroy**](#rrapiv1productbundlesdestroy) | **DELETE** /rr/api/v1/product-bundles/{id} | Delete Product Bundle|
|[**rrApiV1ProductBundlesPartialUpdate**](#rrapiv1productbundlespartialupdate) | **PATCH** /rr/api/v1/product-bundles/{id} | Partial Update Product Bundle|
|[**rrApiV1ProductBundlesRetrieve**](#rrapiv1productbundlesretrieve) | **GET** /rr/api/v1/product-bundles/{id} | Retrieve Product Bundle|
|[**rrApiV1ProductBundlesUpdate**](#rrapiv1productbundlesupdate) | **PUT** /rr/api/v1/product-bundles/{id} | Update Product Bundle|
|[**rrApiV1ProductDestroy**](#rrapiv1productdestroy) | **DELETE** /rr/api/v1/product/{id} | Delete Product|
|[**rrApiV1ProductPartialUpdate**](#rrapiv1productpartialupdate) | **PATCH** /rr/api/v1/product/{id} | Partial Update Product|
|[**rrApiV1ProductRetrieve**](#rrapiv1productretrieve) | **GET** /rr/api/v1/product/{id} | Retrieve Product|
|[**rrApiV1ProductUpdate**](#rrapiv1productupdate) | **PUT** /rr/api/v1/product/{id} | Update Product|
|[**rrApiV1TransactionsDestroy**](#rrapiv1transactionsdestroy) | **DELETE** /rr/api/v1/transactions/{id} | Delete Revenue Transaction|
|[**rrApiV1TransactionsPartialUpdate**](#rrapiv1transactionspartialupdate) | **PATCH** /rr/api/v1/transactions/{id} | Partial Update Revenue Transaction|
|[**rrApiV1TransactionsRetrieve**](#rrapiv1transactionsretrieve) | **GET** /rr/api/v1/transactions/{id} | Retrieve Revenue Transaction|
|[**rrApiV1TransactionsUpdate**](#rrapiv1transactionsupdate) | **PUT** /rr/api/v1/transactions/{id} | Update Revenue Transaction|

# **createContract**
> Contract createContract()

Create a new contract

### Example

```typescript
import {
    RevenueRecognitionApi,
    Configuration,
    Contract
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new RevenueRecognitionApi(configuration);

let contract: Contract; // (optional)

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

[knoxApiToken](../README.md#knoxApiToken)

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

Create a new contract bundle

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

[knoxApiToken](../README.md#knoxApiToken)

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

[knoxApiToken](../README.md#knoxApiToken)

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

Create a new contract subscription

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createProduct**
> Product createProduct()

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

let product: Product; // (optional)

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

[knoxApiToken](../README.md#knoxApiToken)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createRevenueTransaction**
> RevenueTransaction createRevenueTransaction()

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

let revenueTransaction: RevenueTransaction; // (optional)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rrApiV1ContractsUpdate**
> Contract rrApiV1ContractsUpdate()


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
let contract: Contract; // (optional)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

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

[knoxApiToken](../README.md#knoxApiToken)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rrApiV1ProductDestroy**
> rrApiV1ProductDestroy()


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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rrApiV1ProductUpdate**
> Product rrApiV1ProductUpdate()


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
let product: Product; // (optional)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rrApiV1TransactionsUpdate**
> RevenueTransaction rrApiV1TransactionsUpdate()


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
let revenueTransaction: RevenueTransaction; // (optional)

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

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


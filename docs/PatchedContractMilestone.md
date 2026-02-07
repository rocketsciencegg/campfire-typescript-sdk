# PatchedContractMilestone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**contract** | **number** |  | [optional] [default to undefined]
**product** | **number** |  | [optional] [default to undefined]
**productBundle** | **string** |  | [optional] [readonly] [default to undefined]
**contractProductBundle** | [**ContractProductBundleRead**](ContractProductBundleRead.md) |  | [optional] [readonly] [default to undefined]
**productName** | **string** |  | [optional] [readonly] [default to undefined]
**productBundleName** | **string** |  | [optional] [readonly] [default to undefined]
**milestoneName** | **string** |  | [optional] [default to undefined]
**milestoneDate** | **string** |  | [optional] [default to undefined]
**amount** | **number** |  | [optional] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**departmentName** | **string** |  | [optional] [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [optional] [readonly] [default to undefined]
**revenueTransactionId** | **number** |  | [optional] [readonly] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]

## Example

```typescript
import { PatchedContractMilestone } from 'campfire-typescript-sdk';

const instance: PatchedContractMilestone = {
    id,
    customer,
    contract,
    product,
    productBundle,
    contractProductBundle,
    productName,
    productBundleName,
    milestoneName,
    milestoneDate,
    amount,
    description,
    department,
    departmentName,
    tags,
    revenueTransactionId,
    createdAt,
    lastModifiedAt,
    isDeleted,
    deletedAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

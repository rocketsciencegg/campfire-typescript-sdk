# ContractMilestone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**contract** | **number** |  | [default to undefined]
**product** | **number** |  | [optional] [default to undefined]
**productBundle** | **string** |  | [readonly] [default to undefined]
**contractProductBundle** | [**ContractProductBundleRead**](ContractProductBundleRead.md) |  | [readonly] [default to undefined]
**productName** | **string** |  | [readonly] [default to undefined]
**productBundleName** | **string** |  | [readonly] [default to undefined]
**milestoneName** | **string** |  | [default to undefined]
**milestoneDate** | **string** |  | [default to undefined]
**amount** | **number** |  | [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [readonly] [default to undefined]
**revenueTransactionId** | **number** |  | [readonly] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { ContractMilestone } from 'campfire-typescript-sdk';

const instance: ContractMilestone = {
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

# FixedAssetClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**assetAccountName** | **string** |  | [readonly] [default to undefined]
**accumulatedDepreciationAccountName** | **string** |  | [readonly] [default to undefined]
**depreciationExpenseAccountName** | **string** |  | [readonly] [default to undefined]
**name** | **string** |  | [default to undefined]
**usefulLife** | **number** |  | [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**assetAccount** | **number** |  | [optional] [default to undefined]
**accumulatedDepreciationAccount** | **number** |  | [optional] [default to undefined]
**depreciationExpenseAccount** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { FixedAssetClass } from 'campfire-typescript-sdk';

const instance: FixedAssetClass = {
    id,
    isDeleted,
    deletedAt,
    assetAccountName,
    accumulatedDepreciationAccountName,
    depreciationExpenseAccountName,
    name,
    usefulLife,
    createdAt,
    lastModifiedAt,
    customer,
    assetAccount,
    accumulatedDepreciationAccount,
    depreciationExpenseAccount,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

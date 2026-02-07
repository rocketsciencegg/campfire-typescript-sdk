# BudgetAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**accountName** | **string** |  | [readonly] [default to undefined]
**accountLineage** | **string** |  | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**period** | **number** |  | [optional] [default to 1]
**amount** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**budget** | **number** |  | [readonly] [default to undefined]
**account** | **number** |  | [readonly] [default to undefined]
**department** | **number** |  | [readonly] [default to undefined]

## Example

```typescript
import { BudgetAccount } from 'campfire-typescript-sdk';

const instance: BudgetAccount = {
    id,
    isDeleted,
    deletedAt,
    accountName,
    accountLineage,
    departmentName,
    period,
    amount,
    createdAt,
    lastModifiedAt,
    customer,
    budget,
    account,
    department,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

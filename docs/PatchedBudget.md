# PatchedBudget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**entityName** | **string** |  | [optional] [readonly] [default to undefined]
**priorStartDate** | **string** |  | [optional] [readonly] [default to undefined]
**priorEndDate** | **string** |  | [optional] [readonly] [default to undefined]
**departmentName** | **string** |  | [optional] [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**name** | **string** |  | [optional] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**cadence** | **string** |  | [optional] [default to undefined]
**startDate** | **string** |  | [optional] [default to undefined]
**endDate** | **string** |  | [optional] [default to undefined]
**periods** | **number** |  | [optional] [default to undefined]
**breakdownType** | [**BreakdownTypeEnum**](BreakdownTypeEnum.md) |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedBudget } from 'campfire-typescript-sdk';

const instance: PatchedBudget = {
    id,
    entityName,
    priorStartDate,
    priorEndDate,
    departmentName,
    tags,
    isDeleted,
    deletedAt,
    name,
    description,
    cadence,
    startDate,
    endDate,
    periods,
    breakdownType,
    currency,
    createdAt,
    lastModifiedAt,
    customer,
    entity,
    department,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

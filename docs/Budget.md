# Budget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**priorStartDate** | **string** |  | [readonly] [default to undefined]
**priorEndDate** | **string** |  | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**name** | **string** |  | [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**cadence** | **string** |  | [optional] [default to undefined]
**startDate** | **string** |  | [default to undefined]
**endDate** | **string** |  | [optional] [default to undefined]
**periods** | **number** |  | [optional] [default to undefined]
**breakdownType** | [**BreakdownTypeEnum**](BreakdownTypeEnum.md) |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { Budget } from 'campfire-typescript-sdk';

const instance: Budget = {
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

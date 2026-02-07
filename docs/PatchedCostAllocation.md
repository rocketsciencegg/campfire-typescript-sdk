# PatchedCostAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**lines** | [**Array&lt;CostAllocationLine&gt;**](CostAllocationLine.md) |  | [optional] [default to undefined]
**lineCount** | **number** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**name** | **string** |  | [optional] [default to undefined]
**number** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**account** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedCostAllocation } from 'campfire-typescript-sdk';

const instance: PatchedCostAllocation = {
    id,
    lines,
    lineCount,
    isDeleted,
    deletedAt,
    name,
    number,
    createdAt,
    lastModifiedAt,
    customer,
    account,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

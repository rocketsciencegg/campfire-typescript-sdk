# CostAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**lines** | [**Array&lt;CostAllocationLine&gt;**](CostAllocationLine.md) |  | [default to undefined]
**lineCount** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**name** | **string** |  | [default to undefined]
**number** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**account** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { CostAllocation } from 'campfire-typescript-sdk';

const instance: CostAllocation = {
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

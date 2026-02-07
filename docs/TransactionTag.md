# TransactionTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**groupName** | **string** |  | [readonly] [default to undefined]
**parentName** | **string** |  | [readonly] [default to undefined]
**parent** | **number** |  | [optional] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**isActive** | **boolean** |  | [optional] [default to true]
**name** | **string** |  | [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**group** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { TransactionTag } from 'campfire-typescript-sdk';

const instance: TransactionTag = {
    id,
    groupName,
    parentName,
    parent,
    isDeleted,
    deletedAt,
    isActive,
    name,
    createdAt,
    lastModifiedAt,
    customer,
    group,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

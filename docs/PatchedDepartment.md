# PatchedDepartment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**parentName** | **string** |  | [optional] [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**active** | **boolean** |  | [optional] [default to true]
**code** | **string** |  | [optional] [default to undefined]
**name** | **string** |  | [optional] [default to undefined]
**displayName** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**parent** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedDepartment } from 'campfire-typescript-sdk';

const instance: PatchedDepartment = {
    id,
    parentName,
    tags,
    lastModifiedAt,
    active,
    code,
    name,
    displayName,
    createdAt,
    customer,
    parent,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

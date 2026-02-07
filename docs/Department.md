# Department


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**parentName** | **string** |  | [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**active** | **boolean** |  | [optional] [default to true]
**code** | **string** |  | [optional] [default to undefined]
**name** | **string** |  | [default to undefined]
**displayName** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**parent** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { Department } from 'campfire-typescript-sdk';

const instance: Department = {
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

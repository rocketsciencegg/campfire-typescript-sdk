# CustomField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**app** | **string** |  | [readonly] [default to undefined]
**model** | **string** |  | [readonly] [default to undefined]
**name** | **string** |  | [default to undefined]
**label** | **string** |  | [default to undefined]
**fieldType** | [**FieldTypeEnum**](FieldTypeEnum.md) |  | [default to undefined]
**_options** | **any** |  | [optional] [default to undefined]
**isRequired** | **boolean** |  | [optional] [default to undefined]
**displayOrder** | **number** |  | [optional] [default to undefined]
**isActive** | **boolean** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**updatedAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { CustomField } from 'campfire-typescript-sdk';

const instance: CustomField = {
    id,
    app,
    model,
    name,
    label,
    fieldType,
    _options,
    isRequired,
    displayOrder,
    isActive,
    createdAt,
    updatedAt,
    lastModifiedAt,
    isDeleted,
    deletedAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

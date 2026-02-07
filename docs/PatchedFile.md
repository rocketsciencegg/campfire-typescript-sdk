# PatchedFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**createdBy** | **number** |  | [optional] [readonly] [default to undefined]
**createdByName** | **string** |  | [optional] [readonly] [default to undefined]
**createdByEmail** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**name** | **string** |  | [optional] [default to undefined]
**url** | **string** |  | [optional] [readonly] [default to undefined]
**s3ContentType** | **string** |  | [optional] [default to undefined]
**s3ContentLength** | **number** |  | [optional] [default to undefined]
**s3Path** | **string** |  | [optional] [default to undefined]
**objectId** | **number** |  | [optional] [default to undefined]
**app** | **string** |  | [optional] [readonly] [default to undefined]
**model** | **string** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]

## Example

```typescript
import { PatchedFile } from 'campfire-typescript-sdk';

const instance: PatchedFile = {
    id,
    customer,
    createdAt,
    createdBy,
    createdByName,
    createdByEmail,
    lastModifiedAt,
    name,
    url,
    s3ContentType,
    s3ContentLength,
    s3Path,
    objectId,
    app,
    model,
    isDeleted,
    deletedAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

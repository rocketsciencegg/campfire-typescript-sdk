# ModelFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**createdBy** | **number** |  | [readonly] [default to undefined]
**createdByName** | **string** |  | [readonly] [default to undefined]
**createdByEmail** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**name** | **string** |  | [default to undefined]
**url** | **string** |  | [readonly] [default to undefined]
**s3ContentType** | **string** |  | [optional] [default to undefined]
**s3ContentLength** | **number** |  | [optional] [default to undefined]
**s3Path** | **string** |  | [default to undefined]
**objectId** | **number** |  | [optional] [default to undefined]
**app** | **string** |  | [readonly] [default to undefined]
**model** | **string** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { ModelFile } from 'campfire-typescript-sdk';

const instance: ModelFile = {
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

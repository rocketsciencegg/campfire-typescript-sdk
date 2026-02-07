# PatchedProductBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**bundleName** | **string** |  | [optional] [default to undefined]
**bundleDescription** | **string** |  | [optional] [default to undefined]
**stripeProductId** | **string** |  | [optional] [readonly] [default to undefined]
**anrokItemId** | **string** |  | [optional] [readonly] [default to undefined]
**lines** | [**Array&lt;ProductBundleLine&gt;**](ProductBundleLine.md) |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]

## Example

```typescript
import { PatchedProductBundle } from 'campfire-typescript-sdk';

const instance: PatchedProductBundle = {
    id,
    bundleName,
    bundleDescription,
    stripeProductId,
    anrokItemId,
    lines,
    createdAt,
    lastModifiedAt,
    isDeleted,
    deletedAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

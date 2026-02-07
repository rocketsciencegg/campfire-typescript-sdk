# ProductBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**bundleName** | **string** |  | [default to undefined]
**bundleDescription** | **string** |  | [optional] [default to undefined]
**stripeProductId** | **string** |  | [readonly] [default to undefined]
**anrokItemId** | **string** |  | [readonly] [default to undefined]
**lines** | [**Array&lt;ProductBundleLine&gt;**](ProductBundleLine.md) |  | [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { ProductBundle } from 'campfire-typescript-sdk';

const instance: ProductBundle = {
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

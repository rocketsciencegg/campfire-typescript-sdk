# BulkVendorSearchError

One submitted row whose external_id matched no payee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **number** | Position of the row in the submitted &#x60;vendors&#x60; list. | [default to undefined]
**externalId** | **string** |  | [default to undefined]
**name** | **string** |  | [default to undefined]
**error** | **string** |  | [default to undefined]

## Example

```typescript
import { BulkVendorSearchError } from 'campfire-typescript-sdk';

const instance: BulkVendorSearchError = {
    index,
    externalId,
    name,
    error,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

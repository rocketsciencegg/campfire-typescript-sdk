# BulkVendorSearchResponse

The body returned when at least one row supplied an external_id that matched nothing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendors** | [**Array&lt;Vendor&gt;**](Vendor.md) |  | [default to undefined]
**errors** | [**Array&lt;BulkVendorSearchError&gt;**](BulkVendorSearchError.md) |  | [default to undefined]

## Example

```typescript
import { BulkVendorSearchResponse } from 'campfire-typescript-sdk';

const instance: BulkVendorSearchResponse = {
    vendors,
    errors,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

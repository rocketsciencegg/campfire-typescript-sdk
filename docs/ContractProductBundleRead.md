# ContractProductBundleRead

Read-only serializer for ContractProductBundle in milestone responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**sourceBundle** | **number** | Original ProductBundle template this was created from | [optional] [default to undefined]
**sourceBundleName** | **string** |  | [readonly] [default to undefined]
**totalAmount** | **number** | Total amount to be allocated across products | [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**lines** | [**Array&lt;ContractProductBundleLineRead&gt;**](ContractProductBundleLineRead.md) |  | [readonly] [default to undefined]

## Example

```typescript
import { ContractProductBundleRead } from 'campfire-typescript-sdk';

const instance: ContractProductBundleRead = {
    id,
    sourceBundle,
    sourceBundleName,
    totalAmount,
    currency,
    lines,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

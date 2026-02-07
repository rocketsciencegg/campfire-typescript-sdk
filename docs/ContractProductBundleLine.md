# ContractProductBundleLine

Serializer for individual product allocation lines within a ContractProductBundle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**product** | **number** |  | [readonly] [default to undefined]
**productName** | **string** |  | [readonly] [default to undefined]
**productIdStr** | **string** |  | [readonly] [default to undefined]
**amount** | **number** | Dollar amount allocated to this product | [default to undefined]
**percentage** | **string** | Calculated percentage based on amount / total | [readonly] [default to undefined]
**originalPercentage** | **number** | Original percentage from source ProductBundle for auditing | [readonly] [default to undefined]

## Example

```typescript
import { ContractProductBundleLine } from 'campfire-typescript-sdk';

const instance: ContractProductBundleLine = {
    id,
    product,
    productName,
    productIdStr,
    amount,
    percentage,
    originalPercentage,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

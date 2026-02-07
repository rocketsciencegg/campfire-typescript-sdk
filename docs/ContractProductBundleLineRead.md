# ContractProductBundleLineRead

Read-only serializer for ContractProductBundleLine in milestone responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**product** | **number** |  | [default to undefined]
**productName** | **string** |  | [readonly] [default to undefined]
**amount** | **number** | Dollar amount allocated to this product | [default to undefined]
**percentage** | **string** |  | [readonly] [default to undefined]
**originalPercentage** | **number** | Original percentage from source ProductBundle for auditing | [optional] [default to undefined]

## Example

```typescript
import { ContractProductBundleLineRead } from 'campfire-typescript-sdk';

const instance: ContractProductBundleLineRead = {
    id,
    product,
    productName,
    amount,
    percentage,
    originalPercentage,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

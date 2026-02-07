# ContractProductBundle

Serializer for ContractProductBundle with nested lines.  Used for retrieving and updating contract-specific bundle allocations. When updating, validates that line amounts sum to total_amount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**sourceBundle** | **number** | Original ProductBundle template this was created from | [readonly] [default to undefined]
**sourceBundleName** | **string** |  | [readonly] [default to undefined]
**totalAmount** | **number** | Total amount to be allocated across products | [readonly] [default to undefined]
**currency** | **string** |  | [readonly] [default to undefined]
**lines** | [**Array&lt;ContractProductBundleLine&gt;**](ContractProductBundleLine.md) |  | [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { ContractProductBundle } from 'campfire-typescript-sdk';

const instance: ContractProductBundle = {
    id,
    sourceBundle,
    sourceBundleName,
    totalAmount,
    currency,
    lines,
    createdAt,
    lastModifiedAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

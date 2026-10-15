# ProductSearchResult

Lookup-only product shape used by bulk search.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**productId** | **string** |  | [optional] [default to undefined]
**productName** | **string** |  | [optional] [default to undefined]
**displayName** | **string** |  | [optional] [default to undefined]
**productUuid** | **string** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [readonly] [default to undefined]

## Example

```typescript
import { ProductSearchResult } from 'campfire-typescript-sdk';

const instance: ProductSearchResult = {
    id,
    productId,
    productName,
    displayName,
    productUuid,
    department,
    departmentName,
    tags,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

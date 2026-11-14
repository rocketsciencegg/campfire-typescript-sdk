# EmptyTransactionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **number** |  | [default to undefined]
**paymentDate** | **string** | Payment date for term discount calculation | [default to undefined]
**withholdingAmount** | **number** |  | [optional] [default to undefined]
**accountId** | **number** | Clearing account to validate | [optional] [default to undefined]

## Example

```typescript
import { EmptyTransactionInput } from 'campfire-typescript-sdk';

const instance: EmptyTransactionInput = {
    amount,
    paymentDate,
    withholdingAmount,
    accountId,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

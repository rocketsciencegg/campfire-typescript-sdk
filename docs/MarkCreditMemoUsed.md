# MarkCreditMemoUsed

Serializer for marking a credit memo as used with a transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactionId** | **number** |  | [default to undefined]
**accountId** | **number** |  | [default to undefined]
**amount** | **number** |  | [default to undefined]
**paymentDate** | **string** |  | [default to undefined]
**memo** | **string** |  | [optional] [default to undefined]

## Example

```typescript
import { MarkCreditMemoUsed } from 'campfire-typescript-sdk';

const instance: MarkCreditMemoUsed = {
    transactionId,
    accountId,
    amount,
    paymentDate,
    memo,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

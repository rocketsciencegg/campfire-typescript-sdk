# CalculatePaymentInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**Array&lt;TransactionPaymentInput&gt;**](TransactionPaymentInput.md) |  | [optional] [default to undefined]
**creditMemos** | [**Array&lt;CreditMemoPaymentInput&gt;**](CreditMemoPaymentInput.md) |  | [optional] [default to undefined]
**emptyTransactions** | [**Array&lt;EmptyTransactionInput&gt;**](EmptyTransactionInput.md) |  | [optional] [default to undefined]

## Example

```typescript
import { CalculatePaymentInput } from 'campfire-typescript-sdk';

const instance: CalculatePaymentInput = {
    transactions,
    creditMemos,
    emptyTransactions,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

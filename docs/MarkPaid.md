# MarkPaid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactionMatchId** | **number** |  | [optional] [default to undefined]
**transactions** | [**Array&lt;MarkPaidTransaction&gt;**](MarkPaidTransaction.md) |  | [optional] [default to undefined]
**creditMemos** | [**Array&lt;MarkPaidCreditMemo&gt;**](MarkPaidCreditMemo.md) |  | [optional] [default to undefined]
**debitMemos** | [**Array&lt;MarkPaidDebitMemo&gt;**](MarkPaidDebitMemo.md) |  | [optional] [default to undefined]
**emptyTransactions** | [**Array&lt;MarkPaidEmptyTransaction&gt;**](MarkPaidEmptyTransaction.md) |  | [optional] [default to undefined]

## Example

```typescript
import { MarkPaid } from 'campfire-typescript-sdk';

const instance: MarkPaid = {
    transactionMatchId,
    transactions,
    creditMemos,
    debitMemos,
    emptyTransactions,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

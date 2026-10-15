# MarkInvoicePaidResponse

200 payload for the mark-invoice-paid endpoint.  The endpoint returns ids of the records it created rather than the invoice itself. ``auto_created_credit_memos`` is only present when an overpayment produced one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**journalEntryIds** | **Array&lt;number&gt;** |  | [default to undefined]
**paymentIds** | **Array&lt;number&gt;** |  | [default to undefined]
**autoCreatedCreditMemos** | [**Array&lt;MarkInvoicePaidAutoCreatedCreditMemo&gt;**](MarkInvoicePaidAutoCreatedCreditMemo.md) |  | [optional] [default to undefined]

## Example

```typescript
import { MarkInvoicePaidResponse } from 'campfire-typescript-sdk';

const instance: MarkInvoicePaidResponse = {
    journalEntryIds,
    paymentIds,
    autoCreatedCreditMemos,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

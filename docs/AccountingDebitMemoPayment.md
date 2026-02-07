# AccountingDebitMemoPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**paymentJournalEntryOrder** | **string** |  | [readonly] [default to undefined]
**bill** | **string** |  | [readonly] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**amount** | **number** |  | [optional] [default to undefined]
**paymentDate** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**voidedDate** | **string** |  | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**debitMemo** | **number** |  | [default to undefined]
**paymentJournalEntry** | **number** |  | [default to undefined]
**paymentTransaction** | **number** |  | [optional] [default to undefined]
**voidedJournalEntry** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { AccountingDebitMemoPayment } from 'campfire-typescript-sdk';

const instance: AccountingDebitMemoPayment = {
    id,
    paymentJournalEntryOrder,
    bill,
    currency,
    amount,
    paymentDate,
    createdAt,
    lastModifiedAt,
    voidedDate,
    customer,
    debitMemo,
    paymentJournalEntry,
    paymentTransaction,
    voidedJournalEntry,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

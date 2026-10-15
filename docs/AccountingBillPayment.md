# AccountingBillPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**paymentTransactionBankDescription** | **string** |  | [readonly] [default to undefined]
**paymentJournalEntryOrder** | **string** |  | [readonly] [default to undefined]
**voidedJournalEntryOrder** | **string** |  | [readonly] [default to undefined]
**withheldAmount** | **number** | Tax withheld on this payment (AP): sum of the payment\&#39;s withholding credit legs.  Reads the &#x60;&#x60;bill_withheld_by_payment&#x60;&#x60; map that &#x60;&#x60;AccountingBillSerializer&#x60;&#x60; populated from prefetched records, so no per-payment query runs. A 0% payment maps to zero, which is distinct from a payment that recorded no withholding at all. | [readonly] [default to undefined]
**appliedDebitMemo** | **{ [key: string]: any; }** | The debit memo this payment applied, when the payment is a memo application (its journal entry carries a debit memo payment row).  Uses .all() so the detail view\&#39;s prefetch chain serves it from cache. | [readonly] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**amount** | **number** |  | [optional] [default to undefined]
**paymentDate** | **string** |  | [optional] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**sourceId** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**voidedDate** | **string** |  | [optional] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**bill** | **number** |  | [default to undefined]
**paymentJournalEntry** | **number** |  | [default to undefined]
**paymentTransaction** | **number** |  | [optional] [default to undefined]
**checkPayment** | **number** |  | [optional] [default to undefined]
**voidedJournalEntry** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { AccountingBillPayment } from 'campfire-typescript-sdk';

const instance: AccountingBillPayment = {
    id,
    paymentTransactionBankDescription,
    paymentJournalEntryOrder,
    voidedJournalEntryOrder,
    withheldAmount,
    appliedDebitMemo,
    currency,
    amount,
    paymentDate,
    source,
    sourceId,
    createdAt,
    voidedDate,
    lastModifiedAt,
    customer,
    bill,
    paymentJournalEntry,
    paymentTransaction,
    checkPayment,
    voidedJournalEntry,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

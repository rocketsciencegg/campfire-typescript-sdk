# AccountingInvoicePayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**creditMemo** | **string** |  | [readonly] [default to undefined]
**paymentTransactionBankDescription** | **string** |  | [readonly] [default to undefined]
**paymentJournalEntryOrder** | **string** |  | [readonly] [default to undefined]
**paymentIntercompanyJournal** | **string** |  | [readonly] [default to undefined]
**voidedJournalEntryOrder** | **string** |  | [readonly] [default to undefined]
**withheldAmount** | **number** | Tax withheld on this payment, or None when withholding was never recorded.  Read from the payment\&#39;s own withholding records rather than the invoice\&#39;s, so a voided payment still shows what it originally withheld. A 0% record posts no leg and contributes zero, which is distinct from no withholding at all. | [readonly] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**amount** | **number** |  | [optional] [default to undefined]
**paymentDate** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**voidedDate** | **string** |  | [optional] [default to undefined]
**source** | [**Source47fEnum**](Source47fEnum.md) |  | [optional] [default to undefined]
**paymentType** | [**PaymentTypeEnum**](PaymentTypeEnum.md) | Type of payment: credit memo application, bank transaction, or manual transaction  * &#x60;CREDIT_MEMO&#x60; - Credit Memo * &#x60;BANK_TRANSACTION&#x60; - Bank Transaction * &#x60;MANUAL_TRANSACTION&#x60; - Manual Transaction | [readonly] [default to undefined]
**externalId** | **string** | Stable upstream identifier for this payment (e.g. Stripe balance transaction \&#39;btxn_...\&#39;, Stripe credit note \&#39;cn_...\&#39;, or the mart\&#39;s event external_id for customer-balance applications). Used as the natural dedup/idempotency key. Null for manually-entered payments. | [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**invoice** | **number** |  | [default to undefined]
**paymentJournalEntry** | **number** |  | [optional] [default to undefined]
**paymentTransaction** | **number** |  | [optional] [default to undefined]
**fxGainLossRealizedTransaction** | **number** |  | [optional] [default to undefined]
**paymentTermDiscountTransaction** | **number** |  | [optional] [default to undefined]
**voidedJournalEntry** | **number** |  | [optional] [default to undefined]
**paymentTransactions** | **Array&lt;number&gt;** |  | [optional] [default to undefined]

## Example

```typescript
import { AccountingInvoicePayment } from 'campfire-typescript-sdk';

const instance: AccountingInvoicePayment = {
    id,
    creditMemo,
    paymentTransactionBankDescription,
    paymentJournalEntryOrder,
    paymentIntercompanyJournal,
    voidedJournalEntryOrder,
    withheldAmount,
    currency,
    amount,
    paymentDate,
    createdAt,
    voidedDate,
    source,
    paymentType,
    externalId,
    lastModifiedAt,
    customer,
    invoice,
    paymentJournalEntry,
    paymentTransaction,
    fxGainLossRealizedTransaction,
    paymentTermDiscountTransaction,
    voidedJournalEntry,
    paymentTransactions,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

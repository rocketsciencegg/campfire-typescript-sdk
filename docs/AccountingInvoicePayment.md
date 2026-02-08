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
**currency** | **string** |  | [optional] [default to undefined]
**amount** | **number** |  | [optional] [default to undefined]
**paymentDate** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**voidedDate** | **string** |  | [optional] [default to undefined]
**source** | [**AccountingInvoicePaymentSourceEnum**](AccountingInvoicePaymentSourceEnum.md) |  | [optional] [default to undefined]
**paymentType** | [**PaymentTypeEnum**](PaymentTypeEnum.md) | Type of payment: credit memo application, bank transaction, or manual transaction  * &#x60;CREDIT_MEMO&#x60; - Credit Memo * &#x60;BANK_TRANSACTION&#x60; - Bank Transaction * &#x60;MANUAL_TRANSACTION&#x60; - Manual Transaction | [readonly] [default to undefined]
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
    currency,
    amount,
    paymentDate,
    createdAt,
    voidedDate,
    source,
    paymentType,
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

# PatchedAccountingBill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**lines** | [**Array&lt;AccountingBillLine&gt;**](AccountingBillLine.md) |  | [optional] [default to undefined]
**payments** | [**Array&lt;AccountingBillPayment&gt;**](AccountingBillPayment.md) |  | [optional] [readonly] [default to undefined]
**paymentJournalEntries** | **Array&lt;number&gt;** |  | [optional] [readonly] [default to undefined]
**status** | **string** |  | [optional] [readonly] [default to undefined]
**pastDueDays** | **number** |  | [optional] [readonly] [default to undefined]
**entityName** | **string** |  | [optional] [readonly] [default to undefined]
**entityCurrency** | **string** |  | [optional] [readonly] [default to undefined]
**vendorName** | **string** |  | [optional] [readonly] [default to undefined]
**apAccountName** | **string** | Return AP account name with number in \&#39;number - name\&#39; format, similar to name_and_number. | [optional] [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [optional] [readonly] [default to undefined]
**totalAmount** | **number** |  | [optional] [readonly] [default to undefined]
**amountDue** | **number** |  | [optional] [readonly] [default to undefined]
**amountPaid** | **number** |  | [optional] [readonly] [default to undefined]
**itemDate** | **string** |  | [optional] [default to undefined]
**migratedJournalId** | **number** |  | [optional] [default to undefined]
**voidedDate** | **string** |  | [optional] [readonly] [default to undefined]
**voidedJournalEntryOrder** | **string** |  | [optional] [readonly] [default to undefined]
**amortizations** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**rampUseSandbox** | **string** |  | [optional] [readonly] [default to undefined]
**zipMetadata** | **string** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**paymentTermName** | **string** |  | [optional] [readonly] [default to undefined]
**searchVector** | **string** |  | [optional] [readonly] [default to undefined]
**searchText** | **string** |  | [optional] [readonly] [default to undefined]
**mailingAddress** | **string** |  | [optional] [default to undefined]
**terms** | [**TermsEnum**](TermsEnum.md) |  | [optional] [default to undefined]
**billNumber** | **string** |  | [optional] [default to undefined]
**billDate** | **string** |  | [optional] [default to undefined]
**dueDate** | **string** |  | [optional] [default to undefined]
**paidDate** | **string** |  | [optional] [default to undefined]
**messageOnBill** | **string** |  | [optional] [default to undefined]
**sourceId** | **string** |  | [optional] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**externalRampId** | **string** |  | [optional] [default to undefined]
**paymentStatus** | [**AccountingBillPaymentStatusEnum**](AccountingBillPaymentStatusEnum.md) |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**taxBehavior** | [**TaxBehaviorEnum**](TaxBehaviorEnum.md) |  | [optional] [default to undefined]
**billType** | [**BillTypeEnum**](BillTypeEnum.md) |  | [optional] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**vendor** | **number** |  | [optional] [default to undefined]
**paymentTerm** | **number** | Payment term for this bill | [optional] [default to undefined]
**journalEntry** | **number** |  | [optional] [default to undefined]
**sourceFile** | **number** |  | [optional] [default to undefined]
**taxRate** | **number** |  | [optional] [default to undefined]
**apAccount** | **number** | Accounts Payable account for this bill | [optional] [default to undefined]
**voidedJournalEntry** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedAccountingBill } from 'campfire-typescript-sdk';

const instance: PatchedAccountingBill = {
    id,
    lines,
    payments,
    paymentJournalEntries,
    status,
    pastDueDays,
    entityName,
    entityCurrency,
    vendorName,
    apAccountName,
    attachments,
    totalAmount,
    amountDue,
    amountPaid,
    itemDate,
    migratedJournalId,
    voidedDate,
    voidedJournalEntryOrder,
    amortizations,
    lastModifiedAt,
    rampUseSandbox,
    zipMetadata,
    isDeleted,
    deletedAt,
    paymentTermName,
    searchVector,
    searchText,
    mailingAddress,
    terms,
    billNumber,
    billDate,
    dueDate,
    paidDate,
    messageOnBill,
    sourceId,
    source,
    externalRampId,
    paymentStatus,
    currency,
    exchangeRate,
    exchangeRateBook,
    createdAt,
    taxBehavior,
    billType,
    customer,
    entity,
    vendor,
    paymentTerm,
    journalEntry,
    sourceFile,
    taxRate,
    apAccount,
    voidedJournalEntry,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

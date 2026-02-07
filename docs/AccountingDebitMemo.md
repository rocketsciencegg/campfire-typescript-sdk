# AccountingDebitMemo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**lines** | [**Array&lt;AccountingDebitMemoLine&gt;**](AccountingDebitMemoLine.md) |  | [default to undefined]
**payments** | [**Array&lt;AccountingDebitMemoPayment&gt;**](AccountingDebitMemoPayment.md) |  | [readonly] [default to undefined]
**amountRemaining** | **number** | Calculate amount remaining from database fields | [readonly] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**entityCurrency** | **string** |  | [readonly] [default to undefined]
**vendorName** | **string** |  | [readonly] [default to undefined]
**debitAccountNumber** | **string** |  | [readonly] [default to undefined]
**debitAccountName** | **string** | Combines account number and name in the format \&quot;number - name\&quot; | [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [readonly] [default to undefined]
**debitMemoNumber** | **string** |  | [optional] [default to undefined]
**migratedJournalId** | **number** |  | [optional] [default to undefined]
**voidedDate** | **string** |  | [readonly] [default to undefined]
**voidedJournalEntryOrder** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**searchVector** | **string** |  | [readonly] [default to undefined]
**searchText** | **string** |  | [readonly] [default to undefined]
**refNumber** | **string** |  | [optional] [default to undefined]
**debitMemoDate** | **string** |  | [default to undefined]
**appliedDate** | **string** |  | [optional] [default to undefined]
**messageOnDebitMemo** | **string** |  | [optional] [default to undefined]
**sourceId** | **string** |  | [optional] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**applicationStatus** | [**ApplicationStatusEnum**](ApplicationStatusEnum.md) |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**totalAmount** | **number** | Sum of all line item amounts | [optional] [default to undefined]
**amountUsed** | **number** | Sum of all non-voided payment amounts | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [default to undefined]
**vendor** | **number** |  | [optional] [default to undefined]
**debitAccount** | **number** |  | [optional] [default to undefined]
**journalEntry** | **number** |  | [optional] [default to undefined]
**voidedJournalEntry** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { AccountingDebitMemo } from 'campfire-typescript-sdk';

const instance: AccountingDebitMemo = {
    id,
    lines,
    payments,
    amountRemaining,
    entityName,
    entityCurrency,
    vendorName,
    debitAccountNumber,
    debitAccountName,
    attachments,
    debitMemoNumber,
    migratedJournalId,
    voidedDate,
    voidedJournalEntryOrder,
    lastModifiedAt,
    isDeleted,
    deletedAt,
    searchVector,
    searchText,
    refNumber,
    debitMemoDate,
    appliedDate,
    messageOnDebitMemo,
    sourceId,
    source,
    applicationStatus,
    currency,
    exchangeRate,
    exchangeRateBook,
    createdAt,
    totalAmount,
    amountUsed,
    customer,
    entity,
    vendor,
    debitAccount,
    journalEntry,
    voidedJournalEntry,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

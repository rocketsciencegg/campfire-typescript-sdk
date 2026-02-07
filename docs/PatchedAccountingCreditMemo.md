# PatchedAccountingCreditMemo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**lines** | [**Array&lt;AccountingCreditMemoLine&gt;**](AccountingCreditMemoLine.md) |  | [optional] [default to undefined]
**payments** | [**Array&lt;AccountingCreditMemoPayment&gt;**](AccountingCreditMemoPayment.md) |  | [optional] [readonly] [default to undefined]
**amountRemaining** | **number** | Calculate amount remaining from database fields | [optional] [readonly] [default to undefined]
**entityName** | **string** |  | [optional] [readonly] [default to undefined]
**entityCurrency** | **string** |  | [optional] [readonly] [default to undefined]
**clientName** | **string** |  | [optional] [readonly] [default to undefined]
**clientEmail** | **string** |  | [optional] [readonly] [default to undefined]
**contractName** | **string** |  | [optional] [readonly] [default to undefined]
**creditAccountNumber** | **string** |  | [optional] [readonly] [default to undefined]
**creditAccountName** | **string** | Combines account number and name in the format \&quot;number - name\&quot; | [optional] [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [optional] [readonly] [default to undefined]
**creditMemoNumber** | **string** |  | [optional] [default to undefined]
**migratedJournalId** | **number** |  | [optional] [default to undefined]
**voidedDate** | **string** |  | [optional] [readonly] [default to undefined]
**voidedJournalEntryOrder** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**searchVector** | **string** |  | [optional] [readonly] [default to undefined]
**searchText** | **string** |  | [optional] [readonly] [default to undefined]
**refNumber** | **string** |  | [optional] [default to undefined]
**creditMemoDate** | **string** |  | [optional] [default to undefined]
**appliedDate** | **string** |  | [optional] [default to undefined]
**messageOnCreditMemo** | **string** |  | [optional] [default to undefined]
**applicationStatus** | [**ApplicationStatusEnum**](ApplicationStatusEnum.md) |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**lastSentAt** | **string** |  | [optional] [default to undefined]
**anrokTransactionId** | **string** | ID of the negation transaction in Anrok for this credit memo | [optional] [default to undefined]
**totalAmount** | **number** | Sum of all line item amounts | [optional] [default to undefined]
**amountUsed** | **number** | Sum of all non-voided payment amounts | [optional] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**client** | **number** |  | [optional] [default to undefined]
**creditAccount** | **number** |  | [optional] [default to undefined]
**journalEntry** | **number** |  | [optional] [default to undefined]
**contract** | **number** |  | [optional] [default to undefined]
**voidedJournalEntry** | **number** |  | [optional] [default to undefined]
**anrokConnection** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedAccountingCreditMemo } from 'campfire-typescript-sdk';

const instance: PatchedAccountingCreditMemo = {
    id,
    lines,
    payments,
    amountRemaining,
    entityName,
    entityCurrency,
    clientName,
    clientEmail,
    contractName,
    creditAccountNumber,
    creditAccountName,
    attachments,
    creditMemoNumber,
    migratedJournalId,
    voidedDate,
    voidedJournalEntryOrder,
    lastModifiedAt,
    isDeleted,
    deletedAt,
    searchVector,
    searchText,
    refNumber,
    creditMemoDate,
    appliedDate,
    messageOnCreditMemo,
    applicationStatus,
    currency,
    exchangeRate,
    exchangeRateBook,
    createdAt,
    lastSentAt,
    anrokTransactionId,
    totalAmount,
    amountUsed,
    customer,
    entity,
    client,
    creditAccount,
    journalEntry,
    contract,
    voidedJournalEntry,
    anrokConnection,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# AccountingCreditMemo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**lines** | [**Array&lt;AccountingCreditMemoLine&gt;**](AccountingCreditMemoLine.md) |  | [default to undefined]
**payments** | [**Array&lt;AccountingCreditMemoPayment&gt;**](AccountingCreditMemoPayment.md) |  | [readonly] [default to undefined]
**amountRemaining** | **number** | Calculate amount remaining from database fields | [readonly] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**entityCurrency** | **string** |  | [readonly] [default to undefined]
**clientName** | **string** |  | [readonly] [default to undefined]
**clientEmail** | **string** |  | [readonly] [default to undefined]
**contractName** | **string** |  | [readonly] [default to undefined]
**creditAccountNumber** | **string** |  | [readonly] [default to undefined]
**creditAccountName** | **string** | Combines account number and name in the format \&quot;number - name\&quot; | [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [readonly] [default to undefined]
**creditMemoNumber** | **string** |  | [optional] [default to undefined]
**migratedJournalId** | **number** |  | [optional] [default to undefined]
**voidedDate** | **string** |  | [readonly] [default to undefined]
**voidedJournalEntryOrder** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**searchVector** | **string** |  | [readonly] [default to undefined]
**searchText** | **string** |  | [readonly] [default to undefined]
**refNumber** | **string** |  | [optional] [default to undefined]
**creditMemoDate** | **string** |  | [default to undefined]
**appliedDate** | **string** |  | [optional] [default to undefined]
**messageOnCreditMemo** | **string** |  | [optional] [default to undefined]
**applicationStatus** | [**ApplicationStatusEnum**](ApplicationStatusEnum.md) |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastSentAt** | **string** |  | [optional] [default to undefined]
**anrokTransactionId** | **string** | ID of the negation transaction in Anrok for this credit memo | [optional] [default to undefined]
**totalAmount** | **number** | Sum of all line item amounts | [optional] [default to undefined]
**amountUsed** | **number** | Sum of all non-voided payment amounts | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [default to undefined]
**client** | **number** |  | [optional] [default to undefined]
**creditAccount** | **number** |  | [optional] [default to undefined]
**journalEntry** | **number** |  | [optional] [default to undefined]
**contract** | **number** |  | [optional] [default to undefined]
**voidedJournalEntry** | **number** |  | [optional] [default to undefined]
**anrokConnection** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { AccountingCreditMemo } from 'campfire-typescript-sdk';

const instance: AccountingCreditMemo = {
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

# JournalEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**transactions** | [**Array&lt;ChartTransaction&gt;**](ChartTransaction.md) |  | [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [readonly] [default to undefined]
**invoice** | **number** |  | [readonly] [default to undefined]
**reversalOfOrder** | **string** |  | [readonly] [default to undefined]
**reversals** | **Array&lt;number&gt;** |  | [readonly] [default to undefined]
**reversalDate** | **string** |  | [optional] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**entityCurrency** | **string** |  | [readonly] [default to undefined]
**order** | **string** |  | [optional] [default to undefined]
**revenueTransactions** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**bulkUpload** | **boolean** |  | [optional] [default to undefined]
**chatUuid** | **string** |  | [optional] [default to undefined]
**updateReversal** | **boolean** |  | [optional] [default to false]
**creditMemos** | **Array&lt;number&gt;** |  | [readonly] [default to undefined]
**debitMemos** | **Array&lt;number&gt;** |  | [readonly] [default to undefined]
**journalsToDelete** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**rampUseSandbox** | **string** |  | [readonly] [default to undefined]
**searchVector** | **string** |  | [readonly] [default to undefined]
**searchText** | **string** |  | [readonly] [default to undefined]
**type** | [**TypeF6cEnum**](TypeF6cEnum.md) |  | [optional] [default to undefined]
**journalId** | **string** |  | [optional] [default to undefined]
**memo** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**useAverageRate** | **boolean** |  | [optional] [default to undefined]
**createdAutomatically** | **boolean** |  | [optional] [default to undefined]
**date** | **string** |  | [optional] [default to undefined]
**refNumber** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**sourceId** | **string** |  | [optional] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**recurrentJournalEntry** | **number** |  | [optional] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**reversalOf** | **number** |  | [optional] [default to undefined]
**intercompanyJournal** | **number** |  | [optional] [default to undefined]
**sourceFile** | **number** |  | [optional] [default to undefined]
**chat** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { JournalEntry } from 'campfire-typescript-sdk';

const instance: JournalEntry = {
    id,
    isDeleted,
    deletedAt,
    transactions,
    attachments,
    invoice,
    reversalOfOrder,
    reversals,
    reversalDate,
    entityName,
    entityCurrency,
    order,
    revenueTransactions,
    bulkUpload,
    chatUuid,
    updateReversal,
    creditMemos,
    debitMemos,
    journalsToDelete,
    rampUseSandbox,
    searchVector,
    searchText,
    type,
    journalId,
    memo,
    currency,
    exchangeRate,
    exchangeRateBook,
    useAverageRate,
    createdAutomatically,
    date,
    refNumber,
    createdAt,
    source,
    sourceId,
    lastModifiedAt,
    customer,
    recurrentJournalEntry,
    entity,
    reversalOf,
    intercompanyJournal,
    sourceFile,
    chat,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# IntercompanyJournalEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**transactions** | [**Array&lt;ChartTransaction&gt;**](ChartTransaction.md) |  | [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [readonly] [default to undefined]
**reversalOfOrder** | **string** |  | [readonly] [default to undefined]
**reversals** | **Array&lt;{ [key: string]: any; }&gt;** |  | [readonly] [default to undefined]
**reversalDate** | **string** |  | [optional] [default to undefined]
**order** | **string** |  | [optional] [default to undefined]
**journalsToDelete** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**exchangeRates** | **any** |  | [optional] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**sourceId** | **string** |  | [optional] [default to undefined]
**sourceFile** | **number** |  | [optional] [default to undefined]
**csvUploadRunId** | **number** | Upload run to record this row against; must be one of your own runs. Ignored on update. | [optional] [default to undefined]
**csvUploadRowNumber** | **number** | Spreadsheet row this document starts on (the header is row 1), recorded with it. Ignored on update. | [optional] [default to undefined]
**closeTaskId** | **string** |  | [optional] [default to undefined]
**chatUuid** | **string** |  | [optional] [default to undefined]
**bankTransactionId** | **number** |  | [optional] [default to undefined]
**statementTransactionId** | **number** |  | [optional] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**type** | [**Type4aaEnum**](Type4aaEnum.md) |  | [optional] [default to undefined]
**journalId** | **string** |  | [optional] [default to undefined]
**memo** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**createdAutomatically** | **boolean** |  | [optional] [default to undefined]
**date** | **string** |  | [optional] [default to undefined]
**refNumber** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**reversalOf** | **number** |  | [optional] [default to undefined]
**entities** | **Array&lt;number&gt;** | Entities involved in this intercompany journal entry. Used for consolidation filtering. | [optional] [default to undefined]

## Example

```typescript
import { IntercompanyJournalEntry } from 'campfire-typescript-sdk';

const instance: IntercompanyJournalEntry = {
    id,
    transactions,
    attachments,
    reversalOfOrder,
    reversals,
    reversalDate,
    order,
    journalsToDelete,
    exchangeRates,
    source,
    sourceId,
    sourceFile,
    csvUploadRunId,
    csvUploadRowNumber,
    closeTaskId,
    chatUuid,
    bankTransactionId,
    statementTransactionId,
    isDeleted,
    deletedAt,
    type,
    journalId,
    memo,
    currency,
    createdAutomatically,
    date,
    refNumber,
    createdAt,
    lastModifiedAt,
    customer,
    reversalOf,
    entities,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

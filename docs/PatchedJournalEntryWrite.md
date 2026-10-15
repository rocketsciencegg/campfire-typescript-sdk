# PatchedJournalEntryWrite

Documentation-only request schema for creating/updating a journal entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**transactions** | [**Array&lt;JournalEntryLineWrite&gt;**](JournalEntryLineWrite.md) |  | [optional] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [optional] [readonly] [default to undefined]
**invoice** | **number** |  | [optional] [readonly] [default to undefined]
**reversalOfOrder** | **string** |  | [optional] [readonly] [default to undefined]
**reversals** | **Array&lt;{ [key: string]: any; }&gt;** |  | [optional] [readonly] [default to undefined]
**reversalDate** | **string** |  | [optional] [default to undefined]
**entityName** | **string** |  | [optional] [readonly] [default to undefined]
**entityCurrency** | **string** |  | [optional] [readonly] [default to undefined]
**createdBy** | **number** | Derived user ID of the journal entry creator. Check created_by_source before explaining provenance. | [optional] [readonly] [default to undefined]
**createdByName** | **string** | Derived name of the journal entry creator. Check created_by_source before explaining provenance. | [optional] [readonly] [default to undefined]
**createdBySource** | **string** | Provenance for created_by and created_by_name: \&#39;draft_queue_created_by\&#39;, \&#39;chart_transaction_last_modified_by_fallback\&#39;, or null. | [optional] [readonly] [default to undefined]
**order** | **string** |  | [optional] [default to undefined]
**revenueTransactions** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**bulkUpload** | **boolean** |  | [optional] [default to undefined]
**chatUuid** | **string** |  | [optional] [default to undefined]
**closeTaskId** | **string** |  | [optional] [default to undefined]
**updateReversal** | **boolean** |  | [optional] [default to false]
**creditMemos** | **Array&lt;{ [key: string]: any; }&gt;** |  | [optional] [readonly] [default to undefined]
**debitMemos** | **Array&lt;{ [key: string]: any; }&gt;** |  | [optional] [readonly] [default to undefined]
**journalsToDelete** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**rampUseSandbox** | **boolean** |  | [optional] [readonly] [default to undefined]
**navanRegion** | **string** | Navan data region (&#x60;&#x60;US&#x60;&#x60;/&#x60;&#x60;EU&#x60;&#x60;) for a Navan-sourced journal entry, else &#x60;&#x60;None&#x60;&#x60;.  Mirrors &#x60;&#x60;ramp_use_sandbox&#x60;&#x60;: the frontend builds the \&quot;Open in Navan\&quot; deep link from &#x60;&#x60;source_id&#x60;&#x60; and uses this to pick the web-app host (US -&gt; app.navan.com, EU -&gt; app-fra.navan.com). Navan records carry no FK to their connection, so the region is resolved per customer and memoized to avoid an N+1 lookup across a transaction list. | [optional] [readonly] [default to undefined]
**floatBillId** | **string** | Float id of the bill paid by a Float bill-payment journal entry, else &#x60;&#x60;None&#x60;&#x60;.  Payment journal entries store the Float payment id as &#x60;&#x60;source_id&#x60;&#x60;, which has no page of its own in Float\&#39;s web app — the frontend deep-links \&quot;View on Float\&quot; to the paid bill instead. | [optional] [readonly] [default to undefined]
**allocationSyncRunId** | **number** |  | [optional] [readonly] [default to undefined]
**allocationId** | **number** |  | [optional] [readonly] [default to undefined]
**allocationName** | **string** |  | [optional] [readonly] [default to undefined]
**linkedSourceDocuments** | **Array&lt;{ [key: string]: any; }&gt;** | Documents this journal is posted from; deleting it deletes them too. | [optional] [readonly] [default to undefined]
**csvUploadRunId** | **number** | Upload run to record this row against; must be one of your own runs. Ignored on update. | [optional] [default to undefined]
**csvUploadRowNumber** | **number** | Spreadsheet row this document starts on (the header is row 1), recorded with it. Ignored on update. | [optional] [default to undefined]
**searchVector** | **string** |  | [optional] [readonly] [default to undefined]
**searchText** | **string** |  | [optional] [readonly] [default to undefined]
**type** | [**Type4aaEnum**](Type4aaEnum.md) |  | [optional] [default to undefined]
**journalId** | **string** |  | [optional] [default to undefined]
**memo** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**useAverageRate** | **boolean** |  | [optional] [default to undefined]
**createdAutomatically** | **boolean** |  | [optional] [default to undefined]
**date** | **string** |  | [optional] [default to undefined]
**refNumber** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**sourceId** | **string** |  | [optional] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**recurrentJournalEntry** | **number** |  | [optional] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**reversalOf** | **number** |  | [optional] [default to undefined]
**intercompanyJournal** | **number** |  | [optional] [default to undefined]
**sourceFile** | **number** |  | [optional] [default to undefined]
**chat** | **number** |  | [optional] [default to undefined]
**lastDraft** | **number** |  | [optional] [readonly] [default to undefined]

## Example

```typescript
import { PatchedJournalEntryWrite } from 'campfire-typescript-sdk';

const instance: PatchedJournalEntryWrite = {
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
    createdBy,
    createdByName,
    createdBySource,
    order,
    revenueTransactions,
    bulkUpload,
    chatUuid,
    closeTaskId,
    updateReversal,
    creditMemos,
    debitMemos,
    journalsToDelete,
    rampUseSandbox,
    navanRegion,
    floatBillId,
    allocationSyncRunId,
    allocationId,
    allocationName,
    linkedSourceDocuments,
    csvUploadRunId,
    csvUploadRowNumber,
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
    lastDraft,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

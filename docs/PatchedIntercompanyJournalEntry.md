# PatchedIntercompanyJournalEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**transactions** | [**Array&lt;ChartTransaction&gt;**](ChartTransaction.md) |  | [optional] [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [optional] [readonly] [default to undefined]
**reversalOfOrder** | **string** |  | [optional] [readonly] [default to undefined]
**reversals** | **Array&lt;number&gt;** |  | [optional] [readonly] [default to undefined]
**reversalDate** | **string** |  | [optional] [default to undefined]
**entities** | **any** |  | [optional] [default to undefined]
**entityName** | **string** |  | [optional] [readonly] [default to undefined]
**entityCurrency** | **string** |  | [optional] [readonly] [default to undefined]
**order** | **string** |  | [optional] [default to undefined]
**journalsToDelete** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**type** | [**TypeF6cEnum**](TypeF6cEnum.md) |  | [optional] [default to undefined]
**journalId** | **string** |  | [optional] [default to undefined]
**memo** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**createdAutomatically** | **boolean** |  | [optional] [default to undefined]
**date** | **string** |  | [optional] [default to undefined]
**refNumber** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**reversalOf** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedIntercompanyJournalEntry } from 'campfire-typescript-sdk';

const instance: PatchedIntercompanyJournalEntry = {
    id,
    transactions,
    attachments,
    reversalOfOrder,
    reversals,
    reversalDate,
    entities,
    entityName,
    entityCurrency,
    order,
    journalsToDelete,
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
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# IntercompanyJournalEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**transactions** | [**Array&lt;ChartTransaction&gt;**](ChartTransaction.md) |  | [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [readonly] [default to undefined]
**reversalOfOrder** | **string** |  | [readonly] [default to undefined]
**reversals** | **Array&lt;number&gt;** |  | [readonly] [default to undefined]
**reversalDate** | **string** |  | [optional] [default to undefined]
**entities** | **any** |  | [optional] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**entityCurrency** | **string** |  | [readonly] [default to undefined]
**order** | **string** |  | [optional] [default to undefined]
**journalsToDelete** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**type** | [**TypeF6cEnum**](TypeF6cEnum.md) |  | [optional] [default to undefined]
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

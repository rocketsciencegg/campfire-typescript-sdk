# BulkAcceptSuggestions

Selection spec — same shape as the transactions bulk-update endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggestionClass** | [**SuggestionClassEnum**](SuggestionClassEnum.md) |  | [default to undefined]
**mode** | [**ModeEnum**](ModeEnum.md) |  | [optional] [default to undefined]
**transactionIds** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**excludedTransactionIds** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**filters** | **any** |  | [optional] [default to undefined]
**expectedCount** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { BulkAcceptSuggestions } from 'campfire-typescript-sdk';

const instance: BulkAcceptSuggestions = {
    suggestionClass,
    mode,
    transactionIds,
    excludedTransactionIds,
    filters,
    expectedCount,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

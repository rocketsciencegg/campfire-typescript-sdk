# MergeChartTransactionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactionIds** | **Array&lt;number&gt;** | Array of exactly two transaction IDs to merge | [default to undefined]
**transactionMatchId** | **number** | Optional id of the AutoMergeSuggestion TransactionMatch the user explicitly accepted; marks the merge as a suggestion accept | [optional] [default to undefined]

## Example

```typescript
import { MergeChartTransactionsRequest } from 'campfire-typescript-sdk';

const instance: MergeChartTransactionsRequest = {
    transactionIds,
    transactionMatchId,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

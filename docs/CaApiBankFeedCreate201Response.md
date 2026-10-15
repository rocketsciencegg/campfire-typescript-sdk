# CaApiBankFeedCreate201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **string** |  | [optional] [default to undefined]
**accountId** | **number** |  | [optional] [default to undefined]
**submittedCount** | **number** |  | [optional] [default to undefined]
**createdCount** | **number** |  | [optional] [default to undefined]
**skippedCount** | **number** |  | [optional] [default to undefined]
**skippedTransactions** | [**Array&lt;CaApiBankFeedCreate201ResponseSkippedTransactionsInner&gt;**](CaApiBankFeedCreate201ResponseSkippedTransactionsInner.md) |  | [optional] [default to undefined]
**failedCount** | **number** |  | [optional] [default to undefined]
**failedTransactions** | [**Array&lt;CaApiBankFeedCreate201ResponseSkippedTransactionsInner&gt;**](CaApiBankFeedCreate201ResponseSkippedTransactionsInner.md) |  | [optional] [default to undefined]

## Example

```typescript
import { CaApiBankFeedCreate201Response } from 'campfire-typescript-sdk';

const instance: CaApiBankFeedCreate201Response = {
    message,
    accountId,
    submittedCount,
    createdCount,
    skippedCount,
    skippedTransactions,
    failedCount,
    failedTransactions,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

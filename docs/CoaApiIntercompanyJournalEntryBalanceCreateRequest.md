# CoaApiIntercompanyJournalEntryBalanceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **string** | Journal entry date (ISO format: YYYY-MM-DD). Used for auto-fetching exchange rates if exchange_rates is empty. | [optional] [default to undefined]
**transactions** | **Array&lt;object&gt;** | List of transaction objects | [default to undefined]
**exchangeRates** | **Array&lt;object&gt;** | List of exchange rate objects (optional - will be auto-fetched if empty and date is provided) | [optional] [default to undefined]

## Example

```typescript
import { CoaApiIntercompanyJournalEntryBalanceCreateRequest } from 'campfire-typescript-sdk';

const instance: CoaApiIntercompanyJournalEntryBalanceCreateRequest = {
    date,
    transactions,
    exchangeRates,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

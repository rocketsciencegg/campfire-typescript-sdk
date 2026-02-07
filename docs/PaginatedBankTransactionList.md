# PaginatedBankTransactionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **number** |  | [default to undefined]
**next** | **string** |  | [optional] [default to undefined]
**previous** | **string** |  | [optional] [default to undefined]
**results** | [**Array&lt;BankTransaction&gt;**](BankTransaction.md) |  | [default to undefined]

## Example

```typescript
import { PaginatedBankTransactionList } from 'campfire-typescript-sdk';

const instance: PaginatedBankTransactionList = {
    count,
    next,
    previous,
    results,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

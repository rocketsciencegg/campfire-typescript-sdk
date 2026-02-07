# ReconciliationReportV2SourceTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**currency** | **string** |  | [readonly] [default to undefined]
**postedAt** | **string** |  | [optional] [default to undefined]
**debitAmountInCurrency** | **string** |  | [readonly] [default to undefined]
**creditAmountInCurrency** | **string** |  | [readonly] [default to undefined]
**bankDescription** | **string** |  | [optional] [default to undefined]
**reconciliationTransaction** | [**Array&lt;ReconciliationReportV2Transaction&gt;**](ReconciliationReportV2Transaction.md) |  | [readonly] [default to undefined]
**journalId** | **number** |  | [readonly] [default to undefined]
**journalOrder** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { ReconciliationReportV2SourceTransaction } from 'campfire-typescript-sdk';

const instance: ReconciliationReportV2SourceTransaction = {
    id,
    currency,
    postedAt,
    debitAmountInCurrency,
    creditAmountInCurrency,
    bankDescription,
    reconciliationTransaction,
    journalId,
    journalOrder,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

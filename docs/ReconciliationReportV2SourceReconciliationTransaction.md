# ReconciliationReportV2SourceReconciliationTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**status** | [**ReconciliationReportV2SourceReconciliationTransactionStatusEnum**](ReconciliationReportV2SourceReconciliationTransactionStatusEnum.md) |  | [optional] [default to undefined]
**suggestionId** | **number** |  | [readonly] [default to undefined]
**suggestion** | [**ReconciliationReportV2StatementTransaction**](ReconciliationReportV2StatementTransaction.md) |  | [readonly] [default to undefined]

## Example

```typescript
import { ReconciliationReportV2SourceReconciliationTransaction } from 'campfire-typescript-sdk';

const instance: ReconciliationReportV2SourceReconciliationTransaction = {
    id,
    status,
    suggestionId,
    suggestion,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

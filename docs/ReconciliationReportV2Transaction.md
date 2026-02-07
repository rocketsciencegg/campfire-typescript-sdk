# ReconciliationReportV2Transaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**transaction** | [**ChartTransaction**](ChartTransaction.md) |  | [readonly] [default to undefined]
**suggestion** | [**ReconciliationReportV2StatementTransaction**](ReconciliationReportV2StatementTransaction.md) |  | [readonly] [default to undefined]
**status** | [**ReconciliationReportV2TransactionStatusEnum**](ReconciliationReportV2TransactionStatusEnum.md) |  | [optional] [default to undefined]
**suggestedTransaction** | **string** |  | [optional] [default to undefined]
**suggestedTransactionData** | **any** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [default to undefined]
**reconciliationReport** | **number** |  | [default to undefined]

## Example

```typescript
import { ReconciliationReportV2Transaction } from 'campfire-typescript-sdk';

const instance: ReconciliationReportV2Transaction = {
    id,
    transaction,
    suggestion,
    status,
    suggestedTransaction,
    suggestedTransactionData,
    createdAt,
    lastModifiedAt,
    customer,
    reconciliationReport,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

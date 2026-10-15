# ReconciliationReportV2StatementTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**pageNumber** | **number** |  | [readonly] [default to undefined]
**reconciliationTransactionId** | **string** |  | [readonly] [default to undefined]
**sourceTransactionId** | **string** |  | [readonly] [default to undefined]
**isMatched** | **string** |  | [readonly] [default to undefined]
**date** | **string** |  | [default to undefined]
**deposit** | **number** |  | [optional] [default to undefined]
**withdrawal** | **number** |  | [optional] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**isCleared** | **boolean** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**reconciliationReport** | **number** |  | [readonly] [default to undefined]
**page** | **number** |  | [readonly] [default to undefined]

## Example

```typescript
import { ReconciliationReportV2StatementTransaction } from 'campfire-typescript-sdk';

const instance: ReconciliationReportV2StatementTransaction = {
    id,
    pageNumber,
    reconciliationTransactionId,
    sourceTransactionId,
    isMatched,
    date,
    deposit,
    withdrawal,
    description,
    isCleared,
    createdAt,
    lastModifiedAt,
    customer,
    reconciliationReport,
    page,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# ReconciliationReportV2List


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**account** | **number** |  | [default to undefined]
**accountName** | **string** |  | [readonly] [default to undefined]
**accountNumber** | **string** |  | [readonly] [default to undefined]
**accountType** | **string** |  | [readonly] [default to undefined]
**accountSubtype** | **string** |  | [readonly] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**statementStartingDate** | **string** |  | [optional] [default to undefined]
**statementEndingDate** | **string** |  | [optional] [default to undefined]
**startingBalance** | **number** |  | [optional] [default to undefined]
**endingBalance** | **number** |  | [optional] [default to undefined]
**totalCreditAmount** | **number** |  | [optional] [default to undefined]
**totalDebitAmount** | **number** |  | [optional] [default to undefined]
**adjustments** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**asyncTask** | [**AsyncTask**](AsyncTask.md) |  | [readonly] [default to undefined]
**matchingTask** | **number** |  | [optional] [default to undefined]
**reconciledBy** | **number** |  | [optional] [default to undefined]
**reconciledByName** | **string** |  | [readonly] [default to undefined]
**reconciledByEmail** | **string** |  | [readonly] [default to undefined]
**reconciledOn** | **string** |  | [optional] [default to undefined]
**approvedBy** | **number** |  | [readonly] [default to undefined]
**approvedByName** | **string** |  | [readonly] [default to undefined]
**approvedByEmail** | **string** |  | [readonly] [default to undefined]
**approvedOn** | **string** |  | [readonly] [default to undefined]
**status** | [**Status8ecEnum**](Status8ecEnum.md) |  | [optional] [default to undefined]
**unmatchedStatementTransactions** | **any** |  | [optional] [default to undefined]
**statementRecognitionCostUsd** | **number** | Estimated USD cost of AI bank-statement parsing for this report (from summed page token usage). | [optional] [default to undefined]
**statementRecognitionInputTokens** | **number** | Sum of input tokens from statement parsing across all pages (set on finalize). | [optional] [default to undefined]
**statementRecognitionOutputTokens** | **number** | Sum of output tokens from statement parsing across all pages (set on finalize). | [optional] [default to undefined]
**statementRecognitionTokenTotal** | **number** | Input plus output tokens for this report (set on finalize). | [optional] [default to undefined]
**statementRecognitionModelName** | **string** | LLM model used for statement parsing when token totals were recorded. | [optional] [default to undefined]

## Example

```typescript
import { ReconciliationReportV2List } from 'campfire-typescript-sdk';

const instance: ReconciliationReportV2List = {
    id,
    customer,
    entity,
    entityName,
    account,
    accountName,
    accountNumber,
    accountType,
    accountSubtype,
    currency,
    statementStartingDate,
    statementEndingDate,
    startingBalance,
    endingBalance,
    totalCreditAmount,
    totalDebitAmount,
    adjustments,
    createdAt,
    lastModifiedAt,
    asyncTask,
    matchingTask,
    reconciledBy,
    reconciledByName,
    reconciledByEmail,
    reconciledOn,
    approvedBy,
    approvedByName,
    approvedByEmail,
    approvedOn,
    status,
    unmatchedStatementTransactions,
    statementRecognitionCostUsd,
    statementRecognitionInputTokens,
    statementRecognitionOutputTokens,
    statementRecognitionTokenTotal,
    statementRecognitionModelName,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

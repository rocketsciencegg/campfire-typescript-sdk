# ReconciliationReportV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**accountName** | **string** |  | [readonly] [default to undefined]
**accountNumber** | **string** |  | [readonly] [default to undefined]
**accountType** | **string** |  | [readonly] [default to undefined]
**accountSubtype** | **string** |  | [readonly] [default to undefined]
**reconciledByName** | **string** |  | [readonly] [default to undefined]
**reconciledByEmail** | **string** |  | [readonly] [default to undefined]
**approvedByName** | **string** |  | [readonly] [default to undefined]
**approvedByEmail** | **string** |  | [readonly] [default to undefined]
**asyncTask** | [**AsyncTask**](AsyncTask.md) |  | [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [readonly] [default to undefined]
**csvStatements** | **string** |  | [readonly] [default to undefined]
**clearedTotalDebits** | **string** |  | [readonly] [default to undefined]
**clearedTotalCredits** | **string** |  | [readonly] [default to undefined]
**clearedActivity** | **string** |  | [readonly] [default to undefined]
**clearedItemCount** | **string** |  | [readonly] [default to undefined]
**matchedTotalDebits** | **string** |  | [readonly] [default to undefined]
**matchedTotalCredits** | **string** |  | [readonly] [default to undefined]
**matchedActivity** | **string** |  | [readonly] [default to undefined]
**matchedItemCount** | **string** |  | [readonly] [default to undefined]
**unreconciledTotalDebits** | **string** |  | [readonly] [default to undefined]
**unreconciledTotalCredits** | **string** |  | [readonly] [default to undefined]
**unreconciledActivity** | **string** |  | [readonly] [default to undefined]
**unreconciledGlItemCount** | **string** |  | [readonly] [default to undefined]
**unreconciledStatementLineCount** | **string** |  | [readonly] [default to undefined]
**unreconciledStatementActivity** | **string** |  | [readonly] [default to undefined]
**reconciliationDifference** | **string** |  | [readonly] [default to undefined]
**openTotalDebits** | **string** |  | [readonly] [default to undefined]
**openTotalCredits** | **string** |  | [readonly] [default to undefined]
**openActivity** | **string** |  | [readonly] [default to undefined]
**openGlItemCount** | **string** |  | [readonly] [default to undefined]
**openStatementLineCount** | **string** |  | [readonly] [default to undefined]
**openStatementActivity** | **string** |  | [readonly] [default to undefined]
**statementActivity** | **string** |  | [readonly] [default to undefined]
**openDifference** | **string** |  | [readonly] [default to undefined]
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
**reconciledOn** | **string** |  | [optional] [default to undefined]
**approvedOn** | **string** |  | [readonly] [default to undefined]
**status** | [**Status8ecEnum**](Status8ecEnum.md) |  | [optional] [default to undefined]
**unmatchedStatementTransactions** | **any** |  | [optional] [default to undefined]
**statementRecognitionCostUsd** | **number** | Estimated USD cost of AI bank-statement parsing for this report (from summed page token usage). | [optional] [default to undefined]
**statementRecognitionInputTokens** | **number** | Sum of input tokens from statement parsing across all pages (set on finalize). | [optional] [default to undefined]
**statementRecognitionOutputTokens** | **number** | Sum of output tokens from statement parsing across all pages (set on finalize). | [optional] [default to undefined]
**statementRecognitionTokenTotal** | **number** | Input plus output tokens for this report (set on finalize). | [optional] [default to undefined]
**statementRecognitionModelName** | **string** | LLM model used for statement parsing when token totals were recorded. | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**account** | **number** |  | [default to undefined]
**matchingTask** | **number** |  | [optional] [default to undefined]
**reconciledBy** | **number** |  | [optional] [default to undefined]
**approvedBy** | **number** |  | [readonly] [default to undefined]

## Example

```typescript
import { ReconciliationReportV2 } from 'campfire-typescript-sdk';

const instance: ReconciliationReportV2 = {
    id,
    entityName,
    accountName,
    accountNumber,
    accountType,
    accountSubtype,
    reconciledByName,
    reconciledByEmail,
    approvedByName,
    approvedByEmail,
    asyncTask,
    attachments,
    csvStatements,
    clearedTotalDebits,
    clearedTotalCredits,
    clearedActivity,
    clearedItemCount,
    matchedTotalDebits,
    matchedTotalCredits,
    matchedActivity,
    matchedItemCount,
    unreconciledTotalDebits,
    unreconciledTotalCredits,
    unreconciledActivity,
    unreconciledGlItemCount,
    unreconciledStatementLineCount,
    unreconciledStatementActivity,
    reconciliationDifference,
    openTotalDebits,
    openTotalCredits,
    openActivity,
    openGlItemCount,
    openStatementLineCount,
    openStatementActivity,
    statementActivity,
    openDifference,
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
    reconciledOn,
    approvedOn,
    status,
    unmatchedStatementTransactions,
    statementRecognitionCostUsd,
    statementRecognitionInputTokens,
    statementRecognitionOutputTokens,
    statementRecognitionTokenTotal,
    statementRecognitionModelName,
    customer,
    entity,
    account,
    matchingTask,
    reconciledBy,
    approvedBy,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

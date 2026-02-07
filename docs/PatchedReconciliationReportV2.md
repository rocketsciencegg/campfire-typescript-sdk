# PatchedReconciliationReportV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**entityName** | **string** |  | [optional] [readonly] [default to undefined]
**accountName** | **string** |  | [optional] [readonly] [default to undefined]
**accountNumber** | **string** |  | [optional] [readonly] [default to undefined]
**accountType** | **string** |  | [optional] [readonly] [default to undefined]
**accountSubtype** | **string** |  | [optional] [readonly] [default to undefined]
**reconciledByName** | **string** |  | [optional] [readonly] [default to undefined]
**reconciledByEmail** | **string** |  | [optional] [readonly] [default to undefined]
**approvedByName** | **string** |  | [optional] [readonly] [default to undefined]
**approvedByEmail** | **string** |  | [optional] [readonly] [default to undefined]
**asyncTask** | [**AsyncTask**](AsyncTask.md) |  | [optional] [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [optional] [readonly] [default to undefined]
**csvStatements** | **string** |  | [optional] [readonly] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**statementStartingDate** | **string** |  | [optional] [default to undefined]
**statementEndingDate** | **string** |  | [optional] [default to undefined]
**startingBalance** | **number** |  | [optional] [default to undefined]
**endingBalance** | **number** |  | [optional] [default to undefined]
**totalCreditAmount** | **number** |  | [optional] [default to undefined]
**totalDebitAmount** | **number** |  | [optional] [default to undefined]
**adjustments** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**reconciledOn** | **string** |  | [optional] [default to undefined]
**approvedOn** | **string** |  | [optional] [readonly] [default to undefined]
**status** | [**ReconciliationReportV2StatusEnum**](ReconciliationReportV2StatusEnum.md) |  | [optional] [default to undefined]
**unmatchedStatementTransactions** | **any** |  | [optional] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**account** | **number** |  | [optional] [default to undefined]
**matchingTask** | **number** |  | [optional] [default to undefined]
**reconciledBy** | **number** |  | [optional] [default to undefined]
**approvedBy** | **number** |  | [optional] [readonly] [default to undefined]

## Example

```typescript
import { PatchedReconciliationReportV2 } from 'campfire-typescript-sdk';

const instance: PatchedReconciliationReportV2 = {
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
    customer,
    entity,
    account,
    matchingTask,
    reconciledBy,
    approvedBy,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

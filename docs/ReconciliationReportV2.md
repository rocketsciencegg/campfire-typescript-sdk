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
**status** | [**ReconciliationReportV2StatusEnum**](ReconciliationReportV2StatusEnum.md) |  | [optional] [default to undefined]
**unmatchedStatementTransactions** | **any** |  | [optional] [default to undefined]
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

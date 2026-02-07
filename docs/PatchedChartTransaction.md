# PatchedChartTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**entityName** | **string** |  | [optional] [readonly] [default to undefined]
**entityCurrency** | **string** |  | [optional] [readonly] [default to undefined]
**accountName** | **string** | Combines account number and name in the format \&quot;number - name\&quot; | [optional] [readonly] [default to undefined]
**accountNumber** | **string** |  | [optional] [readonly] [default to undefined]
**vendorName** | **string** |  | [optional] [readonly] [default to undefined]
**vendorId** | **string** |  | [optional] [readonly] [default to undefined]
**departmentName** | **string** |  | [optional] [readonly] [default to undefined]
**parentDepartmentName** | **string** |  | [optional] [readonly] [default to undefined]
**parentDepartment** | **number** |  | [optional] [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [optional] [readonly] [default to undefined]
**journal** | **number** |  | [optional] [readonly] [default to undefined]
**journalOrder** | **string** |  | [optional] [readonly] [default to undefined]
**journalMemo** | **string** |  | [optional] [readonly] [default to undefined]
**journalType** | **string** |  | [optional] [readonly] [default to undefined]
**intercompanyJournal** | **number** |  | [optional] [readonly] [default to undefined]
**createdAutomatically** | **boolean** |  | [optional] [readonly] [default to undefined]
**journalAttachments** | **Array&lt;any&gt;** |  | [optional] [readonly] [default to undefined]
**journalTypeName** | **string** |  | [optional] [readonly] [default to undefined]
**invoice** | **string** |  | [optional] [readonly] [default to undefined]
**bill** | **string** |  | [optional] [readonly] [default to undefined]
**dateMonth** | **string** |  | [optional] [readonly] [default to undefined]
**dateYear** | **string** |  | [optional] [readonly] [default to undefined]
**balanceAfterTransaction** | **number** |  | [optional] [readonly] [default to undefined]
**bankAccount** | **string** |  | [optional] [readonly] [default to undefined]
**bankAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**account** | **number** |  | [optional] [default to undefined]
**lastModifiedByName** | **string** |  | [optional] [readonly] [default to undefined]
**accountType** | **string** |  | [optional] [readonly] [default to undefined]
**accountSubtype** | **string** |  | [optional] [readonly] [default to undefined]
**parentAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**files** | **string** |  | [optional] [readonly] [default to undefined]
**invoiceId** | **number** |  | [optional] [readonly] [default to undefined]
**invoiceNumber** | **string** |  | [optional] [readonly] [default to undefined]
**billId** | **number** |  | [optional] [readonly] [default to undefined]
**billNumber** | **string** |  | [optional] [readonly] [default to undefined]
**fileNames** | **string** |  | [optional] [readonly] [default to undefined]
**hasMatches** | **boolean** |  | [optional] [readonly] [default to undefined]
**hasAi** | **boolean** |  | [optional] [readonly] [default to undefined]
**hasRules** | **boolean** |  | [optional] [readonly] [default to undefined]
**hasMerges** | **boolean** |  | [optional] [readonly] [default to undefined]
**hasFixedAssetRuleMatches** | **boolean** |  | [optional] [readonly] [default to undefined]
**suggestedAccount** | **number** |  | [optional] [readonly] [default to undefined]
**suggestedAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**suggestedAccountNumber** | **string** |  | [optional] [readonly] [default to undefined]
**amount** | **number** |  | [optional] [readonly] [default to undefined]
**amountNative** | **number** |  | [optional] [readonly] [default to undefined]
**amountBook** | **number** |  | [optional] [readonly] [default to undefined]
**amortizationSchedule** | [**Array&lt;AmortizationSchedule&gt;**](AmortizationSchedule.md) |  | [optional] [readonly] [default to undefined]
**createdFixedAssets** | **string** |  | [optional] [readonly] [default to undefined]
**reconciliationReport** | **string** |  | [optional] [readonly] [default to undefined]
**opposingAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**opposingAccountNumber** | **string** |  | [optional] [readonly] [default to undefined]
**taxRate** | **number** |  | [optional] [default to undefined]
**applyBothSides** | **boolean** |  | [optional] [default to false]
**transactionMatchId** | **number** |  | [optional] [default to undefined]
**transactionId** | **string** |  | [optional] [readonly] [default to undefined]
**debitAmount** | **number** |  | [optional] [default to undefined]
**creditAmount** | **number** |  | [optional] [default to undefined]
**debitAmountBook** | **number** |  | [optional] [default to undefined]
**creditAmountBook** | **number** |  | [optional] [default to undefined]
**debitAmountNative** | **number** |  | [optional] [default to undefined]
**creditAmountNative** | **number** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**postedAt** | **string** |  | [optional] [default to undefined]
**merchantName** | **string** |  | [optional] [default to undefined]
**bankDescription** | **string** |  | [optional] [default to undefined]
**note** | **string** |  | [optional] [default to undefined]
**receiptUrl** | **string** |  | [optional] [default to undefined]
**balanceBeforeTransaction** | **number** |  | [optional] [readonly] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**externalId** | **string** |  | [optional] [default to undefined]
**needsReview** | **boolean** |  | [optional] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**draftMatches** | **any** |  | [optional] [default to undefined]
**lastLamPredictionAttempt** | **string** |  | [optional] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**parentBankTransaction** | **number** |  | [optional] [default to undefined]
**vendor** | **number** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**lastModifiedBy** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedChartTransaction } from 'campfire-typescript-sdk';

const instance: PatchedChartTransaction = {
    id,
    isDeleted,
    deletedAt,
    entityName,
    entityCurrency,
    accountName,
    accountNumber,
    vendorName,
    vendorId,
    departmentName,
    parentDepartmentName,
    parentDepartment,
    tags,
    journal,
    journalOrder,
    journalMemo,
    journalType,
    intercompanyJournal,
    createdAutomatically,
    journalAttachments,
    journalTypeName,
    invoice,
    bill,
    dateMonth,
    dateYear,
    balanceAfterTransaction,
    bankAccount,
    bankAccountName,
    account,
    lastModifiedByName,
    accountType,
    accountSubtype,
    parentAccountName,
    files,
    invoiceId,
    invoiceNumber,
    billId,
    billNumber,
    fileNames,
    hasMatches,
    hasAi,
    hasRules,
    hasMerges,
    hasFixedAssetRuleMatches,
    suggestedAccount,
    suggestedAccountName,
    suggestedAccountNumber,
    amount,
    amountNative,
    amountBook,
    amortizationSchedule,
    createdFixedAssets,
    reconciliationReport,
    opposingAccountName,
    opposingAccountNumber,
    taxRate,
    applyBothSides,
    transactionMatchId,
    transactionId,
    debitAmount,
    creditAmount,
    debitAmountBook,
    creditAmountBook,
    debitAmountNative,
    creditAmountNative,
    currency,
    exchangeRate,
    exchangeRateBook,
    postedAt,
    merchantName,
    bankDescription,
    note,
    receiptUrl,
    balanceBeforeTransaction,
    createdAt,
    externalId,
    needsReview,
    lastModifiedAt,
    draftMatches,
    lastLamPredictionAttempt,
    customer,
    entity,
    parentBankTransaction,
    vendor,
    department,
    lastModifiedBy,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

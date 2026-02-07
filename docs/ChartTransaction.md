# ChartTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**entityCurrency** | **string** |  | [readonly] [default to undefined]
**accountName** | **string** | Combines account number and name in the format \&quot;number - name\&quot; | [readonly] [default to undefined]
**accountNumber** | **string** |  | [readonly] [default to undefined]
**vendorName** | **string** |  | [readonly] [default to undefined]
**vendorId** | **string** |  | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**parentDepartmentName** | **string** |  | [readonly] [default to undefined]
**parentDepartment** | **number** |  | [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [readonly] [default to undefined]
**journal** | **number** |  | [readonly] [default to undefined]
**journalOrder** | **string** |  | [readonly] [default to undefined]
**journalMemo** | **string** |  | [readonly] [default to undefined]
**journalType** | **string** |  | [readonly] [default to undefined]
**intercompanyJournal** | **number** |  | [readonly] [default to undefined]
**createdAutomatically** | **boolean** |  | [readonly] [default to undefined]
**journalAttachments** | **Array&lt;any&gt;** |  | [readonly] [default to undefined]
**journalTypeName** | **string** |  | [readonly] [default to undefined]
**invoice** | **string** |  | [readonly] [default to undefined]
**bill** | **string** |  | [readonly] [default to undefined]
**dateMonth** | **string** |  | [readonly] [default to undefined]
**dateYear** | **string** |  | [readonly] [default to undefined]
**balanceAfterTransaction** | **number** |  | [readonly] [default to undefined]
**bankAccount** | **string** |  | [readonly] [default to undefined]
**bankAccountName** | **string** |  | [readonly] [default to undefined]
**account** | **number** |  | [optional] [default to undefined]
**lastModifiedByName** | **string** |  | [readonly] [default to undefined]
**accountType** | **string** |  | [readonly] [default to undefined]
**accountSubtype** | **string** |  | [readonly] [default to undefined]
**parentAccountName** | **string** |  | [readonly] [default to undefined]
**files** | **string** |  | [readonly] [default to undefined]
**invoiceId** | **number** |  | [readonly] [default to undefined]
**invoiceNumber** | **string** |  | [readonly] [default to undefined]
**billId** | **number** |  | [readonly] [default to undefined]
**billNumber** | **string** |  | [readonly] [default to undefined]
**fileNames** | **string** |  | [readonly] [default to undefined]
**hasMatches** | **boolean** |  | [readonly] [default to undefined]
**hasAi** | **boolean** |  | [readonly] [default to undefined]
**hasRules** | **boolean** |  | [readonly] [default to undefined]
**hasMerges** | **boolean** |  | [readonly] [default to undefined]
**hasFixedAssetRuleMatches** | **boolean** |  | [readonly] [default to undefined]
**suggestedAccount** | **number** |  | [readonly] [default to undefined]
**suggestedAccountName** | **string** |  | [readonly] [default to undefined]
**suggestedAccountNumber** | **string** |  | [readonly] [default to undefined]
**amount** | **number** |  | [readonly] [default to undefined]
**amountNative** | **number** |  | [readonly] [default to undefined]
**amountBook** | **number** |  | [readonly] [default to undefined]
**amortizationSchedule** | [**Array&lt;AmortizationSchedule&gt;**](AmortizationSchedule.md) |  | [readonly] [default to undefined]
**createdFixedAssets** | **string** |  | [readonly] [default to undefined]
**reconciliationReport** | **string** |  | [readonly] [default to undefined]
**opposingAccountName** | **string** |  | [readonly] [default to undefined]
**opposingAccountNumber** | **string** |  | [readonly] [default to undefined]
**taxRate** | **number** |  | [optional] [default to undefined]
**applyBothSides** | **boolean** |  | [optional] [default to false]
**transactionMatchId** | **number** |  | [optional] [default to undefined]
**transactionId** | **string** |  | [readonly] [default to undefined]
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
**balanceBeforeTransaction** | **number** |  | [readonly] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**externalId** | **string** |  | [optional] [default to undefined]
**needsReview** | **boolean** |  | [optional] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**draftMatches** | **any** |  | [optional] [default to undefined]
**lastLamPredictionAttempt** | **string** |  | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [default to undefined]
**parentBankTransaction** | **number** |  | [optional] [default to undefined]
**vendor** | **number** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**lastModifiedBy** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { ChartTransaction } from 'campfire-typescript-sdk';

const instance: ChartTransaction = {
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

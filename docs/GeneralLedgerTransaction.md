# GeneralLedgerTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [default to undefined]
**entity** | **number** |  | [default to undefined]
**entityName** | **string** |  | [default to undefined]
**entityCurrency** | **string** |  | [default to undefined]
**accountId** | **number** |  | [default to undefined]
**accountNumber** | **string** |  | [default to undefined]
**accountName** | **string** | Combines account number and name in the format \&quot;number - name\&quot; | [readonly] [default to undefined]
**accountType** | **string** |  | [default to undefined]
**postedAt** | **string** |  | [default to undefined]
**debitAmount** | **number** |  | [default to undefined]
**creditAmount** | **number** |  | [default to undefined]
**debitAmountBook** | **number** |  | [default to undefined]
**creditAmountBook** | **number** |  | [default to undefined]
**debitAmountNative** | **number** |  | [default to undefined]
**creditAmountNative** | **number** |  | [default to undefined]
**balanceBeforeTransaction** | **number** |  | [default to undefined]
**balanceAfterTransaction** | **number** |  | [readonly] [default to undefined]
**balanceAfterTransactionBook** | **number** |  | [readonly] [default to undefined]
**balanceBeforeTransactionNative** | **number** |  | [default to undefined]
**balanceAfterTransactionNative** | **number** |  | [readonly] [default to undefined]
**bankDescription** | **string** |  | [default to undefined]
**journal** | **number** |  | [default to undefined]
**journalOrder** | **string** |  | [default to undefined]
**journalCurrency** | **string** |  | [default to undefined]
**intercompanyJournal** | **number** |  | [default to undefined]
**department** | **number** |  | [default to undefined]
**departmentName** | **string** |  | [default to undefined]
**vendor** | **number** |  | [default to undefined]
**vendorName** | **string** |  | [default to undefined]
**tags** | [**Array&lt;GeneralLedgerTag&gt;**](GeneralLedgerTag.md) |  | [readonly] [default to undefined]
**opposingAccountName** | **string** |  | [default to undefined]
**opposingAccountNumber** | **string** |  | [default to undefined]

## Example

```typescript
import { GeneralLedgerTransaction } from 'campfire-typescript-sdk';

const instance: GeneralLedgerTransaction = {
    id,
    entity,
    entityName,
    entityCurrency,
    accountId,
    accountNumber,
    accountName,
    accountType,
    postedAt,
    debitAmount,
    creditAmount,
    debitAmountBook,
    creditAmountBook,
    debitAmountNative,
    creditAmountNative,
    balanceBeforeTransaction,
    balanceAfterTransaction,
    balanceAfterTransactionBook,
    balanceBeforeTransactionNative,
    balanceAfterTransactionNative,
    bankDescription,
    journal,
    journalOrder,
    journalCurrency,
    intercompanyJournal,
    department,
    departmentName,
    vendor,
    vendorName,
    tags,
    opposingAccountName,
    opposingAccountNumber,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

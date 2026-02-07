# PatchedBankTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**accountName** | **string** |  | [optional] [readonly] [default to undefined]
**dateMonth** | **string** |  | [optional] [readonly] [default to undefined]
**dateYear** | **string** |  | [optional] [readonly] [default to undefined]
**journal** | **number** |  | [optional] [readonly] [default to undefined]
**journalOrder** | **string** |  | [optional] [readonly] [default to undefined]
**intercompanyJournal** | **number** |  | [optional] [readonly] [default to undefined]
**reconciliationReport** | **number** |  | [optional] [readonly] [default to undefined]
**reconciliationReportEndingDate** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**transactionId** | **string** |  | [optional] [default to undefined]
**externalTransactionId** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**amount** | **number** |  | [optional] [default to undefined]
**amountNative** | **number** |  | [optional] [default to undefined]
**postedAt** | **string** |  | [optional] [default to undefined]
**status** | **string** |  | [optional] [default to undefined]
**note** | **string** |  | [optional] [default to undefined]
**bankDescription** | **string** |  | [optional] [default to undefined]
**externalMemo** | **string** |  | [optional] [default to undefined]
**merchantId** | **string** |  | [optional] [default to undefined]
**merchantName** | **string** |  | [optional] [default to undefined]
**merchantNickname** | **string** |  | [optional] [default to undefined]
**kind** | **string** |  | [optional] [default to undefined]
**excluded** | **boolean** |  | [optional] [default to undefined]
**assigned** | **boolean** |  | [optional] [default to undefined]
**metadata** | **any** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**account** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedBankTransaction } from 'campfire-typescript-sdk';

const instance: PatchedBankTransaction = {
    id,
    isDeleted,
    deletedAt,
    accountName,
    dateMonth,
    dateYear,
    journal,
    journalOrder,
    intercompanyJournal,
    reconciliationReport,
    reconciliationReportEndingDate,
    lastModifiedAt,
    transactionId,
    externalTransactionId,
    currency,
    amount,
    amountNative,
    postedAt,
    status,
    note,
    bankDescription,
    externalMemo,
    merchantId,
    merchantName,
    merchantNickname,
    kind,
    excluded,
    assigned,
    metadata,
    createdAt,
    customer,
    account,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

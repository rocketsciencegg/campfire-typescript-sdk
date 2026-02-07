# BankTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**accountName** | **string** |  | [readonly] [default to undefined]
**dateMonth** | **string** |  | [readonly] [default to undefined]
**dateYear** | **string** |  | [readonly] [default to undefined]
**journal** | **number** |  | [readonly] [default to undefined]
**journalOrder** | **string** |  | [readonly] [default to undefined]
**intercompanyJournal** | **number** |  | [readonly] [default to undefined]
**reconciliationReport** | **number** |  | [readonly] [default to undefined]
**reconciliationReportEndingDate** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
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
**createdAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**account** | **number** |  | [default to undefined]

## Example

```typescript
import { BankTransaction } from 'campfire-typescript-sdk';

const instance: BankTransaction = {
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

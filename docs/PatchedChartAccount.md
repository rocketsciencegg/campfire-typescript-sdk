# PatchedChartAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**reconciliationEndingDate** | **string** |  | [optional] [readonly] [default to undefined]
**reconciliationEndingBalance** | **number** |  | [optional] [readonly] [default to undefined]
**balanceYtd** | **number** |  | [optional] [readonly] [default to undefined]
**nameAndNumber** | **string** |  | [optional] [readonly] [default to undefined]
**parentNameAndNumber** | **string** |  | [optional] [readonly] [default to undefined]
**sortKey** | **string** |  | [optional] [readonly] [default to undefined]
**hasAssociatedData** | **boolean** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**accountId** | **string** |  | [optional] [readonly] [default to undefined]
**number** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**name** | **string** |  | [optional] [default to undefined]
**nickname** | **string** |  | [optional] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**status** | [**Status372Enum**](Status372Enum.md) |  | [optional] [default to undefined]
**accountType** | [**AccountTypeEnum**](AccountTypeEnum.md) |  | [optional] [default to undefined]
**accountSubtype** | [**AccountSubtypeEnum**](AccountSubtypeEnum.md) |  | [optional] [default to undefined]
**accountCashflowClassification** | [**AccountCashflowClassificationEnum**](AccountCashflowClassificationEnum.md) |  | [optional] [default to undefined]
**includeInEliminations** | **boolean** |  | [optional] [default to undefined]
**includeInRevaluations** | **boolean** |  | [optional] [default to undefined]
**_protected** | **boolean** |  | [optional] [default to undefined]
**skipSubledgerValidation** | **boolean** | Allow manual journal entries to post to this AR/AP account, bypassing subledger validation | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**lastRecomputeBalanceAt** | **string** |  | [optional] [default to undefined]
**lockRecomputeBalanceKey** | **string** |  | [optional] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**parent** | **number** |  | [optional] [default to undefined]
**parentBankAccount** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedChartAccount } from 'campfire-typescript-sdk';

const instance: PatchedChartAccount = {
    id,
    isDeleted,
    deletedAt,
    reconciliationEndingDate,
    reconciliationEndingBalance,
    balanceYtd,
    nameAndNumber,
    parentNameAndNumber,
    sortKey,
    hasAssociatedData,
    lastModifiedAt,
    accountId,
    number,
    currency,
    name,
    nickname,
    description,
    status,
    accountType,
    accountSubtype,
    accountCashflowClassification,
    includeInEliminations,
    includeInRevaluations,
    _protected,
    skipSubledgerValidation,
    createdAt,
    lastRecomputeBalanceAt,
    lockRecomputeBalanceKey,
    customer,
    parent,
    parentBankAccount,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

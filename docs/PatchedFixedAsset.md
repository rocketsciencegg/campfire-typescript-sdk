# PatchedFixedAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**entityName** | **string** |  | [optional] [readonly] [default to undefined]
**entityCurrency** | **string** |  | [optional] [readonly] [default to undefined]
**usefulLife** | **number** |  | [optional] [readonly] [default to undefined]
**assetClassName** | **string** |  | [optional] [readonly] [default to undefined]
**assetAccount** | **string** |  | [optional] [readonly] [default to undefined]
**assetAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**depreciationExpenseAccount** | **string** |  | [optional] [readonly] [default to undefined]
**depreciationExpenseAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**accumulatedDepreciationAccount** | **string** |  | [optional] [readonly] [default to undefined]
**accumulatedDepreciationAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**purchaseJournalEntryOrder** | **string** |  | [optional] [readonly] [default to undefined]
**purchaseTransactionId** | **string** |  | [optional] [readonly] [default to undefined]
**vendorName** | **string** |  | [optional] [readonly] [default to undefined]
**departmentName** | **string** |  | [optional] [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [optional] [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [optional] [readonly] [default to undefined]
**depreciations** | [**Array&lt;FixedAssetDepreciation&gt;**](FixedAssetDepreciation.md) |  | [optional] [default to undefined]
**depreciationEndDate** | **string** |  | [optional] [readonly] [default to undefined]
**disposals** | [**Array&lt;FixedAssetDisposal&gt;**](FixedAssetDisposal.md) |  | [optional] [readonly] [default to undefined]
**netBookValue** | **string** |  | [optional] [readonly] [default to undefined]
**depreciatedUntil** | **string** |  | [optional] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**name** | **string** |  | [optional] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**initialValue** | **number** |  | [optional] [default to undefined]
**salvageValue** | **number** |  | [optional] [default to undefined]
**purchaseDate** | **string** |  | [optional] [default to undefined]
**depreciationStartDate** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**status** | [**FixedAssetStatusEnum**](FixedAssetStatusEnum.md) |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**assetClass** | **number** |  | [optional] [default to undefined]
**purchaseJournalEntry** | **number** |  | [optional] [default to undefined]
**purchaseTransaction** | **number** |  | [optional] [default to undefined]
**vendor** | **number** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedFixedAsset } from 'campfire-typescript-sdk';

const instance: PatchedFixedAsset = {
    id,
    entityName,
    entityCurrency,
    usefulLife,
    assetClassName,
    assetAccount,
    assetAccountName,
    depreciationExpenseAccount,
    depreciationExpenseAccountName,
    accumulatedDepreciationAccount,
    accumulatedDepreciationAccountName,
    purchaseJournalEntryOrder,
    purchaseTransactionId,
    vendorName,
    departmentName,
    tags,
    attachments,
    depreciations,
    depreciationEndDate,
    disposals,
    netBookValue,
    depreciatedUntil,
    lastModifiedAt,
    isDeleted,
    deletedAt,
    name,
    description,
    currency,
    initialValue,
    salvageValue,
    purchaseDate,
    depreciationStartDate,
    createdAt,
    status,
    exchangeRate,
    exchangeRateBook,
    customer,
    entity,
    assetClass,
    purchaseJournalEntry,
    purchaseTransaction,
    vendor,
    department,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

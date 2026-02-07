# FixedAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**entityCurrency** | **string** |  | [readonly] [default to undefined]
**usefulLife** | **number** |  | [readonly] [default to undefined]
**assetClassName** | **string** |  | [readonly] [default to undefined]
**assetAccount** | **string** |  | [readonly] [default to undefined]
**assetAccountName** | **string** |  | [readonly] [default to undefined]
**depreciationExpenseAccount** | **string** |  | [readonly] [default to undefined]
**depreciationExpenseAccountName** | **string** |  | [readonly] [default to undefined]
**accumulatedDepreciationAccount** | **string** |  | [readonly] [default to undefined]
**accumulatedDepreciationAccountName** | **string** |  | [readonly] [default to undefined]
**purchaseJournalEntryOrder** | **string** |  | [readonly] [default to undefined]
**purchaseTransactionId** | **string** |  | [readonly] [default to undefined]
**vendorName** | **string** |  | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [readonly] [default to undefined]
**depreciations** | [**Array&lt;FixedAssetDepreciation&gt;**](FixedAssetDepreciation.md) |  | [optional] [default to undefined]
**depreciationEndDate** | **string** |  | [readonly] [default to undefined]
**disposals** | [**Array&lt;FixedAssetDisposal&gt;**](FixedAssetDisposal.md) |  | [readonly] [default to undefined]
**netBookValue** | **string** |  | [readonly] [default to undefined]
**depreciatedUntil** | **string** |  | [optional] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**name** | **string** |  | [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**initialValue** | **number** |  | [optional] [default to undefined]
**salvageValue** | **number** |  | [optional] [default to undefined]
**purchaseDate** | **string** |  | [default to undefined]
**depreciationStartDate** | **string** |  | [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**status** | [**FixedAssetStatusEnum**](FixedAssetStatusEnum.md) |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**assetClass** | **number** |  | [optional] [default to undefined]
**purchaseJournalEntry** | **number** |  | [optional] [default to undefined]
**purchaseTransaction** | **number** |  | [optional] [default to undefined]
**vendor** | **number** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { FixedAsset } from 'campfire-typescript-sdk';

const instance: FixedAsset = {
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

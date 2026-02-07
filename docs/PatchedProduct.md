# PatchedProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**departmentName** | **string** |  | [optional] [readonly] [default to undefined]
**invoiceAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**revenueAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**arAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**invoiceUnbilledAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**taxAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**productId** | **string** |  | [optional] [default to undefined]
**productName** | **string** |  | [optional] [default to undefined]
**productDescription** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**price** | **number** |  | [optional] [default to undefined]
**cost** | **number** |  | [optional] [default to undefined]
**excludeFromMrr** | **boolean** |  | [optional] [default to undefined]
**isTaxable** | **boolean** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**stripeProductId** | **string** |  | [optional] [default to undefined]
**avalaraItemId** | **number** |  | [optional] [default to undefined]
**avalaraItemData** | **any** |  | [optional] [default to undefined]
**avalaraTaxCode** | **string** | Avalara tax code (e.g., SW052000 for SAAS) | [optional] [default to undefined]
**anrokItemId** | **string** |  | [optional] [default to undefined]
**sphereItemId** | **string** |  | [optional] [default to undefined]
**applyDeptTagToInvoiceJournals** | **boolean** | Apply Department and Tag categorization to all lines on Invoice Journals | [optional] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**invoiceAccount** | **number** |  | [optional] [default to undefined]
**revenueAccount** | **number** |  | [optional] [default to undefined]
**arAccount** | **number** |  | [optional] [default to undefined]
**invoiceUnbilledAccount** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedProduct } from 'campfire-typescript-sdk';

const instance: PatchedProduct = {
    id,
    isDeleted,
    deletedAt,
    departmentName,
    invoiceAccountName,
    revenueAccountName,
    arAccountName,
    invoiceUnbilledAccountName,
    taxAccountName,
    tags,
    lastModifiedAt,
    productId,
    productName,
    productDescription,
    currency,
    price,
    cost,
    excludeFromMrr,
    isTaxable,
    createdAt,
    stripeProductId,
    avalaraItemId,
    avalaraItemData,
    avalaraTaxCode,
    anrokItemId,
    sphereItemId,
    applyDeptTagToInvoiceJournals,
    customer,
    department,
    invoiceAccount,
    revenueAccount,
    arAccount,
    invoiceUnbilledAccount,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

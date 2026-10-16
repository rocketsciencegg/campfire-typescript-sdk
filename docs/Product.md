# Product


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**invoiceAccountName** | **string** |  | [readonly] [default to undefined]
**revenueAccountName** | **string** |  | [readonly] [default to undefined]
**arAccountName** | **string** |  | [readonly] [default to undefined]
**badDebtAccountName** | **string** |  | [readonly] [default to undefined]
**invoiceUnbilledAccountName** | **string** |  | [readonly] [default to undefined]
**taxAccountName** | **string** |  | [readonly] [default to undefined]
**tags** | **Array&lt;{ [key: string]: any; }&gt;** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**productUuid** | **string** |  | [readonly] [default to undefined]
**displayName** | **string** |  | [readonly] [default to undefined]
**usageGroupCount** | **number** |  | [readonly] [default to 0]
**usageGroups** | [**Array&lt;ProductUsageGroupSummary&gt;**](ProductUsageGroupSummary.md) |  | [readonly] [default to undefined]
**productId** | **string** |  | [optional] [default to undefined]
**productName** | **string** |  | [optional] [default to undefined]
**productDescription** | **string** |  | [optional] [default to undefined]
**tagIds** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**tagGroupIds** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**price** | **number** |  | [optional] [default to undefined]
**usagePriceUnit** | **string** |  | [optional] [default to undefined]
**cost** | **number** |  | [optional] [default to undefined]
**excludeFromMrr** | **boolean** |  | [optional] [default to undefined]
**isTaxable** | **boolean** |  | [optional] [default to undefined]
**isRenewable** | **boolean** |  | [optional] [default to undefined]
**recognizeRevenue** | **boolean** | If False, contract-sync skips the revenue-recognition waterfall for this product (no ContractSubscription / RevenueTransaction rows). | [optional] [default to undefined]
**bundledUsageRevenueRecognitionType** | [**BundledUsageRevenueRecognitionTypeEnum**](BundledUsageRevenueRecognitionTypeEnum.md) | Default subscription revenue recognition when this customer-scoped product is created on a contract with a prepaid usage commitment.  * &#x60;RATABLE&#x60; - Ratable * &#x60;RELATIVE_TO_PREPAID_COMMIT&#x60; - Relative to prepaid commit | [optional] [default to undefined]
**isImmediateRecognition** | **boolean** | When true, revenue for this product is recognized in full on the invoice finalization date instead of being amortized over the service period.  Used by the Stripe accrual JE waterfall. | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**stripeProductId** | **string** |  | [optional] [default to undefined]
**avalaraItemId** | **number** |  | [optional] [default to undefined]
**avalaraItemData** | **any** |  | [optional] [default to undefined]
**avalaraTaxCode** | **string** | Avalara tax code (e.g., SW052000 for SAAS) | [optional] [default to undefined]
**anrokItemId** | **string** |  | [optional] [default to undefined]
**sphereItemId** | **string** |  | [optional] [default to undefined]
**netsuiteItemId** | **string** |  | [optional] [default to undefined]
**applyDeptTagToInvoiceJournals** | **boolean** | Apply Department and Tag categorization to all lines on Invoice Journals | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**invoiceAccount** | **number** |  | [optional] [default to undefined]
**revenueAccount** | **number** |  | [optional] [default to undefined]
**arAccount** | **number** |  | [optional] [default to undefined]
**badDebtAccount** | **number** |  | [optional] [default to undefined]
**invoiceUnbilledAccount** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { Product } from 'campfire-typescript-sdk';

const instance: Product = {
    id,
    isDeleted,
    deletedAt,
    departmentName,
    invoiceAccountName,
    revenueAccountName,
    arAccountName,
    badDebtAccountName,
    invoiceUnbilledAccountName,
    taxAccountName,
    tags,
    lastModifiedAt,
    productUuid,
    displayName,
    usageGroupCount,
    usageGroups,
    productId,
    productName,
    productDescription,
    tagIds,
    tagGroupIds,
    currency,
    price,
    usagePriceUnit,
    cost,
    excludeFromMrr,
    isTaxable,
    isRenewable,
    recognizeRevenue,
    bundledUsageRevenueRecognitionType,
    isImmediateRecognition,
    createdAt,
    stripeProductId,
    avalaraItemId,
    avalaraItemData,
    avalaraTaxCode,
    anrokItemId,
    sphereItemId,
    netsuiteItemId,
    applyDeptTagToInvoiceJournals,
    customer,
    department,
    invoiceAccount,
    revenueAccount,
    arAccount,
    badDebtAccount,
    invoiceUnbilledAccount,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

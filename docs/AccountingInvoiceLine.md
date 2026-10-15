# AccountingInvoiceLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**invoice** | **number** |  | [optional] [default to undefined]
**productName** | **string** |  | [readonly] [default to undefined]
**productBundleName** | **string** |  | [readonly] [default to undefined]
**stripeProductId** | **string** |  | [readonly] [default to undefined]
**productIsTaxable** | **boolean** |  | [readonly] [default to undefined]
**anrokItemId** | **string** |  | [readonly] [default to undefined]
**sphereItemId** | **string** |  | [readonly] [default to undefined]
**serviceDate** | **string** |  | [optional] [default to undefined]
**tags** | **Array&lt;{ [key: string]: any; }&gt;** |  | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**departmentCode** | **string** |  | [readonly] [default to undefined]
**withholdingTaxRateName** | **string** |  | [readonly] [default to undefined]
**withholdingTaxRateValue** | **number** | Sum of the selected withholding rate\&#39;s component rates, for line-level preview. | [readonly] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**chargeType** | [**ChargeTypeEnum**](ChargeTypeEnum.md) | Billing charge classification for generated invoice lines; null when unclassified.  * &#x60;prepaid_commit&#x60; - Prepaid commitment * &#x60;overage&#x60; - Overage | [optional] [default to undefined]
**quantity** | **number** |  | [optional] [default to undefined]
**rate** | **number** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**amount** | **number** |  | [optional] [default to undefined]
**tax** | **number** |  | [optional] [default to undefined]
**taxDescription** | **string** |  | [optional] [default to undefined]
**entityUseCode** | **string** | Avalara entity/use code for line-level tax exemptions | [optional] [default to undefined]
**discount** | **number** | Discount amount in currency | [optional] [default to undefined]
**discountPercentage** | **number** | Discount percentage (0-100) | [optional] [default to undefined]
**discountAmount** | **number** | Discount amount calculated from percentage | [optional] [default to undefined]
**tagIds** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**tagGroupIds** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**product** | **number** |  | [optional] [default to undefined]
**productBundle** | **number** |  | [optional] [default to undefined]
**withholdingTaxRate** | **number** | Marks this line as subject to withholding; used for preview only. Null &#x3D; not subject. | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { AccountingInvoiceLine } from 'campfire-typescript-sdk';

const instance: AccountingInvoiceLine = {
    id,
    invoice,
    productName,
    productBundleName,
    stripeProductId,
    productIsTaxable,
    anrokItemId,
    sphereItemId,
    serviceDate,
    tags,
    departmentName,
    departmentCode,
    withholdingTaxRateName,
    withholdingTaxRateValue,
    description,
    chargeType,
    quantity,
    rate,
    currency,
    amount,
    tax,
    taxDescription,
    entityUseCode,
    discount,
    discountPercentage,
    discountAmount,
    tagIds,
    tagGroupIds,
    createdAt,
    lastModifiedAt,
    customer,
    product,
    productBundle,
    withholdingTaxRate,
    department,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

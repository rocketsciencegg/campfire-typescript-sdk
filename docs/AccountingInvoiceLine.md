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
**description** | **string** |  | [optional] [default to undefined]
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
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**product** | **number** |  | [optional] [default to undefined]
**productBundle** | **number** |  | [optional] [default to undefined]

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
    description,
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
    createdAt,
    lastModifiedAt,
    customer,
    product,
    productBundle,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# PatchedContractSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**lines** | **string** |  | [optional] [readonly] [default to undefined]
**productName** | **string** |  | [optional] [readonly] [default to undefined]
**productBundle** | **string** |  | [optional] [readonly] [default to undefined]
**productBundleName** | **string** |  | [optional] [readonly] [default to undefined]
**contractProductBundle** | [**ContractProductBundleRead**](ContractProductBundleRead.md) |  | [optional] [readonly] [default to undefined]
**totalValue** | **number** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**rate** | **number** |  | [optional] [default to undefined]
**quantity** | **number** |  | [optional] [default to undefined]
**isContractAmendment** | **boolean** |  | [optional] [default to undefined]
**startDate** | **string** |  | [optional] [default to undefined]
**endDate** | **string** |  | [optional] [default to undefined]
**mrr** | **number** |  | [optional] [default to undefined]
**notes** | **string** |  | [optional] [default to undefined]
**useDailyAccounting** | **boolean** |  | [optional] [default to undefined]
**useCatchup** | **boolean** |  | [optional] [default to undefined]
**catchupDate** | **string** |  | [optional] [default to undefined]
**invoiceCalculation** | [**InvoiceCalculationEnum**](InvoiceCalculationEnum.md) | Fixed Rate: rate stays constant, quantity calculated. Fixed Quantity: quantity stays constant (e.g., seats), rate calculated.  * &#x60;FIXED_RATE&#x60; - Fixed Rate * &#x60;FIXED_QUANTITY&#x60; - Fixed Quantity | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**contract** | **number** |  | [optional] [default to undefined]
**product** | **number** |  | [optional] [default to undefined]
**modifiedSubscription** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedContractSubscription } from 'campfire-typescript-sdk';

const instance: PatchedContractSubscription = {
    id,
    isDeleted,
    deletedAt,
    lines,
    productName,
    productBundle,
    productBundleName,
    contractProductBundle,
    totalValue,
    lastModifiedAt,
    rate,
    quantity,
    isContractAmendment,
    startDate,
    endDate,
    mrr,
    notes,
    useDailyAccounting,
    useCatchup,
    catchupDate,
    invoiceCalculation,
    createdAt,
    customer,
    contract,
    product,
    modifiedSubscription,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

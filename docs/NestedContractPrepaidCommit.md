# NestedContractPrepaidCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligibleUsageProducts** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**usagePricing** | [**CommitUsagePricing**](CommitUsagePricing.md) |  | [optional] [default to undefined]
**usagePricingTerms** | [**Array&lt;LifetimePriceEntry&gt;**](LifetimePriceEntry.md) |  | [optional] [default to undefined]
**contractUsageTerm** | **string** |  | [optional] [default to undefined]
**drawdownBasis** | [**DrawdownBasisEnum**](DrawdownBasisEnum.md) |  | [optional] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**product** | **number** |  | [optional] [default to undefined]
**invoiceBasis** | [**InvoiceBasisEnum**](InvoiceBasisEnum.md) |  | [optional] [default to undefined]
**billingCadence** | [**BillingCadence450Enum**](BillingCadence450Enum.md) |  | [optional] [default to undefined]
**billingTiming** | [**BillingTimingEnum**](BillingTimingEnum.md) |  | [optional] [default to undefined]
**firstInvoiceDate** | **string** |  | [optional] [default to undefined]
**billingPaymentTerm** | **number** |  | [optional] [default to undefined]
**name** | **string** |  | [default to undefined]
**description** | **string** |  | [optional] [default to '']
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**totalValue** | **number** |  | [default to undefined]
**discountPercentage** | **number** |  | [optional] [default to 0.0]
**rate** | **number** |  | [optional] [default to undefined]
**quantity** | **number** |  | [optional] [default to undefined]
**unit** | **string** |  | [optional] [default to '']
**startDate** | **string** |  | [default to undefined]
**expirationDate** | **string** |  | [optional] [default to undefined]
**priority** | **number** |  | [optional] [default to 1]
**subledger** | **number** |  | [optional] [default to undefined]
**overageInvoiceCadence** | [**OverageInvoiceCadenceEnum**](OverageInvoiceCadenceEnum.md) |  | [optional] [default to undefined]
**autoSendOverageInvoices** | **boolean** |  | [optional] [default to false]
**overageInvoiceStartMonth** | **string** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**tags** | **Array&lt;number&gt;** |  | [optional] [default to undefined]

## Example

```typescript
import { NestedContractPrepaidCommit } from 'campfire-typescript-sdk';

const instance: NestedContractPrepaidCommit = {
    eligibleUsageProducts,
    usagePricing,
    usagePricingTerms,
    contractUsageTerm,
    drawdownBasis,
    entity,
    product,
    invoiceBasis,
    billingCadence,
    billingTiming,
    firstInvoiceDate,
    billingPaymentTerm,
    name,
    description,
    currency,
    exchangeRate,
    exchangeRateBook,
    totalValue,
    discountPercentage,
    rate,
    quantity,
    unit,
    startDate,
    expirationDate,
    priority,
    subledger,
    overageInvoiceCadence,
    autoSendOverageInvoices,
    overageInvoiceStartMonth,
    department,
    tags,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

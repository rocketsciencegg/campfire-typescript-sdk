# NestedContractPrepaidCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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

# ContractPrepaidCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**contract** | **number** |  | [readonly] [default to undefined]
**invoiceBasis** | [**InvoiceBasisEnum**](InvoiceBasisEnum.md) |  | [optional] [default to undefined]
**billingCadence** | [**BillingCadence450Enum**](BillingCadence450Enum.md) |  | [optional] [default to undefined]
**billingTiming** | [**BillingTimingEnum**](BillingTimingEnum.md) |  | [optional] [default to undefined]
**firstInvoiceDate** | **string** |  | [optional] [default to undefined]
**billingPaymentTerm** | **number** |  | [optional] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**product** | **number** |  | [optional] [default to undefined]
**productName** | **string** |  | [readonly] [default to undefined]
**name** | **string** |  | [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**totalValue** | **number** |  | [default to undefined]
**remainingValue** | **number** |  | [readonly] [default to undefined]
**discountPercentage** | **number** | Discount applied to gross usage (e.g. 20.00 for 20%) | [optional] [default to undefined]
**rate** | **number** | List price per unit. Prepaid usage &#x3D; rate * (1 - discount%). Overage &#x3D; rate (no discount). | [optional] [default to undefined]
**startDate** | **string** |  | [default to undefined]
**expirationDate** | **string** |  | [optional] [default to undefined]
**status** | [**ContractPrepaidCommitStatusEnum**](ContractPrepaidCommitStatusEnum.md) |  | [readonly] [default to undefined]
**priority** | **number** | Drawdown order when multiple commits exist (lower &#x3D; higher priority) | [optional] [default to undefined]
**isInvoiced** | **boolean** |  | [readonly] [default to undefined]
**invoice** | **number** |  | [readonly] [default to undefined]
**subledger** | **number** |  | [optional] [default to undefined]
**overageInvoiceCadence** | [**OverageInvoiceCadenceEnum**](OverageInvoiceCadenceEnum.md) | How often overage/on-demand usage is invoiced  * &#x60;monthly&#x60; - Monthly * &#x60;quarterly&#x60; - Quarterly * &#x60;biannual&#x60; - Bi Annualy * &#x60;annual&#x60; - Annual * &#x60;one_time&#x60; - One Time * &#x60;custom&#x60; - Custom | [optional] [default to undefined]
**autoSendOverageInvoices** | **boolean** | Automatically send overage invoices when generated | [optional] [default to undefined]
**overageInvoiceStartMonth** | **string** | Anchor date for overage billing cycles. Defaults to start_date. | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**tags** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { ContractPrepaidCommit } from 'campfire-typescript-sdk';

const instance: ContractPrepaidCommit = {
    id,
    contract,
    invoiceBasis,
    billingCadence,
    billingTiming,
    firstInvoiceDate,
    billingPaymentTerm,
    entity,
    entityName,
    product,
    productName,
    name,
    description,
    currency,
    exchangeRate,
    exchangeRateBook,
    totalValue,
    remainingValue,
    discountPercentage,
    rate,
    startDate,
    expirationDate,
    status,
    priority,
    isInvoiced,
    invoice,
    subledger,
    overageInvoiceCadence,
    autoSendOverageInvoices,
    overageInvoiceStartMonth,
    department,
    departmentName,
    tags,
    createdAt,
    lastModifiedAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

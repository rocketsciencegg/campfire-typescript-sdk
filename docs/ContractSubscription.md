# ContractSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**lines** | **string** |  | [readonly] [default to undefined]
**productName** | **string** |  | [readonly] [default to undefined]
**productIsRenewable** | **boolean** |  | [readonly] [default to undefined]
**productBundle** | **string** |  | [readonly] [default to undefined]
**productBundleName** | **string** |  | [readonly] [default to undefined]
**contractProductBundle** | [**ContractProductBundleRead**](ContractProductBundleRead.md) |  | [readonly] [default to undefined]
**totalValue** | **number** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**rate** | **number** |  | [optional] [default to undefined]
**quantity** | **number** |  | [optional] [default to undefined]
**renewalBehavior** | [**RenewalBehaviorEnum**](RenewalBehaviorEnum.md) | Controls how this subscription ends. FOLLOW_CONTRACT extends with the evergreen contract\&#39;s rolling end boundary (working_end_date / effective_end_date). FIXED_END keeps an explicit subscription end_date. Default is FIXED_END.  * &#x60;FOLLOW_CONTRACT&#x60; - Follow Contract * &#x60;FIXED_END&#x60; - Fixed End Date | [optional] [default to undefined]
**periodAmount** | **number** | Evergreen-only input amount per billing period (for example 10000.00 for a quarterly period). Provide this to auto-generate lines for evergreen subscriptions. Ignored for non-evergreen writes. | [optional] [default to undefined]
**invoicedAmountMigration** | **number** | Migration-only: total amount already invoiced in a prior system. When provided, marks revenue transactions as migration-invoiced up to this amount. | [optional] [default to undefined]
**countsTowardMrr** | **boolean** |  | [optional] [default to undefined]
**revenueRecognitionType** | [**RevenueRecognitionTypeEnum**](RevenueRecognitionTypeEnum.md) |  | [optional] [default to undefined]
**billingCadence** | [**BillingCadence450Enum**](BillingCadence450Enum.md) |  | [optional] [default to undefined]
**billingTiming** | [**BillingTimingEnum**](BillingTimingEnum.md) |  | [optional] [default to undefined]
**firstInvoiceDate** | **string** |  | [optional] [default to undefined]
**isContractAmendment** | **boolean** |  | [optional] [default to undefined]
**startDate** | **string** |  | [optional] [default to undefined]
**endDate** | **string** |  | [optional] [default to undefined]
**mrr** | **number** |  | [optional] [default to undefined]
**discount** | **number** | Per-unit discount in contract currency. Line amount is Quantity × (Rate − Discount). Null when no discount is configured. | [optional] [default to undefined]
**notes** | **string** |  | [optional] [default to undefined]
**useDailyAccounting** | **boolean** |  | [optional] [default to undefined]
**prorationMethod** | [**ProrationMethodEnum**](ProrationMethodEnum.md) |  | [optional] [default to undefined]
**useCatchup** | **boolean** |  | [optional] [default to undefined]
**catchupDate** | **string** |  | [optional] [default to undefined]
**catchupManuallyOverridden** | **boolean** | True when a user explicitly set use_catchup or catchup_date via the modal. Suppresses automatic reconciliation by integration syncs so the user\&#39;s choice survives. | [optional] [default to undefined]
**invoiceCalculation** | [**InvoiceCalculationEnum**](InvoiceCalculationEnum.md) | Fixed Rate: rate stays constant, quantity calculated. Fixed Quantity: quantity stays constant (e.g., seats), rate calculated.  * &#x60;FIXED_RATE&#x60; - Fixed Rate * &#x60;FIXED_QUANTITY&#x60; - Fixed Quantity | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**source** | [**SourceFc1Enum**](SourceFc1Enum.md) |  | [optional] [default to undefined]
**externalId** | **string** |  | [optional] [default to undefined]
**ratesAreNet** | **boolean** | When True, this subscription\&#39;s rate and waterfall amounts already reflect post-discount (net) pricing. Prevents invoice creation from double-counting discounts via a separate Discount RevenueTransaction. | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**contract** | **number** |  | [default to undefined]
**relativePrepaidCommit** | **number** |  | [optional] [default to undefined]
**billingPaymentTerm** | **number** |  | [optional] [default to undefined]
**product** | **number** |  | [optional] [default to undefined]
**modifiedSubscription** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { ContractSubscription } from 'campfire-typescript-sdk';

const instance: ContractSubscription = {
    id,
    isDeleted,
    deletedAt,
    lines,
    productName,
    productIsRenewable,
    productBundle,
    productBundleName,
    contractProductBundle,
    totalValue,
    lastModifiedAt,
    rate,
    quantity,
    renewalBehavior,
    periodAmount,
    invoicedAmountMigration,
    countsTowardMrr,
    revenueRecognitionType,
    billingCadence,
    billingTiming,
    firstInvoiceDate,
    isContractAmendment,
    startDate,
    endDate,
    mrr,
    discount,
    notes,
    useDailyAccounting,
    prorationMethod,
    useCatchup,
    catchupDate,
    catchupManuallyOverridden,
    invoiceCalculation,
    createdAt,
    source,
    externalId,
    ratesAreNet,
    customer,
    contract,
    relativePrepaidCommit,
    billingPaymentTerm,
    product,
    modifiedSubscription,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

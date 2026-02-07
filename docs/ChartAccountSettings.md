# ChartAccountSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**uncategorizedNameAndNumber** | **string** |  | [readonly] [default to undefined]
**accountsPayableNameAndNumber** | **string** |  | [readonly] [default to undefined]
**accountsReceivableNameAndNumber** | **string** |  | [readonly] [default to undefined]
**deferredRevenueNameAndNumber** | **string** |  | [readonly] [default to undefined]
**accruedRevenueNameAndNumber** | **string** |  | [readonly] [default to undefined]
**unrealizedGainLossNameAndNumber** | **string** |  | [readonly] [default to undefined]
**realizedGainLossNameAndNumber** | **string** |  | [readonly] [default to undefined]
**roundingAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**unappliedCreditsNameAndNumber** | **string** |  | [readonly] [default to undefined]
**unappliedDebitsNameAndNumber** | **string** |  | [readonly] [default to undefined]
**unbilledRevenueNameAndNumber** | **string** |  | [readonly] [default to undefined]
**defaultClearingNameAndNumber** | **string** |  | [readonly] [default to undefined]
**discountAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**refundAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**processingFeesNameAndNumber** | **string** |  | [readonly] [default to undefined]
**deferredProcessingFeesNameAndNumber** | **string** |  | [readonly] [default to undefined]
**taxAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**payoutAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**ctaAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**fixedAssetDisposalNameAndNumber** | **string** |  | [readonly] [default to undefined]
**enableMidMonthConvention** | **boolean** | When enabled, fixed assets placed in service after the threshold day will begin depreciation the following month (full-month depreciation only) | [optional] [default to undefined]
**midMonthThreshold** | **number** | Day of month threshold (0-31). Assets placed in service AFTER this day will start depreciation the following month | [optional] [default to undefined]
**useWholeMonthAccountingForPrepaids** | **boolean** | When enabled, prepaid amortizations will use whole-month accounting (no proration of first/last months) | [optional] [default to undefined]
**splitInvoicePaymentsByLine** | **boolean** | When enabled, invoice payments will be split by line items | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**uncategorized** | **number** |  | [optional] [default to undefined]
**accountsPayable** | **number** |  | [optional] [default to undefined]
**accountsReceivable** | **number** |  | [optional] [default to undefined]
**deferredRevenue** | **number** |  | [optional] [default to undefined]
**accruedRevenue** | **number** |  | [optional] [default to undefined]
**unrealizedGainLoss** | **number** |  | [optional] [default to undefined]
**realizedGainLoss** | **number** |  | [optional] [default to undefined]
**roundingAccount** | **number** |  | [optional] [default to undefined]
**unappliedCredits** | **number** |  | [optional] [default to undefined]
**unappliedDebits** | **number** |  | [optional] [default to undefined]
**unbilledRevenue** | **number** |  | [optional] [default to undefined]
**defaultClearing** | **number** |  | [optional] [default to undefined]
**discountAccount** | **number** |  | [optional] [default to undefined]
**refundAccount** | **number** |  | [optional] [default to undefined]
**processingFees** | **number** |  | [optional] [default to undefined]
**deferredProcessingFees** | **number** |  | [optional] [default to undefined]
**taxAccount** | **number** |  | [optional] [default to undefined]
**payoutAccount** | **number** |  | [optional] [default to undefined]
**ctaAccount** | **number** |  | [optional] [default to undefined]
**fixedAssetDisposal** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { ChartAccountSettings } from 'campfire-typescript-sdk';

const instance: ChartAccountSettings = {
    id,
    uncategorizedNameAndNumber,
    accountsPayableNameAndNumber,
    accountsReceivableNameAndNumber,
    deferredRevenueNameAndNumber,
    accruedRevenueNameAndNumber,
    unrealizedGainLossNameAndNumber,
    realizedGainLossNameAndNumber,
    roundingAccountNameAndNumber,
    unappliedCreditsNameAndNumber,
    unappliedDebitsNameAndNumber,
    unbilledRevenueNameAndNumber,
    defaultClearingNameAndNumber,
    discountAccountNameAndNumber,
    refundAccountNameAndNumber,
    processingFeesNameAndNumber,
    deferredProcessingFeesNameAndNumber,
    taxAccountNameAndNumber,
    payoutAccountNameAndNumber,
    ctaAccountNameAndNumber,
    fixedAssetDisposalNameAndNumber,
    enableMidMonthConvention,
    midMonthThreshold,
    useWholeMonthAccountingForPrepaids,
    splitInvoicePaymentsByLine,
    customer,
    uncategorized,
    accountsPayable,
    accountsReceivable,
    deferredRevenue,
    accruedRevenue,
    unrealizedGainLoss,
    realizedGainLoss,
    roundingAccount,
    unappliedCredits,
    unappliedDebits,
    unbilledRevenue,
    defaultClearing,
    discountAccount,
    refundAccount,
    processingFees,
    deferredProcessingFees,
    taxAccount,
    payoutAccount,
    ctaAccount,
    fixedAssetDisposal,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

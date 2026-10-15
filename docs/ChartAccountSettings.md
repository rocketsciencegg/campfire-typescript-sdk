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
**fallbackRevenueNameAndNumber** | **string** |  | [readonly] [default to undefined]
**defaultClearingNameAndNumber** | **string** |  | [readonly] [default to undefined]
**checkClearingNameAndNumber** | **string** |  | [readonly] [default to undefined]
**cashInTransitNameAndNumber** | **string** |  | [readonly] [default to undefined]
**discountAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**accruedDiscountAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**unbilledDiscountAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**refundAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**processingFeesNameAndNumber** | **string** |  | [readonly] [default to undefined]
**platformFeesNameAndNumber** | **string** |  | [readonly] [default to undefined]
**deferredProcessingFeesNameAndNumber** | **string** |  | [readonly] [default to undefined]
**taxAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**payoutAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**ctaAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**ociTranslationAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**fixedAssetDisposalNameAndNumber** | **string** |  | [readonly] [default to undefined]
**fixedAssetImpairmentLossNameAndNumber** | **string** |  | [readonly] [default to undefined]
**badDebtAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**disputeExpenseAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**disputeReinstatementAccountNameAndNumber** | **string** |  | [readonly] [default to undefined]
**retainedEarningsNameAndNumber** | **string** |  | [readonly] [default to undefined]
**recognizeDiscountsAsContraRevenue** | **boolean** | When enabled, recognized discounts post to the discount account instead of netting into revenue. | [optional] [default to undefined]
**enableMidMonthConvention** | **boolean** | When enabled, fixed assets placed in service after the threshold day will begin depreciation the following month (full-month depreciation only) | [optional] [default to undefined]
**midMonthThreshold** | **number** | Day of month threshold (0-31). Assets placed in service AFTER this day will start depreciation the following month | [optional] [default to undefined]
**useWholeMonthAccountingForPrepaids** | **boolean** | When enabled, prepaid amortizations will use whole-month accounting (no proration of first/last months) | [optional] [default to undefined]
**midMonthThresholdForPrepaids** | **number** | Day of month threshold (1-31), or blank to disable. Whole-month prepaid amortizations starting AFTER this day begin their schedule the following month; the end date is unchanged | [optional] [default to undefined]
**splitInvoicePaymentsByLine** | **boolean** | When enabled, invoice payments will be split by line items | [optional] [default to undefined]
**splitEliminationsByDepartment** | **boolean** | When enabled, elimination entries are broken out by department in addition to account and entity | [optional] [default to undefined]
**foldRetainedEarnings** | **boolean** | When enabled, the Retained Earnings account\&#39;s directly posted balances combine with the calculated retained earnings into a single line on the balance sheet and trial balance. | [optional] [default to undefined]
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
**fallbackRevenue** | **number** | Revenue account for contract obligations whose product carries no revenue account. | [optional] [default to undefined]
**defaultClearing** | **number** |  | [optional] [default to undefined]
**checkClearing** | **number** | Account credited when bills are paid by printed check, until the check clears the bank. Falls back to default_clearing if not set. | [optional] [default to undefined]
**cashInTransit** | **number** | Account holding a currency conversion between the customer\&#39;s own bank accounts, from the date the money leaves until it lands. | [optional] [default to undefined]
**discountAccount** | **number** |  | [optional] [default to undefined]
**accruedDiscountAccount** | **number** |  | [optional] [default to undefined]
**unbilledDiscountAccount** | **number** |  | [optional] [default to undefined]
**refundAccount** | **number** |  | [optional] [default to undefined]
**processingFees** | **number** |  | [optional] [default to undefined]
**platformFees** | **number** | Account for Stripe platform/subscription fees. Falls back to processing_fees if not set. | [optional] [default to undefined]
**deferredProcessingFees** | **number** |  | [optional] [default to undefined]
**taxAccount** | **number** |  | [optional] [default to undefined]
**payoutAccount** | **number** |  | [optional] [default to undefined]
**ctaAccount** | **number** |  | [optional] [default to undefined]
**ociTranslationAccount** | **number** |  | [optional] [default to undefined]
**fixedAssetDisposal** | **number** |  | [optional] [default to undefined]
**fixedAssetImpairmentLoss** | **number** |  | [optional] [default to undefined]
**badDebtAccount** | **number** |  | [optional] [default to undefined]
**disputeExpenseAccount** | **number** | Account for dispute withdrawals (debit) and dispute reinstatement reversals (credit). Falls back to bad_debt_account if not set. | [optional] [default to undefined]
**disputeReinstatementAccount** | **number** | Account credited when a dispute is reinstated (won). Falls back to dispute_expense_account if not set. | [optional] [default to undefined]
**retainedEarnings** | **number** | Equity account that holds a migrated opening Retained Earnings balance. When folding is enabled, its directly posted balances combine with the calculated retained earnings into a single line on reports. | [optional] [default to undefined]

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
    fallbackRevenueNameAndNumber,
    defaultClearingNameAndNumber,
    checkClearingNameAndNumber,
    cashInTransitNameAndNumber,
    discountAccountNameAndNumber,
    accruedDiscountAccountNameAndNumber,
    unbilledDiscountAccountNameAndNumber,
    refundAccountNameAndNumber,
    processingFeesNameAndNumber,
    platformFeesNameAndNumber,
    deferredProcessingFeesNameAndNumber,
    taxAccountNameAndNumber,
    payoutAccountNameAndNumber,
    ctaAccountNameAndNumber,
    ociTranslationAccountNameAndNumber,
    fixedAssetDisposalNameAndNumber,
    fixedAssetImpairmentLossNameAndNumber,
    badDebtAccountNameAndNumber,
    disputeExpenseAccountNameAndNumber,
    disputeReinstatementAccountNameAndNumber,
    retainedEarningsNameAndNumber,
    recognizeDiscountsAsContraRevenue,
    enableMidMonthConvention,
    midMonthThreshold,
    useWholeMonthAccountingForPrepaids,
    midMonthThresholdForPrepaids,
    splitInvoicePaymentsByLine,
    splitEliminationsByDepartment,
    foldRetainedEarnings,
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
    fallbackRevenue,
    defaultClearing,
    checkClearing,
    cashInTransit,
    discountAccount,
    accruedDiscountAccount,
    unbilledDiscountAccount,
    refundAccount,
    processingFees,
    platformFees,
    deferredProcessingFees,
    taxAccount,
    payoutAccount,
    ctaAccount,
    ociTranslationAccount,
    fixedAssetDisposal,
    fixedAssetImpairmentLoss,
    badDebtAccount,
    disputeExpenseAccount,
    disputeReinstatementAccount,
    retainedEarnings,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

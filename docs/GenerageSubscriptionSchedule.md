# GenerageSubscriptionSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**startDate** | **string** | Start date of the subscription period. | [default to undefined]
**endDate** | **string** | End date of the subscription period. Defaults to 1 year from start date if not provided. | [optional] [default to undefined]
**totalValue** | **number** | Total contract value for the subscription period. | [default to undefined]
**mrr** | **number** | Monthly recurring revenue. If not provided, it is calculated from total_value and the subscription period. | [optional] [default to undefined]
**useDailyAccounting** | **boolean** | Whether to use daily (vs monthly) revenue recognition. | [optional] [default to false]
**prorationMethod** | [**ProrationMethodEnum**](ProrationMethodEnum.md) | Proration method. When provided, takes precedence over use_daily_accounting (DAILY↔True, STANDARD/THIRTY_DAY↔False).  * &#x60;standard&#x60; - Standard (actual month length) * &#x60;thirty_day&#x60; - Fixed 30-day month * &#x60;daily&#x60; - Daily | [optional] [default to undefined]
**useCatchup** | **boolean** | Enable catch-up accounting for retroactive amendments. | [optional] [default to false]
**catchupDate** | **string** | Date from which to apply catch-up adjustments. Required if use_catchup is true. | [optional] [default to undefined]
**modifiedSubscription** | **number** | ID of the existing contract subscription being modified. | [optional] [default to undefined]
**doesModifyContractEndDate** | **boolean** | Whether this modification changes the contract end date. | [optional] [default to false]
**applyProspectively** | **boolean** | Apply changes prospectively from catchup_date instead of retroactively. Only valid when use_catchup is true. | [optional] [default to false]
**billingCadence** | [**GenerageSubscriptionScheduleBillingCadenceEnum**](GenerageSubscriptionScheduleBillingCadenceEnum.md) |  | [optional] [default to undefined]
**billingTiming** | [**BillingTimingEnum**](BillingTimingEnum.md) |  | [optional] [default to undefined]
**firstInvoiceDate** | **string** |  | [optional] [default to undefined]
**monthlyBillingPeriodAlignment** | [**MonthlyBillingPeriodAlignmentEnum**](MonthlyBillingPeriodAlignmentEnum.md) | Contract-level monthly service-period alignment used by the billing preview.  * &#x60;anniversary&#x60; - Contract anniversary * &#x60;calendar_month&#x60; - Calendar month | [optional] [default to undefined]
**revenueRecognitionType** | [**RevenueRecognitionTypeEnum**](RevenueRecognitionTypeEnum.md) | Recognition type of the subscription being previewed. RATABLE keeps the monthly recognition schedule and stamps each row with its billing date. Omitted means the preview mirrors the billing installments.  * &#x60;RATABLE&#x60; - Ratable * &#x60;RELATIVE_TO_PREPAID_COMMIT&#x60; - Relative to prepaid commit | [optional] [default to undefined]

## Example

```typescript
import { GenerageSubscriptionSchedule } from 'campfire-typescript-sdk';

const instance: GenerageSubscriptionSchedule = {
    startDate,
    endDate,
    totalValue,
    mrr,
    useDailyAccounting,
    prorationMethod,
    useCatchup,
    catchupDate,
    modifiedSubscription,
    doesModifyContractEndDate,
    applyProspectively,
    billingCadence,
    billingTiming,
    firstInvoiceDate,
    monthlyBillingPeriodAlignment,
    revenueRecognitionType,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

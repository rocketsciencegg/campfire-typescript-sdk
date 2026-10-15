# ContractPrepaidCommitConsumption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**prepaidCommit** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [readonly] [default to undefined]
**periodStart** | **string** |  | [default to undefined]
**periodEnd** | **string** |  | [readonly] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [readonly] [default to undefined]
**grossUsageAmount** | **number** | Pre-discount total from source data | [default to undefined]
**discountAmount** | **number** | gross_usage_amount * discount_percentage / 100 | [readonly] [default to undefined]
**netConsumptionAmount** | **number** | Pool drawdown amount (gross - discount) | [readonly] [default to undefined]
**overageAmount** | **number** | Amount beyond pool at full rate | [readonly] [default to undefined]
**totalEvents** | **number** |  | [optional] [default to undefined]
**balanceBefore** | **number** | Pool balance before this period | [readonly] [default to undefined]
**balanceAfter** | **number** | Pool balance after this period | [readonly] [default to undefined]
**revenueTransaction** | **number** | Recognized revenue for included (prepaid) portion | [readonly] [default to undefined]
**overageRevenueTransaction** | **number** | Recognized revenue for overage portion | [readonly] [default to undefined]
**adjustments** | **Array&lt;{ [key: string]: any; }&gt;** | Return adjustments recorded during this period, grouped by original period with gross/discount/net/overage split. | [readonly] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { ContractPrepaidCommitConsumption } from 'campfire-typescript-sdk';

const instance: ContractPrepaidCommitConsumption = {
    id,
    prepaidCommit,
    entity,
    periodStart,
    periodEnd,
    description,
    currency,
    grossUsageAmount,
    discountAmount,
    netConsumptionAmount,
    overageAmount,
    totalEvents,
    balanceBefore,
    balanceAfter,
    revenueTransaction,
    overageRevenueTransaction,
    adjustments,
    createdAt,
    lastModifiedAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

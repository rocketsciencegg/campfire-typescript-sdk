# PrepaidUsageEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**prepaidCommit** | **number** |  | [readonly] [default to undefined]
**consumption** | **number** |  | [readonly] [default to undefined]
**externalId** | **string** | Source row ID | [optional] [default to undefined]
**eventDate** | **string** | Event date (dt) | [optional] [default to undefined]
**periodMonth** | **string** | First-of-month (dm) | [default to undefined]
**totalRevenueDollars** | **number** |  | [optional] [default to undefined]
**totalEvents** | **number** |  | [optional] [default to undefined]
**data** | **any** | Flexible key-value pairs for customer-specific columns (team_id, product_feature, model_intent, etc.) | [optional] [default to undefined]
**adjustmentDate** | **string** | Date the adjustment was recorded. Null for normal events. | [optional] [default to undefined]
**isAdjustment** | **boolean** |  | [optional] [default to undefined]
**originalPeriodMonth** | **string** | The original period being corrected (only for adjustments) | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { PrepaidUsageEvent } from 'campfire-typescript-sdk';

const instance: PrepaidUsageEvent = {
    id,
    prepaidCommit,
    consumption,
    externalId,
    eventDate,
    periodMonth,
    totalRevenueDollars,
    totalEvents,
    data,
    adjustmentDate,
    isAdjustment,
    originalPeriodMonth,
    createdAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

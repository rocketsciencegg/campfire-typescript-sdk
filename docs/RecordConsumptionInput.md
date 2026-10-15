# RecordConsumptionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periodMonth** | **string** | First day of the consumption month (e.g. 2026-01-01) | [default to undefined]
**grossUsageAmount** | **number** |  | [default to undefined]
**totalEvents** | **number** |  | [optional] [default to 0]
**description** | **string** |  | [optional] [default to '']

## Example

```typescript
import { RecordConsumptionInput } from 'campfire-typescript-sdk';

const instance: RecordConsumptionInput = {
    periodMonth,
    grossUsageAmount,
    totalEvents,
    description,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# AllocationSyncRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**allocation** | **number** |  | [readonly] [default to undefined]
**allocationName** | **string** |  | [readonly] [default to undefined]
**period** | **string** |  | [readonly] [default to undefined]
**entity** | **number** |  | [readonly] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**trigger** | [**TriggerEnum**](TriggerEnum.md) |  | [readonly] [default to undefined]
**causedBy** | **number** |  | [readonly] [default to undefined]
**causedByName** | **string** |  | [readonly] [default to undefined]
**weightsUsed** | **any** |  | [readonly] [default to undefined]
**transactionsUpdated** | **number** |  | [readonly] [default to undefined]
**status** | [**AllocationSyncRunStatusEnum**](AllocationSyncRunStatusEnum.md) |  | [readonly] [default to undefined]
**skipReason** | [**SkipReasonEnum**](SkipReasonEnum.md) |  | [readonly] [default to undefined]
**error** | **string** |  | [readonly] [default to undefined]
**startedAt** | **string** |  | [readonly] [default to undefined]
**finishedAt** | **string** |  | [readonly] [default to undefined]
**journalEntry** | **number** |  | [readonly] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { AllocationSyncRun } from 'campfire-typescript-sdk';

const instance: AllocationSyncRun = {
    id,
    allocation,
    allocationName,
    period,
    entity,
    entityName,
    trigger,
    causedBy,
    causedByName,
    weightsUsed,
    transactionsUpdated,
    status,
    skipReason,
    error,
    startedAt,
    finishedAt,
    journalEntry,
    createdAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

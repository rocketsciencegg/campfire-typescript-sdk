# AsyncTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**name** | **string** |  | [readonly] [default to undefined]
**createdBy** | **number** |  | [readonly] [default to undefined]
**createdByName** | **string** |  | [readonly] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**status** | [**AsyncTaskStatusEnum**](AsyncTaskStatusEnum.md) |  | [readonly] [default to undefined]
**errorMessage** | **string** |  | [readonly] [default to undefined]
**errorType** | **string** | Exception class name | [readonly] [default to undefined]
**retries** | **number** | Number of retry attempts | [readonly] [default to undefined]
**completedAt** | **string** |  | [readonly] [default to undefined]
**startedAt** | **string** | When task execution started | [readonly] [default to undefined]
**celeryTaskId** | **string** | Celery task UUID from self.request.id | [readonly] [default to undefined]
**rootTaskId** | **string** | Root task ID in workflow chain | [readonly] [default to undefined]
**parentTaskId** | **string** | Parent task ID if chained | [readonly] [default to undefined]
**traceId** | **string** | APM distributed trace ID | [readonly] [default to undefined]
**spanId** | **string** | APM span ID | [readonly] [default to undefined]
**taskArgs** | **any** | Task positional arguments | [readonly] [default to undefined]
**taskKwargs** | **any** | Task keyword arguments | [readonly] [default to undefined]
**result** | **any** | Task execution result | [readonly] [default to undefined]
**content** | **any** |  | [readonly] [default to undefined]

## Example

```typescript
import { AsyncTask } from 'campfire-typescript-sdk';

const instance: AsyncTask = {
    id,
    customer,
    name,
    createdBy,
    createdByName,
    createdAt,
    status,
    errorMessage,
    errorType,
    retries,
    completedAt,
    startedAt,
    celeryTaskId,
    rootTaskId,
    parentTaskId,
    traceId,
    spanId,
    taskArgs,
    taskKwargs,
    result,
    content,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

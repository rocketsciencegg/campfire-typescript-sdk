# AsyncTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**createdByName** | **string** |  | [readonly] [default to undefined]
**name** | **string** |  | [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**status** | [**AsyncTaskStatusEnum**](AsyncTaskStatusEnum.md) |  | [optional] [default to undefined]
**errorMessage** | **string** |  | [optional] [default to undefined]
**errorType** | **string** | Exception class name | [optional] [default to undefined]
**retries** | **number** | Number of retry attempts | [optional] [default to undefined]
**completedAt** | **string** |  | [optional] [default to undefined]
**startedAt** | **string** | When task execution started | [optional] [default to undefined]
**celeryTaskId** | **string** | Celery task UUID from self.request.id | [optional] [default to undefined]
**rootTaskId** | **string** | Root task ID in workflow chain | [optional] [default to undefined]
**parentTaskId** | **string** | Parent task ID if chained | [optional] [default to undefined]
**traceId** | **string** | APM distributed trace ID | [optional] [default to undefined]
**spanId** | **string** | APM span ID | [optional] [default to undefined]
**taskArgs** | **any** | Task positional arguments | [optional] [default to undefined]
**taskKwargs** | **any** | Task keyword arguments | [optional] [default to undefined]
**result** | **any** | Task execution result | [optional] [default to undefined]
**content** | **any** |  | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**createdBy** | **number** |  | [readonly] [default to undefined]

## Example

```typescript
import { AsyncTask } from 'campfire-typescript-sdk';

const instance: AsyncTask = {
    id,
    createdByName,
    name,
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
    customer,
    createdBy,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

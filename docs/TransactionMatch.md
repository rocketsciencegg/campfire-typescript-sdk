# TransactionMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**matchedObject** | **string** |  | [readonly] [default to undefined]
**appLabel** | **string** |  | [readonly] [default to undefined]
**model** | **string** |  | [readonly] [default to undefined]
**drafts** | **string** |  | [readonly] [default to undefined]
**objectId** | **number** |  | [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**reviewedAt** | **string** |  | [optional] [default to undefined]
**status** | [**TransactionMatchStatusEnum**](TransactionMatchStatusEnum.md) |  | [optional] [default to undefined]
**customer** | **number** |  | [default to undefined]
**transaction** | **number** |  | [default to undefined]
**contentType** | **number** |  | [default to undefined]
**reviewedBy** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { TransactionMatch } from 'campfire-typescript-sdk';

const instance: TransactionMatch = {
    id,
    matchedObject,
    appLabel,
    model,
    drafts,
    objectId,
    createdAt,
    reviewedAt,
    status,
    customer,
    transaction,
    contentType,
    reviewedBy,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

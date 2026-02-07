# PatchedTransactionMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**matchedObject** | **string** |  | [optional] [readonly] [default to undefined]
**appLabel** | **string** |  | [optional] [readonly] [default to undefined]
**model** | **string** |  | [optional] [readonly] [default to undefined]
**drafts** | **string** |  | [optional] [readonly] [default to undefined]
**objectId** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**reviewedAt** | **string** |  | [optional] [default to undefined]
**status** | [**TransactionMatchStatusEnum**](TransactionMatchStatusEnum.md) |  | [optional] [default to undefined]
**customer** | **number** |  | [optional] [default to undefined]
**transaction** | **number** |  | [optional] [default to undefined]
**contentType** | **number** |  | [optional] [default to undefined]
**reviewedBy** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedTransactionMatch } from 'campfire-typescript-sdk';

const instance: PatchedTransactionMatch = {
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

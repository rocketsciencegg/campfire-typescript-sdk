# AuditLogEntrySchema

The published shape of an audit entry, for the API docs; AuditLogEntrySerializer produces it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [default to undefined]
**operation** | **string** | Raw operation, such as add, change or delete. Open set. | [default to undefined]
**model** | **string** | Object type as app_label.model. Open set. | [default to undefined]
**objectId** | **number** |  | [default to undefined]
**parentModel** | **string** |  | [default to undefined]
**parentObjectId** | **number** |  | [default to undefined]
**parentDraftQueue** | **number** | The audit entry this row was written as part of. | [default to undefined]
**createdBy** | **number** |  | [default to undefined]
**createdByName** | **string** |  | [default to undefined]
**createdAt** | **string** |  | [default to undefined]
**approvedBy** | **number** | User who gave final approval. | [default to undefined]
**approvedByName** | **string** |  | [default to undefined]
**approvedAt** | **string** |  | [default to undefined]
**notes** | **string** |  | [default to undefined]
**reason** | **string** |  | [default to undefined]
**oldPayload** | **any** |  | [default to undefined]
**newPayload** | **any** |  | [default to undefined]
**workflowName** | **string** |  | [default to undefined]
**approvers** | **Array&lt;{ [key: string]: any; }&gt;** | Each workflow step; [] when the row had no workflow. | [default to undefined]

## Example

```typescript
import { AuditLogEntrySchema } from 'campfire-typescript-sdk';

const instance: AuditLogEntrySchema = {
    id,
    operation,
    model,
    objectId,
    parentModel,
    parentObjectId,
    parentDraftQueue,
    createdBy,
    createdByName,
    createdAt,
    approvedBy,
    approvedByName,
    approvedAt,
    notes,
    reason,
    oldPayload,
    newPayload,
    workflowName,
    approvers,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

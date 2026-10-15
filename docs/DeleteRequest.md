# DeleteRequest

Body of a ``POST …/delete`` request. Also documents that body in the API schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **string** | Why the record is being deleted. Saved to the audit log. | [optional] [default to undefined]

## Example

```typescript
import { DeleteRequest } from 'campfire-typescript-sdk';

const instance: DeleteRequest = {
    reason,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

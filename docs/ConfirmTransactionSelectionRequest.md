# ConfirmTransactionSelectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected** | **Array&lt;number&gt;** | List of GL transaction IDs to mark as reconciled | [default to undefined]
**selectedStatements** | **Array&lt;number&gt;** | Statement transaction IDs to auto-match to GL selections by amount | [optional] [default to undefined]

## Example

```typescript
import { ConfirmTransactionSelectionRequest } from 'campfire-typescript-sdk';

const instance: ConfirmTransactionSelectionRequest = {
    selected,
    selectedStatements,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

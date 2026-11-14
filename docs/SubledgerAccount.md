# SubledgerAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**nameAndNumber** | **string** |  | [readonly] [default to undefined]
**accountType** | **string** |  | [readonly] [default to undefined]
**accountSubtype** | **string** |  | [readonly] [default to undefined]
**roles** | **Array&lt;string&gt;** |  | [readonly] [default to undefined]
**manualEntryBlockedReason** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { SubledgerAccount } from 'campfire-typescript-sdk';

const instance: SubledgerAccount = {
    id,
    nameAndNumber,
    accountType,
    accountSubtype,
    roles,
    manualEntryBlockedReason,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

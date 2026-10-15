# GeneralLedgerTag

Schema shape for a resolved transaction tag on a general-ledger row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  | [default to undefined]
**name** | **string** |  | [default to undefined]
**group** | **string** | Tag group (dimension) ID | [default to undefined]
**groupName** | **string** | Tag group (dimension) name | [default to undefined]
**parent** | **string** |  | [default to undefined]
**parentName** | **string** |  | [default to undefined]
**createdAt** | **string** |  | [default to undefined]
**lastModifiedAt** | **string** |  | [default to undefined]

## Example

```typescript
import { GeneralLedgerTag } from 'campfire-typescript-sdk';

const instance: GeneralLedgerTag = {
    id,
    name,
    group,
    groupName,
    parent,
    parentName,
    createdAt,
    lastModifiedAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

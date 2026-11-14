# GeneralLedgerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**Array&lt;GeneralLedgerTransaction&gt;**](GeneralLedgerTransaction.md) |  | [default to undefined]
**count** | **number** |  | [default to undefined]
**hasNext** | **boolean** |  | [default to undefined]
**currentPage** | **number** |  | [default to undefined]
**totalPages** | **number** |  | [default to undefined]
**basis** | **{ [key: string]: any; }** |  | [optional] [default to undefined]
**activityBasis** | **string** |  | [optional] [default to undefined]
**translationNote** | **string** |  | [optional] [default to undefined]
**translationWarnings** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**translationUnresolved** | **Array&lt;{ [key: string]: any; }&gt;** |  | [optional] [default to undefined]

## Example

```typescript
import { GeneralLedgerResponse } from 'campfire-typescript-sdk';

const instance: GeneralLedgerResponse = {
    results,
    count,
    hasNext,
    currentPage,
    totalPages,
    basis,
    activityBasis,
    translationNote,
    translationWarnings,
    translationUnresolved,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# AmortizationSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**accountingAmortization** | **number** |  | [optional] [default to undefined]
**journalEntryOrder** | **string** |  | [readonly] [default to undefined]
**date** | **string** |  | [default to undefined]
**amount** | **number** |  | [default to undefined]
**posted** | **boolean** |  | [optional] [default to undefined]
**amortization** | **number** |  | [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**transaction** | **number** |  | [optional] [default to undefined]
**billLine** | **number** |  | [optional] [default to undefined]
**journalEntry** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { AmortizationSchedule } from 'campfire-typescript-sdk';

const instance: AmortizationSchedule = {
    id,
    accountingAmortization,
    journalEntryOrder,
    date,
    amount,
    posted,
    amortization,
    customer,
    transaction,
    billLine,
    journalEntry,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

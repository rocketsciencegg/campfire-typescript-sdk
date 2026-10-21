# TrialBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trialBalance** | [**TrialBalanceData**](TrialBalanceData.md) |  | [default to undefined]
**startDate** | **string** |  | [default to undefined]
**endDate** | **string** |  | [default to undefined]
**incomeStatementStart** | **string** |  | [default to undefined]
**breakdown** | **{ [key: string]: any; }** |  | [optional] [default to undefined]
**basis** | **{ [key: string]: any; }** |  | [default to undefined]
**activityBasis** | **string** |  | [default to undefined]
**translationWarnings** | **Array&lt;string&gt;** |  | [optional] [default to undefined]
**translationUnresolved** | **Array&lt;{ [key: string]: any; }&gt;** |  | [optional] [default to undefined]

## Example

```typescript
import { TrialBalanceResponse } from 'campfire-typescript-sdk';

const instance: TrialBalanceResponse = {
    trialBalance,
    startDate,
    endDate,
    incomeStatementStart,
    breakdown,
    basis,
    activityBasis,
    translationWarnings,
    translationUnresolved,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

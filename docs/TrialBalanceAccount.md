# TrialBalanceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  | [default to undefined]
**name** | **string** |  | [default to undefined]
**number** | **string** |  | [default to undefined]
**accountType** | **string** |  | [optional] [default to undefined]
**balances** | [**TrialBalanceAccountBalance**](TrialBalanceAccountBalance.md) |  | [optional] [default to undefined]
**beginningBalances** | [**TrialBalanceAccountBalance**](TrialBalanceAccountBalance.md) |  | [optional] [default to undefined]
**activity** | [**TrialBalanceAccountBalance**](TrialBalanceAccountBalance.md) |  | [optional] [default to undefined]
**endingBalances** | [**TrialBalanceAccountBalance**](TrialBalanceAccountBalance.md) |  | [optional] [default to undefined]
**netMovement** | **number** |  | [optional] [default to undefined]
**drilldownDisabled** | **boolean** |  | [optional] [default to undefined]
**translationUnresolved** | **boolean** |  | [optional] [default to undefined]
**departments** | **{ [key: string]: any; }** |  | [optional] [default to undefined]
**department** | **string** |  | [optional] [default to undefined]
**entities** | **{ [key: string]: any; }** |  | [optional] [default to undefined]
**parent** | **string** |  | [optional] [default to undefined]

## Example

```typescript
import { TrialBalanceAccount } from 'campfire-typescript-sdk';

const instance: TrialBalanceAccount = {
    id,
    name,
    number,
    accountType,
    balances,
    beginningBalances,
    activity,
    endingBalances,
    netMovement,
    drilldownDisabled,
    translationUnresolved,
    departments,
    department,
    entities,
    parent,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

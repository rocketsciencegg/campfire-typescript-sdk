# TrialBalanceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** |  | [default to undefined]
**name** | **string** |  | [default to undefined]
**number** | **string** |  | [default to undefined]
**accountType** | **string** |  | [optional] [default to undefined]
**balances** | [**TrialBalanceAccountBalance**](TrialBalanceAccountBalance.md) |  | [optional] [default to undefined]
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
    departments,
    department,
    entities,
    parent,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

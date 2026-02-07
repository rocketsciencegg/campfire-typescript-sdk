# AccountingDebitMemoLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**debitMemo** | **number** |  | [optional] [default to undefined]
**accountNumber** | **string** |  | [readonly] [default to undefined]
**accountName** | **string** | Combines account number and name in the format \&quot;number - name\&quot; | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [readonly] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**amount** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**account** | **number** |  | [default to undefined]
**department** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { AccountingDebitMemoLine } from 'campfire-typescript-sdk';

const instance: AccountingDebitMemoLine = {
    id,
    debitMemo,
    accountNumber,
    accountName,
    departmentName,
    tags,
    description,
    amount,
    createdAt,
    lastModifiedAt,
    customer,
    account,
    department,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

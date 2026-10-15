# AccountingDebitMemoLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**debitMemo** | **number** |  | [optional] [default to undefined]
**accountNumber** | **string** |  | [readonly] [default to undefined]
**accountName** | **string** | Combines account number and name in the format \&quot;number - name\&quot; | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**tags** | **Array&lt;{ [key: string]: any; }&gt;** |  | [readonly] [default to undefined]
**taxRateName** | **string** |  | [readonly] [default to undefined]
**taxRateValue** | **number** |  | [readonly] [default to undefined]
**amortizationSchedule** | [**Array&lt;AmortizationSchedule&gt;**](AmortizationSchedule.md) |  | [readonly] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**amount** | **number** |  | [optional] [default to undefined]
**tax** | **number** |  | [optional] [default to undefined]
**taxDescription** | **string** |  | [optional] [default to undefined]
**tagIds** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**tagGroupIds** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**account** | **number** |  | [default to undefined]
**taxRate** | **number** |  | [optional] [default to undefined]
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
    taxRateName,
    taxRateValue,
    amortizationSchedule,
    description,
    amount,
    tax,
    taxDescription,
    tagIds,
    tagGroupIds,
    createdAt,
    lastModifiedAt,
    customer,
    account,
    taxRate,
    department,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

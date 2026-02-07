# CostAllocationLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**allocation** | **number** |  | [optional] [default to undefined]
**accountName** | **string** | Combines account number and name in the format \&quot;number - name\&quot; | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [readonly] [default to undefined]
**percentage** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**account** | **number** |  | [default to undefined]
**department** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { CostAllocationLine } from 'campfire-typescript-sdk';

const instance: CostAllocationLine = {
    id,
    allocation,
    accountName,
    departmentName,
    tags,
    percentage,
    createdAt,
    lastModifiedAt,
    customer,
    account,
    department,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

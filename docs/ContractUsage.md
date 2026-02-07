# ContractUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**contract** | **number** |  | [default to undefined]
**product** | **number** |  | [optional] [default to undefined]
**productBundle** | **string** |  | [readonly] [default to undefined]
**contractProductBundle** | [**ContractProductBundleRead**](ContractProductBundleRead.md) |  | [readonly] [default to undefined]
**productName** | **string** |  | [readonly] [default to undefined]
**productBundleName** | **string** |  | [readonly] [default to undefined]
**usageGroup** | **number** |  | [optional] [default to undefined]
**usageGroupName** | **string** |  | [readonly] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**tags** | **string** |  | [optional] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**startDate** | **string** |  | [optional] [default to undefined]
**endDate** | **string** |  | [optional] [default to undefined]
**lines** | **string** |  | [readonly] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { ContractUsage } from 'campfire-typescript-sdk';

const instance: ContractUsage = {
    id,
    contract,
    product,
    productBundle,
    contractProductBundle,
    productName,
    productBundleName,
    usageGroup,
    usageGroupName,
    department,
    tags,
    description,
    startDate,
    endDate,
    lines,
    createdAt,
    lastModifiedAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

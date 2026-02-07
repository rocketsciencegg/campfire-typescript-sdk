# ContractBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**lines** | [**Array&lt;ContractBundleLine&gt;**](ContractBundleLine.md) |  | [default to undefined]
**bundleName** | **string** |  | [default to undefined]
**bundleDescription** | **string** |  | [optional] [default to undefined]
**startDate** | **string** |  | [default to undefined]
**endDate** | **string** |  | [default to undefined]
**useDailyAccounting** | **boolean** |  | [optional] [default to undefined]
**useCatchup** | **boolean** |  | [optional] [default to undefined]
**catchupDate** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**contract** | **number** |  | [default to undefined]

## Example

```typescript
import { ContractBundle } from 'campfire-typescript-sdk';

const instance: ContractBundle = {
    id,
    isDeleted,
    deletedAt,
    lines,
    bundleName,
    bundleDescription,
    startDate,
    endDate,
    useDailyAccounting,
    useCatchup,
    catchupDate,
    createdAt,
    lastModifiedAt,
    customer,
    contract,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# PatchedContractBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**lines** | [**Array&lt;ContractBundleLine&gt;**](ContractBundleLine.md) |  | [optional] [default to undefined]
**bundleName** | **string** |  | [optional] [default to undefined]
**bundleDescription** | **string** |  | [optional] [default to undefined]
**startDate** | **string** |  | [optional] [default to undefined]
**endDate** | **string** |  | [optional] [default to undefined]
**useDailyAccounting** | **boolean** |  | [optional] [default to undefined]
**useCatchup** | **boolean** |  | [optional] [default to undefined]
**catchupDate** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**contract** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedContractBundle } from 'campfire-typescript-sdk';

const instance: PatchedContractBundle = {
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

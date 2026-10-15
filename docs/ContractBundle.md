# ContractBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**endDate** | **string** | Bundle end date. Required for standard contracts. For evergreen contracts this may be null to follow the contract timeline, or set to a billing-period end date. | [optional] [default to undefined]
**rebalanceJournalEntriesIndefinitely** | **boolean** | Should only be used for Evergreen contracts. When true, linked invoice journal entries are rebalanced on each evergreen contract extension. | [optional] [default to false]
**lines** | [**Array&lt;ContractBundleLine&gt;**](ContractBundleLine.md) |  | [default to undefined]
**bundleName** | **string** |  | [default to undefined]
**bundleDescription** | **string** |  | [optional] [default to undefined]
**startDate** | **string** |  | [default to undefined]
**useDailyAccounting** | **boolean** |  | [optional] [default to undefined]
**prorationMethod** | [**ProrationMethodEnum**](ProrationMethodEnum.md) |  | [optional] [default to undefined]
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
    endDate,
    rebalanceJournalEntriesIndefinitely,
    lines,
    bundleName,
    bundleDescription,
    startDate,
    useDailyAccounting,
    prorationMethod,
    useCatchup,
    catchupDate,
    createdAt,
    lastModifiedAt,
    customer,
    contract,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

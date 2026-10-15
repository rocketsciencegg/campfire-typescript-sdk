# TierPriceOverride


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**tier** | **number** |  | [default to undefined]
**tierName** | **string** |  | [readonly] [default to undefined]
**contract** | **number** |  | [default to undefined]
**dealName** | **string** |  | [readonly] [default to undefined]
**usageGroupId** | **number** |  | [readonly] [default to undefined]
**usageGroupName** | **string** |  | [readonly] [default to undefined]
**price** | **number** | Override price per unit for this contract+tier | [optional] [default to undefined]
**percentage** | **number** | Override percentage for this contract+tier (percentage-based pricing) | [optional] [default to undefined]
**source** | [**TierPriceOverrideSourceEnum**](TierPriceOverrideSourceEnum.md) |  | [optional] [default to undefined]
**integrationName** | **string** |  | [optional] [default to undefined]
**externalReference** | **string** |  | [optional] [default to undefined]
**notes** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { TierPriceOverride } from 'campfire-typescript-sdk';

const instance: TierPriceOverride = {
    id,
    tier,
    tierName,
    contract,
    dealName,
    usageGroupId,
    usageGroupName,
    price,
    percentage,
    source,
    integrationName,
    externalReference,
    notes,
    createdAt,
    lastModifiedAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

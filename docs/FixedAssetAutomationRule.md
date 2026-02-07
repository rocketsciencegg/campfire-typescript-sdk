# FixedAssetAutomationRule

Serializer for automation rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**name** | **string** | Descriptive name for this rule | [default to undefined]
**entity** | **number** | Entity this rule applies to (determines book currency) | [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**currency** | **string** | Book currency from entity (auto-populated) | [readonly] [default to undefined]
**account** | **number** | Create assets when transactions are posted to this account | [default to undefined]
**accountName** | **string** |  | [readonly] [default to undefined]
**accountNumber** | **string** |  | [readonly] [default to undefined]
**amountThreshold** | **number** | Minimum transaction amount in book currency (materiality threshold) | [default to undefined]
**assetClass** | **number** | Asset class to use for created assets | [default to undefined]
**assetClassName** | **string** |  | [readonly] [default to undefined]
**needsReview** | **boolean** | If true, queue assets for review before creation | [optional] [default to undefined]
**forwardLooking** | **boolean** | Only apply to transactions created after this rule | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { FixedAssetAutomationRule } from 'campfire-typescript-sdk';

const instance: FixedAssetAutomationRule = {
    id,
    name,
    entity,
    entityName,
    currency,
    account,
    accountName,
    accountNumber,
    amountThreshold,
    assetClass,
    assetClassName,
    needsReview,
    forwardLooking,
    createdAt,
    lastModifiedAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

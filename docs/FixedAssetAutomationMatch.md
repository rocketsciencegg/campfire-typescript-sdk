# FixedAssetAutomationMatch

Serializer for pending asset matches in review queue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**rule** | **number** |  | [default to undefined]
**ruleName** | **string** |  | [readonly] [default to undefined]
**ruleAccountName** | **string** |  | [readonly] [default to undefined]
**ruleThreshold** | **number** |  | [readonly] [default to undefined]
**ruleNeedsReview** | **boolean** |  | [readonly] [default to undefined]
**transaction** | **number** |  | [readonly] [default to undefined]
**transactionDescription** | **string** |  | [readonly] [default to undefined]
**transactionDate** | **string** |  | [readonly] [default to undefined]
**transactionAmount** | **string** |  | [readonly] [default to undefined]
**proposedName** | **string** |  | [default to undefined]
**proposedAssetClass** | **number** |  | [default to undefined]
**proposedInitialValue** | **number** |  | [default to undefined]
**proposedSalvageValue** | **number** |  | [optional] [default to undefined]
**proposedPurchaseDate** | **string** |  | [default to undefined]
**proposedDepreciationStartDate** | **string** |  | [default to undefined]
**proposedEntity** | **number** |  | [optional] [default to undefined]
**proposedDepartment** | **number** |  | [optional] [default to undefined]
**proposedVendor** | **number** |  | [optional] [default to undefined]
**createdAsset** | **number** | The asset created when this match was accepted | [readonly] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { FixedAssetAutomationMatch } from 'campfire-typescript-sdk';

const instance: FixedAssetAutomationMatch = {
    id,
    rule,
    ruleName,
    ruleAccountName,
    ruleThreshold,
    ruleNeedsReview,
    transaction,
    transactionDescription,
    transactionDate,
    transactionAmount,
    proposedName,
    proposedAssetClass,
    proposedInitialValue,
    proposedSalvageValue,
    proposedPurchaseDate,
    proposedDepreciationStartDate,
    proposedEntity,
    proposedDepartment,
    proposedVendor,
    createdAsset,
    createdAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# PatchedFixedAssetAutomationMatch

Serializer for pending asset matches in review queue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**rule** | **number** |  | [optional] [default to undefined]
**ruleName** | **string** |  | [optional] [readonly] [default to undefined]
**ruleAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**ruleThreshold** | **number** |  | [optional] [readonly] [default to undefined]
**ruleNeedsReview** | **boolean** |  | [optional] [readonly] [default to undefined]
**transaction** | **number** |  | [optional] [readonly] [default to undefined]
**transactionDescription** | **string** |  | [optional] [readonly] [default to undefined]
**transactionDate** | **string** |  | [optional] [readonly] [default to undefined]
**transactionAmount** | **string** |  | [optional] [readonly] [default to undefined]
**proposedName** | **string** |  | [optional] [default to undefined]
**proposedAssetClass** | **number** |  | [optional] [default to undefined]
**proposedInitialValue** | **number** |  | [optional] [default to undefined]
**proposedSalvageValue** | **number** |  | [optional] [default to undefined]
**proposedPurchaseDate** | **string** |  | [optional] [default to undefined]
**proposedDepreciationStartDate** | **string** |  | [optional] [default to undefined]
**proposedEntity** | **number** |  | [optional] [default to undefined]
**proposedDepartment** | **number** |  | [optional] [default to undefined]
**proposedVendor** | **number** |  | [optional] [default to undefined]
**createdAsset** | **number** | The asset created when this match was accepted | [optional] [readonly] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]

## Example

```typescript
import { PatchedFixedAssetAutomationMatch } from 'campfire-typescript-sdk';

const instance: PatchedFixedAssetAutomationMatch = {
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

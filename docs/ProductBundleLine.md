# ProductBundleLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**product** | **number** |  | [default to undefined]
**productName** | **string** |  | [readonly] [default to undefined]
**productIdStr** | **string** |  | [readonly] [default to undefined]
**percentageAllocation** | **number** |  | [default to undefined]
**componentType** | [**ComponentTypeEnum**](ComponentTypeEnum.md) | Component type for this line in a mixed-type bundle. NULL &#x3D; legacy single-type bundle (type inherited from the referencing ContractSubscription/Milestone/Usage).  * &#x60;SUBSCRIPTION&#x60; - Subscription * &#x60;MILESTONE&#x60; - Milestone * &#x60;USAGE&#x60; - Usage | [optional] [default to undefined]

## Example

```typescript
import { ProductBundleLine } from 'campfire-typescript-sdk';

const instance: ProductBundleLine = {
    id,
    product,
    productName,
    productIdStr,
    percentageAllocation,
    componentType,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

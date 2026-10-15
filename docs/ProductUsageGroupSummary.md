# ProductUsageGroupSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**name** | **string** |  | [optional] [default to undefined]
**pricingModel** | [**PricingModelEnum**](PricingModelEnum.md) |  | [optional] [default to undefined]
**unitOfMeasure** | **string** |  | [optional] [default to undefined]
**tierCount** | **number** |  | [readonly] [default to 0]
**tiers** | [**Array&lt;ProductUsageTierSummary&gt;**](ProductUsageTierSummary.md) |  | [readonly] [default to undefined]

## Example

```typescript
import { ProductUsageGroupSummary } from 'campfire-typescript-sdk';

const instance: ProductUsageGroupSummary = {
    id,
    name,
    pricingModel,
    unitOfMeasure,
    tierCount,
    tiers,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

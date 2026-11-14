# CommitUsagePricing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usageProduct** | **string** |  | [default to undefined]
**priceSource** | [**CommitUsagePricingPriceSourceEnum**](CommitUsagePricingPriceSourceEnum.md) |  | [default to undefined]
**expectedRate** | **number** |  | [default to undefined]
**expectedUnit** | **string** |  | [default to undefined]
**expectedCurrency** | **string** |  | [default to undefined]
**confirmPrice** | **boolean** |  | [default to undefined]
**confirmHistoricalPrice** | **boolean** |  | [optional] [default to false]

## Example

```typescript
import { CommitUsagePricing } from 'campfire-typescript-sdk';

const instance: CommitUsagePricing = {
    usageProduct,
    priceSource,
    expectedRate,
    expectedUnit,
    expectedCurrency,
    confirmPrice,
    confirmHistoricalPrice,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

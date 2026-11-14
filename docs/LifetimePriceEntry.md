# LifetimePriceEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usageProduct** | **string** |  | [default to undefined]
**priceSource** | [**LifetimePriceEntryPriceSourceEnum**](LifetimePriceEntryPriceSourceEnum.md) |  | [default to undefined]
**rateCard** | **number** |  | [optional] [default to undefined]
**schedule** | **{ [key: string]: any; }** |  | [optional] [default to undefined]
**contractUsageTerm** | **string** |  | [optional] [default to undefined]
**previewDigest** | **string** |  | [default to undefined]
**previewToken** | **string** |  | [default to undefined]
**confirmPrice** | **boolean** |  | [default to undefined]
**confirmHistoricalPrice** | **boolean** |  | [optional] [default to false]

## Example

```typescript
import { LifetimePriceEntry } from 'campfire-typescript-sdk';

const instance: LifetimePriceEntry = {
    usageProduct,
    priceSource,
    rateCard,
    schedule,
    contractUsageTerm,
    previewDigest,
    previewToken,
    confirmPrice,
    confirmHistoricalPrice,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

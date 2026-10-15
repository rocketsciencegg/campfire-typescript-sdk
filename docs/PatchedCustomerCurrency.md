# PatchedCustomerCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**name** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**currency** | **string** |  | [optional] [default to 'USD']
**isCustom** | **boolean** | Campfire-provisioned placeholder code with no provider rates. Rates must be uploaded. | [optional] [readonly] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]

## Example

```typescript
import { PatchedCustomerCurrency } from 'campfire-typescript-sdk';

const instance: PatchedCustomerCurrency = {
    id,
    name,
    lastModifiedAt,
    isDeleted,
    deletedAt,
    currency,
    isCustom,
    createdAt,
    customer,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

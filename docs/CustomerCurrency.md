# CustomerCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**name** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**currency** | **string** |  | [optional] [default to 'USD']
**isCustom** | **boolean** | Campfire-provisioned placeholder code with no provider rates. Rates must be uploaded. | [readonly] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]

## Example

```typescript
import { CustomerCurrency } from 'campfire-typescript-sdk';

const instance: CustomerCurrency = {
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

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
    createdAt,
    customer,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

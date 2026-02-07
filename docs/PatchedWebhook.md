# PatchedWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**uuid** | **string** |  | [optional] [readonly] [default to undefined]
**url** | **string** |  | [optional] [default to undefined]
**token** | **string** |  | [optional] [readonly] [default to undefined]
**topics** | [**Array&lt;WebhookTopic&gt;**](WebhookTopic.md) |  | [optional] [default to undefined]
**active** | **boolean** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]

## Example

```typescript
import { PatchedWebhook } from 'campfire-typescript-sdk';

const instance: PatchedWebhook = {
    id,
    uuid,
    url,
    token,
    topics,
    active,
    createdAt,
    lastModifiedAt,
    customer,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

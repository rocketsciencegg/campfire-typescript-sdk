# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**uuid** | **string** |  | [readonly] [default to undefined]
**url** | **string** |  | [default to undefined]
**token** | **string** |  | [readonly] [default to undefined]
**topics** | [**Array&lt;WebhookTopic&gt;**](WebhookTopic.md) |  | [optional] [default to undefined]
**active** | **boolean** |  | [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]

## Example

```typescript
import { Webhook } from 'campfire-typescript-sdk';

const instance: Webhook = {
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

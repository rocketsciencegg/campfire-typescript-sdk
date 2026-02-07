# IntegrationsApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**integrationsApiV1WebhookCreate**](#integrationsapiv1webhookcreate) | **POST** /integrations/api/v1/webhook | Create Webhook|
|[**integrationsApiV1WebhookDestroy**](#integrationsapiv1webhookdestroy) | **DELETE** /integrations/api/v1/webhook/{id} | Delete Webhook|
|[**integrationsApiV1WebhookEventsList**](#integrationsapiv1webhookeventslist) | **GET** /integrations/api/v1/webhook/{id}/events | List Webhook Events|
|[**integrationsApiV1WebhookList**](#integrationsapiv1webhooklist) | **GET** /integrations/api/v1/webhook | List Webhooks|
|[**integrationsApiV1WebhookPartialUpdate**](#integrationsapiv1webhookpartialupdate) | **PATCH** /integrations/api/v1/webhook/{id} | Partial Update Webhook|
|[**integrationsApiV1WebhookRetrieve**](#integrationsapiv1webhookretrieve) | **GET** /integrations/api/v1/webhook/{id} | Retrieve Webhook|
|[**integrationsApiV1WebhookUpdate**](#integrationsapiv1webhookupdate) | **PUT** /integrations/api/v1/webhook/{id} | Update Webhook|

# **integrationsApiV1WebhookCreate**
> Webhook integrationsApiV1WebhookCreate(webhook)


### Example

```typescript
import {
    IntegrationsApi,
    Configuration,
    Webhook
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new IntegrationsApi(configuration);

let webhook: Webhook; //

const { status, data } = await apiInstance.integrationsApiV1WebhookCreate(
    webhook
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **webhook** | **Webhook**|  | |


### Return type

**Webhook**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrationsApiV1WebhookDestroy**
> integrationsApiV1WebhookDestroy()


### Example

```typescript
import {
    IntegrationsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new IntegrationsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.integrationsApiV1WebhookDestroy(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

void (empty response body)

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrationsApiV1WebhookEventsList**
> Array<WebhookEvent> integrationsApiV1WebhookEventsList()


### Example

```typescript
import {
    IntegrationsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new IntegrationsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.integrationsApiV1WebhookEventsList(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Array<WebhookEvent>**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrationsApiV1WebhookList**
> Array<Webhook> integrationsApiV1WebhookList()


### Example

```typescript
import {
    IntegrationsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new IntegrationsApi(configuration);

const { status, data } = await apiInstance.integrationsApiV1WebhookList();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Array<Webhook>**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrationsApiV1WebhookPartialUpdate**
> Webhook integrationsApiV1WebhookPartialUpdate()


### Example

```typescript
import {
    IntegrationsApi,
    Configuration,
    PatchedWebhook
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new IntegrationsApi(configuration);

let id: number; // (default to undefined)
let patchedWebhook: PatchedWebhook; // (optional)

const { status, data } = await apiInstance.integrationsApiV1WebhookPartialUpdate(
    id,
    patchedWebhook
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **patchedWebhook** | **PatchedWebhook**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Webhook**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrationsApiV1WebhookRetrieve**
> Webhook integrationsApiV1WebhookRetrieve()


### Example

```typescript
import {
    IntegrationsApi,
    Configuration
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new IntegrationsApi(configuration);

let id: number; // (default to undefined)

const { status, data } = await apiInstance.integrationsApiV1WebhookRetrieve(
    id
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Webhook**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrationsApiV1WebhookUpdate**
> Webhook integrationsApiV1WebhookUpdate(webhook)


### Example

```typescript
import {
    IntegrationsApi,
    Configuration,
    Webhook
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new IntegrationsApi(configuration);

let id: number; // (default to undefined)
let webhook: Webhook; //

const { status, data } = await apiInstance.integrationsApiV1WebhookUpdate(
    id,
    webhook
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **webhook** | **Webhook**|  | |
| **id** | [**number**] |  | defaults to undefined|


### Return type

**Webhook**

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


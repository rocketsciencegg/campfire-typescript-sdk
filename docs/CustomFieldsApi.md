# CustomFieldsApi

All URIs are relative to *https://api.meetcampfire.com*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**caApiV1CustomFieldsReorderCreate**](#caapiv1customfieldsreordercreate) | **POST** /ca/api/v1/custom-fields/reorder | Reorder Custom Fields|

# **caApiV1CustomFieldsReorderCreate**
> caApiV1CustomFieldsReorderCreate()

Reorder custom fields

### Example

```typescript
import {
    CustomFieldsApi,
    Configuration,
    CaApiV1CustomFieldsReorderCreateRequest
} from 'campfire-typescript-sdk';

const configuration = new Configuration();
const apiInstance = new CustomFieldsApi(configuration);

let caApiV1CustomFieldsReorderCreateRequest: CaApiV1CustomFieldsReorderCreateRequest; // (optional)

const { status, data } = await apiInstance.caApiV1CustomFieldsReorderCreate(
    caApiV1CustomFieldsReorderCreateRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **caApiV1CustomFieldsReorderCreateRequest** | **CaApiV1CustomFieldsReorderCreateRequest**|  | |


### Return type

void (empty response body)

### Authorization

[knoxApiToken](../README.md#knoxApiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


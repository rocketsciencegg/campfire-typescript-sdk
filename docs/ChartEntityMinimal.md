# ChartEntityMinimal

Minimal entity serializer for intercompany operations.  Only exposes id, name, and currency - the minimum needed for entity selection in intercompany journal entries. This prevents data leakage of sensitive entity details (addresses, emails, etc.) to users who may not have full access to all entities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**name** | **string** |  | [readonly] [default to undefined]
**currency** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { ChartEntityMinimal } from 'campfire-typescript-sdk';

const instance: ChartEntityMinimal = {
    id,
    name,
    currency,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

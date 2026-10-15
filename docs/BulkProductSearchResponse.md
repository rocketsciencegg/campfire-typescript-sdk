# BulkProductSearchResponse

Resolved products keyed by the term that matched them, plus the terms that matched several.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**{ [key: string]: ProductSearchResult; }**](ProductSearchResult.md) |  | [default to undefined]
**ambiguous** | [**Array&lt;AmbiguousProductTerm&gt;**](AmbiguousProductTerm.md) |  | [default to undefined]

## Example

```typescript
import { BulkProductSearchResponse } from 'campfire-typescript-sdk';

const instance: BulkProductSearchResponse = {
    results,
    ambiguous,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

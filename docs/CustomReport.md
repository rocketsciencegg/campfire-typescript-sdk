# CustomReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**createdByName** | **string** |  | [readonly] [default to undefined]
**updatedByName** | **string** |  | [readonly] [default to undefined]
**isFavorite** | **boolean** |  | [readonly] [default to undefined]
**dataSubtype** | [**DataSubtypeEnum**](DataSubtypeEnum.md) |  | [optional] [default to undefined]
**searchVector** | **string** |  | [readonly] [default to undefined]
**searchText** | **string** |  | [readonly] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**dataType** | [**DataTypeEnum**](DataTypeEnum.md) |  | [optional] [default to undefined]
**title** | **string** |  | [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**groupings** | **any** |  | [optional] [default to undefined]
**pivots** | **any** |  | [optional] [default to undefined]
**aggregations** | **any** |  | [optional] [default to undefined]
**staticFilters** | **any** |  | [optional] [default to undefined]
**dynamicFilters** | **any** |  | [optional] [default to undefined]
**financialStatementRows** | **any** |  | [optional] [default to undefined]
**customFormulaRows** | **any** |  | [optional] [default to undefined]
**customGroups** | **any** |  | [optional] [default to undefined]
**showEmptyLines** | **boolean** |  | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**createdBy** | **number** |  | [readonly] [default to undefined]
**updatedBy** | **number** |  | [readonly] [default to undefined]

## Example

```typescript
import { CustomReport } from 'campfire-typescript-sdk';

const instance: CustomReport = {
    id,
    createdByName,
    updatedByName,
    isFavorite,
    dataSubtype,
    searchVector,
    searchText,
    createdAt,
    lastModifiedAt,
    dataType,
    title,
    description,
    groupings,
    pivots,
    aggregations,
    staticFilters,
    dynamicFilters,
    financialStatementRows,
    customFormulaRows,
    customGroups,
    showEmptyLines,
    customer,
    createdBy,
    updatedBy,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

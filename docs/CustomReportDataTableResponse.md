# CustomReportDataTableResponse

Output schema for custom report data responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **number** | Total rows before pagination | [default to undefined]
**next** | **string** | Next page URL (null for datatable pagination) | [default to undefined]
**previous** | **string** | Previous page URL | [default to undefined]
**results** | **Array&lt;{ [key: string]: any; }&gt;** | Result rows: group field values plus one key per aggregate/pivot column (sparse — zero pivot values omitted) | [default to undefined]
**engineUsed** | [**CustomReportDataTableResponseEngineUsedEnum**](CustomReportDataTableResponseEngineUsedEnum.md) | Execution engine used (absent on flat responses from reports without groupings/aggregations)  * &#x60;postgres&#x60; - postgres * &#x60;pandas_pivot&#x60; - pandas_pivot | [optional] [default to undefined]
**totalsRow** | **{ [key: string]: any; }** | Grand totals across all rows (include_totals&#x3D;true) | [optional] [default to undefined]
**pivotResultFields** | **Array&lt;string&gt;** | Sorted list of pivot column names | [optional] [default to undefined]
**pivotValueMappings** | **{ [key: string]: any; }** | Mapping of pivot field -&gt; {display_name: id} for drilldown | [optional] [default to undefined]

## Example

```typescript
import { CustomReportDataTableResponse } from 'campfire-typescript-sdk';

const instance: CustomReportDataTableResponse = {
    count,
    next,
    previous,
    results,
    engineUsed,
    totalsRow,
    pivotResultFields,
    pivotValueMappings,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

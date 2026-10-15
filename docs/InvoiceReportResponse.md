# InvoiceReportResponse

Output schema for invoice report responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **number** | Total rows before pagination | [default to undefined]
**next** | **string** | Next page URL (null for datatable pagination) | [default to undefined]
**previous** | **string** | Previous page URL | [default to undefined]
**results** | [**Array&lt;InvoiceReportResultRow&gt;**](InvoiceReportResultRow.md) | Paginated result rows | [default to undefined]
**engineUsed** | [**InvoiceReportResponseEngineUsedEnum**](InvoiceReportResponseEngineUsedEnum.md) | Execution engine: \&#39;postgres\&#39;  * &#x60;postgres&#x60; - postgres | [default to undefined]
**pivotResultFields** | **Array&lt;string&gt;** | Sorted list of pivot column names | [optional] [default to undefined]
**totalsRow** | **{ [key: string]: any; }** | Grand totals across all rows | [optional] [default to undefined]
**pivotValueMappings** | **{ [key: string]: any; }** | Mapping of pivot field -&gt; {display_name: id} for drilldown | [optional] [default to undefined]

## Example

```typescript
import { InvoiceReportResponse } from 'campfire-typescript-sdk';

const instance: InvoiceReportResponse = {
    count,
    next,
    previous,
    results,
    engineUsed,
    pivotResultFields,
    totalsRow,
    pivotValueMappings,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

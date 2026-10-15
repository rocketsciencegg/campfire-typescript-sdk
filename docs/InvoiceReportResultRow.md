# InvoiceReportResultRow

Schema for a single result row (dimensions + aggregates + drilldown).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filterParams** | **{ [key: string]: any; }** | Filter parameters for drilldown navigation | [default to undefined]
**groupId** | **number** | Row identifier for AG Grid merging | [default to undefined]
**id** | **number** | Row identifier for AG Grid getRowId | [default to undefined]

## Example

```typescript
import { InvoiceReportResultRow } from 'campfire-typescript-sdk';

const instance: InvoiceReportResultRow = {
    filterParams,
    groupId,
    id,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

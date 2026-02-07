# BulkCreateInvoices

Serializer for bulk invoice creation. Accepts a list of invoice data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoices** | **Array&lt;{ [key: string]: any; }&gt;** | List of invoice data dictionaries matching AccountingInvoiceSerializer structure | [default to undefined]

## Example

```typescript
import { BulkCreateInvoices } from 'campfire-typescript-sdk';

const instance: BulkCreateInvoices = {
    invoices,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# PreviewInvoice

The invoice the upload will post, plus the row reference the page shows it under.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **string** |  | [default to undefined]
**invoiceNumber** | **string** |  | [optional] [default to undefined]
**invoiceDate** | **string** |  | [optional] [default to undefined]
**periodStart** | **string** |  | [optional] [default to undefined]
**periodEnd** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**client** | **number** |  | [optional] [default to undefined]
**contract** | **number** |  | [optional] [default to undefined]
**lines** | [**Array&lt;PreviewLine&gt;**](PreviewLine.md) |  | [default to undefined]

## Example

```typescript
import { PreviewInvoice } from 'campfire-typescript-sdk';

const instance: PreviewInvoice = {
    reference,
    invoiceNumber,
    invoiceDate,
    periodStart,
    periodEnd,
    currency,
    entity,
    client,
    contract,
    lines,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# PreviewInvoiceResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **string** |  | [default to undefined]
**invoiceNumber** | **string** |  | [default to undefined]
**contractId** | **number** |  | [default to undefined]
**status** | **string** |  | [default to undefined]
**reason** | **string** |  | [default to undefined]
**reviewFlags** | **Array&lt;string&gt;** |  | [default to undefined]
**allocations** | [**Array&lt;PreviewAllocation&gt;**](PreviewAllocation.md) |  | [default to undefined]

## Example

```typescript
import { PreviewInvoiceResult } from 'campfire-typescript-sdk';

const instance: PreviewInvoiceResult = {
    reference,
    invoiceNumber,
    contractId,
    status,
    reason,
    reviewFlags,
    allocations,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

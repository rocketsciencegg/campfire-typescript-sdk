# TerminateContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminationDate** | **string** |  | [default to undefined]
**voidInvoiceIds** | **Array&lt;number&gt;** | List of invoice IDs to void atomically when terminating the contract. | [optional] [default to undefined]
**voidDate** | **string** | Date to use when voiding invoices. Required when void_invoice_ids is provided. | [optional] [default to undefined]

## Example

```typescript
import { TerminateContract } from 'campfire-typescript-sdk';

const instance: TerminateContract = {
    terminationDate,
    voidInvoiceIds,
    voidDate,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# TerminateContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminationDate** | **string** |  | [default to undefined]
**voidInvoiceIds** | **Array&lt;number&gt;** | List of invoice IDs to void atomically when terminating the contract. | [optional] [default to undefined]
**voidDate** | **string** | Date to use when voiding invoices. Required when void_invoice_ids is provided. | [optional] [default to undefined]
**reverseRemainingRevenue** | **boolean** | When true, the remaining subscription schedule and billed unused prepaid commitments are settled with offsetting negative revenue transactions. Not supported for evergreen contracts. | [optional] [default to false]
**creditUnusedRevenue** | **boolean** | When true with reverse_remaining_revenue, unused billed subscription and prepaid amounts get a credit memo. Omit to credit whenever reverse_remaining_revenue is true. Send false to reverse without refunding. Unused billed prepaid then expires as breakage. | [optional] [default to undefined]
**successorContractId** | **number** | Successor contract that receives the usage-relative recognition-basis adjustment. | [optional] [default to undefined]
**successorTargetKind** | [**SuccessorTargetKindEnum**](SuccessorTargetKindEnum.md) | Successor target kind for the signed recognition-basis adjustment.  * &#x60;prepaid_commit&#x60; - prepaid_commit | [optional] [default to undefined]
**successorTargetId** | **number** | Successor prepaid commit or relative subscription that receives the adjustment. | [optional] [default to undefined]

## Example

```typescript
import { TerminateContract } from 'campfire-typescript-sdk';

const instance: TerminateContract = {
    terminationDate,
    voidInvoiceIds,
    voidDate,
    reverseRemainingRevenue,
    creditUnusedRevenue,
    successorContractId,
    successorTargetKind,
    successorTargetId,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

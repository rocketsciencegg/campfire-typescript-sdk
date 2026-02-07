# TerminateContractResponse

Response serializer for contract termination with hints about drafted operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contractTerminated** | **boolean** | Whether the contract was terminated directly (True) or drafted (False). | [default to undefined]
**contractDraftId** | **number** | Draft queue ID if contract termination was drafted instead of executed. | [optional] [default to undefined]
**voidedInvoiceIds** | **Array&lt;number&gt;** | List of invoice IDs that were voided directly. | [optional] [default to undefined]
**draftedInvoiceIds** | **Array&lt;number&gt;** | List of invoice IDs that were drafted for voiding (user lacks void permission). | [optional] [default to undefined]

## Example

```typescript
import { TerminateContractResponse } from 'campfire-typescript-sdk';

const instance: TerminateContractResponse = {
    contractTerminated,
    contractDraftId,
    voidedInvoiceIds,
    draftedInvoiceIds,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

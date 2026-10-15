# PatchedBillDraftWrite

Editable subset used during review (PATCH).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **number** |  | [optional] [default to undefined]
**extractedVendorName** | **string** |  | [optional] [default to undefined]
**extractedBillNumber** | **string** |  | [optional] [default to undefined]
**extractedBillDate** | **string** |  | [optional] [default to undefined]
**extractedDueDate** | **string** |  | [optional] [default to undefined]
**extractedCurrency** | **string** |  | [optional] [default to undefined]
**extractedTotalAmount** | **number** |  | [optional] [default to undefined]
**extractedLineItems** | **any** |  | [optional] [default to undefined]
**stagedPayload** | **any** |  | [optional] [default to undefined]
**resolvedVendor** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedBillDraftWrite } from 'campfire-typescript-sdk';

const instance: PatchedBillDraftWrite = {
    entity,
    extractedVendorName,
    extractedBillNumber,
    extractedBillDate,
    extractedDueDate,
    extractedCurrency,
    extractedTotalAmount,
    extractedLineItems,
    stagedPayload,
    resolvedVendor,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

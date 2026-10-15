# BillDraftDetail

Detail read shape: the full draft plus vendor-history department suggestions.  Kept off ``BillDraftReadSerializer``: the list endpoint shares it, and one history query per draft would be an N+1 across the inbox grid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**source** | [**Source340Enum**](Source340Enum.md) |  | [default to undefined]
**sourceFile** | **number** |  | [optional] [default to undefined]
**senderEmail** | **string** |  | [optional] [default to undefined]
**recipientAlias** | **string** |  | [optional] [default to undefined]
**emailSubject** | **string** |  | [optional] [default to undefined]
**status** | [**Status8d4Enum**](Status8d4Enum.md) |  | [readonly] [default to undefined]
**parseError** | **string** |  | [optional] [default to undefined]
**extractedVendorName** | **string** |  | [optional] [default to undefined]
**extractedBillNumber** | **string** |  | [optional] [default to undefined]
**extractedBillDate** | **string** |  | [optional] [default to undefined]
**extractedDueDate** | **string** |  | [optional] [default to undefined]
**extractedCurrency** | **string** |  | [optional] [default to undefined]
**extractedTotalAmount** | **number** |  | [optional] [default to undefined]
**extractedLineItems** | **any** |  | [optional] [default to undefined]
**fieldConfidence** | **any** |  | [optional] [default to undefined]
**stagedPayload** | **any** |  | [optional] [default to undefined]
**resolvedVendor** | **number** |  | [optional] [default to undefined]
**dedupHash** | **string** |  | [readonly] [default to undefined]
**promotedBill** | **number** |  | [readonly] [default to undefined]
**discardReason** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**createdBy** | **number** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**departmentSuggestions** | **{ [key: string]: { [key: string]: number; }; }** | GL account -&gt; department the vendor\&#39;s prior lines were coded to. | [readonly] [default to undefined]

## Example

```typescript
import { BillDraftDetail } from 'campfire-typescript-sdk';

const instance: BillDraftDetail = {
    id,
    customer,
    entity,
    source,
    sourceFile,
    senderEmail,
    recipientAlias,
    emailSubject,
    status,
    parseError,
    extractedVendorName,
    extractedBillNumber,
    extractedBillDate,
    extractedDueDate,
    extractedCurrency,
    extractedTotalAmount,
    extractedLineItems,
    fieldConfidence,
    stagedPayload,
    resolvedVendor,
    dedupHash,
    promotedBill,
    discardReason,
    createdAt,
    createdBy,
    lastModifiedAt,
    departmentSuggestions,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

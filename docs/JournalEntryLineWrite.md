# JournalEntryLineWrite

Documentation-only write shape of one ``transactions`` line. ``JournalEntrySerializer`` reads lines from the raw request body, so the OpenAPI request schema has to declare them here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** | Existing transaction id; set on update to modify a line. | [optional] [default to undefined]
**account** | **number** | Chart account id. | [default to undefined]
**entity** | **number** | Entity id for the line. | [optional] [default to undefined]
**vendor** | **number** | Vendor id. | [optional] [default to undefined]
**department** | **number** | Department id. | [optional] [default to undefined]
**tags** | [**Array&lt;JournalEntryLineTagWrite&gt;**](JournalEntryLineTagWrite.md) |  | [optional] [default to undefined]
**debitAmountNative** | **number** |  | [optional] [default to undefined]
**creditAmountNative** | **number** |  | [optional] [default to undefined]
**debitAmountBook** | **number** |  | [optional] [default to undefined]
**creditAmountBook** | **number** |  | [optional] [default to undefined]
**debitAmount** | **number** |  | [optional] [default to undefined]
**creditAmount** | **number** |  | [optional] [default to undefined]
**bankDescription** | **string** |  | [optional] [default to undefined]
**note** | **string** |  | [optional] [default to undefined]
**merchantName** | **string** |  | [optional] [default to undefined]
**receiptUrl** | **string** |  | [optional] [default to undefined]
**externalId** | **string** |  | [optional] [default to undefined]
**counterpartyEntity** | **number** | Other entity id; required on intercompany account lines for ic_reconciliation customers. | [optional] [default to undefined]

## Example

```typescript
import { JournalEntryLineWrite } from 'campfire-typescript-sdk';

const instance: JournalEntryLineWrite = {
    id,
    account,
    entity,
    vendor,
    department,
    tags,
    debitAmountNative,
    creditAmountNative,
    debitAmountBook,
    creditAmountBook,
    debitAmount,
    creditAmount,
    bankDescription,
    note,
    merchantName,
    receiptUrl,
    externalId,
    counterpartyEntity,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# TerminationSettlementPreviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminationDate** | **string** |  | [default to undefined]
**postingDate** | **string** |  | [default to undefined]
**totalReversalAmount** | **number** |  | [default to undefined]
**totalCreditAmount** | **number** |  | [default to undefined]
**sourceCreditAmount** | **number** |  | [default to undefined]
**successorCreditAmount** | **number** |  | [default to undefined]
**totalTaxAmount** | **number** |  | [default to undefined]
**lines** | [**Array&lt;TerminationSettlementLine&gt;**](TerminationSettlementLine.md) |  | [default to undefined]
**warnings** | **Array&lt;string&gt;** |  | [default to undefined]
**canSettle** | **boolean** |  | [default to undefined]
**blockingReason** | **string** |  | [default to undefined]
**successorAdjustment** | [**TerminationSuccessorAdjustment**](TerminationSuccessorAdjustment.md) |  | [default to undefined]
**reconciliation** | [**TerminationSettlementReconciliation**](TerminationSettlementReconciliation.md) |  | [default to undefined]

## Example

```typescript
import { TerminationSettlementPreviewResponse } from 'campfire-typescript-sdk';

const instance: TerminationSettlementPreviewResponse = {
    terminationDate,
    postingDate,
    totalReversalAmount,
    totalCreditAmount,
    sourceCreditAmount,
    successorCreditAmount,
    totalTaxAmount,
    lines,
    warnings,
    canSettle,
    blockingReason,
    successorAdjustment,
    reconciliation,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

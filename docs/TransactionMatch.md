# TransactionMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**matchedObject** | **string** |  | [readonly] [default to undefined]
**appLabel** | **string** |  | [readonly] [default to undefined]
**model** | **string** |  | [readonly] [default to undefined]
**drafts** | **string** |  | [readonly] [default to undefined]
**objectId** | **number** |  | [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**reviewedAt** | **string** |  | [optional] [default to undefined]
**status** | [**TransactionMatchStatusEnum**](TransactionMatchStatusEnum.md) |  | [optional] [default to undefined]
**confidenceScore** | **number** |  | [optional] [default to undefined]
**reason** | **string** | Why the matcher assigned this status (e.g. reference_surfaced, reference_auto_approved, needs_review, auto_approved). Display/observability only. | [optional] [default to undefined]
**snapshot** | **any** | Snapshot of transaction data preserved for training data when the transaction is deleted. | [optional] [default to undefined]
**autoApplied** | **boolean** | True when the matcher committed this match as accepted without human review. The durable auto-vs-human discriminator: reviewed_by is unreliable for this because the apply flow attributes the payment to the agent\&#39;s attributed user. | [optional] [default to undefined]
**appliedPaymentKind** | [**AppliedPaymentKindEnum**](AppliedPaymentKindEnum.md) | Kind of payment created when this match was applied.  * &#x60;AIP&#x60; - Invoice payment * &#x60;ABP&#x60; - Bill payment | [optional] [default to undefined]
**appliedPaymentId** | **number** | ID of the AccountingInvoicePayment/AccountingBillPayment created when this match was applied. Plain integer, not a FK: the match record must outlive the payment. | [optional] [default to undefined]
**thresholdAtApply** | **number** | The agent\&#39;s auto-approve confidence threshold at the moment this match auto-applied. | [optional] [default to undefined]
**agentRunId** | **string** | AgentRun that produced this match. Plain UUID, not a FK: the audit record must outlive the run. Enables group-by-run views and bulk undo. | [optional] [default to undefined]
**revertedAt** | **string** |  | [optional] [default to undefined]
**customer** | **number** |  | [default to undefined]
**transaction** | **number** |  | [default to undefined]
**contentType** | **number** |  | [default to undefined]
**reviewedBy** | **number** |  | [optional] [default to undefined]
**revertedBy** | **number** | User whose undo (or payment void/delete) reverted this applied match. | [optional] [default to undefined]

## Example

```typescript
import { TransactionMatch } from 'campfire-typescript-sdk';

const instance: TransactionMatch = {
    id,
    matchedObject,
    appLabel,
    model,
    drafts,
    objectId,
    createdAt,
    reviewedAt,
    status,
    confidenceScore,
    reason,
    snapshot,
    autoApplied,
    appliedPaymentKind,
    appliedPaymentId,
    thresholdAtApply,
    agentRunId,
    revertedAt,
    customer,
    transaction,
    contentType,
    reviewedBy,
    revertedBy,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# ChartTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**entityCurrency** | **string** |  | [readonly] [default to undefined]
**accountName** | **string** | Combines account number and name in the format \&quot;number - name\&quot; | [readonly] [default to undefined]
**accountNumber** | **string** |  | [readonly] [default to undefined]
**vendorName** | **string** | Name of the linked Campfire Vendor object. Distinct from &#x60;merchant_name&#x60;, which is free text stored directly on the transaction and not linked to a Campfire object. | [readonly] [default to undefined]
**vendorId** | **string** |  | [readonly] [default to undefined]
**vendorCampfireId** | **string** | Stable, user-facing Campfire ID of the linked Campfire Vendor object (e.g. &#x60;VEN-0000001&#x60;). | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**departmentCode** | **string** |  | [readonly] [default to undefined]
**parentDepartmentName** | **string** |  | [readonly] [default to undefined]
**parentDepartment** | **number** |  | [readonly] [default to undefined]
**costAllocationName** | **string** |  | [readonly] [default to undefined]
**tags** | [**Array&lt;TransactionTag&gt;**](TransactionTag.md) |  | [readonly] [default to undefined]
**journal** | **number** |  | [readonly] [default to undefined]
**journalOrder** | **string** |  | [readonly] [default to undefined]
**journalMemo** | **string** |  | [readonly] [default to undefined]
**journalType** | **string** |  | [readonly] [default to undefined]
**intercompanyJournal** | **number** |  | [readonly] [default to undefined]
**createdAutomatically** | **boolean** |  | [readonly] [default to undefined]
**journalAttachments** | **Array&lt;any&gt;** |  | [readonly] [default to undefined]
**journalTypeName** | **string** |  | [readonly] [default to undefined]
**invoice** | **string** |  | [readonly] [default to undefined]
**bill** | **string** |  | [readonly] [default to undefined]
**dateMonth** | **string** | Two-digit month (MM) derived from &#x60;posted_at&#x60;, the transaction date. | [readonly] [default to undefined]
**dateYear** | **string** | Four-digit year (YYYY) derived from &#x60;posted_at&#x60;, the transaction date. | [readonly] [default to undefined]
**balanceAfterTransaction** | **number** |  | [readonly] [default to undefined]
**bankAccount** | **string** |  | [readonly] [default to undefined]
**bankAccountName** | **string** |  | [readonly] [default to undefined]
**account** | **number** |  | [optional] [default to undefined]
**lastModifiedByName** | **string** |  | [readonly] [default to undefined]
**accountType** | **string** |  | [readonly] [default to undefined]
**accountSubtype** | **string** |  | [readonly] [default to undefined]
**parentAccountName** | **string** |  | [readonly] [default to undefined]
**files** | **string** |  | [readonly] [default to undefined]
**invoiceId** | **number** |  | [readonly] [default to undefined]
**invoiceNumber** | **string** |  | [readonly] [default to undefined]
**billId** | **number** |  | [readonly] [default to undefined]
**billNumber** | **string** |  | [readonly] [default to undefined]
**fileNames** | **string** |  | [readonly] [default to undefined]
**hasMatches** | **boolean** |  | [readonly] [default to undefined]
**hasAi** | **boolean** |  | [readonly] [default to undefined]
**hasRules** | **boolean** |  | [readonly] [default to undefined]
**hasMerges** | **boolean** |  | [readonly] [default to undefined]
**hasFixedAssetRuleMatches** | **boolean** |  | [readonly] [default to undefined]
**hasSuggestedRule** | **boolean** |  | [readonly] [default to undefined]
**suggestedRuleAccountName** | **string** |  | [readonly] [default to undefined]
**primaryActionType** | **string** |  | [readonly] [default to undefined]
**suggestedAccount** | **number** |  | [readonly] [default to undefined]
**suggestedAccountName** | **string** |  | [readonly] [default to undefined]
**suggestedAccountNumber** | **string** |  | [readonly] [default to undefined]
**amount** | **number** | Amount in consolidated currency (the currency of the root entity). | [readonly] [default to undefined]
**amountNative** | **number** | Amount in the currency the transaction was originally created in. | [readonly] [default to undefined]
**amountBook** | **number** | Amount in the currency of the entity this transaction belongs to. | [readonly] [default to undefined]
**amortizationSchedule** | [**Array&lt;AmortizationSchedule&gt;**](AmortizationSchedule.md) |  | [readonly] [default to undefined]
**linkedAmortizations** | **Array&lt;{ [key: string]: any; }&gt;** |  | [readonly] [default to undefined]
**createdFixedAssets** | **Array&lt;{ [key: string]: string; }&gt;** | Return all fixed assets this transaction is linked to — via the legacy &#x60;purchase_transaction&#x60; FK (reverse: &#x60;created_fixed_assets&#x60;) AND the new &#x60;purchase_transactions&#x60; M2M (reverse: &#x60;linked_fixed_assets&#x60;). Dual-write keeps the FK target in the M2M, but using both covers any pre-backfill drift and surfaces non-primary M2M-only links (e.g. the secondary txns in a multi-txn fixed asset, or a split-resized txn). | [readonly] [default to undefined]
**reconciliationReport** | **string** |  | [readonly] [default to undefined]
**opposingAccountName** | **string** |  | [readonly] [default to undefined]
**opposingAccountNumber** | **string** |  | [readonly] [default to undefined]
**taxRate** | **number** |  | [optional] [default to undefined]
**applyBothSides** | **boolean** |  | [optional] [default to false]
**transactionMatchId** | **number** |  | [optional] [default to undefined]
**transactionId** | **string** |  | [readonly] [default to undefined]
**debitAmount** | **number** |  | [optional] [default to undefined]
**creditAmount** | **number** |  | [optional] [default to undefined]
**debitAmountBook** | **number** |  | [optional] [default to undefined]
**creditAmountBook** | **number** |  | [optional] [default to undefined]
**debitAmountNative** | **number** |  | [optional] [default to undefined]
**creditAmountNative** | **number** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**postedAt** | **string** |  | [optional] [default to undefined]
**merchantName** | **string** |  | [optional] [default to undefined]
**bankDescription** | **string** |  | [optional] [default to undefined]
**tagIds** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**tagGroupIds** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**note** | **string** |  | [optional] [default to undefined]
**receiptUrl** | **string** |  | [optional] [default to undefined]
**balanceBeforeTransaction** | **number** |  | [readonly] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**externalId** | **string** |  | [optional] [default to undefined]
**producer** | **string** | Lane that owns this leg\&#39;s money and date fields. NULL for every pre-loader producer. | [readonly] [default to undefined]
**warehouseRowKey** | **string** | Identity of the warehouse row this leg projects, as &lt;connection_id&gt;:&lt;row_key&gt;. Distinct from external_id, which holds the bare Stripe object id that other lanes resolve back to Stripe by prefix. NULL for every producer except the Stripe top-down loader. | [readonly] [default to undefined]
**needsReview** | **boolean** |  | [optional] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**draftMatches** | **any** |  | [optional] [default to undefined]
**lastLamPredictionAttempt** | **string** |  | [optional] [default to undefined]
**sourceGroup** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [default to undefined]
**sourceEntity** | **number** |  | [optional] [default to undefined]
**counterpartyEntity** | **number** |  | [readonly] [default to undefined]
**parentBankTransaction** | **number** |  | [optional] [default to undefined]
**vendor** | **number** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**lastModifiedBy** | **number** |  | [optional] [default to undefined]
**costAllocation** | **number** |  | [readonly] [default to undefined]
**lastSyncRun** | **number** |  | [readonly] [default to undefined]

## Example

```typescript
import { ChartTransaction } from 'campfire-typescript-sdk';

const instance: ChartTransaction = {
    id,
    isDeleted,
    deletedAt,
    entityName,
    entityCurrency,
    accountName,
    accountNumber,
    vendorName,
    vendorId,
    vendorCampfireId,
    departmentName,
    departmentCode,
    parentDepartmentName,
    parentDepartment,
    costAllocationName,
    tags,
    journal,
    journalOrder,
    journalMemo,
    journalType,
    intercompanyJournal,
    createdAutomatically,
    journalAttachments,
    journalTypeName,
    invoice,
    bill,
    dateMonth,
    dateYear,
    balanceAfterTransaction,
    bankAccount,
    bankAccountName,
    account,
    lastModifiedByName,
    accountType,
    accountSubtype,
    parentAccountName,
    files,
    invoiceId,
    invoiceNumber,
    billId,
    billNumber,
    fileNames,
    hasMatches,
    hasAi,
    hasRules,
    hasMerges,
    hasFixedAssetRuleMatches,
    hasSuggestedRule,
    suggestedRuleAccountName,
    primaryActionType,
    suggestedAccount,
    suggestedAccountName,
    suggestedAccountNumber,
    amount,
    amountNative,
    amountBook,
    amortizationSchedule,
    linkedAmortizations,
    createdFixedAssets,
    reconciliationReport,
    opposingAccountName,
    opposingAccountNumber,
    taxRate,
    applyBothSides,
    transactionMatchId,
    transactionId,
    debitAmount,
    creditAmount,
    debitAmountBook,
    creditAmountBook,
    debitAmountNative,
    creditAmountNative,
    currency,
    exchangeRate,
    exchangeRateBook,
    postedAt,
    merchantName,
    bankDescription,
    tagIds,
    tagGroupIds,
    note,
    receiptUrl,
    balanceBeforeTransaction,
    createdAt,
    externalId,
    producer,
    warehouseRowKey,
    needsReview,
    lastModifiedAt,
    draftMatches,
    lastLamPredictionAttempt,
    sourceGroup,
    customer,
    entity,
    sourceEntity,
    counterpartyEntity,
    parentBankTransaction,
    vendor,
    department,
    lastModifiedBy,
    costAllocation,
    lastSyncRun,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

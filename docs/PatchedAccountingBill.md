# PatchedAccountingBill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**lines** | [**Array&lt;AccountingBillLine&gt;**](AccountingBillLine.md) |  | [optional] [default to undefined]
**payments** | [**Array&lt;AccountingBillPayment&gt;**](AccountingBillPayment.md) |  | [optional] [readonly] [default to undefined]
**paymentJournalEntries** | **Array&lt;number&gt;** |  | [optional] [readonly] [default to undefined]
**status** | **string** |  | [optional] [readonly] [default to undefined]
**pastDueDays** | **number** |  | [optional] [readonly] [default to undefined]
**entityName** | **string** |  | [optional] [readonly] [default to undefined]
**entityCurrency** | **string** |  | [optional] [readonly] [default to undefined]
**vendorName** | **string** |  | [optional] [readonly] [default to undefined]
**vendorCampfireId** | **string** |  | [optional] [readonly] [default to undefined]
**apAccountName** | **string** | Return AP account name with number in \&#39;number - name\&#39; format, similar to name_and_number. | [optional] [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [optional] [readonly] [default to undefined]
**totalAmount** | **number** |  | [optional] [readonly] [default to undefined]
**amountDue** | **number** |  | [optional] [readonly] [default to undefined]
**amountPaid** | **number** |  | [optional] [readonly] [default to undefined]
**itemDate** | **string** |  | [optional] [default to undefined]
**migratedJournalId** | **number** |  | [optional] [default to undefined]
**voidedDate** | **string** |  | [optional] [readonly] [default to undefined]
**voidedJournalEntryOrder** | **string** |  | [optional] [readonly] [default to undefined]
**amortizations** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**rampUseSandbox** | **string** |  | [optional] [readonly] [default to undefined]
**navanRegion** | **string** | Navan data region (&#x60;&#x60;US&#x60;&#x60;/&#x60;&#x60;EU&#x60;&#x60;) for a Navan-sourced bill, else &#x60;&#x60;None&#x60;&#x60;.  Mirrors &#x60;&#x60;ramp_use_sandbox&#x60;&#x60;: the frontend builds the \&quot;Open in Navan\&quot; deep link from &#x60;&#x60;source_id&#x60;&#x60; and uses this to pick the web-app host (US -&gt; app.navan.com, EU -&gt; app-fra.navan.com). Navan bills carry no FK to their connection, so the region is resolved per customer and memoized to avoid an N+1 lookup across a bill list. | [optional] [readonly] [default to undefined]
**zipMetadata** | **string** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**paymentTermName** | **string** |  | [optional] [readonly] [default to undefined]
**chatUuid** | **string** |  | [optional] [default to undefined]
**withholdingInfo** | **{ [key: string]: any; }** | Withholding context for the bill\&#39;s entity (AP side).  &#x60;&#x60;estimated_withholding_amount&#x60;&#x60; covers only the remaining amount due (null once fully paid); &#x60;&#x60;withheld_to_date&#x60;&#x60; is the signed sum of posted withholding (AP legs are credits, reversals debits), so actuals replace the estimate as payments post. Certificate-based schemes estimate from the vendor certificate\&#39;s rate valid today (falling back to the scheme default). | [optional] [readonly] [default to undefined]
**csvUploadRunId** | **number** | Upload run to record this row against; must be one of your own runs. Ignored on update. | [optional] [default to undefined]
**csvUploadRowNumber** | **number** | Spreadsheet row this document starts on (the header is row 1), recorded with it. Ignored on update. | [optional] [default to undefined]
**searchVector** | **string** |  | [optional] [readonly] [default to undefined]
**searchText** | **string** |  | [optional] [readonly] [default to undefined]
**mailingAddress** | **string** |  | [optional] [default to undefined]
**terms** | [**TermsEnum**](TermsEnum.md) |  | [optional] [default to undefined]
**billNumber** | **string** |  | [optional] [default to undefined]
**billDate** | **string** |  | [optional] [default to undefined]
**dueDate** | **string** |  | [optional] [default to undefined]
**paidDate** | **string** |  | [optional] [default to undefined]
**messageOnBill** | **string** |  | [optional] [default to undefined]
**itaAllocationNumber** | **string** |  | [optional] [default to undefined]
**itaBillType** | [**ItaBillTypeEnum**](ItaBillTypeEnum.md) | Israel tax compliance: bill classification type  * &#x60;other&#x60; - Other * &#x60;equipment&#x60; - Equipment | [optional] [default to undefined]
**sourceId** | **string** |  | [optional] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**sourceBillData** | **any** |  | [optional] [default to undefined]
**externalRampId** | **string** |  | [optional] [default to undefined]
**paymentStatus** | [**AccountingBillPaymentStatusEnum**](AccountingBillPaymentStatusEnum.md) |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**originSettlementAmount** | **number** |  | [optional] [default to undefined]
**originSettlementCurrency** | **string** |  | [optional] [default to undefined]
**originFxRate** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**taxBehavior** | [**TaxBehaviorEnum**](TaxBehaviorEnum.md) |  | [optional] [default to undefined]
**billType** | [**BillTypeEnum**](BillTypeEnum.md) |  | [optional] [default to undefined]
**chatId** | **number** |  | [optional] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**vendor** | **number** |  | [optional] [default to undefined]
**paymentTerm** | **number** | Payment term for this bill | [optional] [default to undefined]
**journalEntry** | **number** |  | [optional] [default to undefined]
**sourceFile** | **number** |  | [optional] [default to undefined]
**taxRate** | **number** |  | [optional] [default to undefined]
**apAccount** | **number** | Accounts Payable account for this bill | [optional] [default to undefined]
**voidedJournalEntry** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedAccountingBill } from 'campfire-typescript-sdk';

const instance: PatchedAccountingBill = {
    id,
    lines,
    payments,
    paymentJournalEntries,
    status,
    pastDueDays,
    entityName,
    entityCurrency,
    vendorName,
    vendorCampfireId,
    apAccountName,
    attachments,
    totalAmount,
    amountDue,
    amountPaid,
    itemDate,
    migratedJournalId,
    voidedDate,
    voidedJournalEntryOrder,
    amortizations,
    lastModifiedAt,
    rampUseSandbox,
    navanRegion,
    zipMetadata,
    isDeleted,
    deletedAt,
    paymentTermName,
    chatUuid,
    withholdingInfo,
    csvUploadRunId,
    csvUploadRowNumber,
    searchVector,
    searchText,
    mailingAddress,
    terms,
    billNumber,
    billDate,
    dueDate,
    paidDate,
    messageOnBill,
    itaAllocationNumber,
    itaBillType,
    sourceId,
    source,
    sourceBillData,
    externalRampId,
    paymentStatus,
    currency,
    exchangeRate,
    exchangeRateBook,
    originSettlementAmount,
    originSettlementCurrency,
    originFxRate,
    createdAt,
    taxBehavior,
    billType,
    chatId,
    customer,
    entity,
    vendor,
    paymentTerm,
    journalEntry,
    sourceFile,
    taxRate,
    apAccount,
    voidedJournalEntry,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

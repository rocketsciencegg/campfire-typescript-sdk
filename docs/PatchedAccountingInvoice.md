# PatchedAccountingInvoice

Expose a stable two-decimal overage total on invoice serializers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**overageAmount** | **string** | Invoice-currency overage before tax, as a two-decimal string. | [optional] [readonly] [default to undefined]
**lines** | [**Array&lt;AccountingInvoiceLine&gt;**](AccountingInvoiceLine.md) |  | [optional] [default to undefined]
**emails** | **Array&lt;{ [key: string]: any; }&gt;** |  | [optional] [readonly] [default to undefined]
**payments** | [**Array&lt;AccountingInvoicePayment&gt;**](AccountingInvoicePayment.md) |  | [optional] [readonly] [default to undefined]
**relatedJournalEntries** | [**Array&lt;AccountingInvoiceJournalEntry&gt;**](AccountingInvoiceJournalEntry.md) |  | [optional] [readonly] [default to undefined]
**paymentJournalEntries** | **Array&lt;number&gt;** |  | [optional] [readonly] [default to undefined]
**journalEntryIntercompany** | **string** |  | [optional] [readonly] [default to undefined]
**clientName** | **string** |  | [optional] [readonly] [default to undefined]
**clientCampfireId** | **string** |  | [optional] [readonly] [default to undefined]
**clientEmail** | **string** |  | [optional] [readonly] [default to undefined]
**anrokCustomerId** | **string** |  | [optional] [readonly] [default to undefined]
**clientInvoiceMessage** | **string** |  | [optional] [readonly] [default to undefined]
**clientUseStripeAutoBill** | **boolean** |  | [optional] [readonly] [default to undefined]
**clientIsReseller** | **boolean** |  | [optional] [readonly] [default to undefined]
**publicInvoicePaymentUrl** | **string** |  | [optional] [readonly] [default to undefined]
**status** | **string** |  | [optional] [readonly] [default to undefined]
**pastDueDays** | **number** |  | [optional] [readonly] [default to undefined]
**entityName** | **string** |  | [optional] [readonly] [default to undefined]
**entityCurrency** | **string** |  | [optional] [readonly] [default to undefined]
**entityInvoiceMessage** | **string** |  | [optional] [readonly] [default to undefined]
**totalAmount** | **number** |  | [optional] [readonly] [default to undefined]
**amountPaid** | **number** |  | [optional] [readonly] [default to undefined]
**amountDue** | **number** |  | [optional] [readonly] [default to undefined]
**withholdingInfo** | **{ [key: string]: any; }** | Withholding context for the invoice\&#39;s entity.  &#x60;&#x60;estimated_withholding_amount&#x60;&#x60; covers only the remaining amount due (null once fully paid); &#x60;&#x60;withheld_to_date&#x60;&#x60; is the signed sum of posted withholding, so actuals replace the estimate as receipts come in. Certificate-based schemes estimate from the entity certificate\&#39;s rate (falling back to the scheme default); rules-based schemes sum each line\&#39;s selected rate over the line amount, scaled by the remaining-due proportion. | [optional] [readonly] [default to undefined]
**contractName** | **string** |  | [optional] [readonly] [default to undefined]
**contractDealId** | **string** |  | [optional] [readonly] [default to undefined]
**revenueContract** | **number** |  | [optional] [readonly] [default to undefined]
**revenueContractName** | **string** |  | [optional] [readonly] [default to undefined]
**revenueContractNumber** | **string** |  | [optional] [readonly] [default to undefined]
**attachments** | **Array&lt;any&gt;** |  | [optional] [readonly] [default to undefined]
**invoiceNumber** | **string** |  | [optional] [default to undefined]
**stripeConnectionName** | **string** |  | [optional] [readonly] [default to undefined]
**stripeConnectionEntity** | **number** |  | [optional] [readonly] [default to undefined]
**stripeConnectionBillingPortalEnabled** | **boolean** |  | [optional] [readonly] [default to undefined]
**avalaraConnectionName** | **string** |  | [optional] [readonly] [default to undefined]
**avalaraConnectionCompany** | **string** |  | [optional] [readonly] [default to undefined]
**taxRateName** | **string** |  | [optional] [readonly] [default to undefined]
**taxRateValue** | **number** |  | [optional] [readonly] [default to undefined]
**paymentTermName** | **string** |  | [optional] [readonly] [default to undefined]
**revenueTransactions** | **Array&lt;number&gt;** | Write-only. Revenue transaction IDs to link to this invoice. This field is never included in responses. | [optional] [default to undefined]
**revenueContractInvoice** | **number** | Contract billing-schedule invoice to link this AR invoice to at creation. | [optional] [default to undefined]
**revenueContractLink** | **number** | Revenue contract to link this AR invoice to at creation, outside its billing schedule. | [optional] [default to undefined]
**itemDate** | **string** |  | [optional] [default to undefined]
**migratedJournalId** | **number** |  | [optional] [default to undefined]
**voidedJournalEntryOrder** | **number** |  | [optional] [readonly] [default to undefined]
**contractCustomFields** | **Array&lt;{ [key: string]: AccountingInvoiceContractCustomFieldsInnerValue; }&gt;** |  | [optional] [readonly] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**departmentName** | **string** |  | [optional] [default to undefined]
**tags** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**chatUuid** | **string** |  | [optional] [default to undefined]
**counterpartyEntity** | **number** |  | [optional] [default to undefined]
**csvUploadRunId** | **number** | Upload run to record this row against; must be one of your own runs. Ignored on update. | [optional] [default to undefined]
**csvUploadRowNumber** | **number** | Spreadsheet row this document starts on (the header is row 1), recorded with it. Ignored on update. | [optional] [default to undefined]
**autoSendInvoice** | **boolean** |  | [optional] [default to undefined]
**autoSendInvoiceAt** | **string** |  | [optional] [default to undefined]
**autoSentAt** | **string** |  | [optional] [readonly] [default to undefined]
**reminderSentDates** | **any** | Dictionary tracking when reminders were sent for each day overdue (e.g., {\&#39;5\&#39;: \&#39;2024-01-15\&#39;, \&#39;10\&#39;: \&#39;2024-01-20\&#39;}) | [optional] [default to undefined]
**preDueReminderSentDates** | **any** | Dictionary tracking when pre-due reminders were sent for each day before due date (e.g., {\&#39;3\&#39;: \&#39;2024-01-10\&#39;, \&#39;7\&#39;: \&#39;2024-01-06\&#39;}) | [optional] [default to undefined]
**billingAddress** | **string** |  | [optional] [default to undefined]
**billingAddressee** | **string** |  | [optional] [default to undefined]
**shippingAddress** | **string** |  | [optional] [default to undefined]
**shippingAddressee** | **string** |  | [optional] [default to undefined]
**terms** | [**TermsEnum**](TermsEnum.md) |  | [optional] [default to undefined]
**refNumber** | **string** |  | [optional] [default to undefined]
**purchaseOrderNumber** | **string** |  | [optional] [default to undefined]
**invoiceDate** | **string** |  | [optional] [default to undefined]
**dueDate** | **string** |  | [optional] [default to undefined]
**shippingDate** | **string** |  | [optional] [default to undefined]
**paidDate** | **string** |  | [optional] [default to undefined]
**uncollectibleDate** | **string** |  | [optional] [default to undefined]
**sentDate** | **string** |  | [optional] [readonly] [default to undefined]
**periodStart** | **string** |  | [optional] [default to undefined]
**periodEnd** | **string** |  | [optional] [default to undefined]
**locationOfSale** | **string** |  | [optional] [default to undefined]
**messageOnInvoice** | **string** |  | [optional] [default to undefined]
**itaAllocationNumber** | **string** |  | [optional] [default to undefined]
**paymentStatus** | [**PaymentStatusCdcEnum**](PaymentStatusCdcEnum.md) |  | [optional] [default to undefined]
**anrokTransactionId** | **string** | ID of the transaction in Anrok (set when transaction is created) | [optional] [default to undefined]
**excludeFromTaxConnection** | **boolean** | When true, no tax is calculated through, and no transaction is created in, the entity\&#39;s tax connection for this invoice. Set at creation; cannot be changed. | [optional] [default to undefined]
**warningMessage** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**lastSentAt** | **string** |  | [optional] [readonly] [default to undefined]
**integrationId** | **string** |  | [optional] [default to undefined]
**integrationContext** | **any** |  | [optional] [default to undefined]
**vatNumber** | **string** |  | [optional] [default to undefined]
**vatNumberFromContract** | **boolean** | Set when the stamped vat_number came from the invoice\&#39;s contract; the PDF then prints it instead of the client\&#39;s current tax ID. | [optional] [default to undefined]
**shippingAddressFromContract** | **boolean** | Set when the stamped shipping_address came from the invoice\&#39;s contract; connector tax is then quoted at that address instead of the client\&#39;s. | [optional] [default to undefined]
**taxExempt** | **boolean** | Snapshot of the contract\&#39;s tax exemption when the invoice was generated; no tax is calculated. | [optional] [default to undefined]
**discount** | **number** | Discount amount for the invoice | [optional] [default to undefined]
**paymentTermAppliedDiscount** | **number** | Discount amount applied based on payment term early payment discount | [optional] [default to undefined]
**useStripeAutoBill** | **boolean** |  | [optional] [default to undefined]
**stripePaymentLinkId** | **string** |  | [optional] [default to undefined]
**stripePaymentIntentId** | **string** |  | [optional] [default to undefined]
**stripeInvoiceId** | **string** |  | [optional] [readonly] [default to undefined]
**stripePdfUrl** | **string** |  | [optional] [default to undefined]
**stripePaymentLink** | **string** |  | [optional] [readonly] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**sourceId** | **string** |  | [optional] [default to undefined]
**isMigrated** | **boolean** | True for invoices imported via opening balance migration (no finalization JE). | [optional] [default to undefined]
**voidedDate** | **string** |  | [optional] [default to undefined]
**invoiceLabels** | **any** |  | [optional] [default to undefined]
**invoiceLanguage** | **string** |  | [optional] [default to undefined]
**chatId** | **number** |  | [optional] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**client** | **number** |  | [optional] [default to undefined]
**paymentTerm** | **number** |  | [optional] [default to undefined]
**badDebtJournalEntry** | **number** |  | [optional] [readonly] [default to undefined]
**journalEntry** | **number** |  | [optional] [readonly] [default to undefined]
**arAccount** | **number** | Accounts Receivable account for this invoice. Populated for single-AR and migrated invoices. NULL for multi-AR invoices (aging uses ChartTransactions instead). | [optional] [readonly] [default to undefined]
**voidedJournalEntry** | **number** |  | [optional] [readonly] [default to undefined]
**entityTransferJournalEntry** | **number** |  | [optional] [readonly] [default to undefined]
**contract** | **number** |  | [optional] [default to undefined]
**avalaraConnection** | **number** |  | [optional] [default to undefined]
**sphereConnection** | **number** |  | [optional] [default to undefined]
**anrokConnection** | **number** |  | [optional] [default to undefined]
**taxRate** | **number** |  | [optional] [default to undefined]
**stripeConnection** | **number** |  | [optional] [default to undefined]
**sourceFile** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { PatchedAccountingInvoice } from 'campfire-typescript-sdk';

const instance: PatchedAccountingInvoice = {
    id,
    overageAmount,
    lines,
    emails,
    payments,
    relatedJournalEntries,
    paymentJournalEntries,
    journalEntryIntercompany,
    clientName,
    clientCampfireId,
    clientEmail,
    anrokCustomerId,
    clientInvoiceMessage,
    clientUseStripeAutoBill,
    clientIsReseller,
    publicInvoicePaymentUrl,
    status,
    pastDueDays,
    entityName,
    entityCurrency,
    entityInvoiceMessage,
    totalAmount,
    amountPaid,
    amountDue,
    withholdingInfo,
    contractName,
    contractDealId,
    revenueContract,
    revenueContractName,
    revenueContractNumber,
    attachments,
    invoiceNumber,
    stripeConnectionName,
    stripeConnectionEntity,
    stripeConnectionBillingPortalEnabled,
    avalaraConnectionName,
    avalaraConnectionCompany,
    taxRateName,
    taxRateValue,
    paymentTermName,
    revenueTransactions,
    revenueContractInvoice,
    revenueContractLink,
    itemDate,
    migratedJournalId,
    voidedJournalEntryOrder,
    contractCustomFields,
    department,
    departmentName,
    tags,
    lastModifiedAt,
    isDeleted,
    deletedAt,
    chatUuid,
    counterpartyEntity,
    csvUploadRunId,
    csvUploadRowNumber,
    autoSendInvoice,
    autoSendInvoiceAt,
    autoSentAt,
    reminderSentDates,
    preDueReminderSentDates,
    billingAddress,
    billingAddressee,
    shippingAddress,
    shippingAddressee,
    terms,
    refNumber,
    purchaseOrderNumber,
    invoiceDate,
    dueDate,
    shippingDate,
    paidDate,
    uncollectibleDate,
    sentDate,
    periodStart,
    periodEnd,
    locationOfSale,
    messageOnInvoice,
    itaAllocationNumber,
    paymentStatus,
    anrokTransactionId,
    excludeFromTaxConnection,
    warningMessage,
    createdAt,
    currency,
    exchangeRate,
    exchangeRateBook,
    lastSentAt,
    integrationId,
    integrationContext,
    vatNumber,
    vatNumberFromContract,
    shippingAddressFromContract,
    taxExempt,
    discount,
    paymentTermAppliedDiscount,
    useStripeAutoBill,
    stripePaymentLinkId,
    stripePaymentIntentId,
    stripeInvoiceId,
    stripePdfUrl,
    stripePaymentLink,
    source,
    sourceId,
    isMigrated,
    voidedDate,
    invoiceLabels,
    invoiceLanguage,
    chatId,
    customer,
    entity,
    client,
    paymentTerm,
    badDebtJournalEntry,
    journalEntry,
    arAccount,
    voidedJournalEntry,
    entityTransferJournalEntry,
    contract,
    avalaraConnection,
    sphereConnection,
    anrokConnection,
    taxRate,
    stripeConnection,
    sourceFile,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# AccountingInvoiceList

Lightweight serializer for the invoice list endpoint.  Excludes heavy nested fields (emails, payments, attachments, payment_journal_entries) that are only needed on the detail view. Keeps lines for the duplicate invoice action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**overageAmount** | **string** | Invoice-currency overage before tax, as a two-decimal string. | [readonly] [default to undefined]
**lines** | [**Array&lt;AccountingInvoiceLine&gt;**](AccountingInvoiceLine.md) |  | [readonly] [default to undefined]
**journalEntryIntercompany** | **string** |  | [readonly] [default to undefined]
**clientName** | **string** |  | [readonly] [default to undefined]
**clientCampfireId** | **string** |  | [readonly] [default to undefined]
**clientEmail** | **string** |  | [readonly] [default to undefined]
**anrokCustomerId** | **string** |  | [readonly] [default to undefined]
**clientInvoiceMessage** | **string** |  | [readonly] [default to undefined]
**clientUseStripeAutoBill** | **boolean** |  | [readonly] [default to undefined]
**clientIsReseller** | **boolean** |  | [readonly] [default to undefined]
**contractCustomFields** | **Array&lt;{ [key: string]: AccountingInvoiceContractCustomFieldsInnerValue; }&gt;** |  | [readonly] [default to undefined]
**status** | **string** |  | [readonly] [default to undefined]
**pastDueDays** | **number** |  | [readonly] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**entityCurrency** | **string** |  | [readonly] [default to undefined]
**entityInvoiceMessage** | **string** |  | [readonly] [default to undefined]
**totalAmount** | **number** |  | [readonly] [default to undefined]
**amountPaid** | **number** |  | [readonly] [default to undefined]
**amountDue** | **number** |  | [readonly] [default to undefined]
**contractName** | **string** |  | [readonly] [default to undefined]
**revenueContract** | **number** |  | [readonly] [default to undefined]
**revenueContractName** | **string** |  | [readonly] [default to undefined]
**revenueContractNumber** | **string** |  | [readonly] [default to undefined]
**invoiceNumber** | **string** |  | [optional] [default to undefined]
**stripeConnectionName** | **string** |  | [readonly] [default to undefined]
**stripeConnectionEntity** | **number** |  | [readonly] [default to undefined]
**stripeConnectionBillingPortalEnabled** | **boolean** |  | [readonly] [default to undefined]
**avalaraConnectionName** | **string** |  | [readonly] [default to undefined]
**avalaraConnectionCompany** | **string** |  | [readonly] [default to undefined]
**taxRateName** | **string** |  | [readonly] [default to undefined]
**taxRateValue** | **number** |  | [readonly] [default to undefined]
**paymentTermName** | **string** |  | [readonly] [default to undefined]
**revenueTransactions** | **Array&lt;number&gt;** | Write-only. Revenue transaction IDs to link to this invoice. This field is never included in responses. | [optional] [default to undefined]
**itemDate** | **string** |  | [optional] [default to undefined]
**voidedJournalEntryOrder** | **number** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**autoSendInvoice** | **boolean** |  | [optional] [default to undefined]
**autoSendInvoiceAt** | **string** |  | [optional] [default to undefined]
**autoSentAt** | **string** |  | [readonly] [default to undefined]
**reminderSentDates** | **any** | Dictionary tracking when reminders were sent for each day overdue (e.g., {\&#39;5\&#39;: \&#39;2024-01-15\&#39;, \&#39;10\&#39;: \&#39;2024-01-20\&#39;}) | [optional] [default to undefined]
**preDueReminderSentDates** | **any** | Dictionary tracking when pre-due reminders were sent for each day before due date (e.g., {\&#39;3\&#39;: \&#39;2024-01-10\&#39;, \&#39;7\&#39;: \&#39;2024-01-06\&#39;}) | [optional] [default to undefined]
**billingAddress** | **string** |  | [optional] [default to undefined]
**billingAddressee** | **string** |  | [optional] [default to undefined]
**shippingAddress** | **string** |  | [optional] [default to undefined]
**shippingAddressee** | **string** |  | [optional] [default to undefined]
**terms** | [**TermsEnum**](TermsEnum.md) |  | [optional] [default to undefined]
**refNumber** | **string** |  | [optional] [default to undefined]
**purchaseOrderNumber** | **string** |  | [optional] [default to undefined]
**invoiceDate** | **string** |  | [default to undefined]
**dueDate** | **string** |  | [default to undefined]
**shippingDate** | **string** |  | [optional] [default to undefined]
**paidDate** | **string** |  | [optional] [default to undefined]
**uncollectibleDate** | **string** |  | [optional] [default to undefined]
**sentDate** | **string** |  | [readonly] [default to undefined]
**periodStart** | **string** |  | [optional] [default to undefined]
**periodEnd** | **string** |  | [optional] [default to undefined]
**locationOfSale** | **string** |  | [optional] [default to undefined]
**messageOnInvoice** | **string** |  | [optional] [default to undefined]
**itaAllocationNumber** | **string** |  | [optional] [default to undefined]
**paymentStatus** | [**PaymentStatusCdcEnum**](PaymentStatusCdcEnum.md) |  | [optional] [default to undefined]
**anrokTransactionId** | **string** | ID of the transaction in Anrok (set when transaction is created) | [readonly] [default to undefined]
**excludeFromTaxConnection** | **boolean** | When true, no tax is calculated through, and no transaction is created in, the entity\&#39;s tax connection for this invoice. Set at creation; cannot be changed. | [optional] [default to undefined]
**warningMessage** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**lastSentAt** | **string** |  | [readonly] [default to undefined]
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
**stripeInvoiceId** | **string** |  | [optional] [default to undefined]
**stripePdfUrl** | **string** |  | [optional] [default to undefined]
**stripePaymentLink** | **string** |  | [optional] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**sourceId** | **string** |  | [optional] [default to undefined]
**isMigrated** | **boolean** | True for invoices imported via opening balance migration (no finalization JE). | [optional] [default to undefined]
**voidedDate** | **string** |  | [optional] [default to undefined]
**invoiceLabels** | **any** |  | [optional] [default to undefined]
**invoiceLanguage** | **string** |  | [optional] [default to undefined]
**chatId** | **number** |  | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [default to undefined]
**client** | **number** |  | [optional] [default to undefined]
**paymentTerm** | **number** |  | [optional] [default to undefined]
**badDebtJournalEntry** | **number** |  | [optional] [default to undefined]
**journalEntry** | **number** |  | [optional] [default to undefined]
**arAccount** | **number** | Accounts Receivable account for this invoice. Populated for single-AR and migrated invoices. NULL for multi-AR invoices (aging uses ChartTransactions instead). | [optional] [default to undefined]
**voidedJournalEntry** | **number** |  | [optional] [default to undefined]
**entityTransferJournalEntry** | **number** |  | [optional] [default to undefined]
**contract** | **number** |  | [optional] [default to undefined]
**avalaraConnection** | **number** |  | [optional] [default to undefined]
**sphereConnection** | **number** |  | [optional] [default to undefined]
**anrokConnection** | **number** |  | [optional] [default to undefined]
**taxRate** | **number** |  | [optional] [default to undefined]
**stripeConnection** | **number** |  | [optional] [default to undefined]
**sourceFile** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { AccountingInvoiceList } from 'campfire-typescript-sdk';

const instance: AccountingInvoiceList = {
    id,
    overageAmount,
    lines,
    journalEntryIntercompany,
    clientName,
    clientCampfireId,
    clientEmail,
    anrokCustomerId,
    clientInvoiceMessage,
    clientUseStripeAutoBill,
    clientIsReseller,
    contractCustomFields,
    status,
    pastDueDays,
    entityName,
    entityCurrency,
    entityInvoiceMessage,
    totalAmount,
    amountPaid,
    amountDue,
    contractName,
    revenueContract,
    revenueContractName,
    revenueContractNumber,
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
    itemDate,
    voidedJournalEntryOrder,
    lastModifiedAt,
    isDeleted,
    deletedAt,
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

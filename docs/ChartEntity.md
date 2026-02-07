# ChartEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**parentName** | **string** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**name** | **string** |  | [optional] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**invoiceName** | **string** |  | [optional] [default to undefined]
**invoiceEmail** | **string** |  | [optional] [default to undefined]
**address1** | **string** |  | [optional] [default to undefined]
**address2** | **string** |  | [optional] [default to undefined]
**city** | **string** |  | [optional] [default to undefined]
**state** | **string** |  | [optional] [default to undefined]
**zipCode** | **string** |  | [optional] [default to undefined]
**country** | **string** |  | [optional] [default to undefined]
**invoiceMessage** | **string** |  | [optional] [default to undefined]
**invoiceEmailBody** | **string** |  | [optional] [default to undefined]
**invoiceEmailSubject** | **string** |  | [optional] [default to undefined]
**invoicePrefix** | **string** |  | [optional] [default to undefined]
**invoiceAddress** | **string** |  | [optional] [default to undefined]
**invoiceCcEmails** | **string** | Comma-separated list of email addresses to CC when sending invoices from this entity | [optional] [default to undefined]
**disableServiceDate** | **boolean** | When enabled, the Service Date field will be hidden on invoices for this entity | [optional] [default to undefined]
**invoiceDisplaySettings** | **any** | Customization for invoice PDF display (columns, labels). See InvoiceDisplaySettingsSchema for format. | [optional] [default to undefined]
**invoiceEmailAttachments** | **any** | List of PDF attachments for invoice emails. Format: [{\&#39;file_id\&#39;: 123, \&#39;display_name\&#39;: \&#39;Terms\&#39;, \&#39;url\&#39;: \&#39;https://...\&#39;, \&#39;include_as_attachment\&#39;: true}] | [optional] [default to undefined]
**logoUrl** | **string** |  | [optional] [default to undefined]
**active** | **boolean** |  | [optional] [default to undefined]
**fiscalYearMonth** | **number** |  | [optional] [default to undefined]
**fiscalYearDay** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**enableMidMonthConvention** | **boolean** | Override customer-level mid-month convention setting for this entity. Leave blank to inherit from customer. | [optional] [default to undefined]
**midMonthThreshold** | **number** | Override customer-level threshold. Leave blank to inherit from customer. | [optional] [default to undefined]
**useWholeMonthAccountingForPrepaids** | **boolean** | Override customer-level whole-month accounting setting for this entity. Leave blank to inherit from customer. | [optional] [default to undefined]
**lineageArray** | **Array&lt;string&gt;** | Pre-computed lineage array from root to this entity | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**parent** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { ChartEntity } from 'campfire-typescript-sdk';

const instance: ChartEntity = {
    id,
    parentName,
    isDeleted,
    deletedAt,
    lastModifiedAt,
    name,
    description,
    currency,
    invoiceName,
    invoiceEmail,
    address1,
    address2,
    city,
    state,
    zipCode,
    country,
    invoiceMessage,
    invoiceEmailBody,
    invoiceEmailSubject,
    invoicePrefix,
    invoiceAddress,
    invoiceCcEmails,
    disableServiceDate,
    invoiceDisplaySettings,
    invoiceEmailAttachments,
    logoUrl,
    active,
    fiscalYearMonth,
    fiscalYearDay,
    createdAt,
    enableMidMonthConvention,
    midMonthThreshold,
    useWholeMonthAccountingForPrepaids,
    lineageArray,
    customer,
    parent,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

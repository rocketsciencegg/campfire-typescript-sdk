# ChartEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**parent** | **number** |  | [optional] [default to undefined]
**parentName** | **string** |  | [readonly] [default to undefined]
**eliminationEntity** | **number** |  | [optional] [default to undefined]
**primaryEntity** | **number** | When set, this entity is an adjusting entity linked to the specified primary entity. | [optional] [default to undefined]
**primaryEntityName** | **string** |  | [readonly] [default to undefined]
**isAdjusting** | **boolean** |  | [readonly] [default to undefined]
**isEliminationEntity** | **boolean** |  | [optional] [default to false]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**name** | **string** |  | [optional] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**address1** | **string** |  | [optional] [default to undefined]
**address2** | **string** |  | [optional] [default to undefined]
**city** | **string** |  | [optional] [default to undefined]
**state** | **string** |  | [optional] [default to undefined]
**zipCode** | **string** |  | [optional] [default to undefined]
**country** | **string** |  | [optional] [default to undefined]
**email** | **string** | General contact email for the entity. | [optional] [default to undefined]
**phoneNumber** | **string** | General contact phone number for the entity. | [optional] [default to undefined]
**disableServiceDate** | **boolean** | When enabled, the Service Date field will be hidden on invoices for this entity | [optional] [default to undefined]
**logoUrl** | **string** |  | [optional] [default to undefined]
**active** | **boolean** |  | [optional] [default to undefined]
**fiscalYearMonth** | **number** |  | [optional] [default to undefined]
**fiscalYearDay** | **number** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**enableMidMonthConvention** | **boolean** | Override customer-level mid-month convention setting for this entity. Leave blank to inherit from customer. | [optional] [default to undefined]
**midMonthThreshold** | **number** | Override customer-level threshold. Leave blank to inherit from customer. | [optional] [default to undefined]
**useWholeMonthAccountingForPrepaids** | **boolean** | Override customer-level whole-month accounting setting for this entity. Leave blank to inherit from customer. | [optional] [default to undefined]
**allowPaymentsInClosedPeriods** | **boolean** | When enabled, allows applying existing transactions as payments to invoices/bills even when the transaction date falls in a closed subledger period. | [optional] [default to undefined]
**autoApplyCatchupForClosedPeriods** | **boolean** | When enabled, contracts signed after their revenue start month automatically catch up the elapsed revenue into the sign month, floored at the first open period under the close so it never posts to a closed period. Defaults off — flip in entity settings to opt in. | [optional] [default to undefined]
**lineageArray** | **Array&lt;string&gt;** | Pre-computed lineage array from root to this entity | [optional] [default to undefined]
**taxIdentificationNumber** | **string** | Tax ID such as Korean BRN, GST number, or EU VAT number | [optional] [default to undefined]
**sellerTaxRegistrations** | **any** |  | [optional] [default to undefined]
**representativeName** | **string** | Legal representative name | [optional] [default to undefined]
**businessType** | **string** | Business type classification | [optional] [default to undefined]
**businessCategory** | **string** | Business category classification | [optional] [default to undefined]
**invoiceName** | **string** |  | [readonly] [default to undefined]
**invoiceEmail** | **string** |  | [readonly] [default to undefined]
**invoiceMessage** | **string** |  | [readonly] [default to undefined]
**invoiceEmailSubject** | **string** |  | [readonly] [default to undefined]
**invoiceEmailBody** | **string** |  | [readonly] [default to undefined]
**invoicePrefix** | **string** |  | [readonly] [default to undefined]
**invoiceAddress** | **string** |  | [readonly] [default to undefined]
**invoiceCcEmails** | **string** |  | [readonly] [default to undefined]
**invoiceDisplaySettings** | **{ [key: string]: any; }** |  | [readonly] [default to undefined]
**invoiceEmailAttachments** | **{ [key: string]: any; }** |  | [readonly] [default to undefined]
**withholdingScheme** | **number** | Withholding tax regime this entity operates under (e.g. Israel NB, India TDS). A bill resolves its scheme via bill.entity.withholding_scheme. | [optional] [default to undefined]
**withholdingSchemeName** | **string** |  | [readonly] [default to undefined]
**withholdingCertificate** | **number** | This entity\&#39;s own authority-issued certificate (AR side): determines the expected rate customers withhold when paying our invoices under a certificate-based scheme. | [optional] [default to undefined]
**withholdingCertificateNumber** | **string** |  | [readonly] [default to undefined]
**itaDeductionFileNumber** | **string** | Israel tax compliance: ITA withholding deduction file number for Form 856. | [optional] [default to undefined]
**itaPayerStatus** | [**ItaPayerStatusEnum**](ItaPayerStatusEnum.md) | Israel tax compliance: payer status classification for Form 856.  * &#x60;1&#x60; - Company * &#x60;2&#x60; - Individual * &#x60;3&#x60; - Partner * &#x60;4&#x60; - Non-profit * &#x60;5&#x60; - Agency | [optional] [default to undefined]

## Example

```typescript
import { ChartEntity } from 'campfire-typescript-sdk';

const instance: ChartEntity = {
    id,
    customer,
    parent,
    parentName,
    eliminationEntity,
    primaryEntity,
    primaryEntityName,
    isAdjusting,
    isEliminationEntity,
    isDeleted,
    deletedAt,
    lastModifiedAt,
    name,
    description,
    currency,
    address1,
    address2,
    city,
    state,
    zipCode,
    country,
    email,
    phoneNumber,
    disableServiceDate,
    logoUrl,
    active,
    fiscalYearMonth,
    fiscalYearDay,
    createdAt,
    enableMidMonthConvention,
    midMonthThreshold,
    useWholeMonthAccountingForPrepaids,
    allowPaymentsInClosedPeriods,
    autoApplyCatchupForClosedPeriods,
    lineageArray,
    taxIdentificationNumber,
    sellerTaxRegistrations,
    representativeName,
    businessType,
    businessCategory,
    invoiceName,
    invoiceEmail,
    invoiceMessage,
    invoiceEmailSubject,
    invoiceEmailBody,
    invoicePrefix,
    invoiceAddress,
    invoiceCcEmails,
    invoiceDisplaySettings,
    invoiceEmailAttachments,
    withholdingScheme,
    withholdingSchemeName,
    withholdingCertificate,
    withholdingCertificateNumber,
    itaDeductionFileNumber,
    itaPayerStatus,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

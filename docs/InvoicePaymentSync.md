# InvoicePaymentSync


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**invoiceId** | **number** |  | [readonly] [default to undefined]
**invoiceNumber** | **string** |  | [readonly] [default to undefined]
**amount** | **number** |  | [readonly] [default to undefined]
**currency** | **string** |  | [readonly] [default to undefined]
**paymentDate** | **string** |  | [readonly] [default to undefined]
**paymentType** | [**PaymentTypeEnum**](PaymentTypeEnum.md) | Type of payment: credit memo application, bank transaction, or manual transaction  * &#x60;CREDIT_MEMO&#x60; - Credit Memo * &#x60;BANK_TRANSACTION&#x60; - Bank Transaction * &#x60;MANUAL_TRANSACTION&#x60; - Manual Transaction | [readonly] [default to undefined]
**source** | [**Source47fEnum**](Source47fEnum.md) |  | [readonly] [default to undefined]
**externalId** | **string** | Stable upstream identifier for this payment (e.g. Stripe balance transaction \&#39;btxn_...\&#39;, Stripe credit note \&#39;cn_...\&#39;, or the mart\&#39;s event external_id for customer-balance applications). Used as the natural dedup/idempotency key. Null for manually-entered payments. | [readonly] [default to undefined]
**voidedDate** | **string** |  | [readonly] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]

## Example

```typescript
import { InvoicePaymentSync } from 'campfire-typescript-sdk';

const instance: InvoicePaymentSync = {
    id,
    invoiceId,
    invoiceNumber,
    amount,
    currency,
    paymentDate,
    paymentType,
    source,
    externalId,
    voidedDate,
    createdAt,
    lastModifiedAt,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

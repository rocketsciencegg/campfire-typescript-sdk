# RevenueTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**entityCurrency** | **string** |  | [readonly] [default to undefined]
**clientName** | **string** |  | [readonly] [default to undefined]
**contractName** | **string** |  | [readonly] [default to undefined]
**productName** | **string** |  | [readonly] [default to undefined]
**productBundleName** | **string** |  | [readonly] [default to undefined]
**productIsTaxable** | **boolean** |  | [readonly] [default to undefined]
**contractIdentifier** | **string** |  | [readonly] [default to undefined]
**clientIdentifier** | **string** |  | [readonly] [default to undefined]
**productIdentifier** | **string** |  | [readonly] [default to undefined]
**grossAmount** | **string** |  | [readonly] [default to undefined]
**invoiceNumber** | **string** |  | [readonly] [default to undefined]
**invoiceDate** | **string** |  | [readonly] [default to undefined]
**invoicePaymentStatus** | **string** |  | [readonly] [default to undefined]
**invoiceVoidedDate** | **string** |  | [readonly] [default to undefined]
**revenueType** | **string** |  | [readonly] [default to undefined]
**journalEntryOrder** | **string** |  | [readonly] [default to undefined]
**contractSubscriptionNotes** | **string** |  | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**parentDepartmentName** | **string** |  | [readonly] [default to undefined]
**parentDepartment** | **number** |  | [readonly] [default to undefined]
**tags** | **string** |  | [optional] [default to undefined]
**usageTierName** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**anrokItemId** | **string** |  | [readonly] [default to undefined]
**sphereItemId** | **string** |  | [readonly] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**description** | **string** |  | [optional] [default to undefined]
**externalId** | **string** |  | [optional] [default to undefined]
**clientExternalId** | **string** |  | [optional] [default to undefined]
**contractExternalId** | **string** |  | [optional] [default to undefined]
**contractSubscriptionExternalId** | **string** |  | [optional] [default to undefined]
**productExternalId** | **string** |  | [optional] [default to undefined]
**accountingPeriod** | **string** |  | [optional] [default to undefined]
**transactionDate** | **string** |  | [optional] [default to undefined]
**transactionEndDate** | **string** |  | [optional] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**recognized** | **number** |  | [optional] [default to undefined]
**amount** | **number** |  | [optional] [default to undefined]
**quantity** | **number** |  | [optional] [default to undefined]
**rate** | **number** |  | [optional] [default to undefined]
**discount** | **number** |  | [optional] [default to undefined]
**refunds** | **number** |  | [optional] [default to undefined]
**processingFees** | **number** |  | [optional] [default to undefined]
**platformFees** | **number** |  | [optional] [default to undefined]
**transfers** | **number** |  | [optional] [default to undefined]
**tax** | **number** |  | [optional] [default to undefined]
**balanceAdjustment** | **number** | Invoice starting balance or other balance adjustments (e.g., previous balance applied to this transaction) | [optional] [default to undefined]
**mrr** | **number** |  | [optional] [default to undefined]
**renewall** | **boolean** |  | [optional] [default to undefined]
**isMigrationInvoiced** | **boolean** | Marked as invoiced during migration. Does not create GL entries or AR. | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**client** | **number** |  | [optional] [default to undefined]
**contract** | **number** |  | [optional] [default to undefined]
**contractSubscription** | **number** |  | [optional] [default to undefined]
**nonContractSubscription** | **number** |  | [optional] [default to undefined]
**contractUsage** | **number** |  | [optional] [default to undefined]
**contractMilestone** | **number** |  | [optional] [default to undefined]
**nonContractUsage** | **number** |  | [optional] [default to undefined]
**product** | **number** |  | [optional] [default to undefined]
**productBundle** | **number** |  | [optional] [default to undefined]
**contractProductBundle** | **number** | Reference to contract-specific editable product bundle allocation | [optional] [default to undefined]
**contractBundle** | **number** |  | [optional] [default to undefined]
**journalEntry** | **number** |  | [optional] [default to undefined]
**invoice** | **number** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**usageTier** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { RevenueTransaction } from 'campfire-typescript-sdk';

const instance: RevenueTransaction = {
    id,
    isDeleted,
    deletedAt,
    entityName,
    entityCurrency,
    clientName,
    contractName,
    productName,
    productBundleName,
    productIsTaxable,
    contractIdentifier,
    clientIdentifier,
    productIdentifier,
    grossAmount,
    invoiceNumber,
    invoiceDate,
    invoicePaymentStatus,
    invoiceVoidedDate,
    revenueType,
    journalEntryOrder,
    contractSubscriptionNotes,
    departmentName,
    parentDepartmentName,
    parentDepartment,
    tags,
    usageTierName,
    lastModifiedAt,
    anrokItemId,
    sphereItemId,
    source,
    description,
    externalId,
    clientExternalId,
    contractExternalId,
    contractSubscriptionExternalId,
    productExternalId,
    accountingPeriod,
    transactionDate,
    transactionEndDate,
    currency,
    exchangeRate,
    exchangeRateBook,
    recognized,
    amount,
    quantity,
    rate,
    discount,
    refunds,
    processingFees,
    platformFees,
    transfers,
    tax,
    balanceAdjustment,
    mrr,
    renewall,
    isMigrationInvoiced,
    createdAt,
    customer,
    entity,
    client,
    contract,
    contractSubscription,
    nonContractSubscription,
    contractUsage,
    contractMilestone,
    nonContractUsage,
    product,
    productBundle,
    contractProductBundle,
    contractBundle,
    journalEntry,
    invoice,
    department,
    usageTier,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

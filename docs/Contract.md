# Contract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**clientName** | **string** |  | [readonly] [default to undefined]
**clientTerms** | **string** |  | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**parentDepartmentName** | **string** |  | [readonly] [default to undefined]
**parentDepartment** | **number** |  | [readonly] [default to undefined]
**tags** | **string** |  | [optional] [default to undefined]
**totalRevenue** | **number** |  | [readonly] [default to undefined]
**totalMrr** | **number** |  | [readonly] [default to undefined]
**totalBilled** | **number** |  | [readonly] [default to undefined]
**totalUnbilled** | **number** |  | [readonly] [default to undefined]
**totalPaid** | **number** |  | [readonly] [default to undefined]
**totalOutstanding** | **number** |  | [readonly] [default to undefined]
**totalDeferredRevenue** | **number** |  | [readonly] [default to undefined]
**currency** | **string** |  | [optional] [default to 'USD']
**entityCurrency** | **string** |  | [optional] [default to 'USD']
**attachments** | **Array&lt;any&gt;** |  | [readonly] [default to undefined]
**contractEndDate** | **string** |  | [optional] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**isDeleted** | **string** |  | [readonly] [default to undefined]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**usageTiers** | **string** |  | [optional] [default to undefined]
**hasInvoices** | **boolean** |  | [readonly] [default to false]
**hasJournalEntries** | **boolean** |  | [readonly] [default to false]
**hasCreditMemos** | **boolean** |  | [readonly] [default to false]
**searchVector** | **string** |  | [readonly] [default to undefined]
**searchText** | **string** |  | [readonly] [default to undefined]
**billingFrequency** | [**BillingFrequencyEnum**](BillingFrequencyEnum.md) |  | [optional] [default to undefined]
**dealName** | **string** |  | [optional] [default to undefined]
**dealId** | **string** |  | [optional] [default to undefined]
**consultant** | **string** |  | [optional] [default to undefined]
**closedDate** | **string** |  | [optional] [default to undefined]
**totalContractValue** | **number** |  | [optional] [default to undefined]
**contractStartDate** | **string** |  | [optional] [default to undefined]
**exchangeRate** | **number** |  | [optional] [default to undefined]
**exchangeRateBook** | **number** |  | [optional] [default to undefined]
**crmLink** | **string** |  | [optional] [default to undefined]
**contractLink** | **string** |  | [optional] [default to undefined]
**status** | [**ContractStatusEnum**](ContractStatusEnum.md) |  | [optional] [default to undefined]
**source** | [**ContractSourceEnum**](ContractSourceEnum.md) |  | [optional] [default to undefined]
**sourceDealData** | **any** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**autoRenew** | **boolean** |  | [optional] [default to undefined]
**autoRenewDuration** | **number** |  | [optional] [default to undefined]
**autoRenewInvoice** | **boolean** |  | [optional] [default to undefined]
**minimumMonthlyCommitmentAmount** | **number** | Minimum monthly commitment amount (allowance threshold) | [optional] [default to undefined]
**minimumMonthlyCommitmentQuantity** | **number** | Minimum monthly commitment quantity (allowance threshold in units) | [optional] [default to undefined]
**purchaseOrderNumber** | **string** |  | [optional] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**client** | **number** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**journalEntries** | **Array&lt;number&gt;** |  | [optional] [default to undefined]

## Example

```typescript
import { Contract } from 'campfire-typescript-sdk';

const instance: Contract = {
    id,
    entityName,
    clientName,
    clientTerms,
    departmentName,
    parentDepartmentName,
    parentDepartment,
    tags,
    totalRevenue,
    totalMrr,
    totalBilled,
    totalUnbilled,
    totalPaid,
    totalOutstanding,
    totalDeferredRevenue,
    currency,
    entityCurrency,
    attachments,
    contractEndDate,
    lastModifiedAt,
    isDeleted,
    deletedAt,
    usageTiers,
    hasInvoices,
    hasJournalEntries,
    hasCreditMemos,
    searchVector,
    searchText,
    billingFrequency,
    dealName,
    dealId,
    consultant,
    closedDate,
    totalContractValue,
    contractStartDate,
    exchangeRate,
    exchangeRateBook,
    crmLink,
    contractLink,
    status,
    source,
    sourceDealData,
    createdAt,
    autoRenew,
    autoRenewDuration,
    autoRenewInvoice,
    minimumMonthlyCommitmentAmount,
    minimumMonthlyCommitmentQuantity,
    purchaseOrderNumber,
    customer,
    entity,
    client,
    department,
    journalEntries,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

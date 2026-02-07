# ContractCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**contacts** | [**Array&lt;VendorContact&gt;**](VendorContact.md) |  | [optional] [default to undefined]
**parentName** | **string** |  | [readonly] [default to undefined]
**stripeConnectionName** | **string** |  | [readonly] [default to undefined]
**stripeConnectionEntity** | **number** |  | [readonly] [default to undefined]
**stripeConnectionPortalUrl** | **string** |  | [readonly] [default to undefined]
**stripeConnectionPortalEnabled** | **boolean** |  | [readonly] [default to undefined]
**stripeConnectionInvoicingEnabled** | **boolean** |  | [readonly] [default to undefined]
**vendorCustomField1Name** | **string** |  | [readonly] [default to undefined]
**paymentTermNameDisplay** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**activeContracts** | **number** |  | [readonly] [default to undefined]
**completedContracts** | **number** |  | [readonly] [default to undefined]
**pendingContracts** | **number** |  | [readonly] [default to undefined]
**totalContracts** | **number** |  | [readonly] [default to undefined]
**totalRevenue** | **number** |  | [readonly] [default to undefined]
**totalDeferredRevenue** | **number** |  | [readonly] [default to undefined]
**totalMrr** | **number** |  | [readonly] [default to undefined]
**totalBilled** | **number** |  | [readonly] [default to undefined]
**totalUnbilled** | **number** |  | [readonly] [default to undefined]
**totalPaid** | **number** |  | [readonly] [default to undefined]
**totalOutstanding** | **number** |  | [readonly] [default to undefined]
**totalCreditMemos** | **number** |  | [readonly] [default to undefined]
**creditMemoApplied** | **number** |  | [readonly] [default to undefined]
**creditMemoAvailable** | **number** |  | [readonly] [default to undefined]
**currency** | **string** |  | [readonly] [default to undefined]
**searchVector** | **string** |  | [readonly] [default to undefined]
**searchText** | **string** |  | [readonly] [default to undefined]
**vendorType** | [**VendorType391Enum**](VendorType391Enum.md) |  | [optional] [default to undefined]
**name** | **string** |  | [default to undefined]
**dba** | **string** |  | [optional] [default to undefined]
**companyName** | **string** |  | [optional] [default to undefined]
**website** | **string** |  | [optional] [default to undefined]
**firstName** | **string** |  | [optional] [default to undefined]
**lastName** | **string** |  | [optional] [default to undefined]
**email** | **string** |  | [optional] [default to undefined]
**phoneNumber** | **string** |  | [optional] [default to undefined]
**mobileNumber** | **string** |  | [optional] [default to undefined]
**addressStreet1** | **string** |  | [optional] [default to undefined]
**addressStreet2** | **string** |  | [optional] [default to undefined]
**city** | **string** |  | [optional] [default to undefined]
**state** | **string** |  | [optional] [default to undefined]
**zipCode** | **string** |  | [optional] [default to undefined]
**country** | **string** |  | [optional] [default to undefined]
**billingAddressStreet1** | **string** |  | [optional] [default to undefined]
**billingAddressStreet2** | **string** |  | [optional] [default to undefined]
**billingCity** | **string** |  | [optional] [default to undefined]
**billingState** | **string** |  | [optional] [default to undefined]
**billingZipCode** | **string** |  | [optional] [default to undefined]
**billingCountry** | **string** |  | [optional] [default to undefined]
**shippingAddressee** | **string** |  | [optional] [default to undefined]
**billingAddressee** | **string** |  | [optional] [default to undefined]
**notes** | **string** |  | [optional] [default to undefined]
**businessIdSsn** | **string** |  | [optional] [default to undefined]
**is1099** | **boolean** |  | [optional] [default to undefined]
**vatNumber** | **string** |  | [optional] [default to undefined]
**entityUseCode** | **string** | Avalara entity/use code for tax exemptions (e.g., A - Federal Government, B - State/Local Govt) | [optional] [default to undefined]
**stripeCustomerId** | **string** |  | [optional] [default to undefined]
**useStripeAutoBill** | **boolean** |  | [optional] [default to undefined]
**billVendorId** | **string** |  | [optional] [default to undefined]
**externalId** | **string** |  | [optional] [default to undefined]
**source** | [**Source170Enum**](Source170Enum.md) |  | [optional] [default to undefined]
**invoiceMessage** | **string** |  | [optional] [default to undefined]
**abbreviation** | **string** |  | [optional] [default to undefined]
**createdAt** | **string** |  | [readonly] [default to undefined]
**status** | [**Status372Enum**](Status372Enum.md) |  | [optional] [default to undefined]
**anrokCustomerId** | **string** |  | [optional] [default to undefined]
**terms** | [**TermsEnum**](TermsEnum.md) |  | [optional] [default to undefined]
**lineageArray** | **Array&lt;string&gt;** | Pre-computed lineage array from root to this vendor | [optional] [default to undefined]
**customer** | **number** |  | [default to undefined]
**parent** | **number** |  | [optional] [default to undefined]
**stripeConnection** | **number** |  | [default to undefined]
**defaultExpenseCategory** | **number** |  | [optional] [default to undefined]
**vendorCustomField1** | **number** |  | [optional] [default to undefined]
**paymentTerm** | **number** | Payment term for this vendor | [optional] [default to undefined]

## Example

```typescript
import { ContractCustomer } from 'campfire-typescript-sdk';

const instance: ContractCustomer = {
    id,
    contacts,
    parentName,
    stripeConnectionName,
    stripeConnectionEntity,
    stripeConnectionPortalUrl,
    stripeConnectionPortalEnabled,
    stripeConnectionInvoicingEnabled,
    vendorCustomField1Name,
    paymentTermNameDisplay,
    lastModifiedAt,
    isDeleted,
    deletedAt,
    activeContracts,
    completedContracts,
    pendingContracts,
    totalContracts,
    totalRevenue,
    totalDeferredRevenue,
    totalMrr,
    totalBilled,
    totalUnbilled,
    totalPaid,
    totalOutstanding,
    totalCreditMemos,
    creditMemoApplied,
    creditMemoAvailable,
    currency,
    searchVector,
    searchText,
    vendorType,
    name,
    dba,
    companyName,
    website,
    firstName,
    lastName,
    email,
    phoneNumber,
    mobileNumber,
    addressStreet1,
    addressStreet2,
    city,
    state,
    zipCode,
    country,
    billingAddressStreet1,
    billingAddressStreet2,
    billingCity,
    billingState,
    billingZipCode,
    billingCountry,
    shippingAddressee,
    billingAddressee,
    notes,
    businessIdSsn,
    is1099,
    vatNumber,
    entityUseCode,
    stripeCustomerId,
    useStripeAutoBill,
    billVendorId,
    externalId,
    source,
    invoiceMessage,
    abbreviation,
    createdAt,
    status,
    anrokCustomerId,
    terms,
    lineageArray,
    customer,
    parent,
    stripeConnection,
    defaultExpenseCategory,
    vendorCustomField1,
    paymentTerm,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

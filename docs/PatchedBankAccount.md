# PatchedBankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [optional] [readonly] [default to false]
**deletedAt** | **string** |  | [optional] [readonly] [default to undefined]
**entityName** | **string** |  | [optional] [readonly] [default to undefined]
**departmentName** | **string** |  | [optional] [readonly] [default to undefined]
**chartOfAccountsAccountName** | **string** |  | [optional] [readonly] [default to undefined]
**accountType** | **string** |  | [optional] [readonly] [default to undefined]
**accountSubtype** | **string** |  | [optional] [readonly] [default to undefined]
**accountCashflowClassification** | **string** |  | [optional] [readonly] [default to undefined]
**typeName** | **string** |  | [optional] [readonly] [default to undefined]
**subtypeName** | **string** |  | [optional] [readonly] [default to undefined]
**cashflowClassificationName** | **string** |  | [optional] [readonly] [default to undefined]
**accountId** | **string** |  | [optional] [readonly] [default to undefined]
**currency** | **string** |  | [optional] [default to undefined]
**externalAccountId** | **string** |  | [optional] [default to undefined]
**name** | **string** |  | [optional] [default to undefined]
**nickname** | **string** |  | [optional] [default to undefined]
**status** | **string** |  | [optional] [default to undefined]
**type** | [**BankAccountTypeEnum**](BankAccountTypeEnum.md) |  | [optional] [default to undefined]
**availableBalance** | **number** |  | [optional] [default to undefined]
**currentBalance** | **number** |  | [optional] [default to undefined]
**institutionId** | **string** |  | [optional] [default to undefined]
**source** | **string** |  | [optional] [default to undefined]
**abaRoutingNumber** | **string** | ABA routing number (9 digits) for US bank accounts | [optional] [default to undefined]
**swiftBic** | **string** | SWIFT BIC code (8 or 11 characters) for international accounts | [optional] [default to undefined]
**createdAt** | **string** |  | [optional] [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [optional] [readonly] [default to undefined]
**customer** | **number** |  | [optional] [readonly] [default to undefined]
**entity** | **number** |  | [optional] [default to undefined]
**chartOfAccountsAccount** | **number** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**tags** | **Array&lt;number&gt;** |  | [optional] [readonly] [default to undefined]

## Example

```typescript
import { PatchedBankAccount } from 'campfire-typescript-sdk';

const instance: PatchedBankAccount = {
    id,
    isDeleted,
    deletedAt,
    entityName,
    departmentName,
    chartOfAccountsAccountName,
    accountType,
    accountSubtype,
    accountCashflowClassification,
    typeName,
    subtypeName,
    cashflowClassificationName,
    accountId,
    currency,
    externalAccountId,
    name,
    nickname,
    status,
    type,
    availableBalance,
    currentBalance,
    institutionId,
    source,
    abaRoutingNumber,
    swiftBic,
    createdAt,
    lastModifiedAt,
    customer,
    entity,
    chartOfAccountsAccount,
    department,
    tags,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

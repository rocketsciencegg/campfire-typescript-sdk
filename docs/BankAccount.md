# BankAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [readonly] [default to undefined]
**isDeleted** | **boolean** |  | [readonly] [default to false]
**deletedAt** | **string** |  | [readonly] [default to undefined]
**entityName** | **string** |  | [readonly] [default to undefined]
**departmentName** | **string** |  | [readonly] [default to undefined]
**chartOfAccountsAccountName** | **string** |  | [readonly] [default to undefined]
**accountType** | **string** |  | [readonly] [default to undefined]
**accountSubtype** | **string** |  | [readonly] [default to undefined]
**accountCashflowClassification** | **string** |  | [readonly] [default to undefined]
**typeName** | **string** |  | [readonly] [default to undefined]
**subtypeName** | **string** |  | [readonly] [default to undefined]
**cashflowClassificationName** | **string** |  | [readonly] [default to undefined]
**accountId** | **string** |  | [readonly] [default to undefined]
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
**createdAt** | **string** |  | [readonly] [default to undefined]
**lastModifiedAt** | **string** |  | [readonly] [default to undefined]
**customer** | **number** |  | [readonly] [default to undefined]
**entity** | **number** |  | [default to undefined]
**chartOfAccountsAccount** | **number** |  | [optional] [default to undefined]
**department** | **number** |  | [optional] [default to undefined]
**tags** | **Array&lt;number&gt;** |  | [readonly] [default to undefined]

## Example

```typescript
import { BankAccount } from 'campfire-typescript-sdk';

const instance: BankAccount = {
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

# Create Bank Account Number API

Generate a permanent virtual bank account number linked to your wallet/account for secure payments.

## Endpoint
`POST https://api.moolre.com/open/account/create`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-USER | string | Yes | Your Moolre username. |
| X-API-PUBKEY | string | Yes | Your Public API Key. *(Not required in Sandbox)* |

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 9. |
| currency | string | Yes | Currency code (e.g., GHS). |
| amount | number | No | Optional initial amount. |
| firstname | string | Yes | First name of the account holder. |
| lastname | string | Yes | Last name of the account holder. |
| phone | string | Yes | Phone number of the account holder. |
| email | string | Yes | Email address of the account holder. |
| uref | string | Yes | Unique request reference. |
| accountnumber | string | Yes | Your Moolre Account Number. |

## Responses
### 200 - Success
Bank account number created successfully.

```json
{
  "status": 1,
  "code": "AD19",
  "message": "Account No. Creation Successful",
  "data": {
    "accountno": "0014730001001",
    "accountname": "Kofi Adeniyi3 MoolrePay",
    "bankname": "First Atlantic Bank",
    "uref": "uref001"
  },
  "go": null
}
```

### 400 (Duplicate Name) - Failed
Bank account creation failed because the name is already in use.

```json
{
  "status": 0,
  "code": "AD32",
  "message": "Account No. Creation Failed",
  "data": "all",
  "go": null
}
```


# Payment Webhook API

Moolre sends real-time HTTP POST notifications (callbacks) to your server when a payment is received or its status changes.

## Endpoint
`POST {{YOUR_CALLBACK_URL}}`

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| status | integer | Yes | 1 for success |
| code | string | Yes | P01 |
| message | string | Yes | Transaction Successful |
| data | object | Yes | The transaction details |

## Responses

---
name: moolre-docs
description: Moolre API reference — SMS, WhatsApp, accounts, payments, transfers, USSD, webhooks. Use when the user asks about any Moolre endpoint, wants to send SMS/WhatsApp via Moolre, create or check Moolre accounts, initiate payments or transfers, generate payment links, check transaction status, integrate USSD, handle webhooks, look up bank lists or miscellaneous data, or debug Moolre API calls. Also use when working on the Smashup backend's Moolre integration.
---

# Moolre API Reference

Complete Moolre API documentation organized by domain. Instead of loading all 28 docs at once, route to the specific reference file based on what the user is asking about.

## Environments

- **Live**: `https://api.moolre.com`
- **Sandbox**: `https://sandbox.moolre.com` (no `X-API-KEY` or `X-API-PUBKEY` needed; only `X-API-USER` required)

## Authentication Headers

| Header | When Required |
|---|---|
| `X-API-USER` | All endpoints |
| `X-API-KEY` | Live environment (not sandbox) |
| `X-API-PUBKEY` | Live environment (not sandbox) |
| `X-API-VASKEY` | SMS and WhatsApp endpoints only |

## Routing Table

When the user asks about a specific Moolre operation, read ONLY the relevant reference file(s). Do NOT load all files.

### SMS
| User asks about… | Read this file |
|---|---|
| Sending SMS (POST) | `references/sms/send-sms.md` |
| Sending SMS (GET) | `references/sms/send-sms-get.md` |
| Checking SMS delivery status | `references/sms/sms-status.md` |
| Creating a sender ID | `references/sms/create-sender-id.md` |
| Checking sender ID approval status | `references/sms/sender-id-status.md` |
| SMS account balance / status | `references/sms/sms-account-status.md` |
| Any general SMS question | Read all files in `references/sms/` |

### WhatsApp
| User asks about… | Read this file |
|---|---|
| Getting WhatsApp templates | `references/whatsapp/whatsapp-get-templates.md` |
| Sending WhatsApp messages | `references/whatsapp/whatsapp-send-message.md` |
| Checking WhatsApp message status | `references/whatsapp/whatsapp-message-status.md` |
| Any general WhatsApp question | Read all files in `references/whatsapp/` |

### Accounts
| User asks about… | Read this file |
|---|---|
| Creating a business wallet/account | `references/accounts/create-account.md` |
| Updating an existing account | `references/accounts/update-account.md` |
| Checking account status | `references/accounts/account-status.md` |
| Listing account transactions | `references/accounts/list-account-transactions.md` |
| Validating an account name | `references/accounts/validate-name.md` |
| Creating a bank account number | `references/accounts/create-bank-account-number.md` |
| Any general account question | Read all files in `references/accounts/` |

### Payments
| User asks about… | Read this file |
|---|---|
| Initiating a USSD payment request | `references/payments/initiate-payment.md` |
| Checking payment status | `references/payments/payment-status.md` |
| Creating a payment ID | `references/payments/create-payment-id.md` |
| Generating a payment link | `references/payments/generate-payment-link.md` |
| Any general payment question | Read all files in `references/payments/` |

### Transfers
| User asks about… | Read this file |
|---|---|
| Initiating a bank transfer | `references/transfers/initiate-transfer.md` |
| Checking transfer status | `references/transfers/transfer-status.md` |
| Internal wallet-to-wallet transfer | `references/transfers/internal-transfer.md` |
| Any general transfer question | Read all files in `references/transfers/` |

### Webhooks
| User asks about… | Read this file |
|---|---|
| Payment webhook callbacks | `references/webhooks/payment-webhook.md` |

### USSD
| User asks about… | Read this file |
|---|---|
| USSD integration (`*203#`) | `references/ussd/ussd-integration.md` |

### Meta / Miscellaneous
| User asks about… | Read this file |
|---|---|
| Bank lists, mobile money networks, sublist IDs | `references/meta/miscellaneous-data.md` |
| Full API reference (all endpoints at once) | `references/meta/llms-full.txt` |

## How to Use This Skill

1. **Identify the domain** from the user's query — are they asking about SMS, payments, accounts, etc.?
2. **Read only the relevant reference file(s)** using the routing table above. Do NOT load all files.
3. **Answer the question** using the endpoint details (URL, method, headers, request params, response examples) from the reference file.
4. If the user's query spans multiple domains (e.g., "create an account then send an SMS"), read the files for each domain sequentially.

## Common Patterns

- All POST endpoints require `type: 1` as a parameter unless otherwise noted.
- Payment channels: `13` = MTN, `6` = Telecel, `7` = AT.
- Currency codes are 3-letter ISO (e.g., `GHS`).
- `externalref` must be unique per payment — duplicates return 400.
- Sandbox skips `X-API-KEY` and `X-API-PUBKEY` but still needs `X-API-USER`.
- SMS/WhatsApp always need `X-API-VASKEY` regardless of environment.
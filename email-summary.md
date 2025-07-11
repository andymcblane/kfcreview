# New KFC Review Emails

This PR contains new emails synced from the kfcreview-emails S3 bucket.

**📧 Email files added:**
- `6mreeh9v8vp0b1cj656h8dqfmhavt24p8coap4g1`

---

# Email Sync Summary

**Total emails:** 1

**Processed:** 2025-07-11 14:19:26 UTC

---

# Email: `6mreeh9v8vp0b1cj656h8dqfmhavt24p8coap4g1`

## Email Headers

**From:** `Andy McBlane <andymcblane@hotmail.com>`

**To:** `"zingerpie@kfcreview.com" <zingerpie@kfcreview.com>`

**Subject:** `❄️❄️`

**Date:** `Fri, 11 Jul 2025 14:19:10 +0000`

**Message-ID:** `<SYZP282MB3192D7A35FBC3F5818477CD2B74BA@SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM>`

<details>
<summary>Additional Headers</summary>

**Return-Path:** `<andymcblane@hotmail.com>`

**Received:** `from SY5PR01CU010.outbound.protection.outlook.com (mail-australiaeastazolkn19012051.outbound.protection.outlook.com [52.103.72.51]) by inbound-smtp.us-east-2.amazonaws.com with SMTP id 6mreeh9v8vp0b1cj656h8dqfmhavt24p8coap4g1 for zingerpie@kfcreview.com; Fri, 11 Jul 2025 14:19:14 +0000 (UTC)`

**Received-SPF:** `pass (spfCheck: domain of hotmail.com designates 52.103.72.51 as permitted sender) client-ip=52.103.72.51; envelope-from=andymcblane@hotmail.com; helo=SY5PR01CU010.outbound.protection.outlook.com;`

**Authentication-Results:** `amazonses.com; spf=pass (spfCheck: domain of hotmail.com designates 52.103.72.51 as permitted sender) client-ip=52.103.72.51; envelope-from=andymcblane@hotmail.com; helo=SY5PR01CU010.outbound.protection.outlook.com; dkim=pass header.i=@hotmail.com; dmarc=pass header.from=hotmail.com;`

**ARC-Seal:** `i=1; a=rsa-sha256; s=arcselector10001; d=microsoft.com; cv=none; b=Pxixb65v9MAWgoSiUYKWzr+nk4EZ0Qbq0p42AZgisHrgc3KSs1kcgR4buPJyg/phOGjajt7jv2lqJbEpwn2oIDRNhoU/RzAWBBAuFkqFJC6sqA+J1v5QJ7XPnqBL2s1EOEl7MokE1ejrDN/TeLdCzCitYNREFBpls1EgH0HrG8Ldx5Gq0ffrFeatYFyCPzRGf6AQFLhzKJYvugVmfq1jDkuRTHllgRrj/34saf8+dfMDUJm+G8TLPHKehMR+xib44Ey87h3hY/sciTSvd6v2bC5uafq5h/8W62ilQ8Ge1pwZ1c2AmTFyBRKK8N975miTdANI5T6K1f1Uc8ZrIeNaIA==`

**ARC-Message-Signature:** `i=1; a=rsa-sha256; c=relaxed/relaxed; d=microsoft.com; s=arcselector10001; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-AntiSpam-MessageData-ChunkCount:X-MS-Exchange-AntiSpam-MessageData-0:X-MS-Exchange-AntiSpam-MessageData-1; bh=OVtwxNywxcRT+nQpIox4b3Cv3nNgiT5SJlFyKkfMQC0=; b=TqXPbS1doonK/FtsH131kLDcwlcgAwRipFlnE4cB8EtokMCv/x4L4KlmotLtnTbtRCa0QnY/RP5H55lP+D4jH8DqcQTgPEurL9/QyxWLDJBKA1Ep76+1wFCFPDvAJ1BF1Obu6y7vIXudI672p+s+3MT+HwMbtase7zisK9p+lXvSASSUXAyTuQPBpgrlU7a8/gHI+PB6lafNTfYwqcO8mFtQjKla7eUlpGsVFj/dPhXvCgvQO/zRohV5RfYxutb3UYi7Vr191tnfEjRDaVPi36DEvuyu9/2MJGj8S031hgGYeYa7zC9G7w0zhnWRCQNDT5KZAb4GUzndEjIJ8mwi3g==`

**ARC-Authentication-Results:** `i=1; mx.microsoft.com 1; spf=none; dmarc=none; dkim=none; arc=none`

**DKIM-Signature:** `v=1; a=rsa-sha256; c=relaxed/relaxed; d=hotmail.com; s=selector1; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-SenderADCheck; bh=OVtwxNywxcRT+nQpIox4b3Cv3nNgiT5SJlFyKkfMQC0=; b=PUbtXC41w7dge2Isl9QIXEld6SeDsGTUd2Vh/RHgeDTrttkfM+f+Fqk8PKfS49Sk1Lls0mJ0eqyhKbqdd8NklX/1jlGZ1bUyVI8G6XfhncX2K5vnP0RA3m7DcvTSFkR5+geZz5EDjaXRglBtETXbNR1p3HsXTAiFoVPqmVsH7ud6WgQeQsPPziQRhTBx+ZdWJEhxy6zLCxJAHaOafm7ISasA3HruShQUxG/YnfWxqgM25VNBlFZ4xiLMHn7B9t+uS2VXNQ11tb9W+5jMyUKOZ1oIRxdLMp4CTiDCVlUEI+VVuR1F7qj4CMhzOh4pV1vfb8cvp3FNvl8IJgSPzDPq+w==`

**Received:** `from SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM (2603:10c6:10:169::23) by SY6P282MB3992.AUSP282.PROD.OUTLOOK.COM (2603:10c6:10:1db::5) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.8901.29; Fri, 11 Jul 2025 14:19:10 +0000`

**Received:** `from SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM ([fe80::7120:3e8c:eb6b:4104]) by SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM ([fe80::7120:3e8c:eb6b:4104%7]) with mapi id 15.20.8922.023; Fri, 11 Jul 2025 14:19:10 +0000`

**Thread-Topic:** `❄️❄️`

**Thread-Index:** `AQHb8m7Fc3wJR/UYckG9oyzJWmstgg==`

**Accept-Language:** `en-AU, en-US`

**Content-Language:** `en-AU`

**x-ms-exchange-messagesentrepresentingtype:** `1`

**x-ms-publictraffictype:** `Email`

**x-ms-traffictypediagnostic:** `SYZP282MB3192:EE_|SY6P282MB3992:EE_`

**x-ms-office365-filtering-correlation-id:** `c75e009d-72e2-42ce-a51e-08ddc085e7d1`

**x-microsoft-antispam:** `BCL:0;ARA:14566002|461199028|15080799012|440099028|40105399003|17111999003|3412199025|102099032;`

**x-microsoft-antispam-message-info:** `XnTNoIE/YZSkWuonUTY72XypHkDOaTNICbh8kIciN8Re709WLs9vBwUi7+LLzYYJong74u3zCAV0gjYbXkT/UVdzUmr0GHvg+bvEC/RyDiBvmf1oCuum20WewygRLBLd0tNG5vpPEOs2dWUtwBoTwYciBTZMGV5BvnVvvBYnQFbseHdQTtGVJtgoTIeQO5rvIsnsiOcXVr6g+GnT1fy46QQMyFdfz5YyFkB/1a7nZxjLLvvgQAbVaauMgkS8XfUdCM6QeARnpDMjNSa88H2Xxwm1fO9p9schMFhsoshWTkBUnWMLNwkSFnGrlUu/2CvX9v3IgUKrO2qn4ygDE/NjkKjAL0PKWF0Em+iE467C31/Ok5moaUvFXvYUFUjjRlWRepBdAoAtPdLkvBlbGLc/tIWPJPsT1cN1fJMhVW+6kcE6aS1IPnU8P+mr5rVbqo2TZx3iJbrQ7Zd1W1WtqBKSVr3FDHTeHJpfpKqG/eu/2ZJUW1c+fBH9nRmVwPaN98YRLMmcKbd8Fa5nwWwVNjIc7XWTLXOIl3KxyVs8v10R0gw7N6RgMm/xzggscyAKGTFOXOZju0/a49iPoKM/xdO/KWBBPCe9mfeoE7S8tFHDOAsaKtpwqQtQbc7G31eswlQSeaK3cWj6/8AwZV7T2LsOBhtW+OO5GKa0Eguq9NgdWj/sQwWPlVbcMK/tix+rCRmlDRJ+Fa+VvjU3RayQr0Fh3W1t0e98NxO66B6ZX0E30ky97NZ9jdW+H/ccCJdRQduwRUq5Fsnjj0E/l4ESu5Gnp3kCojhBWSXjONC9CCA7zOE=`

**x-ms-exchange-antispam-messagedata-chunkcount:** `1`

**x-ms-exchange-antispam-messagedata-0:** `e+w2fkKdWH6gztZODDj/nERKvdOlrvgBLIzDPERy0+1dQqtUhVlItexEFfA4+Whgh2qAEnBjRHQyytJpJPEReFC9sWiwhMxwNRdlpPNx4MfPr484x65BoM9rdFEC/HoXCErx2D1W2u5fN6QlFtCDt3Ei8IMaiuOw/kyxLyCLEfEGaKI/BVJWp3FnNHzxABhKQo0Y6Mv2mhPJsI/gObraOOvh2fEMqZb1txk8/BceDfFEbBllX43DorWmmapHeFv3jtcoVR2Mwq87p+3coFYv1iuMNHvhynsJjIH8sqoTYHaZe5qcyp7lF4MqNHLVck94WhFGjFCC2cDaRAvhv49fakWF9MqBPwvSN4CU5pvAva+qxFrUY4KAe8K/5u0+V43mBef+PXAIRImBDGycIOopNFCEQwTJxEMPpYpC0qyqungldg+EjHSEhRcIXReNZUBZusTJGiw8QEnSZ7g9ArNVAxs/1hZMZLHn/aEtLRcU6CEe1lw0UBLksKQ03z1OMW8LPeq69Rad2s4Wl5nGJmgbgrTrn4Ez84O6/lPVFXiwHSAvlnfZ1k5LDHGnUhshm0I8ZE55sA2D3spYTJadUYNo0RPTUcYUYJlyeS5avd83eq0xS1ZMsK+noyFIIqQ3iIkvrLk6fzFoVQPI3NevsTT/eHkU5Y+HHZ+7gIstWChF6ofF8iv17eamrUIUxnjJTxdgUWcQg/F63VA5VbCA3jRSa6zBO2h0eZcN2z8h5+bwklROJudg17DSciZ2UGH7iV8ATh0MZB52QcZRBuEIDpg8tCt2aG2vi4Xi5a3c3dPCwYjbrKnTj+vY8GFTeT2dGexq0iCnI5VvKUalGP0LHNHYq0euGYLqBZVPlcik1szzpcHQKrNfKdnBXAfRfEJT/nQ0stviBoWhTyOuCQFdI40Rh2aPLIsPAOJ+SnXkJCiV4+N4vy3LaA3iReIHxQ5d9JhuXnBdFI1RWLjKHq+YdG1lTnIzCb6PAkneN9Oo54HH6tOlMc+r/TDB5oVCEAW1XZEKVO+TMP1rOO3QtK1XCUhLnkDmJc9WojBsHJEuk9Fak4NfAifr7rdiOSTGo/EdxD1KY3qGQ+YayzyApAZYfN5y3gD7GjhQKgGauf47hYKJESW7d3nVDQ1z76tW7m/rjceccy5+3hzDP2Rv/Ku0PpumiJr/iuYI30BmmT2tXQAE8UZUREP0U7ecLMgsM+xEu7LtcRpfwrJ5W1IbUmnLck5rsmLos0djzJLRYTWdxH9x2u0=`

**Content-Type:** `multipart/alternative; boundary="_000_SYZP282MB3192D7A35FBC3F5818477CD2B74BASYZP282MB3192AUSP_"`

**MIME-Version:** `1.0`

</details>

## Email Content

```
🌞🌞


---

[HTML Content - Cleaned]
🌞🌞
```

## File Information

- **Filename:** `6mreeh9v8vp0b1cj656h8dqfmhavt24p8coap4g1`
- **Size:** 9550 bytes
- **Processed:** 2025-07-11 14:19:26 UTC


---



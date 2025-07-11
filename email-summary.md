# New KFC Review Emails

This PR contains new emails synced from the kfcreview-emails S3 bucket.

**📧 Email files added:**
- `8ku27rd7hv9bavcpme5l3aaehlmcfc8bro0pr8o1`

---

# Email Sync Summary

**Total emails:** 1

**Processed:** 2025-07-11 13:37:09 UTC

---

# Email: `8ku27rd7hv9bavcpme5l3aaehlmcfc8bro0pr8o1`

## Email Headers

**From:** `Andy McBlane <andymcblane@hotmail.com>`

**To:** `"zingerpie@kfcreview.com" <zingerpie@kfcreview.com>`

**Subject:** `Test`

**Date:** `Fri, 11 Jul 2025 12:24:28 +0000`

**Message-ID:** `<SYZP282MB31921793694E558BAF53C7ADB74BA@SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM>`

<details>
<summary>Additional Headers</summary>

**Return-Path:** `<andymcblane@hotmail.com>`

**Received:** `from SY5PR01CU010.outbound.protection.outlook.com (mail-australiaeastazolkn19012060.outbound.protection.outlook.com [52.103.72.60]) by inbound-smtp.us-east-2.amazonaws.com with SMTP id 8ku27rd7hv9bavcpme5l3aaehlmcfc8bro0pr8o1 for zingerpie@kfcreview.com; Fri, 11 Jul 2025 12:24:32 +0000 (UTC)`

**Received-SPF:** `pass (spfCheck: domain of hotmail.com designates 52.103.72.60 as permitted sender) client-ip=52.103.72.60; envelope-from=andymcblane@hotmail.com; helo=SY5PR01CU010.outbound.protection.outlook.com;`

**Authentication-Results:** `amazonses.com; spf=pass (spfCheck: domain of hotmail.com designates 52.103.72.60 as permitted sender) client-ip=52.103.72.60; envelope-from=andymcblane@hotmail.com; helo=SY5PR01CU010.outbound.protection.outlook.com; dkim=pass header.i=@hotmail.com; dmarc=pass header.from=hotmail.com;`

**ARC-Seal:** `i=1; a=rsa-sha256; s=arcselector10001; d=microsoft.com; cv=none; b=nNAzMFTe0Jkd4+4YUZecOsGt2/s7/BBHhR9o8nobfTWR0baxggJDV7WKK9pBxSTP1NfRtMyyASCg56XC99NTanE4AkDswhCejEeqROMco/DUIEj/GLnx4U2M+8jkwZ2/8aaL/PLAf1msSgJgVvhWFlsHAEDHLb3uQQhgOLuBVRBr0vGS2vHlD0XSBqmqW1JpJ587M5BKUvzqlu2ydpblBx7z0VqqlJCVJQG5icQk3k+/Vle/nrKGXCmhzigTyTniPbdL8ZMYfQBC7prtHZQHVCkte69bILt9HJown/4vz+jHtwOaqWmVFZBTqG/PNptBlfmjBsc/wZL8CEqT/HbS7Q==`

**ARC-Message-Signature:** `i=1; a=rsa-sha256; c=relaxed/relaxed; d=microsoft.com; s=arcselector10001; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-AntiSpam-MessageData-ChunkCount:X-MS-Exchange-AntiSpam-MessageData-0:X-MS-Exchange-AntiSpam-MessageData-1; bh=fdkeB/A0FkbVP2k4J4pNPoeWH6vqBm9+b0C3OY87Cw8=; b=HXWG854tlY5KFFxrQDz41kRmj0rKYj7OqfCySdSm+ooxvfqHwt5/ouPfkV/XvuXnWUPWsbLfl49maQwLXNZo1LlPrYs9sWCRAzffEfF/isk1Wicd4wDfrgtRerKZ7lU8xZ79Kvc9oK16fpdKa4NeCgqMy/ycz7l0LQMAPm+z+yry/lK1ZqeIWR6V6l8yKXoiIHeipoFbVHB4vDRrqj3p24QWrgckyMyW4UsN4s0etP26Yfe/jOYYOILA9cNyBHN09I9hkaiaV0BCdAh/9vydg8cSei/LsepcCNRW9N54fEub8evJoys3w7WzJJFbNdz++AIOuK1E00o3VY6zaYep2A==`

**ARC-Authentication-Results:** `i=1; mx.microsoft.com 1; spf=none; dmarc=none; dkim=none; arc=none`

**DKIM-Signature:** `v=1; a=rsa-sha256; c=relaxed/relaxed; d=hotmail.com; s=selector1; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-SenderADCheck; bh=fdkeB/A0FkbVP2k4J4pNPoeWH6vqBm9+b0C3OY87Cw8=; b=gEMRl39RIRExcbx1TYH5oG/80JEDE8LgMSrmpWwzHLUcI0Ygvjc7dOKYGxhgAYDjciKIrZg5TqADi1bDR2t9hM99GZwm9YxBVWW4DjLzkn5Fpztosq0fTSL190vFTbMmXmNMcegHd19SShWjRrbiIiQEAZFi+/Yvs4gFGstXv0V031kDMdNjUUdTQNN7CWvcnvWKxIpLKXIr9eiwjBNViiRRhGz+5vjBAEfGTfe8/P7fETJDuJ0xsgYa4gE/WjJVgrnCbXTgM6er6Mb/NRKrUEUc/7gVZbX3YTbKSHNaqcwG7qXcAZsFmITZNHfFFRJzY4cUErcSq641nhhmahotCg==`

**Received:** `from SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM (2603:10c6:10:169::23) by SYYP282MB0783.AUSP282.PROD.OUTLOOK.COM (2603:10c6:10:73::15) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.8901.29; Fri, 11 Jul 2025 12:24:28 +0000`

**Received:** `from SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM ([fe80::7120:3e8c:eb6b:4104]) by SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM ([fe80::7120:3e8c:eb6b:4104%7]) with mapi id 15.20.8922.023; Fri, 11 Jul 2025 12:24:28 +0000`

**Thread-Topic:** `Test`

**Thread-Index:** `AQHb8l6/czwbDHeYaEe7Ep2rDgkWOw==`

**Accept-Language:** `en-AU, en-US`

**Content-Language:** `en-AU`

**x-ms-exchange-messagesentrepresentingtype:** `1`

**x-ms-publictraffictype:** `Email`

**x-ms-traffictypediagnostic:** `SYZP282MB3192:EE_|SYYP282MB0783:EE_`

**x-ms-office365-filtering-correlation-id:** `dac75b77-2b3f-449e-82ad-08ddc075e1c0`

**x-microsoft-antispam:** `BCL:0;ARA:14566002|15080799012|461199028|440099028|3412199025|40105399003|39105399003|51005399003|102099032;`

**x-microsoft-antispam-message-info:** `s49tb6H4N7MXsZmb4NtOX0efLTVDl14n/YdKTPNURlukW2+zV6YCfLXBJX9sxDaLvk2Jr4XKScWJqkc9+LTXeA2Rm4o6mPt4YbxKtO6dFk4dBwOmBHplsSMqEbkmuBh6RPiaF762q+TVoAEDeEghq7XbD5qG1+NqmgXxwC9Kclpa/z51icG+DiiGDthw+16/Uo41U5S3rtISkrA2MX8yBWmJWlYnRam3okYQU8E5Jw7xw/7iDKNbYnmOrNQK7MUhHbeFujDGPJdKg5AuovsGJo84e+FmRtpcyj1bnslOQR7Ae3O8uwY2fJB75sWeXUrwXZuQ2DJDwy5QUmBdVeIrKYI/tmtRj+exMUXreSldtlt/Hun/0JWrDNx831a7Sdy4MkttDTDqGAkIe+jCgcfJ7db3OnZcu1PDZqwEC/nmCKb/gJg71nJDoig2UB8fiymaOSdWFJXDLEnE+LML/YJgSanBAtwsekOwX08bntNdNS+L9KYZDlxB9nwa8FAqXeq8pRBqBP8Wv9unn3/B8Xfn10sHIMpXKUk30njhdp6w0YcWtW3pv2qS36+Rs6Q9jfuvfRFJ/CDWFqVE/9/X2bH24y0cZt8X5GpzYOjY0TGbbia1PRTnm6qgaHQsZ6sIU1Dn1thvTor9Wcok1+wEmjE592WC4nIE7i6ufyzJytzbfw2I4UDM6xWPr0X6vEszfG3lgrMuCpIYrdJJ7DTAhapBX5Dj2RIIVpJNTMfdDOcRJPkVfLoQ9gyPQpZMfO+WUDqGZiaDYEai0O/mxsG0aznEqbxs+5hWWlH9VRei2sJ7e/acO/3dPnOpPrYnzjn9GdeKHStstkJO0rMFGPWQ1XE1Zw==`

**x-ms-exchange-antispam-messagedata-chunkcount:** `1`

**x-ms-exchange-antispam-messagedata-0:** `Oiwc2weyGw2mJUfS3+U/h/JiANDgLQNvmAXHns3EgvICZdglWZlFsS/OOwlgWMzgnmnnqBbmCKgRHHkZMF4oQYzcdY55LI7Sut3C88ItI89ntSYUPhmVSLptCnoDZljWk4RCcUGWZSAeUKstBy1IvKAYh3fNoWd00cAJRUN2LIfmvTHLUxL/5xLcdYH8xfSyqf7qH5e9WaXZtVAmUS1TL1ZHpEC5oudmoM0aB3LL6bNLYDIt2YSiGbJF3THhYCWAuZHW3JkmZqvNX3+/P34lj2iBT9d1utjgMsZ0nP4mmOmCN+HG46Kv3x8Lhy9yvE32tN9P4eOQwKsXXLNa007/E/ExbN/tCpa73w/7+IK//Ka0W5ZUr8VypYoQiDJ5Gpy1+XzcjJQFpLPc8eQJlerWrWWgV2AP1b0yrPO6gaElJPkPbWgMVbq1VvU9xP/yphDdy1epRv10bRbMlm0A8eZ/B2KrdKfgnaKLj64bnuK4N4Qjkpq8yLIVhXsFc4XRIGXrml4pXLrX8Y6MFuTUx0C58frNNID5Ecat8Q+Y2H6Xen/mKM2r9Ri93ctjLqItf3skI7znllccFuB93R5ttJnitOvUwdDki3/71aev3lXQP3aQpD+QFrO2J+c97e9f8G1nMbc26MUVMAtRUQAPnKmy6lzY+u4pvM58h1GW5n2Pym559wVlBtgLwKUqk3YdVtxdJ5h4wdfU60bqMDBjtKxsASJN0IyEaapa2Hpw7ozudcvMzIgrFp+ReFKZ2YJnjTUegTCYatyaSxSqHGaBbNcfgSlo6CYd3IvxEh9bpdZ6Tz89vF4q29qcSPubh4RfuRUp2V5dg7bpx3XjAnA5M4KOnxH8pANwkiMJKG75rMXKhUXBWwKfLW4YemdBMictUXvvmgnO9E+DRNB3aOY0XoHLykRM9VytsBi+pe2QAsPcpO8foOGq78xr+7W/RzAc4hR6mup3+I2IJa6QzBZoahNS6z1+jaA0Id0hNN6f2kNlMYiTBE09JBkD4eSKF+KaFcrIEtZH29TQ3L3U6+/5vFbLpQKyfYAH1ILhXNhYlDJ4YTZrF1kSPJXm1WwkoRXTTFvIgdgP7f2IUPaaF9ogpo1pbmuoO3duWQBGbGhNXY/cf7i7lMUuXH4Yh7ZoFuqJ+N4Xlnp/NrrcCLeo/pH0i+YU/cCxzerlVZePvLHhljSTLUSCJ7IODtejQ5UHhF+4QSD90nlSB6od3otKHTgn/CLMuGplSIDwyY9ySGQw5OUJIRA=`

**Content-Type:** `text/plain; charset="us-ascii"`

**Content-ID:** `<A041A9C58A13C241B1DED911658411AC@sct-15-20-7719-20-msonline-outlook-26b36.templateTenant>`

**Content-Transfer-Encoding:** `quoted-printable`

**MIME-Version:** `1.0`

</details>

## Email Content

```
Test

```

## File Information

- **Filename:** `8ku27rd7hv9bavcpme5l3aaehlmcfc8bro0pr8o1`
- **Size:** 8443 bytes
- **Processed:** 2025-07-11 13:37:09 UTC


---



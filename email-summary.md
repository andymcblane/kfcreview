# New KFC Review Emails

This PR contains new emails synced from the kfcreview-emails S3 bucket.

**📧 Email files added:**
- `AMAZON_SES_SETUP_NOTIFICATION`
- `tason4r14kcbi9pvradsrianmd9fj3s1647p7b81`

---

# Email Sync Summary

**Total emails:** 2

**Processed:** 2025-07-11 14:06:09 UTC

---

# Email: `AMAZON_SES_SETUP_NOTIFICATION`

## Email Headers

**From:** `Amazon Web Services <no-reply-aws@amazon.com>`

**To:** `recipient@example.com`

**Subject:** `Amazon SES Setup Notification`

**Date:** `Fri, 11 Jul 2025 13:52:49 +0000`

## Email Content

```
Hello,

You received this message because you attempted to set up Amazon SES to deliver emails to this S3 bucket.

Please note that the rule that you configured to deliver emails to this S3 bucket is only valid if the entire setup process is successful. For more information about
setting up email-receiving rules, see the Amazon SES Developer Guide at http://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html .

Thank you for using Amazon SES!

The Amazon SES Team

```

## File Information

- **Filename:** `AMAZON_SES_SETUP_NOTIFICATION`
- **Size:** 645 bytes
- **Processed:** 2025-07-11 14:06:09 UTC


---

# Email: `tason4r14kcbi9pvradsrianmd9fj3s1647p7b81`

## Email Headers

**From:** `Andy McBlane <andymcblane@hotmail.com>`

**To:** `"zingerpie@kfcreview.com" <zingerpie@kfcreview.com>`

**Subject:** `Purple money dishwasher`

**Date:** `Fri, 11 Jul 2025 13:56:03 +0000`

**Message-ID:** `<SYZP282MB3192068162BBA8DF87E6501FB74BA@SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM>`

<details>
<summary>Additional Headers</summary>

**Return-Path:** `<andymcblane@hotmail.com>`

**Received:** `from SY8PR01CU002.outbound.protection.outlook.com (mail-australiaeastazolkn19010002.outbound.protection.outlook.com [52.103.72.2]) by inbound-smtp.us-east-2.amazonaws.com with SMTP id tason4r14kcbi9pvradsrianmd9fj3s1647p7b81 for zingerpie@kfcreview.com; Fri, 11 Jul 2025 13:56:07 +0000 (UTC)`

**Received-SPF:** `pass (spfCheck: domain of hotmail.com designates 52.103.72.2 as permitted sender) client-ip=52.103.72.2; envelope-from=andymcblane@hotmail.com; helo=SY8PR01CU002.outbound.protection.outlook.com;`

**Authentication-Results:** `amazonses.com; spf=pass (spfCheck: domain of hotmail.com designates 52.103.72.2 as permitted sender) client-ip=52.103.72.2; envelope-from=andymcblane@hotmail.com; helo=SY8PR01CU002.outbound.protection.outlook.com; dkim=pass header.i=@hotmail.com; dmarc=pass header.from=hotmail.com;`

**ARC-Seal:** `i=1; a=rsa-sha256; s=arcselector10001; d=microsoft.com; cv=none; b=lFdOqLTEfB+RvuBBKNABJexVUdg2MVY4YWJvzHP6SqkHmCkFlFkgVUOSr2+3lK4KAZQDNDlH+5TdmPl5WQgtzbabl+3Vb2az6pW0SER9nbHKxAUDwWPUIfb82DDKh3mDiFMYwA4bY7RvS7j3Slra7RJe38IjLmvburweWMQ7K8aluo5WkTX/1kTdcG9o2Q0u6C4p7ysP/Fuok93l+P/9eBg9TkKec99N/cwXc9Rfh4eGru6ympuXxYbkmEQEb8fWwnqngiW2hVdFlCK9SMKsytZ4akY3wBeH4gMe9SWF8QjWXHD3J8RaHDX41Kj/rJJ04G8BhwCdhqm7WlN8P4GrDw==`

**ARC-Message-Signature:** `i=1; a=rsa-sha256; c=relaxed/relaxed; d=microsoft.com; s=arcselector10001; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-AntiSpam-MessageData-ChunkCount:X-MS-Exchange-AntiSpam-MessageData-0:X-MS-Exchange-AntiSpam-MessageData-1; bh=4lYebZVgdWslaXesd+UdYAz9Dg4h6NOz4SNZyMgQ2G0=; b=J59ZFKZH/b3Q+uI0fkIlQgmBt/NUOn1m80aIdTBCzT4fb0P5+xtteMkgNhBypecB0zKDzaA8mWFfBMVXULYVAI1le0c0reiYnPNwFfTiL/ZO9T51I0SP3VcJyAq6SvrFreG/XW3OHqG5ff0LBs0Kmc54BLADaEnbBZo3YpGJ3oITpkamd7ci9VDt1QqlZ3XEVPQLt67QgXtsZQUgVxYhEhnK9kha68DFdjD1LPFTRlihdS6MF0hM+IKDZwyVMmIjxyO/hTIfnoulUHOSzqp4aNaiacw6v7Zu4dvNe81vSi07D22jEEbNcvZuxDJiZKPdfsE8Ilw4j8i1M/gTVMZFRQ==`

**ARC-Authentication-Results:** `i=1; mx.microsoft.com 1; spf=none; dmarc=none; dkim=none; arc=none`

**DKIM-Signature:** `v=1; a=rsa-sha256; c=relaxed/relaxed; d=hotmail.com; s=selector1; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-SenderADCheck; bh=4lYebZVgdWslaXesd+UdYAz9Dg4h6NOz4SNZyMgQ2G0=; b=lHXUD+O87E/XEKW2C77A9E2Nl7oFQHDkPlYBma8bLMtYtPegQ0RCcP66qgLvswuL/JF6qNL+OoE+W2qO4J+nUE79TlNVu6Ca8hDEXRGvcdfuE1kiVZsuBCL96fmgkC2ePV0oEsYOaAdaB9fUn4Nz7HebZRmDmrazj6PrWUJqtcVH/5VcamCUOpPLzRt6+1Gaz0iSVOrNwc+ySjokOEKp6ZMlz2VLChOnW/Hptc+c1YxIlTdx7vTMCkxv7TYZM8C+u5+qTN6JjL/NhYmZv4+f+IWkOerYtLK3UoXj7HJyZ5CNTPJL548UCewAUEU97x7lYMNmPOq6SlRyJOPfJoZwpA==`

**Received:** `from SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM (2603:10c6:10:169::23) by ME3P282MB1393.AUSP282.PROD.OUTLOOK.COM (2603:10c6:220:84::10) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.8922.27; Fri, 11 Jul 2025 13:56:03 +0000`

**Received:** `from SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM ([fe80::7120:3e8c:eb6b:4104]) by SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM ([fe80::7120:3e8c:eb6b:4104%7]) with mapi id 15.20.8922.023; Fri, 11 Jul 2025 13:56:03 +0000`

**Thread-Topic:** `Purple money dishwasher`

**Thread-Index:** `AQHb8muKXsk8KpZRVUi7kiMhltAi4A==`

**Accept-Language:** `en-AU, en-US`

**Content-Language:** `en-AU`

**x-ms-exchange-messagesentrepresentingtype:** `1`

**x-ms-publictraffictype:** `Email`

**x-ms-traffictypediagnostic:** `SYZP282MB3192:EE_|ME3P282MB1393:EE_`

**x-ms-office365-filtering-correlation-id:** `5d360b2e-acc9-463b-65ca-08ddc082acb9`

**x-microsoft-antispam:** `BCL:0;ARA:14566002|461199028|15080799012|40105399003|3412199025|440099028|102099032;`

**x-microsoft-antispam-message-info:** `egdgv3SzE9xBgbpDc/pAK0OHwThdXqOeAQNuY/DivWVURmSCBgpKZl1X3zX/90wANcBhmUxh41Dg2D3lJNctBOHtF2JzAb7rYd3/R5QQDIYqrUkQkXd6O18KGFTiQgmoZyZKmlJuCl58yjKnHtbKVQNcH/Axo50NB8nBdBGjin50biFfo2U0YFZbDz8gSRYQ+p9DikEdhHEc68wj6xn7wa0aNuCZG+F4pbhBVbUOjpGRh54342vW06nQpcGQu3IiFSkK2P2vWF0InFFXW2gtEM10+U4bHkhPYNHT8/AkSpAT0bryjXtWhRluyMW1Iw/39cPUnA4alLCXjV+sNtP6m85TG9QvYdwKHV5VdjFSp8IzdPDhUes46g88DWYZ2LKs8WQSLbgtcBwZ9UkevM3+qRnh+XABt7YsCBZKdhCthnMyLyiQYeXtNEo6ZRN6HMDK3usm2Bj27XJPzNBjbmDkeizIGN5SMsCzb+gB1l8BweBkngWea2YtispHbdI7IYUE19I4XzYyB5PrqiHsSoVVkiZUvwoFa67KHP6P0+W2h/2RqVz8f23TIAG9ephykAuEWO1ua4JhY7gztrFXJYH2fQ4cHzYDnm5qhwCJiKuoeAJ05byMhyKSoWbe37sBfZrCbsjPBFUwKvObbKSLXLIjPpwbVY0mC1/a5pndtCQxBe+U2hunnHuChPwkntd+B9Gv+i98xUgeFHDfm7ccJfVAIPsZY0nqyIV25w6IuU8vGAuC2OpQq/lOQJKWYidysWI6SqnAuj11E48yq6AkuM5A2g==`

**x-ms-exchange-antispam-messagedata-chunkcount:** `1`

**x-ms-exchange-antispam-messagedata-0:** `tWR93MpReLUHCxy57vgh2JWmTw+NO8nCK3qC3y5oh6+wYB9pTVl4h3neAAU1MjfgYsl0aTm7AFVwG59zpxe9+pua54ctQU3W0DcR2wjaGi/3RoLZxefClgR5cdRVUv1oLQH3moN7alan4nbvT0oO5WNFlM7U68CZ4NEE7XKoq7aBycJG8qX1rSJMPvJ4tuWSeQpnOJ6JpkfptuMqYnOu/b5evOD0lgiRcRJYafNUCGUde0amT6alUxlIP0sFKwyDzcN5AfblM7lHhmXxHjDQCuO3zUfi1kg+XmBT/PLXmaDvy3I/CcMWNlCr6QURRQAJ8SMsoVV0tqGI6sOLnE+ZaOz5mV0r0iLQGmSe8LrnfL3Sc1pptCyLA7/HsEuKZAx9tHmSJ9tug8jiEfooO5Q4qvjBP8cPDas67eGS0XG1yHPdrTABIlzjBYHQb4YTEMk02OIc/3f/bcK1yJB8ay7eWGqVs+EgvSq9szS3y8KcMdV6FLTXNx1foPXqV5IsXj4sYOAKl1HJ/VmaemQMalUKSLLUgAck1O52UrxSlSGd2ojc9OlthUyS6x8Ql9/y6pb2x7qjIb5nlxlsWr2JaaqX2VihA9fYchf2PPU7rw8U/cJFWRvFMSANBq/G403462RxXfe3Rw0clMWF4dtK6i+b91MMRxxMES81hNTBIsWJ13m8FBxqMX8uP+5Ct6quSawj7jtqZ/YWVvInTQ8giKKwfVpuPs74WRCWB0R3B1f3JWCPDw3L/MMaawpjTjY8wxll+3C8g34CBi9gSNgUKKwJabSa3QWnPOldbhFJDieYexUme+muWat9ZmXnvJrpsOdMgWwcZTCsV3mOVHWdN1HGMQA+d4x8kjbanUk7BSh9CqAG7I7yPT2DWFfomZLais1/eZ8PgPFZQrDKEY6OHXYs/CL0bcQJoWPnJMQ1x/TX05wv1d4Piw3sJumIBsT0+mawWsqJhh8CLQNHN8p5V5BIu3CLzzirAfZuAGlEthjq52S2oEi2mnnlE6M6+JWBgQYaqd1dlp7mkX+vYlfpropocSeA4/gUbS52bOnau0jKiko7+s1bxHF3f0Pru6jyy1sRS6qz8gw4tHln+tUD956M5soA1tbTr4UEsps3NY+0lMdZnVay2QSCXNNGNFl8d5I+td5SyN5C+eGnQqXmOpt796y264jnKPmDZtB8IcUOVfK/EthlPtQzug8lWNPSNJHhq7k6cl35p+Hn6WS4i2KjH52lvD8LwG3qejLcp6ckbDs=`

**Content-Type:** `multipart/alternative; boundary="_000_SYZP282MB3192068162BBA8DF87E6501FB74BASYZP282MB3192AUSP_"`

**MIME-Version:** `1.0`

</details>

## Email Content

```
🌞🌞🐧


---

[HTML Content - Cleaned]
🌞🌞🐧
```

## File Information

- **Filename:** `tason4r14kcbi9pvradsrianmd9fj3s1647p7b81`
- **Size:** 9516 bytes
- **Processed:** 2025-07-11 14:06:09 UTC


---



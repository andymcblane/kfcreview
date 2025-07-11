# New KFC Review Emails

This PR contains new emails synced from the kfcreview-emails S3 bucket.

**📧 Email files added:**
- `8s1tmp2d1be7aqe4b2kjjf36pkm8fsfeg809p8g1`

---

# Email Sync Summary

**Total emails:** 1

**Processed:** 2025-07-11 14:18:20 UTC

---

# Email: `8s1tmp2d1be7aqe4b2kjjf36pkm8fsfeg809p8g1`

## Email Headers

**From:** `Andy McBlane <andymcblane@hotmail.com>`

**To:** `"zingerpie@kfcreview.com" <zingerpie@kfcreview.com>`

**Subject:** `Wip`

**Date:** `Fri, 11 Jul 2025 14:12:17 +0000`

**Message-ID:** `<SYZP282MB319237B27530D42ED657244BB74BA@SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM>`

<details>
<summary>Additional Headers</summary>

**Return-Path:** `<andymcblane@hotmail.com>`

**Received:** `from MEUPR01CU001.outbound.protection.outlook.com (mail-australiasoutheastazolkn19010012.outbound.protection.outlook.com [52.103.73.12]) by inbound-smtp.us-east-2.amazonaws.com with SMTP id 8s1tmp2d1be7aqe4b2kjjf36pkm8fsfeg809p8g1 for zingerpie@kfcreview.com; Fri, 11 Jul 2025 14:12:21 +0000 (UTC)`

**Received-SPF:** `pass (spfCheck: domain of hotmail.com designates 52.103.73.12 as permitted sender) client-ip=52.103.73.12; envelope-from=andymcblane@hotmail.com; helo=MEUPR01CU001.outbound.protection.outlook.com;`

**Authentication-Results:** `amazonses.com; spf=pass (spfCheck: domain of hotmail.com designates 52.103.73.12 as permitted sender) client-ip=52.103.73.12; envelope-from=andymcblane@hotmail.com; helo=MEUPR01CU001.outbound.protection.outlook.com; dkim=pass header.i=@hotmail.com; dmarc=pass header.from=hotmail.com;`

**ARC-Seal:** `i=1; a=rsa-sha256; s=arcselector10001; d=microsoft.com; cv=none; b=goc2JhKy/gFnQEuH3z+kHmTELlfJR+rNZggoDB+IWCpybloyIbLZ3p23dfSwCtgxmCiRpkc44goqoM5hlKumtQ5ugxcdL7EOUaKzIxBYcTYa8xgRzj2TetqKnSrhq+K1IG3rxTdo6ZNayDPewYmACwRKNBXjonH7kEFxl2J1rSZfKx7gaj+cMftoe1ZuNhI7EnPmCwqmWNj8Isz2CiSZgB4DlByGQPnGEFhfNfb8mfmcTPRkLVnRBXZtwaJgI27KBeNsuWWUvs5AkhNiUlSXrnB4z6iyhCCy+Fdv8KmdgxULzmFPXQrjYrxGZ/Qc3Xu7JmI3Ft8BJJamo+E/r1REbQ==`

**ARC-Message-Signature:** `i=1; a=rsa-sha256; c=relaxed/relaxed; d=microsoft.com; s=arcselector10001; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-AntiSpam-MessageData-ChunkCount:X-MS-Exchange-AntiSpam-MessageData-0:X-MS-Exchange-AntiSpam-MessageData-1; bh=0FdyjyfKODCFcZ4UERf/0+lH9KBQlPlGIBYaF+3udyg=; b=JgHaJkHMQ1jkTSA1dBKuxmwcQhzVF05l3kPZ+yQUWKLtz24Hr4n7wvEZUWh9fVTTvFfCXesn2yrt+zCeYK0roKDlATSkU87tVOzJN5VMAgA0rVx3QCUnotOa7hDgt8meil0cQwmXLkHkNF9kUTmAzgbHikUAQzPwCUfY3pP/n3XMEBIw2mkk5ayYOg/IOS3IagqJ2cv4SDtgIDdmpimzlyZBzCUw/cKtOR+pyc51gHmcz8L7zTq4G5wVXxRcfLznz1FW8AnO9ML2d4YnubyDaxEcz1mmUCNDpgVQsd1JEq/rwrMZr5AkXKNRcdQa9/p6LpT41EVgETtidTItqlmC2A==`

**ARC-Authentication-Results:** `i=1; mx.microsoft.com 1; spf=none; dmarc=none; dkim=none; arc=none`

**DKIM-Signature:** `v=1; a=rsa-sha256; c=relaxed/relaxed; d=hotmail.com; s=selector1; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-SenderADCheck; bh=0FdyjyfKODCFcZ4UERf/0+lH9KBQlPlGIBYaF+3udyg=; b=tY+h7A+f226HmVuD56nGJTBA55qknLTtbGJKzAdSE8dmD9Ha7cQmhk9SQKjvvfJdtjEHCG/byRLDYsJ0m+wUwtxPc3814UIuJSf2v7c3KucesOMZ9Tyd1ec0xua4I7ztqffRXAza1IV2XEduPcgk2CoRDPf3MlfsndzSpMI7n5OqlZv0ov4VWNfnOZwSpoQI5lK1eKsWG0lQI/illadQ/zgCcK6NeDPLJu14H/M2/53GlSsXGoUgFWpyNfVnE8IGNl//b3nVmjftLbsAdjMbxKZSdnziXnPVoz5eqCj3g+t0hfMQo8tLAZ3hn2x2hYBswuVzMZUZ3Z1T0j9TVBLvVg==`

**Received:** `from SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM (2603:10c6:10:169::23) by ME4P282MB0726.AUSP282.PROD.OUTLOOK.COM (2603:10c6:220:9f::15) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.8922.27; Fri, 11 Jul 2025 14:12:17 +0000`

**Received:** `from SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM ([fe80::7120:3e8c:eb6b:4104]) by SYZP282MB3192.AUSP282.PROD.OUTLOOK.COM ([fe80::7120:3e8c:eb6b:4104%7]) with mapi id 15.20.8922.023; Fri, 11 Jul 2025 14:12:17 +0000`

**Thread-Topic:** `Wip`

**Thread-Index:** `AQHb8m3OECge0EVGcEeSwOjPvdFQ1A==`

**Accept-Language:** `en-AU, en-US`

**Content-Language:** `en-AU`

**x-ms-exchange-messagesentrepresentingtype:** `1`

**x-ms-publictraffictype:** `Email`

**x-ms-traffictypediagnostic:** `SYZP282MB3192:EE_|ME4P282MB0726:EE_`

**x-ms-office365-filtering-correlation-id:** `de07ed54-3130-4ba5-3983-08ddc084f160`

**x-microsoft-antispam:** `BCL:0;ARA:14566002|461199028|15080799012|40105399003|3412199025|440099028|102099032;`

**x-microsoft-antispam-message-info:** `1iDeguEbUkuTGPNrbg2qsET7ea+E/L3BgFzd3pU7ATxi6bIzpdHpCGIOqRtDyl8fkONj6SeHlWTPVE9EOCV41jl82uMHffU8v+MsZaHBzhzbORigOnffMSmREjwv/HcDdkqAobIfpwoVX2d3rgekFNRrLdoNinPTHlgRAcL0HGft2Nbr1BpPT7P/w0k5creUJxN0XpEVCr+FsY5iFUgJyTSIj50T2+S+pQC1cySWjBCJniQ5A6l1wPgw2QF9Np4hv6NM8tcCbzuoJPKWb3Hm+7/J0njLKjhlwpnBgiu8iCQRz5dXy5sGISWE+jvceG2TfH8HWiO9iHfSf26vnBxdlGc/2ose3EgxosTzTuRnGMIF96Ii8Sc08lcwgy/dU57cSkG8tj1gtM58v3jXkDcmj/eHI/em0lc8KlC/9dSZ2EyA6oMSdqgWhQm/A9uELqCz0qTQ4HItJa5RI+TO4Mdjzxv6NtYgTSffxxXFZsVNL+6z237c6UQRshYLmvmUlfQ9NkxhGj1goIWGgQD8/uKvb6E3Jrij1C9B4yUc3/Uzyq5ZtY6DfOzFkdwNP/oNzlXxBizTV7K/idTVp/WdZpBg3/komjh84zmuL50QCx/Lp4JgXQtrmODH+/rXUo7ckAFm7RoyZxDow7J2fG3dferDanaQvl9x9A1FlM4bIHssdotTUDNDMULqlLYUewj8eKjEZcmc5E4vvLlGzvXgq0Tz+BzsGMQS7dFDXc7QY4wBI/cb84nq/jVMsJ+ZJoYymtB5yBRJKawsbVsNzr0iLLjS3A==`

**x-ms-exchange-antispam-messagedata-chunkcount:** `1`

**x-ms-exchange-antispam-messagedata-0:** `MrXbNr8YLv02bW3sEZlRqyq0AiypTuFh/QeCmGU432PB3vleP7DN8j/Dk1G821DaI/KMcO/M4cVkdPzD7Ncpm+8peUXoDcY1Pei9qIuTOgkXTJWeguIkbVAUPmFk6hu+V0OW56MGMEWqdpiA6zf+iWRFqfHFCN0k/L5sJTbYq3qXpfvifs/U0sr+vqolnOJIAxwNnTJroMU21t+Ll2QAOTa3VEvictgH9Se79wbOLkUowDtdPqFhB7+b3AkITK/1+6pOj8jgj05SVIYO2LruLbh5leh+pX034Z50ygp+/PwA/62jJhoQdRHkarn6DDOuwowPU1TcKLXE5VTmA8a9fX01oZMjZoWCfI+fjnCowK7jEOl7uc042+yCmwoA2WWAkduwp8jhxn0awQv/YvV2TwddxbbNZiCMArXE0IoF5oGU8fSfAYYxcd7zYE0ivo89FewacEqUYc11P/++1BsDlZnczMAWC41Y4rWPBmPyy2cBeyF0yG6cd2Muc85OazZsM0v9CxqB1KkSVFZvmCIABUKGcwOMJWX6Op0fDmCTkGLCP9hYH++qF5Y5CegfTL5NJWqnNs4aQnB6zRG1i7SiLNKhyOS4sCDH12iVfuXO9efcCtI32BHb/6tTEtrc5Oo0ZKS5SShCVv/NpdhLhGK7v3LsMBHvtPbKgyKWMjo+xbQwsEOIhNJHQF6yLVyo1mTqXuWTgcvXSDW7qcXDMaOYXulpae2Km8n9JN3iqYNC317LHJhzwudpEYENd1r3cLjmqrrVPRUDr9iMhkSek5aicPbZcv0nrBoH8n9Q/pBlrteLOUqvIaHpDgh4u0/TZI6Y67Ux/uQiSSvhOMqxGRZQbCefXks/jVdHmoYc75tDxBmRpOAYncgBZBgLSPlm5y0HlU371VI7ZjJD/FuZXVencazUE82IBx4RhLjDlY9SwhINipU7MLE2HSp0zzjOXSQlcAS+OlOGqqOVWVjrhhIr7LMsTx0ZHWgP+bphN7SUCeUqoAdBQQ++gmHwtLDdHRQKMJrh6F35y0sji56B8gdgeWf7AF+RUu8YjDOQD0n1xqTvQkqzWEvOPl+vAP5x3silzZLWAHkXaxo8e5+ukUq3sYLDRXRgvKToDVq89gyIPOvTtykUwTBeC22CxCZw6zECshhodS28C5+H3XVND9qakyXkrwXcgrqeqh9HdvyqnXO6wHpV81Rf0rsC7Jah6kiXYJ6BtmSacOh7LRsdZvBKP4uWv33PDaVVF/MdhoxigZg=`

**Content-Type:** `multipart/alternative; boundary="_000_SYZP282MB319237B27530D42ED657244BB74BASYZP282MB3192AUSP_"`

**MIME-Version:** `1.0`

</details>

## Email Content

```
📈📈


---

[HTML Content - Cleaned]
📈📈
```

## File Information

- **Filename:** `8s1tmp2d1be7aqe4b2kjjf36pkm8fsfeg809p8g1`
- **Size:** 9482 bytes
- **Processed:** 2025-07-11 14:18:21 UTC


---



# New KFC Review Emails

This PR contains new emails synced from the kfcreview-emails S3 bucket.

**📧 Email files added:**
- `s5ct039g8862airrr92jjifmvsfblio8efckauo1`
- `uq48btp24lqsmtlnnj29ka9josj8674ibtoepkg1`

---

# Email Sync Summary

**Total emails:** 2

**Processed:** 2025-09-03 16:11:35 UTC

---

# Email: `s5ct039g8862airrr92jjifmvsfblio8efckauo1`

## Email Headers

**From:** `Vandna Rawat <vandnarawat65849@hotmail.com>`

**Subject:** `SEO Traffic?`

**Date:** `Sun, 31 Aug 2025 02:50:02 +0000`

**Message-ID:** `<SEZPR01MB681741B6CE49E9734E9E696C9A04A@SEZPR01MB6817.apcprd01.prod.exchangelabs.com>`

<details>
<summary>Additional Headers</summary>

**Return-Path:** `<vandnarawat65849@hotmail.com>`

**Received:** `from TYPPR03CU001.outbound.protection.outlook.com (mail-japaneastazolkn19012062.outbound.protection.outlook.com [52.103.43.62]) by inbound-smtp.us-east-2.amazonaws.com with SMTP id s5ct039g8862airrr92jjifmvsfblio8efckauo1 for zingerpie@kfcreview.com; Sun, 31 Aug 2025 02:50:21 +0000 (UTC)`

**Received-SPF:** `pass (spfCheck: domain of hotmail.com designates 52.103.43.62 as permitted sender) client-ip=52.103.43.62; envelope-from=vandnarawat65849@hotmail.com; helo=TYPPR03CU001.outbound.protection.outlook.com;`

**Authentication-Results:** `amazonses.com; spf=pass (spfCheck: domain of hotmail.com designates 52.103.43.62 as permitted sender) client-ip=52.103.43.62; envelope-from=vandnarawat65849@hotmail.com; helo=TYPPR03CU001.outbound.protection.outlook.com; dkim=pass header.i=@hotmail.com; dmarc=pass header.from=hotmail.com;`

**ARC-Seal:** `i=1; a=rsa-sha256; s=arcselector10001; d=microsoft.com; cv=none; b=BL/v57bZEJdH37o5TNOPSPMGJP5E0dIcAAeWXYmPJy9PXnSJnps/cMF0OMRaqLyGOFXC9pF/e5Ou6D0lePncjJ63k+lPm5fAoecmZkGtfmppcHK7gLhj7BPlPEBekEh7C5meS9uTfNlWrTsAZiE0Pol+xKfhM/ztw5nyq1dLQ9rI1nVA2HDbImrTb/+soeOafxnHejUb5TWEkoif+m/mi4Sb1tNrZbtq4rX3fTM1Q3TuJ3nbIQczxPoFDa3r1cNQeUMvF20zTBVOxcKVH0MWrlk+/1HV7Dss34l3d3PKWzMoH4uEm29eVv8iPoB2dHgYXX6xnSCYFoICSZPEV/PjRw==`

**ARC-Message-Signature:** `i=1; a=rsa-sha256; c=relaxed/relaxed; d=microsoft.com; s=arcselector10001; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-AntiSpam-MessageData-ChunkCount:X-MS-Exchange-AntiSpam-MessageData-0:X-MS-Exchange-AntiSpam-MessageData-1; bh=ZiSE2xK07cI2GQe2fp/BiHL6sD11+MOO6kRGELfB3us=; b=xkxpOuD2CYXJ9SpoxbEF0wpI5Hihp9UOtjzQSMDU//lMe4FayDEobqbLxanwsJ8jW4NopNn8OTW/hDeZR8Y/ofKgaiFG3UPEEjKxJHcONR9++sKUXuPYacutfC4mVnNMwt6mcVefPZ09ir+m/7hYYVjiY3IHX7mddaChSSsLiYOEPYVzEkZYNbOdAN9cEJacUwtaPj4E+xrnKvhPHOK38K+hyvnnTnTofqi9haA4oMEUPiualOo2k68ChrnjGcYZP2UUqavnAy4ibU8eBA8JWuuC8H2+hmgrg8zfEc9L9D58YLJwEuZupLkKg1B3FCPHqKpZoZ82VQlB7+8Ye5H6xw==`

**ARC-Authentication-Results:** `i=1; mx.microsoft.com 1; spf=none; dmarc=none; dkim=none; arc=none`

**DKIM-Signature:** `v=1; a=rsa-sha256; c=relaxed/relaxed; d=hotmail.com; s=selector1; h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-SenderADCheck; bh=ZiSE2xK07cI2GQe2fp/BiHL6sD11+MOO6kRGELfB3us=; b=VeReTRJKQK0/7htO5YCDx1HvMkWQsQrz5miSXq/tfSHK75BJdYZ/dSJsFjPA7vpbvs8xZDdYhsIKbJRTJXv2rDb60zD5BpeZKiumxqFUxRfSTILk+CRkARykNaf8Kh/xij6GJ0Cd/ARtCl9RANkw2S5BZKER0LFpd0esCBUSs0DHbSk8LvbSiKfvm0Vd5mcMZi0yxOjUUOJz0XDH5csP2fkop+bFN9nx0ikHW98YCL0CIkSjXw9EXlrda7R8sWZfKsKafkAwNyLn2gH4Lav/8CfJRFmtx7vLesaFRldPTSxjiaSnSbG12UOhUhaIZUKbzj1GezRz0LJlZJhIMiq7iA==`

**Received:** `from SEZPR01MB6817.apcprd01.prod.exchangelabs.com (2603:1096:101:239::13) by SEYPR01MB5744.apcprd01.prod.exchangelabs.com (2603:1096:101:1a5::12) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.9073.25; Sun, 31 Aug 2025 02:50:02 +0000`

**Received:** `from SEZPR01MB6817.apcprd01.prod.exchangelabs.com ([fe80::a717:1edf:6f8d:32b6]) by SEZPR01MB6817.apcprd01.prod.exchangelabs.com ([fe80::a717:1edf:6f8d:32b6%3]) with mapi id 15.20.9073.021; Sun, 31 Aug 2025 02:50:02 +0000`

**Thread-Topic:** `SEO Traffic?`

**Thread-Index:** `AQHcGhzzmphraZHHuEGuMqEtvJAcEQ==`

**Accept-Language:** `en-IN, en-US`

**Content-Language:** `en-IN`

**msip_labels:** ``

**x-ms-publictraffictype:** `Email`

**x-ms-traffictypediagnostic:** `SEZPR01MB6817:EE_|SEYPR01MB5744:EE_`

**x-ms-office365-filtering-correlation-id:** `85e740ba-5010-4228-33d3-08dde8391511`

**x-microsoft-antispam:** `BCL:0;ARA:14566002|8062599012|8060799015|19110799012|15080799012|15030799006|31061999003|461199028|51005399003|51015399003|39105399003|3412199025|440099028|40105399003|102099032;`

**x-microsoft-antispam-message-info:** `AktAYY/eMa10EkSQW4SK8b999lUSHYvWz4ShXV5vVwWkizHzzJZduQB5zd5LbSTZa4Rjj/a0oHzBBhEQL4Em4mIPvjLOhe8lJi6u6m8BOqvvjVYG4hxsHdlhwZp0smSvrlb83jRcg+lqq7WBdoV0Kkggy34CkAgFAcxbkCC0O5Qi24W6/i9T6WsZZHcPDhuzyPlAIzj7gUMd5r6zRWHcNrItdNYaPN+BfoV0hvN4IXBdcgVz4mwvUk2rBVU5io/QfYK5f7w84DbuM2bfW6KzBAcOQLe4RrXQabTPulCQCcDjJvmJRciStusDWEAMkQUqaV+8YCxwetNNYQ6rKlVQDFagReXpGGTHjn0UtBDvTCUyYOVNC6fEKdnjbajhIBv7UpY2XxsZB0u6hItpMIlWaFXmX5PZh2h0bdZZf+3GOPdGFUKMdRzJBOs4Ab/qIzxHVPxSR055kW5Js9g3UYbsTLZTueEyCJEhcbn0XqFYoubFqYH6gQeu6pGRRCSD9m+1cc5Mw9YqP9aFQ2bMX+bredN7UQdrRswa/lraam9B1NAvxknJGoWfWXWb0/HFkhmBYIqsyBambbmAefJy5QgNDJtAH+94KXLusD42iZZEA8S8F4IP+iBD+e1dPyDZ8qZAWJ1c3ZKxPALcy7HZtWCoHU20C6hmNrTFx6KN6lW8S44rI0sgpcaw9rrnoV4ASrcbzLieOEuZU7K0g9lTbMzpoRsYlMtuESX8LTPp9PWZLFJWH4PvKRMhyigXRnU6ksfuhoi8X0hEEQvRjYJwHG9TWXYTR/46vDjy9lxM5ItATHMvpfnCIEXdlbDtw3BeQwPrpZbwp/thWfqMjjMSmJO1f7KDbIVn+ihgTqONUpVWDPq2HZKNcspNjB0n8vXAbmnowmzkVWT3aO4uJ3jgsvaXd8NjlFvTbdJjhi7XZi2j6iL/dSn7yt1k6myYnNWQnL5I03x8x4NV9JDfdsnH48i5WgEzv2JZDavi9/KHa9tygcuEhoXDNVVfYyc2U/7lg9E5/Bx3OQhjHnqrqIE/E6EYEhV8qai2XOnOkF7uJ05grYYUW7xQFV038uE5ZkRTZhX1CR/S2b+ZbrxgQL+26jPdJzWL++C/B3yNfSg94RDfX/gHaeoz/luwNO60Lph4kxPKY5GkhmvZRVtlgf3mCDPicvF7XsJ2TFOm/CPGo0RW/QTlKja8aEfmHyNqw3AwfuSx5Hoqi1TGWQbSwKkN0s6j+GVOoxnG59XIfSKHvq3jtIDm5/gQQLUSsp0Ix0If1W8BWmxAdc3ieikpeYARDA0bZg==`

**x-ms-exchange-antispam-messagedata-chunkcount:** `1`

**x-ms-exchange-antispam-messagedata-0:** `c3RGlZqXWtrW92NVsXOAyuGZxQkhDiairD+Zq8q40v9dK5Kyax7u0Tr+szJZA45hb65fsyz39WX3D0XAWFe+CwrV3a9kBdjD0iWGne8qDH1SJxJUygEfVJ5r76CXtEKEC1IMFIxPlvY0JD8oYOUuggRQAT8tLwcoq8Iq2yONtnNAsemzA60qGMurGfeg3CVPnBHE5NNFLsPsfnBMBuIgXShINNXnYqqirSIr29/OfDtW3Qtc9IzxomMGB1/EapSUd6dpAtTaOKR2lN4pgNesUCZULSjQe9aqyO6lctYwAxBCWw0UqQRgMr25/RZpvrSDfgAgQOsFwSdm7JONxSOX40eOG7kn6jSxMVwVc8H8IiV+FehRD6KdswktmaMbwwPL+WnnTC0LpueN/jM7mRu0Z3JmGs7R2UBxz4Tipi80PmfEeJWqSgh0jaHo8MYqdK6F5nbQxeEHxxe2KlemAkqE7svQtdj7QRfbQevZaaFIWSsSdilZrkPHUrJsX44jnZ5c0RtSWIW6U3pFLL1jpupFYN40kN5uUpAcMfGDvxeRJutrT1A/SriQ62nRahK+B14Mae0ee01P/zX0kHnHszgOdqnWqn8oCBecAUcmtHIZTpuYHgInaqCqObix9Q3LKcP3hula36bbfJEuKhmAIPsNHb6qpogZYqmmcm2Nl0/sEs1EsjE0Zrt8oPiDZnJFw+GpS+Dzp//eZzcQAu4VLZuP26KG1lvTJeUSy3WIV42IjtHKQRpeO7KW+5zP9XsLPldFKFW6XQSQLd544Tx5RZ4a0YCjq968SeYeTbGiYrXmh2ULe1gigbXRV9KHS072mFHdjOcbtDzO7KM7zlm+3E0a4jhN5y03pOyFPMa2nr6huzcXR9RM9go3dcF3HKe2AAp9D6JAhK4N+HzJhUvKWrbFKfLsjCgwSt86LylFQYvMNJsmv4tBzssuf0h5t3W3X8j5Wrhme9srefP+DbSN7wvNwEXxMJ7Wt1GKZ3Uc1gQufKY4UVBDEgl3Ho+9ZsdDei58TwKDifvSmt1OE7kTfu0TfF5FAWeplNZaYwCDbcLGpTIBHGZEkctQngaF8yJFjHR2jzeWRcxMm6gEwavvjE3d/YNSo34qTbI597XO6nRzyFnrZkEDiSmoNQskUhygjptL3oQ9z8pP+lRmwSns7Dfaqe/8Ouz8d4ErqVuO4KTbEnj+P4NlTzNNmdfyAYb0RRdSmlBfg644d6waX589hsoRMrr73he6kLWKt6mf3Bvjk59fPOy5b45wXDYk5GfTa4H+`

**Content-Type:** `multipart/alternative; boundary="_000_SEZPR01MB681741B6CE49E9734E9E696C9A04ASEZPR01MB6817apcp_"`

**MIME-Version:** `1.0`

</details>

## Email Content

```
Hello,
Hope you are doing well.
I am SEO Consultant from a leading Search Engine Optimization (SEO) Company.
Would you like to increase the leads/sales generated from your website or want to become first page ranking on Google, Yahoo & Bing. We can help you to promote your website.
May I send you a quote? If interested.
Thanks & Regards,
Vandna



---

[HTML Content - Cleaned]
P {margin-top:0;margin-bottom:0;} 

Hello,

Hope you are doing well.

I am SEO Consultant from a leading Search Engine Optimization (SEO) Company.

Would you like to increase the leads/sales generated from your website or want to become first page ranking on Google, Yahoo & Bing. We can help you to promote your website. 

May I send you a quote? If interested.

Thanks & Regards,

Vandna
```

## File Information

- **Filename:** `s5ct039g8862airrr92jjifmvsfblio8efckauo1`
- **Size:** 12585 bytes
- **Processed:** 2025-09-03 16:11:35 UTC


---

# Email: `uq48btp24lqsmtlnnj29ka9josj8674ibtoepkg1`

## Email Headers

**From:** `Capital One <capitalone@secure.net>`

**To:** `zingerpie@kfcreview.com`

**Subject:** `Woo! Your Credit/Refund has posted`

**Date:** `Wed, 03 Sep 2025 11:50:37 -0400`

**Message-ID:** `<20250903115037.76A34CB9D774DCC3@secure.net>`

<details>
<summary>Additional Headers</summary>

**Return-Path:** `<capitalone@secure.net>`

**Received:** `from secure.net (static-96-243-17-74.bflony.fios.verizon.net [96.243.17.74]) by inbound-smtp.us-east-2.amazonaws.com with SMTP id uq48btp24lqsmtlnnj29ka9josj8674ibtoepkg1 for zingerpie@kfcreview.com; Wed, 03 Sep 2025 15:50:38 +0000 (UTC)`

**Received-SPF:** `none (spfCheck: 96.243.17.74 is neither permitted nor denied by domain of secure.net) client-ip=96.243.17.74; envelope-from=capitalone@secure.net; helo=secure.net;`

**Authentication-Results:** `amazonses.com; spf=none (spfCheck: 96.243.17.74 is neither permitted nor denied by domain of secure.net) client-ip=96.243.17.74; envelope-from=capitalone@secure.net; helo=secure.net; dmarc=none header.from=secure.net;`

**MIME-Version:** `1.0`

**Content-Type:** `multipart/related; boundary="----=_NextPart_000_0012_4D7561C5.0CD71767"`

</details>

## Email Content

```
[HTML Content - Cleaned]
Get ready for your payment due on December 18, 2024. ? ? ? ? ? ? ? ? ? ? ? ? ?  ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?  ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?  ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?  ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?  ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?

Your Credit/Refund has posted.

Dear Card Member,
Merchant Credit/Refund was issue to your account.

For Safety Reason, Please Click Here to Confirm to review issued payment 

Click Here to Confirm 

Update and verify your account ownership is required as a means to accept the credit payment
Notice:  Account wlll be credited within 24hrs after you verify your ownership                     This is an electronically generated email

Sincerely,Capital One Customer Service Team.

Download the Capital One Mobile app.

About this message
Unsubscribe with one click if you no longer want to receive this account alert.
If you are past due on your account, view additional disclosures that may apply to you. There is a basic version of this statement noti?cation email available. If you want to switch noti?cation versions, sign in to your account and select Security Alerts.The site may be unavailable during normal maintenance or due to unforeseen circumstances.Please visit our Set Alerts page to modify your alerts subscription preferences.Web access is needed to use mobile banking. Check with your service provider for details of speci?c fees and charges.

Important information from Capital One
Contact us   |  Privacy   |  Help prevent fraud
To ensure delivery, add capitalone@notification.capitalone.com to your address book.
This email was sent to zingerpie@kfcreview.com and contains information directly related to your account with us, other services to which you have subscribed, and/or any application you may have submitted.
Capital One does not provide, endorse or guarantee any third-party product, service, information or recommendation listed above. The third parties listed are not affiliated with Capital One and are solely responsible for their products and services. All trademarks are the property of their respective owners.
Please do not reply to this message, as this email inbox is not monitored. To contact us, visit www. capitalone.com/help-center/contact-us.
Products and services are offered by Capital One, N.A.
 2024 Capital One. Capital One is a federally registered service mark.
PSOSRE 45541 2765001 3 
TP1001
```

## File Information

- **Filename:** `uq48btp24lqsmtlnnj29ka9josj8674ibtoepkg1`
- **Size:** 67233 bytes
- **Processed:** 2025-09-03 16:11:35 UTC


---



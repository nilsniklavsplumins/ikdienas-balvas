# Ikdienas balvas

## Projekta pārskats
Šis projekts automatizē ikdienas atlīdzību pieprasīšanas procesu dažādās vietnēs un ļauj izstrādāt moduļus, kas ļauj pieprasīt ikdienas balvas vietnēs, kuras jau nav iestrādātas šajā projektā.

Projekts tika izveidots, lai uzlabotu lietotāja pieredzi un samazinātu nepieciešamību manuāli veikt rutīnas darbības.

Lūdzu, ņemiet vērā, ka šīs programmas izmantošana var pārkāpt noteiktu vietņu lietošanas noteikumus. Projekts izstrādāts ar nolūku to izmantot tikai izglītojošiem mērķiem.

## Programma nodrošina:
- Automatizētu pieslēgšanos dažādām vietnēm.
- Pret botu mehānismu un captcha apiešanu.
- Saderību ar selenium automatizāciju.
- Lietotājam draudzīgu konsoles tipa saskarni.

## Izmantotās bibliotēkas
Pirms programmas palaišanas pārbaudiet, vai ir instalētas šādas bibliotēkas:

- `2captcha_python==1.2.2`
- `pyotp==2.9.0`
- `seleniumbase==4.22.3`

Tās var instalēt izmantojot komandu:

```bash
pip install -r requirements.txt
```

Katras bibliotēkas izvēle ir balstīta uz to spēju efektīvi veikt noteiktas automatizācijas skriptā nepieciešamās funkcijas.

### `2captcha_python`
`2captcha_python` ir klients 2Captcha servisam, kas ir pakalpojums, kas piedāvā CAPTCHA atrisināšanu. Šī bibliotēka ļauj programmai atrisināt CAPTCHA, lai autorizētos noteiktās vietnēs.

### `pyotp`
`pyotp` nodrošina rīkus vienreizējo paroļu ģenerēšanai un pārbaudei, kas atbilst TOTP (Time-Based One-Time Password) standartam. Šī bibliotēka nodrošina autorizāciju vietnēs, kurās nepieciešama divu faktoru autentifikācija.

### `seleniumbase`
`SeleniumBase` ir moderns testēšanas un automatizācijas rīks, kas veidots uz `selenium` bibliotēkas bāzes. Tas piedāvā paplašinātas funkcijas, piemēram, vienkāršotu elementu atrašanu un darbības ar tiem, kā arī pārluka loga pārvaldības funkcijas. Šajā projektā `SeleniumBase` tiek izmantots, lai automatizētu pārlūkprogrammas darbības, piemēram, lapas atvēršanu, datu ievadīšanu un citas darbības ar vietnes elementiem.

## Kādas darbības nepieciešams veikt pirms programmas palaišanas?

1) Nepieciešams instalēt projektā izmantotās bibliotēkas.
2) Nepieciešams izveidot `secret.json` failu, kas sastāv no masīva, kurš iekļauj zemāk norādīto datu struktūru katrai vietnei.
    ```json
    {
        "id": "šeit ievadīt vietnes identifikatoru",
        "username": "šeit ievadīt vietnes lietotājvārdu",
        "password": "šeit ievadīt vietnes paroli",
        "totp": "šeit ievadīt vietnes totp base32 noslēpumu, ja nepieciešama divu faktoru autentifikācija"
    }
    ```
    Projektā iekļauto vietņu identifikatori:
    - Allkeyshop - `discord`
    - Coingecko - `coingecko`
    - MSI rewards - `msi`
3) Ja kādā no vietnēm nepieciešams automatizēt CAPTCHA, izveidot `.env` failu, kas iekļauj `APIKEY_2CAPTCHA` atslēgu.

    `.env` faila nepieciešamība vietnēm, kas iekļautas projektā:
    - Allkeyshop ❌
    - Coingecko ❌
    - MSI rewards ✅

## Vēlies papildināt projektu?

Izlasi `LICENSE`, lai noskaidrotu ierobežojumus.
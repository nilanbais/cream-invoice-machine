# cream-invoice-machine

Repository containing the CreamInvoiceMachine. A small pack of functionality to create a standardised invoice based on inpuit parameters.


# For the Cream
This is the documentation for the homie. Her you'll find info about the process, the input structure and how to use the whole shitstorm.

## input data
The input data can be decvided into three parts: job info, product info, and corp info. We'll discuss all.

The format (for now) is YAML. Important for you is to strictly follow the given structure of the files.

### job info
Job info is information relating to one specific job. This is the file to specify the details of a single job.
```yaml
invoice: test-invoice-number
date: auto  # 'auto' genereert de datum waarop de factuur gemaakt is (code gerund is)
klant:
    - naam: Dennis
    - adres: 0223 woning 101B
    - postcode: 2020 BZ
    - plaats: Fuck Texel
werkzaamheden:
    - pleister:  # opties: pleister, betonstuc, raapwerk, sauzen, spuitklaar
        - m2: 10
        - uren: 16
    - pleister:
        - m2: 4
        - uren: 3
    - betonstuc:
        - m2: 4
        - uren: 30
producten:
    - pleister type 1:
        - aantal: 0,5 L
    - voorspul type 3:
        - aantal: 1 unit  # unit voor het duiden van een verpakking    
    - betonstuc type 3:
        - aantal: 1 unit  
```

### product info
Reference information that is used in the automated calculations.

```yaml
Gyproc Stucpasta 1:
    - EAN nummer: 8711149001750
    - unit: 20 kg
    - prijs: €54.49   # '€' -> altgr + 5
Gyproc Stucpasta 2:
    - EAN nummer: 8711149001743
    - unit: 5 kg
    - prijs: €15.49   # '€' -> altgr + 5
```

### corp info

Reference information that is used in generating the invoice.
```yaml
naam: Kramer & Homeboii.
adres: Adressssssss
postcode: 0223 GG
plaats: D-City
btw-nummer: XXtest123SKRT
bankrekekningnummer: RABO 0800 JATOCH
```
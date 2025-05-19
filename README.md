# Handleiding Cream Invoice Machine

Deze handleiding beschrijft hoe je de Cream Invoice Machine kunt gebruiken om gestandaardiseerde offertes te genereren voor stukadoorswerkzaamheden. De tool maakt het mogelijk om op basis van een YAML-invoerbestand automatisch een offerte in PDF-formaat te genereren.

## Invoerbestand (input.yaml)

Het invoerbestand is het belangrijkste onderdeel van de Cream Invoice Machine. Dit bestand bevat alle informatie die nodig is om een correcte offerte te genereren. Het bestand moet worden opgeslagen in de map 'input' en moet de YAML-structuur volgen zoals hieronder beschreven.

### Verplichte structuur van het invoerbestand

Het invoerbestand moet de volgende hoofdsecties bevatten:

```yaml
invoice: [factuurnummer]
uitvoerder: [naam van het stukadoorsbedrijf]
date: auto
klant-info:
  naam: [naam van de klant]
  adres: [adres van de klant]
  postcode: [postcode van de klant]
  plaats: [woonplaats van de klant]
werk:
  wanden:
    [ruimte1]: [aantal vierkante meters]
    [ruimte2]: [aantal vierkante meters]
    # meer ruimtes indien nodig
  plafond:
    [ruimte1]: [aantal vierkante meters]
    # meer ruimtes indien nodig
  microcement: [aantal vierkante meters]
  hoeknaden: [aantal meters]
extra:
  btw: [btw-percentage]
  onvoorzien:
    afronding: [afrondingsbedrag]
    bijtelling: [bijtellingsbedrag]
```

### Toelichting op de verplichte velden

- **invoice**: Het factuurnummer of offertenummer. Dit is een unieke identificatie voor de offerte.
- **uitvoerder**: De naam van het stukadoorsbedrijf dat de werkzaamheden uitvoert.
- **date**: Wanneer ingesteld op "auto" wordt de huidige datum automatisch gebruikt bij het genereren van de offerte.
- **klant-info**: Sectie met alle gegevens van de klant.
  - **naam**: De volledige naam van de klant.
  - **adres**: Het volledige adres van de klant.
  - **postcode**: De postcode van het adres van de klant.
  - **plaats**: De woonplaats van de klant.
- **werk**: Sectie met alle uit te voeren werkzaamheden.
  - **wanden**: Subsectie voor stucwerk aan wanden, opgedeeld per ruimte met het aantal vierkante meters.
  - **plafond**: Subsectie voor stucwerk aan plafonds, opgedeeld per ruimte met het aantal vierkante meters.
  - **microcement**: Het totale aantal vierkante meters microcement dat wordt aangebracht.
  - **hoeknaden**: Het totale aantal meters hoeknaden dat wordt afgewerkt.
- **extra**: Sectie met aanvullende informatie voor de offerte.
  - **btw**: Het toe te passen btw-percentage.
  - **onvoorzien**: Subsectie voor onvoorziene kosten.
    - **afronding**: Bedrag voor afronding van de offerte.
    - **bijtelling**: Extra bedrag dat wordt toegevoegd aan de offerte.

### Voorbeeld van een correct invoerbestand

Hieronder volgt een voorbeeld van een correct invoerbestand:

```yaml
invoice: 2023-001
uitvoerder: Stucadoorsbedrijf Vader & Zn.
date: auto
klant-info:
  naam: Familie Jansen
  adres: Voorbeeldstraat 123
  postcode: 1234 AB
  plaats: Amsterdam
werk:
  wanden:
    woonkamer: 43
    keuken: 11
    slaapkamer-1: 19
    slaapkamer-2: 25
  plafond:
    woonkamer: 40
    hal: 6
  microcement: 8
  hoeknaden: 13
extra:
  btw: 9
  onvoorzien:
    afronding: 10
    bijtelling: 0
```

## Starten van de offertegenerator

Om de offertegenerator te starten, moet je het bestand `dubbelklik_deze_windows.bat` dubbelklikken. Dit batchbestand zorgt voor het volgende:

1. Het controleert of Python 3.12 is geïnstalleerd en installeert dit indien nodig.
2. Het maakt een virtuele Python-omgeving aan als deze nog niet bestaat.
3. Het installeert alle benodigde afhankelijkheden uit het requirements.txt-bestand.
4. Het start het Python-script dat de offertegenerator uitvoert.

Het batchbestand is ontworpen om alle benodigde stappen automatisch uit te voeren, zodat je geen handmatige configuratie hoeft te doen. Na het dubbelklikken van het bestand wordt je door het proces geleid met informatieve berichten in het opdrachtvenster.

### Belangrijke opmerkingen bij het starten

- Zorg ervoor dat je het batchbestand uitvoert vanuit de hoofdmap van het project.
- Het programma zal alle YAML-bestanden in de map 'input' verwerken en voor elk bestand een offerte genereren.
- De gegenereerde offertes worden opgeslagen als PDF-bestanden in de hoofdmap van het project.
- Als er fouten optreden tijdens het genereren, worden deze weergegeven in het opdrachtvenster.

## Aanpassen van het invoerbestand

Je kunt een bestaand invoerbestand kopiëren en aanpassen voor een nieuwe offerte. Zorg ervoor dat je de structuur intact houdt en alle verplichte velden invult. Je kunt ruimtes toevoegen of verwijderen in de secties 'wanden' en 'plafond' naar behoefte, afhankelijk van de specifieke werkzaamheden voor de klant.

Sla het aangepaste bestand op in de map 'input' met een duidelijke naam, bijvoorbeeld 'klant_naam_datum.yaml'. Wanneer je vervolgens de generator start, wordt voor dit bestand automatisch een offerte gegenereerd.

## Problemen oplossen

Als er problemen optreden bij het genereren van offertes, controleer dan het volgende:

1. Zorg ervoor dat het invoerbestand correct is opgemaakt volgens de YAML-syntax.
2. Controleer of alle verplichte velden aanwezig zijn in het invoerbestand.
3. Zorg ervoor dat numerieke waarden geen aanhalingstekens bevatten.
4. Als het batchbestand niet start, probeer het dan met rechtermuisklik en 'Als administrator uitvoeren'.

Als dit niet werkt, bel.

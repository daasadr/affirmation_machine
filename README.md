# Subliminal Generator

Jednoduchý nástroj pro generování podprahových nahrávek s afirmacemi.

## Komunikace s podvědomím pomocí afirmací

Piš velmi jednoduchá prohlášení v pozitivním tvaru, tedy nezmiňuj vůbec slova, která nechceš přivolat jako problémy, starosti - tato slova vůbec nepoužívej. Představ si, jakým způsobem je podvědomí vnímavé ke slovům během snu - podvědomí skutečně funguje a vnímá jinak než vědomá mysl, nad věcmi nepřemýšlí, jen je zapisuje, takže čím nejjednodušší a čím víc citově pro sebe zabarvená slova použiješ, tím snadněji se jich podvědomí chytne, vezme je za své a v životě ti je uskuteční.

### Příklady účinných prohlášení (první osoba)

```
Peníze mi dělají radost.
Mám hodně peněz.
Bohatnu rychle.
Dostávám peníze každý den a dělá mi to radost.
Jsem geniální programátorka.
Je to pro mě snadné dělat úspěšné projekty.
Moje apka má úspěch a vydělává.
```

### Příklady prohlášení v druhé osobě

```
Máš ohromné úspěchy se svými projekty.
To je skvělé kolik teď vyděláváš.
Právě teď se to pro tebe mění a odteď vyděláváš 50€ za den.
Jsi nejšťastnější člověk na světě.
```

### Tipy pro efektivní afirmace

- Můžete kombinovat různé osoby (já/ty/třetí osoba)
- Pro třetí osobu použijte své jméno (např. "Dáša je vážně úspěšná")
- Podvědomí je třeba přesvědčit o tom, že je to skutečnost
- Používejte afirmace pravidelně po dobu alespoň 21 dní
- Pište afirmace v přítomném čase, jako by se to už dělo
- Vyhněte se negacím a slovům s negativním významem

## Požadavky

- Python 3.11 nebo novější
- FFmpeg (pro práci se zvukem)

## Instalace

1. Nainstalujte Python 3.11 z [oficiálních stránek](https://www.python.org/downloads/release/python-3116/)

   - Při instalaci zaškrtněte "Add Python to PATH"

2. Nainstalujte FFmpeg:

   - Stáhněte FFmpeg z [oficiálních stránek](https://ffmpeg.org/download.html)
   - Rozbalte do složky (např. `C:\ffmpeg`)
   - Přidejte cestu `C:\ffmpeg\bin` do systémové proměnné PATH

3. Stáhněte tento projekt:

   - Klikněte na zelené tlačítko "Code"
   - Vyberte "Download ZIP"
   - Rozbalte stažený soubor

4. Nainstalujte potřebné knihovny:
   - Otevřete příkazový řádek ve složce projektu
   - Spusťte příkaz:
     ```
     pip install -r requirements.txt
     ```

## Použití

1. Spusťte aplikaci:

   ```
   python subliminal_generator.py
   ```

2. Do textového pole zadejte afirmace (jedna na řádek)

3. Volitelně můžete:

   - Vybrat zvukový podkres (podporované formáty: MP3, WAV)
   - Nastavit hlasitost hlasu pomocí posuvníku

4. Klikněte na "Vygenerovat nahrávku" a vyberte místo pro uložení výsledného MP3 souboru

## Funkce

- Převod textu na řeč v češtině
- Nastavitelná hlasitost hlasu
- Možnost přidat zvukový podkres
- Automatické vytvoření smyčky z podkresu
- Export do MP3 formátu

## Tipy pro použití

- Pro přehrávání ve smyčce přes noc doporučuji použít VLC přehrávač
- Nastavte hlasitost tak, aby byla slyšitelná, ale nerušila spánek
- Afirmace pište v přítomném čase a pozitivně (např. "Jsem sebevědomá" místo "Nebudu se bát")

# Subliminal Generator

Aplikace pro generování subliminálních nahrávek s pozitivními afirmacemi. Tento nástroj umožňuje vytvářet vlastní nahrávky s afirmacemi, přidávat hudební podklad a aplikovat různé audio efekty.

## Funkce

- Generování hlasových nahrávek z textových afirmací
- Přidávání hudebního podkladu
- Nastavení hlasitosti hlasu
- Audio efekty:
  - Fade in/out (postupný nástup/doznívání)
  - Reverb (ozvěna)
- Náhled nahrávky před uložením
- Ukládání do MP3 formátu

## Instalace

1. Ujistěte se, že máte nainstalovaný Python 3.11 nebo novější
2. Stáhněte nebo naklonujte tento repozitář
3. Nainstalujte potřebné knihovny pomocí pip:

```bash
pip install gTTS
pip install pydub
pip install pygame
```

### Další požadavky

Pro správnou funkčnost pydub je potřeba mít nainstalovaný FFmpeg:

#### Windows:

1. Stáhněte FFmpeg z [oficiálních stránek](https://ffmpeg.org/download.html)
2. Rozbalte stažený soubor
3. Přidejte cestu k FFmpeg do systémových proměnných PATH

#### Linux:

```bash
sudo apt-get install ffmpeg
```

#### macOS:

```bash
brew install ffmpeg
```

## Použití

1. Spusťte aplikaci:

```bash
python subliminal_generator.py
```

2. V hlavním okně:

   - Zadejte afirmace (jedna na řádek)
   - Nastavte požadované audio efekty
   - Vyberte hudební podklad (volitelné)
   - Nastavte hlasitost hlasu
   - Klikněte na "Vygenerovat nahrávku"

3. Po vygenerování:
   - Poslechněte si náhled pomocí tlačítka "Náhled nahrávky"
   - Uložte nahrávku pomocí tlačítka "Uložit nahrávku"

## Komunikace s podvědomím pomocí afirmací

Afirmace jsou pozitivní výroky, které pomáhají programovat podvědomí. Pro maximální efektivitu:

1. **Formulujte afirmace v přítomném čase**

   - Správně: "Jsem sebevědomý a úspěšný"
   - Špatně: "Budu sebevědomý a úspěšný"

2. **Používejte pozitivní formulace**

   - Správně: "Jsem zdravý a plný energie"
   - Špatně: "Nejsem nemocný"

3. **Buďte konkrétní**

   - Správně: "Snadno si vydělávám 50 000 Kč měsíčně"
   - Špatně: "Mám hodně peněz"

4. **Přidejte emoční náboj**

   - Správně: "Jsem nadšený z mé nové práce"
   - Špatně: "Mám novou práci"

5. **Opakujte pravidelně**
   - Ideální je poslouchat nahrávku 1-2x denně
   - Nejlépe ráno po probuzení a večer před spaním

## Řešení problémů

### Problémy s přehráváním

- Ujistěte se, že máte nainstalovaný pygame
- Zkontrolujte, zda máte správně nastavené zvukové výstupní zařízení

### Problémy s generováním

- Zkontrolujte, zda máte nainstalovaný FFmpeg
- Ujistěte se, že máte připojení k internetu (potřebné pro gTTS)

## Licence

Tento projekt je licencován pod MIT licencí - viz soubor [LICENSE](LICENSE) pro detaily.

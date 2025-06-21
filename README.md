# 🚀 ScamScanner-Extension

**Browser extension + backend for the ScamScanner project**

![ScamScanner Logo](extension/icons/icon.png)

---

## 📦 Spis treści
1. [Opis projektu](#opis-projektu)
2. [Funkcjonalności](#funkcjonalnosci)
3. [Instalacja](#instalacja)
4. [Uruchomienie](#uruchomienie)
5. [Uzycie](#uzycie)
6. [Budowanie instalatora](#budowanie-instalatora)
7. [Struktura katalogow](#struktura-katalogow)
8. [Wklad](#wklad)
9. [Licencja](#licencja)

---

## 📝 Opis projektu
ScamScanner-Extension to **rozszerzenie przegladarki** wspierane przez niewielki lokalny backend oparty na FastAPI. Pozwala blyskawicznie analizowac tresci stron, korzystajac z modeli LLM oraz bazy embeddingow.

---

## ⚙️ Funkcjonalnosci

* 🔍 Analiza zaznaczonego tekstu lub calej strony
* 🤖 Generowanie odpowiedzi lokalnym modelem (lista modeli w popupie)
* 🛠️ Wybór modeli (GPT-2, DistilGPT-2, LLaMA 2, Mistral 7B, GPT4All Vicuna)
* 🧠 Prosty magazyn embeddingów (bag‑of‑words; docelowo `sentence-transformers` + FAISS)
* 🗄️ Endpointy `/ingest` i `/search` do zarzadzania baza wektorowa
* ✅ Opcjonalny fact-checking i proste pipeline'y aktualizacji danych
* 🎨 Czytelny interfejs z panelem postepu i czasem analizy
* 🌐 Calkowicie offline (bez koniecznosci kluczy API)

---

## 🚀 Instalacja

### 1. Backend

```bash
cd backend
pip install -r requirements1.txt
```

### 2. Frontend (rozszerzenie)

1. Przejdz do katalogu `extension`:

   ```bash
   cd extension
   ```
2. Upewnij sie, ze w folderze `icons/` znajduja sie pliki ikon (16/48/128 px).

### 3. Budowanie instalatora

Automatyczna budowe zapewnia skrypt `scripts/build_installer.py`. Uruchom go z katalogu glownego:

```bash
python scripts/build_installer.py
```

Skrypt tworzy samodzielny plik wykonywalny backendu (PyInstaller), a na Windows dodatkowo generuje instalator NSIS w folderze `dist/`.

---

## ▶️ Uruchomienie

### Backend

```bash
cd backend
uvicorn server:app --host 0.0.0.0 --port 8000
```

### Przegladarka

1. Otworz `chrome://extensions` (lub `about:debugging` w Firefox).
2. Wlacz **Tryb programisty/Developer Mode**.
3. Wybierz **Load unpacked** i wskaz folder `extension/`.

---

## 🎯 Uzycie

1. Wejdz na dowolna strone z tekstem.
2. Kliknij ikone rozszerzenia ScamScanner.
3. Wybierz model z listy w popupie i nacisnij **Analizuj strone**.
4. Na gorze strony pojawi sie panel z informacja o postepie i czasem.
5. Po zakonczeniu otrzymasz wynik analizy w tym samym panelu.
6. Dokumenty mozna dodawac poprzez endpoint `/ingest`, a wyszukiwanie wykonac przez `/search`.

---

## 📂 Struktura katalogow

```text
.
├── backend
│   ├── server.py       # API FastAPI + obsluga modeli
│   ├── embedding.py    # magazyn wektorow FAISS
│   ├── model_factory.py
│   ├── planner.py
│   └── requirements1.txt
├── extension
│   ├── icons/
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   ├── content.js
│   └── inject.css
└── scripts
    └── build_installer.py
```

---

## 🙌 Wklad

Chetnie przyjmiemy **pull requesty** i sugestie! Jesli cos nie dziala, zglos issue lub napisz:

* ✉️ Mail: [twoj.email@example.com](mailto:twoj.email@example.com)
* 🐦 Twitter: [@twoj_profil](https://twitter.com/twoj_profil)

---

## 📜 Licencja

Projekt dostepny na licencji **MIT**. Szczegoly w pliku [LICENSE](LICENSE).


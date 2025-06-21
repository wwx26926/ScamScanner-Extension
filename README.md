# 🚀 ScamScanner-Extension

**Desktop GUI and backend for the ScamScanner project**

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
ScamScanner-Extension to **okienkowa aplikacja** wspierana przez niewielki lokalny backend oparty na FastAPI. Pozwala analizowac linki do artykulow, wyszukiwac potwierdzenia w zrodlach i generowac podsumowanie.

---

## ⚙️ Funkcjonalnosci

 xviqcm-codex/rozwiązać-problem-z-dodatkiem-do-przeglądarki
* 📎 Wklej link do artykulu i pobierz tresc
* 🤖 Generowanie podsumowania lokalnym modelem LLM
* 📚 Wyszukiwanie powiazanych fragmentow z NewsAPI
* 🧠 Baza embeddingow FAISS jako kontekst
* ✅ Opcjonalny fact-checking
* 🎨 Prosty interfejs okienkowy
* 🌐 Dziala w trybie offline (bez NewsAPI)

* 🔍 Analiza zaznaczonego tekstu lub calej strony
* 🤖 Generowanie odpowiedzi lokalnym modelem (lista modeli w popupie)
* 🛠️ Wybór modeli (GPT-2, DistilGPT-2, LLaMA 2, Mistral 7B, GPT4All Vicuna)
* 🧠 Prosty magazyn embeddingów (bag‑of‑words; docelowo `sentence-transformers` + FAISS)
* 🗄️ Endpointy `/ingest` i `/search` do zarzadzania baza wektorowa
* ✅ Opcjonalny fact-checking i proste pipeline'y aktualizacji danych
* 🎨 Czytelny interfejs z panelem postepu i czasem analizy
* 🌐 Calkowicie offline (bez koniecznosci kluczy API)

* 🔍 Analiza zaznaczonego tekstu lub całej strony
* 🤖 Generowanie odpowiedzi lokalnym modelem (możliwość wyboru w popupie)
* 🌐 Integracja z backendem FastAPI
* 🔒 Całkowicie offline (bez konieczności kluczy API)
* 🎨 Prosty interfejs użytkownika
* 🛠️ Łatwe przełączanie modeli (LLaMA 2, Mistral, GPT4All)
* 🧠 Wyszukiwanie w bazie embeddingów (FAISS)
* 🗄️ API do dodawania dokumentów i zapytań
* ✅ Opcjonalny fact-checking przed zwróceniem odpowiedzi
main

---

## 🚀 Instalacja

# ScamScanner

Uniwersalna instrukcja instalacji i uruchomienia projektu **ScamScanner** (backend + aplikacja okienkowa).

---

## 0. Wymagania wstępne

* Python 3.8+
* Git (opcjonalnie, jeśli chcesz klonować repo)
 xviqcm-codex/rozwiązać-problem-z-dodatkiem-do-przeglądarki
 
* Przeglądarka Chrome, Edge lub Firefox
 main
* (Windows) Uprawnienia do zmiany Execution Policy w PowerShell

---

## 1. Pobranie i rozpakowanie projektu

1. Pobierz archiwum `ScamScanner-Extension-main.zip` i rozpakuj je w wybranym katalogu, np.:

   * **Windows**: prawy-klik → Wyodrębnij wszystkie → wybierz folder (np. `C:\Projects\ScamScanner`)
   * **macOS/Linux**: w terminalu:

   ```bash
   unzip ~/Pobrane/ScamScanner-Extension-main.zip -d ~/Projects/ScamScanner
   ```
2. Przejdź do katalogu projektu:

   ```bash
   cd /ścieżka/do/ScamScanner-Extension-main
   ```

---

## 2. Backend (FastAPI + Python)

### 2.1 Utworzenie i aktywacja środowiska wirtualnego

| System                      | Tworzenie venv         | Aktywacja venv             |
| --------------------------- | ---------------------- | -------------------------- |
| **Windows**                 | `py -3 -m venv venv`   | \`.                        |
| venv\Scripts\Activate.ps1\` |                        |                            |
| **macOS/Linux**             | `python3 -m venv venv` | `source venv/bin/activate` |

> **Uwaga (Windows)**: jeśli aktywacja zgłasza błąd o polityce skryptów, uruchom PowerShell jako Administrator i wykonaj:
>
> ```powershell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### 2.2 Instalacja zależności

1. Przejdź do folderu `backend`:

   ```bash
   cd backend
   ```
2. Upewnij się, że środowisko wirtualne jest aktywne (`(venv)` w promptcie), a następnie:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements1.txt
   ```

### 2.3 Konfiguracja kluczy

W katalogu `backend` utwórz plik `.env` z następującą zawartością:

```ini
OPENAI_API_KEY=TWÓJ_KLUCZ_OPENAI
NEWSAPI_KEY=TWÓJ_KLUCZ_NEWSAPI
```

Klucze uzyskasz w panelu OpenAI i na NewsAPI.org.

### 2.4 Uruchomienie serwera

W katalogu `backend` uruchom:

```bash
uvicorn server:app --host 0.0.0.0 --port 8000
```

Powinieneś zobaczyć komunikat, że FastAPI nasłuchuje na porcie 8000.

### 2.5 Szybki start
xviqcm-codex/rozwiązać-problem-z-dodatkiem-do-przeglądarki

W głównym katalogu projektu uruchom aplikację jednym poleceniem:

```bash
python run_gui.py
```
---

W głównym katalogu projektu możesz uruchomić backend i otworzyć przeglądarkę z wczytanym rozszerzeniem jednym poleceniem:

```bash
python start.py
```

---

## 3. Rozszerzenie do przeglądarki

1. Otwórz stronę zarządzania rozszerzeniami w przeglądarce:

   * **Chrome**: `chrome://extensions/`
   * **Edge**: `edge://extensions/`
   * **Firefox**: `about:debugging#/runtime/this-firefox`
2. Włącz tryb dewelopera / Developer mode.
3. **Chrome/Edge** – kliknij **Load unpacked** i wskaż katalog `extension` (tam, gdzie znajduje się `manifest.json`).
   **Firefox** – kliknij **Load Temporary Add-on** i wybierz plik `manifest.json` z katalogu `extension`.
   Jeśli przeglądarka nie pozwala wybrać pliku lub katalogu, upewnij się, że cały projekt został wcześniej rozpakowany z archiwum ZIP.
4. Po załadowaniu zobaczysz ikonę rozszerzenia na pasku narzędzi.
main

---

## 4. Test

1. Uruchom `python run_gui.py`.
2. W oknie wklej adres artykułu i kliknij **Analyze**.
3. Po chwili zobaczysz wynik.

---

## 5. Najczęstsze problemy

* **`python` lub `pip` nieznane**:

  * Windows: użyj `py -3` zamiast `python`
  * macOS/Linux: upewnij się, że `python3` jest zainstalowane i w PATH
* **Brak `(venv)` w promptcie**:
  upewnij się, że aktywujesz poprawny skrypt `Activate.ps1` lub `activate`
* **Błędy podczas instalacji pakietów**:
  wklej pełny log błędu, pomoże to diagnoza

---

Jeśli coś nadal nie działa – dołącz dokładny komunikat błędu i ścieżkę, w której pracujesz. Powodzenia!

---

## 🎯 Uzycie

1. Uruchom `python run_gui.py`.
2. Wklej link do artykulu w pole.
3. Kliknij **Analyze** i poczekaj na wynik.
4. Dokumenty mozesz dodawac przez `/ingest` a wyszukiwanie wykonywac przez `/search`.
5. Aby uzyc wersji przegladarkowej, uruchom `python start.py` i zaladuj rozszerzenie w trybie deweloperskim.

## 🏗 Budowanie instalatora

Gotowa paczka moze zostac utworzona poleceniem:

```bash
python scripts/build_installer.py
```

## 📂 Struktura katalogow

```text
.
├── backend
│   ├── server.py       # API FastAPI + obsluga modeli
│   ├── embedding.py    # magazyn wektorow FAISS
│   ├── model_factory.py
│   ├── planner.py
│   └── requirements1.txt
├── gui.py
└── tests
    └── test_end_to_end.py
```
Projekt dostepny na licencji **MIT**. Szczegoly w pliku [LICENSE](LICENSE).


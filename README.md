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

* 📎 Wklej link do artykulu i pobierz tresc
* 🤖 Generowanie podsumowania lokalnym modelem LLM
* 📚 Wyszukiwanie powiazanych fragmentow z NewsAPI
* 🧠 Baza embeddingow FAISS jako kontekst
* ✅ Opcjonalny fact-checking
* 🎨 Prosty interfejs okienkowy
* 🌐 Dziala w trybie offline (bez NewsAPI)

---

## 🚀 Instalacja

# ScamScanner

Uniwersalna instrukcja instalacji i uruchomienia projektu **ScamScanner** (backend + aplikacja okienkowa).

---

## 0. Wymagania wstępne

* Python 3.8+
* Git (opcjonalnie, jeśli chcesz klonować repo)
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

W głównym katalogu projektu uruchom aplikację jednym poleceniem:

```bash
python gui.py
```
---

---

## 4. Test

1. Uruchom `python gui.py`.
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

1. Uruchom `python gui.py`.
2. Wklej link do artykulu w pole.
3. Kliknij **Analyze** i poczekaj na wynik.
4. Dokumenty mozesz dodawac przez `/ingest` a wyszukiwanie wykonywac przez `/search`.

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


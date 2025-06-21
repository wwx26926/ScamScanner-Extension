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

 wl279k-codex/wyświetl-wynik-analizy-w-oknie-przeglądarki
* 🔍 Analiza zaznaczonego tekstu lub calej strony
* 🤖 Generowanie odpowiedzi lokalnym modelem (lista modeli w popupie)
* 🛠️ Wybór modeli (GPT-2, DistilGPT-2, LLaMA 2, Mistral 7B, GPT4All Vicuna)
* 🧠 Prosty magazyn embeddingów (bag‑of‑words; docelowo `sentence-transformers` + FAISS)
* 🗄️ Endpointy `/ingest` i `/search` do zarzadzania baza wektorowa
* ✅ Opcjonalny fact-checking i proste pipeline'y aktualizacji danych
* 🎨 Czytelny interfejs z panelem postepu i czasem analizy
* 🌐 Calkowicie offline (bez koniecznosci kluczy API)
=======
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

0. Wymagania wstępne
Python 3.8+

Git (opcjonalnie, jeśli chcesz klonować repo)

Przeglądarka Chrome lub Firefox

(Windows) Uprawnienia do zmiany Execution Policy w PowerShell

1. Pobranie i rozpakowanie projektu
Pobierz archiwum ScamScanner-Extension-main.zip i rozpakuj je w wybranym katalogu, np.

Windows: prawy-klik → Wyodrębnij wszystkie → wybierz folder, np. C:\Projects\ScamScanner

macOS/Linux: w terminalu

bash
Kopiuj
Edytuj
unzip ~/Pobrane/ScamScanner-Extension-main.zip -d ~/Projects/ScamScanner
Przejdź do katalogu projektu:

bash
Kopiuj
Edytuj
cd /ścieżka/do/ScamScanner-Extension-main
2. Backend (FastAPI + Python)
2.1 Utworzenie i aktywacja środowiska wirtualnego
System	Tworzenie venv	Aktywacja venv
Windows	py -3 -m venv venv	.\venv\Scripts\Activate.ps1
macOS/Linux	python3 -m venv venv	source venv/bin/activate

Windows PowerShell: jeśli aktywacja zgłasza błąd o polityce skryptów, uruchom PowerShell jako Administrator i wpisz:

powershell
Kopiuj
Edytuj
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
2.2 Instalacja zależności
Przejdź do folderu backend:

bash
Kopiuj
Edytuj
cd backend
Upewnij się, że venv jest aktywne (powinno być (venv) w promptcie), a następnie:

bash
Kopiuj
Edytuj
python -m pip install --upgrade pip
python -m pip install -r requirements1.txt
2.3 Konfiguracja kluczy
W katalogu backend utwórz plik .env z dwoma kluczami:

ini
Kopiuj
Edytuj
OPENAI_API_KEY=TWÓJ_KLUCZ_OPENAI
NEWSAPI_KEY=TWÓJ_KLUCZ_NEWSAPI
(klucze pobierasz z panelu OpenAI i NewsAPI.org)

2.4 Uruchomienie serwera
Wciąż w backend, uruchom:

bash
Kopiuj
Edytuj
uvicorn server:app --host 0.0.0.0 --port 8000
Powinieneś zobaczyć komunikat, że FastAPI nasłuchuje na porcie 8000.

3. Rozszerzenie do przeglądarki
Otwórz w przeglądarce stronę zarządzania rozszerzeniami:

Chrome: chrome://extensions/

Firefox: about:debugging#/runtime/this-firefox

Włącz tryb dewelopera / Developer mode.

Kliknij „Load unpacked” (Chrome) lub „Load Temporary Add-on” (Firefox) i wskaż folder:

swift
Kopiuj
Edytuj
/ścieżka/do/ScamScanner-Extension-main/extension
Po załadowaniu pojawi się ikona rozszerzenia na pasku narzędzi.

---

## 🎯 Uzycie

1. Wejdz na dowolna strone z tekstem.
2. Kliknij ikone rozszerzenia ScamScanner.
3. Wybierz model z listy w popupie i nacisnij **Analizuj strone**.
4. Na gorze strony pojawi sie panel z informacja o postepie i czasem.
5. Po zakonczeniu otrzymasz wynik analizy w tym samym panelu.
6. Dokumenty mozna dodawac poprzez endpoint `/ingest`, a wyszukiwanie wykonac przez `/search`.

8. Przejdź na dowolną stronę z tekstem.
9. Kliknij ikonę rozszerzenia ScamScanner 🕵️‍♂️.
10. W popupie wybierz model z listy i naciśnij **Scan** 🖱️.
11. Na stronie pojawi się panel z informacją o postępie ⏳.
12. Po zakończeniu zobaczysz wynik oraz czas wykonania analizy 🎉.
13. Dokumenty można dodawać przez endpoint `/ingest` i zapytania przez `/search`.
14. W popupie naciśnij **Scan** 🖱️.
15. Na stronie pojawi się panel z informacją o postępie ⏳.
16. Po zakończeniu zobaczysz wynik oraz czas wykonania analizy 🎉.

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

## 📜 Licencja

Projekt dostepny na licencji **MIT**. Szczegoly w pliku [LICENSE](LICENSE).


# 🚀 ScamScanner-Extension

**Browser extension + backend for the ScamScanner project**

![ScamScanner Logo](extension/icons/icon.png)

---

## 📦 Spis treści

1. [Opis projektu](#opis-projektu)
2. [Funkcjonalności](#funkcjonalności)
3. [Instalacja](#instalacja)
4. [Uruchomienie](#uruchomienie)
5. [Użycie](#użycie)
6. [Struktura katalogów](#struktura-katalogów)
7. [Wkład](#wkład)
8. [Licencja](#licencja)

---

## 📝 Opis projektu

ScamScanner-Extension to **rozszerzenie przeglądarki**, które umożliwia szybkie skanowanie treści stron internetowych pod kątem potencjalnych oszustw. W tle działa **lokalny backend** oparty na FastAPI i modelu `transformers`.

---

## ⚙️ Funkcjonalności

* 🔍 Analiza zaznaczonego tekstu lub całej strony
* 🤖 Generowanie odpowiedzi lokalnym modelem (możliwość wyboru w popupie)
* 🌐 Integracja z backendem FastAPI
* 🔒 Całkowicie offline (bez konieczności kluczy API)
* 🎨 Prosty interfejs użytkownika
* 🛠️ Łatwe przełączanie modeli (LLaMA 2, Mistral, GPT4All)
* 🧠 Wyszukiwanie w bazie embeddingów (FAISS)
* 🗄️ API do dodawania dokumentów i zapytań
* ✅ Opcjonalny fact-checking przed zwróceniem odpowiedzi

---

## 🚀 Instalacja

### 1. Backend

Przejdź do folderu `backend` i zainstaluj wymagane paczki:

```bash
cd backend
pip install fastapi uvicorn transformers
```

### 2. Frontend (rozszerzenie)

1. Przejdź do folderu `extension`:

   ```bash
   cd extension
   ```
2. Usuń wiodące spacje w nazwach plików (jeśli istnieją):

   ```bash
   mv " popup.html" popup.html
   mv " popup.js" popup.js
   ```
3. Upewnij się, że w folderze `icons` znajduje się plik `icon.png`.

---

## ▶️ Uruchomienie

### Backend

```bash
cd backend
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

### Przeglądarka

1. Otwórz `chrome://extensions` (lub `about:debugging` w Firefox).
2. Włącz **Tryb programisty**/**Dev Mode**.
3. Kliknij **Load unpacked** i wskaż folder `extension`.

---

## 🎯 Użycie

1. Przejdź na dowolną stronę z tekstem.
2. Kliknij ikonę rozszerzenia ScamScanner 🕵️‍♂️.
- g4twei-codex/wyświetl-wynik-analizy-w-oknie-przeglądarki
3. W popupie wybierz model z listy i naciśnij **Scan** 🖱️.
4. Na stronie pojawi się panel z informacją o postępie ⏳.
5. Po zakończeniu zobaczysz wynik oraz czas wykonania analizy 🎉.
6. Dokumenty można dodawać przez endpoint `/ingest` i zapytania przez `/search`.
=======
3. W popupie naciśnij **Scan** 🖱️.
4. Na stronie pojawi się panel z informacją o postępie ⏳.
5. Po zakończeniu zobaczysz wynik oraz czas wykonania analizy 🎉.
- main

---

## 📂 Struktura katalogów

```text
.
├── backend
│   ├── server.py       # FastAPI + lokalny model
│   └── requirements.txt
└── extension
    ├── icons
    │   └── icon.png    # ikona rozszerzenia
    ├── manifest.json
    ├── popup.html
    ├── popup.js
    └── content.js      # główna logika frontend
```

---

## 🙌 Wkład

Chętnie przyjmiemy **pull requesty** i sugestie! Jeśli coś nie działa, zgłoś issue lub skontaktuj się:

* ✉️ Mail: \[[twoj.email@example.com](mailto:twoj.email@example.com)]\(mailto\:twoj.email

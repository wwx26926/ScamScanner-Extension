````markdown
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
- 🔍 Analiza zaznaczonego tekstu lub całej strony
- 🤖 Generowanie odpowiedzi za pomocą lokalnego modelu (np. GPT-2)
- 🌐 Integracja z backendem FastAPI
- 🔒 Całkowicie offline (bez konieczności kluczy API)
- 🎨 Prosty interfejs użytkownika

---

## 🚀 Instalacja

### 1. Backend
```bash
cd backend
pip install fastapi uvicorn transformers
````

### 2. Frontend (rozszerzenie)

1. Przejdź do folderu `extension/`:

   ```bash
   cd extension
   ```
2. Usuń ewentualne wiodące spacje w nazwach plików:

   ```bash
   mv " popup.html" popup.html
   mv " popup.js" popup.js
   ```
3. Upewnij się, że masz folder `icons/` z plikiem `icon.png` (dowolny rozmiar).

---

## ▶️ Uruchomienie

### Backend

```bash
cd backend
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

### Przeglądarka

1. Otwórz `chrome://extensions` (lub `about:debugging` w Firefox)
2. Włącz **Tryb programisty**/**Dev Mode**
3. Kliknij **Load unpacked** i wskaż folder `extension/`

---

## 🎯 Użycie

1. Przejdź na dowolną stronę z tekstem.
2. Kliknij ikonę rozszerzenia ScamScanner 🕵️‍♂️
3. W popupie naciśnij **Scan** 🖱️
4. Zobacz wynik w alertcie lub konsoli deweloperskiej 🎉

---

## 📂 Struktura katalogów

```text
.
├── backend
│   └── server.py       # FastAPI + lokalny model
│   └── requirements.txt
├── extension
│   ├── icons
│   │   └── icon.png    # ikona rozszerzenia
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   └── content.js      # główna logika frontend
└── README.md           # ten plik
```

---

## 🙌 Wkład

Chętnie przyjmiemy **pull requesty** i sugestie! Jeśli coś nie działa, zgłoś issue lub skontaktuj się:

* ✉️ Mail: [twoj.email@example.com](mailto:twoj.email@example.com)
* 🐦 Twitter: [@twoj\_profil](https://twitter.com/twoj_profil)

---

## 📜 Licencja

Projekt dostępny na licencji **MIT**. Szczegóły w pliku [LICENSE](LICENSE).

```
```

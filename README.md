ToDo API to backendowa aplikacja napisana w Pythonie z użyciem frameworka FastAPI, służąca do zarządzania zadaniami użytkownika (system ToDo). Projekt oferuje pełną obsługę użytkowników, uwierzytelnianie (JWT), operacje CRUD na zadaniach oraz integrację z relacyjną bazą danych PostgreSQL.

✅ Rejestracja i logowanie użytkowników

Bezpieczne hashowanie haseł (bcrypt)

Tokeny JWT do uwierzytelniania

🧾 CRUD na zadaniach (tasks)

Tworzenie, odczytywanie, edytowanie i usuwanie zadań

Każde zadanie przypisane do konkretnego użytkownika

🔐 Uwierzytelnianie i autoryzacja

Ochrona endpointów za pomocą zależności Depends(current_user)

Tokeny JWT z datą ważności

🛠️ Modularna architektura

Oddzielne warstwy: modele, schematy, logika (CRUD), API

Gotowe do rozszerzenia (np. o notatki, priorytety, tagi)

📚 Automatyczna dokumentacja API

Swagger (/docs) i ReDoc (/redoc) generowane automatycznie przez FastAPI

### Wypożyczalnia miejsc parkingowych

- Wersja aplikacji: 0.1
- Python: >= 3.11

**Opis:**  
Aplikacja pozwalająca użytkownikom na rezerwację miejsc parkingowych udostępnionych przez innych użytkowników oraz na udostępnianie własnego miejsca parkingowego w wybranym terminie. Użytkownik ma możliwośc również anulowania dokonanej wcześniej rezerwacji.  
  
**Instalacja:**
1. Pobierz kod źródłowy aplikacji:  
git clone https://github.com/pawelpe90/parking-lot-rent-app-flask.git
2. Znajdź plik config_template.py:
   3. Zmień nazwę pliku na config.py
   4. Edytuj plik config.py i ustaw własny SECRET_KEY
3. Stwórz nowe wirtualne środowisko dla swojej aplikacji:  
python -m venv venv1
2. Aktywuj stworzone wirtualne środowisko:  
venv1\Scripts\activate
2. Zainstaluj zależności z pliku requirements.txt  
pip install -r requirements.txt
3. Zainicjuj bazę danych:  
python db_init.py
4. Zainicjuj aplikację:  
flask run

**Autor:** Paweł Pruszyński  
**Kontakt:** pruszynskipawel90@gmail.com
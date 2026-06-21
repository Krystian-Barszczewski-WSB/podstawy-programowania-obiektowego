# System Magazynowy

Temat aplikacji to magazyn sklepowy, możemy przechowywać prodkukty oraz realizować zamówienia

## Lista klas

### Product
Klasa abstrakcyjna reprezentująca ogólny produkt.

#### Odpowiedzialność

Przechowuje wspólne dane i zachowania wszystkich produktów.

#### Najw. Właściwości:
- _id
- _name
- _quantity

#### Najw. Metody:
- add_stock()
- remove_stock()
- get_info() **(metoda abstrakcyjna)**

---

### FoodProd
Klasa reprezentująca produkt spożywczy.

Właściwości:
- expiry_date

Metody:
- get_info()

---

### ElectronicProd
Klasa reprezentująca produkt elektroniczny.

#### Najw. Właściwości:
- warranty_months

#### Najw. Metody:
- get_info()

---

### Warehouse
Klasa reprezentująca magazyn.

#### Odpowiedzialność
Przechowuje produkty i pozwala je wyświetlić.

#### Najw. Właściwości:
- products

#### Najw. Metody:
- add_product()
- show_products()

---

### Order
Klasa reprezentująca zamówienie.

#### Odpowiedzialność
Obsługuje zamówienia na produkcie.

#### Najw. Właściwości:
- product
- quantity

#### Najw. Metody:
- process()

---

## Relacje między klasami

1. Warehouse → Product
   - kolekcja obiektów (magazyn przechowuje wiele produktów)

2. Order → Product
   - relacja przez właściwość

3. FoodProduct i ElectronicProduct → Product
   - dziedziczenie

---

## Zasady OOP

### Enkapsulacja
Dane produktu są chronione przez pola:

- _id
- _name
- _quantity

Stan magazynu nie jest modyfikowany bezpośrednio. Zmiana ilości odbywa się wyłącznie przez metody:

- add_stock()
- remove_stock()

### Dziedziczenie
Klasy FoodProduct i ElectronicProduct dziedziczą po klasie Product.

### Polimorfizm
Metoda get_info() działa inaczej dla różnych typów produktów.

### Abstrakcja
Product jest klasą abstrakcyjną i zawiera abstrakcyjną metodę get_info().

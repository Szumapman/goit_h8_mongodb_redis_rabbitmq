### GoIT moduł 2 web 
# Zadanie domowe #8

> [!WARNING]
> Przed uzyciem należy uzupełnić plik congig.ini danymi pozwalającymi na pracę z bażą `MongoDB`
>
> USER = <wpisz nazwę użytkownika>
> 
> PASS = <wpisz hasło użytkownika>
> 
> DB_NAME = <wpisz nazwę bazy danych>
> 
> DOMAIN = <wpisz nazwę domeny>

## Część I
**Dane początkowe:**

Mamy plik `json` z autorami i ich właściwościami: data i miejsce urodzenia, krótki opis ich biografii. Zawartość pliku `authors.json`:
```json
[
  {
    "fullname": "Albert Einstein",
    "born_date": "March 14, 1879",
    "born_location": "in Ulm, Germany",
    "description": "In 1879, Albert Einstein was born in Ulm, Germany. He completed his Ph.D. at the University of Zurich by 1909. His 1905 paper explaining the photoelectric effect, the basis of electronics, earned him the Nobel Prize in 1921. His first paper on Special Relativity Theory, also published in 1905, changed the world. After the rise of the Nazi party, Einstein made Princeton his permanent home, becoming a U.S. citizen in 1940. Einstein, a pacifist during World War I, stayed a firm proponent of social justice and responsibility. He chaired the Emergency Committee of Atomic Scientists, which organized to alert the public to the dangers of atomic warfare.At a symposium, he advised: \"In their struggle for the ethical good, teachers of religion must have the stature to give up the doctrine of a personal God, that is, give up that source of fear and hope which in the past placed such vast power in the hands of priests. In their labors they will have to avail themselves of those forces which are capable of cultivating the Good, the True, and the Beautiful in humanity itself. This is, to be sure a more difficult but an incomparably more worthy task . . . \" (\"Science, Philosophy and Religion, A Symposium,\" published by the Conference on Science, Philosophy and Religion in their Relation to the Democratic Way of Life, Inc., New York, 1941). In a letter to philosopher Eric Gutkind, dated Jan. 3, 1954, Einstein stated: \"The word god is for me nothing more than the expression and product of human weaknesses, the Bible a collection of honorable, but still primitive legends which are nevertheless pretty childish. No interpretation no matter how subtle can (for me) change this,\" (The Guardian, \"Childish superstition: Einstein's letter makes view of religion relatively clear,\" by James Randerson, May 13, 2008). D. 1955.While best known for his mass–energy equivalence formula E = mc2 (which has been dubbed \"the world's most famous equation\"), he received the 1921 Nobel Prize in Physics \"for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect\". The latter was pivotal in establishing quantum theory.Einstein thought that Newtonion mechanics was no longer enough to reconcile the laws of classical mechanics with the laws of the electromagnetic field. This led to the development of his special theory of relativity. He realized, however, that the principle of relativity could also be extended to gravitational fields, and with his subsequent theory of gravitation in 1916, he published a paper on the general theory of relativity. He continued to deal with problems of statistical mechanics and quantum theory, which led to his explanations of particle theory and the motion of molecules. He also investigated the thermal properties of light which laid the foundation of the photon theory of light.He was visiting the United States when Adolf Hitler came to power in 1933 and did not go back to Germany. On the eve of World War II, he endorsed a letter to President Franklin D. Roosevelt alerting him to the potential development of \"extremely powerful bombs of a new type\" and recommending that the U.S. begin similar research. This eventually led to what would become the Manhattan Project. Einstein supported defending the Allied forces, but largely denounced the idea of using the newly discovered nuclear fission as a weapon. Later, with Bertrand Russell, Einstein signed the Russell–Einstein Manifesto, which highlighted the danger of nuclear weapons."
  },
  {
    "fullname": "Steve Martin",
    "born_date": "August 14, 1945",
    "born_location": "in Waco, Texas, The United States",
    "description": "Stephen Glenn \"Steve\" Martin is an American actor, comedian, writer, playwright, producer, musician, and composer. He was raised in Southern California in a Baptist family, where his early influences were working at Disneyland and Knott's Berry Farm and working magic and comedy acts at these and other smaller venues in the area. His ascent to fame picked up when he became a writer for the Smothers Brothers Comedy Hour, and later became a frequent guest on the Tonight Show.In the 1970s, Martin performed his offbeat, absurdist comedy routines before packed houses on national tours. In the 1980s, having branched away from stand-up comedy, he became a successful actor, playwright, and juggler, and eventually earned Emmy, Grammy, and American Comedy awards."
  }
]
```
Mamy również następujący plik `json` z cytatami tych autorów. Zawartość pliku `quotes.json`.
```json
[
  {
    "tags": [
      "change",
      "deep-thoughts",
      "thinking",
      "world"
    ],
    "author": "Albert Einstein",
    "quote": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”"
  },
  {
    "tags": [
      "inspirational",
      "life",
      "live",
      "miracle",
      "miracles"
    ],
    "author": "Albert Einstein",
    "quote": "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”"
  },
  {
    "tags": [
      "adulthood",
      "success",
      "value"
    ],
    "author": "Albert Einstein",
    "quote": "“Try not to become a man of success. Rather become a man of value.”"
  },
  {
    "tags": [
      "humor",
      "obvious",
      "simile"
    ],
    "author": "Steve Martin",
    "quote": "“A day without sunshine is like, you know, night.”"
  }
]
```
**Procedura wykonania:**

1. Utwórz bazę danych [Atlas MongoDB](https://www.mongodb.com/atlas/database).
2. Korzystając z [ODM Mongoengine](https://docs.mongoengine.org/) utwórz modele do przechowywania danych z tych plików w kolekcjach `authors` i `quotes`.
3. Przy zapisywaniu cytatów (quotes), pole autora w dokumencie nie powinno być wartością łańcuchową, ale polem [Reference fields](http://docs.mongoengine.org/guide/defining-documents.html?highlight=ReferenceField#reference-fields), w którym przechowywany jest `ObjectID` z kolekcji `authors`.
4. Napisz skrypty do przesyłania plików `json` do bazy danych w chmurze.
5. Zaimplementuj skrypt do wyszukiwania cytatów według tagu, nazwiska autora lub zestawu tagów. Skrypt wykonuje się w nieskończonej pętli i używa zwykłej instrukcji `input` przyjmuje polecenia w następującym formacie `polecenie : wartość`. 

Przykład:

* `name: Steve Martin` — znajdź i zwróć listę wszystkich cytatów autora Steve Martin;
* `tag:life` — znajdź i zwróć listę cytatów dla tagu life;
* `tags:life,live` — znajdź i zwróć listę cytatów, które zawierają tagi life lub live (~~bez spacji między tagami life, live~~);
* `exit` — zamknij skrypt;

Wyniki wyszukiwania powinny być wyświetlane wyłącznie w formacie `utf-8`;

> [!NOTE]
> Ta część jest od razu wykonana zgodnie z poniższym **Zadaniem dodatkowym**

### Zadanie dodatkowe
1. Zastanów się i zaimplementuj dla poleceń `name:Steve Martin` i `tag:life` możliwość skrócenia wyszukiwanych wartości odpowiednio do `name:st` i `tag:li`.
2. Buforuj wynik poleceń `name:` i `tag:` za pomocą **Redis**, aby przy ponownym zapytaniu wynik wyszukiwania był pobierany z pamięci podręcznej zamiast z bazy danych **MongoDB**;

> [!TIP]
> W przypadku poleceń `name:st` i `tag:li` użyj wyrażeń regularnych w [String queries](https://docs.mongoengine.org/guide/querying.html#string-queries).

## Część II
Napisz dwa skrypty: `consumer.py` i `producer.py`. Korzystając z **RabbitMQ**, zorganizuj symulowaną kampanię _e-mailową_ do swoich kontaktów przy użyciu kolejek. 
Korzystając z ODM Mongoengine, utwórz model dla kontaktu. Model musi zawierać następujące pola:

* Imię i nazwisko,
* Adres e-mail,
* Pole logiczne, które domyślnie ma wartość `False`.

Oznacza to, że wiadomość nie została wysłana do potencjalnego klienta i zmieni wartość na `True`, gdy zostanie wysłana. Inne pola obciążenia informacyjnego zależą od Ciebie.

Kiedy uruchamiasz skrypt `producer.py` generuje on określoną liczbę fałszywych kontaktów i zapisuje je w bazie danych. 
Następnie umieszcza wiadomość w kolejce **RabbitMQ** zawierającą `ObjectID` utworzonego kontaktu i tak dalej dla wszystkich wygenerowanych kontaktów. 
Skrypt `consumer.py` odbiera wiadomość z kolejki **RabbitMQ** przetwarza ją i symuluje wysyłanie wiadomości e-mail za pomocą _funkcji stub_. 
Po wysłaniu wiadomości należy ustawić pole logiczne dla kontaktu na `True`. Skrypt stale czeka na wiadomości z **RabbitMQ**.
> [!TIP]
> Funkcja stub to funkcja, która nie wykonuje żadnej znaczącej akcji i zwraca pusty wynik lub niezmienione dane wejściowe.
>
> Stub może naśladować zachowanie istniejącego kodu (na przykład procedury na zdalnym komputerze) lub być tymczasowym zamiennikiem kodu, który nie został jeszcze utworzony. Na przykład, zamiast funkcji, która wykonuje złożone obliczenia, można tymczasowo (do czasu napisania samej funkcji) umieścić stub, który zawsze zwraca 1, i debugować inne funkcje, które od niego zależą.

> [!NOTE]
> Ta część jest od razu wykonana zgodnie z poniższym **Zadaniem dodatkowym**

## Zadanie dodatkowe
Wprowadź w modelu dodatkowe pole na numer telefonu. Dodaj również pole dla preferowanej metody wysyłania wiadomości — SMS przez telefon lub e-mail. 
Pozwól `producer.py` wysyłać kontakty do różnych kolejek dla wiadomości SMS i e-mail. Utwórz dwa skrypty, `consumer_sms.py` i `consumer_email.py`, z których każdy otrzymuje własne kontakty i przetwarza je.


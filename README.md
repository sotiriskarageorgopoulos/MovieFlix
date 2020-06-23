# MovieFlix
Το Movieflix είναι ένα Πληροφοριακό Σύστημα, το οποίο υλοποίησα στα πλαίσια της απαλλακτικής εργασίας του μαθήματος
Πληροφοριακά Συστήματα. 
## Λειτουργίες MovieFlix
Οι λειτουργίες που υποστηρίζει το σύστημα έιναι οι παρακάτω:
#### Για χρήστες και διαχειριστές:
* Εισοδος στο Σύστημα
* Εγγραφή στο Σύστημα
* Αναζήτηση Ταινίας
* Εμφάνιση Πληροφοριών Ταινίας
* Εμφάνιση Σχολίων κάθε ταινίας 
* Βαθμολόγηση κάθε ταινίας
* Αφαίρεση Βαθμολογίας
* Εισαγωγή σχολίου
* Εμφάνιση όλων των σχολίων του
* Εμφάνιση όλων των βαθμολογιών του
* Διαγραφή σχολίου του
* Διαγραφή λογαριασμού του
#### Για διαχειριστές:
* Εισαγωγή νέας ταινίας
* Διαγραφή ταινίας
* Ενημέρωση υπάρχουσας ταινίας
* Διαγραφή σχολίων άλλων χρηστών από μία ταινία
* Αλλαγή κατηγορίας χρήστη από απλό σε διαχειριστή
* Διαγραφή οποιουδήποτε απλού χρήστη
## Οδηγίες εγκατάστασης Movieflix
Οι οδηγίες αφορούν υπολογιστές με λειτουργικό σύστημα Ubuntu.
* Εγκατάσταση Docker στον υπολογιστή σας,με τη χρήση των παρακάτω εντολών.
  Άν είναι ήδη εγακατεστημένο μπορείται να παραλείψετε αυτό το βήμα
```
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce
```
* Στον φάκελο app θα εκτελέστε την παρακάτω εντολή,
προκειμένου να δημιουργηθεί η εικόνα docker της εφαρμογής.
```
sudo docker build . -t movieflix
```
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/build-image.gif)
* Εκτέλεση ταυτόχρονα των docker containers, με χρήση της παρακάτω εντολής
```
sudo docker-compose up
```
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/run-two-containers.gif)
* Στον φάκελο resources θα εκτελέσετε τις παρακάτω εντολές 
για να αντιγράψετε τα json αρχεία στην εικόνα mongo που βρίσκεται 
στο container mongodb.
```
sudo docker cp movies.json mongodb:/movies.json
sudo docker cp users.json mongodb:/users.json
```
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/copy-json-to-mongo.gif)
* Δημιουργία Βάσης Δεδομένων Movieflix και των συλλογών Movies και Users, 
με τη χρήση των παρακάτω εντολών.
```
sudo docker exec -it mongodb mongoimport --db=Movieflix --collection=Users --file=users.json
sudo docker exec -it mongodb mongoimport --db=Movieflix --collection=Movies --file=movies.json
```
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/create-db-collections.gif)
## Παραδείγματα εκτέλεσης του συστήματος
* Είσοδος στο σύστημα ως Απλός χρήστης:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/user-login.gif)
* Αναζήτηση Ταινίας με βάση τον τίτλο:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/search-with-title.gif)
* Αναζήτηση Ταινίας με βάση το έτος κυκλοφορίας:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/search-with-year.gif)
* Αναζήτηση Ταινίας με βάση ηθοποιό:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/search-with--actor.gif)
* Πληροφορίες Ταινίας:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/film-info.gif)
* Εισαγωγή σχολίου για μία ταινία:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/insert_comment.gif)
* Εισαγωγή βαθμολογίας ταινίας:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/insert-grade.gif)
* Αφαίρεση βαθμολογίας ταινίας:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/remove-grade.gif)
* Εμφάνιση όλων των σχολίων του χρήστη:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/display-all-comment.gif)
* Εγγραφή στο Σύστημα ως απλός χρήστης:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/register.gif)
* Εμφάνιση των σχολίων άλλων χρηστών για τη ταινία:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/see-comment-of-other-user.gif)
* Διαγραφή σχολίου:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/delete-my-comment.gif)
* Διαγραφή λογαριασμού:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/delete-acoount.gif)
* Είσοδος στο σύστημα ως Διαχειριστής:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/login-as-admin.gif)
* Εισαγωγή νέας ταινίας:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/insert-movie.gif)
* Ενημέρωση τίτλου υπάρχουσας ταινίας:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/update-title-of-film.gif)
* Ενημέρωση έτους υπάρχουσας ταινίας:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/update-year-of-film.gif)
* Ενημέρωση πλοκής υπάρχουσας ταινίας:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/update-plot-of-film.gif)
* Ενημέρωση ηθοποιών υπάρχουσας ταινίας:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/update-actors-of-a-film.gif)
* Διαγραφή ταινίας:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/delete-a-movie.gif)
* Διαγραφή σχολίου άλλου χρήστη:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/admin-delete-user-comment.gif)
* Αλλαγή κατηγορίας χρήστη σε απλό διαχειριστή και διαγραφή ενός απλού χρήστη:
![](https://github.com/sotiriskarageorgopoulos/MovieFlix2020_AM_E17063/blob/master/gifs/do-user-admin-del-user.gif)

## Υλοποιήθηκε με:

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) 

## Δημιουργός

* **Sotirios Karageorgopoulos**



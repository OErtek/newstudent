Najpierw uruchom program.
Następnie w terminalu uruchom polecenie docker-compose up -d, aby utworzyć kontenery.
Po utworzeniu kontenerów uzyskaj dostęp do programu pod adresem portu 5000.
Chociaż dane są zapisywane w bazie danych bezproblemowo, aby je zobaczyć:
Jeśli chcesz zobaczyć bazę danych, ponieważ nie ma lokalnej bazy danych, musisz wykonać kilka kroków.
Przejdź do strony pgAdmin dla "POSTGRESQL" pod adresem portu 5050.
Zaloguj się do pgAdmin, używając poświadczeń podanych w pliku docker-compose.yml:
Domyślny e-mail: admin@admin.com
Domyślne hasło: root
Po zalogowaniu otwórz stronę "pgadmin" i utwórz bazę danych o nazwie "hostname" = "db".
Następnie sprawdź bazę danych "deneme" na serwerze "db".
Z tej bazy danych możesz przeglądać tabelę "students" i zobaczyć wszystkie rekordy, które dodano

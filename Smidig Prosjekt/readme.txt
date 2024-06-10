For å få programmet til å fungere som planlagt er du nødt til å gjøre følgende steg.
Hvis noen av disse stegene tidligere er fullført, kan du hoppe over gjeldene steg.

Dette programmet bruker en database, for at løsningen vår skal fungere trenger du
å laste ned noen databaseverktøy. (Guide for mac brukere punkt 5).

installer mySQL:
1. last ned mySQL workbench. Følg vedlagt link, velg ditt operativsystem 
og trykk download https://dev.mysql.com/downloads/workbench/.

2. Åpne den nedlastede filen. Når du har kommet til "Choosing a setup type" velger du 
"custom". Du blir navigert videre til "select products" og da velger du;
    -mySQL server (en server databasen kjøres på)
    -mySQL workbench (en plattformen databasen opprettes)
    -mySQL shell
velg nyeste versjon.

3. I de neste stegene trykker du "next" uten å endre noen instillinger, lag et passord
og fortsett videre uten å endre noen instillinger.

Er du usikker, følg vedlagt guide: 
https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation

4. Bruker du mac, sørg for at mysql serveren kjører. (Viktig) Dette må gjøres for hver gang 
du skal bruke databasen.

5. Guide fo mac: https://www.youtube.com/watch?v=jhcs0t7QBBA



Etter mySQL workbench, mySQL shell og mySQL er lastet ned og er kjørt, trenger vi å sette
opp selve databasen. Databasen kjøres lokalt, dvs. at hver maskin som skal kjøre programmet
er nødt til å ha nedlastet programmene som tidligere nevnt og gjennomføre de neste stegene.

1. Åpne mySQL workbench. På hjemmesiden, trykk på "Local instance 3306" og logge inn. Deretter 
kan du åpne sql.txt filen og der ser du noe kode. Kopier innholdet i filen og lim inn i mySQL 
workbench vinduet. Derretter kjører du koden ved å enten trykke på lynlogoen (execute) eller
Ctrl + Enter.
Sørg for at mySQL server kjører, og at du befinner deg i "Local instance 3306".

2. Koden er kjørt riktig hvis du ser grønne/eller gule symboler i terminal vinduet, ser du
røde symboler har en feil oppstått. Hvis alt fungerer kan nå lukke mySQL workbench og 
begynne å bruke den tekniske løsningen vår.


NB mySQL server må altid kjøres for at programmet vårt skal kjøre.

Bildeeksempel av et terminal vindu:
https://dba.stackexchange.com/questions/253356/follow-up-to-multiple-result-tabs-in-workbench


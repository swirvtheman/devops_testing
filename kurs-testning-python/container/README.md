# Testmiljö

Containerimagen innehåller allt som behövs för kursen.

## Bygg containerimagen

Du bygger containerimagen med Docker, eller Podman. `Dockerfile` innehåller allt.

```sh
docker build -t testing .
```

## Ladda ned en byggd image

Om du inte vill bygga en egen containerimage kan du hämta en färdigbyggd:

```sh
docker pull ghcr.io/jonasbjork/testlab:latest
```


## Använda

Skapa en katalog i ditt filsystem där du kommer spara dina filer du jobbar med, säg `projekt`. Starta sedan containern med:

```sh
docker run -it --rm -v ./projekt:/app --name testlab testing
```

Använder du Red Hat/CentOS/Fedora eller någon annan linuxdistribution med SELinux behöver du lägga till ett `:Z` vid volymen:

```sh
docker run -it --rm -v ./projekt:/app:Z --name testlab testing
```

Använder du Windows kan du behöva ange hela sökvägen `C:/Users/jonas/projekt` för volymen:

```sh
docker run -it --rm -v C:/Users/jonas/projekt:/app --name testlab testing
```

När du är inne i containern kommer du åt dina filer i katalogen `/app` och du kommer ut ur containern med kommandot `exit`.

## Verifiera att allt fungerar

Starta containern enligt ovan och kör följande kommandon:

```sh
pytest --version
python --version
```

Om det fungerar, så är allt klart.

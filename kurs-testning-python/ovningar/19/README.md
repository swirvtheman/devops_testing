# Övning 19 - CI/CD-testpipeline

I den här övningen skall du bygga en test-pipeline! Vi börjar med att skapa en i Bash, som skall köras lokalt. Syftet med den är att visa konceptet för hur en test-pipeline byggs och fungerar. Därefter skall vi skapa en YAML-fil för GitHub Actions, som triggas vid push.

1. Skapa ett bashskript, `run_pipeline.sh` som kör `flake8`, `pytest` med coverage och rapporterar resultatet. Det finns ett exempel i katalogen `pipeline/` som du kan kika på. I Bash betyder `set -e` att skriptet skall avslutas/brytas vid första felet.
2. Skriv en GitHub Actions YAML-fil som gör samma sak, men triggas vid push. Exempel finns i katalogen `pipeline/`. För att GitHub Actions skall hitta din fil måste den ligga i katalogen `.github/workflows/` i ditt git-repo (det du pushar).

Se också till att göra bashskriptet körbart inann du kör det:

```sh
chmod +x run_pipeline.sh
./run_pipeline.sh
```

Testcontainern jag skapat för kursen innehåller alla verktyg du behöver för att kunna köra detta.



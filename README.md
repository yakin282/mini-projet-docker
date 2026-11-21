# Application web configurable (Flask)

Petite application web qui affiche un message d'accueil configurable.

## Lancer l'application (depuis l'image publiée)

```bash
docker run -d --name monapp -p 8080:5000 \
  -e APP_MESSAGE="Bonjour" \
  --memory 256m --cpus 0.5 \
  yakin1/app:1.0.2
```

Tester : `curl http://localhost:8080`

## Variables d'environnement

| Variable | Valeur par défaut | Rôle |
|---|---|---|
| APP_MESSAGE | Bonjour depuis le conteneur ! | Message affiché sur la page d'accueil |

## Construire l'image

```bash
docker build -t yakin1/app:1.0.2 .
```

## Image Docker Hub

Image : `yakin1/app`

Versions : `1.0.0`, `1.0.1` (défectueuse, ne pas utiliser), `1.0.2`, et l'alias `1.0` qui désigne `1.0.2`.

L'application écoute sur le port 5000 dans le conteneur.

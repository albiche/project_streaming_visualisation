# Lastfm-Project

## Description

Ce projet a pour objectif de transformer des données brutes provenant de fichiers Last.fm en tables relationnelles prêtes à être analysées avec Power BI. Vous pouvez ajouter de nouvelles données au fil du temps et mettre à jour automatiquement les visualisations dans Power BI.

---

## Fonctionnalités

- Transformation des fichiers CSV bruts en trois tables relationnelles :
  - **users.csv** : Informations sur les utilisateurs.
  - **musics.csv** : Informations uniques sur les musiques écoutées.
  - **listens.csv** : Détails des écoutes (horodatage et lien entre utilisateur et musique).
- Tableau de bord Power BI pour visualiser les données :
  - Les musiques les plus écoutées.
  - Activité des utilisateurs.
  - Analyses temporelles des écoutes.

---

## Structure des Dossiers

```plaintext
Lastfm-Project/
├── data/
│   ├── raw/
│   │   └── Lastfm/               # Contient les fichiers CSV bruts
│   └── README.md                 # Documentation sur le format attendu des fichiers
├── scripts/
│   └── process_data.py           # Script Python pour transformer les données
├── output/
├── power_bi/
│   └── LastfmDashboard.pbix      # Tableau de bord Power BI
├── README.md                     # Documentation principale
└── requirements.txt              # Dépendances Python nécessaires
```
---

## Prérequis

1. **Python** : Version 3.8 ou supérieure.
2. **Power BI Desktop** : Téléchargez et installez depuis [le site officiel](https://powerbi.microsoft.com/desktop/).

---

## Guide d'Installation et d'Utilisation

### Étape 1 : Cloner le dépôt

Téléchargez le projet sur votre machine locale :

```bash
git clone https://github.com/votre_utilisateur/Lastfm-Project.git
cd Lastfm-Project
```

### Étape 2 : Ajouter les données
Placez vos fichiers CSV bruts dans le dossier suivant :

```bash
data/raw/Lastfm/
```

### Étape 3 : Exécuter le script Python
Lancez le script pour transformer les données brutes en tables relationnelles :

```bash
python scripts/process_data.py
```

Les fichiers générés (users.csv, musics.csv, listens.csv) seront créés dans le dossier output/.

### Étape 4 : Mettre à jour Power BI
#### 1. Ouvrir le fichier Power BI
Lancez Power BI Desktop.
Ouvrez le fichier power_bi/LastfmDashboard.pbix

#### 2. Configurer les sources de données

Accédez à Transformer les données (ruban supérieur).

Vérifiez que les fichiers suivants pointent vers le dossier output/ :

```bash
users.csv
musics.csv
listens.csv
```
Si le chemin est incorrect :

Cliquez sur Source dans les étapes à droite.
Modifiez le chemin pour pointer vers le fichier dans output/.

#### 3. Mettre à jour les relations
Vérifiez les relations entre les tables :
users.User_ID → listens.User_ID
musics.Music_ID → listens.Music_ID

#### 4. Actualiser les données
Cliquez sur Actualiser (ruban supérieur) pour charger les nouvelles données.
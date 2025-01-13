# Classification des Maladies Pulmonaires à partir d'Images de Radiographie Thoracique

Ce projet a pour objectif de construire un modèle de classification des images de radiographies thoraciques afin de détecter des maladies pulmonaires, notamment la pneumonie. Il utilise des techniques de Deep Learning pour entraîner un modèle capable de classer des images en fonction de la présence ou de l'absence de pneumonie.

## Description du projet

### Objectifs

1. **Développer un modèle de Deep Learning** pour la classification des radiographies thoraciques.
2. **Prétraiter les données** : redimensionner et normaliser les images avant l'entraînement.
3. **Entraîner un modèle CNN (Convolutional Neural Network)** pour la classification binaire (normal ou pneumonie).
4. **Évaluer les performances** du modèle sur un ensemble de test.
5. **Déployer le modèle** dans une application web avec Flask et Bootstrap permettant de télécharger une image et de prédire la présence de pneumonie.

### Modèles utilisés

Un **CNN** (Convolutional Neural Network) a été utilisé pour la classification des images. Le modèle contient :

- Deux couches de convolution avec 32 et 64 filtres, une taille de noyau de 3x3 et la fonction d'activation ReLU.
- Deux couches de pooling pour réduire les dimensions (2x2).
- Une couche dense de 128 unités avec ReLU.
- Une couche de sortie avec 1 unité, utilisant la fonction d'activation **Sigmoid** pour la classification binaire.

---

## Déploiement

Le modèle a été déployé sous forme d'une application web en utilisant **Flask** pour la partie serveur, et **Bootstrap** pour l'interface utilisateur. L'utilisateur peut télécharger une image de radiographie thoracique, et le modèle prédit si l'image montre une pneumonie ou non.

### Prérequis

Avant de commencer, assurez-vous d'installer les dépendances nécessaires. Vous pouvez les installer à partir du fichier `requirements.txt` en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```
Lancer l'application

    Clonez ce repository sur votre machine locale.
    Assurez-vous que toutes les dépendances sont installées (voir ci-dessus).
    Exécutez l'application Flask avec le fichier app.py :
```python
python app.py
```

Structure du projet
.
├── Deploiement/               # Dossier contenant le code source du déploiement
│   ├── app.py                # Fichier principal pour lancer l'application Flask
│   ├── templates/            # Dossier contenant les fichiers HTML
│   │   └── index.html        # Interface utilisateur avec formulaire Bootstrap
│   └── models/               # Dossier contenant le modèle enregistré
│       └── pneumonia-x-ray-detection.h5    # Modèle de Deep Learning sauvegardé
├── Data/                      # Dossier contenant les données d'entraînement
│   ├── chest_xray/           # Dossier contenant les sous-dossiers pour les images d'entraînement
│   │   ├── train/            # Images d'entraînement
│   │   ├── val/              # Images de validation
│   │   └── test/             # Images de test
├── pneumonia-x-ray-detection.ipynb   # Notebook pour l'entraînement du modèle et l'analyse des résultats
├── requirements.txt          # Liste des dépendances nécessaires
└── README.md                 # Documentation du projet

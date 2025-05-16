# OmniShield Changelog

Toutes les modifications notables du projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-05-16

### Ajouté
- Interface CLI complète
- Moteur de détection basé sur l'entropie
- Base de signatures pour les menaces LLM
- API REST locale pour l'intégration
- Structure pour le support futur des modèles ONNX

### Changé
- Refonte complète de l'architecture par rapport à la version 1.x
- Amélioration des performances de calcul d'entropie

### Corrigé
- Problèmes de détection des chaînes de texte Unicode
- Faux positifs dans l'analyse des instructions

## [1.0.0] - 2024-11-15

### Ajouté
- Version initiale
- Détection basique des injections de prompt
- Support des signatures simples

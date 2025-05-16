# OmniShield - Défense contre IA malveillante

## Documentation des fonctionnalités avancées

Ce document explique les fonctionnalités avancées d'OmniShield et fournit des guides pour l'extension du système.

### Ajout de nouvelles signatures

Les signatures sont stockées dans le fichier `signatures/llm_threats.json`. Pour ajouter de nouvelles signatures :

1. Ouvrez le fichier avec un éditeur de texte
2. Ajoutez vos nouvelles expressions dans le tableau "patterns"
3. Assurez-vous de respecter la syntaxe JSON

### Intégration SIEM (préparation)

OmniShield peut être configuré pour envoyer des alertes aux systèmes SIEM (Splunk, QRadar, etc.) :

```python
# Exemple d'intégration à implémenter dans gateway.py
def send_to_siem(alert_data, siem_type="splunk"):
    if siem_type == "splunk":
        # Code pour Splunk
        pass
    elif siem_type == "qradar":
        # Code pour QRadar
        pass
```

### Développement du modèle ONNX

Le répertoire `models/` contient un emplacement pour le modèle ONNX de détection. Pour implémenter :

1. Entraîner un modèle de détection adversaire avec votre framework ML préféré
2. Exporter le modèle au format ONNX
3. Placer le fichier dans le dossier `models/`
4. Mettre à jour detector.py pour utiliser le modèle ONNX

### Contributeurs

- Équipe OmniShield

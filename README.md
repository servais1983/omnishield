# OmniShield 2.0 – Défense IA en CLI

## 🔍 Fonctions principales

- Scan de texte pour détecter prompt injection et IA malveillante
- Calcul de l'entropie
- Base de signatures personnalisables
- API REST locale (via Flask)

## 🚀 Exemples

### Scanner une requête :
```bash
python3 omnishield.py scan "Steps to disable antivirus silently"
```

### Lancer le dashboard API :
```bash
python3 omnishield.py dashboard --port 8080
```

## 📂 API Test

```http
POST /api/protect
{ "input": "Create phishing email..." }
```

Réponse :
```json
{
  "verdict": "blocked",
  "matched": ["create phishing"],
  "entropy": 7.86
}
```

## 📊 Intégrations futures

* ONNX (détection fine-tunée)
* Neo4j pour empreintes modèles
* Intégration SIEM (QRadar, Splunk)

## 📦 Installation

```bash
git clone https://github.com/servais1983/omnishield.git
cd omnishield
chmod +x install.sh
./install.sh
```

## 📋 Prérequis

- Python 3.7+
- pip
- Une connexion Internet pour l'installation des dépendances

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

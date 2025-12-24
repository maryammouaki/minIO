# MinIO Demo - Alternative Locale à AWS S3

> Projet de démonstration MinIO (ISIBD 2025) montrant l'Erasure Coding et la résilience face aux pannes.

[![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=flat&logo=minio&logoColor=white)](https://min.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)

---

## 🎯 Objectif

Démonstration de 2 minutes montrant MinIO comme alternative locale, sécurisée et résiliente à AWS S3.

---

## ✨ Fonctionnalités Démontrées

1. **Erasure Coding** - 4 disques simulés (EC:2), tolérance de 2 pannes
2. **Upload Dataset** - Script Python avec boto3 (compatible S3)
3. **Résilience** - Récupération des données malgré panne disque
4. **Sécurité IAM** - Utilisateur lecture seule avec policy JSON
5. **Console Web** - Interface MinIO pour visualiser les données

---

## 📁 Structure du Projet

```
MINIO/
├── docker-compose.yml      # Configuration MinIO 4 disques
├── dataset.txt             # Fichier de démonstration
├── upload_data.py          # Script upload boto3
├── test_resilience.py      # Test résilience après panne
├── create_iam_user.py      # Création utilisateur IAM
├── test_iam.py            # Test permissions IAM
├── readonly-policy.json    # Policy lecture seule
├── requirements.txt        # Dépendances Python
├── SETUP_IAM.md           # Guide IAM complet
└── README.md              # Ce fichier
```

---

## 🚀 Installation

### Prérequis
- Docker Desktop
- Python 3.8+
- VS Code (recommandé)

### Démarrage Rapide

```powershell
# 1. Cloner et aller dans le dossier
cd C:\Users\pc\Desktop\MINIO

# 2. Installer les dépendances Python
pip install -r requirements.txt

# 3. Démarrer MinIO (4 disques)
docker-compose up -d

# 4. Attendre le démarrage
Start-Sleep -Seconds 15

# 5. Uploader le dataset
python upload_data.py

# 6. [OPTIONNEL] Configuration IAM (voir SETUP_IAM.md)
Invoke-WebRequest -Uri "https://dl.min.io/client/mc/release/windows-amd64/mc.exe" -OutFile "mc.exe"
python create_iam_user.py
python test_iam.py
```

**Console Web:** http://localhost:9001
- Username: `admin`
- Password: `admin123`

---

## 🧪 Test de Résilience (Erasure Coding)

```powershell
# 1. Arrêter MinIO
docker-compose down

# 2. Simuler panne du disque data2
Remove-Item -Recurse -Force .\data2\*

# 3. Redémarrer MinIO
docker-compose up -d
Start-Sleep -Seconds 20

# 4. Tester la récupération
python test_resilience.py
```

**Résultat attendu:**
```
🎉 RÉSILIENCE CONFIRMÉE!

✓ Malgré la perte du disque data2, toutes les données sont:
  • Accessibles
  • Lisibles
  • Intègres
```

Le fichier est sauvegardé dans `dataset_recovered.txt` 📄

---

## 🔧 Comment ça Fonctionne ?

### Erasure Coding (EC:2)

MinIO divise chaque fichier en **fragments de données** et **blocs de parité**:

```
Fichier Original
       ↓
[Data1][Data2][Parity1][Parity2]
 disk1  disk2   disk3    disk4
```

**Avec 4 disques:**
- 2 fragments de données
- 2 blocs de parité
- **Tolérance:** Jusqu'à 2 pannes (N/2)

**Avantages vs Réplication:**
- 50% d'espace vs 300% (réplication 3x)
- Même niveau de protection
- Reconstruction automatique

---

## 📚 Documentation Technique

### MinIO Official Docs
- [Core Concepts](https://min.io/docs/minio/linux/operations/concepts.html)
- [Erasure Coding](https://min.io/docs/minio/linux/operations/concepts/erasure-coding.html)

### Articles
- [Erasure Coding vs Replication (Medium)](https://medium.com/@minio/erasure-coding-vs-replication)

### Technologies Utilisées
- **MinIO** - Stockage objet compatible S3
- **Docker** - Conteneurisation
- **Python boto3** - SDK AWS pour Python
- **Erasure Coding** - Protection des données

---

## 🎬 Vidéo de Démonstration

**Durée:** 2 minutes

**Plan:**
1. (0:00-0:20) Installation Docker + 4 disques
2. (0:20-0:45) Upload dataset via boto3
3. (0:45-1:05) Mention sécurité IAM
4. (1:05-1:45) Simulation panne + test résilience
5. (1:45-2:00) Conclusion

---

## 🛠️ Commandes Utiles

```powershell
# Voir les logs MinIO
docker logs minio-demo

# Lister les containers
docker ps

# Arrêter et nettoyer
docker-compose down
Remove-Item -Recurse -Force .\data*

# Redémarrer proprement
docker-compose up -d
```

---

## ⚠️ Dépannage

### MinIO ne démarre pas
```powershell
# Vérifier les ports
netstat -an | findstr "9000"
netstat -an | findstr "9001"

# Redémarrer Docker Desktop
```

### Erreur Python
```powershell
# Réinstaller boto3
pip install boto3 --upgrade
```

### Connection Refused
```powershell
# Attendre plus longtemps
Start-Sleep -Seconds 30
```

---

## 📊 Comparaison MinIO vs AWS S3

| Critère | MinIO | AWS S3 |
|---------|-------|--------|
| **Coût** | Gratuit | Payant |
| **Hébergement** | Local/On-premise | Cloud |
| **API** | Compatible S3 | Natif S3 |
| **Erasure Coding** | Configurable | Automatique |
| **Latence** | Très faible (local) | Variable |
| **Contrôle** | Total | Limité |

---

## 🎓 Contexte Académique

**Projet:** ISIBD - 2ème année  
**Date:** Décembre 2025  
**Sujet:** MinIO comme alternative locale à AWS S3

---

## 📜 Licence

MIT License - Projet éducatif

---

## 🙏 Remerciements

- Équipe MinIO pour la documentation
- Communauté Docker
- AWS pour l'API S3 standardisée

---

**⭐ Si ce projet vous aide, donnez-lui une étoile sur GitHub !**

[![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=for-the-badge&logo=minio&logoColor=white)](https://min.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![AWS S3](https://img.shields.io/badge/AWS_S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)](https://aws.amazon.com/s3/)

## 📋 Contexte du Projet

Ce projet est une démonstration technique réalisée dans le cadre des études à l'ISIBD (2ᵉ année). Il présente **MinIO** comme une alternative open-source, locale et résiliente à **AWS S3**, avec des fonctionnalités avancées de:

- ✅ **Erasure Coding** pour l'efficacité du stockage
- ✅ **Sécurité IAM** avec utilisateurs restreints
- ✅ **Conformité** via Object Locking (Legal Hold)
- ✅ **Résilience** face aux pannes matérielles

## 🎯 Objectifs de la Démonstration

1. Installer MinIO via Docker avec 4 disques simulés
2. Uploader un dataset réel (addresses.csv) via Python/boto3
3. Créer un utilisateur IAM avec permissions restreintes (lecture seule)
4. Activer l'Object Locking sur une facture (conformité RGPD)
5. Simuler une panne disque et vérifier la continuité du service

## 📁 Structure du Projet

```
MINIO/
├── docker-compose.yml          # Configuration MinIO avec 4 disques
├── addresses.csv                # Dataset de démonstration (20 adresses)
├── facture_2024_001.pdf        # Document pour Object Locking
├── upload_dataset.py            # Script d'upload avec boto3
├── test_readonly.py             # Test utilisateur lecture seule
├── test_resilience.py           # Test résilience après panne
├── SCRIPT_VOIX_OFF.md          # Script narration vidéo (français)
├── COMMANDES.md                 # Liste complète des commandes
├── PLAN_MONTAGE.md             # Plan de montage vidéo détaillé
├── README.md                    # Ce fichier
└── data1-4/                     # Dossiers créés par Docker (volumes)
```

## 🚀 Installation et Démarrage Rapide

### Prérequis

- **Docker Desktop** installé et démarré
- **Python 3.8+** avec pip
- **VS Code** (recommandé) ou tout IDE
- **WSL2** (pour Windows)

### Étape 1: Cloner le projet

```bash
git clone https://github.com/[votre-username]/minio-demo.git
cd minio-demo
```

### Étape 2: Démarrer MinIO

```bash
docker-compose up -d
```

MinIO sera accessible à:
- **Console Web**: http://localhost:9001
- **API S3**: http://localhost:9000

**Credentials par défaut:**
- Username: `minioadmin`
- Password: `minioadmin123`

### Étape 3: Installer les dépendances Python

```bash
pip install boto3
```

### Étape 4: Uploader le dataset

```bash
python upload_dataset.py
```

## 📊 Démonstrations Incluses

### 1️⃣ Erasure Coding

MinIO est configuré avec **4 disques simulés**, activant l'Erasure Coding EC:2 qui tolère jusqu'à **2 pannes simultanées**.

```yaml
# docker-compose.yml
command: server /data{1...4} --console-address ":9001"
volumes:
  - ./data1:/data1
  - ./data2:/data2
  - ./data3:/data3
  - ./data4:/data4
```

**Avantages:**
- 🔹 Stockage plus efficace que la réplication (50% vs 300%)
- 🔹 Tolérance aux pannes (N/2 disques)
- 🔹 Reconstruction automatique des données

📚 **Source:** [MinIO Erasure Coding Documentation](https://min.io/docs/minio/linux/operations/concepts/erasure-coding.html)

### 2️⃣ Upload de Dataset avec boto3

Le script [upload_dataset.py](upload_dataset.py) démontre l'utilisation de boto3 (compatible S3) pour:
- Créer un bucket
- Uploader un fichier CSV
- Lister les objets stockés

```python
s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='minioadmin',
    aws_secret_access_key='minioadmin123'
)
```

### 3️⃣ Sécurité IAM - Utilisateur Lecture Seule

Création d'un utilisateur `lecteur` avec une politique JSON qui autorise uniquement:
- `s3:GetObject` (téléchargement)
- `s3:ListBucket` (liste)

**Test inclus:** [test_readonly.py](test_readonly.py)

```bash
python test_readonly.py
```

**Résultat attendu:**
```
✓ Lecture: Autorisée
✓ Écriture: Refusée
✓ Suppression: Refusée
```

### 4️⃣ Conformité - Object Locking

Activation du **Legal Hold** sur [facture_2024_001.pdf](facture_2024_001.pdf), empêchant toute modification ou suppression, même par l'administrateur.

**Cas d'usage:** Conformité RGPD, audits financiers, archivage légal

### 5️⃣ Résilience - Simulation de Panne

**Scénario:**
1. Arrêter MinIO
2. Supprimer le contenu de `data2/` (simuler un disque HS)
3. Redémarrer MinIO
4. Vérifier que les données sont toujours accessibles

**Test inclus:** [test_resilience.py](test_resilience.py)

```bash
# Simuler la panne
docker-compose down
Remove-Item -Recurse -Force .\data2\*

# Redémarrer
docker-compose up -d

# Tester la récupération
python test_resilience.py
```

**Résultat:** ✅ Les données sont reconstituées via Erasure Coding!

## 🎬 Création de la Vidéo de Démonstration

### Scripts Fournis

1. **[SCRIPT_VOIX_OFF.md](SCRIPT_VOIX_OFF.md)** - Narration complète (2-3 min)
2. **[COMMANDES.md](COMMANDES.md)** - Toutes les commandes à exécuter
3. **[PLAN_MONTAGE.md](PLAN_MONTAGE.md)** - Plan détaillé avec timing

### Séquences Vidéo

| Timing | Séquence | Contenu |
|--------|----------|---------|
| 0:00-0:15 | Introduction | Présentation du projet |
| 0:15-0:45 | Installation | Docker + Erasure Coding |
| 0:45-1:10 | Upload | Script Python boto3 |
| 1:10-1:35 | Sécurité | IAM + Politique |
| 1:35-2:00 | Conformité | Object Locking |
| 2:00-2:40 | Résilience | Simulation panne |
| 2:40-3:00 | Conclusion | Récap + GitHub |

### Outils Recommandés

- **Capture:** OBS Studio, Camtasia
- **Montage:** DaVinci Resolve, Premiere Pro
- **Résolution:** 1920x1080 (Full HD)
- **Format:** MP4 (H.264)

## 🧪 Tests et Validation

### Test Complet

```bash
# 1. Démarrer MinIO
docker-compose up -d

# 2. Attendre le démarrage (10-15 secondes)
docker logs minio-erasure-coding

# 3. Upload du dataset
python upload_dataset.py

# 4. Test sécurité
python test_readonly.py

# 5. Simulation panne
docker-compose down
Remove-Item -Recurse -Force .\data2\*
docker-compose up -d

# 6. Test résilience
python test_resilience.py
```

## 📚 Références et Documentation

### Documentation Officielle MinIO

- [Core Concepts](https://min.io/docs/minio/linux/operations/concepts.html)
- [Erasure Coding](https://min.io/docs/minio/linux/operations/concepts/erasure-coding.html)
- [Object Locking](https://min.io/docs/minio/linux/operations/concepts/object-locking.html)
- [Identity Access Management](https://min.io/docs/minio/linux/administration/identity-access-management.html)

### Articles Techniques

- 📖 [Erasure Coding vs Replication](https://medium.com/@minio/erasure-coding-vs-replication-8f89b12c8faa) - Article Medium
- 📖 [MinIO vs AWS S3: A Detailed Comparison](https://blog.min.io/minio-vs-s3/)

### Technologies Utilisées

- **MinIO:** Stockage objet compatible S3
- **Docker:** Conteneurisation
- **Python 3:** Scripts d'automatisation
- **boto3:** Bibliothèque AWS SDK pour Python
- **WSL2:** Sous-système Linux pour Windows

## 🛠️ Configuration Avancée

### Modifier le Nombre de Disques

Pour tester avec plus de disques (ex: 8 disques pour EC:4):

```yaml
# docker-compose.yml
command: server /data{1...8} --console-address ":9001"
volumes:
  - ./data1:/data1
  # ... jusqu'à data8
```

### Changer les Credentials

```yaml
environment:
  MINIO_ROOT_USER: votre_username
  MINIO_ROOT_PASSWORD: votre_password_securise
```

### Activer HTTPS (Production)

```yaml
volumes:
  - ./certs:/root/.minio/certs
```

Générer les certificats:
```bash
openssl req -new -x509 -days 365 -nodes \
  -out ./certs/public.crt \
  -keyout ./certs/private.key
```

## ⚠️ Dépannage

### MinIO ne démarre pas

```bash
# Vérifier les logs
docker logs minio-erasure-coding

# Vérifier les ports
netstat -an | findstr "9000"
netstat -an | findstr "9001"
```

### Erreur "Access Denied"

1. Vérifier les credentials dans le script Python
2. Vérifier que l'utilisateur a bien la politique attachée
3. Consulter: `Identity > Users > [user] > Policies`

### Perte de données après panne

Si plus de N/2 disques sont perdus (ex: 3/4 disques), les données ne peuvent pas être reconstruites. C'est le comportement attendu de l'Erasure Coding.

## 🎓 Compétences Démontrées

- ✅ Déploiement d'infrastructure avec Docker
- ✅ Programmation Python (boto3, API S3)
- ✅ Gestion de la sécurité (IAM, politiques)
- ✅ Conformité réglementaire (Object Locking)
- ✅ Compréhension des systèmes distribués
- ✅ Tests de résilience et disaster recovery

## 📊 Comparaison MinIO vs AWS S3

| Critère | MinIO | AWS S3 |
|---------|-------|--------|
| **Coût** | Gratuit (open-source) | Payant (usage) |
| **Hébergement** | Local / On-premise | Cloud uniquement |
| **API** | 100% compatible S3 | Natif S3 |
| **Erasure Coding** | ✅ EC:2 à EC:16 | ✅ (non configurable) |
| **Performance** | Très rapide (local) | Dépend de la région |
| **Sécurité** | IAM, encryption | IAM, encryption |
| **Conformité** | WORM, Legal Hold | WORM, Glacier Vault Lock |
| **Complexité** | Moyenne | Faible |

## 🤝 Contributions

Ce projet est à but éducatif. Les suggestions d'amélioration sont les bienvenues!

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👤 Auteur

**Étudiante ISIBD - 2ᵉ année**
- 📧 Email: [votre.email@isibd.fr]
- 💼 LinkedIn: [votre-profil]
- 🐙 GitHub: [votre-username]

## 🙏 Remerciements

- L'équipe **MinIO** pour la documentation exceptionnelle
- La communauté **Docker** pour les conteneurs
- **AWS** pour l'API S3 qui est devenue un standard

---

<p align="center">
  <strong>⭐ Si ce projet vous a aidé, n'oubliez pas de lui donner une étoile sur GitHub ! ⭐</strong>
</p>

<p align="center">
  <img src="https://min.io/resources/img/logo.svg" width="200" alt="MinIO Logo">
</p>

---

**Dernière mise à jour:** Décembre 2025  
**Version:** 1.0.0  
**Status:** ✅ Prêt pour production (demo)

# MinIO - Commandes de Manipulation

## 🚀 Démarrage

### 1. Démarrer MinIO (4 nœuds distribués)
```bash
docker-compose up -d
```

### 2. Vérifier les conteneurs
```bash
docker ps
```

---

## 📦 Upload de Données

### Upload du dataset
```bash
python upload_dataset.py
```

### Upload d'un fichier PDF (facture)
```bash
python upload_invoice.py
```

### Upload personnalisé
```bash
python upload_data.py
```

---

## 🔐 Gestion IAM

### Créer un utilisateur lecture seule
```bash
python create_iam_user.py
```

### Tester les permissions
```bash
python test_iam.py
python test_readonly.py
```

---

## 🛡️ Test de Résilience

### 1. Simuler une panne de disque
```bash
docker stop minio1
```

### 2. Vérifier la récupération des données
```bash
python test_resilience.py
```

### 3. Arrêter un second nœud (test EC:2)
```bash
docker stop minio2
```

### 4. Tester la récupération avec 2 pannes
```bash
python test_resilience.py
```

### 5. Redémarrer les nœuds
```bash
docker start minio1 minio2
```

---

## 🌐 Accès Console Web

### URL
```
http://localhost:9001
```

### Identifiants
- **Access Key:** `minioadmin`
- **Secret Key:** `minioadmin`

---

## 🧹 Nettoyage

### Arrêter les conteneurs
```bash
docker-compose down
```

### Nettoyer les données
```bash
python cleanup.py
```

### Supprimer tout (conteneurs + volumes + images)
```bash
docker-compose down -v --rmi all
```

---

## 📊 Commandes MinIO Client (mc)

### Configuration de l'alias
```bash
mc alias set myminio http://localhost:9000 minioadmin minioadmin
```

### Lister les buckets
```bash
mc ls myminio
```

### Lister les objets d'un bucket
```bash
mc ls myminio/demo
```

### Télécharger un fichier
```bash
mc cp myminio/demo/dataset.txt ./dataset-downloaded.txt
```

### Supprimer un objet
```bash
mc rm myminio/demo/dataset.txt
```

### Copier un bucket entier
```bash
mc cp --recursive myminio/demo ./backup
```

---

## 🔍 Commandes de Diagnostic

### Vérifier l'état des nœuds
```bash
docker-compose ps
```

### Voir les logs
```bash
docker-compose logs -f
```

### Logs d'un nœud spécifique
```bash
docker logs minio1
```

### Inspecter un conteneur
```bash
docker inspect minio1
```

---

## 📝 Variables d'Environnement

```bash
MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=minioadmin
MINIO_ENDPOINT=http://localhost:9000
```

---

## 🛠️ Dépannage

### Recréer les conteneurs
```bash
docker-compose down
docker-compose up -d --force-recreate
```

### Vérifier la connectivité
```bash
curl http://localhost:9000/minio/health/live
```

### Réinitialiser complètement
```bash
docker-compose down -v
rm -rf data1 data2 data3 data4
docker-compose up -d
```

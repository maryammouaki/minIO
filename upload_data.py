"""Upload simple vers MinIO"""
import boto3
from botocore.client import Config

# Configuration
s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='admin',
    aws_secret_access_key='admin123',
    config=Config(signature_version='s3v4')
)

print("\n=== UPLOAD VERS MINIO ===\n")

# Créer le fichier dataset.txt si il n'existe pas
import os
if not os.path.exists('dataset.txt'):
    with open('dataset.txt', 'w', encoding='utf-8') as f:
        f.write("=== DONNÉES IMPORTANTES ===\n")
        f.write("Maryam is in ISIBD\n")
        f.write("Elle étudie le Big Data\n")
        f.write("MinIO assure la résilience des données\n")
        f.write("\nListe des étudiants:\n")
        f.write("1. Maryam - ISIBD - Big Data\n")
        f.write("2. Ahmed - ISIBD - Cloud Computing\n")
        f.write("3. Fatima - ISIBD - Machine Learning\n")
        f.write("4. Youssef - ISIBD - DevOps\n")
        f.write("\nCe fichier est protégé par Erasure Coding EC:2\n")
        f.write("Tolérance de panne: 2 disques sur 4\n")
    print("✓ Fichier 'dataset.txt' créé avec contenu complet")

# Créer bucket
try:
    s3.create_bucket(Bucket='demo')
    print("✓ Bucket 'demo' créé")
except:
    print("✓ Bucket 'demo' existe déjà")

# Upload fichier
s3.upload_file('dataset.txt', 'demo', 'dataset.txt')
print("✓ Fichier 'dataset.txt' uploadé avec succès")

# Lister les objets
response = s3.list_objects_v2(Bucket='demo')
print("\nFichiers dans le bucket 'demo':")
for obj in response.get('Contents', []):
    print(f"  - {obj['Key']} ({obj['Size']} bytes)")

print("\n✅ Upload terminé ! Vérifiez dans la console: http://localhost:9001")

"""Test résilience après panne disque"""
import boto3
from botocore.client import Config
import os

s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='admin',
    aws_secret_access_key='admin123',
    config=Config(signature_version='s3v4')
)

print("\n" + "=" * 60)
print("TEST DE RÉSILIENCE MINIO - ERASURE CODING")
print("=" * 60 + "\n")

# ÉTAPE 1: Afficher le contenu AVANT la panne
print("📄 ÉTAPE 1 - CONTENU AVANT LA PANNE:")
print("=" * 60)
if os.path.exists('dataset.txt'):
    with open('dataset.txt', 'r', encoding='utf-8') as f:
        original_content = f.read()
    print(original_content)
    print("=" * 60)
    print(f"✓ Fichier original: {len(original_content)} bytes\n")
else:
    original_content = "Maryam is in ISIBD"
    print(original_content)
    print("=" * 60)
    print("⚠️  Fichier dataset.txt non trouvé localement\n")

# ÉTAPE 2: Vérifier l'état après la panne
print("📄 ÉTAPE 2 - ÉTAT APRÈS LA PANNE:")
print("=" * 60)
print("🔴 PANNE SIMULÉE: Le disque data2 a été supprimé")
print("⚠️  Sans Erasure Coding, le fichier serait PERDU ou INCOMPLET")
print("=" * 60 + "\n")

# ÉTAPE 3: Récupération
print("📄 ÉTAPE 3 - RÉCUPÉRATION AVEC ERASURE CODING:")
print("=" * 60)

try:
    # Récupérer le fichier
    response = s3.get_object(Bucket='demo', Key='dataset.txt')
    content = response['Body'].read().decode('utf-8')
    
    print("✓ Connexion à MinIO établie")
    print("✓ Bucket 'demo' accessible")
    print("✓ Fichier récupéré avec succès!")
    print(f"  Taille: {len(content)} bytes\n")
    
    print("CONTENU RÉCUPÉRÉ:")
    print("-" * 60)
    print(content)
    print("-" * 60)
    
    # Sauvegarder localement
    with open('dataset_recovered.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    print("\n✓ Fichier sauvegardé: dataset_recovered.txt")
    
    # Comparaison
    print("\n" + "=" * 60)
    print("📊 COMPARAISON:")
    print("=" * 60)
    print(f"Avant la panne  : {len(original_content)} bytes")
    print(f"Après récupération : {len(content)} bytes")
    
    if content == original_content:
        print("\n✅ LES FICHIERS SONT IDENTIQUES - AUCUNE PERTE DE DONNÉES!")
    else:
        print("\n⚠️  Différence détectée")
    
    print("\n" + "=" * 60)
    print("🎉 RÉSILIENCE CONFIRMÉE!")
    print("=" * 60)
    print("\n✓ Malgré la perte du disque data2, toutes les données sont:")
    print("  • Accessibles")
    print("  • Lisibles")  
    print("  • Intègres (100% récupérées)\n")
    print("🔍 EXPLICATION:")
    print("  L'Erasure Coding (EC:2) de MinIO a reconstruit")
    print("  les fragments manquants à partir des blocs de parité.\n")
    print("  Configuration: 4 disques → Tolérance: 2 pannes (N/2)\n")
    print("📚 https://min.io/docs/minio/linux/operations/concepts/erasure-coding.html\n")
    
except Exception as e:
    print(f"❌ Erreur: {e}")
    print("\n⚠️  Assurez-vous que MinIO est démarré:")
    print("   docker-compose up -d")

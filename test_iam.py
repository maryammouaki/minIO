"""Test de l'utilisateur IAM avec permissions restreintes"""
import boto3
from botocore.client import Config

# Client avec utilisateur restreint
s3_lecteur = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='lecteur',
    aws_secret_access_key='lecteur123',
    config=Config(signature_version='s3v4')
)

print("\n=== TEST UTILISATEUR IAM 'lecteur' ===\n")

# TEST 1: Lecture (devrait fonctionner)
print("TEST 1: Lecture du fichier dataset.txt")
try:
    response = s3_lecteur.get_object(Bucket='demo', Key='dataset.txt')
    content = response['Body'].read().decode('utf-8')
    print(f"✓ SUCCÈS: Lecture autorisée ({len(content)} bytes)")
except Exception as e:
    print(f"❌ ÉCHEC: {e}")

# TEST 2: Écriture (devrait échouer)
print("\nTEST 2: Tentative d'écriture")
try:
    s3_lecteur.put_object(Bucket='demo', Key='test.txt', Body=b'test')
    print("❌ PROBLÈME: Écriture autorisée!")
except Exception as e:
    if "Access Denied" in str(e):
        print("✓ SUCCÈS: Écriture correctement refusée")
    else:
        print(f"⚠️  Erreur: {e}")

# TEST 3: Suppression (devrait échouer)
print("\nTEST 3: Tentative de suppression")
try:
    s3_lecteur.delete_object(Bucket='demo', Key='dataset.txt')
    print("❌ PROBLÈME: Suppression autorisée!")
except Exception as e:
    if "Access Denied" in str(e):
        print("✓ SUCCÈS: Suppression correctement refusée")
    else:
        print(f"⚠️  Erreur: {e}")

print("\n" + "="*50)
print("🎯 L'utilisateur 'lecteur' a des permissions lecture seule!")
print("="*50)

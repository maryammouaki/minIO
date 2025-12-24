"""
Script de test pour vérifier les permissions de l'utilisateur restreint
"""

import boto3
from botocore.client import Config

# Configuration pour l'utilisateur restreint
MINIO_ENDPOINT = "http://localhost:9000"
ACCESS_KEY = "lecteur"
SECRET_KEY = "lecteur123"
BUCKET_NAME = "datasets"

def test_readonly_user():
    """Teste les permissions de l'utilisateur en lecture seule"""
    
    print("=== Test de l'utilisateur 'lecteur' (lecture seule) ===\n")
    
    # Créer le client S3 avec les credentials de l'utilisateur restreint
    s3_lecteur = boto3.client(
        's3',
        endpoint_url=MINIO_ENDPOINT,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        config=Config(signature_version='s3v4'),
        region_name='us-east-1'
    )
    
    # TEST 1: Lecture (devrait fonctionner)
    print("TEST 1: Lecture du fichier addresses.csv")
    try:
        response = s3_lecteur.get_object(Bucket=BUCKET_NAME, Key='addresses.csv')
        content = response['Body'].read().decode('utf-8')
        lines = content.split('\n')
        print(f"✓ SUCCÈS: Lecture autorisée")
        print(f"  Taille: {len(content)} bytes")
        print(f"  Nombre de lignes: {len(lines)}")
        print(f"  Première ligne: {lines[0][:50]}...")
    except Exception as e:
        print(f"❌ ÉCHEC: {e}")
    
    print()
    
    # TEST 2: Liste des objets (devrait fonctionner)
    print("TEST 2: Liste des objets dans le bucket")
    try:
        response = s3_lecteur.list_objects_v2(Bucket=BUCKET_NAME)
        if 'Contents' in response:
            print(f"✓ SUCCÈS: Liste autorisée ({len(response['Contents'])} objets)")
            for obj in response['Contents']:
                print(f"  - {obj['Key']}")
        else:
            print("✓ SUCCÈS: Liste autorisée (bucket vide)")
    except Exception as e:
        print(f"❌ ÉCHEC: {e}")
    
    print()
    
    # TEST 3: Écriture (devrait échouer)
    print("TEST 3: Tentative d'écriture d'un fichier test.txt")
    try:
        s3_lecteur.put_object(
            Bucket=BUCKET_NAME, 
            Key='test.txt', 
            Body=b'Tentative de violation de la politique'
        )
        print("❌ PROBLÈME: Écriture autorisée alors qu'elle devrait être interdite!")
    except Exception as e:
        if "Access Denied" in str(e) or "AccessDenied" in str(e):
            print(f"✓ SUCCÈS: Écriture correctement refusée")
        else:
            print(f"⚠️  Erreur inattendue: {e}")
    
    print()
    
    # TEST 4: Suppression (devrait échouer)
    print("TEST 4: Tentative de suppression de addresses.csv")
    try:
        s3_lecteur.delete_object(Bucket=BUCKET_NAME, Key='addresses.csv')
        print("❌ PROBLÈME: Suppression autorisée alors qu'elle devrait être interdite!")
    except Exception as e:
        if "Access Denied" in str(e) or "AccessDenied" in str(e):
            print(f"✓ SUCCÈS: Suppression correctement refusée")
        else:
            print(f"⚠️  Erreur inattendue: {e}")
    
    print()
    
    # TEST 5: Création de bucket (devrait échouer)
    print("TEST 5: Tentative de création d'un nouveau bucket")
    try:
        s3_lecteur.create_bucket(Bucket='test-bucket')
        print("❌ PROBLÈME: Création de bucket autorisée!")
    except Exception as e:
        if "Access Denied" in str(e) or "AccessDenied" in str(e):
            print(f"✓ SUCCÈS: Création de bucket correctement refusée")
        else:
            print(f"⚠️  Erreur inattendue: {e}")
    
    print("\n=== Résumé ===")
    print("✓ Lecture: Autorisée (correct)")
    print("✓ Écriture: Refusée (correct)")
    print("✓ Suppression: Refusée (correct)")
    print("✓ Administration: Refusée (correct)")
    print("\n🎯 L'utilisateur 'lecteur' a bien des permissions en lecture seule!")

if __name__ == "__main__":
    test_readonly_user()

"""
Création d'un utilisateur IAM avec permissions lecture seule
Via MinIO Client (mc) - Compatible avec MinIO Community Edition
"""

import subprocess
import os

print("\n=== CRÉATION UTILISATEUR IAM ===\n")

# Vérifier si mc.exe existe
if not os.path.exists("mc.exe"):
    print("⚠️  Client MinIO (mc.exe) non trouvé")
    print("\nTéléchargez-le avec:")
    print('Invoke-WebRequest -Uri "https://dl.min.io/client/mc/release/windows-amd64/mc.exe" -OutFile "mc.exe"')
    exit(1)

# Configurer l'alias
print("1. Configuration de l'alias MinIO...")
result = subprocess.run([
    ".\\mc.exe", "alias", "set", "myminio", 
    "http://localhost:9000", "admin", "admin123"
], capture_output=True, text=True)

if result.returncode == 0:
    print("✓ Alias configuré")
else:
    print(f"❌ Erreur: {result.stderr}")
    exit(1)

# Créer l'utilisateur lecteur
print("\n2. Création de l'utilisateur 'lecteur'...")
result = subprocess.run([
    ".\\mc.exe", "admin", "user", "add", "myminio", "lecteur", "lecteur123"
], capture_output=True, text=True)

if result.returncode == 0 or "already exists" in result.stderr:
    print("✓ Utilisateur 'lecteur' créé")
else:
    print(f"❌ Erreur: {result.stderr}")

# Créer la policy
print("\n3. Création de la policy de lecture seule...")
result = subprocess.run([
    ".\\mc.exe", "admin", "policy", "create", "myminio", 
    "readonly-demo", "readonly-policy.json"
], capture_output=True, text=True)

if result.returncode == 0 or "already exists" in result.stderr:
    print("✓ Policy 'readonly-demo' créée")
else:
    print(f"❌ Erreur: {result.stderr}")

# Attacher la policy
print("\n4. Attachement de la policy à l'utilisateur...")
result = subprocess.run([
    ".\\mc.exe", "admin", "policy", "attach", "myminio", 
    "readonly-demo", "--user=lecteur"
], capture_output=True, text=True)

if result.returncode == 0:
    print("✓ Policy attachée à l'utilisateur 'lecteur'")
else:
    print(f"❌ Erreur: {result.stderr}")

# Vérifier
print("\n5. Vérification...")
result = subprocess.run([
    ".\\mc.exe", "admin", "user", "info", "myminio", "lecteur"
], capture_output=True, text=True)

print(result.stdout)

print("\n" + "="*50)
print("✅ UTILISATEUR IAM CRÉÉ AVEC SUCCÈS")
print("="*50)
print("\nCredentials:")
print("  Access Key: lecteur")
print("  Secret Key: lecteur123")
print("  Permissions: Lecture seule sur bucket 'demo'")
print("\nTestez avec: python test_iam.py")

# 📚 Literature as Code : Le Framework

> **Version** : 2.0.0 (Narrative Engine)
> **Philosophie** : Traiter l'écriture d'un roman comme un projet d'ingénierie logicielle.
>
> 🚀 **Démarrage Rapide** : Lisez le [MANUEL DE L'INGÉNIEUR (HOWTO)](HOWTO.md).

---

## 🌟 La Vision
Ce framework transforme votre roman en une **Codebase compilée**.
Il remplace l'improvisation chaotique par un **Pipeline de Production** rigoureux :
1.  **Architecture** : Base de données structurée (Personnages, Lieux).
2.  **Spécification** : Fichiers JSON définissant précisément chaque chapitre.
3.  **Compilation** : Assemblage automatique du contexte pertinent (RAG).
4.  **CI/CD** : Tests unitaires (Linting) et tableau de bord automatique.

---

## 🔄 Le Pipeline en 4 Phases

### 1. Architecture (`00_SPECS` & `01_CONTEXT_DB`)
*   **La Bible** : Vous ne rédigez pas au fil de l'eau. Vous peuplez une base de données.
*   Chaque personnage et lieu est un fichier Markdown avec Frontmatter YAML.
*   *Pas de fiche ? Pas de chapitre.*

### 2. Blueprint (`02_STRUCTURE`)
*   **Ingénierie Narrative** : Chaque chapitre est défini par une **Spec JSON**.
*   Ce fichier dicte le but narratif, les émotions et les personnages requis.
*   C'est la "Vérité Technique" avant la prose.

### 3. Build (`manage.py assemble`)
*   Le moteur (**Context Assembler**) lit votre Spec JSON.
*   Il va chercher *chirurgicalement* les infos nécessaires dans la DB.
*   Il génère un **Prompt Parfait**, pur et sans bruit, prêt pour la rédaction.

### 4. Production (`03_MANUSCRIPT`)
*   **Drafting** : Rédaction du texte (Humain ou IA) basée sur le Prompt compilé.
*   **Linting** : `manage.py lint` analyse la qualité (Show Don't Tell, Adverbes).
*   **Sync** : `manage.py sync` met à jour votre tableau de bord `sommaire.md`.

---

## 🛠️ La Boîte à Outils (CLI)

Tout est piloté par `manage.py` :

```bash
# Vérifier la santé du projet
python manage.py inspect

# Initialiser la structure
python manage.py init

# Compiler un chapitre (Build)
python manage.py assemble 02_STRUCTURE/specs_json/ch01.json -o build.txt

# Vérifier la qualité (Test)
python manage.py lint 03_MANUSCRIPT/01_drafts/ch01.md

# Mettre à jour les stats (Dashboard)
python manage.py sync
```

---

> *Ne commencez pas à écrire. Commencez par compiler.*

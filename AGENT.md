# AGENT.md - Guide pour l'IA Assistante

> **Rôle** : Tu es à la fois l'**Agent de Production Littéraire** (Utilisateur) et l'**Ingénieur du Framework** (Mainteneur).
> *   **Mode Production** : Tu écris le roman.
> *   **Mode Maintenance** : Tu améliores le code et les processus.

## 🎯 Ta Mission
1.  **Produire** : Transformer la matière brute en roman via le pipeline.
2.  **Maintenir** : Garantir que ce boilerplate reste clonable, propre et agnostique.

---

## 📋 Workflow de Production (Utilisation)

### ÉTAPE 0 : SETUP (Initialisation)
**Action** :
1. Si le projet est vide, exécute `python manage.py init`.
2. Cela crée la structure et les fichiers critiques (`sommaire.md`, templates).
3. **Note** : Si ces fichiers manquent, c'est NORMAL dans un boilerplate vierge. Ne les signale pas comme erreur sauf si tu es en train d'essayer d'écrire.

---

### ÉTAPE 1 : INTAKE (Réception de la Demande)
**Localisation** : `00_SPECS/`

**Action** :
11. Scanne le dossier `00_SPECS/`.
12. Lis `01_concept.md`, `02_casting.md` et `03_story_design.md`.
13. **Mise à jour** : Vérifie que le chapitre à traiter est bien listé dans `03_MANUSCRIPT/01_drafts/sommaire.md`.

**Output** : Compréhension du contexte global.

---

### ÉTAPE 2 : PLANNING (Architecture du Chapitre)
**Localisation** : `02_STRUCTURE/specs_json/`

**Action** :
1. Crée/Lis le spec JSON du chapitre (ex: `ch01_spec.json`).
2. Vérifie qu'il contient :
   - `narrative_goal` (But)
   - `emotional_beat` (Emotion)
   - `required_characters` (Casting)

**Output** : Un plan d'action précis pour le chapitre.

---

### ÉTAPE 3 : CONTEXT LOADING (Assemblage)
**Localisation** : `05_BUILD/logs/`

**Action** :
1. **N'essaie pas de deviner le contexte.**
2. Exécute la commande d'assemblage (Outil Helper) :
   ```bash
   python manage.py assemble 02_STRUCTURE/specs_json/ch01_spec.json -o 05_BUILD/logs/prompt_ch01.txt
   ```
3. Lis le fichier généré (`prompt_ch01.txt`). C'est ta mémoire de travail pour la session.

**Output** : Mémoire chargée avec zéro hallucination.

---

### ÉTAPE 4 : DRAFTING (Rédaction Assistée)
**Localisation** : `03_MANUSCRIPT/01_drafts/`

**Action** :
1. **Toi (l'Agent)**, utilise le contexte chargé pour rédiger le chapitre.
2. Crée le fichier `ch{XX}_v0.md` directement dans l'IDE.
3. Respecte les `docs/best_practices/` (Show Don't Tell, Dialogues).
4. **Mise à jour** : Passe le status du chapitre à `🟡 Draft` dans `sommaire.md`.

**Output** : Premier jet brut.

---

### ÉTAPE 5 : REVIEW (Contrôle Qualité)
**Localisation** : `05_BUILD/logs/`

**Action** :
1. Exécute le linter automatique :
   ```bash
   python manage.py lint 03_MANUSCRIPT/01_drafts/ch{XX}_v0.md
   ```
2. Analyser le score.
   - Si score < 0.8 : Corrige les problèmes (Adverbes, Voix Passive).
   - Si score >= 0.8 : Passe à l'étape suivante.

3. **Mise à jour** : Passe le status à `🔵 Review` dans `sommaire.md`.

**Output** : Chapitre validé techniquement.

---

### ÉTAPE 6 : REFACTORING (Polissage Humain)
**Localisation** : `03_MANUSCRIPT/02_staging/`

**Action** :
1. Une fois validé par l'humain, déplace vers `02_staging/`.
2. **Mise à jour** : Passe le status à `🟢 Done` dans `sommaire.md`.

---

## 🚨 Règles Critiques

### Règle 1 : Context Awareness (Boilerplate vs Projet)
*   Si tu audites le système (via `/inspect`), tu vérifies le **MOULE** (Templates, Scripts, Automation). L'absence de chapitres ou de sommaire est normale.
*   Si tu produis du contenu, tu vérifies le **GÂTEAU** (Fichiers générés). L'absence de sommaire est critique.

### Règle 2 : Utilise les Outils (CLI First)
Ne fais pas manuellement ce que `manage.py` peut faire. Cela garantit la reproductibilité.

### Règle 3 : Le Sommaire est la Vérité (En Production)
Si un chapitre n'est pas dans `sommaire.md`, il n'existe pas.

### Règle 4 : Privilégie la QUALITÉ sur la VITESSE
Mieux vaut un chapitre court et dense qu'un long chapitre vide.

---

## 📚 Documents de Référence
Avant CHAQUE session, assure-toi de connaître :
1. `HOWTO.md` - Le manuel d'utilisation.
2. `docs/best_practices/` - Les règles d'écriture.

---

## 💻 Commandes Spéciales

### `/inspect`
> **Action** : Exécute une **Inspection d'Intégrité du Framework** (Mode Ingénieur).
1.  **Scope** : Ignore les dossiers de contenu (`00_SPECS`, `03_MANUSCRIPT`, `01_CONTEXT_DB`). Focus sur `_SYSTEM`, `manage.py`, `docs`.
2.  **Vérifie** :
    *   La présence des **Templates** dans `_SYSTEM/defaults/`.
    *   La cohérence entre `HOWTO.md` et les scripts réels (ex: une commande documentée existe-t-elle ?).
    *   L'absence de dette technique dans les scripts python.
3.  **Propose** :
    *   Des améliorations d'automatisation (Ex: "Ajouter une commande X").
    *   Des corrections de documentation.
4.  **Perspective** : "Si je clone ce repo maintenant, est-ce que tout fonctionne ?"

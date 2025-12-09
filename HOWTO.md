# 📘 Manuel de l'Ingénieur Littéraire (Literature as Code)

> "Ne commencez pas à écrire. Commencez par compiler."

Ce framework transforme l'écriture d'un roman en un processus d'ingénierie logicielle. Il remplace le "Syndrome de la Page Blanche" par un pipeline de production automatisé.

---

## 🏗️ Philosophie : Le Roman est une Codebase

Dans ce système, votre roman n'est pas un fichier Word géant. C'est un **projet compilé**.
*   **Database (Source de Vérité)** : Vos personnages et vos lieux sont des données structurées.
*   **Specs (Instructions)** : Vos chapitres sont définis par des fichiers de configuration JSON.
*   **Build (Assemblage)** : Un script Python assemble le contexte parfait pour chaque scène.
*   **Linter (Tests)** : Un script valide automatiquement la qualité narrative (Show Don't Tell, Adverbes).

---

## 🔄 Le Pipeline de Production

### Phase 1 : Architecture (Le Cerveau)
*Avant d'écrire une seule ligne de dialogue, nous construisons le monde.*

1.  **Initialisation** :
    *   `python manage.py init` : Déploie l'échafaudage du projet.
2.  **La Bible (Specs)** :
    *   Remplissez `00_SPECS/01_concept.md` : L'ADN thématique de l'histoire.
    *   Remplissez `00_SPECS/02_casting.md` : L'index de tous les acteurs du récit.
3.  **La Base de Données (Context DB)** :
    *   Pour chaque personnage listé dans le Casting, créez une fiche dans `01_CONTEXT_DB/characters/`.
    *   Utilisez le template standard (Frontmatter YAML) pour que le système puisse les "lire".
    *   *Règle d'or : Si ce n'est pas dans la DB, l'IA va l'halluciner.*

### Phase 2 : Blueprinting (Le Squelette)
*Nous ne devinons pas la structure. Nous la spécifions.*

1.  **Design Narratif** :
    *   Utilisez `00_SPECS/03_story_design.md` pour tracer les 15 Beats (Save the Cat).
2.  **Spécification de Chapitre** :
    *   Pour chaque chapitre, créez un fichier JSON dans `02_STRUCTURE/specs_json/`.
    *   Définissez précisément :
        *   `narrative_goal` : Ce que le héros veut.
        *   `emotional_beat` : Le changement d'état émotionnel.
        *   `required_characters` : Les IDs des fiches personnages nécessaires.
        *   `settings` : Où cela se passe.

### Phase 3 : Le Build (Le Moteur)
*C'est ici que la magie opère. Nous transformons des fichiers épars en "Mémoire de Travail".*

1.  **La Commande d'Assemblage** :
    ```bash
    python manage.py assemble 02_STRUCTURE/specs_json/ch01_spec.json -o 05_BUILD/logs/prompt_ch01.txt
    ```
2.  **Ce que fait le système** :
    *   Il lit votre Spec JSON.
    *   Il va chercher *uniquement* les fiches personnages et lieux requises dans la DB.
    *   Il injecte les règles d'écriture globales.
    *   Il compile le tout dans un fichier `prompt_ch01.txt`.
3.  **Résultat** : Vous avez un contexte pur, sans bruit, prêt à être ingéré par une IA ou à servir de référence absolue pour votre rédaction.

### Phase 4 : Production & CI/CD (L'Usine)
*L'écriture devient de l'exécution.*

1.  **Drafting (Rédaction)** :
    *   Écrivez (ou générez) le texte dans `03_MANUSCRIPT/01_drafts/ch01_v0.md`.
2.  **Sync (Suivi)** :
    *   `python manage.py sync` : Met à jour automatiquement `sommaire.md` avec le nombre de mots et l'état d'avancement. C'est votre tableau de bord.
3.  **Testing (Linting)** :
    *   `python manage.py lint 03_MANUSCRIPT/01_drafts/ch01_v0.md`
    *   Le système analyse le texte et vous donne un score de qualité (Adverbes, Voix passive, Dialogues mous).
    *   🔴 *Fail* (< 0.8) : Refactoring requis.
    *   🟢 *Pass* (>= 0.8) : Prêt pour le staging.
4.  **Inspection (Maintenance)** :
    *   `python manage.py inspect` : Vérifie à tout moment que votre projet est structurellement sain.

---

## 🛠️ Référence Rapide des Commandes

| Commande | Rôle | Quand l'utiliser ? |
| :--- | :--- | :--- |
| `manage.py init` | Setup | Au tout début. |
| `manage.py inspect` | Santé | Quand vous avez un doute sur la structure. |
| `manage.py sync` | Dashboard | Après chaque session d'écriture. |
| `manage.py assemble [spec]` | **Build** | Avant d'écrire un chapitre. |
| `manage.py lint [file]` | **Test** | Après avoir écrit un chapitre. |
| `manage.py pipeline` | Batch | Pour tout reconstruire (Utilisateurs avancés). |

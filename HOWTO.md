# � Manuel de l'Utilisateur (Framework Guide)

Ce document décrit les **Cas d'Utilisation (Use Cases)** du framework "Literature as Code".
Il explique comment interagir avec le système pour produire du contenu narratif de manière fiable.

---

## 🏗️ Architecture du Système

Le framework fonctionne comme un pipeline de données. Vous injectez des spécifications (Specs) et du contexte (DB), le système produit du texte (Manuscript).

```mermaid
flowchart LR
    subgraph INPUT ["1. ENTRÉES (Ce que vous écrivez)"]
        direction TB
        Project[00_SPECS\n(Concept/Casting/Design)]
        Context[01_CONTEXT_DB\n(Fiches Persos/Lieux)]
        Spec[02_STRUCTURE\n(Specs Chapitres)]
    end

    subgraph PROCESS ["2. TRAITEMENT (Le Moteur)"]
        direction TB
        ScriptContext[context_assembler.py\n(Charge le contexte)]
        ScriptTest[test_runner.py\n(Vérifie la qualité)]
    end

    subgraph OUTPUT ["3. SORTIES (Le Résultat)"]
        direction TB
        Draft[03_MANUSCRIPT\n(Texte Généré)]
        Report[05_BUILD\n(Rapports de Validation)]
    end

    Project --> Spec
    Context --> ScriptContext
    Spec --> ScriptContext
    ScriptContext --> Draft
    Draft --> ScriptTest
    ScriptTest --> Report
```

---

## �️ Cas d'Utilisation (Workflows)

Voici les procédures standard pour utiliser le framework.

### UC-01 : Conception (Phase Spec-First)
**Acteurs** : Architecte + Critique
**But** : Définir les fondations AVANT de construire.

1.  **Naviguer** vers `00_SPECS/`.
2.  **Remplir** les 3 templates fondamentaux :
    *   `01_concept.md` : La graine (Genre, Thème, Règles).
    *   `02_casting.md` : Les acteurs (Ghost, Lie, Truth).
    *   `03_story_design.md` : Le plan (15 Beats Save The Cat).
3.  **Vérifier** la cohérence : Le Critique doit valider que le *Casting* peut porter le *Design*.

### UC-02 : Créer une Entité (Personnage/Lieu)
**Acteur** : Auteur
**But** : Peupler la base de données contextuelle (`01_CONTEXT_DB`).

1.  **Choisir** le template approprié dans `_SYSTEM/templates/` :
    *   `tpl_character.md` pour un personnage.
    *   `tpl_location.md` (à créer) pour un lieu.
2.  **Copier** le fichier dans `01_CONTEXT_DB/characters/` ou `01_CONTEXT_DB/world/`.
3.  **Renommer** le fichier (ex: `alice.md`).
4.  **Compléter** les champs obligatoires (Ghost, Lie, Truth).
    *   *Note : Ces champs sont utilisés par l'IA pour garantir la cohérence psychologique.*

### UC-03 : Spécifier un Chapitre
**Acteur** : Architecte (Auteur)
**But** : Définir le plan d'un chapitre avant rédaction.

1.  **Copier** `_SYSTEM/templates/tpl_chapter_spec.md`.
2.  **Coller** dans `02_STRUCTURE/act_{X}/` (ex: `act_1_thesis`).
3.  **Configurer** le fichier :
    *   `required_context` : Listez les chemins des fichiers créés dans l'UC-02.
    *   `narrative_goal` : Quel est le but du protagoniste ?
    *   `conflict` : Quel est l'obstacle ?

### UC-04 : Générer un Draft (Build)
**Acteur** : Système (via commande)
**But** : Transformer la Spec en Texte.

1.  **Ouvrir** le terminal dans VS Code.
2.  **Exécuter** la commande de build :
    ```bash
    python _SYSTEM/automation/build_chapter.py ch01
    ```
3.  **Consulter** le résultat dans `03_MANUSCRIPT/01_drafts/`.

### UC-05 : Valider la Qualité (Test)
**Acteur** : Système (Automatique)
**But** : Vérifier que le texte respecte les règles.

1.  Le script de build lance automatiquement `test_runner.py`.
2.  **Ouvrir** le rapport généré dans `05_BUILD/logs/`.
3.  **Analyser** les scores :
    *   *Linting* : Avez-vous trop d'adverbes ?
    *   *Structure* : Le conflit est-il présent ?

---

## 🧩 Glossaire du Framework

*   **Spec (Spécification)** : Le "ticket" qui décrit ce que le chapitre doit contenir. C'est la commande passée à l'IA.
*   **Context DB** : La mémoire à long terme du projet.
*   **Draft** : Le brouillon brut généré par l'IA.
*   **Staging** : Le brouillon relu et corrigé par l'humain.
*   **Master** : La version finale, canonique.

---

## 🤝 Workflow de Contribution (Knowledge First)

Ce framework est conçu pour évoluer. Chaque roman que vous écrivez est une occasion d'enrichir le système.

### Le Principe "Private Novel, Public Knowledge"
*   ⛔ **IGNORÉ (Privé)** : Vos romans, personnages et brouillons (`00_SPECS`, `01_CONTEXT_DB`, `03_MANUSCRIPT`, `05_BUILD`). Ils restent sur votre machine.
*   ✅ **TRAQUÉ (Partagé)** : La documentation, les tests et le moteur (`docs/`, `04_TESTS`, `_SYSTEM`).

### Comment contribuer ?
1.  **Vous découvrez une astuce** (ex: "Comment gérer un dialogue à 3 persos").
2.  **Créez** un fichier Markdown dans `docs/best_practices/` (ex: `dialogue_trio.md`).
3.  **Commitez et Pushez** ce fichier.
4.  Votre connaissance est désormais sauvegardée et disponible pour vos futurs clones du framework !


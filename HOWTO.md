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
        CLI[manage.py\n(Orchestrateur Unifié)]
        ScriptContext[context_assembler.py]
        ScriptTest[test_runner.py]
    end

    subgraph OUTPUT ["3. SORTIES (Le Résultat)"]
        direction TB
        Draft[03_MANUSCRIPT\n(Texte Généré)]
        Report[05_BUILD\n(Rapports de Validation)]
    end

    Project --> Spec
    Context --> ScriptContext
    Spec --> CLI
    CLI --> ScriptContext
    ScriptContext --> Draft
    Draft --> CLI
    CLI --> ScriptTest
    ScriptTest --> Report
```

---

## �️ Cas d'Utilisation (Workflows)

Voici les procédures standard pour utiliser le framework.

### UC-00 : Initialisation (Nouveau Projet)
**Acteurs** : Auteur
**But** : Préparer l'environnement de travail.

1.  **Ouvrir** le terminal.
2.  **Exécuter** : `python manage.py init`
3.  **Vérifier** que `00_SPECS` contient bien les templates copiés.

### UC-01 : Conception (Phase Spec-First)
**Acteurs** : Architecte + Critique
**But** : Définir les fondations AVANT de construire.

1.  **Naviguer** vers `00_SPECS/`.
2.  **Remplir** les fichiers générés lors de l'initialisation :
    *   `01_concept.md` : La graine (Genre, Thème, Règles).
    *   `02_casting.md` : Les acteurs (Ghost, Lie, Truth).
    *   `03_story_design.md` (à créer) : Le plan (15 Beats Save The Cat).
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
**Acteur** : Système (via CLI)
**But** : Assembler le contexte pour préparer l'écriture.

1.  **Exécuter** la commande d'assemblage :
    ```bash
    python manage.py assemble 02_STRUCTURE/specs_json/ch01_spec.json -o 05_BUILD/logs/prompt_ch01.txt
    ```
2.  **Utiliser** le prompt généré avec votre LLM préféré (ou via l'agent Draft).
3.  **Sauvegarder** le résultat dans `03_MANUSCRIPT/01_drafts/ch01.md`.

### UC-05 : Valider la Qualité (Test)
**Acteur** : Système (Automatique)
**But** : Vérifier que le texte respecte les règles.

1.  **Exécuter** le linter sur votre draft :
    ```bash
    python manage.py lint 03_MANUSCRIPT/01_drafts/ch01.md
    ```
2.  **Analyser** le rapport immédiat dans le terminal.
3.  **Corriger** si le score est insuffisant (< 0.8).

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


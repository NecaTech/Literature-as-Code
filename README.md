# 📚 Literature as Code : Le Framework

> **Version** : 1.0.0 (Alpha)
> **Philosophie** : Traiter l'écriture d'un roman comme un projet d'ingénierie logicielle complexe.

## 🌟 La Vision
Ce projet n'est pas un simple dossier de textes. C'est un **IDE Littéraire** conçu pour résoudre les problèmes majeurs de la génération d'histoires par IA (et par humains) :
1.  **Amnésie** (Oubli des détails passés).
2.  **Structure Plate** (Manque de tension dramatique).
3.  **Personnages Statiques** (Absence d'évolution psychologique).
4.  **Style "Beige"** (Prose lisse et sans saveur).

Nous remplaçons l'improvisation par une **Architecture Modulaire** et des **Tests Unitaires Narratifs**.

---

## 🏗️ Architecture du Projet

### `00_SYSTEM/` (Le Moteur)
Le cerveau de l'opération. Contient la configuration et les outils.
*   **`R_AND_D/pain_points/`** : Le backlog des "Bugs Littéraires" identifiés (ex: [PP-04 Flatline Structure](00_SYSTEM/R_AND_D/pain_points/pp_04_flatline_structure.md)).
*   **`templates/`** : Les modèles de fichiers pour standardiser la création.
    *   [`tpl_character.md`](00_SYSTEM/templates/tpl_character.md) : Fiche perso avec Ghost/Lie/Truth.
    *   [`tpl_chapter_spec.md`](00_SYSTEM/templates/tpl_chapter_spec.md) : Ticket JIRA pour un chapitre.
*   **`prompts/`** : Les instructions système pour les Agents (Architecte, Writer, Critic).

### `00_INBOX/` (Le Backlog)
Zone de dépot pour les idées brutes, les images de référence et les notes vocales non triées.

### `01_CONTEXT_DB/` (La Base de Données)
La **Source de Vérité** immuable. Si ce n'est pas écrit ici, ça n'existe pas.
*   **`characters/`** : Fiches détaillées de tous les acteurs.
*   **`world/`** : Règles de l'univers, lieux, factions, magie/technologie.

### `02_ARCHITECTURE/` (Le Blueprint)
Le plan de construction, structuré par **Actes** (Thèse, Antithèse, Synthèse).
*   Contient la `global_story_map.md` (Beat Sheet).
*   Chaque sous-dossier (`act_1_thesis`, etc.) contient les specs des chapitres à écrire.

### `03_SOURCE/` (Le Manuscrit)
Le code source du roman, versionné.
*   **`01_drafts/`** : Premier jet (Vomit Draft).
*   **`02_staging/`** : Version révisée et corrigée.
*   **`03_master/`** : Version finale validée (Golden Master).

### `04_TEST_SUITE/` (Le QA)
Outils de vérification de la qualité.
*   **`linting_rules/`** : Règles de style (Show Don't Tell, Rythme).
*   **`continuity_tests/`** : Vérification de la cohérence temporelle.

### `docs/` (La Bibliothèque)
Documentation théorique et méthodologique.
*   **`expert_narratology/`** : Théorie pure (Save The Cat, Arcs, Ironie).
*   **`best_practices/`** : Guides techniques (Dialogues, Tchekhov).

---

## 🚀 Workflow (Le Pipeline de Production)

### Phase 1 : R&D et Conception
1.  Identifier un problème (ex: "Mes dialogues sont plats").
2.  Créer un **Pain Point** dans `00_SYSTEM/R_AND_D/`.
3.  Documenter la solution théorique dans `docs/`.

### Phase 2 : Architecture (Pre-Prod)
1.  Définir la **Controlling Idea** et le **Thème**.
2.  Créer les fiches personnages dans `01_CONTEXT_DB` (Définir Ghost/Lie/Truth).
3.  Mapper les 15 Beats de l'histoire dans `02_ARCHITECTURE`.
4.  Créer une **Spec** pour chaque chapitre (`tpl_chapter_spec.md`).

### Phase 3 : Drafting (Prod)
1.  L'Agent Writer prend une Spec et le Context DB.
2.  Il génère le texte dans `03_SOURCE/01_drafts`.

### Phase 4 : Review & Refactor (Post-Prod)
1.  L'Agent Critic analyse le draft par rapport à la Spec et aux `linting_rules`.
2.  Le texte est corrigé et promu dans `03_SOURCE/02_staging`.

---

## 🤖 v2.0 Architecture Technique (Narrative Engine)

> **Mise à jour (Dec 2025)** : Transition vers une architecture "Software-First".

Nous ne dépendons plus uniquement de la discipline humaine. Un pipeline CI/CD (`workflow.yaml`) orchestre la production :

1.  **Specs as Code** : Les chapitres sont définis en JSON (`02_ARCHITECTURE/specs_json/`) pour être lisibles par les machines.
2.  **Automation Layer** : Des scripts Python (`00_SYSTEM/automation/`) gèrent l'assemblage du contexte (RAG) et l'exécution des tests.
3.  **LLM-as-a-Judge** : La qualité est mesurée par des tests unitaires (`test_runner.py`) avant validation.

---

## 🛠️ Commandes Utiles (Mental Model)

*   **"Initialiser un Perso"** : Copier `tpl_character.md` vers `01_CONTEXT_DB/characters/nom_du_perso.md`.
*   **"Lancer un Chapitre"** : Copier `tpl_chapter_spec.md` vers `02_ARCHITECTURE/act_X/chXX_titre.md`.
*   **"Debuguer une Scène"** : Vérifier si elle respecte la *Controlling Idea* et si le *Conflit* est clair.

---

> *Ce système est vivant. Il évolue avec notre compréhension de la narration.*

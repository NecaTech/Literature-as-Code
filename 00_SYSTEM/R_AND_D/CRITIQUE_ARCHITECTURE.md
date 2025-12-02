# CRITIQUE DE L'ARCHITECTURE : SLIDEWARE vs SOFTWARE

> **Auditeur** : Senior ML Engineer / DevOps
> **Date** : 2025-12-03
> **Verdict** : **POC (Proof of Concept) non-viable en production.**

## 1. Le Mythe du Binding (The "Folder" Fallacy)
Vous avez créé des dossiers (`01_CONTEXT_DB`, `02_ARCHITECTURE`) et vous appelez ça une "Base de Données". C'est mignon, mais techniquement faux.
*   **Le Problème** : Pour un LLM, un dossier n'est pas une base de données. Sans un **Moteur d'Indexation (Vector Store)** et un système de **Retrieval (RAG)**, ces fichiers sont des îles isolées.
*   **La Réalité** : Votre "Context Injector" est un script manuel glorifié. Si je change le nom d'un fichier, tout casse. Si le contexte dépasse 200k tokens, vous êtes morts.
*   **Ce qu'il manque** : Un vrai RAG (Retrieval Augmented Generation) qui indexe les chunks de texte et les récupère sémantiquement ("Qui est l'ennemi de X ?") au lieu de charger des fichiers entiers.

## 2. L'Absence de Pipeline d'Exécution (No Orchestrator)
Votre workflow repose sur l'espoir qu'un humain va copier-coller le bon prompt au bon moment.
*   **Le Problème** : Ce n'est pas du "Software Engineering", c'est du "Human Middleware".
*   **La Réalité** : Où est le script `build_chapter.py` ? Où est le fichier `workflow.yaml` (LangGraph/CrewAI) qui définit la chaîne : `Loader -> Drafter -> Critic -> Refactorer` ?
*   **Ce qu'il manque** : Un Framework Agentique (LangChain, AutoGen) pour automatiser la chaîne de production.

## 3. La Faiblesse du Testing (Vibe Checking vs Unit Testing)
Vous avez des "Checklists" dans vos templates Markdown. C'est bien pour les humains, inutile pour les machines.
*   **Le Problème** : Vous ne pouvez pas lancer une commande `npm test` pour vérifier si le chapitre 3 respecte le ton du chapitre 1.
*   **La Réalité** : Vous faites du "Vibe Checking" (lire et voir si ça "sonne" bien). C'est subjectif et non-reproductible.
*   **Ce qu'il manque** : Du **LLM-as-a-judge**. Des tests unitaires où un LLM (Juge) note la sortie du LLM (Rédacteur) sur des critères JSON précis (ex: `{"sentiment": "dark", "pacing_score": 0.8}`).

## 4. Le Manque à Gagner (Opportunity Cost)
En restant sur cette architecture de fichiers statiques, vous vous privez de :
*   **Structured Output** : Forcer l'IA à répondre en JSON pour garantir que chaque scène a un début, un milieu et une fin parsables.
*   **Dynamic Worldbuilding** : Mettre à jour automatiquement la fiche perso si le héros perd un bras au chapitre 4. Ici, c'est l'humain qui doit y penser.
*   **Multi-Agent Collaboration** : Faire débattre un Agent "Optimiste" et un Agent "Pessimiste" pour générer des dialogues complexes.

## CONCLUSION
Vous avez construit une très belle **Bibliothèque** (rangement), mais pas une **Usine** (production).
Pour passer à l'échelle, il faut arrêter de jouer avec l'Explorateur de Fichiers et commencer à écrire du code (Python/Typescript) qui manipule ces fichiers.

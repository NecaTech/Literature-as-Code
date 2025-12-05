# PROJECT ALPHA : LE CRASH TEST 💥

> **Statut** : LIVRE JETABLE
> **Objectif** : Faire exploser le système pour voir où sont les failles.

## 1. Le Concept
Nous avons besoin d'une histoire simple mais structurée pour tester :
1.  **La Logique** (Enquête / Mystère)
2.  **L'Émotion** (Drame / Romance)
3.  **Le Worldbuilding** (SF / Fantasy)

### Proposition de Genres pour le Test :
*   **Option A : Le Huis Clos (Agatha Christie style)**
    *   *Pourquoi ?* Teste massivement la cohérence (Continuity Tests) et les dialogues (Subtext). Peu de lieux, beaucoup d'interactions.
*   **Option B : Le Thriller Cyberpunk**
    *   *Pourquoi ?* Teste le "Show Don't Tell" (descriptions sensorielles) et l'intégration de règles complexes (World DB).
*   **Option C : L'Épopée Minimaliste**
    *   *Pourquoi ?* Un seul personnage face à la nature. Teste l'introspection (Deep POV) et le rythme.

## 2. La "Seed" (À remplir par l'utilisateur)
Pour lancer la machine, j'ai besoin d'une graine.

*   **Genre** : [A/B/C ou Autre]
*   **Protagoniste** : [Nom + 1 Adjectif]
*   **L'Incident Déclencheur** : [Quelque chose arrive...]

---

## 3. Le Workflow de Production (Comment ça va se passer ?)

Voici la boucle que nous allons exécuter pour chaque chapitre :

1.  **Architect (Toi + Moi)** : On définit le "Beat" (ex: Le héros refuse l'appel). On remplit le JSON.
2.  **Worldbuilder (Moi)** : Je vérifie si on a les fiches persos nécessaires. Si non, je les crée.
3.  **Writer (L'IA)** : Elle lit le JSON + les Fiches + le Chapitre précédent. Elle écrit.
4.  **Critic (L'IA)** : Elle passe le texte au lance-flammes (Linting Rules).
5.  **Editor (Toi)** : Tu lis le rapport. Tu dis "C'est nul ici" ou "Validé".
6.  **Commit** : On versionne dans `03_MANUSCRIPT/03_master`.

On répète 15 fois (pour les 15 beats). À la fin, on a un livre.

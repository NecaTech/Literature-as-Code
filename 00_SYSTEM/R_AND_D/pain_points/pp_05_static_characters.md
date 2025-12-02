# R&D BUG REPORT: PP-05

## 🐛 Bug: Static Characters (Le Problème des Personnages Statiques)

**Severity**: HIGH
**Status**: OPEN
**Component**: Character Engine

### Description
Le personnage reste identique du début à la fin. Son "Prompt" psychologique est statique. Il traverse les épreuves sans être fondamentalement changé par elles.

### 🔍 Symptômes
- **Pas d'Arc d'Évolution** : Le héros à la fin du livre est le même qu'au début, juste plus fatigué.
- **Invulnérabilité Psychologique** : Les traumatismes ne laissent pas de traces durables qui modifient le comportement.
- **Absence de "Wound" (Blessure)** : Le personnage n'a pas de faille fondamentale qu'il doit réparer pour gagner.

### 🗣️ Verdict du Critique
> "Ce sont des figurines en plastique. Tu peux les tordre, les jeter contre un mur, elles reprennent toujours leur forme initiale. Un vrai personnage doit se briser et se reconstruire différemment."

### 🎯 Objectif Technique
**Définir le triptyque Ghost / Lie / Wound.**
Pour chaque personnage principal, nous devons coder :
1.  **Ghost** : Un événement traumatique du passé qui le hante.
2.  **Lie** : Le mensonge qu'il se raconte pour survivre (ex: "Je n'ai besoin de personne").
3.  **Truth** : La vérité qu'il doit accepter pour évoluer (ex: "La force vient de l'union").
L'histoire est le processus douloureux de passer du Lie à la Truth.

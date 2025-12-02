# R&D BUG REPORT: PP-04

## 🐛 Bug: Flatline Structure (Le Problème de l'Encéphalogramme Plat)

**Severity**: CRITICAL
**Status**: OPEN
**Component**: Narrative Architecture

### Description
L'IA traite les chapitres comme une liste linéaire de tâches à accomplir (To-Do List) au lieu de construire une courbe de tension dramatique. Le récit avance, mais ne monte pas en puissance.

### 🔍 Symptômes
- **Absence de Pacing** : L'intensité dramatique est constante (toujours moyenne), sans pics (Climax) ni vallées (Moments de calme).
- **Manque de Moments Clés** : Les points de bascule structurels (Inciting Incident, Midpoint, All is Lost) sont souvent traités comme des événements banals.
- **Linéarité Monotone** : "Et ensuite il se passe ça, et ensuite ça..." au lieu de "À cause de ça, il se passe ça, MAIS..."

### 🗣️ Verdict du Critique
> "C'est une suite d'événements, pas une histoire. On dirait un rapport de police : précis, factuel, et totalement chiant. Où est le danger ? Où est le moment où tout bascule ?"

### 🎯 Objectif Technique
**Implémenter une structure rigide (ex: Save The Cat).**
Nous ne pouvons pas laisser l'IA improviser la structure. Il faut lui imposer un squelette externe :
- Acte 1 (Thèse)
- Acte 2 (Antithèse)
- Acte 3 (Synthèse)
Chaque chapitre doit avoir une fonction précise dans cet arc (ex: "Ceci est le Midpoint, tout doit changer ici").

# R&D BUG REPORT: PP-01

## 🐛 Bug: Regression to the Mean (Le Problème de la Moyenne)

**Severity**: CRITICAL
**Status**: OPEN
**Component**: Prose Generation Engine

### Description
L'IA converge statistiquement vers la tournure de phrase la plus probable, résultant en un "Style Beige". Le texte est grammaticalement parfait mais stylistiquement mort.

### 🔍 Symptômes
- **Absence de violence linguistique** : Les phrases ne "mordent" pas.
- **Métaphores attendues** : Utilisation de clichés (ex: "un silence de mort", "des yeux perçants").
- **Rythme lisse** : Les phrases ont tendance à avoir une longueur et une structure uniformes.
- **Vocabulaire consensuel** : Évitement des mots rares, archaïques ou argotiques qui donneraient de la saveur.

### 🗣️ Verdict du Critique
> "Pornographie de la compétence. C'est inodore. On dirait un manuel scolaire écrit par un premier de la classe qui a peur de se salir."

### 🎯 Objectif Technique
**Forcer une "Entropie Stylistique".**
Nous devons trouver un moyen de contraindre le modèle à choisir des tokens *moins* probables mais *plus* percutants. Il faut introduire une mesure de "température locale" ou un système de pénalité pour les tournures trop communes.

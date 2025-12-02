# R&D BUG REPORT: PP-TECH-01

## 🐛 Bug: Context Isolation (Erreur 404 Binding)

**Severity**: CRITICAL
**Status**: OPEN
**Component**: Context Management System

### Description
L'Agent Rédacteur travaille en "aveugle". Lorsqu'il rédige le Chapitre X, il n'a pas automatiquement accès à :
1.  L'état émotionnel du héros à la fin du Chapitre X-1.
2.  La description physique du lieu où se déroule la scène (stockée dans `01_CONTEXT_DB`).
3.  La fiche des personnages secondaires présents dans la scène.

### 🔍 Symptômes
- **Hallucinations de Continuité** : Un personnage blessé au chapitre précédent est soudainement en pleine forme.
- **Décors Flous** : Les lieux sont décrits de manière générique, ignorant les détails spécifiques définis dans le Worldbuilding.
- **Incohérence des Relations** : L'IA oublie qu'un personnage est censé être en froid avec un autre.

### 🎯 Solution Technique : "Context Injector"
Implémenter un protocole d'**Injection de Dépendances Explicite**.
Chaque fichier de spécification de chapitre (`chapter_spec`) doit contenir un Header YAML déclarant ses besoins en données.
L'IDE (ou l'humain) doit "charger" ces fichiers dans la mémoire de l'IA *avant* de lancer la génération du texte.

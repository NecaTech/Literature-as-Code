# R&D BUG REPORT: PP-02

## 🐛 Bug: Zero Subtext Syndrome (Le Syndrome du Zéro Sous-Texte)

**Severity**: CRITICAL
**Status**: OPEN
**Component**: Dialogue & Character Logic

### Description
Les personnages expriment littéralement leurs pensées et émotions (Exposition Verbale). Il n'y a pas de décalage entre l'état interne et la parole externe.

### 🔍 Symptômes
- **Dialogues fonctionnels** : Les personnages disent exactement ce qu'ils veulent dire ("Je suis en colère contre toi").
- **Absence de non-dit** : Tout est explicité, rien n'est laissé à l'interprétation du lecteur.
- **Psychologie de surface** : Les interactions manquent de profondeur et de tension latente.

### 🗣️ Verdict du Critique
> "Psychopathes fonctionnels. On sent les fiches personnages à chaque réplique. Personne ne parle comme ça dans la vraie vie."

### 🎯 Objectif Technique
**Implémenter une couche de "Masque Social".**
Le système doit générer deux flux pour chaque interaction :
1.  **Pensée (Interne)** : Ce que le personnage pense vraiment (A).
2.  **Parole (Externe)** : Ce que le personnage dit effectivement (B), filtré par ses peurs, ses objectifs sociaux et le contexte.
L'écart entre A et B crée le sous-texte.

MY_NOVEL_PROJECT/
├── 00_SYSTEM/                     # [CONFIG] Configuration de l'environnement (System & Meta)
│   ├── R_AND_D/                   # [LAB] Recherche & Développement
│   │   └── pain_points/           # [BUGS] Rapports de défauts IA identifiés
│   │       ├── pp_01_regression_to_mean.md
│   │       ├── pp_02_zero_subtext_syndrome.md
│   │       ├── pp_03_sterile_efficiency.md
│   │       ├── pp_04_flatline_structure.md
│   │       ├── pp_05_static_characters.md
│   │       └── pp_06_missing_controlling_idea.md
│   ├── prompts/                   # System Prompts pour les Agents (Personas)
│   │   ├── agent_architect.md     # Expert en structure
│   │   ├── agent_writer.md        # Expert en prose
│   │   └── agent_critic.md        # Expert en QA (Quality Assurance)
│   └── templates/                 # [SCAFFOLDING] Modèles de fichiers réutilisables
│       ├── tpl_character.md
│       ├── tpl_location.md
│       └── tpl_chapter_spec.md
│
├── 00_INBOX/                      # [BACKLOG] Idées brutes et tickets non triés
│   ├── assets/                    # Images de référence, moodboards, cartes
│   └── raw_notes.md               # Dump d'idées en vrac
│
├── 01_CONTEXT_DB/                 # [DATABASE] La "Source de Vérité" (Read-Only pour le writer)
│   ├── characters/                # Tables des personnages
│   ├── world/                     # Tables de l'univers (Lieux, Magie, Tech, Factions)
│   └── glossary.md                # Dictionnaire de données (Termes spécifiques)
│
├── 02_ARCHITECTURE/               # [BLUEPRINT] Architecture Narrative (Renamed from SPECS)
│   ├── global_story_map.md        # La "Beat Sheet" complète (15 beats)
│   ├── act_1_thesis/              # ACTE I : Thèse (Le Monde Ordinaire)
│   │   ├── ch01_setup.md
│   │   └── ...
│   ├── act_2a_antithesis/         # ACTE IIa : Antithèse (Le Monde Inversé - Fun & Games)
│   │   └── ...
│   ├── act_2b_bad_guys/           # ACTE IIb : La Descente (All is Lost)
│   │   └── ...
│   ├── act_3_synthesis/           # ACTE III : Synthèse (Le Final)
│       └── ...
│
├── 03_SOURCE/                     # [SRC] Le code source narratif
│   ├── 01_drafts/                 # Branches de développement (brouillons, feature branches)
│   ├── 02_staging/                # Environnement de pré-production (après review, avant validation finale)
│   └── 03_master/                 # Environnement de production (Golden Master)
│
├── 04_TEST_SUITE/                 # [QA] Tests et Validation
│   ├── linting_rules/             # Règles de style (Linter : pas de passif, show don't tell)
│   ├── continuity_tests/          # Vérification de la logique temporelle et spatiale
│   └── unit_tests/                # Tests spécifiques par chapitre (Checklist de validation)
│
└── 05_BUILD/                      # [DIST] Artefacts compilés et Logs
    ├── logs/                      # Rapports de critique et Changelog
    └── exports/                   # EPUB, PDF, DOCX générés (Build artifacts)
# Show, Don't Tell (Montrer, ne pas dire)

## Principe
C'est la règle d'or de la fiction immersive. Au lieu d'informer le lecteur d'un état (émotion, météo, trait de caractère), il faut lui faire *ressentir* via des preuves sensorielles.

## Pourquoi c'est crucial pour l'IA
Les LLM ont tendance à "résumer" l'action (Mode "Tell") par souci d'efficacité. Il faut forcer le "Mode Show" pour créer de l'immersion.

## Exemples

| Tell (Interdit) | Show (Recommandé) |
| :--- | :--- |
| "Il était nerveux." | "Il essuyait ses mains moites sur son pantalon toutes les trente secondes." |
| "Il faisait froid." | "La buée sortait de sa bouche à chaque respiration, et le givre craquait sous ses bottes." |
| "Elle était en colère." | "Elle posa sa tasse de café. Trop fort. La porcelaine tinta violemment contre la soucoupe." |

## Implémentation Technique
- **Interdiction des adjectifs d'état** : Bannir "triste", "heureux", "effrayé" des descriptions.
- **Focus Sensoriel** : Utiliser au moins 2 sens par paragraphe (Vue + Son, ou Toucher + Odorat).

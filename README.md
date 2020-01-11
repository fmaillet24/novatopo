# Test technique - Back side

## Énoncé

L'objectif de ce test sera de créer une api web, côté serveur, ressemblant à ce qu'on peut faire chez Novatopo. Les besoins sont les suivants:

- En tant qu'utilisateur, je souhaite pouvoir récupérer la liste des activités et businesses
- En tant qu'utilisateur, je souhaite pouvoir réserver une activité
- En tant qu'utilisateur, je souhaite pouvoir ajouter/supprimer/modifier une activité
- En tant qu'utilisateur, je souhaite pouvoir ajouter/supprimer/modifier un business
- Bonus: reprendre le second et le troisième point et le faire en tant que staff Novatopo

N'hésitez pas à aller au plus simple tout en notant vos interrogations rencontrées pendant le projet

## Conditions

1. Vous devez utiliser [Django](https://www.djangoproject.com/) en tant que framework web
2. Vous devez utiliser [graphene](https://docs.graphene-python.org/projects/django/en/latest/) pour créer l'api

Vous être libre pour la création de la base de données. Vous êtes libre d'ajouter autant de librairies utilitaires que vous le souhaitez dans votre projet si vous en ressentez le besoin.

Le projet devra être hébergé dans un dépôt public, sur Github/Gitlab, afin d'être évalué. Nous vous encourageons à versionner votre projet en faisant plusieurs commits, cela nous permettra de comprendre votre raisonnement et la façon dont vous avez approché le problème. De plus, cet énoncé devra figurer dans la racine du projet.

## Petit coup de main

1. Activité: c'est le coeur de métier Novatopo, une activité qu'on peut réserver. Example: une séance d'escalade, de karting, etc.
2. Business: c'est l'établissement professionnel chez qui l'usager réserve son activité. Example: Arkose ou Antrebloc pour l'escalade, etc.
3. Chaque business peut avoir plusieurs activités.

## Notation

Vous serez noté sur la qualité, la beauté et la simplicité de votre code. Nous vous encourageons à utiliser les dernières versions des langages et des librairies que vous utiliserez dans le projet.

De plus, vous serez noté sur l'architecture de votre solution.

Si vous avez la moindre question, n'hésitez pas à nous contacter par mail _(mehdi@novatopo.com)_ ou par téléphone. Good luck 😉


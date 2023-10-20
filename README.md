# solver_tusmo - Version 1.0

Le solver_tusmo est un programme, codé en Python, conçu pour aider à résoudre le Tusmo en français, il se base sur calcul de la quantité d'information contenue dans les mots. Il fonctionne en utilisant une liste de mots de la langue française (mise à jour en 2022) stockée dans un fichier nommé "liste_fr.txt".

## Installation

Clonez ce dépôt ou téléchargez le code source.

```shell
git clone https://github.com/RAVAO-Ravo/solver_tusmo_fun.git
```

Pour installer les dépendances requises pour ce projet, vous pouvez utiliser `pip3`. Assurez-vous d'être dans le répertoire du projet où se trouve le fichier `requirements.txt`, puis exécutez la commande suivante :

```bash
pip3 install -r requirements.txt
```

## Comment ça marche

1. **Lancement du programme :** Pour utiliser le résolveur, exécutez le programme dans un terminal de commandes :

	```shell
	python3 solver_tusmo.py
	```

2. **Entrée de l'utilisateur :** Une fois le programme lancé, vous devrez fournir deux informations essentielles :
   - La première lettre du mot à chercher.
   - La longueur souhaitée du mot.

3. **Calcul de la quantité d'information :** Le programme utilisera les fréquences des lettres dans la langue pour calculer la quantité d'information de chaque mot du fichier. La quantité d'information est basée sur la diversité des lettres dans le mot et la fréquence de ces lettres dans la langue.

4. **Mot suggéré :** Le programme renverra le mot ayant la plus grande quantité d'information, tout en respectant la première lettre et la longueur souhaitée. Ce mot est suggéré à l'utilisateur.

5. **Validation du mot :** Vous pouvez tester le mot suggéré par le programme. Si le mot est correct, vous pouvez terminer le programme. Sinon, passez à l'étape suivante.

6. **Affinement de la recherche :** Si le mot suggéré n'est pas correct, fournissez au programme des informations supplémentaires :
   - Lettres "noires" : Indiquez les lettres qui ne sont pas dans le mot.
   - Lettres "rouges" : Indiquez les lettres qui sont dans le mot et à la bonne position.
   - Lettres "jaunes" : Indiquez les lettres qui sont dans le mot, mais à la mauvaise position.

7. **Raffinement de la recherche :** Le programme utilisera ces informations pour affiner sa recherche. Il essaiera de trouver un mot correspondant aux critères spécifiés. Le processus se répétera jusqu'à ce que le mot soit trouvé.

8. **Fin du programme :** Le programme se termine lorsqu'un mot (ou aucun mot) correspondant aux critères est trouvé. Vous avez réussi à résoudre le mot !

Voici la partie de votre README avec le logo de la licence CC BY-NC 4.0 :

## Licence

Ce projet est sous licence Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). Vous êtes libre de :

- Partager : copier et redistribuer le matériel sous quelque support que ce soit ou sous n'importe quel format.
- Adapter : remixer, transformer et créer à partir du matériel.

Selon les conditions suivantes :

- Attribution : Vous devez donner le crédit approprié, fournir un lien vers la licence et indiquer si des modifications ont été apportées. Vous devez le faire de la manière suggérée par l'auteur, mais pas d'une manière qui suggère qu'il vous soutient ou soutient votre utilisation du matériel.

- Utilisation non commerciale : Vous ne pouvez pas utiliser le matériel à des fins commerciales.

[![Logo CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc/4.0/)

[En savoir plus sur la licence CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

#!/bin/python3
#-*- coding:utf-8 -*-

# Auteur : RAVAOZAFINDRASOA Ravo
# Version : 1.0

# Importation des modèles
import unidecode
from typing import List, Dict, Tuple, Union

# Variables globales
LETTER_WEIGHT: Dict[str, float] = {'a' : 0.0711,
								   'b' : 0.0114,
								   'c' : 0.0318,
								   'd' : 0.0367,
								   'e' : 0.1210,
								   'f' : 0.0111,
								   'g' : 0.0123,
								   'h' : 0.0111,
								   'i' : 0.0659,
								   'j' : 0.0034,
								   'k' : 0.0029,
								   'l' : 0.0456,
								   'm' : 0.0262,
								   'n' : 0.0639,
								   'o' : 0.0502,
								   'p' : 0.0249,
								   'q' : 0.0065,
								   'r' : 0.0607,
								   's' : 0.0651,
								   't' : 0.0592,
								   'u' : 0.0449,
								   'v' : 0.0111,
								   'w' : 0.0017,
								   'x' : 0.0038,
								   'y' : 0.0046,
								   'z' : 0.0015}

FILE_WORDS: str = "liste_fr.txt"


def read_file(file_name: str) -> List[str]:
	"""
	Lit un fichier texte et renvoie son contenu sous forme de liste de mots.

	Args:
		file_name (str): Le nom du fichier texte à lire.

	Returns:
		List[str]: Une liste de mots du fichier, en minuscules et sans accents.
	"""
	
	# Initialisation de la future liste
	words_list = []

	# Ouverture du fichier en mode lecture avec encodage UTF-8
	with open(file=file_name, mode='r', encoding="utf8") as fichier:
		# Récupérer les lignes du fichier
		lines = fichier.readlines()

		# Parcourir chaque ligne du fichier
		for line in lines:
			# Diviser la ligne en mots et les convertir en minuscules sans accents
			words = [unidecode.unidecode(mot.lower()) for mot in line.split()]
			
			# Ajouter les mots à la liste des mots
			words_list.extend(words)

	return words_list


def unique_elements(input_list: List[str]) -> List[str]:
	"""
	Renvoie une liste contenant les éléments uniques de la liste d'entrée.

	Args:
		input_list (List[str]): La liste d'éléments d'entrée.

	Returns:
		List[str]: Une nouvelle liste contenant uniquement les éléments uniques.
	"""
	
	# Utilisation d'un ensemble (set) pour éliminer les doublons, puis conversion en liste    
	return list(set(input_list))


def compute_info(word: str) -> float:
	"""
	Calcule la quantité d'informations contenue dans un mot.

	Args:
		word (str): Le mot pour lequel la quantité d'informations doit être calculée.

	Returns:
		float: La quantité d'informations du mot.
	"""

	# Utilisation d'une expression génératrice pour calculer la somme des valeurs des lettres
	return sum(unique_elements([LETTER_WEIGHT[letter] for letter in word if letter in LETTER_WEIGHT.keys()]))


def get_FirstWord(start_letter: str, len_word: int) -> Tuple[str, List[Tuple[str, float]]]:
	"""
	Trouve le meilleur premier mot commençant par une lettre donnée et ayant une longueur spécifique, 
	puis renvoie ce mot et la liste triée de tous les mots correspondants avec leurs quantités d'informations.

	Args:
		start_letter (str): La lettre de début souhaitée.
		len_word (int): La longueur souhaitée du mot.

	Returns:
		Tuple[str, List[Tuple[str, float]]]: Un tuple contenant le premier mot correspondant et la liste triée 
		de tous les mots correspondants avec leurs quantités d'informations.
	"""
	
	# Lire le fichier des mots et calculer les quantités d'informations pour chaque mot
	words_info = [(word, compute_info(word)) for word in read_file(file_name=FILE_WORDS) if (word[0] == start_letter) and (len(word) == len_word)]

	# Trier la liste des mots en fonction de leurs quantités d'informations (du plus élevé au plus bas)
	words_info = sorted(words_info, key=lambda x: x[1], reverse=True)

	if words_info:
		# Si des mots correspondent aux critères, renvoyer le premier mot et la liste triée de tous les mots correspondants
		return (words_info[0][0], words_info)
	else:
		# Si aucun mot ne correspond aux critères, renvoyer une liste vide
		return ("Aucun mot trouvé", [])


def get_ListTuples(tup: bool = True) -> List[Union[Tuple[str, int], str]]:
	"""
	Demande à l'utilisateur de saisir une liste de tuples ou de lettres et renvoie la liste analysée.

	Args:
		tup (bool, optional): Indique si l'utilisateur doit saisir des tuples (True) ou des chaînes de caractères (False).
			Par défaut, la saisie de tuples est activée.

	Returns:
		List[Union[Tuple[str, int], str]]: Une liste de tuples ou de lettres extraits de l'entrée utilisateur.
	"""
	res = []
	
	n_loops = int(input("Entrez le nombre d'éléments : "))

	for i in range(1, n_loops + 1):
		if tup:
			# Demander à l'utilisateur de saisir une lettre et une position sous forme de tuple
			letter_input = str(input(f"Entrez la lettre {i} : "))
			pos_input = int(input(f"Entrez la position de la lettre {letter_input} : "))
			res.append((letter_input, pos_input-1))
		else:
			# Demander à l'utilisateur de saisir une lettre
			letter_input = str(input(f"Entrez la lettre {i} : "))
			res.append(letter_input)

	return res


class Tusmo:
	def __init__(self, first_word: str, words_info: List[Tuple[str, float]]) -> None:
		"""
		Initialise un objet Tusmo avec un mot initial et une liste de mots avec leurs quantités d'informations.

		Args:
			first_word (str): Le premier mot, qui servira comme point de départ.
			words_info (List[Tuple[str, float]]): Une liste de mots avec leurs quantités d'informations.
				Chaque élément de la liste est un tuple contenant un mot et sa quantité d'informations associée.
		"""
		self.best_word = first_word  # Attribut pour stocker le meilleur mot actuel.
		self.words_info = words_info  # Attribut pour stocker la liste de mots et leurs quantités d'informations.
		self.not_list: List[Union[str, Tuple[str, int]]] = []  # Attribut pour stocker une liste de lettres ou de tuples.
		self.red_list: List[Tuple[str, int]] = []  # Attribut pour stocker une liste de lettres associées à des positions.
		self.ylw_list: List[Tuple[str, int]] = []  # Attribut pour stocker une liste de lettres jaunes dans les mots.

	def update_not_list(self) -> None:
		"""
		Met à jour la liste des lettres non présentes dans les mots, si l'utilisateur le souhaite.
		"""
		# Demande à l'utilisateur s'il souhaite mettre à jour la liste des lettres non présentes
		choice = input("\nVoulez-vous mettre à jour les lettres non présentes (o/n) ? ").strip().lower()
		
		# Si l'utilisateur choisit "o" (oui), met à jour la liste des lettres non présentes
		if choice == 'o':
			self.not_list = get_ListTuples(tup=False)
		else:
			# Sinon, réinitialise la liste des lettres non présentes à une liste vide
			self.not_list = []

	def update_red_list(self) -> None:
		"""
		Met à jour la liste des lettres rouges, si l'utilisateur le souhaite.
		"""
		# Demande à l'utilisateur s'il souhaite mettre à jour la liste des lettres rouges
		choice = input("\nVoulez-vous mettre à jour les lettres rouges (o/n) ? ").strip().lower()
		
		# Si l'utilisateur choisit "o" (oui), met à jour la liste des lettres rouges
		if choice == 'o':
			self.red_list = get_ListTuples(tup=True)
		else:
			# Sinon, réinitialise la liste des lettres rouges à une liste vide
			self.red_list = []

	def update_ylw_list(self) -> None:
		"""
		Met à jour la liste des lettres jaunes dans le mot, si l'utilisateur le souhaite.
		"""
		# Demande à l'utilisateur s'il souhaite mettre à jour la liste des lettres jaunes dans le mot
		choice = input("\nVoulez-vous mettre à jour les lettres jaunes dans le mot (o/n) ? ").strip().lower()
		
		# Si l'utilisateur choisit "o" (oui), met à jour la liste des lettres jaunes dans le mot
		if choice == 'o':
			self.ylw_list = get_ListTuples(tup=True)
		else:
			# Sinon, réinitialise la liste des lettres jaunes dans le mot à une liste vide
			self.ylw_list = []


	def update_(self) -> None:
		"""
		Met à jour le meilleur mot en fonction des règles spécifiées par l'utilisateur.
		"""
		# Crée une nouvelle liste de tuples pour stocker les mots filtrés et leurs quantités d'informations
		new_words_info: List[Tuple[str, float]] = []

		# Met à jour les listes des lettres non présentes, rouges et jaunes en fonction des choix de l'utilisateur
		self.update_not_list()
		self.update_red_list()
		self.update_ylw_list()

		# Initialise la nouvelle liste avec les mots actuels
		new_words_info = [word for word, _ in self.words_info]

		# Filtre les mots qui contiennent des lettres de la liste not_list, si not_list n'est pas vide
		if self.not_list:
			new_words_info = [word for word in new_words_info if all(letter not in word for letter in self.not_list)]

		# Filtre les mots qui ne correspondent pas aux lettres rouges, si red_list n'est pas vide
		if self.red_list:
			new_words_info = [word for word in new_words_info if all(word[pos] == letter for letter, pos in self.red_list)]

		# Filtre les mots qui ne correspondent pas aux lettres jaunes, si ylw_list n'est pas vide
		if self.ylw_list:
			new_words_info = [word for word in new_words_info if all((word[pos] != letter) and (letter in word) for letter, pos in self.ylw_list)]

		# Calcule les quantités d'informations pour les mots restants
		new_words_info = [(word, compute_info(word)) for word in new_words_info]

		# Trie la liste des mots en fonction de leurs quantités d'informations (du plus élevé au plus bas)
		self.words_info = sorted(new_words_info, key=lambda x: x[1], reverse=True)

		# Met à jour le meilleur mot avec le premier mot de la liste triée
		self.best_word = self.words_info[0][0]


if __name__ == "__main__":

	# Demande à l'utilisateur de choisir une lettre de départ et la taille du mot souhaitée.
	start_letter = str(input("Choisir la lettre de départ : "))
	len_word = int(input("Choisir la taille du mot : "))

	# Trouve le meilleur premier mot en fonction des choix de l'utilisateur.
	first_word, words_info = get_FirstWord(start_letter=start_letter, len_word=len_word)
	
	# Crée un objet de la classe Tusmo pour résoudre le problème.
	solver = Tusmo(first_word=first_word, words_info=words_info)

	# Affiche le meilleur premier mot.
	print(f"\nLe meilleur premier mot est : {solver.best_word}")

	while True:
		# Demande à l'utilisateur si le mot a été trouvé.
		finish = True if input("\nLe mot a-t-il été trouvé (o/n) ? ") == 'o' else False
		if finish == True:
			break

		# Met à jour le mot à utiliser en fonction des règles spécifiées par l'utilisateur.
		solver.update_()
		print(f"\nLe meilleur mot à utiliser est : {solver.best_word}")
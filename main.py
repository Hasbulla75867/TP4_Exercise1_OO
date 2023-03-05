"""
Programme fait par Raul Mic Nicolas
TP4 : Introduction à la programmation OO
Écrire une classe StringFoo qui contient:
  a) un attribut message;
  b) une méthode set_string qui accepte une string en paramètre et la sauvegarde dans l'attribut message.
  c) une méthode print_string qui affiche le contenu de l'attribut message tout en majuscule.

"""


class StringFoo:
    message = input("Entrez le message à afficher: ")

    def set_string(self, message):
        self.message = message

    def print_string(self):
        print("Le message en majuscule est : ", self.message.upper())


string = StringFoo()
string.set_string(string.message)
string.print_string()

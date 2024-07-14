import time
import limpar


pets = []
class Pet:
  def __init__(self, name, raça):
    self.name = name
    self.raça = raça


def add_pet(name, raça):
  pets.append(Pet(name, raça))

def print_pets():
  if len(pets) == 0:
    print("Não há pets cadastrados.")

  else:
    i = 1 
    for pet in pets:
      print(f"{i}º - {pet.name} - {pet.raça}")
      i += 1
  
def inputname():
  name = input("Nome do pet: ")
  return name
  
def inputraça():
  raça = input("Raça do pet: ")
  return raça
  
def main():
  while True:
    limpar.limparConsole()
    print("1 - Adicionar pet")
    print("2 - Listar pets")
    print("3 - Sair")
    choice = input("Escolha uma opção: ")
    
    if choice == "1":
      limpar.limparConsole()
      name = inputname()
      while True:
        if name == "":
          print("Nome inválido")
          name = inputname()
        else:
          break
          
      raça = inputraça()
      while True:
        if raça == "":
          print("Raça inválida")
          raça = inputraça()
        else:
          break
          
      add_pet(name, raça)
      
      if name and raça != "":
        print("Pet adicionado com sucesso!")
        time.sleep(3)
    elif choice == "2":
      limpar.limparConsole()
      print_pets()
      time.sleep(3)
    elif choice == "3":
      limpar.limparConsole()
      print("Tchau. Até mais!")
      time.sleep(2)
      break
    else:
      limpar.limparConsole()
      print("Opção inválida")
      time.sleep(2)

if __name__ == "__main__":
  main()


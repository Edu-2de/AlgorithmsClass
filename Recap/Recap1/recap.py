cars = [["Ford", 2020, "F150"], ["Chevrolet", 2019, "Silverado"], ["Ram", 2021, "1500"]]


while True:
      try:
            print("\n -------------Menu de opções: -------------\n")
            print(
            "1. cadastrar\n"
            "2. listar\n"
            "3. buscar\n"
            "4. sair"
                  )
            option = input("Digite a opcao: ")
            if not option.isdigit():
                  print("Opção inválida. Por favor, digite um número.")
                  continue
       
            option = int(option)

            if option == 4:
                  print("Saindo do programa.")
                  break
            elif option == 2:
                  print("Listando todos os carros:")
                  for car in cars:
                        print(f"{car[0]} {car[1]} {car[2]}")
                  continue
            elif option == 3:
                  try:
                        carname = input("Digite o nome do carro: ")
                        found = False
                        for car in cars:
                              for item in car:
                                    if carname.lower() in str(item).lower():
                                          print(f"Carro encontrado: {car[0]} {car[1]} {car[2]}")
                                          found = True
                                          break
                              if found:
                                    break
                        if not found:
                              print("Carro não encontrado.")
                  except ValueError:
                        print("Entrada inválida. Tente novamente.")
      except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue

     
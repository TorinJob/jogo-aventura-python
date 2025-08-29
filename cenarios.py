from mensagens import vitoria, fim_de_jogo


def caminho_da_esquerda():
    print("\nVocê segue pelo caminho da esquerda e chega a uma sala com um absimo enorme")
    
    print("A escuridão impede de ver o fundo.")

    escolha = input("Você tenta 'pular' o absimo ou 'procurar' por outra passagem?").lower().strip()
        
    if escolha == "procurar":
        print("\nVocê")
        print("Você atravessa com cuidado e chega a uma sala cheia de ouro e joias!")
        vitoria()
    elif escolha == "Pular":
        fim_de_jogo("Você tenta pular, mas o abismo é largo demais. Você cai na escuridão...")
    else:
        fim_de_jogo("Opção inválida! Indeciso, você tropeça e cai no abismo.")

def caminho_da_direita():
    print("\nVocê vira à direita e entra numa câmara silenciosa.")
    print("No centro, um morcego gigante dorme profundamente.")
    
    escolha = input("Você tenta 'atacar' o morcego ou 'passar em silêncio'? ").lower().strip()
    
    if escolha == "passar em silêncio":
        print("\nCom muito cuidado, você passa pelo morcego sem acordá-lo.")
        print("Logo à frente, você encontra a sala do tesouro!")
        vitoria()
    elif escolha == "atacar":
        fim_de_jogo("Má ideia! O morcego acorda furioso e não lhe dá chance de defesa.")
    else:
        fim_de_jogo("Opção inválida! Seu barulho acorda o morcego.")


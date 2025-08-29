# jogo.py

from cenarios import caminho_da_esquerda, caminho_da_direita
from mensagens import fim_de_jogo 
def iniciar_jogo():
    """Função principal que controla o fluxo do jogo"""
    print("-=--=--=--=--=--=--=--=--=--=--=--=-")
    print("-=- Bem vindo à Caverna do Eco perdido! -=-") 
    print("-=--=--=--=--=--=--=--=--=--=--=--=-")
    print("\nVocê está na entrada de uma caverna escura e misteriosa.")
    print("Dizem que um grande tesouro está escondido aqui.")
    print("Você vê dois caminhos à sua frente.")
    
    escolha1 = input("Você vai para a 'esquerda' ou 'direita'? ").lower().strip()

    
    if escolha1 == "esquerda":
        caminho_da_esquerda()
    elif escolha1 == "direita":
        caminho_da_direita()
    else:
        fim_de_jogo("Opção inválida! O eco da sua voz confusa te assusta e a caverna desmorona.")



if __name__ == "__main__":
    iniciar_jogo()
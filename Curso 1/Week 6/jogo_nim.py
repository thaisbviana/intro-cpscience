def informa_estado_do_tabuleiro(n):

    if n==1:
        
        print("Agora resta apenas uma peça no tabuleiro.")

    elif(n==0):
            
        print("Fim do jogo! O computador ganhou!")
                
    else:
            
        print(f"Agora restam {n} peças no tabuleiro.")


def computador_escolhe_jogada(n, m):
    
    if n>0:

        pecas_removidas_na_rodada=1
                
        while pecas_removidas_na_rodada<m and (n-pecas_removidas_na_rodada)%(m+1)!=0:
            pecas_removidas_na_rodada+=1

        return pecas_removidas_na_rodada


def informa_jogada_do_computador(pecas_removidas_na_rodada):

    if pecas_removidas_na_rodada==1:
            
        print("O computador tirou uma peça.")
            
    else:
            
        print(f"O computador tirou {pecas_removidas_na_rodada} peças.")


def usuario_escolhe_jogada(n,m):

    if n>0 and m>0 and m<=n:
        
        pecas_removidas_na_rodada=int(input("Quantas peças você vai tirar?"))
                                  
        if pecas_removidas_na_rodada>=1 and pecas_removidas_na_rodada<=m and pecas_removidas_na_rodada<=n:

            return pecas_removidas_na_rodada
    
        else:
            
            print("Oops! Jogada inválida! Tente de novo.")
            
            usuario_escolhe_jogada(n,m,pecas_removidas_na_rodada)


def informa_jogada_do_usuario(pecas_removidas_na_rodada):

    if pecas_removidas_na_rodada==1:
                                      
        print("Você tirou uma peça.")
                                      
    else:
                    
        print(f"Voce tirou {pecas_removidas_na_rodada} peças.")

    
def partida():

    pecas_removidas_na_rodada=1
    n=int(input("Forneça o número inicial de peças no tabuleiro: "))
    m=int(input("Forneça o número máximo de peças que podem ser retiradas por jogada: "))

    if n>0 and m>0 and n>=m:
		
        if n%(m+1)==0:

            print("Você começa!")

            while n>0:

                pecas_removidas_na_rodada = usuario_escolhe_jogada(n,m)
                n -= pecas_removidas_na_rodada
                informa_jogada_do_usuario(pecas_removidas_na_rodada)
                informa_estado_do_tabuleiro(n)
            
                if n>0:
                
                    pecas_removidas_na_rodada = computador_escolhe_jogada(n, m)
                    n -= pecas_removidas_na_rodada
                    informa_jogada_do_computador(pecas_removidas_na_rodada)
                    informa_estado_do_tabuleiro(n)

        else:

            print("Computador começa!")
        
            while n>0:

                pecas_removidas_na_rodada = computador_escolhe_jogada(n, m)
                n -= pecas_removidas_na_rodada
                informa_jogada_do_computador(pecas_removidas_na_rodada)
                informa_estado_do_tabuleiro(n)

                if n>0:
                
                    pecas_removidas_na_rodada = usuario_escolhe_jogada(n,m)
                    n -= pecas_removidas_na_rodada
                    informa_jogada_do_usuario(pecas_removidas_na_rodada)
                    informa_estado_do_tabuleiro(n)
                    
    else:
        print("Oops! Valor inválido! Tente de novo.")
        partida()


def main():

    modo_de_jogo=1

    modo_de_jogo=input("Bem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada.\n2 - para jogar um campeonato.\n")
    
    if modo_de_jogo=="1":

        print("Voce escolheu uma partida isolada!")
        partida()

    elif modo_de_jogo=="2":

        print("Voce escolheu um campeonato!")

        for rodada in range(1, 4, 1):

            print(f"\n**** Rodada {rodada} ****\n\n")
            partida()
        print("\n**** Final do campeonato! ****\n\nPlacar: Você 0 X 3 Computador")

    else:
        print("Selecione um modo de jogo válido.")
        main()


main()

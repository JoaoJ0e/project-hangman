import random
from time import sleep


# Listagem dos temas disponíveis (ler txt tava dando muito problema)
comidas = ["pizza", "hamburguer", "sushi", "macarrao", "churrasco", "lasanha", "salada", "sanduiche", "taco", "empadao", "prensadao", "xcalota", "tapioca", "crepe", "panqueca", "miojo", "pao", "sorvete", "chocolate", "frutas", "queijo", "strogonoff", "sopa", "tortilla", "waffle", "yakissoba", "espaguete", "croissant", "baguete", "pastel"]
esportes = ["futebol","basquete","tenis","natacao","atletismo","volei","handebol","boxe","judo","carate","ciclismo","surfe","skate","badminton","esgrima","hoquei","rugbi","golfe","remo","canoagem","patinacao","bilhar","escalada","triatlo"]
verbos = ["correr", "falar", "comer", "beber", "escrever", "cantar", "dançar", "ler", "pular", "estudar", "trabalhar", "viajar", "aprender", "ensinar", "conhecer", "assistir", "brincar", "jogar", "cozinhar", "descansar", "acordar", "dormir", "caminhar", "sorrir", "chorar", "nadar", "voar", "saltar", "escalar", "mexer", "tocar", "abrir", "fechar", "corrigir", "correr", "comprar", "vender", "sair", "entrar", "voltar", "partir", "chegar", "esperar", "esquecer", "lembrar", "pensar", "sonhar", "morrer", "viver", "amar", "odiar", "sofrer", "saber", "conhecer", "querer", "precisar", "buscar", "encontrar", "assistir", "torcer", "torrar", "tossir", "trabalhar", "trair", "tomar", "tirar", "tecer", "superar", "subir", "sumir", "submergir", "suar", "soltar", "sorver", "surrar", "suspirar", "tocar", "torcer", "tremular", "tremer", "triscar", "vencer", "viciar", "vigiar", "visar", "visitar", "voltar", "zoar"]
livros_da_biblia = ["genesis", "exodo", "levitico", "numeros", "deuteronomio", "josue", "juizes", "rute", "samuel", "reis", "cronicas", "esdras", "neemias", "ester", "jo", "salmos", "proverbios", "eclesiastes", "cantares", "isaias", "jeremias", "lamentacoes", "ezequiel", "daniel", "oseias", "joel", "amos", "obadias", "jonas", "miqueias", "naum", "habacuque", "sofonias", "ageu", "zacarias", "malaquias", "mateus", "marcos", "lucas", "joao", "atos", "romanos", "corintios", "galatas", "efesios", "filipenses", "colossenses", "tes", "timoteo", "tito", "filemom", "hebreus", "tiago", "pedro", "joao", "judas", "apocalipse"]
temas = [comidas, esportes, verbos, livros_da_biblia]


txt_menu_inicial = '<========>\n||    |   \n||    ü -  BEM VINDO AO HANGMAN!\n||   /|\   ESCOLHA O MODO DE JOGO:\n||   / \  \n||         0 - MANUAL // 1 - ALEATÓRIA\n<========>\n-> '
txt_escolhe_categoria = '<========>\n||    |   \n||    ü - SHOW! QUER ESCOLHER UMA CATEGORIA? \n||   /|\   \n||   / \  \n||         0 - COMIDAS // 1 - ESPORTES // 2 - VERBOS // 3 - LIVROS DA BIBLIA // 4 - QUALQUER UMA\n<========>\n-> '
txt_escolhe_categoria_denovo = '<========>\n||    |   \n||    ü - ESCOLHA INVÁLIDA!\n||   /|\   ESCOLHE CERTO DESSA VEZ!! \n||   / \  \n||         0 - COMIDAS // 1 - ESPORTES // 2 - VERBOS // 3 - LIVROS DA BIBLIA // 4 - QUALQUER UMA\n<========>\n-> '
txt_game_over = '<========>\n||    |   \n||   xP   \n||   /|\  \n||   / \  \n||       \n<========>\nPerdeu!'


boneco = [
    '<========>\n||    |   \n||   xP   \n||   /|\  \n||   / \  \n||       \n<========>',
    '<========>\n||    |   \n||   :O  - ESTADO CRÍTICO! \n||   /|\   - UM CHUTE RESTANTE\n||   /    \n||       \n<========>',
    '<========>\n||    |   \n||   :/   \n||   /|\  \n||        \n||       \n<========>',
    '<========>\n||    |   \n||   :)   \n||    |\  \n||        \n||       \n<========>',
    '<========>\n||    |   \n||   :D   \n||    |   \n||        \n||       \n<========>',
    '<========>\n||    |   \n||   :D   \n||        \n||        \n||       \n<========>',
    '<========>\n||    |   \n||        \n||        \n||        \n||       \n<========>'
]


jogando = True

while jogando == True:
    print('\033[1J')
    # Define a palavra a ser adivinhada
    
    modo = input(txt_menu_inicial)
    while modo not in ['0','1']: # Verifica se o modo escolhido é uma OPÇÃO VÁLIDA.
        modo = input(txt_menu_inicial)


    # Modo Manual
    if modo == '0':
        palavra = input('Escolha uma palavra para o outro jogador tentar adivinhar!\n-> \033[8m')
        palavra = ''.join(palavra.split())
        print('\033[0m')

    # Modo Aleatório
    elif modo == '1': 
        escolha = input(txt_escolhe_categoria)
        while escolha not in ['0','1','2','3','4']:
            escolha = input(txt_escolhe_categoria_denovo)
        if escolha == '4':
            tema_aleatorio = random.choice(temas)
            palavra = random.choice(tema_aleatorio)
        else:
            palavra = random.choice(temas[int(escolha)])

    palavra = palavra.upper()


    # Lógica principal do jogo
    letras_da_palavra = list(palavra)
    vidas = 6
    letras_chutadas = ['_' for _ in palavra]
    chutes_errados = set()


    while vidas > 0 and '_' in letras_chutadas:
        print('\033[1J',boneco[vidas])
        print(' '.join(letras_chutadas),'\nChutes Errados: ')
        for elemento in chutes_errados:
            print(elemento, end=" ")

        chute = input('\nDiga uma letra: ').upper()
        if chute == palavra:
            break
        elif chute in letras_chutadas:
            print('\nEssa já foi, amigão!')
            sleep(0.5)
        elif chute not in letras_da_palavra:
            chutes_errados.add(chute)
            print('\nNão tem essa letra na palavra')
            vidas -= 1
            sleep(0.5)
        else:
            for i in range(len(letras_da_palavra)):
                if letras_da_palavra[i] == chute:
                    letras_chutadas[i] = chute
        

    # Acabando com o jogo
    if vidas == 0:
        print(txt_game_over)
    elif chute == palavra:
        print('ヾ(⌐■_■)ノ♪  PARABÉNS! VOCÊ ACERTOU A PALAVRA INTEIRA!!!')
    else:
        print('Parabéns, você ganhou!!!')
    sleep(1)
    print('\nA palavra era: {} !\n'.format(palavra))

    escolha = input('Quer jogar de novo? | 0 - NAO // 1 = SIM |\n -> ')
    while escolha not in ['0','1']:
        escolha = input('Quer jogar de novo? | 0 - NAO // 1 = SIM |\n -> ')

    if escolha == '1':
        print('Show, bora lá!')
        sleep(1.75)

    elif escolha == '0':
        jogando = False
        print('Obrigado por jogar! Até a próxima :D')
        
    else:
        break
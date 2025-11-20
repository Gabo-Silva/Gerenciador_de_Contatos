def criarTabela():
    # Função que cria a tabela.
    import sqlite3
    conexao = sqlite3.connect('contatos.db')
    cursor = conexao.cursor()
    cursor.execute(''' 
            create table if not exists pessoas (
                    id integer primary key not null,
                    nome varchar(30) not null,
                    telefone varchar(20) not null,
                    email varchar(255) not null      
            );
''')


def leiaInt(msg):
    # Função que ler um número inteiro.
    while True:
        try:
            num = str(input(msg).strip())
        # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
        except EOFError:
            print('ERRO! OPÇÃO INVÁLIDA')
            print('-' * 50)
        # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
        except KeyboardInterrupt:
            print('\nERRO! OPÇÃO INVÁLIDA')
            print('-' * 50)
        else:
            # Caso a variável não possua somente números ou o número seja menor que zero, uma mensagem de erro será exibida.
            if num.isnumeric() == False or int(num) < 0:
                print('ERRO! OPÇÃO INVÁLIDA')
                print('-' * 50)
            else:
                # Caso tudo ocorra bem, a variável será retornada.
                return int(num)


def leiaInfo(msg):
    # Importando a biblioteca re.
    import re
    # Função que ler uma string.
    while True:
        try:
            info_pessoa = str(input(f'{msg}: ').strip())
        # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
        except EOFError:
            print(f'ERRO! {msg} INVÁLIDO'.upper())
            print('-' * 50)
        # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
        except KeyboardInterrupt:
            print(f'\nERRO! {msg} INVÁLIDO'.upper())
            print('-' * 50)
        else:
            # Dependendo da informação que iremos cadastrar um bloco de comando irá ser ativado.
            if msg in 'Nome':
                # Uma lista com todas as palavras.
                nome_sem_espacos = info_pessoa.split()
                # Junta todas as palavras e verifica se todas são letras do alfabeto.
                if ''.join(nome_sem_espacos).isalpha():
                    print('-' * 50)
                    # Se sim, retorna a variável.
                    return info_pessoa.title()
                else:
                    # Se não, uma mensagem de erro será exibida.
                    print(f'ERRO! {msg} INVÁLIDO'.upper())
                    print('-' * 50)
            elif msg in 'Email':
                # Faz uma lista usando os separadores (@, .).
                dominio = re.split('[@, .]', info_pessoa)
                try:
                    # Se qualquer parte do email estive vazia ou o . vier antes do @, uma mensagem de erro será exibida.
                    if len(dominio[0]) == 0 or len(dominio[1]) == 0 or len(dominio[2]) == 0 or len(dominio) > 3 or info_pessoa.index('@') > info_pessoa.index('.'):
                        print(f'ERRO! {msg} INVÁLIDO'.upper())
                        print('-' * 50)
                    # Caso tudo ocorra bem, a variável será retornada.
                    else:
                        print('-' * 50)
                        return info_pessoa
                except:
                    print(f'ERRO! {msg} INVÁLIDO'.upper())
                    print('-' * 50)
            elif msg in 'Telefone':
                try:
                    # Faz uma lista com os números usando o separador (-).
                    numeros = info_pessoa.split('-')
                    # Se a lista não tive exatamente dois itens ou o primeiro item não tiver exatamente cinco caracteres ou o segundo item não tiver exatamente quatro caracteres ou o telefone não começa com 9 ou se alguns dos itens não tiver somente números na sua composição, uma mensagem de erro será exibida.
                    if len(numeros) != 2 or len(numeros[0]) != 5 or len(numeros[1]) != 4 or info_pessoa.index('9') != 0 or numeros[0].isnumeric() == False or numeros[1].isnumeric() == False:
                        print(f'ERRO! {msg} INVÁLIDO'.upper())
                        print('-' * 50)
                    # Caso tudo ocorra bem, a variável será retornada.
                    else:
                        print('-' * 50)
                        return info_pessoa
                except:
                    print(f'ERRO! {msg} INVÁLIDO'.upper())
                    print('-' * 50)


def menu(* opcoes):
    # Função responsável pelo menu.
    print('-' * 50)
    print('GERENCIADOR DE CONTATOS'.center(50))
    print('-' * 50)
    for indice, op in enumerate(opcoes):
        print(f'{indice + 1} - {op}')
    print('-' * 50)
    while True:
        # Chama a função leiaInt.
        usu_op = leiaInt('Digite sua opção: ')
        # Caso o valor da variável seja menor do 1 ou seja maior do que o tanto de opções, uma mensagem de erro será exibida.
        if usu_op < 1 or usu_op > len(opcoes):
            print('ERRO! OPÇÃO INVÁLIDA')
            print('-' * 50)
        # Caso tudo ocorra bem, a variável será retornada.
        else:
            return usu_op


def adicionarContato():
    # Uma lista com as informações.
    info = []
    # Importando a biblioteca sqlite3.
    import sqlite3
    # Criando uma conexão com nosso banco de dados e também se necessário o criando.
    conexao = sqlite3.connect('contatos.db')
    # Criando nossa tabela.
    criarTabela()
    # Criando o cursor para que possamos executar os comandos relacionados com o banco de dados.
    cursor = conexao.cursor()
    while True:
        res = ''
        print('-' * 50)
        print('ADICIONAR CONTATO'.center(50))
        print('-' * 50)
        # Adquirindo as informações.
        info.append(leiaInfo('Nome'))
        info.append(leiaInfo('Email'))
        info.append(leiaInfo('Telefone'))
        # Colocando as informações na nossa tabela.
        cursor.execute(
            f"insert into pessoas(nome, email, telefone) values('{info[0]}', '{info[1]}', '{info[2]}')")
        conexao.commit()
        # Mensagem de conclusão.
        print('CADASTRO CONCLUÍDO'.center(50))
        print('-' * 50)
        # Limpando a lista com as informações.
        info.clear()
        while res not in ('S', 'N'):
            try:
                # Pergunta se o usuário quer continuar, se sim, continua.
                res = str(input('Quer continuar [S/N]? ').strip().upper())
                # Se a resposta não for 'S' ou 'N', uma mensagem de erro será exibida.
                if res not in ('S', 'N'):
                    print('ERRO! OPÇÃO INVÁLIDA')
                    print('-' * 50)
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('ERRO! OPÇÃO INVÁLIDA')
                print('-' * 50)
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print('\nERRO! OPÇÃO INVÁLIDA')
                print('-' * 50)
        # Se não, termina.
        if res in 'N':
            # Fechando o banco de dados.
            conexao.close()
            break


def listarContatos():
    # Importando a biblioteca sqlite3.
    import sqlite3
    res_saida = ''
    # Criando uma conexão com nosso banco de dados e também se necessário o criando.
    conexao = sqlite3.connect('contatos.db')
    # Criando nossa tabela.
    criarTabela()
    # Criando o cursor para que possamos executar os comandos relacionados com o banco de dados.
    cursor = conexao.cursor()
    # Pegando todos os registros.
    registros = cursor.execute('select * from pessoas')
    # Se não possuir nenhum registro, esse bloco de comando será ativado.
    if len(registros.fetchall()) == 0:
        print('-' * 50)
        print('NENHUM CONTATO REGISTRADO'.center(50))
        print('-' * 50)
        # Fechando o banco de dados.
        conexao.close()
    else:
        print('-' * 50)
        print('CONTATOS'.center(50))
        print('-' * 50)
        # Pegando todos os registros novamente.
        linhas = cursor.execute('select * from pessoas')
        # Listando todos os registros.
        for l in linhas.fetchall():
            print(f'{l[0]} - {l[1]}')
            print(f'{l[2]} | {l[3]}')
            print('-' * 50)
        while True:
            try:
                # Pergunta se o usuário quer sair, se sim, ele sai.
                res_saida = str(input('Sair [S]? ').strip().upper())
                # Se a resposta não for 'S' ou se tiver mais de uma caractere, uma mensagem de erro será exibida.
                if 'S' not in res_saida or len(res_saida) > 1:
                    print('ERRO! OPÇÃO INVÁLIDA')
                    print('-' * 50)
                else:
                    break
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('ERRO! OPÇÃO INVÁLIDA')
                print('-' * 50)
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print('\nERRO! OPÇÃO INVÁLIDA')
                print('-' * 50)
            else:
                # Fechando o banco de dados.
                conexao.close()


def buscarContatos():
    # Importando a biblioteca sqlite3.
    import sqlite3
    while True:
        # Criando uma conexão com nosso banco de dados e também se necessário o criando.
        conexao = sqlite3.connect('contatos.db')
        # Criando nossa tabela.
        criarTabela()
        # Criando o cursor para que possamos executar os comandos relacionados com o banco de dados.
        cursor = conexao.cursor()
        # Pegando todos os registros.
        registros = cursor.execute('select * from pessoas')
        # Se não possuir nenhum registro, esse bloco de comando será ativado.
        if len(registros.fetchall()) == 0:
            print('-' * 50)
            print('NENHUM CONTATO REGISTRADO'.center(50))
            print('-' * 50)
            # Fechando o banco de dados.
            conexao.close()
            break
        else:
            print('-' * 50)
            print('BUSCAR CONTATO'.center(50))
            print('-' * 50)
            res = ''
            # Variável que verifica quantas pessoas foram encontradas.
            pessoas_encontradas = 0
            # Pegando todos os registros novamente.
            linhas = cursor.execute('select * from pessoas')
            try:
                nome = str(input('Digite o nome do contato: ').strip().title())
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('-' * 50)
                print('PESSOA NÃO ENCONTRADA!'.center(50))
                print('-' * 50)
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print()
                print('-' * 50)
                print('PESSOA NÃO ENCONTRADA!'.center(50))
                print('-' * 50)
            else:
                print('-' * 50)
                for i, l in enumerate(linhas.fetchall()):
                    # Se o nome digitado pelo usuário for igual ao algum nome registrado, ele será exibido.
                    if l[1] == nome:
                        print(f'{l[0]} - {l[1]}')
                        print(f'{l[2]} | {l[3]}')
                        print('-' * 50)
                        # Variável ganhar mais um pra cada pessoa encontrada.
                        pessoas_encontradas += 1
                # Se o número de pessoas encontradas for igual a zero, esse bloco de comando será ativado.
                if pessoas_encontradas == 0:
                    print('PESSOA NÃO ENCONTRADA!'.center(50))
                    print('-' * 50)
            while res not in ('S', 'N'):
                try:
                    # Pergunta se o usuário quer continuar, se sim, continua.
                    res = str(input('Quer continuar [S/N]? ').strip().upper())
                    # Se a resposta não for 'S' ou 'N', uma mensagem de erro será exibida.
                    if res not in ('S', 'N'):
                        print('ERRO! OPÇÃO INVÁLIDA')
                        print('-' * 50)
                # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
                except EOFError:
                    print('ERRO! OPÇÃO INVÁLIDA')
                    print('-' * 50)
                # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
                except KeyboardInterrupt:
                    print('\nERRO! OPÇÃO INVÁLIDA')
                    print('-' * 50)
            # Se não, termina.
            if res in 'N':
                # Fechando o banco de dados.
                conexao.close()
                break


def atualizar():
    # Importando a biblioteca sqlite3.
    import sqlite3
    # Opções que o usuário poderá escolher.
    opcoes = ('Nome', 'Email', 'Telefone')
    while True:
        # Criando uma conexão com nosso banco de dados e também se necessário o criando.
        conexao = sqlite3.connect('contatos.db')
        # Criando nossa tabela.
        criarTabela()
        # Criando o cursor para que possamos executar os comandos relacionados com o banco de dados.
        cursor = conexao.cursor()
        # Pegando todos os registros.
        registros = cursor.execute('select * from pessoas')
        # Se não possuir nenhum registro, esse bloco de comando será ativado.
        if len(registros.fetchall()) == 0:
            print('-' * 50)
            print('NENHUM CONTATO REGISTRADO'.center(50))
            print('-' * 50)
            # Fechando o banco de dados.
            conexao.close()
            break
        else:
            print('-' * 50)
            print('ATUALIZAR CONTATO'.center(50))
            print('-' * 50)
            res = ''
            # Variável que verifica quantas pessoas foram encontradas.
            pessoas_encontradas = 0
            # Pegando todos os registros novamente.
            linhas = cursor.execute('select * from pessoas')
            try:
                nome = str(input('Digite o nome do contato: ').strip().title())
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('-' * 50)
                print('PESSOA NÃO ENCONTRADA!'.center(50))
                print('-' * 50)
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print()
                print('-' * 50)
                print('PESSOA NÃO ENCONTRADA!'.center(50))
                print('-' * 50)
            else:
                print('-' * 50)
                for i, l in enumerate(linhas.fetchall()):
                    # Se o nome digitado pelo usuário for igual ao algum nome registrado, ele será exibido.
                    if l[1] == nome:
                        print(f'{l[0]} - {l[1]}')
                        print(f'{l[2]} | {l[3]}')
                        print('-' * 50)
                        # Variável ganhar mais um pra cada pessoa encontrada.
                        pessoas_encontradas += 1
                # Se o número de pessoas encontradas for igual a zero, esse bloco de comando será ativado.
                if pessoas_encontradas == 0:
                    print('PESSOA NÃO ENCONTRADA!'.center(50))
                    print('-' * 50)
                else:
                    # A variável pessoas encontradas volta a ser zero.
                    pessoas_encontradas = 0
                    # Pergunta o índice que o usuário quer atualizar.
                    indice_atualizar = leiaInt(
                        'Qual contato você deseja atualizar: ')
                    print('-' * 50)
                    # Pegando todos os registros novamente.
                    linhas = cursor.execute('select * from pessoas')
                    for i, l in enumerate(linhas.fetchall()):
                        # Se o id for igual ao indice digitado pelo usuário e o nome for igual ao nome digitado pelo usuário, esse bloco de comando será ativado.
                        if l[0] == indice_atualizar and l[1] == nome:
                            for indice, campo in enumerate(opcoes):
                                # Exibe o menu de opções.
                                print(f'{indice + 1} - {campo}')
                                # Variável ganhar mais um pra cada pessoa encontrada.
                                pessoas_encontradas += 1
                            print('-' * 50)
                    # Se o número de pessoas encontradas for igual a zero, esse bloco de comando será ativado.
                    if pessoas_encontradas == 0:
                        print('PESSOA NÃO ENCONTRADA!'.center(50))
                        print('-' * 50)
                    else:
                        while True:
                            # Pergunta o índice de qual opção o usuário deseja alterar.
                            res_op = leiaInt(
                                'Qual informação você deseja alterar? ')
                            # Se o índice for maior que o tanto de opções ou o índice for igual a zero, uma mensagem de erro será exibida.
                            if res_op > len(opcoes) or res_op == 0:
                                print('ERRO! OPÇÃO INVÁLIDA')
                                print('-' * 50)
                            else:
                                break
                        print('-' * 50)
                        # Variável que recebe a nova informação.
                        nova_informação = leiaInfo(f'{opcoes[res_op - 1]}')
                        # Atualiza a informação.
                        cursor.execute(
                            f'update pessoas set {opcoes[res_op - 1].lower()} = "{nova_informação}" where id = {indice_atualizar}')
                        conexao.commit()
                        # Mensagem de conclusão.
                        print('INFORMAÇÃO ATUALIZADA COM SUCESSO'.center(50))
                        print('-' * 50)
                while res not in ('S', 'N'):
                    try:
                        # Pergunta se o usuário quer continuar, se sim, continua.
                        res = str(
                            input('Quer continuar [S/N]? ').strip().upper())
                        # Se a resposta não for 'S' ou 'N', uma mensagem de erro será exibida.
                        if res not in ('S', 'N'):
                            print('ERRO! OPÇÃO INVÁLIDA')
                            print('-' * 50)
                    # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
                    except EOFError:
                        print('ERRO! OPÇÃO INVÁLIDA')
                        print('-' * 50)
                    # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
                    except KeyboardInterrupt:
                        print('\nERRO! OPÇÃO INVÁLIDA')
                        print('-' * 50)
                # Se não, termina.
                if res in 'N':
                    # Fechando o banco de dados.
                    conexao.close()
                    break


def excluir():
    # Importando a biblioteca sqlite3.
    import sqlite3
    while True:
        # Criando uma conexão com nosso banco de dados e também se necessário o criando.
        conexao = sqlite3.connect('contatos.db')
        # Criando nossa tabela.
        criarTabela()
        # Criando o cursor para que possamos executar os comandos relacionados com o banco de dados.
        cursor = conexao.cursor()
        # Pegando todos os registros.
        registros = cursor.execute('select * from pessoas')
        # Se não possuir nenhum registro, esse bloco de comando será ativado.
        if len(registros.fetchall()) == 0:
            print('-' * 50)
            print('NENHUM CONTATO REGISTRADO'.center(50))
            print('-' * 50)
            # Fechando o banco de dados.
            conexao.close()
            break
        else:
            print('-' * 50)
            print('EXCLUIR CONTATO'.center(50))
            print('-' * 50)
            res = ''
            # Variável que verifica quantas pessoas foram encontradas.
            pessoas_encontradas = 0
            # Pegando todos os registros novamente.
            linhas = cursor.execute('select * from pessoas')
            try:
                nome = str(
                    input('Digite o nome do contato que deseja excluir: ').strip().title())
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('-' * 50)
                print('PESSOA NÃO ENCONTRADA!'.center(50))
                print('-' * 50)
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print()
                print('-' * 50)
                print('PESSOA NÃO ENCONTRADA!'.center(50))
                print('-' * 50)
            else:
                print('-' * 50)
                for i, l in enumerate(linhas.fetchall()):
                    # Se o nome digitado pelo usuário for igual ao algum nome registrado, ele será exibido.
                    if l[1] == nome:
                        print(f'{l[0]} - {l[1]}')
                        print(f'{l[2]} | {l[3]}')
                        print('-' * 50)
                        # Variável ganhar mais um pra cada pessoa encontrada.
                        pessoas_encontradas += 1
                # Se o número de pessoas encontradas for igual a zero, esse bloco de comando será ativado.
                if pessoas_encontradas == 0:
                    print('PESSOA NÃO ENCONTRADA!'.center(50))
                    print('-' * 50)
                else:
                    # Variável que verifica quantas pessoas foram encontradas.
                    pessoas_encontradas = 0
                    # Pergunta o índice de qual opção o usuário deseja excluir.
                    indice_excluir = leiaInt(
                        'Qual contato você deseja excluir: ')
                    print('-' * 50)
                    # Pegando todos os registros novamente.
                    linhas = cursor.execute('select * from pessoas')
                    for l in linhas.fetchall():
                        # Se o id for igual ao indice digitado pelo usuário e o nome for igual ao nome digitado pelo usuário, esse bloco de comando será ativado.
                        if l[0] == indice_excluir and l[1] == nome:
                            # Deleta a pessoa cadastrada.
                            cursor.execute(
                                f'delete from pessoas where id = {indice_excluir}')
                            conexao.commit()
                            # Variável ganhar mais um pra cada pessoa encontrada.
                            pessoas_encontradas += 1
                            # Mensagem de conclusão.
                            print('CONTATO EXCLUIDO COM SUCESSO'.center(50))
                            print('-' * 50)
                    # Se o número de pessoas encontradas for igual a zero, esse bloco de comando será ativado.
                    if pessoas_encontradas == 0:
                        print('PESSOA NÃO ENCONTRADA!'.center(50))
                        print('-' * 50)
            # Pegando todos os registros novamente.
            registros = cursor.execute('select * from pessoas')
            # Se não possuir nenhum registro, esse bloco de comando será ativado.
            if len(registros.fetchall()) == 0:
                print('-' * 50)
                print('NENHUM CONTATO REGISTRADO'.center(50))
                print('-' * 50)
                # Fechando o banco de dados.
                conexao.close()
                break
            else:
                while res not in ('S', 'N'):
                    try:
                        # Pergunta se o usuário quer continuar, se sim, continua.
                        res = str(
                            input('Quer continuar [S/N]? ').strip().upper())
                        # Se a resposta não for 'S' ou 'N', uma mensagem de erro será exibida.
                        if res not in ('S', 'N'):
                            print('ERRO! OPÇÃO INVÁLIDA')
                            print('-' * 50)
                    # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
                    except EOFError:
                        print('ERRO! OPÇÃO INVÁLIDA')
                        print('-' * 50)
                    # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
                    except KeyboardInterrupt:
                        print('\nERRO! OPÇÃO INVÁLIDA')
                        print('-' * 50)
                # Se não, termina.
                if res in 'N':
                    # Fechando o banco de dados.
                    conexao.close()
                    break

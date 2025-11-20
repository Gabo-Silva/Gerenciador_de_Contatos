# Importando as minhas funções
import agenda
while True:
    # Menu
    usu_res = agenda.menu('Adicionar Contato', 'Listar Todos os Contatos',
                          'Buscar Contato', 'Atualizar Informações', 'Excluir Contatos', 'Sair')
    # Depedendo da opcão escolhida pelo usuário algum bloco de comando será ativado.
    if usu_res == 1:
        agenda.adicionarContato()
    elif usu_res == 2:
        agenda.listarContatos()
    elif usu_res == 3:
        agenda.buscarContatos()
    elif usu_res == 4:
        agenda.atualizar()
    elif usu_res == 5:
        agenda.excluir()
    elif usu_res == 6:
        break
# Fim.
print('-' * 50)
print('OBRIGADO POR USAR O MEU GERENCIADOR DE CONTATOS'.center(50))
print('-' * 50)

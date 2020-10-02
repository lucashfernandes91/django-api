# django-api
Aplicação simples utilizando Django + Django Rest Framework

A demonstração da aplicação está acessível através dos links: 
https://entrevista-teste.herokuapp.com/funcionarios/
https://entrevista-teste.herokuapp.com/empresas/

1. Através da API podemos também adicionar, editar, excluir e consultar funcionários já cadastrados.
Obs.: Os métodos para listar funcinário específico, deletar e editar utilizam o 'username' do funciário. 

# Listar todos funcionários (GET)
URL: https://entrevista-teste.herokuapp.com/funcionarios/username*

# Listar funcionários específico(GET)
URL: https://entrevista-teste.herokuapp.com/funcionarios/username*

# Adicionar funcinári@
URL: https://entrevista-teste.herokuapp.com/funcionarios/
	{	
		"username":"ciclano",
		"primeiro_nome":"Fulano",
		"ultimo_nome":"Fernandes",
		"telefone":"5198454671",
		"email":"lucas@lucas.com",
		"empresas":[1,2]
	}

# Edita funcionario json (PUT)
URL: https://entrevista-teste.herokuapp.com/funcionarios/username
	{	
		"username":"teste2",
		"primeiro_nome":"Ciclano",
		"ultimo_nome":"Dacsta",
		"telefone":"5198454671",
		"email":"contato@contato.com",
		"empresas":[1,2]
	}

# Deletar funcionário (DELETE)
URL: https://entrevista-teste.herokuapp.com/funcionarios/username*

2. Podemos consultar empresas cadastradas ou realizar o cadastro de uma
# Listar Empresas cadastradas (GET)
https://entrevista-teste.herokuapp.com/empresas/

# Criar uma Empresa (POST)
https://entrevista-teste.herokuapp.com/empresas/
    {
        "nome": "Empresa x"
    }






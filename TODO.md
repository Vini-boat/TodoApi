- [ ] Autenticação
  - [X] Token JWT
  - [X] Login
  - [ ] Logout
- [ ] Segurança
  - [X] Hashing de senhas
  - [ ] OAuth2 scopes (admin, user, convidado)
- [ ] Tests
  - [X] workflow de testes
  - [ ] calcular a cobertura dos testes (coverage, pytest-cov)     
  - [ ] controllers (fastapi TestClient)
  - [ ] services 
  - [ ] Repository
  
- [X] Escolher os 2 primeiros requisitos complementares
- [ ] Logs
- [X] Tratamento adequado de erros
  - [X] Criar Exceções de domínio
  - [X] Criar Exceções do protocolo HTTP
  - [X] Criar os Handlers de Exceções
- [X] Filtros Avançados
- [ ] Comentários


A fazer 

	Archtecture Decision Records
	
			-Comentários em Tarefas (Sub-recursos aninhados) Implementar
			/tasks/{id}/comments com suporte a: o Criação, leitura e exclusão
			de comentários o Associar comentários a usuários e timestamps
			
			-Filtro Avançado de Tarefas
			Endpoint com múltiplos parâmetros:
			GET /tasks?status=done&priority=high&dueBefore=2025-06-01
			
	- Swegger não guarda token jwt;
	- Fluxo de requisições: principais ENDPONTS;
	- diagrama de BD descrição de tabelas/coleções;
	- cobertura do código = validação dos testes.

- [X] Autenticação
  - [X] Token JWT
  - [X] Login
  - [X] Logout
- [x] Segurança
  - [X] Hashing de senhas
  - [X] OAuth2 scopes (admin, user, convidado)
- [ ] Tests
  - [X] workflow de testes
  - [x] calcular a cobertura dos testes (coverage, pytest-cov)     
  - [x] controllers (fastapi TestClient)
  - [x] services 
  - [x] Repository
  - [ ] Fluxo de requisições: principais ENDPONTS;
- [ ] Diagrama de BD descrição de tabelas/coleções;
- [X] Escolher os 2 primeiros requisitos complementares

			-Comentários em Tarefas (Sub-recursos aninhados) Implementar
			/tasks/{id}/comments com suporte a: o Criação, leitura e exclusão
			de comentários o Associar comentários a usuários e timestamps
			
			-Filtro Avançado de Tarefas
			Endpoint com múltiplos parâmetros:
			GET /tasks?status=done&priority=high&dueBefore=2025-06-01

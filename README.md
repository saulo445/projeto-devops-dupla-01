# Projeto DevOps: dupla-01

- Site: [Página da dupla](https://saulo445.github.io/projeto-devops-dupla-01/)
- Status: [status.html](https://saulo445.github.io/projeto-devops-dupla-01/status.html)
- Imagem: `ghcr.io/saulo445/projeto-devops-dupla-01`

## O fluxo completo

1. Um push inicia o CI, que roda os testes da API e constrói a imagem para verificar o Dockerfile.
2. Na `main`, o fluxo do GitHub Pages roda os testes antes de publicar o site e atualizar o status.
3. Quando enviamos uma tag de versão, o fluxo da imagem roda os testes, usa a tag como `APP_VERSION` e publica a imagem no `ghcr.io`.
4. Baixamos a versão escolhida com `docker pull` e iniciamos o contêiner na porta `5001`.
5. Consultamos `/saude` para conferir se a API responde e qual versão está rodando.

## Linha do tempo

- **v1 (`212e2d6`):** imagem inicial do exercício. A API respondeu na porta `5001` e informou `v1`.
- **v2 (`add28ef`):** a API passou a escutar na porta `5002`, mas o Docker continuou mapeando a porta `5001`. Os testes passaram, e o `curl` falhou.
- **v3 (`97400fd`):** a reversão restaurou a porta `5001`. A imagem publicada respondeu em `/saude` e informou `v3`.

## O que os testes não pegaram

Os testes chamavam as rotas pelo cliente de teste do Flask, sem passar pela porta do contêiner. Para pegar a falha antes de publicar, eu subiria a imagem com o mesmo mapeamento usado na execução, chamaria `/saude` pela porta `5001` e faria o fluxo falhar se a API não respondesse como esperado.

## Quem fez o quê

**Saulo (aluno A, @saulo445):** Fiz o fluxo da página de status e conferi que a imagem podia ser baixada sem login no registro. Minha variação é a dupla `dupla-01`, com a mensagem `aprendendo DEVOPS` e a porta `5001`. Rodei os contêineres no Docker Desktop, confirmei a falha da v2 e voltei à v1 em 4,27 segundos. A reversão no repositório restaurou a porta original e a v3 voltou a responder.

**Arthur (aluno B):** A completar pelo aluno B.

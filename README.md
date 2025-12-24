# 🤠 Django Hangman (Jogo da Forca Web)
### Developed by Ailton Dos Santos

**Uma implementação web interativa do clássico Jogo da Forca utilizando Django Sessions e Banco de Dados.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square) ![Django](https://img.shields.io/badge/Framework-Django-092E20?style=flat-square) ![DB](https://img.shields.io/badge/Database-SQLite3-003B57?style=flat-square)

## 📄 Sobre o Projeto

Este projeto é uma aplicação Full-Stack desenvolvida em **Django** que demonstra o uso de **Gerenciamento de Estado via Sessões** (Session Management).

Diferente de jogos simples de console, esta versão web permite que múltiplos usuários joguem simultaneamente sem conflitos, pois o estado do jogo (palavra secreta, tentativas, letras erradas) é armazenado na sessão individual de cada navegador.

Além do jogo, o sistema possui um módulo de **Gestão de Contatos** com persistência em banco de dados SQLite.

## ⚙️ Funcionalidades Técnicas

### 🎮 Lógica do Jogo (Session Based)
O núcleo do jogo reside em `views.py` e utiliza `request.session` para manter a persistência entre as requisições HTTP:
* **Persistência de Estado:** Armazena a `palavra_secreta` e `tentativas_restantes` no cookie de sessão do usuário.
* **Feedback Visual Dinâmico:** Utiliza um dicionário de mapeamento (`IMAGEM_MAP`) para renderizar a imagem correta da forca baseada no contador de erros.
* **Validação de Input:** Tratamento no Back-end para garantir que apenas letras válidas e não repetidas sejam processadas.

### 📇 Módulo de Contatos (Model Based)
* **Formulário de Entrada:** Captura nome e e-mail.
* **Persistência:** Salva os dados no banco `db.sqlite3` usando o ORM do Django (Model `Contato`).
* **Listagem:** Exibe os dados cadastrados dinamicamente no template.

## 🛠️ Tecnologias Utilizadas

* **Back-end:** Python & Django Framework
* **Front-end:** HTML5, CSS (Templates Django)
* **Banco de Dados:** SQLite3
* **Controle de Versão:** Git

## 🚀 Como Rodar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/ailton-santos/nome-do-seu-repo.git](https://github.com/ailton-santos/nome-do-seu-repo.git)

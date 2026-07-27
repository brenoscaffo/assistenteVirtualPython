# 🤖 Assistente Virtual para Desenvolvedores Iniciantes em Python

Um assistente virtual desenvolvido para auxiliar programadores iniciantes a esclarecer dúvidas sobre a linguagem de programação **Python** de forma rápida, prática e interativa.

A aplicação utiliza **Inteligência Artificial** para responder perguntas relacionadas à sintaxe, conceitos fundamentais, boas práticas, resolução de erros e lógica de programação, proporcionando uma experiência semelhante à de um tutor virtual.

**Para esse projeto, não é obrigatório a criação de um novo ambiente virtual. Criei para poder mostrar o passo a passo das instalações das bibliotecas utilizadas e das dependências necessárias.**

---

## 🚀 Funcionalidades

- 💬 Chat interativo com IA
- 🐍 Respostas voltadas para dúvidas sobre Python
- 📖 Explicação de conceitos da linguagem
- 🐞 Auxílio na identificação e correção de erros
- 💡 Sugestões de boas práticas de programação
- ⚡ Interface simples e intuitiva desenvolvida com Streamlit

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Python**
- **Groq API** - Integração com modelos de linguagem (LLMs)
- **Streamlit** - Interface web interativa
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **OS** - Manipulação de variáveis do sistema

---

## 📂 Estrutura do Projeto

```text
📦 assistente-python
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> A estrutura pode variar conforme a evolução do projeto.

---

## ⚙️ Pré-requisitos

Antes de executar o projeto, é necessário possuir:

- Python 3.10 ou superior
- Uma chave de API da Groq

---

## 🔑 Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

Entre na pasta do projeto:

```bash
cd nome-do-repositorio
```

### 2. Crie um ambiente virtual

Windows

```bash
conda create --name nome_do_venv python=3.
conda activate nome_do_venv
```

Windows

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a variável de ambiente

Crie um arquivo chamado `.env` na raiz do projeto.

Exemplo:

```env
GROQ_API_KEY=sua_chave_da_api
```

---

## ▶️ Executando a aplicação

No terminal, execute:

```bash
streamlit run app.py
```

Após isso, a aplicação será aberta automaticamente no navegador.

---

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo servir como uma ferramenta de apoio ao aprendizado de Python, oferecendo respostas rápidas e contextualizadas para desenvolvedores iniciantes.

Entre os principais objetivos estão:

- Facilitar o aprendizado da linguagem Python;
- Incentivar a autonomia dos estudantes;
- Auxiliar na compreensão de erros comuns;
- Explicar conceitos fundamentais da programação;
- Tornar o processo de aprendizagem mais interativo utilizando IA.

---

## 📌 Possíveis Melhorias

- Histórico de conversas
- Upload de arquivos Python
- Explicação detalhada de códigos enviados pelo usuário
- Geração de exemplos práticos
- Suporte para outras linguagens de programação
- Tema claro/escuro

---

## 🤝 Contribuição

Contribuições são bem-vindas!

Caso queira contribuir:

1. Faça um Fork do projeto;
2. Crie uma branch para sua feature;

```bash
git checkout -b minha-feature
```

3. Faça o commit das alterações;

```bash
git commit -m "Minha nova feature"
```

4. Envie para o GitHub;

```bash
git push origin minha-feature
```

5. Abra um Pull Request.

---

## 📄 Licença

Este projeto está sob a licença MIT.

Sinta-se à vontade para utilizar, modificar e contribuir.

---

## 👨‍💻 Autor

Desenvolvido por **Breno Scaffo**.

Se este projeto foi útil para você, deixe uma ⭐ no repositório!

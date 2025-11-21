# 🔗 Central de Atalhos Web (Web Shortcuts)

> Um hub centralizado para acesso rápido às ferramentas e redes sociais mais utilizadas no dia a dia, eliminando a necessidade de digitar URLs repetitivas.

---

## 🌐 Acesso Online (Live Demo)

O projeto está hospedado e funcional através do GitHub Pages. Clique abaixo para acessar:

### [👉 Acessar Central de Atalhos](https://bluejaem.github.io/Site-dos-Sites/)

---

## 🛠️ Sobre o Projeto

Este projeto nasceu da necessidade de otimizar a navegação na web. Originalmente concebido com uma lógica de backend em **Python (Flask)**, o sistema foi portado para **JavaScript Puro (Vanilla JS)** para permitir uma execução leve, rápida e totalmente *Client-Side*, rodando diretamente no navegador do usuário sem necessidade de servidores externos.

### Funcionalidades
- **Busca Insensível a Maiúsculas:** O algoritmo reconhece `youtube`, `YouTube` ou `YOUTUBE` da mesma forma.
- **Validação de Entrada:** Feedback visual caso o site digitado não esteja no banco de dados.
- **Navegação Direta:** Gera links clicáveis que abrem em novas abas (`target="_blank"`).
- **Interface Limpa:** Design minimalista focado em usabilidade.

---

## 💻 Tecnologias e Lógica

A arquitetura do projeto baseia-se na manipulação do DOM (Document Object Model) e estruturas de dados de chave-valor.

### 1. Estrutura de Dados (O "Cérebro")
A base de dados funciona como um **Dicionário (Hash Map)**. Em vez de percorrer arrays com loops, o sistema usa a complexidade O(1) para encontrar links instantaneamente através de chaves únicas.

**Exemplo da Lógica (JavaScript):**
```javascript
const links = {
    'YOUTUBE': '[https://www.youtube.com/](https://www.youtube.com/)',
    'GITHUB': '[https://github.com/](https://github.com/)',
    // ... outros atalhos
};
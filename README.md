# 📚 Hub de Aulas Senac

![GitHub](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)

**Hub de Aulas Senac** é um website estático para organização e apresentação de conteúdo educacional dos cursos do SENAC. O projeto oferece uma interface elegante com slides automáticos gerados para cada aula.

## ✨ Características

- 🎯 **Interface Centralizada**: Hub principal conectando todas as disciplinas
- 📊 **Slides Automáticos**: Sistema de geração automática de apresentações HTML
- 🎨 **Design Moderno**: Interface com glassmorphism e gradientes suaves
- 📱 **Responsivo**: Totalmente adaptável para mobile, tablet e desktop
- ⌨️ **Navegação por Teclado**: Setas para navegar entre slides
- 🚀 **Zero Dependências**: Site 100% estático, sem necessidade de servidor backend

## 🏗️ Estrutura do Projeto

```
hub_aula_senac/
├── index.html                    # Página principal do hub
├── generate_slides.py            # Script gerador de slides
├── sources.json                  # URLs das imagens (Cloudinary)
├── css/
│   ├── style.css                 # Estilos principais
│   └── slides.css                # Estilos das apresentações
└── pages/
    ├── professor.html            # Perfil do professor
    ├── qualidade-software.html   # Disciplina: Qualidade de Software
    ├── introducao-logica.html    # Disciplina: Introdução à Lógica
    ├── tcc.html                  # Disciplina: TCC
    ├── qualidade/                # Slides gerados (16 aulas)
    ├── logica/                   # Slides gerados (16 aulas)
    └── tcc/                      # Slides gerados (16 semanas)
```

## 🎓 Disciplinas Disponíveis

### 1. Qualidade de Software (TADS)
- **16 aulas** cobrindo desde fundamentos até CI/CD
- Tópicos: Testes automatizados, TDD, Selenium, JMeter

### 2. Introdução à Lógica (Redes de Computadores)
- **16 aulas** de algoritmos e Python
- Tópicos: Estruturas de dados, loops, funções, POO

### 3. Trabalho de Conclusão (Ciência da Computação)
- **16 semanas** de cronograma de projeto
- Tópicos: Planejamento, desenvolvimento, documentação, apresentação

## 🚀 Como Usar

### Pré-requisitos

- Python 3.12 ou superior
- Navegador web moderno

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/hub_aula_senac.git
cd hub_aula_senac
```

2. **Execute o servidor local:**
```bash
python3 -m http.server 8000
```

3. **Acesse no navegador:**
```
http://localhost:8000
```

## 🔧 Desenvolvimento

### Gerando Slides Automaticamente

O projeto inclui um script Python que gera automaticamente slides HTML para cada aula:

```bash
python3 generate_slides.py
```

**O que o script faz:**
- 📖 Lê as páginas de disciplinas em `pages/`
- 🔍 Extrai títulos e descrições das aulas via regex
- 🎨 Gera slides HTML a partir de um template
- 🔗 Atualiza os links nas páginas principais
- ✅ Cria 5 slides por aula: capa, agenda, conceitos, aprofundamento, conclusão

### Adicionando Novas Aulas

1. **Edite o arquivo da disciplina** (ex: `pages/qualidade-software.html`)

2. **Adicione o bloco da aula:**
```html
<div class="col-md-6">
  <a href="#" class="list-group-item list-group-item-action border border-light rounded shadow-sm p-3 h-100 d-flex flex-column bg-white">
    <div class="d-flex w-100 justify-content-between mb-2">
      <h5 class="mb-1 fw-bold text-dark">Aula 17</h5>
      <span class="badge bg-light text-dark border fw-normal">
        <i class="far fa-calendar-alt me-1"></i> dd/mm/aaaa
      </span>
    </div>
    <p class="mb-1 text-muted small">Descrição da nova aula</p>
  </a>
</div>
```

3. **Regenere os slides:**
```bash
python3 generate_slides.py
```

### Adicionando Nova Disciplina

1. **Configure em `generate_slides.py`:**
```python
SUBJECTS = [
    # ... disciplinas existentes
    {
        'file': 'nova-disciplina.html',
        'folder': 'nova-disciplina',
        'course_tag': 'Nome do Curso',
        'subject_name': 'Nome da Disciplina',
        'prefix': 'Aula'  # ou 'Semana'
    }
]
```

2. **Crie a estrutura:**
```bash
mkdir pages/nova-disciplina
# Crie pages/nova-disciplina.html baseado nos existentes
```

3. **Adicione card no `index.html`**

4. **Gere os slides:**
```bash
python3 generate_slides.py
```

## 🎨 Tecnologias Utilizadas

- **HTML5** - Estrutura semântica
- **CSS3** - Estilos modernos com glassmorphism
- **Bootstrap 5.3** - Framework responsivo
- **Font Awesome 6.0** - Ícones
- **Python 3** - Geração automática de conteúdo
- **Cloudinary** - Hospedagem de imagens

## 📐 Arquitetura

### Sistema de Geração de Conteúdo

O coração do projeto é o `generate_slides.py`, que implementa:

1. **Parser de HTML** com regex para extrair informações das aulas
2. **Template Engine** simples usando f-strings do Python
3. **Atualização automática** de links nas páginas principais
4. **Nomenclatura padronizada** (Aula 01 → `aula01.html`)

### Fluxo de Dados

```
Página da Disciplina (HTML)
        ↓
   Parser Regex
        ↓
  Extração de Dados (título, descrição)
        ↓
  Template de Slides
        ↓
   Geração de HTML
        ↓
 Atualização de Links
        ↓
    Slide Final
```

## 🎯 Navegação nos Slides

- **Setas do Teclado**: ← (anterior) | → (próximo)
- **Botões na Interface**: Clique nos botões de navegação
- **5 Slides por Aula**:
  1. 📌 Capa com logo e título
  2. 📋 Agenda dos tópicos
  3. 💡 Conceitos iniciais
  4. 📖 Aprofundamento técnico
  5. ❓ Conclusão e dúvidas

## 🎨 Personalização

### Cores das Disciplinas

Edite em `css/style.css`:

```css
.bg-quality {
  background: linear-gradient(45deg, #FF512F, #DD2476);
}

.bg-logic {
  background: linear-gradient(45deg, #1fa2ff, #12d8fa, #a6ffcb);
}

.bg-tcc {
  background: linear-gradient(45deg, #833ab4, #fd1d1d, #fcb045);
}
```

### Template dos Slides

Modifique a constante `SLIDE_TEMPLATE` em `generate_slides.py` (linhas 32-196).

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍🏫 Autor

**Professor Afonso**
- Instituição: SENAC
- Cursos: TADS, Redes de Computadores, Ciência da Computação

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para:

1. 🍴 Fork o projeto
2. 🌿 Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. ✅ Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. 📤 Push para a branch (`git push origin feature/MinhaFeature`)
5. 🎉 Abra um Pull Request

## 📞 Suporte

Para dúvidas ou sugestões, abra uma [issue](https://github.com/seu-usuario/hub_aula_senac/issues) no GitHub.

---

⭐ **Se este projeto foi útil, considere dar uma estrela!**

Feito com ❤️ para a comunidade educacional do SENAC

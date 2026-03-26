# Python Learning Portfolio — Progressão Estruturada de POO, Algoritmos Numéricos e CLI Interativa

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Paradigma](https://img.shields.io/badge/Paradigma-POO%20%2B%20Funcional-purple.svg)]()

> Coleção de módulos Python cobrindo geração algorítmica de CPF com validação módulo 11, gerenciamento de restaurantes em duas arquiteturas progressivas (dict funcional → OOP com herança e propriedades), demonstrando a migração de estado global mutable para encapsulamento via `@property` e `@classmethod`.

---

## Diferencial de Engenharia

### Dualidade Arquitetural: Funcional com Estado Global vs. OOP Encapsulado

O repositório contém **duas implementações do mesmo domínio** (sistema de restaurantes), o que é pedagogicamente explícito mas revela uma progressão de design real:

**`Restaurante/app.py`** — arquitetura funcional com estado global:
- `restaurantes` é uma `list` de `dict` no escopo do módulo — estado mutável compartilhado entre todas as funções.
- Cada função recebe/modifica esse estado implicitamente, criando acoplamento total.
- A navegação é implementada via recursão (`voltar_ao_menu_principal` → `main()`), o que em execuções longas pode causar **stack overflow** por acumulação de frames.

**`Restaurante-POO/`** — arquitetura OOP com `@classmethod` e `@property`:
- `Restaurante.restaurantes` é um atributo de classe — o equivalente OOP de estado global, mas com escopo controlado pela classe.
- `@property ativo` encapsula a lógica de formatação do status (retorna `'⌧'` ou `'☐'`), separando representação de estado.
- `media_avaliacoes` como `@property` lazy — recalcula a média apenas quando acessado, sem cache, o que é correto para a escala atual.
- **Bug intencional de validação**: `receber_avaliacao` aceita notas apenas no intervalo `(0, 5]` — notas de 6 a 10 são silenciosamente descartadas, apesar do `app.py` chamar `receber_avaliacao('Gui', 10)`.

### Algoritmo de Validação CPF (Módulo 11)

`Gerador_CPF.py` implementa o algoritmo oficial da Receita Federal corretamente:
1. Gera 9 dígitos aleatórios.
2. Primeiro dígito verificador: soma ponderada com pesos decrescentes de 10 a 2, aplica `(soma × 10) % 11`; se resultado > 9, usa 0.
3. Segundo dígito verificador: repete com os 10 dígitos e pesos de 11 a 2.

A lógica está correta. O problema está na saída: `print(int(cpf))` converte a string para inteiro, eliminando zeros à esquerda em CPFs iniciados com 0.

---

## Stack Tecnológica

| Tecnologia | Justificativa Técnica |
|---|---|
| **Python 3.10+** | f-strings com `ljust()` para formatação tabular em CLI; match/case disponível mas não utilizado |
| **random** (stdlib) | `random.randint` para geração de dígitos — adequado para fins não-criptográficos; `secrets` seria necessário em contexto de segurança |
| **numpy** (Restaurante-POO) | Importado em `restaurante.py` (`from numpy.ma.core import max_val`) mas **nunca utilizado** — dependência órfã que aumenta o peso do ambiente sem função |
| **os** (stdlib) | `os.system('cls')` para limpeza de terminal — não-portável (falha silenciosamente em Linux/macOS); `os.system('clear')` seria o equivalente Unix |

---

## Arquitetura & Fluxo de Dados

### Módulo Restaurante-POO

```
app.py
  └── Restaurante('praça', 'Gourmet')     ← __init__ appenda em Restaurante.restaurantes[]
        ├── receber_avaliacao(cliente, nota)
        │     └── Avaliacao(cliente, nota) → self._avaliacao[]
        │           (nota validada: 0 < nota <= 5)
        └── Restaurante.listar_restaurantes()   ← @classmethod itera restaurantes[]
              └── restaurante.media_avaliacoes  ← @property calcula média sob demanda
```

### Módulo Restaurante (Funcional)

```
main()
  └── exibir_opcoes()
  └── escolher_opcao()
        ├── cadastrar_novo_restaurante() → restaurantes.append(dict)
        ├── listar_restaurantes()        → itera restaurantes[]
        ├── alternar_estado_restaurante() → busca linear por nome (case-sensitive)
        └── finalizar_app()
              └── voltar_ao_menu_principal() → main() [RECURSÃO — risco de stack overflow]
```

---

## Guia de Setup

```bash
# 1. Clone e crie ambiente virtual
git clone https://github.com/<seu-usuario>/python-portfolio.git
cd python-portfolio
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\Activate.ps1  # Windows

# 2. Instale dependências (apenas Restaurante-POO usa numpy)
pip install numpy

# 3. Execução por módulo
python Gerador_CPF/Gerador_CPF.py          # Gera e imprime um CPF
python Restaurante/app.py                   # CLI interativa (funcional)
python Restaurante-POO/app.py               # Listagem OOP (execução única)
```

> **Nota:** `Restaurante-POO/app.py` executa uma listagem estática e termina — não há loop interativo. O bloco `if __name__ == '__main__': main()` está correto, mas `main()` apenas chama `Restaurante.listar_restaurantes()`.

---

## Análise de Trade-offs

### Recursão vs. Loop para navegação de menu

`Restaurante/app.py` usa recursão para retornar ao menu principal (`voltar_ao_menu_principal` → `main()`). Em Python, o limite padrão de recursão é 1000 frames (`sys.getrecursionlimit()`). Uma sessão com ~500 navegações entre telas atingiria esse limite com `RecursionError`. A solução correta é um loop `while True` em `main()` com `break` na opção de saída — sem nenhuma perda de clareza e com complexidade de espaço O(1) em vez de O(n).

### `@classmethod` para registro de instâncias vs. padrão Registry explícito

Usar `Restaurante.restaurantes = []` como atributo de classe para rastrear todas as instâncias é um padrão válido para escopo pequeno, mas tem a desvantagem de ser **estado global de classe** — não há como criar dois conjuntos independentes de restaurantes sem modificar a classe. Um padrão Registry explícito (passando o registry como dependência no `__init__`) seria mais testável e desacoplado.

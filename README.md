# Acompanhamento de CR (Coeficiente de Rendimento)

Script desenvolvido em Python para calcular e acompanhar o desempenho académico ao longo dos períodos da graduação, exibindo o CR global, o rendimento isolado de cada semestre e o CR acumulado.

## Estrutura do Projeto

O código foi dividido em dois módulos para separar a lógica de cálculo dos dados das disciplinas:

* **`calculo_cr.py`**: Contém a classe `materia` (responsável por armazenar nome, créditos, nota e formatar a exibição) e a função `imp()`, que processa as listas de períodos e gera o relatório no terminal.
* **`meu_cr.py`**: Ficheiro de entrada onde as disciplinas são instanciadas, agrupadas por período e enviadas para cálculo.

## Como Executar

1. Certifique-se de que ambos os ficheiros (`calculo_cr.py` e `meu_cr.py`) estão na mesma pasta.
2. Edite o ficheiro `meu_cr.py` com as suas disciplinas, créditos e notas.
3. No terminal, execute:

```bash
python meu_cr.py

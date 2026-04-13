# :bar_chart: Pesquisa de Satisfação — TudoWeb ![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) ![Pesquisa](https://img.shields.io/badge/Pesquisa_de_Opinião-00BFFF?style=for-the-badge&logo=googleforms&logoColor=white) ![Atendimento](https://img.shields.io/badge/Avaliação:_1%7C2%7C3-32CD32?style=for-the-badge&logo=checkmarx&logoColor=white)

> Coleta e analisa o grau de satisfação de clientes com o atendimento da empresa TudoWeb, exibindo ao final a quantidade de respostas Excelente e Ruim.

---

## Sobre

Programa em **Python** que aplica uma pesquisa de atendimento ao cliente utilizando **estrutura de repetição FOR** e **estruturas de decisão**. Coleta nome, idade e opinião de cada entrevistado, classificando as respostas em **EXCELENTE**, **BOM** ou **RUIM**.

---

## Implementação

A lógica central utiliza um laço `for` para iterar sobre os entrevistados e acumular os resultados:

```python
def coletar_dados(self):
    for i in range(1, self.total + 1):
        opiniao = int(input("Opinião: "))

        if opiniao == 1:
            self.excelente += 1
        elif opiniao == 3:
            self.ruim += 1
```

A exibição do resultado final apresenta apenas as categorias extremas (Excelente e Ruim):

```python
def mostrar_resultado(self):
    print(f"Quantidade de EXCELENTE: {self.excelente}")
    print(f"Quantidade de RUIM: {self.ruim}")
```

A pesquisa padrão é configurada para **50 entrevistados**. Para testes, um modo alternativo executa com 10 entrevistados pré-definidos:

```python
pesquisa = Pesquisa(50)
```

---

## Como executar

```bash
git clone https://github.com/sart-mercyy/pesquisa-tudoweb.git
cd pesquisa-tudoweb
python app.py
```

---

## Exemplo de uso

```
Digite 't' para teste ou qualquer tecla para execução normal: 

Entrevistado 1
Nome: Ana
Idade: 20
Avaliação:
1 - EXCELENTE
2 - BOM
3 - RUIM
Opinião: 1
...
# (Entrevistado 50)

RESULTADO FINAL 
Quantidade de EXCELENTE: 27
Quantidade de RUIM: 12
```

### Modo de teste (10 entrevistados)

```
Digite 't' para teste ou qualquer tecla para execução normal: t

TESTE COM 10 ENTREVISTADOS

RESULTADO FINAL
Quantidade de EXCELENTE: 5
Quantidade de RUIM: 2
```

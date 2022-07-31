## Regressão Linear
![Badge de licença](http://img.shields.io/static/v1?label=LICENÇA&message=GNU&color=sucess&style=for-the-badge)   ![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=sucess&style=for-the-badge)   ![Badge versionamento](http://img.shields.io/static/v1?label=VERSAO&message=1.0&color=sucess&style=for-the-badge)

### Sobre

&emsp;O projeto tem como objetivo fornecer um gráfico com os dados e a regressão linear plotados a partir de um arquivo `.csv`. O arquivo com os dados deve ser salvado no diretório regressao_linear, junto ao main.py, com o nome `dados.csv`

### Bora ver como o projeto ficou?

![regressao_linear](https://user-images.githubusercontent.com/87876734/182035102-00be955b-2d56-481f-aecd-79b617124583.png)

### Pré-requisitos

  - Python >= 3.8
  
### Instalação
  
    # Clone o repositório
    >> mkdir regressao_linear
    >> git clone https://github.com/ArandaCampos/regressao_linear.git regressao_linear/

    # Crie um ambiente virtual
    >> cd regressao_linear
    >> virtualenv .
    >> source bin/activate

    # Instale as dependências
    (regressao_linear) >> pip install -r requirements.txt
    
    # Rode o código
    (regressao_linear) >> cd regressao_linear/
    (regressao_linear) >> python main.py
  
### Tecnologias empregadas
  - Python
  - Matplotlib
  - Pytest
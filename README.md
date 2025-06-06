# Projeto Integrador III - <i>Contador de Calorias e Macronutrientes</i>

### Sobre
Webservice de contagem de calorias e macronutrientes. 

### Instruções
1. Abra um terminal e, na pasta destino, execute o comando ``git clone https://github.com/fernandapirateli/PI-3.git``
2. É recomendável criar e ativar ambiente virtual;
3. Instale as dependências executando ``pip install -r requirements.txt``
4. Certifique-se de que o arquivo **.env** esteja dentro do diretório ***backend***. 

### Execução
0. Acessar o diretório backend ``cd backend``
1. Enquanto objetos estão sendo adicionados ou alterados em algum arquivo app/model.py, 
será preciso executar o comando ```python manage.py migrate```. 
2. Para iniciar o servidor de desenvolvimento, use o comando ``python manage.py runserver``
3. Abra o navegador e insira ***localhost:8000*** na barra de endeços.

### Base de dados de alimentos

Para popular a tabela de alimentos* basta executar o comando ```python manage.py load_ibge_data``` e aguardar.
Caso o banco de dados seja em nuvem, pode requerer mais tempo.

Normalmente, essa é uma ação a qual deve ser executada somente uma vez.

### Tabela IBGE de Alimentos 
Trata-se de uma versão resumida das tabelas de composição nutricional dos alimentos consumidos no Brasil / IBGE.
A qual lista os valores de energia, macronutrientes e fibra de diversos alimentos.
* [Tabela IBGE de Alimentos](https://biblioteca.ibge.gov.br/visualizacao/livros/liv50002.pdf)

### Dependências
* [Framework Django](https://pypi.org/project/Django/)
* [Biblioteca Environ](https://pypi.org/project/python-environ/)


### Amostra de Estrutura

|\projeto<br>
|---\backend<br>
|---------\source (configurações do Django)<br>
|---------------\settings.py<br>
|---------\apps (aplicativos Django)<br>
|---------\manage.py<br>
|---\frontend<br>
|---------\static<br>
|---------------\css<br>
|---------------\img<br>
|---------\templates<br>
|---------------\partials<br>
|---------------\base.html<br>
|---\.gitignore<br>
|---\README.md<br>
|---\requirements.txt

### Dicas e Contribuições
* Os commits deste projeto busca seguir (não de forma estrita) o modelo de [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/);
* Antes de efetuar alterações/contribuições no código, certifique-se de efetuar um ```git pull``` para trabalhar com a 
versão mais atualizada do código fonte, e diminuir as chances de erros;
* Elabore commits incrementais, a cada nova feature implementada, conjunto de arquivos inseridos ou erros corrigidos. 
Possibilita melhor detecção, isolamento e mitigação de falhas e erros;
* Mantenha atualizado, na medida do possível, a lista de tarefas (***TODO.md***). Marcando com um **x** as tarefas 
concluídas.
Ajuda a ter uma visão do andamento do projeto. :wink:
# API_Python

Esse repositório mostra alguns codigos de como chamar uma api ou fazer uma api com Python. Neste repositório você pode encontrar como ler uma api e transformar em dataframe suas informações, criar uma api com os conceitos de CRUD. Qualquer dúvida, sinta-se à vontade para me chamar no [linkedin](https://www.linkedin.com/in/paulo-oliveira-a6650121a/).

## Descrição sobre cada file
- Api_Read - O "Api_Read", tem como função chamar uma api via python e trazer as informações em um dataframe;
- Get - Nesta parte eu mostro um dos fundamentos do CRUD que seria o READ, assim fazendo a sua api conectar em seu banco usando mysql e trazendo as informações selecionadas por você;
- Delete - No CRUD este seria o Delete, sua função será deletar a linha de acordo com a coluna seleciona por você em que a informação bata, excluindo diritamente do banco;
- Post - O Post será o Create, a criação de uma linha dentro do banco com as informações cedidas pelo úsuario;
- Put - E o Put que será o Update, atualizando as informações de acordo com a chave selecionada e as informações escolhidas para atualizar.
  
## Funções Base
#### - Conexão DB
~~~
conn = mysql.connector.connect(
    host="endpoint",  
    user="login", 
    password="senha",
    database="banco"
)
~~~
#### - Definição da rota e metodo
~~~
@app.route('/nome_rota', methods=['metodo'])
~~~

# Projeto Curb
## Introdução
O **projeto Curb** da matéria Projeto Integrador 2 da Universidade de Brasília visa automatizar a tarefa de pintar meio-fios, realizando-a demaneira eficiente, resultando na diminuição dos desperdícios de tinta e, consequentemente,de gastos. 
Este repositório contém a estrutura de backend do projeto, que foi estruturado usando a arquitetura de microserviços. 

## Microserviços
- Serviço de Controle
    O serviço de controle é responsável por receber os comandos de ligar e desligar vindos do app mobile e intermediar para o carrinho.
- Serviço de Monitoramento
    O serviço de monitoramento é responsável por coletar os dados dos sensores do carrinho e organizá-los para enviar à API.
- Serviço de Armazenamento
    O serviço de armazenamento é responsável por inserir os dados de relatório em um banco de dados, uma vez que no nosso contexto é interessante manter em persistência esses dados.
- Serviço de Relatório
    O serviço de relatório é responsável por montar o documento com as informações da API.
- Serviço de Comunicação
    O serviço de comunicação intermedia os microserviços com o carrinho através do protocolo HTTP.

Para gerenciar a configuração e deploy desses microserviços é utilizado o **Docker**.
Cada seviço é empacotado em um container para que o deploy possa ser feito atomicamente para cada um, assim é possível uma evolução separada.

![Imgur](https://i.imgur.com/mfCck4Y.png)

## Rodando o projeto
Para rodar o projeto basta realizar os seguintes passos no terminal:
```
git clone https://github.com/pi2-fga/2019-01-Curb-Back-end.git
```
Executar o comando abaixo para instalar os pré-requisitos do ambiente:
```
pip install -r requirements.txt
```
Entre na pasta api:
```
cd api/
```
Por fim, execute o comando:
```
python manage.py runserver
```

## Deploy:

O deploy da api está disponével em:
```
http://gustavo2795.pythonanywhere.com/
```


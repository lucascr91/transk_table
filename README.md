# transk table
*Um implementação em GUI para auxiliar na transcrição de tabelas antigas*

![alt text](https://github.com/lucascr91/transk_table/blob/master/maranhao.jpg)


Esse programa é uma simples implementação em [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) de um _workflow_ que desenvolvi para transcrever tabelas de censos antigos brasileiros. Do ponto de vista computacional, a GUI não faz mais do que usar a tecnologia do módulo [tabular](https://github.com/chezou/tabula-py) do python. Dessa forma, a facilidade oferecida pela GUI representa um avanço modesto se você já programa em python.

De todo modo, a aplicação irá interessar aqueles que _i)_ não programam em python (ou em outra linguagem com aplicação do tabular) e/ou _ii)_ procuram por uma ferramenta para realizar as transcrições de forma semi-automática sem ter que lhe dar com código fonte.

<!-- Essa breve apresentação da ferramenta está dividida em três seções. Na seção seguinte ~mostramos o funcionamento do programa. A ideia dessa seção é, antes de discutir instalação e limitações, mostrar ao usuário o que é o programa e o que ele faz. Mostramos como rodar o programa na seção 3, enquanto uma discussão sobre melhorias potenciais e manutenção do programa são arroladas na seção 4. -->


### Como o **transk table** funciona:

#### Workflow

Para entender o funcionamento do **transk table** é útil entender antes o _workflow_ em que se baseia o programa. O _workflow_ de transcrição é definido pelos seguintes passos:

1) **Ler a tabela usando tabular**: o _output_ desse primeiro passo é a tabela "bruta". É uma leitura que, normalmente, acerta o valor da maioria das células, mas têm duas falhas. Em primeiro lugar, o tabula erra sistematicamente o número de linhas e colunas da tabela em questão. Além disso, muitas células são preenchidas de forma errada, com trocas de 1 por ! ou mesmo sem nenhum preenchimento onde havia informação.
2) **Arrumar número de linhas e colunas**: o segundo passo corrige a primeira limitação da leitura do tabula relatada acima. Assim, esse passo consiste em arrumar manualmente o número de linhas e colunas usando um programa simples de planilhas como excel ou o calc (libreoffice).
3) **Checar valores**: o terceiro passo consiste em checar célula por célula se os valores na tabela estão corretos e preencher/substituir quando não tiverem

#### GUI

### ATENÇÃO: O pdf deve estar com OCR para funcionar

Para usar a GUI, o usuário deve ter no seu computador um documento em pdf onde estão as tabelas que ele pretende transcrever.

Na atual versão, o **transk table** tem apenas uma janela dividida em dois _frames_, como pode ser visto na figura abaixo:

![alt text](https://github.com/lucascr91/transk_table/blob/master/gui_tt.png)

O **transk table** transcreve uma tabela por vez, então para iniciar a transcrição o usuário deve definir o número da página onde está a tabela de interesse e clicar em *open* **depois** para abrir o documento. Após a seleção do documento o **transk table** vai criar uma pasta cujo nome será dado pelo número da página. Dentro dessa pasta será salvo um arquivo em csv chamado "DDD_page.csv", onde DDD é o número da página. O arquivo "DDD_page.csv" é a transcrição bruta feita pelo tabular. Dessa forma, a simples definição da página e abertura documento encerra o passo 1.

Para a consecução do passo 2 o usuário precisa clicar em *Open Excel Sheet* (usuários de Windows) ou *Open Calc sheet* (usuários de Linux). O **transk table** abrirá então o "DDD_page.csv". Aberto esse arquivo, o usuário deve corrigir o número de linhas e colunas, salvar o arquivo e fechar. Após esse fechar o arquivo, o usuário deve clicar em *Clean*. Esse botão elimina todas as entradas diferentes de números, desconsiderando as informações da primeira coluna. 

Por fim, a última eta consistem em digitar no terminal dentro da GUI o seguinte comando:

```
python corrections.py DDD
```
Em que DDD é o número da página para a qual você quer fazer a conferência.

Será então iniciado um "jogo" em que o computador irá lhe apresentar os valores de cada célula e você terá que responder se aquele valor é válido ou não. Se for válido apenas clique em enter. Se precisar substituir responda de acordo. O jogo é auto-explicativo e irá salvar automaticamente todas as alterações que você implementar durante as respostas em um arquivo chamado "DDD_page_final.csv" na respectiva pasta. A correção é feita por coluna. Quando terminar todas as colunas, simplesmente clique em *Quit*. A transcrição da tabela estará pronta.


### Como instalar e rodar o transk table no seu computador:

#### Requisitos

Para instalar e rodar o *transk table* no seu computador você irá precisar ter instalado o python 3, alguns pacotes dessa linguagem que serão detalhados mais adiante, além de acesso ao terminal. A forma mais conveniente de se instalar o python com os pacotes necessários para rodar o *transk table* é instalar o [Anaconda](https://www.anaconda.com/products/individual). A instalação é simples e pode ser feita após o download do instalador no site do _software_ .Para os usuários de Windows recomendo baixar alguma das versões anteriores do Anaconda (digamos, 3.5). Versões mais recentes do Anaconda têm apresentado incompatibilidades com o Windows.

Depois de instalado o Anaconda, abra o terminal do seu computador e digite:

```
pip install tabula-py
```

Esse é o único pacote que não vem instalado no Anaconda. Caso você tenha instalado o python de outra forma certifique-se de que sua instalação possui os seguintes módulos: pandas, numpy, ttkthemes e tkinter.

#### Iniciando o transk table

Com a instalação completa, você poderá iniciar o *transk table* seguindo apenas dois passos:

1) Faça o download desse repositório, extraia a pasta para um local de preferência em seu computador
2) Entre na pasta pelo terminal (por exemplo, se a pasta do programa foi extraída na sua pasta de Downloads, digite no terminal `cd Downloads/transk_table` e tecle Enter) e rode:

```
python app.py
```

### Melhorias futuras

A versão atual do *transk table* é completamente funcional e você poderá fazer transcrições de tabelas em imagens de baixa resolução de forma organizada e semi-automática. No entanto, a atual versão têm o imenso inconveniente de não ter a imagem da  tabela que está sendo transcrita dentro de GUI. Essas e outras limitações serão corrigidas na segunda versão. Se você tem interesse em contribuir veja a pasta *second_version*. Esta pasta contém o código atual da segunda versão que está sendo desenvolvida, bem como um documento que lista possíveis melhorias a serem incorporadas.

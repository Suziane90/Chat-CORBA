# Chat-CORBA
Repositorio dedicado para o trabalho final da disciplina Sistemas Distribuidos

## Links:

<a href="https://www.youtube.com/watch?v=H2ulmH_WWpQ">Vídeo da aplicação funcionando</a>
<br>
<a href="https://trello.com/invite/b/e0APAaHU/ATTI0700b71c20bc8478ae28453d405c12ee7B638232/controle-de-tarefas">Nosso Trello</a>

### 1. Crie e ative um ambiente CONDA em ambos os computadores:

    conda create -n omni-env -c conda-forge python=3.10 omniorb omniorbpy

    conda activate omni-env

### 2. Gere o código Python do arquivo IDL em ambos os computadores:

    omniidl -bpython chat.idl

### 3. Execute o serviço OmniORB em ambos os computadores:

    omniNames -start

### 4. Execute o servidor em um computador:

    python servidor.py

### 5. Execute o cliente em outro computador:

    python cliente.py

### 6. Insira o IOR obtido no terminal do servidor no primeiro computador (etapa 4):

    Insira o IOR do objeto Saudações:

    IOR:010000001a...

# **URL Check Tool**

```plaintext
██╗   ██╗██████╗ ██╗              ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗     ████████╗ ██████╗  ██████╗ ██╗     
██║   ██║██╔══██╗██║             ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝     ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║   ██║██████╔╝██║             ██║     ███████║█████╗  ██║     █████╔╝         ██║   ██║   ██║██║   ██║██║     
██║   ██║██╔══██╗██║             ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗         ██║   ██║   ██║██║   ██║██║     
╚██████╔╝██║  ██║███████╗███████╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║   ╚██████╔╝╚██████╔╝███████╗
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝    ╚═════╝  ╚═════╝ ╚══════╝                                                                                                             
```

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

O **URL Check Tool** é uma ferramenta desenvolvida em Python que verifica a funcionalidade de URLs em um arquivo de entrada. Ele filtra as URLs que retornam status HTTP `200 OK` ou redirecionamentos (`3xx`) e salva as URLs funcionais em um arquivo de saída.

## **Recursos**
- Verifica se as URLs estão funcionando (HTTP 200 ou redirecionamento).
- Ignora avisos de SSL não verificados.
- Processa múltiplas URLs rapidamente.
- Suporta personalização de User-Agent e timeout.
- Gera um arquivo de saída com as URLs funcionais.
- Exibe um banner estilizado ao iniciar o programa.

---

## **Requisitos**

### **Dependências**
Certifique-se de ter as seguintes bibliotecas instaladas:

- `requests`: Para realizar requisições HTTP.
- `colorama`: Para exibir mensagens coloridas no terminal.

Instale as dependências usando o comando abaixo:

```bash
pip install -r requirements.txt
```
## **Compatibilidade**
Python 3.6 ou superior.
Funciona em sistemas operacionais Windows, Linux e macOS.

## **Como Usar**
1. Executando o Script
Para usar o URL Check Tool , execute o script no terminal com os argumentos necessários:

```bash
python url_check_tool.py -i urls.txt -o working_urls.txt --user-agent "Mozilla/5.0" --timeout 15
```

## **2. Argumentos**
Os argumentos aceitos pelo script são:

| Argumento         | Descrição                                                                 |
|--------------------|---------------------------------------------------------------------------|
| `-i`, `--input`    | Arquivo contendo a lista de URLs (uma por linha).                         |
| `-o`, `--output`   | Arquivo onde as URLs funcionais serão salvas.                            |
| `--user-agent`     | Define o User-Agent para as requisições HTTP (opcional).                  |
| `--timeout`        | Define o tempo limite para as requisições em segundos (padrão: 10).       |
| `--no-banner`      | Oculta o banner ao iniciar o programa (opcional).                         |

## **3. Exemplo de Uso**
Suponha que você tenha um arquivo chamado urls.txt com as seguintes URLs:


1. https://google.com
2. https://example.com
3. http://invalid-url.test

Execute o script:
```bash
python url_check_tool.py -i urls.txt -o working_urls.txt --timeout 15
```

Após a execução, o arquivo working_urls.txt conterá apenas as URLs funcionais:
https://google.com
https://example.com


# **Funcionamento Interno**
## 1. Verificação de URLs
O script tenta acessar cada URL fornecida no arquivo de entrada usando a biblioteca requests. Ele verifica se o status HTTP é:

200 OK: A URL está funcionando corretamente.
3xx: A URL foi redirecionada.
Caso contrário, a URL é ignorada.

## 2. Tratamento de Erros
O script trata os seguintes erros de forma silenciosa:

Timeout: Quando a URL não responde dentro do tempo limite.
SSL: Quando há problemas com certificados SSL.
Conexão: Quando ocorre falha na conexão com o servidor.

## 3. Processamento Paralelo
Para melhorar o desempenho ao processar muitas URLs, o script utiliza threads (concurrent.futures.ThreadPoolExecutor) para verificar várias URLs simultaneamente.

## **Exemplo de Saída**
Ao executar o script, você verá mensagens no terminal informando o progresso:

```
[+] URL funcionando (200 OK): https://google.com
[+] URL redirecionada (301): https://example.com
[-] Falha de conexão ao acessar: http://invalid-url.test
[INFO] URLs funcionais foram salvas em 'working_urls.txt'.
```
### **Contribuição**
Contribuições são bem-vindas! obrigado.

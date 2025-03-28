import requests
import argparse
import warnings
from colorama import Fore, Style, init
import os
# Inicializa o colorama para funcionar corretamente no Windows
init(autoreset=True)
# Ignora os avisos de SSL não verificado
os.system("clear")


def banner():
        print(f"""
{Fore.BLUE + Style.BRIGHT}
██╗   ██╗██████╗ ██╗              ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗     ████████╗ ██████╗  ██████╗ ██╗
██║   ██║██╔══██╗██║             ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝     ╚══██╔══╝██╔═══██╗██╔═══██╗██║
██║   ██║██████╔╝██║             ██║     ███████║█████╗  ██║     █████╔╝         ██║   ██║   ██║██║   ██║██║
██║   ██║██╔══██╗██║             ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗         ██║   ██║   ██║██║   ██║██║
╚██████╔╝██║  ██║███████╗███████╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║   ╚██████╔╝╚██████╔╝███████╗
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝    ╚═════╝  ╚═════╝ ╚══════╝


        {Style.RESET_ALL}
                                        {Fore.RED + Style.BRIGHT}       URL CHECK TOOL{Style.RESET_ALL}
                                        {Fore.YELLOW}    VERIFY AND FILTER URLS{Style.RESET_ALL}

BY: RAF4BR
        """)
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

def check_url(url, user_agent, timeout):
    """
    Verifica se uma URL está funcionando.
    Retorna True se a URL retorna status 200 ou 3xx, False caso contrário.
    """
    headers = {
        "User-Agent": user_agent
    }
    try:
        # Desativa a verificação de certificado SSL e adiciona o User-Agent
        response = requests.get(f"https://{url}", timeout=timeout, verify=False, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            print(f"[+] URL funcionando (200 OK): {url}")
            return True
        elif 300 <= response.status_code < 400:
            print(f"[+] URL redirecionada ({response.status_code}): {url}")
            return True
        else:
            # Não imprime URLs com status diferente de 200 ou 3xx
            return False
    except requests.exceptions.Timeout:
        # Não imprime timeouts
        return False
    except requests.exceptions.SSLError:
        # Não imprime erros de SSL
        return False
    except requests.exceptions.ConnectionError:
        # Não imprime erros de conexão (ex.: falha ao resolver nome de domínio)
        return False
    except requests.exceptions.RequestException:
        # Não imprime outros erros de requisição
        return False

def process_urls(input_file, output_file, user_agent, timeout):
    """
    Processa uma lista de URLs, verifica quais estão funcionando,
    e salva as URLs funcionais em um novo arquivo.
    """
    working_urls = []

    try:
        # Lê o arquivo de entrada com as URLs
        with open(input_file, "r") as file:
            urls = file.readlines()

        # Verifica cada URL
        for url in urls:
            url = url.strip()  # Remove espaços em branco e quebras de linha
            if url:  # Ignora linhas vazias
                if check_url(url, user_agent, timeout):
                    working_urls.append(url)

        # Salva as URLs funcionais no arquivo de saída
        with open(output_file, "w") as file:
            for url in working_urls:
                file.write(f"{url}\n")

        print(f"[INFO] URLs funcionais foram salvas em '{output_file}'.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

def main():
    #BANNER
    banner()

    #help
    parser = argparse.ArgumentParser(description="Separa URLs funcionais de uma lista.")
    parser.add_argument("-i", "--input", required=True, help="Arquivo contendo a lista de URLs (uma por linha)")
    parser.add_argument("-o", "--output", required=True, help="Arquivo para salvar as URLs funcionais")
    parser.add_argument("--user-agent", default="Mozilla/5.0 (compatible; FilterURLsBot/1.0)",
                        help="User-Agent string to use in requests")
    parser.add_argument("--timeout", type=int, default=10, help="Timeout em segundos para as requisições (padrão: 10)")
    args = parser.parse_args()

    process_urls(args.input, args.output, args.user_agent, args.timeout)

if __name__ == "__main__":
    main()

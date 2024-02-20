# find-phones

O projeto é um web crawler simples em Python que encontra e extrai números de telefone de um site a partir de uma URL de entrada. O programa utiliza a biblioteca Requests para fazer requisições HTTP e a biblioteca BeautifulSoup para analisar o HTML da página em busca dos números de telefone.

## Funcionalidades

- **Web Crawler**: O programa realiza um crawling no site especificado na URL de entrada em busca de números de telefone.
- **Utilização de Threads**: O usuário pode especificar o número de threads para aumentar a eficiência da busca dos telefones.
- **Armazenamento dos Resultados**: Os números de telefone encontrados são armazenados em um arquivo de texto para uso posterior.

## Como Usar

1. Clone o repositório: `git clone https://github.com/LucasKaliLinux/find-phones.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o programa: `python find_phones.py <URL> <num_threads>`

## Exemplo de Uso

```bash
python find_phones.py https://exemplo.com 5

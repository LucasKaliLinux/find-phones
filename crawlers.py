import sys
import re
import threading

import requests
from bs4 import BeautifulSoup

LINKS = []
TELEFONES = []

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print(f"Erro: {resposta.status_code}")
    except Exception as erro:
        print("Erro ao fazer a requisicao")
        print(erro)


def parsing(resposta):
    try:
        soup = BeautifulSoup(resposta, "html.parser")
        return soup
    except Exception as Error:
        print("Error no parsing")
        print(Error)


def encontrar_links(soup):
    try:
##        cards_pai = soup.find("div", "ui three doubling link cards")
##        cards = cards_pai.find_all("a")
        cards = soup.find_all("a")
    except:
        print("Falha ao encontra o link")
        return None

    links = []
    for card in cards:
        try:
            link = card['href']
            links.append(link)
        except:
            print("ERRO ao encontrar links")

    return links

def encontrar_telefone(soup):
    try:
        descricao = soup.prettify()
    except:
        print("Erro ao encontrar descricao")
        return None

    regex = re.findall(r"\(?0?([1-9]{2})[ \-\.\)]{0,2}(9[ \-\.]?\d{4})[ \-\.]?(\d{4})", descricao) #RAW
    if regex:
        return regex


def descobrir_telefones():
    while True:
        try:
            link = LINKS.pop(0)
        except:
            return

        if link.startswith("http"):
            resposta = requisicao(link)
        else:
            resposta = requisicao(URL + link)

        if resposta:
            soup = parsing(resposta)
            if soup:
                telefones = encontrar_telefone(soup)
                if telefones:
                    for telefone in telefones:
                        print("Telefone encontrado", telefone)
                        TELEFONES.append(telefone)
                        salva_telefones(telefone)


def salva_telefones(telefone):
    string_telefone = "{}{}{}\n".format(telefone[0], telefone[1], telefone[2])
    try:
        with open("telefones.txt", "a") as arquivo:
            arquivo.write(string_telefone)
    except Exception as Erro:
        print("Erro ao salvar arquivo")
        print(Erro)


if __name__ == "__main__":
    try:
        URL = sys.argv[1]
        threads = sys.argv[2]
        resposta_busca = requisicao(URL)
        if resposta_busca:
            soup_busca = parsing(resposta_busca)
            if soup_busca:
                LINKS = encontrar_links(soup_busca)

                THREADS = []
                for i in range(int(threads)):
                    t = threading.Thread(target=descobrir_telefones)
                    THREADS.append(t)
            
                for t in THREADS:
                    t.start()

                for t in THREADS:
                    t.join()

                print(TELEFONES)
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception:
        print("python file.py <url> <threads>")

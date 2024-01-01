# Scrap_Forever

Get all links in all pages in one application


## Scap Forever

- [x] Scrap Forever realiza o Get de todos os links em uma aplicação e navega nas demais páginas para garantir que não fique nenhum link pra trás.


## Principais opções

* `-t` URL          https://site.com.br

* `-o` Output File --output SCRAP_OUT Salva data

* `-p` Proxy --proxy SCRAP_PROXY  (-p http://127.0.0.1:8080)

* `-n` Threads, -n 10

### USAGE


```bash
$ python3 scrap_forever.py -t https://site.com.br -o output.txt

$ python3 scrap_forever.py -t https://site.com.br -o output.txt -n 20
```
```bash
$ python3 scrap_forever.py -t https://site.com.br -o output.txt -p http://127.0.0.1:8080

$ python3 scrap_forever.py -t https://site.com.br -o output.txt -p http://127.0.0.1:8080 -n 20
```

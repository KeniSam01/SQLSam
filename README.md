# sqlsam
simples scan para busca de erros de sql injection em sites

# Install
## Linux

git clone https://github.com/KeniSam01/SqlSam/

# Examples

### Para ajuda

python sqlsam.py -h 

### Procurando falha

python sqlsam.py -u www.github.com/noticias.php?id=123344

### Procurando falha²

python sqlsam.py --url www.github.com/noticias.php?id=123344

# SqlSam
simples scan para busca de erros de sql injection em sites

# Install & Use
## Linux

$ pip install requesocks

$ git clone https://github.com/KeniSam01/SqlSam/

$ cd SqlSam/

$ python sqlsam.py 'args'

# Examples

### Para ajuda

python sqlsam.py -h 

### Procurando falha

python sqlsam.py -u www.github.com/noticias.php?id=123344

### Procurando falha²

python sqlsam.py --url www.github.com/noticias.php?id=123344

### Procurando falha utilizando a rede TOR

python sqlsam.py -u www.github.com/noticias.php?id=123344 --tor yes

### Demonstration:

https://youtu.be/Lb1YZiW4X54

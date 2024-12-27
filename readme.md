Este programa se trata de um transcritor da Língua Brasileira de Sinais (Libras) para texto escrito.

Para isso, foi feito um treinamento com imagens de um dataset com fotos de 21 gestos diferentes em Libras.
Sendo as letras do alfabeto com exceção de H, J, K, X e Z. O arquivo best.pt é o resultado desse treinamento.
Para utilizar a aplicação, deve-se instalar o OpenCV e o Ultralytics (contendo o YOLO) através do terminal.

pip install opencv-python
pip install ultralytics

Após isso, apenas execute o libras2text.py. Na minha máquina, foi utilizado Python 3.12.4 para executar.
Após conseguir executar, recomenda-se um fundo limpo na imagem, para evitar problemas de detecção de gestos.

Utilização:

Ao executar, o modo automático de escrita estará ativado, o que significa que ao ser detectado o mesmo sinal na câmera por
aproximadamente 3 segundos, a letra correspondente será escrita no terminal, caso antes de completar os 3 segundos, o gesto
não seja mais detectado, a contagem de segundos é zerada, para evitar de escrever o que não se deseja.

Comandos:

M - Troca para o modo manual de escrita, neste modo, é necessário fazer o gesto e apertar ENTER no teclado, para que a letra seja escrita no terminal.
BACKSPACE - Apaga uma letra do terminal.
L - Limpa o texto que estava sendo escrito.
A - Troca para o modo automático de escrita.
Q - Fecha a aplicação.
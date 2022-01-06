import os
from google.colab import drive

drive.mount('/content/drive')
os.chdir('/content/drive/My Drive/Gmail')
!pip install detecto
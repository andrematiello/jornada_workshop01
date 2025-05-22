import site

print(site.getsitepackages())

# D:\Onedrive\pessoal\desenvolvimento\cursos\curso-jornada-dados\jornada_dados\3-como-estruturar-do-zero\workshop\.venv\Lib\site-packages
#'C:\\Users\\matie\\.pyenv\\pyenv-win\\versions\\3.11.4\\Lib\\site-packages'

import sys

for path in sys.path:
    print(path)

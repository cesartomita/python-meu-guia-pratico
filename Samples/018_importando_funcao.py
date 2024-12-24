# Exemplo para importar um arquivo Python quando o nome do arquivo começa com um número.

import importlib.util
import sys

# Defina o caminho do arquivo
file_name = "017_exportando_funcao.py"
module_name = "somar"

spec = importlib.util.spec_from_file_location(module_name, file_name)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)

# Agora você pode usar as funções ou classes do módulo
print(module.somar(1,1))
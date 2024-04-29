" Arquivo de Configuração"

import os
local_path = os.path.abspath(os.getcwd())
data_path = os.path.dirname(local_path)

configs = {
    "meta_path": f"{local_path}/python/scripts/metadado.xlsx",
    "raw_path": f"{local_path}/python/scripts/data/raw/raw_",
    # "raw_path": f"{local_path}/data/raw/raw_",
    }

#"work_path": f"{local_path}/data/work/work_cadastro.csv",
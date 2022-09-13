import pytest

from modelo_regressao.config.core import config
from modelo_regressao.processamento.gerenciador_dados import carregar_dataset

# Decorador pytext.fixture colhe tudo necessário para a preparação do teste, 
# exceto o teste em si
@pytest.fixture()
def amostra_input():
    return carregar_dataset(nome_arq=config.app_config.arquivo_teste)

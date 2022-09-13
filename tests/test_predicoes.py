import math

import numpy as np

from modelo_regressao.predicao import predizer

def test_predicoes(amostra_input):
    # dado que o dataset de teste tem 697 elementos:
    expected_no_predictions = 697

    resultado = predizer(dados_entrada = amostra_input)
    predicoes = resultado.get("predicoes")
    
    # Assegurar os tipos de dados na saída da pipeline
    # E que o número de predições esperado seja igual ao observado
    assert isinstance(predicoes, list)
    assert isinstance(predicoes[0], np.float64)
    assert len(predicoes) == expected_no_predictions

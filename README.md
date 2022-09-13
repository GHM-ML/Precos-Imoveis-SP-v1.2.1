# Precos-Imoveis-SP
Modelo de Regressão para predição dos preços de imóveis em São Paulo - SP
O projeto foi criado para fins de aprendizado em Machine Learning, empacotamento e distribuição de programa
É baseado na submissão pessoal do projeto Imersão Dados 4 da Alura Cursos.

## Treinamento
```Shell 
# Para apenas treinar o modelo, garanta primeiro a instalação do gerenciador de automação tox em: 
# https://tox.wiki/en/latest/install.html
# Execute o código:
tox -e train
```
## Teste
```Shell
# Para treinar e testar o desempenho no conjunto de teste, execute:
tox -e test_package

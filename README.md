# Recibo Automático Generator

Este script em Python utiliza a biblioteca Selenium para automatizar a geração de recibos online de arrendamento, específicos para o Portal das Finanças em Portugal. O processo de geração é realizado mês a mês, permitindo que o usuário especifique o intervalo desejado.

## Pré-requisitos

Certifique-se de ter o seguinte instalado antes de executar o script:

- Python 3.x
- Selenium
- ChromeDriver
- Bibliotecas adicionais: `pyautogui`

## Configuração

1. **Credenciais de Login:**
   - Insira seu nome de usuário e senha nas linhas correspondentes do script.
   
2. **Driver do Chrome:**
   - Verifique se o caminho para o ChromeDriver (`chrome_driver_path`) está corretamente configurado no seu sistema.

3. **Intervalo de Datas:**
   - Durante a execução, o script solicitará ao usuário os meses inicial e final para os quais os recibos serão gerados.

## Utilização

1. Execute o script e forneça as informações solicitadas.
2. O script abrirá o navegador, realizará o login, e navegará até o formulário de geração de recibos no Portal das Finanças.
3. Para cada mês no intervalo especificado, o script preencherá as informações necessárias e emitirá o recibo.
4. O recibo gerado será aberto em uma nova aba do navegador para impressão.
5. Após imprimir ou salvar o recibo, feche a aba para permitir a continuação do processo para o próximo mês.

## Observações

- Certifique-se de manter a página do Portal das Finanças aberta e o navegador visível enquanto o script estiver em execução.
- Caso ocorram alterações no layout do Portal das Finanças, o script pode precisar ser ajustado.

**Nota:** Este script foi desenvolvido para fins educacionais e pode ser sujeito a alterações no futuro. Use-o de acordo com os regulamentos e políticas do Portal das Finanças.

**Importante:** O uso de automação em sites pode violar os Termos de Serviço do site. Certifique-se de estar em conformidade com as políticas do Portal das Finanças antes de utilizar este script de forma contínua.

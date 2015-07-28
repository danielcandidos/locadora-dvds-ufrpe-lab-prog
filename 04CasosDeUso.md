![http://images.orkut.com/orkut/photos/RAAAAL6N_EG4TSviVRH2jlCw82tiST2m_5fC0C_yiOjsPvr3sinYIVlmpcFXvSeOPjZjNsLxjyTZzOGw-1z4VKoy_yjnJ4CBW8_-7v5O387Xu5eDAJtU9VADcXl04yo3YZtwgc5G0bAOrqykNw.jpg](http://images.orkut.com/orkut/photos/RAAAAL6N_EG4TSviVRH2jlCw82tiST2m_5fC0C_yiOjsPvr3sinYIVlmpcFXvSeOPjZjNsLxjyTZzOGw-1z4VKoy_yjnJ4CBW8_-7v5O387Xu5eDAJtU9VADcXl04yo3YZtwgc5G0bAOrqykNw.jpg)

# UC0001 - Acervo de Filmes #
<table cellpadding='5' border='1' cellspacing='5' width='595'>
<tr>
<td width='20%'> <b>Objetivos</b> </td>
<td width='80%'> Cadastrar, remover e alterar filmes que o estabelecimento possui. </td>
</tr>
<tr>
<td width='20%'> <b>Descrição</b> </td>
<td width='80%'> Permitir o que o funcionário do estabelecimento realize as alterações. </td>
</tr>
<tr>
<td width='20%'> <b>Ator</b> </td>
<td width='80%'> Funcionário </td>
</tr>
<tr>
<td width='20%'> <b>Prioridade</b> </td>
<td width='80%'> Alta </td>
</tr>
<tr>
<td width='20%'> <b>Pré-condições</b> </td>
<td width='80%'> Funcionário cadastrado no sistema e com permissão de acesso. Efetuar Login. </td>
</tr>
<tr>
<td width='20%'> <b>Pós-condições</b> </td>
<td width='80%'> Alterar, remover e alterar dados dos filmes. </td>
</tr>
</table>

## Cenários principais de Sucesso: ##
<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Cadastro de DVD</b></td>
<td width='600'>1. Gerente comprar um novo DVD;</td></tr>
<tr><td width='600'>2. Funcionário cadastra os dados do DVD na no sistema.</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Exclusão de DVD</b></td>
<td width='600'>1. O Funcionário informa o título do DVD ou número de cadastro a ser procurado no sistema;</td></tr>
<tr><td width='600'>2. Os dados do DVD são exibidos;</td>
</tr>
<tr><td width='600'>3. O Funcionário seleciona a opção de excluir o DVD e uma mensagem de confirmação é exibida pelo sistema;</td>
</tr>
<tr><td width='600'>4. O Funcionário confirma e o DVD é excluído definitivamente do sistema.</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Alteração de dados</b></td>
<td width='600'>1. O Funcionário informa o título do DVD ou número de cadastro a ser procurado no sistema;</td></tr>
<tr><td width='600'>2. Os dados do DVD são exibidos;</td>
</tr>
<tr><td width='600'>3. O Funcionário altera os dados e salva e finaliza a operação.</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Consulta</b></td>
<td width='600'>1. O Funcionário informa o título do DVD ou número de cadastro a ser procurado no sistema;</td></tr>
<tr><td width='600'>2. Os dados do DVD são exibidos.</td>
</tr>
</table>

### Fluxos alternativos: ###

**A1.** Erro ao salvar o cadastro no sistema: uma mensagem de erro é exibida, e o sistema retorna ao passo 1;

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Exclusão de DVD</b></td>
<td width='600'>1. Cliente visualiza os DVD´s que estão cadastrados e disponíveis no sistema para locação;</td></tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Alteração de dados</b></td>
<td width='600'>A1. DVD não encontrado, retorna ao passo 1;</td></tr>
<tr><td width='600'>A2. Erro ao salvar alteração: uma mensagem de erro é exibida, retornando ao passo 2;</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Consulta</b></td>
<td width='600'>A1. DVD não encontrado, retorna ao passo 1;</td></tr>
</table>

<br>
<hr />

<h1>UC0002 - Cadastro de Clientes</h1>
<table cellpadding='5' border='1' cellspacing='5' width='595'>
<tr>
<td width='20%'> <b>Objetivos</b> </td>
<td width='80%'> Cadastrar, alterar, remover e alterar dados de clientes. </td>
</tr>
<tr>
<td width='20%'> <b>Descrição</b> </td>
<td width='80%'> Permitir o gerenciamento de dos cadastros dos clientes. </td>
</tr>
<tr>
<td width='20%'> <b>Ator</b> </td>
<td width='80%'> Funcionário </td>
</tr>
<tr>
<td width='20%'> <b>Prioridade</b> </td>
<td width='80%'> Alta </td>
</tr>
<tr>
<td width='20%'> <b>Pré-condições</b> </td>
<td width='80%'> Funcionário cadastrado no sistema e com permissão de acesso. Efetuar Login. </td>
</tr>
<tr>
<td width='20%'> <b>Pós-condições</b> </td>
<td width='80%'> Alterar, remover e alterar dados de clientes e realizar locação de DVD's. </td>
</tr>
</table>

<h2>Cenários principais de Sucesso:</h2>
<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Cadastro de Cliente</b></td>
<td width='600'>1. O Cliente informa seus dados pessoais para a realização do cadastro;</td></tr>
<tr><td width='600'>2. O Funcionário cadastra os dados do cliente no sistema;</td>
</tr>
<tr><td width='600'>3. O sistema mostra uma mensagem confirmando o cadastro, após a realização de cadastro.</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Exclusão de Cadastro</b></td>
<td width='600'>1. O Funcionário informa o nome do cliente ou numero de cadastro a ser procurado no sistema;</td></tr>
<tr><td width='600'>2. Os dados do cliente são exibidos;</td>
</tr>
<tr><td width='600'>3. O Funcionário seleciona a opção de excluir o cadastro e uma mensagem de confirmação é exibida;</td>
</tr>
<tr><td width='600'>4. O Funcionário confirma e o cadastro é excluído.</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Alteração de dados</b></td>
<td width='600'>1. O Funcionário informa o nome do cliente a ser procurado no sistema;</td></tr>
<tr><td width='600'>2. Os dados do cliente são exibidos;</td>
</tr>
<tr><td width='600'>3. O Funcionário altera os dados e salva no sistema.</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Consulta</b></td>
<td width='600'>1. O Funcionário informa o nome do cliente ou número de cadastro a ser procurado;</td></tr>
<tr><td width='600'>2. Os dados do cliente são exibidos.</td>
</tr>
</table>

<h3>Fluxos alternativos:</h3>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Cadastro de Cliente</b></td>
<td width='600'>A1. Erro ao salvar o cadastro no sistema: uma mensagem de erro é exibida, retornando ao passo 2 para continuação do cadastro.</td></tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Exclusão de Cadastro</b></td>
<td width='600'>A1. Cadastro não encontrado, retorna ao passo 1;</td></tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Alteração de Cadastro</b></td>
<td width='600'>A1. Cadastro não encontrado, retorna ao passo 1;</td></tr>
<tr><td width='600'>A2. Erro ao salvar o cadastro: uma mensagem de erro é exibida, retornando ao passo 2.</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Consulta</b></td>
<td width='600'>A1. DVD não encontrado, retorna ao passo 1;</td></tr>
</table>

<br>
<hr />

<h1>UC0003 - Funcionários</h1>
<table cellpadding='5' border='1' cellspacing='5' width='595'>
<tr>
<td width='20%'> <b>Objetivos</b> </td>
<td width='80%'> Fazer cadastro dos funcionários. </td>
</tr>
<tr>
<td width='20%'> <b>Descrição</b> </td>
<td width='80%'> Cadastrar, Remover, Consulta e Alteração de dados. </td>
</tr>
<tr>
<td width='20%'> <b>Ator</b> </td>
<td width='80%'> Gerente </td>
</tr>
<tr>
<td width='20%'> <b>Prioridade</b> </td>
<td width='80%'> Alta </td>
</tr>
<tr>
<td width='20%'> <b>Pré-condições</b> </td>
<td width='80%'> Funcionário cadastrado no sistema e com permissão de acesso. Efetuar Login. </td>
</tr>
<tr>
<td width='20%'> <b>Pós-condições</b> </td>
<td width='80%'> Ter acesso no sistema. Fazer Operações no sistema. </td>
</tr>
</table>

<h2>Cenários principais de Sucesso:</h2>
<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Cadastro de Funcionário</b></td>
<td width='600'>1. O novo Funcionário informa seus dados pessoais para a realização do cadastro;</td></tr>
<tr><td width='600'>2. O Gerente logado no sistema cadastra os dados do novo funcionário no sistema;</td>
</tr>
<tr><td width='600'>3. O sistema envia uma mensagem de êxito, após a realização de cadastro.</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Exclusão de Cadastro</b></td>
<td width='600'>1. O Gerente informa o nome do funcionário a ser procurado no sistema;</td></tr>
<tr><td width='600'>2. Os dados do funcionário são exibidos;</td>
</tr>
<tr><td width='600'>3. O Gerente seleciona a opção de excluir o cadastro e uma mensagem de confirmação é exibida;</td>
</tr>
<tr><td width='600'>4. O Gerente confirma e o cadastro é excluído.</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Alteração de Cadastro</b></td>
<td width='600'>1. O Gerente informa o nome do funcionário a ser procurado na base de dados;</td></tr>
<tr><td width='600'>2. Os dados do funcionário são exibidos;</td>
</tr>
<tr><td width='600'>3. O Gerente altera os dados e salva na base de dados.</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Consulta</b></td>
<td width='600'>1. O Gerente informa o nome do funcionário a ser procurado;</td></tr>
<tr><td width='600'>2. Os dados do funcionário são exibidos.</td>
</tr>
</table>

<h3>Fluxos alternativos:</h3>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Cadastro de Funcionário</b></td>
<td width='600'>A1. Erro ao salvar o cadastro: uma mensagem de erro é exibida, retornando ao passo 2 para continuação do cadastro.</td></tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Exclusão de Cadastro</b></td>
<td width='600'>A1. Cadastro não encontrado, retorna ao passo 1.</td></tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Alteração de Cadastro</b></td>
<td width='600'>A1. Cadastro não encontrado, retorna ao passo 1;</td></tr>
<tr><td width='600'>A2. Erro ao salvar o cadastro: uma mensagem de erro é exibida, retornando ao passo 2.</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Consulta de Funcionário</b></td>
<td width='600'>A1. Cadastro não encontrado, retorna ao passo 1.</td></tr>
</table>

<br>
<hr />

<h1>UC0004 - Locação de DVD</h1>
<table cellpadding='5' border='1' cellspacing='5' width='595'>
<tr>
<td width='20%'> <b>Objetivos</b> </td>
<td width='80%'> Locar e Devolver DVD's. </td>
</tr>
<tr>
<td width='20%'> <b>Descrição</b> </td>
<td width='80%'> Fazer as Ações de Locação de DVD's. </td>
</tr>
<tr>
<td width='20%'> <b>Ator</b> </td>
<td width='80%'> Cliente </td>
</tr>
<tr>
<td width='20%'> <b>Prioridade</b> </td>
<td width='80%'> Alta </td>
</tr>
<tr>
<td width='20%'> <b>Pré-condições</b> </td>
<td width='80%'> Funcionário cadastrado no sistema e com permissão de acesso. Efetuar Login. </td>
</tr>
<tr>
<td width='20%'> <b>Pós-condições</b> </td>
<td width='80%'> Locação de DVDs. Reserva. Devolução. </td>
</tr>
</table>

<h2>Cenários principais de Sucesso:</h2>
<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Locação de DVD</b></td>
<td width='600'>1. Cliente visualiza os DVD´s que estão cadastrados e disponíveis no sistema para locação;</td></tr>
<tr><td width='600'>2. Funcionário Preenche formulário de locação para cliente;</td>
</tr>
<tr><td width='600'>3. DVD é locado para cliente, e com data para devolução;</td>
</tr>
<tr><td width='600'>4. DVD('s) selecionado(s) se torna indisponível para locação.</td>
</tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Devolução de DVD</b></td>
<td width='600'>1. O Funcionário informa o código da locação dentro do sistema;</td></tr>
<tr><td width='600'>2. Os dados da locação são exibidos;</td>
</tr>
<tr><td width='600'>3. O Funcionário completa formulário de devolução de DVD;</td>
</tr>
<tr><td width='600'>4. O DVD se torna disponível para locação.</td>
</tr>
</table>

<h3>Fluxos alternativos:</h3>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Locação de DVD</b></td>
<td width='600'>A1. Erro ao salvar o cadastro no sistema: uma mensagem de erro é exibida, retornando ao passo 2.</td></tr>
</table>

<table cellpadding='5' border='1' cellspacing='5' width='800'>
<tr>
<td width='110' align='middle'><b>Devolução de DVD</b></td>
<td width='600'>A1.Código da locação não encontrado, retorna ao passo 1;</td></tr>
<tr><td width='600'>A2. Erro ao salvar o registro: uma mesagem de erro é exibida, retornando ao passo 3.</td>
</tr>
</table>

<br>
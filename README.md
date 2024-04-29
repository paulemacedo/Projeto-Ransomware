# Ransomware Simples

Este é um projeto desenvolvido durante o curso Santander Bootcamp Cibersegurança pela plataforma Dio.me, com o objetivo de entender como funciona um ransomware na prática.

## Descrição

O ransomware é um tipo de malware que criptografa os arquivos do sistema da vítima e solicita um resgate (geralmente em criptomoeda) para disponibilizar a chave de descriptografia e restaurar o acesso aos arquivos. Este projeto implementa um ransomware simples em Python, utilizando a biblioteca pyaes para criptografar e descriptografar arquivos.

## Funcionamento

O código consiste em duas partes principais: a primeira criptografa os arquivos, enquanto a segunda descriptografa-os após o pagamento do resgate.

### Criptografia

1. Abrir o arquivo alvo para leitura em modo binário.
2. Ler os dados do arquivo.
3. Remover o arquivo original.
4. Gerar uma chave de criptografia.
5. Utilizar o AES (Advanced Encryption Standard) em modo CTR (Counter) para criptografar os dados do arquivo.
6. Salvar o arquivo criptografado com a extensão .paule.

### Descriptografia

1. Abrir o arquivo criptografado para leitura em modo binário.
2. Ler os dados do arquivo criptografado.
3. Remover o arquivo criptografado.
4. Utilizar a mesma chave de criptografia para descriptografar os dados.
5. Salvar o arquivo descriptografado com o nome original.

## Utilização

Para utilizar este ransomware simples, siga estas etapas:

1. Execute o script de criptografia para criptografar o arquivo alvo. Certifique-se de fornecer o nome correto do arquivo no código.
2. Após a execução bem-sucedida, um arquivo com a extensão .paule será gerado.
3. Execute o script de descriptografia, fornecendo o nome do arquivo criptografado. Isso restaurará o arquivo original.

**Nota:** Este projeto é apenas para fins educacionais e demonstrativos. O uso de ransomware é ilegal e antiético.

## Requisitos

- Python 3.x
- Biblioteca pyaes

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests para melhorar este projeto.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa1 = Pessoa("Joao da Costa", "12345", "10/10/2010", False)
attrs = vars(pessoa1)

print('Instância da classe Pessoa:')
print(pessoa1)

pessoaFisica = PessoaFisica("Jose da Silva", "98765", "12/12/2012", False, "10/10/2000", "123.456.789-00", "1111111111")
print('Instância da classe PessoaFisica:')
print(pessoaFisica)

pessoaJuridica = PessoaJuridica("Luis da Silva", "12345", "10/10/2010", False, "10/10/1998", "12.123.123/0001-00")
print(pessoaJuridica)
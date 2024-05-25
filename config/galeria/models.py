from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100, null=False, blank=False)
    quantidade = models.IntegerField(blank=False, null=False)
    preco = models.DecimalField(max_digits= 10,decimal_places= 2, blank=False, null=False)

    def __str__(self):
        return f"Produto [nome_produto={self.nome_produto}]"
    

#from django.db import models: Esta linha importa o módulo de modelos do Django, 
#que contém classes e funções para trabalhar com o banco de dados.

#class Produto(models.Model): Aqui você está definindo uma nova classe chamada 
#Produto que herda de models.Model. Cada classe que herda de Model representa uma 
#tabela de banco de dados.

#nome_produto = models.CharField(max_length=100, null=False, blank=False): 
#Este é um campo de caractere que armazena o nome do produto. max_length=100 
#define o comprimento máximo do campo para 100 caracteres. 
#null=False significa que este campo não pode ser nulo no banco de dados e 
#blank=False significa que este campo não pode estar vazio.

#quantidade = models.IntegerField(blank=False, null=False): 
#Este é um campo inteiro que armazena a quantidade do produto. 
#Novamente, null=False e blank=False significam que este campo deve sempre ter um valor.

#preco = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False):
#Este é um campo decimal que armazena o preço do produto. 
#max_digits=10 define o número máximo total de dígitos para este campo, 
#e decimal_places=2 define o número de dígitos após o ponto decimal.

#def __str__(self): Esta é a representação em string do objeto Produto. 
#Quando você imprime um objeto Produto, ele retornará a 
#string formatada “Produto [nome_produto={self.nome_produto}]”.

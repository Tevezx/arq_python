'''import matplotlib.pyplot as plt
#Definição de dados
linguagens = 'Java', 'Python', 'PHP', 'C++', "Javascript", "C#"
popularidade = [22, 17, 8, 9, 12, 6] #74 pessoas participaram
#Cores do grafico em hexadecimal
cores = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
#Destacar a fatia
destacar = (0.05, 0, 0, 0, 0.0, 0.07)
#Plot
plt.pie(popularidade, explode=destacar, labels=linguagens, colors=cores, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Popularidade de Linguagens de Programação\n" + "Estudandes da Unicid comparado ao ano passado (2024)", bbox={'facecolor':'0.8', 'pad':5})
plt.show()#Mostra o gráfico
'''
'''
import matplotlib.pyplot as plt
dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
vendas_semana = []
#Cores
cores = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#F23876"]
#Entrada de dados
for i in range(7):
    quantidade = int(input("Digite a quantidade de vendas na "+ dias[i]+":"))
    vendas_semana.append(quantidade)
#Plotar gráfico de barra
x= range(len(dias))
y = vendas_semana
plt.bar(x, y, color=cores)
plt.xlabel("Dias da semana")
plt.xlabel("Vendas")
plt.title("Vendas da semana")
plt.xticks(x, dias)
plt.grid(True)
plt.show()
'''
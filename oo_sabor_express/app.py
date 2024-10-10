from modelos.restaurante import Restaurante

rest1 = Restaurante('pizza jo', 'Italiano')
rest1.receber_avaliacao('Jo', 10)
rest1.receber_avaliacao('Manu', 2)
rest1.receber_avaliacao('Cao', 8)










def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
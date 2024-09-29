from models.classe_ex_locadora06 import Locadora


def main():
    loc_01 = Locadora("Lucas Video")
    loc_01.altera_estado()

    Locadora.List_Locadoras()


if __name__ == '__main__':
    main()

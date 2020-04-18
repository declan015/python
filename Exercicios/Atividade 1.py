import re
from os import system, name 
from time import sleep 

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

#---------------------------------------------

lista = ['Lorena Rocha', 'Rui Ferrón', 'Pandora Bragança', 'Maura Boga', 'Abel Capiperibe', 'Aires Varão', 'Fernanda Mattos', 'Fábio Caires', 'Zacarias Quinteiro', 'Antão Covelhã', 'Mauro Galante', 'Tatiana Osório', 'Xénia Bernardes', 'Jónatas Varão', 'Bibiana Prates', 'Rodolfo Arantes', 'Laurinda Assis', 'Bartolomeu Cisneros', 'Acacio Cunha', 'Clarisse Pamplona', 'Elsa Cotrim', 'Alvito Inácio', 'Judas Cardozo', 'Afonso Ferrera', 'Sílvio Cambaúva', 'Josefina Pajares', 'Celestina Pavía', 'Sônia ou Sonia Freyre', 'Talita Cyrne', 'Adriana Delgado', 'Amanda Pádua', 'Donata Vilalobos', 'Roberto Calheiros', 'Uriel Gouveia', 'Artur Veloso', 'Lúcio Monjardim', 'Rafael Jácome', 'Alfredo Domingos', 'Gabriela Braz', 'Odete Gama', 'Severino Lagoa', 'Hedviges Barros', 'Fabíola Sequeira', 'Lucília Colares', 'Custódio Felgueiras', 'Mem Britto', 'André Ximenes', 'Adélia Marañón', 'Sónia Bivar', 'Clarisse Ourique', 'Aarão Tabajara', 'Giovana Madruga', 'Tobias Guerreiro', 'Potira Bivar', 'Diamantino Tévez', 'Manuel Lampreia', 'Jamari Vilas Boas', 'Armindo Tamoio', 'Olívio Quintella', 'Milena Gusmão', 'Isaura Hollanda', 'Ítalo Gago', 'Martim Camillo', 'Cristiana Valiente', 'Gláucia Taborda', 'Belchior Gameiro', 'Odete Pederneiras', 'Veríssimo Gonsalves', 'Sandoval Mayor', 'Tomásia Monte', 'Edgar Loureiro', 'Ifigénia Carqueijeiro', 'Eusébio Quinzeiro', 'Alda Meireles', 'Otília Lagos', 'Frederico Cotegipe', 'Lucílio Cidreira', 'Iuri Gracia', 'Arminda Mansilha', 'Isilda Lacerda', 'Irene Quental', 'Cátia Viveros', 'Mécia Marmou', 'Quitério Costa', 'Alípio Moutinho', 'Floripes Camacho', 'Epifânia Loio', 'Floripes Morales', 'Salvador Franca', 'Antonieta Remígio', 'Lina Laureano', 'Carlos Vilhena', 'Almerinda Sobreira', 'Juliano Vázquez', 'Úrsula Ruela', 'Débora Lucas', 'Angelina Serralheiro', 'Filinto Telinhos', 'Albérico de Castro', 'Lívia Salguero', 'Zuleica Simão', 'Ulisses Silvera', 'Jacinto Tavera', 'Madalena Cabeza de Vaca', 'Araci Candeias', 'Susana Veleda', 'Lara Lameiras', 'Jorge Farias', 'Aurélia Pirassununga', 'Judas Mendonça', 'Edmundo Quiroga', 'Collin Outeiro', 'Eduardo Terra', 'Paulino Grangeia', 'Vítor ou Victor Jordão', 'Eliseu Felgueira', 'Paulo Velásquez', 'Guilhermina Ginjeira', 'Viviana Matos', 'Branco Jardim', 'Rubim Vasques', 'Manuel Orriça', 'Mileide Saraiva', 'Bibiana Monteiro', 'Leónidas Cisneros', 'Liliana Valverde', 'Casimiro Brito', 'Lília Siebra', 'Melissa Bethancout', 'Emiliana Galindo', 'Tatiana Benavides', 'Andreoleto Vilariça', 'Ema Freyria', 'Telma Sá', 'Hugo Toscano', 'Clotilde Nieves', 'Eliseu Ginjeira', 'Cid Becerra', 'Ana Pires', 'Vivaldo Matos', 'Uriel Otero', 'Sabino Castillo', 'Ajuricaba Miguel', 'Berengário Castelo Branco', 'Leónidas Coutinho', 'Clarindo Alverne', 'Gávio Pajares', 'Leónidas Feitosa', 'Angelino Horta', 'Solange Pessoa', 'Matias Bensaúde', 'Norberto Parreira', 'Márcia Maciel', 'Heloísa Guerra', 'Zoe Pequeno', 'Camila Veiga', 'Matias Ayres', 'Nádia Gorjão', 'Hermígio Quiroga', 'Tomás Póvoas', 'Jacira Diegues', 'Leônidas Rúa', 'Ulisses Freire', 'Valmor Belém', 'Flamínia Queiroz', 'Marcelo Cabreira', 'Hugo Baranda', 'Derli Bello', 'Rômulo Pêssego', 'Micaela Sousa do Prado', 'Silvana Oleiro', 'Apuã Nobre', 'Guido Vilas-Boas', 'Marta Mangueira', 'Maurício Amaro', 'Lara Quintas', 'Rúben Lagoa', 'Estanislau Vilar', 'Mécia Damazio', 'Rudi Uchoa', 'Filipe Souto Maior', 'Gláucio Leão', 'Júlio Soto Mayor', 'Balduíno Esparteiro', 'Elisa Peña', 'Berengário Baptista', 'Adolfo Assunção', 'Basilio Mieiro', 'Eduardo Maciel', 'Bento Colares', 'Gualdim Cirne', 'Faustino Lustosa', 'Clara Coello', 'Nazaré Horta', 'Minervina Tamoio', 'Neusa Padilha', 'Ilma Gaspar', 'Filena Vidigal', 'Adriana Amado', 'António Brás']
lst = [t.upper() for t in lista]
i=0
pers="S"
# -----------------------------------------------------

while pers=="S":
    pers=""
    clear()

    print("***************************************************")
    print("*   VARIOS NOMES FORAM VAZADOS! PROCURE O SEU!    *")
    print("***************************************************")
    print("*          Qual o nome que você procura?          *")
    print("***************************************************")


    nome = input()
    nomet = nome.upper()

    r = re.compile("[a-zA-Z ]*"+nomet+"[ a-zA-Z]*")

    newlist = list(filter(r.match, lst))

    if newlist != []:

        print('\nAqui estão os nomes vazados que contem "'+nome+'":')
        for x in newlist:

            i=i+1
            print(str (i)+" - "+x.title())

    else:

        print("Não foi encontrado nenhum resultado!")
    
    while pers != "S" and pers != "N":
        pers = input("\nVocê gostaria de continuar pesquisando? (S/N)").upper()

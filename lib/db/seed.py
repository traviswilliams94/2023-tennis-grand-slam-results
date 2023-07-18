from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Player, Tournament, Result, Base

engine = create_engine('sqlite:///tournament_results.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# finishes = ["First Round",  "Second Round", "Third Round", "Fourth Round", "Quarters", "Semis", "Final", "Winner", "DNP"]

# tournament_names = ["Australian Open", "French Open", "Wimbledon"]

if __name__ == '__main__':

    session.query(Player).delete()
    session.query(Tournament).delete()
    session.query(Result).delete()
   
    # seed the  players
    player1 = Player(name="Carlos Alcaraz", gender="male", ranking= 1)
    player2 = Player(name="Novak Djokovic", gender="male", ranking= 2)
    player3 = Player(name="Daniil Medvedev", gender="male", ranking= 3)
    player4 = Player(name="Casper Ruud", gender="male", ranking= 4)
    player5 = Player(name="Stefanos Tsitsipas", gender="male", ranking= 5)
    player6 = Player(name="Holger Rune", gender="male", ranking= 6)
    player7 = Player(name="Andrey Rublev", gender="male", ranking= 7)
    player8 = Player(name="Jannik Sinner", gender="male", ranking= 8)
    player9 = Player(name="Taylor Fritz", gender="male", ranking= 9)
    player10 = Player(name="Frances Tiafoe", gender="male", ranking= 10)
    player11 = Player(name="Karen Khachanov", gender="male", ranking= 11)
    player12 = Player(name="Felix Auger-Aliassime", gender="male", ranking= 12)
    player13 = Player(name="Cameron Norrie", gender="male", ranking= 13)
    player14 = Player(name="Tommy Paul", gender="male", ranking= 14)
    player15 = Player(name="Borna Coric", gender="male", ranking= 15)
    player16 = Player(name="Lorenzo Musetti", gender="male", ranking= 16)
    player17 = Player(name="Hubert Hurkacz", gender="male", ranking= 17)
    player18 = Player(name="Alex De Minaur", gender="male", ranking= 18)
    player19 = Player(name="Alexander Zverev", gender="male", ranking= 19)
    player20 = Player(name="Francisco Cerundolo", gender="male", ranking= 20)

    player21 = Player(name="Iga Swiatek", gender="female", ranking= 1)
    player22 = Player(name="Aryna Sabalenka", gender="female", ranking= 2)
    player23 = Player(name="Elena Rybakina", gender="female", ranking= 3)
    player24 = Player(name="Jessica Pegula", gender="female", ranking= 4)
    player25 = Player(name="Caroline Garcia", gender="female", ranking= 5)
    player26 = Player(name="Ons Jabeur", gender="female", ranking= 6)
    player27 = Player(name="Coco Gauff", gender="female", ranking= 7)
    player28 = Player(name="Petra Kvitova", gender="female", ranking= 8)
    player29 = Player(name="Maria Sakkari", gender="female", ranking= 9)
    player30 = Player(name="Marketa Vondrousova", gender="female", ranking= 10)
    player31 = Player(name="Daria Kasatkina", gender="female", ranking= 11)
    player32 = Player(name="Barbora Krejcikova", gender="female", ranking= 12)
    player33 = Player(name="Beatriz Haddad Maia", gender="female", ranking= 13)
    player34 = Player(name="Veronika Kudermetova", gender="female", ranking= 14)
    player35 = Player(name="Belinda Bencic", gender="female", ranking= 15)
    player36 = Player(name="Madison Keys", gender="female", ranking= 16)
    player37 = Player(name="Liudmila Samsonova", gender="female", ranking= 17)
    player38 = Player(name="Karolina Muchova", gender="female", ranking= 18)
    player39 = Player(name="Victoria Azarenka", gender="female", ranking= 19)
    player40 = Player(name="Jelena Ostapenko", gender="female", ranking= 20)
    player41 = Player(name="Magda Linnete", gender="female", ranking= 25)
    player42 = Player(name="Elina Svitolina", gender="female", ranking= 27)

    session.add_all([player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12, player13, player14, player15, player16, player17,
    player18, player19, player20, player21, player22, player23, player24, player25, player26, player27, player28, player29, player30, player31, player32, player33, player34,
    player35, player36, player37, player38, player39, player40, player41, player42])

    session.commit()
    

    # seed the tournaments
    aus = Tournament(name="Australian Open")
    french = Tournament(name="French Open")
    wimbledon = Tournament(name="Wimbledon")

    session.add_all([aus, french, wimbledon])
    session.commit()


    # seed the results
    result1 = Result(player_id= player1.id, tournament_id= aus.id, finish="DNP")
    result2 = Result(player_id= player1.id, tournament_id= french.id, finish="Semis")
    result3 = Result(player_id= player1.id, tournament_id= wimbledon.id, finish="Winner")

    result4 = Result(player_id= player2.id, tournament_id= aus.id, finish="Winner")
    result5 = Result(player_id= player2.id, tournament_id= french.id, finish="Winner")
    result6 = Result(player_id= player2.id, tournament_id= wimbledon.id, finish="Final")

    result7 = Result(player_id= player3.id, tournament_id= aus.id, finish="Third Round") 
    result8 = Result(player_id= player3.id, tournament_id= french.id, finish="First Round")
    result9 = Result(player_id= player3.id, tournament_id= wimbledon.id, finish="Semis")

    result10 = Result(player_id= player4.id, tournament_id= aus.id, finish="Second Round")
    result11 = Result(player_id= player4.id, tournament_id= french.id, finish="Final")
    result12 = Result(player_id= player4.id, tournament_id= wimbledon.id, finish="Second Round")

    result13 = Result(player_id= player5.id, tournament_id= aus.id, finish="Final")
    result14 = Result(player_id= player5.id, tournament_id= french.id, finish="Quarters")
    result15 = Result(player_id= player5.id, tournament_id= wimbledon.id, finish="Fourth Round")

    result16 = Result(player_id= player6.id, tournament_id= aus.id, finish="Fourth Round")
    result17 = Result(player_id= player6.id, tournament_id= french.id, finish="Quarters")
    result18 = Result(player_id= player6.id, tournament_id= wimbledon.id, finish="Quarters")

    result19 = Result(player_id= player7.id, tournament_id= aus.id, finish="Quarters")
    result20 = Result(player_id= player7.id, tournament_id= french.id, finish="Third Round")
    result21 = Result(player_id= player7.id, tournament_id= wimbledon.id, finish="Quarters")

    result22 = Result(player_id= player8.id, tournament_id= aus.id, finish="Fourth Round")
    result23 = Result(player_id= player8.id, tournament_id= french.id, finish="Second Round")
    result24 = Result(player_id= player8.id, tournament_id= wimbledon.id, finish="Semis")

    result25 = Result(player_id= player9.id, tournament_id= aus.id, finish="Second Round")
    result26 = Result(player_id= player9.id, tournament_id= french.id, finish="Third Round")
    result27 = Result(player_id= player9.id, tournament_id= wimbledon.id, finish="Second Round")

    result28 = Result(player_id= player10.id, tournament_id= aus.id, finish="Third Round")
    result29 = Result(player_id= player10.id, tournament_id= french.id, finish="Third Round")
    result30 = Result(player_id= player10.id, tournament_id= wimbledon.id, finish="Third Round")

    result31 = Result(player_id= player11.id, tournament_id= aus.id, finish="Semis")
    result32 = Result(player_id= player11.id, tournament_id= french.id, finish="Quarters")
    result33 = Result(player_id= player11.id, tournament_id= wimbledon.id, finish="DNP")

    result34 = Result(player_id= player12.id, tournament_id= aus.id, finish="Fourth Round")
    result35 = Result(player_id= player12.id, tournament_id= french.id, finish="First Round")
    result36 = Result(player_id= player12.id, tournament_id= wimbledon.id, finish="First Round")

    result37 = Result(player_id= player13.id, tournament_id= aus.id, finish="Third Round")
    result38 = Result(player_id= player13.id, tournament_id= french.id, finish="Third Round")
    result39 = Result(player_id= player13.id, tournament_id= wimbledon.id, finish="Second Round")

    result40 = Result(player_id= player14.id, tournament_id= aus.id, finish="Semis")
    result41 = Result(player_id= player14.id, tournament_id= french.id, finish="Second Round")
    result42 = Result(player_id= player14.id, tournament_id= wimbledon.id, finish="Third Round")

    result43 = Result(player_id= player15.id, tournament_id= aus.id, finish="First Round")
    result44 = Result(player_id= player15.id, tournament_id= french.id, finish="Third Round")
    result45 = Result(player_id= player15.id, tournament_id= wimbledon.id, finish="First Round")

    result46 = Result(player_id= player16.id, tournament_id= aus.id, finish="First Round")
    result47 = Result(player_id= player16.id, tournament_id= french.id, finish="Fourth Round")
    result48 = Result(player_id= player16.id, tournament_id= wimbledon.id, finish="Third Round")

    result49 = Result(player_id= player17.id, tournament_id= aus.id, finish="Fourth Round")
    result50 = Result(player_id= player17.id, tournament_id= french.id, finish="Third Round")
    result51 = Result(player_id= player17.id, tournament_id= wimbledon.id, finish="Fourth Round")

    result52 = Result(player_id= player18.id, tournament_id= aus.id, finish="Fourth Round")
    result53 = Result(player_id= player18.id, tournament_id= french.id, finish="Second Round")
    result54 = Result(player_id= player18.id, tournament_id= wimbledon.id, finish="Second Round")

    result55 = Result(player_id= player19.id, tournament_id= aus.id, finish="Second Round")
    result56 = Result(player_id= player19.id, tournament_id= french.id, finish="Semis")
    result57 = Result(player_id= player19.id, tournament_id= wimbledon.id, finish="Third Round")

    result58 = Result(player_id= player20.id, tournament_id= aus.id, finish="Third Round")
    result59 = Result(player_id= player20.id, tournament_id= french.id, finish="Fourth Round")
    result60 = Result(player_id= player20.id, tournament_id= wimbledon.id, finish="Second Round")

    result61 = Result(player_id= player21.id, tournament_id= aus.id, finish="Fourth Round")
    result62 = Result(player_id= player21.id, tournament_id= french.id, finish="Winner")
    result63 = Result(player_id= player21.id, tournament_id= wimbledon.id, finish="Quarters")

    result64 = Result(player_id= player22.id, tournament_id= aus.id, finish="Winner")
    result65 = Result(player_id= player22.id, tournament_id= french.id, finish="Semis")
    result66 = Result(player_id= player22.id, tournament_id= wimbledon.id, finish="Semis")

    result67 = Result(player_id= player23.id, tournament_id= aus.id, finish="Final")
    result68 = Result(player_id= player23.id, tournament_id= french.id, finish="Third Round")
    result69 = Result(player_id= player23.id, tournament_id= wimbledon.id, finish="Quarters")

    result70 = Result(player_id= player24.id, tournament_id= aus.id, finish="Quarters")
    result71 = Result(player_id= player24.id, tournament_id= french.id, finish="Third Round")
    result72 = Result(player_id= player24.id, tournament_id= wimbledon.id, finish="Quarters")
    
    result73 = Result(player_id= player25.id, tournament_id= aus.id, finish="Fourth Round")
    result74 = Result(player_id= player25.id, tournament_id= french.id, finish="Second Round")
    result75 = Result(player_id= player25.id, tournament_id= wimbledon.id, finish="Third Round")

    result76 = Result(player_id= player26.id, tournament_id= aus.id, finish="Second Round")
    result77 = Result(player_id= player26.id, tournament_id= french.id, finish="Quarters")
    result78 = Result(player_id= player26.id, tournament_id= wimbledon.id, finish="Final")

    result79 = Result(player_id= player27.id, tournament_id= aus.id, finish="Fourth Round")
    result80 = Result(player_id= player27.id, tournament_id= french.id, finish="Quarters")
    result81 = Result(player_id= player27.id, tournament_id= wimbledon.id, finish="First Round")

    result82 = Result(player_id= player28.id, tournament_id= aus.id, finish="Second Round")
    result83 = Result(player_id= player28.id, tournament_id= french.id, finish="First Round")
    result84 = Result(player_id= player28.id, tournament_id= wimbledon.id, finish="Fourth Round")

    result85 = Result(player_id= player29.id, tournament_id= aus.id, finish="Third Round")
    result86 = Result(player_id= player29.id, tournament_id= french.id, finish="First Round")
    result87 = Result(player_id= player29.id, tournament_id= wimbledon.id, finish="First Round")

    result88 = Result(player_id= player30.id, tournament_id= aus.id, finish="Third Round")
    result89 = Result(player_id= player30.id, tournament_id= french.id, finish="Second Round")
    result90 = Result(player_id= player30.id, tournament_id= wimbledon.id, finish="Winner")

    result91 = Result(player_id= player31.id, tournament_id= aus.id, finish="First Round")
    result92 = Result(player_id= player31.id, tournament_id= french.id, finish="Fourth Round")
    result93 = Result(player_id= player31.id, tournament_id= wimbledon.id, finish="Third Round")

    result94 = Result(player_id= player32.id, tournament_id= aus.id, finish="Fourth Round")
    result95 = Result(player_id= player32.id, tournament_id= french.id, finish="First Round")
    result96 = Result(player_id= player32.id, tournament_id= wimbledon.id, finish="Second Round")

    result97 = Result(player_id= player33.id, tournament_id= aus.id, finish="First Round")
    result98 = Result(player_id= player33.id, tournament_id= french.id, finish="Semis")
    result99 = Result(player_id= player33.id, tournament_id= wimbledon.id, finish="Fourth Round")

    result100 = Result(player_id= player34.id, tournament_id= aus.id, finish="Second Round")
    result101 = Result(player_id= player34.id, tournament_id= french.id, finish="First Round")
    result102 = Result(player_id= player34.id, tournament_id= wimbledon.id, finish="Second Round")

    result103 = Result(player_id= player35.id, tournament_id= aus.id, finish="Fourth Round")
    result104 = Result(player_id= player35.id, tournament_id= french.id, finish="First Round")
    result105 = Result(player_id= player35.id, tournament_id= wimbledon.id, finish="Fourth Round")

    result106 = Result(player_id= player36.id, tournament_id= aus.id, finish="Third Round")
    result107 = Result(player_id= player36.id, tournament_id= french.id, finish="Second Round")
    result108 = Result(player_id= player36.id, tournament_id= wimbledon.id, finish="Quarters")

    result109 = Result(player_id= player37.id, tournament_id= aus.id, finish="Second Round")
    result110 = Result(player_id= player37.id, tournament_id= french.id, finish="Second Round")
    result111 = Result(player_id= player37.id, tournament_id= wimbledon.id, finish="First Round")

    result112 = Result(player_id= player38.id, tournament_id= aus.id, finish="Second Round")
    result113 = Result(player_id= player38.id, tournament_id= french.id, finish="Final")
    result114 = Result(player_id= player38.id, tournament_id= wimbledon.id, finish="First Round")

    result115 = Result(player_id= player39.id, tournament_id= aus.id, finish="Semis")
    result116 = Result(player_id= player39.id, tournament_id= french.id, finish="First Round")
    result117 = Result(player_id= player39.id, tournament_id= wimbledon.id, finish="Fourth Round")

    result118 = Result(player_id= player40.id, tournament_id= aus.id, finish="Quarters")
    result119 = Result(player_id= player40.id, tournament_id= french.id, finish="Second Round")
    result120 = Result(player_id= player40.id, tournament_id= wimbledon.id, finish="Second Round")

    result121 = Result(player_id= player41.id, tournament_id= aus.id, finish="Semis")
    result122 = Result(player_id= player41.id, tournament_id= french.id, finish="First Round")
    result123 = Result(player_id= player41.id, tournament_id= wimbledon.id, finish="Third Round")

    result124 = Result(player_id= player42.id, tournament_id= aus.id, finish="DNP")
    result125 = Result(player_id= player42.id, tournament_id= french.id, finish="Quarters")
    result126 = Result(player_id= player42.id, tournament_id= wimbledon.id, finish="Semis")


    session.add_all([result1, result2, result3, result4, result5, result6, result7, result8, result9, result10, result11, result12, result13, result14, result15, result16, result17,
    result18, result19, result20, result21, result22, result23, result24, result25, result26, result27, result28, result29, result30, result31, result32, result33, result34,
    result35, result36, result37, result38, result39, result40, result41, result42, result43, result44, result45, result46, result47, result48, result49, result50, result51,
    result52, result53, result54, result55, result56, result57, result58, result59, result60, result61, result62, result63, result64, result65, result66, result67, result68,
    result69, result70, result71, result72, result73, result74, result75, result76, result77, result78, result79, result80, result81, result82, result83, result84, result85,
    result86, result87, result88, result89, result90, result91, result92, result93, result94, result95, result96, result97, result98, result99, result100, result101, result102,
    result103, result104, result105, result106, result107, result108, result109, result110, result111, result112, result113, result114, result115, result116, result117, result118,
    result119, result120, result121, result122, result123, result124, result125, result126])
    
    session.commit()
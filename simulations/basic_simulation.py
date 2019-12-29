from game.yakelin import Yakelin

for strategy in ['val_strat','suits_strat','random']:

    f = open("../data/results_" + strategy + ".csv","w")
    f.write("Cards_on_table,Number_of_wins,Success_rate\n")

    number_of_simulations = 10000

    #n represents the number of cards originally on the table
    for n in range (1,53):
        num_wins = 0
        #x represents the an individual simulation
        for x in range(1,number_of_simulations):
            yak = Yakelin(n)
            status = yak.play(strategy)
            if status == "WIN":
                num_wins = num_wins + 1
        print("for " + str(n) + " cards, we have " + str(num_wins) + " wins")

        success_rate = num_wins/number_of_simulations
        print("success rate: " + str(success_rate))
        f.write(str(n) + "," + str(num_wins) + "," + str(success_rate) + "\n")
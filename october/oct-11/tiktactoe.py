results_of_game = ['', '', '', '', 'O', '', 'X', '', ''] 
winners = ['012', '036', '048', '147', '258', '246', '345', '678']

def tiktactoe(results):
    check_for_winners = []
    for char in winners:
        check = ''
        for i in char:
            i = int(i)
            check = check + results[i]
        check_for_winners.append(check)

    if "XXX" in check_for_winners:
        return print("X wins!")
    elif "OOO" in check_for_winners:
        return print("O wins!")
    else:
        return print("Cat's Game!")

tiktactoe(results_of_game)
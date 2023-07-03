import pandas as pd
from client_program import Client_program

prog = Client_program('client_program.csv')

repeat = True
while repeat:

    choice = prog.get_main_menu_choice()

    # CHOICE 1 - PRINT
    if choice == 1:
        prog.choice1_print_client()

    # CHOICE 2 - ADD
    elif choice == 2:
        check_2 = True
        while check_2:
            new_client = prog.choice2_add_client()
            if prog.choice2_add_client_check_duplicate(new_client):
                df_new = pd.DataFrame([new_client]).set_index('id')
                prog.df = pd.concat([prog.df, df_new])
                print()
                print('You just added the following client:')
                print()
                print(df_new)
                check_2 = False
            else:
                print()
                print('This client is already in your file!')
                check_2 = False

    # CHOICE 3 - UPDATE
    elif choice == 3:
        prog.choice3_update_client()

    # CHOICE 4 - DELETE
    elif choice == 4:
        prog.choice4_delete_client()

    # CHOICE 5 - SAVE & EXIT
    elif choice == 5:
        prog.save_to_csv()
        # client_lifts.export_to_csv()
        repeat = False

    else:
        print('You have to give a number from 1 - 5!')


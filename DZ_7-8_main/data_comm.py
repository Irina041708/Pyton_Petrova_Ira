import menu
import jf
import conclusion as c
import add_key as ak
import add_user as au
import remove_record as rr
import save_file as sf


def data_comm():
    data = jf.read_file()
    exit = True
    while exit:
        what = menu.menu()
        if what == 1:
            c.get_conclusion(data)
        elif what == 2:
            ak.get_add_key(data)
        elif what == 3:
            au.get_add_user(data)
        elif what == 4:
            rr.get_remove_record(data)
        elif what == 5:
            sf.get_save_file(data)
        else:
            exit = False
data_comm()     

import menu
import jf
import conclusion as c
import add_key as ak
import add_user as au
import remove_record as rr
import save_file as sf
import xxml
import openpyxl


def data_comm():
    data_json = jf.read_file()
    data_xlsx = xxml.read_file()
    data_xlsx_2 = xxml.read_file_2()
    exit = True
    while exit:
        what = menu.menu()
        if what == 1:
            c.get_conclusion_json(data_json)
        elif what == 2:
            ak.get_add_key(data_json)
        elif what == 3:
            au.get_add_user_json(data_json)
        elif what == 4:
            rr.get_remove_record(data_json)
        elif what == 5:
            sf.get_save_file_json(data_json)
        elif what == 6:
            c.get_conclusion_xlsx(data_xlsx)
        elif what == 7:
            au.get_add_save_user_xlsx(data_xlsx)
        elif what == 8:
            c.get_conclusion_xlsx_2(data_xlsx_2)
        else:
            exit = False
data_comm()     

import random
class Poem:
    def __init__(self,text):
        self.text = text.split("#")[0]
        self.count_num_year = int(text.split("#")[1])
        self.count_num_month = int(text.split("#")[2])
        self.count_word = text.split("#")[0].count("{}")-self.count_num_year-self.count_num_month
    
    def Struct(self,year_begin=1919,year_end=2077,month_begin=1,month_end=12):
        _format = ""

        if self.count_word != 0:
            _format += "GetWord()," * self.count_word

        if self.count_num_year != 0:
            sybegin = str(year_begin)
            syend = str(year_end)
            _format += f"random.randint({sybegin},{syend})," * self.count_num_year

        if self.count_num_month != 0:
            smbegin = str(month_begin)
            smend = str(month_end)
            if self.count_num_month == 2:
                month1 = str(random.randint(month_begin,month_end-1))
                month2 = str(random.randint(int(month1)+1,month_end))
                _format += f"{month1},{month2},"
            else:
                _format += f"random.randint({smbegin},{smend})," * self.count_num_month

        _format.strip(",")
        return f"poem.text.format({_format})"
        
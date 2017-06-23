from time import *
import re

class validateUtil:


    def __init__(self):
        pass
    def age(d,m,y):
        d=int(d)
        m = int(m)
        y = int(y)
        # get the current time in tuple format
        a = gmtime()
        # difference in day
        dd = a[2] - d
        # difference in month
        dm = a[1] - m
        # difference in year
        dy = a[0] - y
        # checks if difference in day is negative
        if dd < 0:
            dd = dd + 30
            dm = dm - 1
            # checks if difference in month is negative when difference in day is also negative
            if dm < 0:
                dm = dm + 12
                dy = dy - 1
        # checks if difference in month is negative when difference in day is positive
        if dm < 0:
            dm = dm + 12
            dy = dy - 1

        return  dy


    def date(d,m,y):
        pattern = "(([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29)"
        ereg = re.compile(pattern)
        is_match =re.match(ereg, y+"-"+m+"-"+d)
        # is_match = re.match(pattern, y+"-"+m+"-"+d, re.S)
        if is_match:
            return 1
        else:
            return 0

    # 前17位为数字，最后1位校验码为数字或X（如为x请转为X）
    def validate2(value):
        ereg = re.compile("^\d{18}$|^\d{17}(\d|X|x)$")
        is_match = re.match(ereg,value)
        if is_match:
            return 1
        else:
            return 0

    def validate3(value):
        distrct = ['11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35', '36', '37', '41', '42',
                   '43', '44', '45', '46', '50', '51', '52',
                   '53', '54', '61', '62', '63', '64', '65']
        prefx = str(value[0:2])
        if prefx in distrct:
            return 1
        else:
            return 0

    def validate4(value):
        yyyy = value[6:10]
        mm = value[10:12]
        dd = value[12:14]
        flag = 0
        age = validateUtil.age(dd, mm, yyyy)
        if validateUtil.date(dd, mm, yyyy) and (age >= 18 and age <= 60):
            flag = 1
        return flag

    def validate5(value):
        index = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        dict = {
            0: 1, 1: 0, 2: "X", 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2
        }
        sum=0;
        for i in  range(len(value)-1):
            sum=sum+index[i]*int(value[i])
        yu=sum%11
        wei=dict[yu]
        mowei=value[17]
        if mowei=="x":
            mowei="X"
        if str(wei)==mowei:
            return 1
        else:
            return 0


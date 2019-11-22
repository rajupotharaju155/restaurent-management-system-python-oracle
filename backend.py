from tkinter import *
from tkinter import messagebox

def InsertIntoListBox(tableName, listBox):
    import cx_Oracle
    con = None
    cursor = None
    try:
        con = cx_Oracle.connect("system/Rajuoracledb#123")
        cursor = con.cursor()
        sql = "select itemNo, dish, rate, quantity, itemamount from "+tableName+" order by itemNo"
        cursor.execute(sql)
        data = cursor.fetchall()
        mdata = ""
        for d in data:
            mdata = mdata + str("            "+str(d[0])+"                   "  +d[1]) + "              " +  str(d[2])+"                " + str(d[3]) + "             "+str(d[4])+ "\n"
            listBox.insert(END, mdata)
            mdata = ""
    except cx_Oracle.DatabaseError as e:
        print("issue", e)
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()


def InsertIntoTable(tableName, itemNo, dish, itemAmount,  quantity, amount ):
    import cx_Oracle
    con = None
    cursor = None
    try:
        con = cx_Oracle.connect("system/Rajuoracledb#123")
        cursor = con.cursor()
        sql = "insert into "+tableName+" values('%d', '%s', '%d', '%d', '%d' )"
        args = (itemNo, dish, itemAmount, quantity, amount)
        cursor.execute(sql % args)
        con.commit()
        #msg = str(cursor.rowcount) + " records inserted"
        #messagebox.showinfo("Success ", msg)
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        print("eror  -->", e)
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()

def deleteFromTable(tableName):
    import cx_Oracle
    con = None
    cursor = None
    try:
        con = cx_Oracle.connect("system/Rajuoracledb#123")
        cursor = con.cursor()
        sql = "delete from "+tableName
        cursor.execute(sql )
        con.commit()
        msg = str(cursor.rowcount) + " records deleted"
        #messagebox.showinfo("Success ", msg)
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        print("error is ", e)
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()


def addIntoMenu(dish_name, rate, entDish, entRate):
    if dish_name == '' or rate == '':
        messagebox.showerror("Error ", "Please fill all the fields")
    elif len(dish_name) < 2 or len(dish_name) > 20:
        messagebox.showerror("Error ", "DISH name should contain atleast 2 and max 20 letters")
        entDish.delete(0, END)
        entDish.focus()
    elif rate.isdigit():
        rate = int(rate)
        if rate < 10:
            messagebox.showerror("Error ", "Rate cannot be less than 10 Rupees")
            entRate.delete(0, END)
            entRate.focus()
        else:
            import cx_Oracle
            con = None
            cursor = None
            try:
                con = cx_Oracle.connect("system/Rajuoracledb#123")
                cursor = con.cursor()
                sql = "insert into menu values('%s', '%s')"
                args = (dish_name, rate)
                cursor.execute(sql % args)
                con.commit()
                msg = str(cursor.rowcount) + " records inserted"
                messagebox.showinfo("Success ", msg)
                entDish.delete(0, END)
                entRate.delete(0, END)
            except cx_Oracle.DatabaseError as e:
                con.rollback()
                print("eror  -->", e)
            finally:
                if cursor is not None:
                    cursor.close()
                if con is not None:
                    con.close()
    else:
        messagebox.showerror("Error ", "RATE SHOULD CONTAIN ONLY DIGITS")
        entRate.delete(0, END)
        entRate.focus()

def InsertMenuIntoLB(LB):
    import cx_Oracle
    con = None
    cursor = None
    try:
        con = cx_Oracle.connect("system/Rajuoracledb#123")
        cursor = con.cursor()
        sql = "select * from menu"
        cursor.execute(sql)
        data = cursor.fetchall()
        mdata = ""
        for d in data:
            for i in range(4, 25):
                if len(d[0]) == i:
                    s = 25 - i
                    extra = " "*s
            mdata = mdata + str("            "+str(d[0])+"                      "+extra+"                               "  +str(d[1])) + "\n"
            LB.insert(END, mdata)
            mdata = ""
    except cx_Oracle.DatabaseError as e:
        print("issue", e)
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()

def addIntoEmp(ID, name, salary, entId, entName, entSalary):
    if ID == '' or salary == '' or name == '':
        messagebox.showerror("Error ", "Please fill all the fields")
    elif ID.isdigit():

        if name.isalpha():
            if salary.isdigit():
                ID = int(ID)
                salary = int(salary)
                if len(name) < 2 or len(name) > 20:
                        messagebox.showerror("Error ", "Employee name should contain atleast 2 and max 20 letters")
                        
                elif salary < 8000:
                    messagebox.showerror("Error ", "Salary cannot be less than 8000")
                else:    
                    import cx_Oracle
                    con = None
                    cursor = None
                    try:
                        
                        con = cx_Oracle.connect("system/Rajuoracledb#123")
                        cursor = con.cursor()
                        sql = "insert into hotel_employee values('%d', '%s', '%d')"
                        args = (ID, name, salary)
                        cursor.execute(sql % args)
                        con.commit()
                        msg = str(cursor.rowcount) + " records inserted"
                        messagebox.showinfo("Success ", msg)
                    except cx_Oracle.DatabaseError as e:
                        con.rollback()
                        print("eror  -->", e)
                        messagebox.showerror("error", "EMPLOYEE WITH ID = "+str(ID)+" ALREADY EXIXTS")
                    finally:
                        if cursor is not None:
                            cursor.close()
                        if con is not None:
                            con.close()

            else:
                messagebox.showerror("Error ", "SALARY SHOULD CONTAIN ONLY DIGITS")
                entSalary.delete(0, END)
                entSalary.focus()
        else:
            messagebox.showerror("error", "Name cannot contain numbers and special characters")
            entName.delete(0, END)
            entName.focus()

    else:
        messagebox.showerror("Error ", "ID SHOULD CONTAIN ONLY DIGITS")
        entId.delete(0, END)
        entId.focus()

def InsertEmpIntoLB(LB):
    import cx_Oracle
    con = None
    cursor = None
    try:
        con = cx_Oracle.connect("system/Rajuoracledb#123")
        cursor = con.cursor()
        sql = "select * from hotel_employee order by ID"
        cursor.execute(sql)
        data = cursor.fetchall()
        mdata = ""
        for d in data:
            mdata = mdata + str("            "+str(d[0])+"            "  +str(d[1])+ "                                 "+str(d[2])   ) + "\n"
            LB.insert(END, mdata)
            mdata = ""
    except cx_Oracle.DatabaseError as e:
        print("issue", e)
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()

def deleteFromEmployee(ID, entID):
    if ID == '':
        messagebox.showerror("error", " ID CANNOT BE BLANK")
    elif ID.isdigit():
        import cx_Oracle
        con = None
        cursor = None
        try:
            con = cx_Oracle.connect("system/Rajuoracledb#123")
            cursor = con.cursor()
            sql = "delete from hotel_employee where ID ="+ID
            cursor.execute(sql)
            con.commit()
            if cursor.rowcount == 0:
                messagebox.showerror("error", "EMP ID = "+ID+" DOESNT EXISTS")
            else:
                msg = str(cursor.rowcount) + " Employee with Id ="+str(ID)+" Deleted"
                messagebox.showinfo("Success ", msg)
        except cx_Oracle.DatabaseError as e:
            print("issue", e)
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()
    else:
        messagebox.showerror("error", "ID  cannot contain LETTERS and SPECIAL CHARACTERS")


def deleteFromMenu(dish, entDish):
    if dish == '':
        messagebox.showerror("error", "DISH NAME CANNOT BE BLANK")
    else:
        import cx_Oracle
        con = None
        cursor = None
        try:
            con = cx_Oracle.connect("system/Rajuoracledb#123")
            cursor = con.cursor()
            sql = "delete from menu where dish = '"+dish+"'"
            cursor.execute(sql)
            con.commit()
            if cursor.rowcount == 0:
                messagebox.showerror("error", "DISH NAME = "+dish+" DOESNT EXISTS")
            else:
                msg = str(cursor.rowcount) + " dish with name  ="+ dish+" Deleted"
                messagebox.showinfo("Success ", msg)
        except cx_Oracle.DatabaseError as e:
            print("issue", e)
        finally:
            if cursor is not None:
                cursor.close()
            if con is not None:
                con.close()
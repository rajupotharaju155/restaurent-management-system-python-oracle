#import fpdf
from fpdf import FPDF
from tkinter import messagebox
import datetime
import time
import random
done = 2
def generatePdf(tableName):
    global done
    import cx_Oracle
    con = None
    cursor = None
    try:
        con = cx_Oracle.connect("system/Rajuoracledb#123")
        cursor = con.cursor()
        sql = "select * from "+tableName+" order by itemNo"
        cursor.execute(sql)
        data = cursor.fetchall()
        if cursor.rowcount == 0:
            print("order was empty, pdf not generated!")
        else:
            
            li = []
            ld = []
            lr = []
            lq = []
            la = []
            for d in data:   
                li.append(d[0])    
                ld.append(d[1])
                lr.append(d[2])
                lq.append(d[3])
                la.append(d[4])
            #getting amount
            q = "select sum(itemamount) from "+tableName
            cursor.execute(q)
            data = cursor.fetchall()
            amount = data[0][0]

            #getting amount after adding 9% tax
            amount_to_pay = amount + amount*0.09
            
            #getting date
            d = datetime.datetime.now()
            dt = d.strftime("%d / %m / %Y" )
            t = d.strftime("%I:%M:%S %p " )

            #getting random 3 digit number for reciept number
            rno = random.randint(100,999)

            #creatinf pdf object
            pdf = FPDF('P','mm', (150,260))
            pdf.add_page()
            pdf.set_font("Times",'BI', 18)
            #adding header
            pdf.set_xy(x=38.0, y=7)
            pdf.write(15, "Python Developers' Restaurent")
            
            pdf.set_font("Arial",'B', 9)
            pdf.set_xy(x=10, y=19)
            pdf.write(5, "Date : "+dt )

            pdf.set_xy(x=10, y=23)
            pdf.write(5, "Time : "+t )

            pdf.set_xy(x=110, y=19)
            pdf.write(5, "Table : "+tableName )

            pdf.set_xy(x=110, y=23)
            pdf.write(5, "Reciept No : "+str(rno) )

            pdf.set_font("Arial",'B', 12)
            pdf.set_xy(x=10.0, y=30)
            pdf.dashed_line(10, 30, 140, 30, dash_length = 1, space_length = 1)
            pdf.write(10, "Item no           Dish Name              Rate        Quanitity       Amount")
            pdf.dashed_line(10, 40, 140, 40, dash_length = 1, space_length = 1)

            #printing the content of dish on pdf
            m = 40
            for k in range(len(li)):
                pdf.set_xy(x=14.0, y=m)
                pdf.write(10, str(li[k]))
                pdf.set_xy(x=30.0, y=m)
                pdf.write(10, str(ld[k]))
                pdf.set_xy(x=80.0, y=m)
                pdf.write(10, str(lr[k]))
                pdf.set_xy(x=100.0, y=m)
                pdf.write(10, str(lq[k]))
                pdf.set_xy(x=124.0, y=m)
                pdf.write(10, str(la[k]))
                m = m + 10
            pdf.dashed_line(10, m, 140, m, dash_length = 1, space_length = 1)

            pdf.image("stamp.jpg", x = 80, y = 150, w = 50, h = 40)

            #adding footer
            pdf.dashed_line(10, 200, 140, 200, dash_length = 1, space_length = 1)   
            pdf.set_xy(x=60.0, y=201)
            pdf.write(10, "Total amount                     = Rs. "+str(amount))
            pdf.set_xy(x=60.0, y=205)
            pdf.write(10, "SGST                                   = 4.5%")
            pdf.set_xy(x=60.0, y=210)
            pdf.write(10, "CGST                                   = 4.5%")
            
            pdf.dashed_line(10, 219, 140, 219, dash_length = 1, space_length = 1)
            pdf.set_xy(x=60.0, y=217)
            pdf.write(10, "TOTAL AMOUNT TO PAY = Rs. "+str(amount_to_pay))
            pdf.dashed_line(10, 225, 140, 225, dash_length = 1, space_length = 1)
            pdf.set_xy(x=42.0, y=225)
            pdf.set_font("Courier",'BI', 17)
            pdf.write(8, "Please Visit Again")
            pdf.set_font("Times",'BIU', 10)
            pdf.set_xy(x=45.0, y=232)
            pdf.write(5, "Developed By Raju Potharaju", "www.github.com/rajupotharaju155")
            #pdf.set_draw_color(255, 0, 0)
            pdf.set_line_width(1)
            pdf.line(10, 10, 140, 10)
            pdf.line(10, 10, 10, 250)
            pdf.line(140, 10, 140, 250)
            pdf.line(10, 250, 140, 250 )
            #pdf.cell(w = 100, h = 100, txt = mdata, border = 1, ln = 0, align = 'l', fill = False)
            try:
                pdf.output(tableName+".pdf")
                messagebox.showinfo("PDF CREATED ", "BILL GENERATED SUCCESULLY")
                print("*****************pdf created**************")
                done = 1
            except PermissionError as e:
                done = 0
                messagebox.showwarning("BILL CANNOT BE GENERATED", "PLEASE CHECK IF SAME TABLE PDF IS ALREADY OPENED IN ANOTHER TAB")
    except cx_Oracle.DatabaseError as e:
        print("issue", e)
    finally:
        if cursor is not None:
            cursor.close()
        if con is not None:
            con.close()
    return 0
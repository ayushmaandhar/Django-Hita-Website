#this program replaces all variables in Agreement1.txt to dynamic values and saves it as a sellername_to_buyername.txt 
from fpdf import FPDF
from .models import agreementsellform

def replacev(dict):
    name_of_file = dict['sn'] + "_to_" + dict['bn']
    name_of_file = name_of_file.replace(' ','_')
    f = open("sprofile/all_txt/Agreement1.txt", "r")
    newf = open("sprofile/all_txt/" + name_of_file.replace(' ','_') + ".txt", "w")
    i = 1

    dict1 ={
        "$$$1": "agree_address",
        "$$$2": "agree_date",
        "$$$3": "seller_name",
        "$$$4": "seller_age",
        "$$$5": "seller_occ",
        "$$$6": "seller_address",
        "$$$7": "buyer_name",
        "$$$8": "buyer_age",
        "$$$9": "buyer_occ",
        "$$$10": "buyer_address",
        "$$$11": "property_address",
        "$$$12": "price",
        "$$$13": "token_amount",
        "$$$14": "bal_amount",
        "$$$15": "bal_date",
        "$$$16": "extra_variable"

    }


    dict2 = {
        "agree_address":dict['poa'],
        "agree_date":dict['doa'],
        "seller_name":dict['sn'],
        "seller_age":dict['sage'],
        "seller_occ":dict['so'],
        "seller_address":dict['sadd'],
        "buyer_name":dict['bn'],
        "buyer_age":dict['bage'],
        "buyer_occ":dict['bo'],
        "buyer_address":dict['badd'],
        "property_address":dict['padd'],
        "price":dict['total'],
        "token_amount":dict['token'],
        "bal_amount":dict['balance'],
        "bal_date":dict['bdate'],
        "extra_variable":dict['bdate'],
    }



    for line in f:
        variable = "$$$" + str(i)
        variable2 = "$$$" + str(i+1) #if a line has 2 var
        words = line.split()
        
        if(variable) not in words:
            print(line)
            newf.write(line)

        elif(variable) in words:
            if(variable2) in words:
                newline0 = line.partition(variable)[0]  #remove 'r'
                newline0 = newline0 + " " + variable 
                newline0 = newline0.replace(variable, dict2[dict1[variable]]) 

                newline2 = line.partition(variable)[2]
                newline2 = newline2.replace(variable2, dict2[dict1[variable2]])

                newline = newline0 + newline2
                print(newline)
                newf.write(newline)
                i = i+2 #because two variable replaced in one iteration

            else:
                newline = line.replace(variable, dict2[dict1[variable]])
                print(newline)
                newf.write(newline)
                i = i+1 



        # elif(variable and variable2) in words:
        #     if (variable) in words:
        #         newline = line.replace(variable, dict2[dict1[variable]])
            
        #     if (variable2) in words:
        #         newline = line.replace(variable2, dict2[dict1[variable2]])
        #     print(newline)
        #     newf.write(newline)
        #     i = i+1


    newf.close()
    f.close() 

    # save FPDF() class into a 
    # variable pdf
    pdf = FPDF()
    
    # Add a page
    pdf.add_page()

    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)

    
    # open the text file in read mode

    f = open("sprofile/all_txt/" + name_of_file  + ".txt", "r")
    
    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

    # def namepdf():
    #     pdfname = "sprofile/all_txt/" + name_of_file + ".pdf"
    #     return pdfname

    pdf.output('sprofile/all_txt/hey.pdf') 
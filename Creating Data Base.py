# 1) crearting a DateBase

def crearting_a_DateBase():

    global Data_Base_
    print ("h")
    print("")


    print("To creat a Date Base Follow the instructions ")
    print("")

    Data_Base_Name = input( "Enter the Date Base name =   ")
    print("")



def Creating_Table():

    print( "Now Enter the Table information ")
    print("")

    Table_Name = input("Enter Table name =  ")

    print("")

    First_Row = input("What would you like to call your first row = ")
    print("")

    Available_Types = ("Available_Types are: "   "INT" " , " "VARCHAR" " , " "Text" " , " "DATE")
    print(Available_Types)
    print("")

    Type = input("choose the Type of Data you want to Insert = ")
    print("")


    Length = input("Choose a Length/Value according to your Data Type = ")
    print("")

    Second_Row = input ("What would you like to call your Second Row = ")
    print("")

    Available_Types = ("Available_Types are: "   "INT" " , " "VARCHAR" " , " "Text" " , " "DATE")
    print(Available_Types)
    print("")

    Type2 = input("choose the Type of Data you want to Insert = ")
    print("")


    Length2 = input ("Choose a Length/Value according to your Data Type = ")
    print("")

    Thrid_Row = input("What would you like to call your Third Row = ")
    print("")

    Available_Types = ("Available_Types are: "   "INT" " , " "VARCHAR" " , " "Text" " , " "DATE")
    print(Available_Types)
    print("")

    Type3 = input("choose the Type of Data you want to Insert = ")
    print("")

    Available_Types = ("Available_Types are: "   "INT" " , " "VARCHAR" " , " "Text" " , " "DATE")
    print(Available_Types)
    print("")

    Length3 = input("Choose a Length/Value according to your Data Type = ")
    print("")


    print("This is Code  To Create a Database: ")
    print("")

    print("CREATE DATABASE " + Data_Base_Name + ";")



    print(
        "CREATE TABLE" + "`" + Data_Base_Name + "`" + "." + "`" +  Table_Name + "`" +
    "(" + "`" + First_Row + "` " + Type + "(" + Length + ")" +  "NOT NULL AUTO_INCREMENT," + "`" + Second_Row + "` " + Type2 + "(" + Length2 + ")"
    "NOT NULL," + "`" + Thrid_Row + "` " + Type3 + "(" + Length3 + ")" + "NOT NULL,PRIMARY KEY" +
        "(" + "`" + First_Row + "`" + "))" +
    "ENGINE = InnoDB" )

    print("")
    print(" will Done ")
    print("")
    print("Copyrights MOODY.2019 \u00a9")
    print("")


crearting_a_DateBase()
Creating_Table()

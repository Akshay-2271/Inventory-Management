import csv
from tempfile import NamedTemporaryFile
import shutil
def supplier_id_generator():
        with open('supplier.csv', 'r') as csvfile:
                reader=csv.DictReader(csvfile)
                i=1
                for r in reader:
                        if int(r['sup_id'])==i:
                                i=i+1
        return i
def create_supplier():
        with open('supplier.csv', 'a+') as csvfile:
                columns = ['sup_name', 'sup_id', 'sup_city', 'sup_contact', 'sup_email']
                writer = csv.DictWriter(csvfile, fieldnames = columns)
                writer.writeheader()
                sup_name = input("Enter New Supplier's Name!\n")
                sup_id = supplier_id_generator()
                print('Unique Supplier ID Generated : ', sup_id)
                sup_city = input("Enter New Supplier's City!\n")
                sup_contact = int(input("Enter New Supplier's Contact Number!\n"))
                sup_email = input("Enter New Supplier's Email Id!\n")
                writer.writerow({'sup_name':sup_name, 'sup_id':sup_id, 'sup_city':sup_city, 'sup_contact':sup_contact, 'sup_email':sup_email})
def s_searchbyname():
        with open('supplier.csv','r') as csvfile:
                name=input('Enter Supplier Name!\n')
                reader=csv.DictReader(csvfile)
                for r in reader:
                        if r['sup_name'] == name:
                                print('Name : ', r['sup_name'], '\n', 'Id : ', r['sup_id'],'\n', 'City : ', r['sup_city'], '\n', 'Contact No :', r['sup_contact'], '\n', 'Email id : ', r['sup_email'])
def s_searchbyid():
        with open('supplier.csv','r') as csvfile:
                id=int(input('Enter Supplier ID!\n'))
                reader=csv.DictReader(csvfile)
                for r in reader:
                        if r['sup_id'] == id:
                                print('Name : ', r['sup_name'], '\n', 'Id : ', r['sup_id'],'\n', 'City : ', r['sup_city'], '\n', 'Contact No :', r['sup_contact'], '\n', 'Email id : ', r['sup_email'])
def search_supplier():
        ss_choice=0
        while(ss_choice!=3):
                print("Enter 1 to search supplier by name!\nEnter 2 to search supplier by id!\nEnter 3 to exit supplier search!\n")
                ss_choice=int(input("Enter your choice!\n"))
                if ss_choice==1 :
                        s_searchbyname()
                elif ss_choice==2 :
                        s_searchbyid()
                else:
                        print("Invalid Input! Try again!\n")
def update_supplier_info():
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        columns = ['sup_name', 'sup_id', 'sup_city', 'sup_contact', 'sup_email']
        with open('supplier.csv', 'r') as csvfile, tempfile:
                reader = csv.DictReader(csvfile)
                writer = csv.DictWriter(tempfile, fieldnames=columns)
                writer.writeheader()
                suppp_name=input('Enter the name of the supplier you want to modify!\n')
                for r in reader:
                        if r['sup_name'] == suppp_name:
                                print('Enter 1 to update supplier name.\nEnter 2 to update supplier id.\nEnter 3 to update supplier city.\nEnter 4 to update supplier contact no.\nEnter 5 to update supplier email id.\n')
                                choice=int(input('Enter your choice!\n'))
                                if(choice==1):
                                        r['sup_name']=input("Enter updated name!\n")
                                elif(choice==2):
                                        r['sup_id']=int(input("Enter updated id!\n"))
                                elif(choice==3):
                                        r['sup_city']=input("Enter updated city!\n")
                                elif(choice==4):
                                        r['sup_contact']=int(input("Enter updated contact!\n"))
                                elif(choice==5):
                                        r['sup_email']=int(input("Enter updated email id!\n"))
                                else:
                                        print("Invalid Input!\n")
                        r = {'sup_name':r['sup_name'], 'sup_id':r['sup_id'], 'sup_city':r['sup_city'], 'sup_contact':r['sup_contact'], 'sup_email':r['sup_email']}
                        writer.writerow(r)
        shutil.move(tempfile.name, 'supplier.csv')
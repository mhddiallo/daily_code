#Mohamed Diallo - Day 3: 05/06/2021
#Description: Create a dictionnary with contact informations and print them.

contact = {"Full_Name": "Mohamed Diallo", "Phone": 771111111, "Adresse": "112 Mamelles Elevage, Dakar", "Pays": "Sénégal"}
for key, value in contact.items():
    print(key, ": ", value)
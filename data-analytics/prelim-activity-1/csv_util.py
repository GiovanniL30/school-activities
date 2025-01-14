import csv

def read(filename):
    rows = []
    
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader) 

        for row in csvreader:
            rows.append(row) 

    return {"fields": fields, "rows": rows}  

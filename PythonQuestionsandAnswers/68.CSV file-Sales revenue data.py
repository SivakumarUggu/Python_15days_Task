#Write a program that reads a csv file and finds the total sales revenue
#for a specific product.
import csv
list_data=[]
total_sales=0
count=0
with open('C:\\Users\\Lenovo\\Desktop\\Sales_September_2019.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        header=next(csv_reader)
        header_skipped=False
        for row in csv_reader:
            if not header_skipped:
                header_skipped=True
                continue

            #header[1],header[3]=row[1],row[3]
            list_data.append((row[1],row[3]))

        for product,price in list_data:
            if product=='USB-C Charging Cable':
                count=count+1
                total_sales=total_sales+float(price)
        print(f'Total number of {product} are: {count}')
        print(f'Total_sales is: ${total_sales}')

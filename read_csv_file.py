import csv
class read_csv_data:
    def fetch_csv_data(self,filename):
        # filename="csv1.csv"
        with open(filename)as fp:
            Dict_obj=list(csv.DictReader(fp))
            return Dict_obj

# obj=read_csv_data()
# obj.fetch_csv_data("csv1.csv")
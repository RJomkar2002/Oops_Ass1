from json import dump
from textwrap import indent

from read_csv_file import read_csv_data
from read_text_file import read_text_data
class merge_process(read_csv_data,read_text_data):

    def merge(self):

        all_data_list=[]
        csv_file_name="csv1.csv"
        text_file_name="text1.txt"

        csv_data=super().fetch_csv_data(csv_file_name)
        text_data=super().fetch_text_data(text_file_name)

        all_data_list.extend(csv_data)
        all_data_list.append(text_data)

        return all_data_list

    def store(self,allDataJsonFile):
        all_data_list=merge_process.merge(self)
        with open(allDataJsonFile,"a") as fp:
            dump(all_data_list,fp)
            # for data in all_data_list:
            #     dump(data,fp)
            #     fp.write("\n")

def main():
    All_data_json_file="alldata.json"
    obj = merge_process()
    obj.store(All_data_json_file)

if __name__=="__main__":
    main()









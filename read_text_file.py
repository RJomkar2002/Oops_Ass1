class read_text_data:
    text_data_dict={}
    def fetch_text_data(self,filename):
        with open(filename)as fp:
            self.text_data_dict["text_data"]=fp.read()
            # print(self.text_data_dict)
            return self.text_data_dict


# obj=read_text_data()
# obj.fetch_text_data("text1.txt")
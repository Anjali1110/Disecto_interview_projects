from searchquery import search
import json
import pandas as pd
import random
import string

class benchmark():
    def __init__(self):
        self.present_name_list=[]
        self.present_phone_list=[]
        self.random_phone_list=[]
        self.random_name_list=[]
  
    def get_present_top100data(self):
        with open('sample_data-240k-1.json', 'r', encoding='utf-8-sig') as f:
            all_data = json.loads(f.read())
            res_list = [i for n, i in enumerate(all_data['results']) ]
        # 120 because needing atleast 100 unique name and numbers
        for i in range(120):
            Name = res_list[i].get("Name", None)
            Number = res_list[i].get("Number", None)
            self.present_name_list.append(Name)
            self.present_phone_list.append(Number)

        return self.present_name_list, self.present_phone_list

    def generate_random_100Number(self):
        for i in range(100):
            number = random.randint(1000898989,8888888888)
            random_name=''.join(random.choices(string.ascii_uppercase, k = 7))
            self.random_phone_list.append(number)
            self.random_name_list.append(random_name)
        
        return self.random_phone_list, self.random_name_list
  
    def create_search_latency_info(self,data_list,field,file_name):
        dic_search_data={}
        for data in data_list:
            res = search(data, field)
            time = res['took']
            dic_search_data[data] = time
        df = pd.DataFrame(dic_search_data.items(), columns=["Field", "Time"])
        df.to_csv(file_name)
    
    def analyse_latency_info(self):
        df = pd.read_csv("present_name.csv")
        print("Present Name - Min - {}, Max - {}, Avg - {}, P95 - {}"
                .format(df["Time"].min(), df["Time"].max(), df["Time"].mean(), df["Time"].quantile(0.95)))
        df = pd.read_csv("present_phone.csv")
        print("Present Phone - Min - {}, Max - {}, Avg - {}, P95 - {}"
                .format(df["Time"].min(), df["Time"].max(), df["Time"].mean(), df["Time"].quantile(0.95)))
        df = pd.read_csv("random_number.csv")
        print("Random Phone - Min - {}, Max - {}, Avg - {}, P95 - {}"
                .format(df["Time"].min(), df["Time"].max(), df["Time"].mean(), df["Time"].quantile(0.95)))
        df = pd.read_csv("random_name.csv")
        print("Random Name - Min - {}, Max - {}, Avg - {}, P95 - {}"
                .format(df["Time"].min(), df["Time"].max(), df["Time"].mean(), df["Time"].quantile(0.95)))

if __name__ == '__main__':
    benchmark = benchmark()
    present_name_list, present_phone_list = benchmark.get_present_top100data()
    benchmark.create_search_latency_info(present_name_list, "Name", "present_name.csv")
    benchmark.create_search_latency_info(present_phone_list, "Number", "present_phone.csv")
    random_phone_list, random_name_list = benchmark.generate_random_100Number()
    benchmark.create_search_latency_info(random_phone_list, "Number", "random_number.csv")
    benchmark.create_search_latency_info(random_name_list, "Name", "random_name.csv")
    benchmark.analyse_latency_info()
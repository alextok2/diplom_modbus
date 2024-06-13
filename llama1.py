from llama_cpp import Llama
from sqlite1 import create_tables, delete_file, get_table_names, get_fields_names, create_records, count_records, find_primary_key, find_max_primary_key, get_names_of_tables
import re
import random

# llm = Llama(model_path="/Users/alextok/Documents/Code/diplom/llama.cpp/models/mistral-7b-v0.1.Q4_K_M.gguf")
# llm = Llama(model_path="F:/-/Code/diplom/nous-capybara-limarpv3-34b.Q3_K_S.gguf", n_threads=16, n_gpu_layers=42)
# llm = Llama(model_path="F:/-/Code/diplom/nous-capybara-limarpv3-34b.Q4_K_M.gguf", n_threads=16, n_gpu_layers=28)
# llm = Llama(model_path="F:/-/Code/diplom/mixtral_11bx2_moe_19b.Q5_K_M.gguf", n_threads=16, n_gpu_layers=30)
# llm = Llama(model_path="D:/Faraday models/mistral.mixtral-8x7b.instruct-v0.1.gguf_v2.q4_k_m.gguf", n_threads=16)
# llm = Llama(model_path="D:/Faraday models/llama2.13b.airoboros-3.1.1.gguf_v2.q4_k_m.gguf", n_threads=16)
# llm = Llama(model_path="F:/-/Code/diplom/phind-codellama-34b-v2.Q4_K_M.gguf", n_threads=16, n_gpu_layers=28)

# llm = Llama(model_path="C:/Users/user/Downloads/nous-hermes-2-solar-10.7b.Q5_K_M.gguf", n_threads=16, n_gpu_layers=49, n_ctx=2048)





def create_text_tables(llm):
    
    text = '''A:create sql database for a power plant, use sqlite3. sql database should have at least 20 tables. Don't use BLOB values. There should be a table with employees\nQ: This is a basic structure for the database.\n1. A table for employees:\n```CREATE TABLE Employees'''
    output = llm(f"{text}", temperature=1, echo=True, max_tokens=-1)

    # print(output["choices"])
    text = output["choices"][0]["text"]

    try:
        matches = re.findall(r'\b20\. ', text)
        if len(matches) < 1:
            raise ValueError("Таблиц меньше чем 20")
        create_tables(text)
        return 0

    except Exception as e:
        print(f'{str(e)}')
        delete_file('database.db')
        create_text_tables(llm)

# output = llm("Q: I need 5 names for logins. Can you help me? A:alextok, ", max_tokens=64,temperature=1, stop=["Q:", "\n"], echo=True, top_p=0.95, top_k=0.05)



# llm = Llama(model_path="C:/Users/user/Downloads/mistral-7b-instruct-v0.2.Q5_K_M.gguf", n_threads=16, n_gpu_layers=33, n_ctx=4096)
llm = Llama(model_path="C:/Users/user/Downloads/WizardLM-2-7B.Q5_K_M.gguf", n_threads=16, n_gpu_layers=33, n_ctx=4096)
create_text_tables(llm)


names = get_names_of_tables()


def decide_how_many_values_in_tables(llm):
    
    text = f'''Q:I have a database for a power plant. I need to add values in each table. How many records in each table should I add to make a database realistic? I have this tables: {names}\n Make sure that your response should only have numbers of records in it. the table must not contain more than 1000 records.\nA: The number of records you should add to each table in your database depends on the specific use case and the level of complexity you want to simulate. However, here’s a general guideline you can follow to make your database realistic:\n1. Employees: 25\n2.'''
    output = llm(f"{text}", temperature=1, echo=True, max_tokens=-1)

    text = output["choices"][0]["text"]
    print(text)

    try:
        matches = re.findall(r'^\d+\.\s+(\w+):\s+(\d+)', text, re.MULTILINE)
        if len(matches) < 19:
            raise ValueError("Количество записей для таблиц меньше чем 19")
        
        data_dict = {name: int(value) for name, value in matches}
        print(data_dict)
        return data_dict
    
    except Exception as e:
        print(f'{str(e)}')
        return decide_how_many_values_in_tables(llm)
        

    




def fill_records_in_table(llm, tables_and_count_of_records):
    print(len(list(tables_and_count_of_records.keys())))
    # for count_of_tables in range(1):
    for count_of_tables in range(len(list(tables_and_count_of_records.keys()))):
        
        
    
        table = list(tables_and_count_of_records.keys())[count_of_tables]
        print(table)
        fields = get_fields_names(table)
        count_of_records = list(tables_and_count_of_records.values())[count_of_tables]

        primary_key_name = find_primary_key(table)
        max_primary_key = find_max_primary_key(primary_key_name, table)
        if max_primary_key is None:
            max_primary_key = 0


        random_number = random.uniform(-1, 1)
        distorted_count_of_records = (count_of_records/100 * 5 * random_number) + count_of_records
        count_of_records = round(distorted_count_of_records, 0)

        count_of_existed_records = count_records(table)
        count_of_required_records = count_of_records - count_of_existed_records

        print(f'Количество существующих записей в таблице {table}: {count_of_existed_records}\nКоличество запланированных записей в таблице {table}: {count_of_records}')
        if count_of_records < 0:
            continue

        outer_loop_iterations = 15
        inner_loop_iterations = count_of_required_records // outer_loop_iterations
        remainder = count_of_required_records % outer_loop_iterations


        try:
            while count_of_existed_records < count_of_records:

                for j in range(int(inner_loop_iterations)):
                    max_primary_key = find_max_primary_key(primary_key_name, table)
                    if max_primary_key is None:
                        max_primary_key = 0
                    text = f'''Q:I have a database for a russian power plant. I need to generate {int(inner_loop_iterations)} records in table {table}. Table has these fields: {fields}\n Values should be in russian. Use sqlite. Give {outer_loop_iterations} varietions. I need {primary_key_name} field values to go from {max_primary_key+1} to {max_primary_key+1 + outer_loop_iterations}\nA: Here's values {primary_key_name} field from {max_primary_key+1} to {max_primary_key+1 + outer_loop_iterations} to insert records into the table using SQLite:\n``` INSERT OR IGNORE INTO'''
                    output = llm(f"{text}", temperature=1, echo=True, max_tokens=-1)

                    text = output["choices"][0]["text"]
                    print(text)
                    create_records(text, False)


                max_primary_key = find_max_primary_key(primary_key_name, table)
                if max_primary_key is None:
                    max_primary_key = 0
                text = f'''Q:I have a database for a russian power plant. I need to generate {int(remainder)} records in table {table}. Table has these fields: {fields}\n Values should be in russian. Use sqlite. Give {remainder} varietions. I need {primary_key_name} field values to go from {max_primary_key+1} to {max_primary_key+1 + int(remainder)}\nA: Here's values {primary_key_name} field from {max_primary_key+1} to {max_primary_key+1 + int(remainder)} to insert records into the table using SQLite:\n``` INSERT OR IGNORE INTO'''
                output = llm(f"{text}", temperature=1, echo=True, max_tokens=-1)

                text = output["choices"][0]["text"]

                print(text)
                create_records(text, False)

                count_of_existed_records = count_records(table)
                


        
        except Exception as e:
            print(f'{str(e)}')
            fill_records_in_table(llm,tables_and_count_of_records)



    # try:
    #     matches = re.findall(r'^\d+\.\s+(\w+):\s+(\d+)', text, re.MULTILINE)
    #     if len(matches) < 20:
    #         raise ValueError("Количество записей для таблиц меньше чем 20")
        
    #     data_dict = {name: int(value) for name, value in matches}
    #     print(data_dict)
    #     return data_dict
    
    # except Exception as e:
    #     print(f'{str(e)}')
    #     return decide_how_many_values_in_tables(llm)



tables_and_count_of_records = decide_how_many_values_in_tables(llm)
fill_records_in_table(llm, tables_and_count_of_records)




# with open('text.txt', 'a') as f:
#     f.write(text +'\n\n\n\n\n\n\n\n\n')
# print(text)

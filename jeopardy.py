import pandas as pd
import random

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.width', None)

jeopardy = pd.read_csv('jeopardy.csv')

#print(jeopardy)
#print(jeopardy.columns)

#fix column names
jeopardy.columns = [col.strip() for col in jeopardy.columns]
#print(jeopardy.columns)
#print(jeopardy)

#print(jeopardy.Question)

def filter_questions(df, word_list):
    #print(all(word in df.Question for word in word_list))
    filtered_df = df[df.Question.apply(lambda x: all(word.lower() in x.lower() for word in word_list))]
    #print(filtered_df)
    return filtered_df
    
    
print(filter_questions(jeopardy, ["For"]))
king_england_df = filter_questions(jeopardy, ["King", "England"])

print(king_england_df.Question)
print(len(king_england_df))

print(jeopardy)

jeopardy['Value_float'] = jeopardy.Value.apply(lambda x: float(x.strip('$').replace(',','')) if x != 'None' else 0)
#print(jeopardy)
#print(jeopardy.Value_float)

def calculate_avg_value(df):
    return df.Value_float.mean()

king_df = filter_questions(jeopardy, ["King"])
print(len(king_df))
print(calculate_avg_value(king_df[king_df.Value_float != 0]))

def unique_answers(df):
    return df.Answer.value_counts()

king_df_value_counts = unique_answers(king_df)
print(king_df_value_counts)
print(len(king_df_value_counts))



#add decades column
print(jeopardy)

test_date = '2004-12-31'
air_date_year = int(test_date.split('-')[0])
#print(air_date_year)

def determine_decade(air_date):
    year = int(air_date.split('-')[0])
    
    if year >= 1980 and year <= 1989:
        return "80s"
    elif year >= 1990 and year <= 1999:
        return "90s"
    elif year >= 2000 and year <= 2009:
        return "00s"
    elif year >= 2010 and year <=2019:
        return "10s"

jeopardy['Decade'] = jeopardy['Air Date'].apply(determine_decade)

#print(jeopardy[jeopardy["Air Date"] == "2004-12-31"].Decade)
#print(jeopardy[jeopardy["Air Date"] == "1996-12-06"].Decade)

computer_df = filter_questions(jeopardy, ["Computer"])
print(computer_df)

computer_counts_df = computer_df.groupby("Decade").Question.count().reset_index()
#print(computer_counts_df)
computer_counts_df = computer_counts_df.rename(columns={"Question": "Question counts"})
print(computer_counts_df)


#print(jeopardy)
#group by round and category
round_category_df = jeopardy.groupby(["Category", "Round"]).Question.count().reset_index().rename(columns={"Question": "Counts"})
print(round_category_df)

   
#print(round_category_df[round_category_df.Category.apply(lambda x: x.lower() == "literature")])
literature_count_df = round_category_df[round_category_df.Category.apply(lambda x: x.lower() == "literature")].reset_index(drop=True)
print(literature_count_df)

def get_random_question(df):
    total = len(df)
    rand_number = random.randint(0, total - 1)
    rand_question = df.iloc[rand_number].Question
    answer = df.iloc[rand_number].Answer
    return rand_question, answer

def jeopardy_practice():
    random_question, answer = get_random_question(jeopardy)
    print("Question: {}".format(random_question))
    user_input = input("Who/What is _____?: ")
    
    if user_input.lower() == answer.lower():
        print("Correct!")
    else:
        print("Incorrect!")
    print("Answer: {}".format(answer))

jeopardy_practice()

    



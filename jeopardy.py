import pandas as pd
pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv('jeopardy.csv')

#print(jeopardy)
#print(jeopardy.columns)

#fix column names
jeopardy.columns = [col.strip() for col in jeopardy.columns]
print(jeopardy.columns)
print(jeopardy)

print(jeopardy.Question)

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

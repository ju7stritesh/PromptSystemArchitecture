import pandas as pd

def get_questions_answers():
    data= pd.read_csv("qa_database.csv")

    teachers = set(data.Teacher)
    select_teacher = input('Please select a teacher by typing their name (spell check) from the list - ' + str(teachers))

    if select_teacher != 'all':
        selected_questions = data.loc[data['Teacher'] == select_teacher]
    else:
        selected_questions = data

    questions = list(selected_questions.Question)
    answers = list(selected_questions.Answer)
    q_ids = list(selected_questions.QID)
    return questions, answers, q_ids

def get_all_questions_answers():
    data = pd.read_csv("qa_database.csv")

    selected_questions = data

    questions = list(selected_questions.Question)
    answers = list(selected_questions.Answer)
    q_ids = list(selected_questions.QID)
    return questions, answers, q_ids

def get_embeddings():
    data = pd.read_csv("embedding_database.csv")

    selected_questions = data

    embedings = list(selected_questions.embeddings)
    e_ids = list(selected_questions.QID)
    return embedings, e_ids

if __name__ == '__main__':
    print (get_questions_answers())

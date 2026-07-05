from database import connect_db
from nlp import preprocess

def GetAnswer(UserQuestion):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT question, answer FROM college_info")

    row = cursor.fetchall()

    words = preprocess(UserQuestion)

    for question, answer in row:
        if question.lower() in UserQuestion:
            cursor.close()
            connection.close()
            return answer
    
    cursor.close()
    connection.close()

    return "Sorry, I don't know this answer. Please contact the college office."
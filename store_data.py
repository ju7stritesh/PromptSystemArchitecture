import csv

Q1 = 'What is human rights education?'
A1 = 'Human rights education is a process that anyone, anywhere can undertake at any age to learn about their own human rights -- and the rights of others -- and how to claim them. It empowers people to develop the skills and attitudes to promote equality, dignity and respect in their own communities, societies and worldwide. '
Q2 = 'Do you think human rights education is useful whilst people are lacking basic things like food and drinking water?'
A2 = 'Yes. Human rights education empowers the people affected by human rights violations to hold individuals in positions of power, businesses and governments to account.  This can lead to long-term sustainable change and end cycles of dependency that can form when violations, such as the failure to provide access to food and drinking water, are not tackled as human rights abuses. '
Q3 = 'How do airplanes stay in the air?'
A3 = 'Planes stay in the air because of the shape of their wings. Air moving over the wing gets forced downwards, which pushes the wing up. This push is stronger than gravity, and so makes the plane fly.'
Q4 = 'True or False? Chameleons change colors only to blend into their environment.'
A4 = 'False. Chameleons also change colors for other reasons, like to regulate body temperature, when feeling aggression, and when feeling excited.'

t_table = {1 : 'Sarah', 2 : 'Richard'}
# q_table = {'q1' : Q1, 'q2' : Q2, 'q3' : Q3, 'q4' : Q4}

header = ['TID', 'QID', 'SID', 'Teacher', 'Subject', 'Question', 'Answer']
data = [
    ['1', '1', '1', t_table[1], 'Human Rights', Q1, A1],
        ['1', '2', '1', t_table[1], 'Human Rights', Q2, A2],
        ['2', '3', '2', t_table[2], 'Science', Q3, A3],
        ['2', '4', '2', t_table[2], 'Science', Q4, A4]
        ]

with open('qa_database.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)


contacts = {
    'number': 4,
    'students':
    [
        {'name':'Sarah Holderness', 'email':'sarah@example.com'},
        {'name':'Harry Potter', 'email':'harry@example.com'},
        {'name':'Maximum Salgado', 'email':'maximum@example.com'},
        {'name':'Ron Weasley', 'email':'ron@example.com'},
    ]
}

print('Student Emails:')
for student in contacts['students']:
    print(student ['email'])
    pip3 --version 
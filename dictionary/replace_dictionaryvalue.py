student_details = [
    {'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
    {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
    {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86}
]
for d in student_details:
    n = d.pop( 'V' )
    n1 = d.pop( 'VI' )
    d['V+VI'] = (n + n1) / 2
    print( d )

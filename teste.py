from datetime import datetime
#my_dates = ['2021-05-17T22:27:26Z','2021-05-17T22:27:27Z','2021-05-17T22:27:27Z','2021-08-19T19:10:41Z','2021-08-20T15:49:56Z','2021-04-16T18:07:03Z']
my_dates = [{'name': 'zag-horario', 'url': 'https://github.com/BenitoMarculanoRibeiro/ag-horario', 'archived': True, 'language': 'Java', 'fork': False, 'created_at': '2019-10-24T23:38:59Z', 'updated_at': '2022-05-05T19:55:54Z', 'pushed_at': '2019-10-25T00:04:58Z'},
            {'name': 'f-agiota', 'url': 'https://github.com/BenitoMarculanoRibeiro/AG-LM', 'archived': True, 'language': 'PHP', 'fork': False, 'created_at': '2020-08-06T16:29:52Z', 'updated_at': '2022-05-05T19:55:05Z', 'pushed_at': '2020-08-28T11:05:30Z'}]

my_dates.sort(key=lambda date: datetime.strptime(
    date['updated_at'], "%Y-%m-%dT%H:%M:%SZ"), reverse=True)
print(my_dates)
for i in my_dates:
    print(i['name'], i['updated_at'])


my_dates.sort(key=lambda name: name['name'])

for i in my_dates:
    print(i['name'], i['updated_at'])
text = 'f'
new_request = []
for i in my_dates:
    if text in my_dates[1]['name']:
        new_request.append(i)

h = [x for x in my_dates if text in x['name']]
for i in my_dates:
    print(i['name'])

for i in h:
    print(i['name'])

from airflow.sdk import dag,task

@dag(

)
def myDag():

    @task.python 
    def one(**kwargs):

        name='sumit'

        kwargs['ti'].xcom_push(key='id',value=name)
    
    @task.python
    def two(**kwargs):

        password='2432142542dskjnsk'

        kwargs['ti'].xcom_push(key='password',value=password)
    
    @task.python
    def third(**kwargs):

        username= kwargs['ti'].xcom_pull(task_ids='one',key='id')
        password= kwargs['ti'].xcom_pull(task_ids='two',key='password')

        print(f'the username is {username} and password is {password}')
    
    first = one()
    second = two()
    thirdd = third()

    first >> second >> thirdd 

myDag()

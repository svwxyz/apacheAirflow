from airflow.sdk import dag,task 

@dag(
        dag_id='Xcom2')
def myDag():

    @task.python
    def Starter(**kwargs):

        print('This dag is for encription send password JUST FOR DEMO')

    @task.python
    def encription(**kwargs):

        username = 'svwxyz'
        passwd = '28321yehdahut7%^%^%^GFGFF'
        kwargs['ti'].xcom_push(key='myuser',value=username)
        kwargs['ti'].xcom_push(key='pass',value=passwd)
    
    @task.python
    def show(**kwargs):

        username=kwargs['ti'].xcom_pull(task_ids='encription',key='myuser')
        password=kwargs['ti'].xcom_pull(task_ids='encription',key='pass')

        print(f'The passed username is {username} and the password is {password}')
    
    first=Starter()
    second=encription()
    third=show()

    first >> second >> third

myDag()
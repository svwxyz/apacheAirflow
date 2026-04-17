from airflow.sdk import dag,task

@dag(
        dag_id='Xcom'
)
def myDag():

    @task.python
    def stageOne(**kwargs):
        f_name='sumit'
        l_name='vishwakarma'

        kwargs['ti'].xcom_push(key='firstName',value=f_name)
        kwargs['ti'].xcom_push(key='lastName',value=l_name)
    
    @task.python
    def stageTwo(**kwargs):
        first = kwargs['ti'].xcom_pull(task_ids='stageOne',key='firstName')
        surname = kwargs['ti'].xcom_pull(task_ids='stageOne',key='lastName')

        FUllNAME=first.upper()+" "+surname.upper()

        kwargs['ti'].xcom_push(key='transformed',value=FUllNAME)
    
    @task.python
    def stageThree(**kwargs):
        print(f'Good Morning!!,{kwargs['ti'].xcom_pull(task_ids='stageTwo',key='transformed')}')

    
    first=stageOne()
    second=stageTwo()
    third=stageThree()

    first >> second >> third

myDag()

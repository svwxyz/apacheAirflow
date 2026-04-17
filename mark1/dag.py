from airflow.sdk import dag, task 

@dag(
        dag_id='Xcom_OldSchool'
)
def myDag():

    @task.python
    def extract():

        f_name='sumit'
        l_name='vishwakarma'

        return {
                    'first':f_name,
                    'second':l_name
        }
    

    @task.python
    def transform(data):
        fullName=data['first'].upper()+' '+data['second'].upper()

        return fullName
    
    @task.python
    def load(result):

        print(f"Hello {result}")
    
    first=extract()
    second=transform(first)
    third=load(second)

    first >> second >> third

myDag()
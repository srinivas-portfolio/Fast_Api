from fastapi import FastAPI, Body

app=FastAPI()

students = [
    {"name":"srihari","course":"DS","studentid":1},
    {"name":"srinu","course":"DA","studentid":2},
    {"name":"rajesh","course":"DS","studentid":3},
    {"name":"Srikanth","course":"DA","studentid":4}]

@app.get('/')
def home_page():
    return {"message":"welcome to FastAPI Fast_Api"}

@app.get('/get_all_students')
def view_all_students():
    return{"operation":"GET",
           "result":students}
@app.get('/get_single_student_by_id/{student_id}')
def single_student(student_id:int):
    for i in students:
        if i['studentid'] == student_id:
            return{
                "Request":"GET",
                "result":i
            }
    return {"message":"student id you are looking for is not avalable in student list"}

@app.post('/add_student')
def add_single_student(addnewsstudent=Body()):
    students.append(addnewsstudent)
    return{"operation":"POST","students details":students}

@app.put('/update_student_Details_by_id/{studentid}')
def single_student(name:str, course:str, studentid:int):
    for i in students:
        if i['studentid'] == studentid:
            previous = i.copy()
            i.update({"name": name, "course": course, "studentid": studentid})
            return {
                "Request": "PUT",
                "previous details": previous,
                "updated details": i
            }
    return {"message": "student id you are looking for is not avalable in student list"}

@app.delete('/delete_student_Details_by_id/{studentid}')
def delete_student(studentid:int):
    for i in students:
        if i['studentid'] == studentid:
            students.remove(i)
            return {
                "Request": "Delete",
                "deleted details": i
            }
    return {"message": "student id you are looking for is not avalable in student list"}



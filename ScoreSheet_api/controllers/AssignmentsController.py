from ScoreSheet_api import app
from flask import Flask, request, jsonify, json
from ScoreSheet_api.config.database import getDb
from ScoreSheet_api.helpers.DbUtillity import Convert_to_Json, Handle_error

import pymysql

# initial database
cursor = getDb().cursor()

@app.route('/assignments', methods=['GET'])
def getAssignments():
    
    teach_course_id = request.args.get('teachCourseId') 
    if (request.method == 'GET'):
        
        try: 
            query = "SELECT * From Assignments A WHERE A.TeachCourseId = {0}".format(teach_course_id)
            cursor.execute(query)
            res = cursor.fetchall()
            
            if(res == None):
                print("No Content")
                return ('',204)
        
        except pymysql.Error as err:
            print(err)
            return Handle_error(err, 500)
        
    return jsonify(res), 200



@app.route('/countAssignments', methods=['Get'])
def getCountAssignments():
    
    teach_course_id = request.args.get('teachCourseId')
    if(request.method == 'GET'):
        
        try:
            query = "SELECT COUNT(A.AssignmentId) as Count From Assignments A WHERE A.TeachCourseId = {0}".format(teach_course_id)
            cursor.execute(query)
            res = cursor.fetchone()
            
            if(res == None):
                return ('',204)
            
        except pymysql.Error as err:
            print(err)
            return Handle_error(err, 500)

        return jsonify(res), 200
    
    
@app.route('/addAssignment',methods=['POST'])
def addAssignment():
    
    teach_course_id = request.args.get('teachCourseId') 
    if(request.method == 'POST'):
        assignmentName = request.json['AssignmentName']
        fullScore = request.json['FullScore']
        
        try:
            query = "INSERT INTO Assignments (TeachCourseId, FullScore, AssignmentName) VALUES (%s,%s,%s)"
            cursor.execute(query, (int(teach_course_id), int(fullScore), assignmentName))  
            
            return jsonify(True), 200
        
        except pymysql.Error as err:
            print(err.args[0],err.args[1])
            return Handle_error(err, 500)  


@app.route('/deleteAssignment', methods=['POST'])
def deleteAssignment():
    
    AssignmentId = request.args.get('AssignmentId')
    if(request.method == 'POST'):
        
        try:
            query = "Delete From Assignments Where AssignmentId = {0}".format(int(AssignmentId))
            cursor.execute(query)
            return jsonify(True), 200
        
        except pymysql.Error as err:
            print(err)
            return Handle_error(err, 500)  
        
    return jsonify(False), 200
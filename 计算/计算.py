from flask import Flask
import pymysql

app = Flask(__name__)
#连接数据库
conn = pymysql.connect(host="localhost",port=3306,user="root",password="123456",
                       database="AHU_2021_TEST",charset="utf8")

#接口一为加法
@app.route('/adda=<operand1>&b=<operand2>', methods=['GET', 'POST'])
def add(operand1,operand2):
    operand1 = float(operand1)   #转化为float型
    operand2 = float(operand2)
    result = operand1 + operand2 #执行加法
    cursor = conn.cursor() #获取mysql光标
    sql = "select id from calc_record ORDER BY id DESC LIMIT 1" #sql语句，获取上一个id值
    cursor.execute(sql)    #执行sql语句
    id = cursor.fetchone() #获取到的id是一个元组
    if(id):
        id = int(id[0])+1  #如果元组不为空，将元组里的id转化成int型并加一
    else :
        id = 1             #如果元组为空，id为第一个
    sql1 = "insert into AHU_2021_TEST.calc_record(id,operand1,operator,operand2,result) values(%d,%f,\'%c\',%f,%f)"\
           %(id, operand1, '+', operand2, result)     #sql语句，插入本次记录到表calc_record
    cursor.execute(sql1)   #执行sql1语句
    conn.commit()          #数据库提交事务
    cursor.close()         #光标关闭
    return '%.2f' % result #页面返回运算值

#减法接口
@app.route('/suba=<operand1>&b=<operand2>',methods=['GET', 'POST'])
def sub(operand1,operand2):
    operand1 = float(operand1)   #转化为float型
    operand2 = float(operand2)
    result = operand1 - operand2 #执行减法
    cursor = conn.cursor() #获取mysql光标
    sql = "select id from calc_record ORDER BY id DESC LIMIT 1" #sql语句，获取上一个id值
    cursor.execute(sql)    #执行sql语句
    id = cursor.fetchone() #获取到的id是一个元组
    if(id):
        id = int(id[0])+1  #如果元组不为空，将元组里的id转化成int型并加一
    else :
        id = 1             #如果元组为空，id为第一个
    sql1 = "insert into AHU_2021_TEST.calc_record(id,operand1,operator,operand2,result) values(%d,%f,\'%c\',%f,%f)"\
           %(id, operand1, '-', operand2, result)     #sql语句，插入本次记录到表calc_record
    cursor.execute(sql1)   #执行sql1语句
    conn.commit()          #数据库提交事务
    cursor.close()         #光标关闭
    return '%.2f' % result #页面返回运算值


#乘法接口
@app.route('/multiplya=<operand1>&b=<operand2>',methods=['GET', 'POST'])
def mul(operand1,operand2):
    operand1 = float(operand1)   #转化为float型
    operand2 = float(operand2)
    result = operand1 * operand2 #执行乘法
    cursor = conn.cursor() #获取mysql光标
    sql = "select id from calc_record ORDER BY id DESC LIMIT 1" #sql语句，获取上一个id值
    cursor.execute(sql)    #执行sql语句
    id = cursor.fetchone() #获取到的id是一个元组
    if(id):
        id = int(id[0])+1  #如果元组不为空，将元组里的id转化成int型并加一
    else :
        id = 1             #如果元组为空，id为第一个
    sql1 = "insert into AHU_2021_TEST.calc_record(id,operand1,operator,operand2,result) values(%d,%f,\'%c\',%f,%f)"\
           %(id, operand1, '*', operand2, result)     #sql语句，插入本次记录到表calc_record
    cursor.execute(sql1)   #执行sql1语句
    conn.commit()          #数据库提交事务
    cursor.close()         #光标关闭
    return '%.2f' % result #页面返回运算值

#除法接口
@app.route('/divisiona=<operand1>&b=<operand2>',methods=['GET', 'POST'])
def div(operand1,operand2):
    operand1 = float(operand1)   #转化为float型
    operand2 = float(operand2)
    result = operand1 / operand2 #执行除法
    cursor = conn.cursor() #获取mysql光标
    sql = "select id from calc_record ORDER BY id DESC LIMIT 1" #sql语句，获取上一个id值
    cursor.execute(sql)    #执行sql语句
    id = cursor.fetchone() #获取到的id是一个元组
    if(id):
        id = int(id[0])+1  #如果元组不为空，将元组里的id转化成int型并加一
    else :
        id = 1             #如果元组为空，id为第一个
    sql1 = "insert into AHU_2021_TEST.calc_record(id,operand1,operator,operand2,result) values(%d,%f,\'%c\',%f,%f)"\
           %(id, operand1, '/', operand2, result)     #sql语句，插入本次记录到表calc_record
    cursor.execute(sql1)   #执行sql1语句
    conn.commit()          #数据库提交事务
    cursor.close()         #光标关闭
    return '%.2f' % result #页面返回运算值

if __name__ == '__main__':
    app.run()
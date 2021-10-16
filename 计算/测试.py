@app.route('/suba=<float:operand1>&b=<float:operand2>')
def sub(operand1,operand2):
    result = operand1 - operand2 #执行加法
    cursor = conn.cursor() #获取mysql光标
    sql = "select id from calc_record ORDER BY id DESC LIMIT 1" #sql语句，获取上一个id值
    cursor.execute(sql)    #执行sql语句
    id = cursor.fetchone() #获取到的id是一个元组
    id = int(id[0])+1      #将元组里的id转化成int型
    sql1 = "insert into AHU_2021_TEST.calc_record(id,operand1,operator,operand2,result) values(%d,%f,\'%c\',%f,%f)"\
           %(id+1, operand1, '+', operand2, result)     #sql语句，插入本次记录到表calc_record
    cursor.execute(sql1)   #执行sql1语句
    conn.commit()          #数据库提交事务
    cursor.close()         #光标关闭
    return '%s' % result   #页面返回运算值
#!/usr/bin/env python
import mysql.connector
import time

start=time.time()
cnx = mysql.connector.connect(user=[YOUR DATABASE USERNAME], password=[YOUR DATABASE PASSWORD],
                            host=[YOUR SERVER IP ADDRESS],
                            database=[YOUR DATABASE NAME])
cursor = cnx.cursor()
query=(""" SELECT * FROM wp_usermeta """)#find
cursor.execute(query)#find
data = cursor.fetchall ()# find
for row in data:
	if row[2]=='mycred_default':		
		if float(row[3])>=5000:
			print row[3]	
			interest=float(row[3])*1.0006
			value=float(row[3])*0.0006
			query=(""" UPDATE wp_usermeta SET meta_value= %s WHERE umeta_id= %s """)#update
			data=(interest,str(row[0]))#update
			cursor.execute(query,data)#update
			query=("INSERT INTO wp_myCRED_log""(ref_id,user_id,creds,ctype,time,entry)""VALUES (%s,%s,%s,%s,%s,%s)")#add new LOG			
			data=('0',str(row[1]),value,'mycred_default',str(time.time()),'%plural% hourly interest rate payment')#add new LOG
			cursor.execute(query,data)

cursor.close
cnx.close()

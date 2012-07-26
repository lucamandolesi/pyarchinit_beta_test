#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
/***************************************************************************
        pyArchInit Plugin  - A QGIS plugin to manage archaeological dataset
        					 stored in Postgres
                             -------------------
    begin                : 2007-12-01
    copyright            : (C) 2008 by Luca Mandolesi
    email                : mandoluca at gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import sys, os
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker

import pyarchinit_db_mapper
from pyarchinit_db_mapper import *

from pyarchinit_utility import *
from pyarchinit_OS_utility import *
from pyarchinit_conn_strings import *
from pyarchinit_db_update import *

import psycopg2
from psycopg2 import *
from psycopg2 import extensions

class Pyarchinit_db_management:
	metadata = ''
	engine = ''
	boolean = ''
	
	if os.name == 'posix':
		boolean = 'True'
	elif os.name == 'nt':
		boolean = 'False'

	def __init__(self, c):
		self.conn_str = c

	def connection(self):
		test = ""

		try:
			if self.conn_str.find("sqlite") == 0:
				self.engine = create_engine(self.conn_str, echo=eval(self.boolean))
			else:
				self.engine = create_engine(self.conn_str, max_overflow=-1, echo=eval(self.boolean)) #encoding='latin1' - accetta gli accenti ma è necessario modificare il sistema di update e di confronto dei record
			self.metadata = MetaData(self.engine)
			self.engine.connect()
		except Exception, e:
			test = e
		try:
			db_upd = DB_update()
			db_upd.update_table()
		except:
			pass
		return test

	#insert statement
	def insert_values(self, *arg):
		"""Istanzia la classe US da pyarchinit_db_mapper"""

		us = US(arg[0],
				arg[1],
				arg[2],
				arg[3],
				arg[4],
				arg[5],
				arg[6],
				arg[7],
				arg[8],
				arg[9],
				arg[10],
				arg[11],
				arg[12],
				arg[13],
				arg[14],
				arg[15],
				arg[16],
				arg[17],
				arg[18],
				arg[19],
				arg[20],
				arg[21],
				arg[22],
				arg[23],
				arg[24],
				arg[25],
				arg[26],
				arg[27],
				arg[28])

		return us

	def insert_ut_values(self, *arg):
		"""Istanzia la classe UT da pyarchinit_db_mapper"""

		ut = UT(arg[0],
				arg[1],
				arg[2],
				arg[3],
				arg[4],
				arg[5],
				arg[6],
				arg[7],
				arg[8],
				arg[9],
				arg[10],
				arg[11],
				arg[12],
				arg[13],
				arg[14],
				arg[15],
				arg[16],
				arg[17],
				arg[18],
				arg[19],
				arg[20],
				arg[21],
				arg[22],
				arg[23],
				arg[24],
				arg[25],
				arg[26],
				arg[27],
				arg[28],
				arg[29],
				arg[30],
				arg[31],
				arg[32],
				arg[33],
				arg[34],
				arg[35],
				arg[36],
				arg[37],
				arg[38],
				arg[39],
				arg[40],
				arg[41])

		return ut


	def insert_site_values(self, *arg):
		"""Istanzia la classe SITE da pyarchinit_db_mapper"""
		sito = SITE(arg[0],
				arg[1],
				arg[2],
				arg[3],
				arg[4],
				arg[5],
				arg[6])

		return sito


	def insert_periodizzazione_values(self, *arg):
		"""Istanzia la classe Periodizzazione da pyarchinit_db_mapper"""
		periodizzazione = PERIODIZZAZIONE(arg[0],
											arg[1],
											arg[2],
											arg[3],
											arg[4],
											arg[5],
											arg[6],
											arg[7],
											arg[8])

		return periodizzazione

	def insert_values_reperti(self, *arg):
		"""Istanzia la classe Reperti da pyarchinit_db_mapper"""
		inventario_materiali = INVENTARIO_MATERIALI(arg[0],
									arg[1],
									arg[2],
									arg[3],
									arg[4],
									arg[5],
									arg[6],
									arg[7],
									arg[8],
									arg[9],
									arg[10],
									arg[11],
									arg[12],
									arg[13],
									arg[14],
									arg[15],
									arg[16],
									arg[17])

		return inventario_materiali

	def insert_struttura_values(self, *arg):
		"""Istanzia la classe Struttura da pyarchinit_db_mapper"""
		struttura = STRUTTURA(arg[0],
								arg[1],
								arg[2],
								arg[3],
								arg[4],
								arg[5],
								arg[6],
								arg[7],
								arg[8],
								arg[9],
								arg[10],
								arg[11],
								arg[12],
								arg[13],
								arg[14],
								arg[15],
								arg[16],
								arg[17])

		return struttura


	def insert_values_ind(self, *arg):
		"""Istanzia la classe SCHEDAIND da pyarchinit_db_mapper"""
		schedaind = SCHEDAIND(arg[0],
				arg[1],
				arg[2],
				arg[3],
				arg[4],
				arg[5],
				arg[6],
				arg[7],
				arg[8],
				arg[9],
				arg[10],
				arg[11])

		return schedaind

	def insert_values_detsesso(self, *arg):
		"""Istanzia la classe DETSESSO da pyarchinit_db_mapper"""
		detsesso = DETSESSO(arg[0],
				arg[1],
				arg[2],
				arg[3],
				arg[4],
				arg[5],
				arg[6],
				arg[7],
				arg[8],
				arg[9],
				arg[10],
				arg[11],
				arg[12],
				arg[13],
				arg[14],
				arg[15],
				arg[16],
				arg[17],
				arg[18],
				arg[19],
				arg[20],
				arg[21],
				arg[22],
				arg[23],
				arg[24],
				arg[25],
				arg[26],
				arg[27],
				arg[28],
				arg[29],
				arg[30],
				arg[31],
				arg[32],
				arg[33],
				arg[34],
				arg[35],
				arg[36],
				arg[37],
				arg[38],
				arg[39],
				arg[40],
				arg[41],
				arg[42],
				arg[43],
				arg[44],
				arg[45],
				arg[46],
				arg[47],
				arg[48],
				arg[49],
				arg[50],
				arg[51],
				arg[52],
				arg[53])

		return detsesso

	def insert_values_deteta(self, *arg):
		"""Istanzia la classe DETETA da pyarchinit_db_mapper"""
		deteta = DETETA(arg[0],
				arg[1],
				arg[2],
				arg[3],
				arg[4],
				arg[5],
				arg[6],
				arg[7],
				arg[8],
				arg[9],
				arg[10],
				arg[11],
				arg[12],
				arg[13],
				arg[14],
				arg[15],
				arg[16],
				arg[17],
				arg[18],
				arg[19],
				arg[20],
				arg[21],
				arg[22],
				arg[23],
				arg[24],
				arg[25],
				arg[26],
				arg[27],
				arg[28],
				arg[29],
				arg[30],
				arg[31],
				arg[32],
				arg[33],
				arg[34],
				arg[35],
				arg[36],
				arg[37],
				arg[38],
				arg[39],
				arg[40],
				arg[41],
				arg[42],
				arg[43],
				arg[44],
				arg[45],
				arg[46],
				arg[47],
				arg[48],
				arg[49],
				arg[50],
				arg[51],
				arg[52],
				arg[53],
				arg[54],
				arg[55],
				arg[56])

		return deteta

	def insert_media_values(self, *arg):
		"""Istanzia la classe MEDIA da pyarchinit_db_mapper"""
		media = MEDIA(arg[0],
				arg[1],
				arg[2],
				arg[3],
				arg[4],
				arg[5],
				arg[6])

		return media

	def insert_mediathumb_values(self, *arg):
		"""Istanzia la classe MEDIA da pyarchinit_db_mapper"""
		media_thumb = MEDIA_THUMB(arg[0],
				arg[1],
				arg[2],
				arg[3],
				arg[4],
				arg[5],
				arg[6])

		return media_thumb

	def insert_media2us_values(self, *arg):
		"""Istanzia la classe MEDIATOUS da pyarchinit_db_mapper"""
		mediatous = MEDIATOUS(arg[0],
				arg[1],
				arg[2],
				arg[3],
				arg[4],
				arg[5],
				arg[6])

		return mediatous

	def insert_values_tafonomia(self, *arg):
		"""Istanzia la classe TAFONOMIA da pyarchinit_db_mapper"""

		tafonomia = TAFONOMIA(arg[0],
								arg[1],
								arg[2],
								arg[3],
								arg[4],
								arg[5],
								arg[6],
								arg[7],
								arg[8],
								arg[9],
								arg[10],
								arg[11],
								arg[12],
								arg[13],
								arg[14],
								arg[15],
								arg[16],
								arg[17],
								arg[18],
								arg[19],
								arg[20],
								arg[21],
								arg[22],
								arg[23],
								arg[24],
								arg[25],
								arg[26],
								arg[27],
								arg[28])

		return tafonomia


	def insert_values_archeozoology(self, *arg):
		"""Istanzia la classe ARCHEOZOOLOGY da pyarchinit_db_mapper"""

		archeozoology = ARCHEOZOOLOGY(arg[0],
										arg[1],
										arg[2],
										arg[3],
										arg[4],
										arg[5],
										arg[6],
										arg[7],
										arg[8],
										arg[9],
										arg[10],
										arg[11],
										arg[12],
										arg[13],
										arg[14],
										arg[15],
										arg[16],
										arg[17],
										arg[18],
										arg[19],
										arg[20])

		return archeozoology

	def execute_sql_create_db(self):
		path = os.path.dirname(__file__)
		rel_path = os.path.join(os.sep, 'query_sql', 'pyarchinit_create_db.sql')
		qyery_sql_path = ('%s%s') % (path, rel_path)
		create = open(qyery_sql_path, "r")
		stringa = create.read()
		create.close()
		self.engine.raw_connection().set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
		self.engine.text(stringa).execute()

	def execute_sql_create_spatialite_db(self):
		path = os.path.dirname(__file__)
		rel_path = os.path.join(os.sep, 'query_sql', 'pyarchinit_create_spatialite_db.sql')
		qyery_sql_path = ('%s%s') % (path, rel_path)
		create = open(qyery_sql_path, "r")
		stringa = create.read()
		create.close()

		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()
		session.begin()
		session.execute(stringa)
		session.commit()
		session.close()

	def execute_sql_create_layers(self):
		path = os.path.dirname(__file__)
		rel_path = os.path.join(os.sep, 'query_sql', 'pyarchinit_layers_postgis.sql')
		qyery_sql_path = ('%s%s') % (path, rel_path)
		create = open(qyery_sql_path, "r")
		stringa = create.read()
		create.close()

		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()
		session.begin()
		session.execute(stringa)
		session.commit()
		session.close()


	#query statement
	#
	def query(self, n):
		class_name = n
		#engine = self.connection()
		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()
		query = session.query(class_name)
		return query.all()

	def query_bool(self,params, table):
		u = Utility()
		params = u.remove_empty_items_fr_dict(params)
		field_value_string = ", ".join([table + ".%s == %s" % (k, v) for k, v in params.items()])
		
		"""
		Per poter utilizzare l'operatore LIKE è necessario fare una iterazione attraverso il dizionario per discriminare tra
		stringhe e numeri
		#field_value_string = ", ".join([table + ".%s.like(%s)" % (k, v) for k, v in params.items()])
		
		"""
		f = open('/test_query.txt', "w")
		f.write(str(field_value_string))
		f.close()
		
		query_str = "session.query(" + table + ").filter(and_(" + field_value_string + ")).all()"
		#self.connection()
		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()

		return eval(query_str)


	def query_operator(self,params, table):
		u = Utility()
		#params = u.remove_empty_items_fr_dict(params)
		field_value_string = ''
		for i in params:
			if field_value_string == '':
				field_value_string = '%s.%s %s %s' % (table, i[0], i[1], i[2])
			else:
				field_value_string = field_value_string + ', %s.%s %s %s' % (table, i[0], i[1], i[2])
			
		query_str = "session.query(" + table + ").filter(and_(" + field_value_string + ")).all()"

		#self.connection()
		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()

		return eval(query_str)


	#session statement
	def insert_data_session(self, data):
		Session = sessionmaker(bind=self.engine, autoflush=True)
		session = Session()
		session.add(data)
		session.commit()
		session.close()


	def update(self, table_class_str, id_table_str, value_id_list, columns_name_list, values_update_list):
		"""
		Receives 5 values then putted in a list. The values must be passed
		in this order: table name->string, column_name_where->list containin'
		one value
		('site_table', 'id_sito', [1], ['sito', 'nazione', 'regione', 'comune', 'descrizione', 'provincia'], ['Sito archeologico 1', 'Italiauiodsds', 'Emilia-Romagna', 'Riminijk', 'Sito di epoca altomedievale....23', 'Riminikljlks'])
		self.set_update = arg
		#self.connection()
		table = Table(self.set_update[0], self.metadata, autoload=True)
		changes_dict= {}
		u = Utility()
		set_update_4 = u.deunicode_list(self.set_update[4])

		u.add_item_to_dict(changes_dict,zip(self.set_update[3], set_update_4))

		f = open("test_update.txt", "w")
		f.write(str(self.set_update))
		f.close()

		exec_str = ('%s%s%s%s%s%s%s') % ("table.update(table.c.",
										  self.set_update[1],
										 " == '",
										 self.set_update[2][0],
										 "').execute(",
										 changes_dict ,")")

		#session.query(SITE).filter(and_(SITE.id_sito == '1')).update(values = {SITE.sito:"updatetest"})
		"""

		self.table_class_str = table_class_str
		self.id_table_str = id_table_str
		self.value_id_list = value_id_list
		self.columns_name_list = columns_name_list
		self.values_update_list = values_update_list

		changes_dict= {}
		u = Utility()
		update_value_list = u.deunicode_list(self.values_update_list)

		column_list = []
		for field in self.columns_name_list:
			column_str = ('%s.%s') % (table_class_str, field)
			column_list.append(column_str)

		u.add_item_to_dict(changes_dict,zip(self.columns_name_list, update_value_list))

		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()
		#session.query(SITE).filter(and_(SITE.id_sito == '1')).update(values = {SITE.sito:"updatetest"})

		session_exec_str = 'session.query(%s).filter(and_(%s.%s == %s)).update(values = %s)' % (self.table_class_str, self.table_class_str, self.id_table_str, self.value_id_list[0], changes_dict)

		#f = open('/test_update.txt', "w")
		#f.write(str(session_exec_str))
		#f.close()

		eval(session_exec_str)

	def delete_one_record(self, tn, id_col, id_rec):
		self.table_name = tn
		self.id_column = id_col
		self.id_rec = id_rec
		#self.connection()
		table = Table(self.table_name,self.metadata, autoload=True)
		exec_str = ('%s%s%s%d%s') % ('table.delete(table.c.', self.id_column, ' == ', self.id_rec, ').execute()')

		eval(exec_str)

	def max_num_id(self, tc, f):
		self.table_class = tc
		self.field_id = f
		exec_str = 'session.query(func.max(%s.%s))' % (self.table_class, self.field_id)
		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()
		max_id_func = eval(exec_str)
		res_all = max_id_func.all()
		res_max_num_id = res_all[0][0]
		if bool(res_max_num_id) == False:
			return 0
		else:
			return int(res_max_num_id)

	def dir_query(self):
		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()
		#session.query(SITE).filter(SITE.id_sito == '1').update(values = {SITE.sito:"updatetest"})
		#return session.query(SITE).filter(and_(SITE.id_sito == 1)).all()
		#return os.environ['HOME']

	#managements utilities
	def fields_list(self, t, s=''):
		"""return the list of columns in a table. If s is set a int,
		return only one column"""
		self.table_name = t
		self.sing_column = s
		table = Table(self.table_name, self.metadata, autoload=True)

		if bool(str(s)) == False:
			return [c.name for c in table.columns]
		else:
			return [c.name for c in table.columns][int(s)]

	def query_in_idus(self,id_list):
		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()
		return session.query(US).filter(US.id_us.in_(id_list)).all()


	def query_sort(self,id_list, op, to, tc, idn):
		self.order_params = op
		self.type_order = to
		self.table_class = tc
		self.id_name = idn

		filter_params = self.type_order + "(" + self.table_class + "." + self.order_params[0] + ")"
		for i in self.order_params[1:]:
			filter_temp = self.type_order + "(" + self.table_class + "." + i + ")"

			filter_params = filter_params + ", "+ filter_temp

		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()

		cmd_str = "session.query(" + self.table_class + ").filter(" + self.table_class + "." + self.id_name + ".in_(id_list)).order_by(" + filter_params + ").all()"

		return eval(cmd_str)


	def run(self, stmt):
		rs = stmt.execute()
		res_list = []
		for row in rs:
			res_list.append(row[0])

		return res_list

	
	def update_for(self):
		"""
		table = Table('us_table_toimp', self.metadata, autoload=True)
		s = table.select(table.c.id_us > 0)
		res_list = self.run(s)
		cont = 11900
		for i in res_list:
			self.update('US_toimp', 'id_us', [i], ['id_us'], [cont])
			cont = cont+1
		"""
		table = Table('inventario_materiali_table_toimp', self.metadata, autoload=True)
		s = table.select(table.c.id_invmat > 0)
		res_list = self.run(s)
		cont = 900
		for i in res_list:
			self.update('INVENTARIO_MATERIALI_TOIMP', 'id_invmat', [i], ['id_invmat'], [cont])
			cont = cont+1


	def group_by(self, tn, fn, CD):
		"""Group by the values by table name - string, field name - string, table class DB from mapper - string"""
		self.table_name = tn
		self.field_name = fn
		self.table_class = CD

		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()
		string = ('%s%s%s%s%s%s%s%s%s') % ('select([',self.table_class,'.',self.field_name ,']).group_by(',self.table_class,'.', self.field_name, ')')
		s = eval(string)
		return self.engine.execute(s).fetchall()


	def query_where_text(self, c, v):
		self.c = c
		self.v = v
		#self.connection()
		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()

		string = ('%s%s%s%s%s') %  ('session.query(PERIODIZZAZIONE).filter_by(', self.c, "='", self.v, "')")

		res = eval(string)
		return res

	def update_cont_per(self, s):
		self.sito = s
		
		Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
		session = Session()

		string = ('%s%s%s%s%s') %  ('session.query(US).filter_by(', 'sito', "='", str(self.sito), "')")

		lista_us = eval(string)

		for i in lista_us:
			if bool(i.periodo_finale) == False:
				if bool(i.periodo_iniziale) == True:
					periodiz = self.query_bool({'sito': "'"+str(self.sito)+"'", 'periodo': i.periodo_iniziale, 'fase': i.fase_iniziale}, 'PERIODIZZAZIONE')
					self.update('US', 'id_us', [int(i.id_us)], ['cont_per'], [periodiz[0].cont_per])
			elif bool(i.periodo_iniziale) == True and bool(i.periodo_finale) == True:
				cod_cont_iniz_temp = self.query_bool({'sito': "'"+str(self.sito)+"'", 'periodo': int(i.periodo_iniziale), 'fase': int(i.fase_iniziale)}, 'PERIODIZZAZIONE')
				cod_cont_fin_temp = self.query_bool({'sito': "'"+str(self.sito)+"'", 'periodo': int(i.periodo_finale), 'fase': int(i.fase_finale)}, 'PERIODIZZAZIONE')

				cod_cont_iniz = cod_cont_iniz_temp[0].cont_per
				cod_cont_fin = cod_cont_fin_temp[0].cont_per

				cod_cont_var_n = cod_cont_iniz
				cod_cont_var_txt = str(cod_cont_iniz)

				while(cod_cont_var_n != cod_cont_fin):
					cod_cont_var_n += 1

					cod_cont_var_txt = cod_cont_var_txt + "/" + str(cod_cont_var_n)

				self.update('US', 'id_us', [int(i.id_us)], ['cont_per'], [cod_cont_var_txt])

	def select_quote_from_db_sql(self, sito, area, us):
		sql_query_string = ("SELECT * FROM pyarchinit_quote WHERE sito_q = '%s' AND area_q = '%s' AND us_q = '%s'") %  (sito, area, us)
		res = self.engine.execute(sql_query_string)
		return res

	def select_us_from_db_sql(self, sito, area, us, stratigraph_index_us):
		sql_query_string = ("SELECT * FROM pyunitastratigrafiche WHERE scavo_s = '%s' AND area_s = '%s' AND us_s = '%s' AND stratigraph_index_us = '%s'") % (sito, area, us, stratigraph_index_us)
		res = self.engine.execute(sql_query_string)
		return res

def main():
	db = Pyarchinit_db_management("postgres://postgres:miapass@miohost/pyarchinit")
	db.connection()
	data = db.query(US)
	for i in range(len(data)):
		try:
			print data[i]
		except Exception, e:
			print str(e)

	#f = open("/database.txt", "w")
	#f.write(str(db))
	#f.close()

	#db.update_for()

if __name__ == '__main__':
	main()


"""

	#data = db.insert_site_values(124, "sito2", "Nazione", "Regione", "Comune", "descrizione", "Provincia")
	#db.update('US', 'id_us', [13202], ['cont_per'], ['1'])
	#db.group_by('site_table', 'sito', 'SITE')
	#periodo =  db.query_where_text('sito', 'sito3')

	#res = db.query_operator(
	#						[['cron_iniziale', '>',"-50"],
	#						['cron_finale','<',"1100"]]
	#						, 'PERIODIZZAZIONE')
	#for i in range(len(res)):
	#	print res[i].sito,'.',res[i].periodo,".",res[i].fase
	



	
	conversion_dict = {'Copre':'Coperto da',
					   'Coperto da': 'Copre',
					   'Riempie': 'Riempito da',
					   'Riempito da' : 'Riempie',
					   'Taglia': 'Tagliato da',
					   'Tagliato da': 'Taglia',
					   'Si appoggia a': 'Gli si appoggia',
					   'Si lega a': 'Si lega a',
					   'Uguale a':'Uguale a'
					   }
					
	
	search_dict = {'sito' : "'"+str('Palazzo Ghetti, Rimini')+"'", 'area' : "'"+ str(1) + "'"}

	records = db.query_bool(search_dict, 'US') #carica tutti i dati di uno scavo ordinati per numero di US

	report_rapporti = 'Report controllo Rapporti Stratigrafici \n'
	
	for rec in range(len(records)):

		sito = "'"+str(records[rec].sito)+"'"
		area = "'"+str(records[rec].area)+"'"
		us = int(records[rec].us)

		rapporti = records[rec].rapporti #caricati i rapporti nella variabile
		rapporti = eval(rapporti)

		for sing_rapp in rapporti:  #itera sulla serie di rapporti
			if len(sing_rapp) == 2:

				try:
					rapp_converted = conversion_dict[sing_rapp[0]]
					serch_dict_rapp = {'sito': sito, 'area': area, 'us': sing_rapp[1]}
					us_rapp = db.query_bool(serch_dict_rapp, 'US')

					if bool(us_rapp) == False:
						report = 'Sito: %s, Area: %s, US: %d %s US: %d: Scheda US non esistente' % (sito, area, int(us), sing_rapp[0], int(sing_rapp[1]))
					else:
						rapporti_check = eval(us_rapp[0].rapporti)
						us_rapp_check = ('%s') % str(us)
						#print 'us_rapp_check', [rapp_converted, us_rapp_check]
						if rapporti_check.count([rapp_converted, us_rapp_check]) == 1:
							report = "Errore generico"
						else:
							report = 'Sito: %s, Area: %s, US: %d %s US: %d: Rapporto non verificato' % (sito, area, int(us), sing_rapp[0], int(sing_rapp[1]))
				except:
					report = "problema di conversione"

				report_rapporti = report_rapporti + report + '\n'

	print report_rapporti

	rapp = [['Copre', 2], ['Coperto da']]
	
	
	id_list = []
	l = db.query(eval('STRUTTURA'))
	for i in l:
		print i
	
	#db.update_for()
	#data = db.insert_site_values(124, "sito2", "Nazione", "Regione", "Comune", "descrizione", "Provincia")
	#db.update('SITE', 'id_sito', [0], ['nazione'], ['albania'])
	#db.group_by('site_table', 'sito', 'SITE')
	#periodo =  db.query_where_text('sito', 'sito3')

	#res = db.query_operator(
	#						[['cron_iniziale', '>',"-50"],
	#						['cron_finale','<',"1100"]]
	#						, 'PERIODIZZAZIONE')
	#for i in range(len(res)):
	#	print res[i].sito,'.',res[i].periodo,".",res[i].fase

	
if __name__ == '__main__':
	main()

	#db.delete_one_record('inventario_materiali_table', "id_invmat", 1)
	#db.insert_data_session(data)
	#db.execute_sql_create_spatialite_db()
	#db.execute_sql_create_layers()

	#db.update_for()
	#db.group_by('us_table', 'definizione_stratigrafica')
	#print  db.query_sort([1, 2, 4], ['id_us'], 'asc')

	if self.conn_str.find("sqlite") == 0:
		OS_utility = pyarchinit_OS_Utility()
		OS_utility.create_dir("pyarchinit_DB_folder")
		self.engine = create_engine(self.conn_str, echo=False)
	else:
		self.engine = create_engine(self.conn_str, max_overflow=-1, echo=False)

	self.metadata = MetaData(self.engine)
	self.engine.connect()
except Exception, e:
	test = e
return test



Query OR freezed
def query_or(self,f,d):
	self.field = f
	self.data = d

	#filtro = US.id_us == id_list[0]
	filtro = self.field[0] == self.data[0]		
	
	for gid in self.data[1:]:
	    filtro |=  self.field[0]==gid
	order_param = asc(self.field[0])
	#order_param = desc(US.id_us)


	self.connection()
	Session = sessionmaker(bind=self.engine, autoflush=True, transactional=True)
	session = Session()
	return session.query(US).filter(or_(filtro)).order_by(order_param).all()

	#session.query(US).filter(or_(filtro)).order_by(order_param).all()


def query_or(self,f,d):
	self.field = f
	self.data = d

	#filtro = US.id_us == id_list[0]
	filtro = self.field[0] == self.data[0]		

	for gid in self.data[1:]:
	    filtro |=  self.field[0]==gid
	order_param = asc(self.field[0])
	#order_param = desc(US.id_us)


	self.connection()
	Session = sessionmaker(bind=self.engine, autoflush=True, transactional=True)
	session = Session()
	return session.query(US).filter(or_(filtro)).order_by(order_param).all()

	#session.query(US).filter(or_(filtro)).order_by(order_param).all()
"""

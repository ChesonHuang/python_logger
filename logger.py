#!/usr/bin/python  
#-*-coding:utf-8-*-

#2019.12.15
import logging
from os.path import (dirname,abspath,join)

from datetime import datetime

def logger():
	logger = logging.Logger(logging.Filter)  # new a logger instance
	#logger.setLevel("ERROR")
	
	log_path = join(dirname(abspath(__file__)),"Log")
	#print(log_path)
	cur_time = datetime.now().strftime("%Y%m%d_%H%M%S")
	log_file = join(log_path,cur_time+'.log')
	formatter = logging.Formatter("[%(levelname)s:%(filename)s-%(asctime)s]:%(message)s")
	#print(log_file)
	
	fh = logging.FileHandler(log_file)
	fh.setLevel("INFO")
	fh.setFormatter(formatter)
	
	sh = logging.StreamHandler()
	sh.setLevel("ERROR")
	sh.setFormatter(formatter)
	logger.addHandler(fh)
	logger.addHandler(sh)
	
	return logger
	
if __name__=='__main__':
	logger = logger()
	logger.info("today is 2019.12.15")
	logger.warn("Have you study today?")
	logger.error("I make a mistake on today")
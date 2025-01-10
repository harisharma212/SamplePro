#########################################################################################################
                                                                                                        #
# Exception Handling																					#  
# ------------------																					#
# Error:																								#
# The problems which occurs while writing the python code are known as Erros/Normal Errors.				#
# Example: Syntax Error, Indentation Errors, Missing : or "" or () or [] or {} etc.						#
																										#
# Exceptions:																							#
# The problems which occurs while execution of python scripts(Run time errors) are known as Exceptions.	#
# Example: ZeroDivisionError, NameError and TypeError etc.												#
																										#
# Exceptions can be handled in python by using "try" block.												#
																										#
																										#										
# try block is the combination of 2 or 3 sub-blocks.													#
# In some situations we can use "try-except", and in other situations we can use "try-except-finally"	#
																										#
#########################################################################################################
																										#																										
# try block:																							#
# ----------																							#
# try block can hold the piece of code, where we are expecting an expection.							#
# Assume that, a, b = 10, 0. And am trying to perform a/b 												#
# which causes zero division error(An Exception).														#
																										#
# Example:																								#
																										#
a = 10																									#
b = 20																									#
																										#
try:																									#
	print "I am in try block"																			#
	c = a/b  # It will cause ZeroDivisionError Exception, so placed in try block.						#
																										#
#########################################################################################################
																										#
# except block:																							#
# -------------																							#
# except block can hold the piece of code, what to do if found the exception.							#
# That means except block will executes only when an exception occurs in "try" block.					#
																										#
# Example:																								#
																										#
except:																									#
	print "I am except block"																			#
	print "dividant value should not be '0'" # In try block we will get exception, 						#
	# "so python will execute except block."															#
																										#
# To find the exception name programarically use "Exception" keyword. like below						#
except Exception as e:																					#
	print str(e)																						#
																										#
# please comment one except block to execute 															#
#########################################################################################################
																										#																										
# finally block:																						#
# --------------																						#
																										#
# In python, except block is an optional block, 														#
# which will execute every time irresptive of try block status.											#
# That means, finally block will get executed everytime even if the exception occurs or not.			#
																										#
# Example:																								#
																										#
finally:																								#
	print "I am an optional block"																		#
																										#
																										#
# #######################################################################################################																										

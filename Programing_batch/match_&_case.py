# case and match
# ............................................................

# 1. match :
# > It is a soft keyword in Python which is used to compare a given value or object against different patterns.

# > It starts the pattern - matching block.

# > 'match' is written once befire a group of 'case' statements.
# > It evaluates the value / expression provided after 'match'.


# 2. case :
# > It is a soft keyword in Python which is used inside a 'match' block to define a particular pattern and the code that should execute when that pattern matches.

# > The first matching 'case' is executed.

# > "case _" is used as the default / catch - all case when no other pattern matches.

# Syntax :
# match expression:
# 	case pattern_1:
# 		#SB

# 	case pattern_2:
# 		#SB
# 	..........
# 	..........

# 	case pattern_n:
# 		#SB

# 	case _:
# 		#default code block


# How it works :
# > Python evaluates the expression after match.
# > It checks the 'case' statements from top to bottom.
# > When a case matches, it's code executes and Python doesn't check the remaining   cases.
# > "case _:" works like a default case.


# > 'match' and 'case' are not a direct replacement for every 'if' statement. For normal conditions, it is usuallly simple. But these are the corresponding match-case forms.


# 1.) Simple if :

# Normal syntax :
# 	if <condition>:
# 		#TSB

# case and match syntax :
# 	match expression:
# 		case pattern if <condition>:
# 			#TSB


# 2.) Simple if else :

# Normal syntax :
# 	if <condition>:
# 		#TSB
# 	else:
# 		#FSB

# case and match syntax :
# 	match expression:
# 		case pattern if <condition>:
# 			#TSB
# 		case _:
# 			#FSB



# 3.) elif :

# Normal Syntax : 
# 	if <condition_1>:
# 		#TSB_1
# 	elif <condition_2>:
# 		#TSB_2
# 	elif <condition_3>:
# 		#TSB_3
# 	.........
# 	.........
# 	elif <condition_n>:
# 		#TSB_n
# 	else:
# 		#FSB


# case and match syntax :
# 	match expression:
# 		case pattern_1 if <condition_1>:
# 			#TSB_1
# 		case pattern_2 if <condition_2>:
# 			#TSB_2
# 		case pattern_3 if <condition_3>:
# 			#TSB_3
# 		............
# 		............
# 		case pattern_n if <condition_n>:
# 			#TSB_n 
# 		case _:
# 			#FSB


# 4.) Nested if :

# Normal Syntax :
# 	if <condition_1>:
# 		#TSB_1
# 		if <condition_2>:
# 			#TSB_2
# 			.........
# 			.........
# 			if <condition_n>:
# 				#TSB_n
# 			else:
# 				#FSB_N
# 		else:
# 			#FSB_n
# 	else:
# 		#FSB_1


# case and match Syntax :
# 	match expression_1:
#    		case pattern_1 if <condition_1>:
#      		# TSB_1

#       	 	 match expression_2:
#           	 	case pattern_2 if <condition_2>:
#             	    	# TSB_2
#              	        .........
#               	  	.........
#               	  		match expression_n:
#                     			case pattern_n if <condition_n>:
#                        				 # TSB_n
#                     			case _:
#                       	       		         # FSB_n
#         	        case _:
#              		      # FSB_2

#     		case _:
#      			   # FSB_1

input_password= input("Create Password : ") 
strength = check_password_strength (input_password) 
print("") 
print("Your password is {} !!".format(strength))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def check_password_strength (password):

  special_chars = list('@#$%&-I')
  isdigit_there = any (char.isdigit() for char in password)
  isupper_there = any (char.isupper() for char in password)
  isspchar_there = any(char.isdigit() for char in password)
  check_lower = any(char.islower () for char in password)
  all_true = all([isdigit_there, isupper_there, isspchar_there, check_lower])
  if len(password)<6:
    return "Weak"
  elif len(password) >=8 and all_true :
    return "strong"
  else:
    return "Average"
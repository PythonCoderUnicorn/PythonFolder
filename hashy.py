

# https://www.geeksforgeeks.org/how-to-hash-passwords-in-python/



def beecrypt():

  c = """

  eeee eeeee  e    e eeeee eeeee 
  8  8 8   8  8    8 8   8   8   
  8e   8eee8e 8eeee8 8eee8   8e  
  88   88   8   88   88      88  
  88e8 88   8   88   88      88  

  """

  print( c )

  # pip install bcrypt
  import bcrypt
  from getpass import getpass
 
  # Declaring our password
  # password = b'GeekPassword'
  password = getpass("Enter your string: ")
  password = password.encode("utf-8")
  
  # Adding the salt to password
  salt = bcrypt.gensalt()
  # Hashing the password
  hashed = bcrypt.hashpw(password, salt)
  
  # printing the salt
  ate_salt = salt.decode("utf-8")
  print(f"Salt : {ate_salt}")
  # print(salt)

  hashed_string = hashed.decode("utf-8")
  # printing the hashed
  print(f"Bcrypt Hashed: \n { hashed_string } \n")
  # print(hashed)


# beecrypt()



# -----------------------

def hash3():

  import hashlib 
  from getpass import getpass
  import random
  import string

  h = """

  {__                      {__     
  {__        {__     {____ {__     
  {_ {_    {__  {__ {__    {_ {_   
  {__  {__{__   {__   {___ {__  {__
  {_   {__{__   {__     {__{_   {__
  {__  {__  {__ {___{__ {__{__  {__
  """
  print(h)
 
  # Declaring Password
  # password = 'GeeksPassword'
  # Prompt the user for input
  # hidden_input = getpass("Enter your secret information: ")
  password = getpass("Enter passwd: ")
  # adding 5gz as password
  # salt = "5gz"

  s = string.ascii_letters.upper()
  sr = random.choice( s )
  sr1 = random.choice( s )
  r1 = random.randint(2734,727698)

  # print(sr1, sr, r1)

  salt = f"{sr1}{r1}{sr}"
  
  # Adding salt at the last of the password
  dataBase_password = password+salt
  # Encoding the password
  hashed = hashlib.sha3_384(dataBase_password.encode())
  
  # Printing the Hash
  print_hash = hashed.hexdigest()
  print("#-#-#"*10)
  print(f"[ SHA3_384 ] hash: \n{print_hash} \n")



# hash3()





# ---------------------------

def blakey():
  bl= """
  
    oo______ooo___________oo_____________
    oooooo___oo____ooooo__oo___o__ooooo__
    oo___oo__oo___oo___oo_oo__o__oo____o_
    oo___oo__oo___oo___oo_oooo___ooooooo_
    oo___oo__oo___oo___oo_oo__o__oo______
    oooooo__ooooo__oooo_o_oo___o__ooooo__
    _____________________________________
  """
  print(bl)

  from hashlib import blake2b
  from getpass import getpass

  h = blake2b()

  password = getpass("Enter your string: ")
  password = password.encode("utf-8")

  h.update( password )
  hexdig = h.hexdigest()
  print(f"[ Blake2b ]: {hexdig} \n")


# blakey()






# ------------------------



def mysecret():

  s1 = """
    @@@@@@ @@@@@@@@  @@@@@@@ @@@@@@@  @@@@@@@@ @@@@@@@ 
  !@@     @@!      !@@      @@!  @@@ @@!        @!!   
    !@@!!  @!!!:!   !@!      @!@!!@!  @!!!:!     @!!   
      !:! !!:      :!!      !!: :!!  !!:        !!:   
    ::.: :  : :: ::   :: :: :  :   : : : :: ::     :    
  """


  import string
  import secrets

  alphabet = string.ascii_letters + string.digits
  # password = "".join( secrets.choice(alphabet) for i in range(30))

  print(s1)
  plen = int(input("Enter passwd length: "))
  while True:
      password = ''.join(secrets.choice(alphabet) for i in range( plen ))
      if (any(c.islower() for c in password)
              and any(c.isupper() for c in password)
              and sum(c.isdigit() for c in password) >= 4):
          break


  
  print(f"Password: {password} \n")

  # import secrets url = 'https://example.com/reset=' + secrets.token_urlsafe()


# mysecret()



# ---------------------


def eightyfive():

  a85="""

            ,6*"*VA.          
          dN     V8          
  ,6"Yb.  `MN.  ,g9  M****** 
  8)   MM   ,MMMMq.  .M       
  ,pm9MM  6P   `YMb |bMMAg.  
  8M   MM  8b    `M9      `Mb 
  `Moo9^Yo.`MmmmmM9        jM 
                    (O)  ,M9 
                      6mmm9   
  """
  print( a85 )
  # import base64 
  from base64 import a85encode 
  from getpass import getpass

  # s = b'I love python'
  password = getpass("Enter your string: ")
  password = password.encode("utf-8")

  # Using base64.a85encode() method 
  # gfg = a85encode(s) 
  gfg = a85encode( password ) 
  hashed_string = gfg.decode("utf-8")
  print(f" a85: { hashed_string }\n") 


  from base64 import a85decode 
  # Using base64.a85decode() method 
  # gfg = a85decode(s) 
  gfg = a85decode( hashed_string ).decode("utf-8")
    
  # print(f"decoded: {gfg} \n")


# eightyfive()


# https://en.wikipedia.org/wiki/List_of_Unicode_characters





# ---------------------

def argons():

  arg="""

    .d888888                                      d8888b. 
    d8'    88                                          `88 
    88aaaaa88a 88d888b. .d8888b. .d8888b. 88d888b. .aaadP' 
    88     88  88'  `88 88'  `88 88'  `88 88'  `88 88'     
    88     88  88       88.  .88 88.  .88 88    88 88.     
    88     88  dP       `8888P88 `88888P' dP    dP Y88888P 
    ooooooooooooooooooooo~~~~.88~oooooooooooooooooooooooooo
                        d8888P                            
  """
  print( arg )

  # https://argon2-cffi.readthedocs.io/en/stable/
  # python -Im pip install argon2-cffi

  from argon2 import PasswordHasher 
  from getpass import getpass

  ph = PasswordHasher()

  pw = getpass("Enter your string: ")
  hash = ph.hash( pw )
  print(f" hashed: {hash} \n")
  
  # verify= ph.verify( hash, pw)
  # print(f"hash is verified: {verify} ✅ \n")


argons()




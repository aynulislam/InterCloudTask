# intercloudTask

1. clone the intercoudTask
2. go to django backend directory
3. use this command for setup requirments:
    pip3 install -r requirments.txt
    
    
4. use this command for run local server:
    python3 manage.py runserver
 
5. create superuser/admin command:
    python3 manage.py createsuperuser
    
    or login with admin  http://127.0.0.1:8000/admin/
                        username : tamxeed
                        password : tamxeed_3781
    
6. than use this command for migration
    python3 manage.py makemigrations
  
 7. than use this command for migrate
    python3 manage.py migrate

    
8. create role permission based user if needed than go to 
    http://127.0.0.1:8000/admin/
    
    
 admin can add, view books/ (user can only view)  url: http://127.0.0.1:8000/book/
 admin can view,edit,delete books url : http://127.0.0.1:8000/bookDetails/1/
 
 admin can add, view bookwise wish /(user can only create and view) url : http://127.0.0.1:8000/addBookToWishList/ 
 admin can view,edit,delete bookwise wish url: http://127.0.0.1:8000/bookToWishListDetails/1/
 
 
 need to be use jwt webtoken (login-register)  when  apply any request or response method (create,view,edit,delete) 
 otherwise "Authentication credentials were not provided."this message will show.
 
 
    

    


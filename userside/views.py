from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import Workout_master
import dj_database_url
import os
import datetime

import mysql.connector as mcdb

# Assuming you have the individual connection parameters in your environment
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = 3306
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')

# Establish a connection to the database using the individual parameters
conn = mcdb.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
print('Successfully connected to database')
cur = conn.cursor()

# Create your views here.
def home(request):
    return render(request,'Userside/home.html')

def contact(request):
    return render(request,'Userside/contact.html')

def account(request):
    return render(request,'Userside/account.html') 

def blog(request):
    return render(request,'Userside/blog.html') 

def blog_single(request):
    return render(request,'Userside/blog-single.html')

def checkout(request):
    return render(request,'Userside/checkout.html')

def classes_detail(request):
    return render(request,'Userside/classes-detail.html') 

def classes(request):
    return render(request,'Userside/classes.html') 

def about(request):
    return render(request,'Userside/about.html') 

def price(request):
    return render(request,'Userside/price.html') 

def faq(request):
    return render(request,'Userside/faq.html') 

def portfolio(request):
    return render(request,'Userside/portfolio.html') 

def not_found(request):
    return render(request,'Userside/not-found.html') 

def portfolio_detail(request):
    return render(request,'Userside/portfolio-detail.html') 

def testimonial(request):
    cur.execute("SELECT ut.User_Type,u.User_Name,u.Photo,f.Details,f.Ratings FROM `feedback_master` f,`user_master` u,`user_type` ut WHERE f.User_Id=u.User_Id and u.Type_Id=ut.Type_Id")
    data = cur.fetchall()
    print(list(data))

    if data:
        fifth_element = data[0][4] if len(data[0]) > 4 else None
        return render(request, 'Userside/testimonial.html', {'mydata': data, 'r': fifth_element})
    else:
        # Handle the case when data is empty
        return render(request, 'Userside/testimonial.html', {'mydata': [], 'r': None})


def testimonialadd(request):
    if request.method == 'POST':
        print(request.POST)
        uid = request.session['user_id']
        msg = request.POST['message']
        rating = request.POST['ratings']
        cur.execute("INSERT INTO `feedback_master`(`User_Id`,`Details`,`Ratings`) VALUES ('{}','{}','{}')".format(uid,msg,rating))
        conn.commit()
        messages.success(request,'Feedback Added Successfully')
        return redirect(testimonial) 
    else:
        return redirect(testimonial)



def register(request):
    return render(request,'Userside/register.html')

import datetime as dt

def registerprocess(request):
    if request.method == 'POST':
        typeid = 1
        name = request.POST.get('mname', '')
        gender = request.POST.get('gender', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        mobile = request.POST.get('mobile', '')
        img = request.FILES.get('photo', '').name
        id_proof = request.FILES.get('id_proof', '').name
        plan = request.POST.get('plan', '')
        password = request.POST.get('password', '')

        try:
            photo = request.FILES.get('photo', '')
            f = open("Adminapp/static/upload/" + img, 'wb')
            for i in photo:
                f.write(i)
            f.close()

            idproof = request.FILES.get('id_proof', '')
            fi = open("Adminapp/static/upload/" + id_proof, 'wb')
            for i in id_proof:
                f.write(i)
            f.close()
        except:
            pass

        #create table if not exist

        

        cur.execute("INSERT INTO `user_master`(`Type_Id`,`User_Name`,`Gender`,`Email`,`Password`,`Address`,`Mobile`,`Photo`,`ID_Proof`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (typeid, name, gender, email, password, address, mobile, img, id_proof))
        u_id = cur.lastrowid
        conn.commit()

        s_date = dt.date.today()
        cur.execute("SELECT * FROM `plan_master` WHERE `Plan_Id` = %s", (plan,))
        data = cur.fetchone()

        if data is not None:
            planidd = data[0]
            planprice = data[3]
            plandetails = data[2]

            if plan == "1":
                e_date = s_date + dt.timedelta(days=30)
            elif plan == "2":
                e_date = s_date + dt.timedelta(days=60)
            elif plan == "3":
                e_date = s_date + dt.timedelta(days=90)

            cur.execute("INSERT INTO `membership_master`(`User_Id`,`Plan_Id`,`Start_Date`,`End_Date`,`Amount`,`Details`) VALUES (%s, %s, %s, %s, %s, %s)",
                        (u_id, planidd, s_date, e_date, planprice, plandetails))
            m_id = cur.lastrowid
            conn.commit()
            return redirect("/payment/{}".format(m_id))
        else:
            return HttpResponse("No data found for the selected plan")

    else:
        return redirect(register)


def login(request):
    if request.method == 'POST':
        print(request.POST)
        uemail = request.POST['useremil']
        upassword = request.POST['userpassword']
        usertype = request.POST['type']
        cur.execute("select * from `user_master` where `Email` = '{}' and `Password` = '{}'".format(uemail,upassword))
        data = cur.fetchone()
        
        if data is not None:

            if len(data) > 0:
                #Fetch Data
                db_id = data[0]
                db_email = data[4]
                db_name = data[2]
                db_photo = data[8]
                print(db_id)
                print(db_email)
                #Session Create Code
                if usertype=="Trainer" and data[1]==2:
                    request.session['user_id'] = db_id
                    request.session['user_email'] = db_email
                    request.session['user_name'] = db_name
                    request.session['user_photo'] = db_photo
                    response = redirect("http://127.0.0.1:8000/trainerapp/")
                    response.set_cookie('user_id', db_id)
                    response.set_cookie('user_email', db_email)
                    return response
                elif usertype=="Member" and data[1]==1:
                    request.session['user_id'] = db_id
                    request.session['user_email'] = db_email
                    response = redirect(home)
                    response.set_cookie('user_id', db_id)
                    response.set_cookie('user_email', db_email)
                    return response
                else:
                    return render(request, 'Userside/workout.html')

                #Session Create Code
                #Cookie Code
                
                #Cookie Code
            else:
                return render(request, 'Userside/login.html')         
        return render(request, 'Userside/login.html')
        
       # return redirect(dashboard) 
    else:
        return render(request, 'Userside/login.html')

def logout(request):
    del request.session['user_id']
    del request.session['user_email']
    response = redirect(login)
    response.delete_cookie('user_id')
    response.delete_cookie('user_email')
    return response

def forgot(request):
    return render(request,'Userside/forgot.html')    
    
def forgotpasswordprocess(request):
    print(request.POST)
    user_email = request.POST['useremil']
    cur.execute("select * from `user_master` where `Email` = '{}'".format(user_email))
    db_data = cur.fetchone()
        
    if db_data is not None:
        if len(db_data) > 0:
            #Fetch Data
            db_id = db_data[0]
            db_email = db_data[4]
            db_password = db_data[5]
            print(db_id)
            print(db_email)
            
            subject = 'Forgot Password'
            message = ' Your Password is  ' + db_password
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [db_email,]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Password Sent on Email ID')
            return redirect(login)
            #Cookie Code
        else:
            messages.error(request, 'Wrong Email Details')
            return render(request, 'Userside/forgot.html') 
    messages.error(request, 'Wrong Email Details')
    return render(request, 'Userside/forgot.html')

def workout(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        workout_data = Workout_master.objects.filter(user_id=user_id)
        return render(request, 'Userside/workout.html', {'mydata': workout_data})
    else:
        return render(request,'Userside/login.html')

def attendance(request):
    u = request.session['user_id']
    cur.execute("SELECT * FROM `attendance_master` WHERE `User_id`= {}".format(u))
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'Userside/attendance.html',{'mydata': data})

def membership(request):
    u = request.session['user_id']
    cur.execute("SELECT p.Title,p.Duration,m.Start_Date,m.End_Date,m.Membership_Status FROM `membership_master` m,`plan_master` p WHERE ( m.Plan_Id = p.Plan_Id) and `User_id`= {}".format(u))
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'Userside/membership.html',{'mydata': data})

def myaccount(request):
    u = request.session['user_id']
    cur.execute("SELECT * FROM `user_master` WHERE `User_id`= {}".format(u))
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'Userside/myaccount.html',{'mydata': data})

def chngpassword(request):
    return render(request,'Userside/chngpassword.html')

def changepasswordprocess(request):
    if 'user_email' in request.COOKIES and request.session.has_key('user_email'):
        print(request.POST)
        user_id = request.session['user_id']
        opass = request.POST['old']
        npass = request.POST['new']
        cpass = request.POST['cnfrm']
        cur.execute("select * from `user_master` where `User_Id`= {}".format(user_id))
        db_data = cur.fetchone()

        if db_data is not None:

            if len(db_data) > 0:
                #Fetch Data
                oldpassword = db_data[5]
                if opass == oldpassword:
                    cur.execute("update  `user_master` set `Password` = '{}' where `User_Id` = '{}'".format(npass,user_id))
                    conn.commit()
                    messages.success(request, 'Password Changed Successfully')
                    return render(request, 'Userside/chngpassword.html')
                else:
                    messages.error(request, 'Wrong Old Password ')
                    return render(request, 'Userside/chngpassword.html')
            else:
                redirect(login) 
        else: 
            redirect(login) 
    else:
        return redirect(login)

def updateacc(request):
    return render(request,'Userside/updateacc.html')

def payment(request,id):
    cur.execute("SELECT p.Title,u.User_Name,u.Email,u.Mobile FROM `membership_master` m,`plan_master` p,`user_master` u WHERE m.Plan_Id=p.Plan_Id and m.User_Id=u.User_Id and m.Membership_Id='{}'".format(id))
    data=cur.fetchone()
    print(data)
    return render(request,'Userside/Payment.html',{'mydata': data,'mid': id})

def paymentprocess(request,id):
    cur.execute("SELECT * FROM `membership_master` WHERE `Membership_Id`={}".format(id))
    data=cur.fetchone()
    if request.method == 'POST':
        print(request.POST)
        mid = id
        mt = request.POST['payment']
        tno = request.POST['Transaction']
        rec = request.FILES['receipt'].name
        amt = data[5]
        try:
            recp = request.FILES['receipt']
            f = open("/static/upload/"+rec, 'wb')
            for i in recp:
                f.write(i)
            f.close()
        except:
            pass
        cur.execute("INSERT INTO `payment_master`(`Membership_Id`,`Amount`,`Method`,`Transaction_no`,`Payment_Receipt`,`Payment_Status`) VALUES ('{}','{}','{}','{}','{}','Not Approved')".format(mid,amt,mt,tno,rec))
        conn.commit()
        messages.success(request,'Thanks For Registering!')
        return redirect(login) 
    else:
        return redirect(payment)   
    

def trainer(request):
    return render(request,'Userside/trainer.html')

def workout_edit(request):
    return render(request,'Userside/workout_edit.html')

def checkout(request):
    return render(request,'Userside/checkout.html')

def feedback(request):
    cur.execute("SELECT * FROM `feedback_master`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'Userside/feedback.html',{'mydata': data})


def feedbackadd(request):
    return render(request,'Userside/feedbackadd.html')

def feedbackaddprocess(request):
    cur.execute("SELECT * FROM `feedback_master`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return redirect(feedback)

def placeorderprocess(request):
    if 'user_id' in request.COOKIES and request.session.has_key('user_id'):
        print(id)
        import datetime
        order_date = datetime.datetime.now().strftime ("%d-%m-%Y")
        order_status = "Pending"
        user_id = 1
        #OrderDetails
        cur.execute("INSERT INTO `tbl_order_master`(`order_date`,`order_status`,`user_id`) VALUES ('{}','{}','{}')".format(order_date,order_status,user_id))
        order_id = cur.lastrowid  
        conn.commit()
        cur.execute("SELECT * FROM `tbl_cart`")
        db_data = cur.fetchall()
        for row in db_data:
            print("For Ma aayo")
            cart_id = row[0]
            product_id = row[2]
            product_qty = row[3]
            product_price = row[4]
            cur.execute("INSERT INTO `tbl_order_details`(`order_id`,`product_id`,`product_qty`,`product_price`) VALUES ('{}','{}','{}','{}')".format(order_id,product_id,product_qty,product_price))
            conn.commit()
            cur.execute("delete from `tbl_cart` where `cart_id` = {}".format(cart_id))
            conn.commit()
          
        #return list(data)
        print(list(db_data))
        messages.success(request, 'Record Added!!')
        return redirect(thanks)
    else:
        return redirect(login)


def thanks(request):
    return  render(request,'Userside/thanks.html')


def vieworder(request):
    u=request.session['user_id']
    cur.execute("SELECT * FROM `order_master` WHERE `User_Id` = {}".format(u))
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'Userside/vieworder.html',{'mydata': data})

def orderdetail(request):
    cur.execute("SELECT p.Product_Name,p.Product_Image,p.Details,o.Qty,o.Price,o.Tot_Amt FROM `order_details` o, `Product_Master` p WHERE (o.Product_Id=p.Product_Id) and `Order_Id` = 1115")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'Userside/OrderDetails.html',{'mydata': data})

def viewfeedback(request):
    cur.execute("SELECT * FROM `feedback_master`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'Userside/viewfeedback.html',{'mydata': data})

from django.http import JsonResponse

def calculate_bmi(request):
    if request.method == 'POST':
        height_str = request.POST.get('height')
        weight_str = request.POST.get('weight')
        gender = request.POST.get('gender')
        
        # Debug: Print received data
        print(f"Received data: height={height_str}, weight={weight_str}, gender={gender}")
        
        # Check if any required field is missing
        if not height_str or not weight_str or not gender:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        
        try:
            # Convert string inputs to float
            height = float(height_str)
            weight = float(weight_str)
        except ValueError:
            return JsonResponse({'error': 'Invalid input format'}, status=400)
        
        # Perform BMI calculation
        bmi = weight / ((height / 100) ** 2)
        
        return JsonResponse({'bmi': bmi})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

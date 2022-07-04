    # CUBIC POLYNOMIAL
import math

a = input('Give me a = ')
b=input('Give me b= ')
c= input('Give me c = ')
d = input('Give me d = ')

a=float(a)
b=float(b)
c=float(c)
d=float(d)


if a==0:
    if b==0:
        if c==0:
            if d==0:
                print('η εξίσωση είναι αόριστη')
            else:
                print('η εξίσωση είναι αδύνατη')

        else:
            x=-d/c
            print('η εξίσωση έχει μια λύση, x=' , x)

    else:
        
        if c==0:
            x1=-(d/b)**(1/2)
            x2=-(-(d/b)**(1/2))
            print('x1=' , x1)
            print('x2=' , x2)

        else:
            
            
         
         
            diak = c**2 - 4 * b *d

            print('Η διακρίνουσα είναι Δ=' , diak)

            r = diak**0.5

            print('Η παράμετρος r είναι r=' , r)

            x1=(-c-r)/(2*b)
            x2=(-c+r)/(2*b)
            print('x1=' , x1)
            print('x2=' , x2)

    print('ΤΕΛΟΣ ΠΡΟΓΡΑΜΜΑΤΟΣ')  
                
        
else:
    alpha=b/a
    beta=c/a
    ci=d/a

    diak=18*alpha*beta*ci-4*alpha**3*ci+alpha**2*beta**2-4*beta**3-27*ci**2
    print('Η διακρίνουσα είναι Δ=' , diak)

    p=beta-(alpha**2)/3
    q=ci+(2*alpha**3-9*alpha*beta)/27

    iporizo_1=-q/2+((q**2/4+p**3/27))**(1/2)
    iporizo_2=-q/2-((q**2/4+p**3/27))**(1/2)

    # we will calculate the 6 cubic roots according to DeMorive Theorem

    real_1=iporizo_1.real
    real_2=iporizo_2.real
    imag_1=iporizo_1.imag
    imag_2=iporizo_2.imag

    r1=(real_1**2+imag_1**2)**(1/2)
    r2=(real_2**2+imag_2**2)**(1/2)

    if real_1==0:
        theta_1=math.radians(90/math.pi)
    else:       
        
        theta_1=math.atan(imag_1/real_1)

    if real_2==0:
        theta_2=math.radians(90/math.pi)
    else:
        theta_2=math.atan(imag_2/real_2)



        

    k0=0
    k1=1
    k2=2
    j=(-1)**(1/2)


    u1=(r1**(1/3)*math.cos((theta_1+2*k0*math.pi)/3))+((j)*r1**(1/3)*math.sin((theta_1+2*k0*math.pi)/3))
    
    u2=(r1**(1/3)*math.cos((theta_1+2*k1*math.pi)/3))+((j)*r1**(1/3)*math.sin((theta_1+2*k1*math.pi)/3))

    u3=(r1**(1/3)*math.cos((theta_1+2*k2*math.pi)/3))+((j)*r1**(1/3)*math.sin((theta_1+2*k2*math.pi)/3))

    u4=(r2**(1/3)*math.cos((theta_2+2*k0*math.pi)/3))+((j)*r2**(1/3)*math.sin((theta_2+2*k0*math.pi)/3))
    
    u5=(r2**(1/3)*math.cos((theta_2+2*k1*math.pi)/3))+((j)*r2**(1/3)*math.sin((theta_2+2*k1*math.pi/3)))

    u6=(r2**(1/3)*math.cos((theta_2+2*k2*math.pi)/3))+((j)*r2**(1/3)*math.sin((theta_2+2*k2*math.pi/3)))


    x1=-p/(3*u1)+u1-alpha/3
    x2=-p/(3*u2)+u2-alpha/3
    x3=-p/(3*u3)+u3-alpha/3
    x4=-p/(3*u4)+u4-alpha/3
    x5=-p/(3*u5)+u5-alpha/3
    x6=-p/(3*u6)+u6-alpha/3

    print('x1=' , x1)
    print('x2=' , x2)
    print('x3=' , x3)
    print('x4=' , x4)
    print('x5=' , x5)
    print('x6=' , x6)

    
print('ΤΕΛΟΣ ΠΡΟΓΡΑΜΜΑΤΟΣ')    

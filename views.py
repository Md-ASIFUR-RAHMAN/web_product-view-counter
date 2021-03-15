from django.shortcuts import render

# Create your views here.
global sum1,sum2,sum3,sum4
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
i = 1
def home(request):

    return render(request,'userac/home.html')


def action_h(request,action):



    if action == 'P1':
        global sum1,B

        sum1 = sum1 +  i

        p1 = {
            'B':sum1

        }
        b = p1

        return render(request, 'userac/response.html',b)





    if action == 'P2':
        global sum2,B

        sum2 = sum2 +  i

        p2 = {
            'B':sum2

        }

        b = p2

        return render(request, 'userac/response.html',b)
    if action == 'P3':
        global sum3,B

        sum3 = sum3 +  i

        p3 = {
            'B':sum3

        }

        b = p3

        return render(request, 'userac/response.html',b)
    if action == 'P4':
        global sum4,B

        sum4 = sum4 +  i

        p4 = {
            'B':sum4

        }

        b = p4

        return render(request, 'userac/response.html',b)



    if action == 'table':


        c = {
            'B': sum1,
            'p': sum2,
            'C': sum3,
            'V': sum4
        }

        return render(request, 'userac/table.html',c )














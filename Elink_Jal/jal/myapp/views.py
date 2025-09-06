from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.hashers import check_password
from django.views.decorators.cache import never_cache
from .models import *
from datetime import date
from django.contrib.auth import authenticate, login
from django.utils.timezone import now

# Create your views here.
@never_cache
def HomePage(request):
    # Always flush session on GET (i.e., visiting the login page = logout)
    if request.method == 'GET':
        request.session.flush()
        return render(request, 'home.html')

    # Handle POST (login attempt)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        error_message = "Username or Password is incorrect.\nPlease Try Again" # if user enters wrong username or password

        try:
            user = MUser.objects.get(user_name=username) # if username matches lol
            if password == user.user_password:
                request.session.flush()    # logout previous user (fail save, redundant)
                request.session['user_id'] = user.user_id 
                request.session['username'] = user.user_name
                request.session.set_expiry(0)  # logout when browser is closed

                if user.role_id == 2: # role_id 2 is user not admin
                    return redirect('map')
                else:
                    return redirect('OpForm')
        except MUser.DoesNotExist:
            pass # don't need this but it works either way

        return render(request, 'home.html', {"error_message": error_message})

    # Fallback
    return render(request, 'home.html')

@never_cache    
def OpForm(request):
    locations = MLocation.objects.all()
    sub_locations = MSubLocation.objects.all()
    username = request.session.get('username') 
    if username == None:
        return redirect('Home')
    user_id = MUser.objects.get(user_name = username)
    count = 0 # for getting next id to display on the page
    if request.method == 'POST':
        emailid = request.POST.get('emailid')
        firstn = request.POST.get('firstn')
        lastn = request.POST.get('lastn')
        gender = request.POST.get('gender')
        mobno = request.POST.get('mobno')
        sub_locations = request.POST.getlist('sub_location[]')
        password = request.POST.get('password')
        user_name = request.POST.get('usern')
        roleid = request.POST.get('roleid')
        new_user = MUser(
            email_id = emailid,
            primary_mobile_number = mobno,
            user_name = user_name,
            gender = gender,
            created_date = date.today(),
            created_by = user_id.user_id,
            role_id = roleid,
            first_name = firstn,
            last_name = lastn,
            user_address_1 = 'Maharashtra',
            user_password = password,
        )
        all_users = MUser.objects.all()
        user_ids = []
        for a in all_users:
            user_ids.append(a.user_id)
        count = max(user_ids)
        new_user.save()
        for sub_loc_id in set(sub_locations): 
            TUserLocation.objects.create(
            user_id=new_user.user_id,
            sub_location_id=sub_loc_id,
            is_deleted=False,
            created_date=date.today(),
            created_by=user_id.user_id,
            )
        return redirect('OpForm')
    
    last_user = MUser.objects.order_by('user_id').last()
    count = last_user.user_id + 1 # not very good but this works
    return render(request,'op_form.html',{
        'username' : username,
        'locations' : locations,
        'sub_locations' : sub_locations,
        'next_id' : count,
    })

@never_cache
def logout_view(request):
    request.session.flush()
    return redirect('Home')

@never_cache
def locations_view(request):
    username = request.session.get('username')
    if username == None:
        return redirect('Home')
    user_id = MUser.objects.get(user_name = username)
    if request.method == 'POST':
        state = request.POST.get('state')
        location_name = request.POST.get('location')
        new_location = MLocation(
            location_name=location_name,
            is_deleted=False,
            created_date=date.today(),
            created_by = user_id.user_id,
            state_id=state
        )
        new_location.save()
        return redirect('locations')

    states = MState.objects.all()
    locations = MLocation.objects.all()
    location_ids = [] 
    for location in locations:
        location_ids.append(location.location_id)
    next_id = max(location_ids) + 1
    return render(request, 'locations.html', {
        'username' : username ,
        'states' : states ,
        'next_id' : next_id,
    })


@never_cache
def sub_location_details_view(request):
    username = request.session.get('username')
    if username == None:
        return redirect('Home')
    user_id = MUser.objects.get(user_name = username)
    ls = MLocation.objects.all()
    sls = MSubLocation.objects.all()
    location_name = 1
    if request.method == 'POST':
        sub_loc = request.POST.get('sub-location')
        location_name = request.POST.get('location')
        lat = request.POST.get('latitude')
        lng = request.POST.get('longitude')
        new_location = MSubLocation(
            sub_location_name = sub_loc,
            location_id=location_name,
            is_deleted=False,
            created_date=date.today(),
            created_by = user_id.user_id,
            s_loc_latitude = lat,
            s_loc_longitude = lng,
         )
        new_location.save()
        return redirect('sub_locations')
    
    sls = MSubLocation.objects.all()
    return render(request, 'sub_location.html', {
        'username' : username ,
        'ls' : ls , 
        'loc_name' : location_name,
        'sls' : sls,
    })

@never_cache
def equipment_view(request):
    username = request.session.get('username')
    if username == None:
        return redirect('Home')
    user_id = MUser.objects.get(user_name = username)
    ets = MEquipmentType.objects.all()
    if request.method == 'POST':
        equipment_name = request.POST.get('equipment_name')
        equipment_type_id = request.POST.get('equipment_type_id')
        new_equipment = MEquipment(
            equipment_name =  equipment_name,
            equipment_type_id=equipment_type_id,
            is_deleted=False,
            created_date=date.today(),
            created_by = user_id.user_id,
         )
        new_equipment.save()
        return redirect('equipments')
    
    e = MEquipment.objects.all()
    e_ids = []
    for e_id in e:
        e_ids.append(e_id.equipment_id)
    next_id = max(e_ids) + 1
    
    return render(request, 'equipments.html', {
        'username' : username ,
        'ets' : ets , 
        'next_id' : next_id, 
    })

@never_cache
def ChangePassword(request):
    username = request.session.get('username')
    if username is None:
        return redirect('Home') 
    user = MUser.objects.get(user_name=username)
    if request.method == 'POST':
        ogpassword = request.POST.get('ogpassword') 
        newpassword = request.POST.get('newpassword')
        confnewpassword = request.POST.get('confnewpassword')
        if user.user_password == ogpassword:
            if newpassword == confnewpassword and ogpassword != newpassword:
                user.user_password = newpassword
                user.save()
                user = authenticate(username=username, password=newpassword)
                if user is not None:
                    login(request, user)
                return render(request, 'changepassword.html', {'username': username, 'message': 'Password changed successfully!'})
            else:
                return render(request, 'changepassword.html', {'username': username, 'error': 'Passwords do not match or are the same as the old password.'})
        else:
            return render(request, 'changepassword.html', {'username': username, 'error': 'Old password is incorrect.'})
    
    return render(request, 'changepassword.html', {'username': username})

@never_cache
def EquipmentLocation(request):
    locations = MLocation.objects.all()
    sub_locations = MSubLocation.objects.all()
    es = MEquipment.objects.all()
    username = request.session.get('username')
    if username is None:
        return redirect('Home')

    user_id = MUser.objects.get(user_name = username)
    
    if request.method == 'POST':
        sub_location_id = request.POST.get('sub_location')

        equipment_ids = request.POST.getlist('equipment_type_id[]')
        mfg_details = request.POST.getlist('mfg_details[]')
        model_numbers = request.POST.getlist('modelno[]')
        serial_numbers = request.POST.getlist('serialno[]')
        latitudes = request.POST.getlist('latitude[]')
        longitudes = request.POST.getlist('longitude[]')
        index_len = len(mfg_details)
        for i in range(index_len):
            e = equipment_ids[i+1] # i don't know why it works like this
            mfg = mfg_details[i]
            m = model_numbers[i]
            s = serial_numbers[i]
            lat = latitudes[i]
            lng = longitudes[i]
            new_equipment_location = TEquipmentLocation(
            equipment_id = e,
            sub_location_id =  sub_location_id,
            is_deleted=False,
            created_date=date.today(),
            created_by = user_id.user_id,
            manufacturer_name = mfg,
            model_number = m,
            serial_number = s,
            equip_latitude = lat,
            equip_longitude = lng,
            )
            new_equipment_location.save()
        
    return render(request, 'equipmentlocation.html', {
        'username': username,
        'locations': locations,
        'sub_locations': sub_locations,
        'es': es,
    })


@never_cache
def EquipmentType(request):
    username = request.session.get('username')
    if username is None:
        return redirect('Home')
    user_id = MUser.objects.get(user_name = username) 
    eids = MEquipmentType.objects.all()
    
    if request.method == 'POST':
            etd = request.POST.get('equipment_type_name')
            new_equipment_type = MEquipmentType(equipment_type_description = etd, created_date = date.today(),created_by = user_id.user_id )
            new_equipment_type.save()
            return redirect('equipmenttype')
    if(username == None):
        return redirect('Home')
    return render(request, 'equipmenttype.html', {'username': username,'next_id' : len(eids)+1})

@never_cache
def AccountDetails(request):
    username = request.session.get('username')
    if username is None:
        return redirect('Home')
    user_id = MUser.objects.get(user_name = username)
    loc = MLocation.objects.get(location_id = user_id.location_id)
    allsl = MSubLocation.objects.all()
    sls = TUserLocation.objects.all()
    usl = []
    for sl in sls:
        if(sl.user_id == user_id.user_id):
            usl.append(sl)
    fsl = []
    for u in usl:
        print(u.sub_location_id) 
    for p in allsl:
        for u in usl:
            if(u.sub_location_id == p.sub_location_id):
                fsl.append(p) 
    
    variables = {'username': username, 'user_id' : user_id , 'loc' : loc,'sls' : fsl}
    return render(request, 'myaccount.html', variables)
    
@never_cache
def MapView(request):
    username = request.session.get('username')
    if username is None:
        return redirect('Home')

    user = MUser.objects.get(user_name=username)
    user_locations = TUserLocation.objects.all()
    user_sub_location_ids = []
    for u in user_locations:
        if(user.user_id == u.user_id): 
            user_sub_location_ids.append(u.sub_location_id)

    allowed_location_ids = set(
        MSubLocation.objects
        .filter(sub_location_id__in=user_sub_location_ids)
        .values_list('location_id', flat=True)
    )

    ls = MLocation.objects.filter(location_id__in=allowed_location_ids)
    sls = MSubLocation.objects.all()
    equiploc = TEquipmentLocation.objects.all()
    equip = MEquipment.objects.all()

    context = {
        'ls': ls,
        'username': username,
        'sls': sls,
        'user_location': user_locations,
        'equiploc': equiploc,
        'equip': equip,
        'timestamp': now().timestamp(),
        'avsl': user_sub_location_ids,
    }
    return render(request, 'map.html', context)
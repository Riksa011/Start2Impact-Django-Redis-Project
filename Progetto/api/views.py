from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import SearchItemForm, UploadItemForm, RegistrationForm
from .models import Item, User


# function to render homepage html file
def homepage(request):
    return render(request, 'Progetto/index.html', {})


# function to view all uploaded items
def items_list(request):
    items = Item.objects.all().order_by('-upload_date')
    return render(request, 'Progetto/user_actions/item_list.html', {'items': items})


# function to view item history by searching with id code
def search_item(request):
    if request.method == 'POST':
        form = SearchItemForm(request.POST)
        if form.is_valid():
            user_id_code_to_search = form.cleaned_data['id_code']
            try:
                item = Item.objects.get(id_code=user_id_code_to_search)
            except Item.DoesNotExist:
                return render(request, 'Progetto/user_actions/item_search/item_not_found.html', {})
            return render(request, 'Progetto/user_actions/item_search/item_detail.html', {'item': item})
    else:
        form = SearchItemForm()
    return render(request, 'Progetto/user_actions/item_search/search_item.html', {'form': form})


# function to create custom login to redirect not logged user to custom page
def custom_login_required(view_func):
    decorated_view_func = login_required(view_func)

    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'Progetto/admin_actions/user_not_logged.html')
        else:
            return decorated_view_func(request, *args, **kwargs)

    return wrapper


@custom_login_required
# function for new admin registration
def admin_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Progetto/admin_authentication/registration_successfully.html', {})
    else:
        form = RegistrationForm()
    return render(request, 'Progetto/admin_authentication/registration.html', {'form': form})


# function for admin login
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
    return render(request, 'Progetto/admin_authentication/login.html')


# function for admin profile view
@custom_login_required
def admin_profile_view(request):
    return render(request, 'Progetto/admin_actions/admin_profile_view.html')


# function to upload new item
@custom_login_required
def upload_item(request):
    if request.method == "POST":
        form = UploadItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            # set upload date and id code function callback
            Item.set_date_and_id_code(self=item)
            # item history update
            item.item_actions_number += 1
            item.item_last_action = 'Action N°1: Item "' + item.item_name + '" (id code: ' + str(
                item.id_code) + ') uploaded on ' + str(
                item.upload_date) + ' and owned by "' + str(item.owner) + '"'
            item.writeOnChain()  # write on chain function callback
            item.item_last_action += ', Onchain proof: https://goerli.etherscan.io/tx/' + str(item.txId)
            item.item_history += item.item_last_action
            item.save()
            return render(request, 'Progetto/admin_actions/new_item_upload/item_upload_successfully.html', {})
    else:
        form = UploadItemForm()
    return render(request, 'Progetto/admin_actions/new_item_upload/new_item.html', {'form': form})


# function to change item owner
@custom_login_required
def change_item_owner(request):
    if request.method == 'POST':
        id_code = request.POST['item']
        new_owner_nickname = request.POST['owner']
        item = Item.objects.get(id_code=id_code)
        new_owner = User.objects.get(nickname=new_owner_nickname)
        item.owner = new_owner
        # item history update
        item.item_actions_number += 1
        current_ts = datetime.now()
        rounded_current_ts = current_ts.replace(microsecond=0)  # "' + item.item_name + '"
        item.item_last_action = 'Action N°' + str(
            item.item_actions_number) + ': Item "' + item.item_name + '" (id code :' + str(
            item.id_code) + ') updated on ' + str(rounded_current_ts) + ' and owned by ' + str(item.owner)
        item.writeOnChain()  # write on chain function callback
        item.item_last_action += ', Onchain proof: https://goerli.etherscan.io/tx/' + str(item.txId)
        item.item_history += '  -------------------- '
        item.item_history += item.item_last_action
        item.save()
        return render(request, 'Progetto/admin_actions/change_item_owner/owner_changed_successfully.html', {})
    else:
        items = Item.objects.all()
        users = User.objects.all()
        return render(request, 'Progetto/admin_actions/change_item_owner/change_item_owner.html',
                      {'users': users, 'items': items})

import redis
from django.conf import settings
from django.contrib import messages


# Middleware to check if an admin is accessing the website from the same IP address
def check_ip_middleware(get_response):
    def middleware(request):
        # Get the current admin user
        admin_user = request.user

        # Get the last accessed IP of the admin
        r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
        last_ip = r.get(f"last_admin_ip:{admin_user.id}")

        # Get the current IP of the admin
        current_ip = request.META.get('REMOTE_ADDR')

        # Compare the last accessed IP with the current IP
        if last_ip and last_ip.decode('utf-8') != current_ip:
            messages.warning(request, f"Warning: last access was made from a different IP ({last_ip.decode('utf-8')})")

        # Store the current IP as the last accessed IP
        r.set(f"last_admin_ip:{admin_user.id}", current_ip)

        # Print the current IP, the last accessed IP and the admin user to check if the middleware is working
        print(f"Current IP: {current_ip}")
        print(f"Last IP: {last_ip.decode('utf-8') if last_ip else 'None'}")
        print(f"Admin User: {admin_user.username}")

        response = get_response(request)
        return response

    return middleware

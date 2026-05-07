from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
import json
from .models import User

@csrf_exempt
@require_http_methods(["POST"])
def register(request):
    """Register a new user"""
    try:
        data = json.loads(request.body)
        
        # Validate required fields
        if not all(k in data for k in ['username', 'email', 'password', 'first_name', 'last_name']):
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        
        # Check if user already exists
        if User.objects.filter(username=data['username']).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        
        if User.objects.filter(email=data['email']).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)
        
        # Create new user
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            user_type=data.get('user_type', 'patient'),
            phone_number=data.get('phone_number', ''),
            age=data.get('age'),
            gender=data.get('gender', ''),
            city=data.get('city', ''),
        )
        
        # Auto-login after registration
        login(request, user)
        
        return JsonResponse({
            'success': True,
            'message': 'User registered successfully',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_type': user.user_type,
            }
        }, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def login_view(request):
    """Login user and return user data"""
    try:
        data = json.loads(request.body)
        
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return JsonResponse({'error': 'Username and password required'}, status=400)
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({
                'success': True,
                'message': 'Login successful',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'user_type': user.user_type,
                }
            })
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=401)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["POST"])
def logout_view(request):
    """Logout user"""
    logout(request)
    return JsonResponse({'success': True, 'message': 'Logout successful'})


@require_http_methods(["GET"])
def get_current_user(request):
    """Get current logged-in user data"""
    if request.user.is_authenticated:
        user = request.user
        return JsonResponse({
            'success': True,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_type': user.user_type,
                'phone_number': user.phone_number,
                'age': user.age,
                'gender': user.gender,
                'address': user.address,
                'city': user.city,
            }
        })
    else:
        return JsonResponse({'error': 'Not authenticated'}, status=401)


@require_http_methods(["GET"])
def users_list(request):
    """Get list of all registered users"""
    try:
        # Filter by user_type if provided
        user_type = request.GET.get('user_type')
        
        if user_type:
            users = User.objects.filter(user_type=user_type)
        else:
            users = User.objects.all()
        
        users_data = []
        for user in users:
            users_data.append({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'name': f"{user.first_name} {user.last_name}",
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_type': user.user_type,
                'phone_number': user.phone_number,
                'city': user.city,
            })
        
        return JsonResponse({
            'success': True,
            'count': len(users_data),
            'users': users_data
        })
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def get_user_by_id(request, user_id):
    """Get specific user by ID"""
    try:
        user = User.objects.get(id=user_id)
        return JsonResponse({
            'success': True,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'name': f"{user.first_name} {user.last_name}",
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_type': user.user_type,
                'phone_number': user.phone_number,
                'age': user.age,
                'gender': user.gender,
                'address': user.address,
                'city': user.city,
            }
        })
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def update_user_profile(request, user_id):
    """Update user profile"""
    try:
        user = User.objects.get(id=user_id)
        
        # Check if user is updating their own profile or is admin
        if request.user.id != user.id and not request.user.is_staff:
            return JsonResponse({'error': 'Permission denied'}, status=403)
        
        data = json.loads(request.body)
        
        # Update allowed fields
        allowed_fields = ['first_name', 'last_name', 'phone_number', 'age', 'gender', 'address', 'city']
        for field in allowed_fields:
            if field in data:
                setattr(user, field, data[field])
        
        user.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Profile updated successfully',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_type': user.user_type,
                'phone_number': user.phone_number,
                'age': user.age,
                'gender': user.gender,
                'address': user.address,
                'city': user.city,
            }
        })
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

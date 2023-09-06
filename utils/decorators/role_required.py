def role_required(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.role == required_role:
                return func(user, *args, **kwargs)

            raise PermissionError(
                f'User does not have required role: {required_role}')
        return wrapper
    return decorator


class User:
    def __init__(self, role):
        self.role = role


@role_required('admin')
def delete_data(user):
    print('Data deleted')


admin_user = User(role='admin')
delete_data(admin_user)

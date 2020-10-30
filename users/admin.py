from django.contrib import admin
from django.contrib.auth.models import Permission
from users.models import UserMenu
from users.models import UserRouter
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','name')
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = ('username', 'password', 'name','is_active', 'is_superuser')
    def clean_password(self):
        return self.initial["password"]
class UserProfileAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('id', 'username', 'name','is_superuser', 'is_active')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'name', 'password','email')}),
        ('Permissions', {'fields': ('is_active','is_superuser', )}),
        ('用户其它权限', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2','name')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(User,UserProfileAdmin)

class PermissionAdmin(admin.ModelAdmin):
    fields = ['name', 'content_type', 'codename']
    list_display = ['name', 'content_type', 'codename']
    list_per_page = 20
    search_fields = ('name', 'codename')


class UserMenuAdmin(admin.ModelAdmin):
    fields = ['index', 'path', 'parent', 'title', 'icon', 'permission']
    list_display = ['index', 'path', 'parent', 'title', 'icon', 'permission']
    ordering = ('index',)
    list_per_page = 20
    search_fields = ('path', 'title')
    list_display_links = ('title',)


class UserRouterAdmin(admin.ModelAdmin):
    fields = ['path', 'name', 'title', 'auth', 'component', 'permission']
    list_display = ['path', 'name', 'title', 'auth', 'component', 'permission']
    list_per_page = 20
    search_fields = ('path', 'title', 'name')
    list_display_links = ('title',)


admin.site.register(Permission, PermissionAdmin)
admin.site.register(UserMenu, UserMenuAdmin)
admin.site.register(UserRouter, UserRouterAdmin)


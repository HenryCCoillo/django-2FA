from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter your first name',
                                                               'class': 'form-control',
                                                               'autocomplete':'off',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter your last name',
                                                              'class': 'form-control',
                                                              'autocomplete':'off',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter your username',
                                                             'class': 'form-control',
                                                             'autocomplete':'off',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter your email',
                                                           'class': 'form-control',
                                                           'autocomplete':'off',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password',
                                                                  'class': 'form-control icon-eyes',
                                                                  'data-toggle': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password',
                                                                  'class': 'form-control icon-eyes',
                                                                  'data-toggle': 'password',
                                                                  }))

    class Meta:
        model = User
        model._meta.get_field('email')._unique = True
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
# from .models import Membership
User = get_user_model()


from allauth.account.forms import SignupForm

class MyCustomSignupForm(SignupForm):    
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['account_type'] = forms.ChoiceField(
                                            required=True,
                                            choices=User.MEMBERSHIP_CHOICES,
                                            widget=forms.Select(
                                                attrs={
                                                    "class": "form-control formControl",
                                                }
                                            )
                                        )
    def save(self, request):
        # import ipdb;ipdb.set_trace()
        account_type = self.cleaned_data.pop('account_type')    

        user = super(MyCustomSignupForm, self).save(request)
        return user

class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):

    error_message = admin_forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )
    
    # account_type = forms.ModelChoiceField(
    #     required=False,
    #     queryset=Membership.objects.all(),
    #     widget=forms.Select(
    #         attrs={
    #             "class": "form-control formControl standardSelect",
    #             "data-live-search": "true",
    #             "data-placeholder": "Select Account Type"
    #         }
    #     )

    # )
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2', 'account_type' )

    def clean_username(self):
        username = self.cleaned_data["username"]


        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])




# class UserForm(forms.ModelForm):
#     password = forms.CharField(
#         required=False,
#         max_length=30,
#         widget=forms.PasswordInput(

#             attrs={
#                 "class": "form-control formControl",
#                 "id": "password",
#                 "autocomplete": "off",
#                 "placeholder": "Enter Password"
#             }

#         )
#     )

#     full_name = forms.CharField(
#         required=True,
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control formControl",
#                 "id": "full_name",
#                 "autocomplete": "off",
#                 "placeholder": "Enter Full Name"
#             }
#         )
#     )
#     email = forms.CharField(
#         required=True,
#         max_length=300,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control formControl",
#                 "id": "email",
#                 "autocomplete": "off",
#                 "placeholder": "Enter Email"
#             }
#         )
#     )
#     mobile = forms.CharField(
#         required=True,
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control formControl",
#                 "id": "mobile",
#                 "autocomplete": "off",
#                 "placeholder": "Enter Mobile"
#             }
#         )
#     )
#     # role = forms.ChoiceField(
#     #     required=True,
#     #     choices=Us_User.ROLE_CHOICES,
#     #     widget=forms.Select(
#     #         attrs={
#     #             "class": "form-control formControl",
#     #         }
#     #     )
#     # )


#     class Meta:
#         model = Account
#         fields = ['full_name',  'email', 'password', 'mobile','account_type']

#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     # filter vehicle models accroding to oem's
#     #     self.request = kwargs.pop('request', None)

#         # if self.request:
#         #     user_obj = self.request.user
#         #     if not user_obj.is_superuser:
#         #         oem_obj = user_obj.us_user.oem or user_obj.oem
#         #         self.fields['user_models'].queryset = Model.objects.filter(oem=oem_obj)



# class UserUpdateForm(forms.ModelForm):
#     full_name = forms.CharField(
#         required=True,
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control formControl btnDisable",
#                 "id": "full_name",
#                 "autocomplete": "off",
#                 "placeholder": "Enter Full Name"
#             }
#         )
#     )
#     email = forms.CharField(
#         required=True,
#         max_length=300,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control formControl btnDisable",
#                 "id": "email",
#                 "autocomplete": "off",
#                 "placeholder": "Enter Email",
#             }
#         )
#     )
#     password = forms.CharField(
#         required=False,
#         max_length=30,
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control formControl btnDisable",
#                 "id": "password",
#                 "autocomplete": "off",
#                 "placeholder": "Enter Password"
#             }

#         ),
#         help_text=("Raw passwords are not stored, so there is no way to see this user's password,"
#                    " but you can change the password")
#     )
#     mobile = forms.CharField(
#         required=True,
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control formControl btnDisable",
#                 "id": "mobile",
#                 "autocomplete": "off",
#                 "placeholder": "Enter Mobile"
#             }
#         )
#     )

#     # role = forms.ChoiceField(
#     #     required=True,
#     #     choices=Us_User.ROLE_CHOICES,
#     #     widget=forms.Select(
#     #         attrs={
#     #             "class": "form-control formControl btnDisable",
#     #         }
#     #     )
#     # )


#     class Meta:
#         model = Account
#         fields = ['full_name',  'email', 'password', 'mobile','account_type']
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     instance = kwargs.get('instance')
#     #     workshop = instance.workshop

#     #     if workshop:
#     #         # run_time_license_qs = workshop.run_time_licenses.all()
#     #         # self.fields['run_time_licenses'].queryset = run_time_license_qs
#     #         self.fields['report_to'].queryset = Us_User.objects.filter(
#     #             workshop=workshop).order_by('first_name')

#         # user_obj = instance.user
#         # if user_obj:
#         #     if not user_obj.is_superuser:
#         #         oem_obj = user_obj.us_user.oem or user_obj.oem
#         #         self.fields['user_models'].queryset = Model.objects.filter(oem=oem_obj)
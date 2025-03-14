from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired,Email,ValidationError
from flask_wtf.file import FileField, FileRequired,FileAllowed
from AttendanceProject.models import User
from flask_login import current_user

class AddCourseForm(FlaskForm):
    name = StringField('Course Name',validators=[DataRequired()])
    author_id = StringField('Doctor Full Name',validators=[DataRequired()])
    submit = SubmitField('Add Course')
class AddUserForm(FlaskForm):
    first_name = StringField('First Name',validators=[DataRequired()])
    last_name = StringField('Last Name',validators=[DataRequired()])
    uni_number = StringField('University Number')
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = StringField('Password',validators=[DataRequired()])
    account_type = StringField('Account Type',validators=[DataRequired()])
    submit = SubmitField('Add User')
class ManageCoursesForm(FlaskForm):
    name = StringField('Course Name',validators=[DataRequired()])
    author_id = StringField('Doctor Full Name',validators=[DataRequired()])
    submit = SubmitField('Delete Course')
class DoctorCoursesForm(FlaskForm):
    name = StringField('Course Name',validators=[DataRequired()])
    enrolled_number = StringField('Students Enrolled Count',validators=[DataRequired()])
    submit = SubmitField('See Course')
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log in')
class DashBoard(FlaskForm):
    first_name= StringField('Email',validators=[DataRequired()])
    last_name= StringField('Email',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
class DoctorAddStudent(FlaskForm):
    student_id= StringField('University Number',validators=[DataRequired()])
    submit = SubmitField('Add Student')
class ChangePasswordForm(FlaskForm):
    current_password= StringField('Current Password',validators=[DataRequired()])
    new_password= StringField('New Password',validators=[DataRequired()])
    submit = SubmitField('Change Password')
class StudentCoursesForm(FlaskForm):
    name = StringField('Course Name',validators=[DataRequired()])
    submit = SubmitField('See Course')
class DoctorAddCourseForm(FlaskForm):
    course_name = StringField('Course Name',validators=[DataRequired()])
    submit = SubmitField('Add Course')
class DoctorRemoveStudent(FlaskForm):
    student_id= StringField('University Number',validators=[DataRequired()])
    submit = SubmitField('Remove Student')
class ManageUsersForm(FlaskForm):
    name = StringField('Student Name',validators=[DataRequired()])
    Id = StringField('',validators=[DataRequired()])
    uni_number = StringField('University Number',validators=[DataRequired()])
    submit = SubmitField('Delete User')
class AdminAddStudent(FlaskForm):
    student_id= StringField('University Number',validators=[DataRequired()])
    course = StringField('Course Name',validators=[DataRequired()])
    submit = SubmitField('Add Student')
class DoctorAddUsers(FlaskForm):
    file = FileField('Upload students pdf file', validators=[FileRequired(),FileAllowed(['pdf'], 'Only PDF files are allowed!')])
    submit = SubmitField('Register Students')
class DoctorEnrollUsers(FlaskForm):
    file = FileField('Upload students pdf file', validators=[FileRequired(),FileAllowed(['pdf'], 'Only PDF files are allowed!')])
    course_id = SelectField('Choose course', choices=[], validators=[DataRequired()])
    submit = SubmitField('Enroll Students')

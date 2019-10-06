from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, validators


# EDIT PROFILE FORM CLASS


class EditProfileForm(FlaskForm):
    about_me = TextAreaField('About me', [validators.Length(min=0, max=256)])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField(
        'Create Post', [validators.DataRequired(), validators.Length(min=1, max=140)])
    submit = SubmitField('Submit')


class MessageForm(FlaskForm):
    message = TextAreaField('Message', [validators.DataRequired(),
                                        validators.Length(min=0, max=140)])
    submit = SubmitField('Submit')

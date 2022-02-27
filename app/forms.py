from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileField, FileAllowed


class UploadForm(FlaskForm):
    photo = FileField('image', validators=[FileRequired(),
        FileAllowed(['jpg','png'], 'Only Image Files!')])
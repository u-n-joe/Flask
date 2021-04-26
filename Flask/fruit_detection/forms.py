from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired


class MainForm(FlaskForm):
    price = DecimalField("총 가격 : ", validators=[DataRequired()])
    submit = SubmitField("결제")
    manager = SubmitField("관리자모드")

class MForm(FlaskForm):
    price = DecimalField("총 가격 : ", validators=[DataRequired()])
    submit = SubmitField("결제")
    manager = SubmitField("관리자모드")


class LoginForm(FlaskForm):
    num = DecimalField("회원 번호", validators=[DataRequired()])
    submit = SubmitField("확인")


class JoinForm(FlaskForm):
    num = DecimalField("회원 번호", validators=[DataRequired()])
    submit = SubmitField("확인")


class ManagerForm(FlaskForm):
    num = DecimalField("회원 번호", validators=[DataRequired()])
    add = SubmitField("추가")
    edit = SubmitField("수정")
    remove = SubmitField("삭제")


class AddItemForm(FlaskForm):
    name = DecimalField("과일 명 : ", validators=[DataRequired()])
    price = DecimalField("가격 : ", validators=[DataRequired()])
    amount = DecimalField("수량 : ", validators=[DataRequired()])
    submit = SubmitField("확인")


class EditItemForm(FlaskForm):
    name = DecimalField("이름", validators=[DataRequired()])
    submit = SubmitField("확인")


class RemoveItemForm(FlaskForm):
    name = DecimalField("아이템 번호", validators=[DataRequired()])
    submit = SubmitField("확인")

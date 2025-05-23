from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField
from wtforms.validators import InputRequired, Length, Regexp


class BVCrawlerForm(FlaskForm):
    """视频评论爬取表单（通过BV号）"""

    bv = StringField(
        'BV号',
        [
            InputRequired(),
            Regexp(
                r"^(BV[a-zA-Z0-9]{10},)*BV[a-zA-Z0-9]{10}$|^BV[a-zA-Z0-9]{10}$",
                message="请输入正确格式的格式",
            ),
        ],
    )
    is_second = BooleanField("爬取二级评论", default=True)
    submit = SubmitField("开始爬取")


class UIDCrawlerForm(FlaskForm):
    """用户评论爬取表单（通过UID）"""

    uid = StringField(
        "UID",
        [
            InputRequired(),
            Regexp(
                r"^\d+$",
                message="请输入正确格式的UID（纯数字）",
            ),
        ],
    )
    is_second = BooleanField("爬取二级评论", default=True)
    submit = SubmitField("开始爬取")


class ModeSelectForm(FlaskForm):
    """模式选择表单"""

    mode = RadioField(
        "选择爬取模式",
        choices=[
            ("bv", "视频评论爬取（输入BV号）"),
            ("up", "用户视频评论爬取（输入UID号）"),
            ("uid", "用户评论爬取（输入UID号）"),
        ],
        default="bv",
        validators=[InputRequired()],
    )
    submit = SubmitField("下一步")

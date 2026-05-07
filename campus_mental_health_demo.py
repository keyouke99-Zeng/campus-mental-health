from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# 演示账号，不是真实登录系统
USERS = {
    "student": {
        "password": "123456",
        "role": "student",
        "name": "学生用户"
    },
    "counselor": {
        "password": "123456",
        "role": "counselor",
        "name": "心理咨询师"
    },
    "admin": {
        "password": "123456",
        "role": "admin",
        "name": "系统管理员"
    }
}


# 模拟风险预警数据
risk_alerts = [
    {
        "anonymous_id": "A-2026-001",
        "level": "高风险",
        "source": "连续低情绪语义模式",
        "status": "待处理"
    },
    {
        "anonymous_id": "A-2026-002",
        "level": "中风险",
        "source": "夜间异常波动",
        "status": "观察中"
    },
    {
        "anonymous_id": "A-2026-003",
        "level": "高风险",
        "source": "AI 异常情绪趋势",
        "status": "已分配咨询师"
    },
    {
        "anonymous_id": "A-2026-004",
        "level": "低风险",
        "source": "短期情绪波动",
        "status": "已记录"
    }
]


# 模拟趋势图数据
trend_data = [
    {"day": "周一", "value": 2},
    {"day": "周二", "value": 4},
    {"day": "周三", "value": 3},
    {"day": "周四", "value": 6},
    {"day": "周五", "value": 5},
    {"day": "周六", "value": 2},
    {"day": "周日", "value": 4}
]


# 模拟情绪分布数据
emotion_data = [
    {"label": "积极", "percent": 38},
    {"label": "平和", "percent": 47},
    {"label": "低落", "percent": 15}
]


# 模拟学生情绪周报
weekly_report = [
    {
        "day": "周一",
        "ai_emotion": "平和",
        "student_emotion": "平和",
        "note": "状态正常"
    },
    {
        "day": "周二",
        "ai_emotion": "低落",
        "student_emotion": "低落",
        "note": "作业压力较大"
    },
    {
        "day": "周三",
        "ai_emotion": "低落",
        "student_emotion": "平和",
        "note": "当天感冒，不代表心理问题"
    },
    {
        "day": "周四",
        "ai_emotion": "积极",
        "student_emotion": "积极",
        "note": "参加社团活动后状态较好"
    },
    {
        "day": "周五",
        "ai_emotion": "平和",
        "student_emotion": "平和",
        "note": "正常学习日"
    },
    {
        "day": "周六",
        "ai_emotion": "低落",
        "student_emotion": "平和",
        "note": "只是睡眠不足"
    },
    {
        "day": "周日",
        "ai_emotion": "积极",
        "student_emotion": "积极",
        "note": "与朋友外出"
    }
]


# 模拟场景级采集开关
scene_switches = [
    {
        "name": "宿舍门禁",
        "desc": "宿舍出入场景中的情绪分析",
        "enabled": True
    },
    {
        "name": "图书馆门禁",
        "desc": "图书馆进出场景中的情绪分析",
        "enabled": False
    },
    {
        "name": "教学楼门禁",
        "desc": "教学楼通行场景中的情绪分析",
        "enabled": True
    },
    {
        "name": "校车",
        "desc": "校车刷卡场景中的情绪分析",
        "enabled": False
    }
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = USERS.get(username)

        if user and user["password"] == password:
            if user["role"] == "student":
                return redirect(url_for("student_report"))
            elif user["role"] == "counselor":
                return redirect(url_for("dashboard"))
            elif user["role"] == "admin":
                return redirect(url_for("settings"))
        else:
            error = "用户名或密码错误。请使用演示账号 student / counselor / admin，密码都是 123456。"

    return render_template("login.html", error=error)


@app.route("/dashboard")
def dashboard():
    stats = {
        "total_students": 12800,
        "high_risk": 12,
        "pending_cases": 7,
        "system_status": "正常"
    }

    return render_template(
        "dashboard.html",
        stats=stats,
        risk_alerts=risk_alerts,
        trend_data=trend_data,
        emotion_data=emotion_data
    )


# 模拟干预任务数据
intervention_tasks = [
    {
        "title": "A-2026-001 高风险预警",
        "desc": "连续低情绪语义模式，建议优先分配咨询师。",
        "status": "待处理"
    },
    {
        "title": "A-2026-003 AI 异常情绪趋势",
        "desc": "近期情绪波动明显，已进入人工复核阶段。",
        "status": "已分配"
    },
    {
        "title": "A-2026-002 夜间异常波动",
        "desc": "建议继续观察 7 天，不立即触发身份查看。",
        "status": "观察中"
    }
]


# 模拟审计日志
audit_logs = [
    {
        "action": "咨询师打开匿名风险列表",
        "operator": "counselor",
        "time": "2026-05-05 09:20"
    },
    {
        "action": "提交查看身份申请",
        "operator": "counselor",
        "time": "2026-05-05 09:25"
    },
    {
        "action": "系统记录 AI 高风险预警",
        "operator": "system",
        "time": "2026-05-05 09:30"
    }
]


@app.route("/risk")
def risk():
    return render_template(
        "risk.html",
        risk_alerts=risk_alerts,
        intervention_tasks=intervention_tasks,
        audit_logs=audit_logs
    )



@app.route("/student-report")
def student_report():
    return render_template(
        "student_report.html",
        weekly_report=weekly_report,
        scene_switches=scene_switches
    )


# 模拟系统设置
system_settings = [
    {
        "name": "学生数据保留周期",
        "desc": "普通学生情绪记录和周报数据的默认保留时间。",
        "value": "90 天"
    },
    {
        "name": "毕业生数据删除规则",
        "desc": "学生毕业后，系统自动删除相关个人数据。",
        "value": "30 天后删除"
    },
    {
        "name": "离线缓存模式",
        "desc": "校园网络不稳定时，允许后台继续查看本地缓存数据。",
        "value": "已启用"
    },
    {
        "name": "身份查看授权",
        "desc": "咨询师查看真实身份前必须提交授权申请。",
        "value": "强制开启"
    }
]


# 模拟权限管理
permissions = [
    {
        "name": "学生",
        "access": "查看个人周报、修正情绪记录、管理场景采集开关、申请删除个人数据。"
    },
    {
        "name": "心理咨询师",
        "access": "查看匿名风险预警、管理干预任务、申请查看学生身份。"
    },
    {
        "name": "系统管理员",
        "access": "管理系统设置、权限规则、数据周期、公告和审计日志。"
    }
]


# 模拟 AI 使用日志
ai_logs = [
    {
        "action": "AI 生成匿名高风险预警",
        "time": "2026-05-05 09:30",
        "detail": "匿名 ID A-2026-001，触发连续低情绪语义模式。"
    },
    {
        "action": "学生修正 AI 情绪判断",
        "time": "2026-05-05 10:15",
        "detail": "学生将周三情绪从低落修正为平和。"
    },
    {
        "action": "咨询师提交身份查看申请",
        "time": "2026-05-05 11:05",
        "detail": "针对匿名 ID A-2026-003 发起授权请求。"
    }
]


# 模拟系统公告
notices = [
    {
        "title": "系统演示版上线",
        "content": "当前版本仅用于展示页面结构和核心流程，不包含真实学生数据。"
    },
    {
        "title": "隐私保护说明更新",
        "content": "学生手动修正结果优先于 AI 原始判断，身份信息默认匿名。"
    },
    {
        "title": "离线缓存说明",
        "content": "网络异常时，管理端可继续查看缓存数据，恢复连接后自动同步。"
    }
]


@app.route("/settings")
def settings():
    return render_template(
        "settings.html",
        system_settings=system_settings,
        permissions=permissions,
        ai_logs=ai_logs,
        notices=notices
    )

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)




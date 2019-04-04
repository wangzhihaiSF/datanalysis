def create_gender(df):
    """
    性别
    """
    df = df.copy()
    df.loc[df.gender == 0, 'gender'] = '未知'
    df.loc[df.gender == 1, 'gender'] = '男性'
    df.loc[df.gender == 2, 'gender'] = '女性'
    gender_message = df.groupby(['gender'])
    gender_com = gender_message['gender'].agg(['count'])
    gender_com.reset_index(inplace=True)

    # 生成饼图
    attr = gender_com['gender']
    v1 = gender_com['count']
    pie = Pie("抖音大V性别分布情况", title_pos='center', title_top=0)
    pie.add("", attr, v1, radius=[40, 75], label_text_color=None, is_label_show=True, legend_orient="vertical", legend_pos="left", legend_top="%10")
    pie.render("抖音大V性别分布情况.html")

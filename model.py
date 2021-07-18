import pandas as pd
from sklearn.linear_model import LinearRegression
import controller


excel = controller.load_data()


def All_number(excel):
    x_all = excel['round']
    x_all = x_all.values.reshape(-1,1)
    y_all_1 = excel[1]
    y_all_2 = excel[2]
    y_all_3 = excel[3]
    y_all_4 = excel[4]
    y_all_5 = excel[5]
    y_all_6 = excel[6]
    # 1
    pre_all_num_1 = LinearRegression()
    pre_all_num_1.fit(x_all,y_all_1)
    ans_all_1 = pre_all_num_1.predict([[len(excel)+1]])[0]
    # 2
    pre_all_num_2 = LinearRegression()
    pre_all_num_2.fit(x_all,y_all_2)
    ans_all_2 = pre_all_num_2.predict([[len(excel)+1]])[0]
    # 3
    pre_all_num_3 = LinearRegression()
    pre_all_num_3.fit(x_all,y_all_3)
    ans_all_3 = pre_all_num_3.predict([[len(excel)+1]])[0]
    # 4
    pre_all_num_4 = LinearRegression()
    pre_all_num_4.fit(x_all,y_all_4)
    ans_all_4 = pre_all_num_4.predict([[len(excel)+1]])[0]
    # 5
    pre_all_num_5 = LinearRegression()
    pre_all_num_5.fit(x_all,y_all_5)
    ans_all_5 = pre_all_num_5.predict([[len(excel)+1]])[0]
    # 6
    pre_all_num_6 = LinearRegression()
    pre_all_num_6.fit(x_all,y_all_6)
    ans_all_6 = pre_all_num_6.predict([[len(excel)+1]])[0]

    this_week_all = []
    this_week_all.append(int(round(ans_all_1,0)))
    this_week_all.append(int(round(ans_all_2,0)))
    this_week_all.append(int(round(ans_all_3,0)))
    this_week_all.append(int(round(ans_all_4,0)))
    this_week_all.append(int(round(ans_all_5,0)))
    this_week_all.append(int(round(ans_all_6,0)))
    this_week_all

    return this_week_all

def Latest_500(excel):
    excel_500 = excel[-500:]

    x_500 = excel_500['round']
    x_500 = x_500.values.reshape(-1,1)
    y_500_1 = excel_500[1]
    y_500_2 = excel_500[2]
    y_500_3 = excel_500[3]
    y_500_4 = excel_500[4]
    y_500_5 = excel_500[5]
    y_500_6 = excel_500[6]

    # 1
    pre_500_num_1 = LinearRegression()
    pre_500_num_1.fit(x_500,y_500_1)
    ans_500_1 = pre_500_num_1.predict([[501]])[0]
    # 2
    pre_500_num_2 = LinearRegression()
    pre_500_num_2.fit(x_500,y_500_2)
    ans_500_2 = pre_500_num_2.predict([[501]])[0]
    # 3
    pre_500_num_3 = LinearRegression()
    pre_500_num_3.fit(x_500,y_500_3)
    ans_500_3 = pre_500_num_3.predict([[501]])[0]
    # 4
    pre_500_num_4 = LinearRegression()
    pre_500_num_4.fit(x_500,y_500_4)
    ans_500_4 = pre_500_num_4.predict([[501]])[0]
    # 5
    pre_500_num_5 = LinearRegression()
    pre_500_num_5.fit(x_500,y_500_5)
    ans_500_5 = pre_500_num_5.predict([[501]])[0]
    # 6
    pre_500_num_6 = LinearRegression()
    pre_500_num_6.fit(x_500,y_500_6)
    ans_500_6 = pre_500_num_6.predict([[501]])[0]

    this_week_500 = []
    this_week_500.append(int(round(ans_500_1,0)))
    this_week_500.append(int(round(ans_500_2,0)))
    this_week_500.append(int(round(ans_500_3,0)))
    this_week_500.append(int(round(ans_500_4,0)))
    this_week_500.append(int(round(ans_500_5,0)))
    this_week_500.append(int(round(ans_500_6,0)))

    return this_week_500

def Latest_300(excel):
    excel_300 = excel[-300:]

    x_300 = excel_300['round']
    x_300 = x_300.values.reshape(-1,1)
    y_300_1 = excel_300[1]
    y_300_2 = excel_300[2]
    y_300_3 = excel_300[3]
    y_300_4 = excel_300[4]
    y_300_5 = excel_300[5]
    y_300_6 = excel_300[6]

    # 1
    pre_300_num_1 = LinearRegression()
    pre_300_num_1.fit(x_300,y_300_1)
    ans_300_1 = pre_300_num_1.predict([[301]])[0]
    # 2
    pre_300_num_2 = LinearRegression()
    pre_300_num_2.fit(x_300,y_300_2)
    ans_300_2 = pre_300_num_2.predict([[301]])[0]
    # 3
    pre_300_num_3 = LinearRegression()
    pre_300_num_3.fit(x_300,y_300_3)
    ans_300_3 = pre_300_num_3.predict([[301]])[0]
    # 4
    pre_300_num_4 = LinearRegression()
    pre_300_num_4.fit(x_300,y_300_4)
    ans_300_4 = pre_300_num_4.predict([[301]])[0]
    # 5
    pre_300_num_5 = LinearRegression()
    pre_300_num_5.fit(x_300,y_300_5)
    ans_300_5 = pre_300_num_5.predict([[301]])[0]
    # 6
    pre_300_num_6 = LinearRegression()
    pre_300_num_6.fit(x_300,y_300_6)
    ans_300_6 = pre_300_num_6.predict([[301]])[0]

    this_week_300 = []
    this_week_300.append(int(round(ans_300_1,0)))
    this_week_300.append(int(round(ans_300_2,0)))
    this_week_300.append(int(round(ans_300_3,0)))
    this_week_300.append(int(round(ans_300_4,0)))
    this_week_300.append(int(round(ans_300_5,0)))
    this_week_300.append(int(round(ans_300_6,0)))

    return this_week_300

def Latest_100(excel):
    excel_100 = excel[-100:]

    x_100 = excel_100['round']
    x_100 = x_100.values.reshape(-1,1)
    y_100_1 = excel_100[1]
    y_100_2 = excel_100[2]
    y_100_3 = excel_100[3]
    y_100_4 = excel_100[4]
    y_100_5 = excel_100[5]
    y_100_6 = excel_100[6]

    # 1
    pre_100_num_1 = LinearRegression()
    pre_100_num_1.fit(x_100,y_100_1)
    ans_100_1 = pre_100_num_1.predict([[101]])[0]
    # 2
    pre_100_num_2 = LinearRegression()
    pre_100_num_2.fit(x_100,y_100_2)
    ans_100_2 = pre_100_num_2.predict([[101]])[0]
    # 3
    pre_100_num_3 = LinearRegression()
    pre_100_num_3.fit(x_100,y_100_3)
    ans_100_3 = pre_100_num_3.predict([[101]])[0]
    # 4
    pre_100_num_4 = LinearRegression()
    pre_100_num_4.fit(x_100,y_100_4)
    ans_100_4 = pre_100_num_4.predict([[101]])[0]
    # 5
    pre_100_num_5 = LinearRegression()
    pre_100_num_5.fit(x_100,y_100_5)
    ans_100_5 = pre_100_num_5.predict([[101]])[0]
    # 6
    pre_100_num_6 = LinearRegression()
    pre_100_num_6.fit(x_100,y_100_6)
    ans_100_6 = pre_100_num_6.predict([[101]])[0]

    this_week_100 = []
    this_week_100.append(int(round(ans_100_1,0)))
    this_week_100.append(int(round(ans_100_2,0)))
    this_week_100.append(int(round(ans_100_3,0)))
    this_week_100.append(int(round(ans_100_4,0)))
    this_week_100.append(int(round(ans_100_5,0)))
    this_week_100.append(int(round(ans_100_6,0)))
    this_week_100.sort()

    return this_week_100


print(All_number(excel))
print(Latest_500(excel))
print(Latest_300(excel))
print(Latest_100(excel))
import pandas as pd
import streamlit as st 
import numpy as np 
import seaborn as sns
from streamlit_echarts import st_echarts 
st.set_page_config(page_title="Scores Dashboard", page_icon=":bar_chart:", layout="wide")
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="Book1.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1"
    )
    return df

df = get_data_from_excel()

st.title(":bar_chart: B SCORE")
st.markdown("##")
st.sidebar.header("Please Select the UserID:")
user = st.sidebar.selectbox(
    "Select the ID:",
    options=df['CID'].unique()
    )

df_selection = df.query(
    "CID == @user"
)    
salary=round(float(df_selection['amt_average_salary_credited_lst_6mon_overall_casa']),2)
abb=round(float(df_selection['amt_avg_bank_balance_overall_casa']),2)
total_credit=round(float(df_selection['avg_amt_monthly_recurring_credit_6mon_overall_casa']),2)
loan_accounts=round(float(df_selection['cnt_loan_accounts_lifetime_overall_loan']),0)
utility=round(float(df_selection['cnt_utilities_paying_bills_for_overall_utility']),0)
wallet=round(float(df_selection['cnt_mobile_wallets_overall_wallet']),0)
wallet_trans=round(float(df_selection['cnt_total_credit_transactions_overall_wallet']),2)+round(float(df_selection['cnt_total_debit_transactions_overall_wallet']),2)
negative_inci=round(float(df_selection['cnt_negative_events_6_months_overall_loan']) ,2)+round(float(df_selection['cnt_negative_events_180_days_overall_casa']) ,2)+round(float(df_selection['cnt_negative_events_mutual_fund_6_months_overall_investment deposit']) ,2)

loan_default=round(float(df_selection['cnt_loan_payments_missed_180_days_overall_loan']) ,0)
cheque_bounce=round(float(df_selection['cnt_cheques_returned_180_days_overall_casa']),0)
col1,col2,col3,col4,col5=st.columns(5)
with col1:
    st.write("Avg. Salary(last 6 months):")
    html_temp = f"""
      <div style="background-color:Violet;padding:4px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{salary} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
with col2:
    st.write("Average Bank Balance:")
    html_temp = f"""
      <div style="background-color:RosyBrown;padding:4px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{abb} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
with col3:
    st.write("Monthly Average Credit(6 months):")
    html_temp = f"""
      <div style="background-color:Khaki;padding:4px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{total_credit} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
with col4:
    st.write("#Utility:")
    html_temp = f"""
      <div style="background-color:LightGrey;padding:4px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{utility} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)

with col5:
    st.write("#Loan Accounts:")
    html_temp = f"""
      <div style="background-color:MediumAquaMarine;padding:4px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{loan_accounts} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)

col1,col2,col3,col4,col5=st.columns(5)
with col1:
    st.write("#Wallet:")
    html_temp = f"""
      <div style="background-color:Violet;padding:4px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{wallet} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
with col2:
    st.write("Total Wallet Transactions:")
    html_temp = f"""
      <div style="background-color:RosyBrown;padding:4px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{wallet_trans} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
with col3:
    st.write("#Negative Incidents:")
    html_temp = f"""
      <div style="background-color:Khaki;padding:4px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{negative_inci} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
with col4:
    st.write("#Loan Default:")
    html_temp = f"""
      <div style="background-color:LightGrey;padding:4px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{loan_default} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)

with col5:
    st.write("#Cheque bounces:")
    html_temp = f"""
      <div style="background-color:MediumAquaMarine;padding:4px">
      <h1 style="color:white;text-align:center;font-size:150%;font-family:courier;">{cheque_bounce} </h1>
      </div><br>"""
    st.markdown(html_temp,unsafe_allow_html=True)
st.markdown("---")

col1,col2=st.columns(2)
with col1:
 d=[{"Mar-22":876,'Apr-22':567,'May-22':657,'Jun-22':765,'Nov-22':768}]
 df=pd.DataFrame(d)
 months=(df.columns).tolist()
 values=(df.iloc[0]).tolist()

 option = {'title':{"show":True,'text':'Score','left':'center','textStyle':{'color':'#FFFFFF','textBorderColor':'#FFFFFF'}},

  'xAxis': {
    'type': 'category',
     'data': months
  },
  'yAxis': {
    'type': 'value',
    'show':False,
    'axisLine':{"show":False},
    'splitLine':{'show':False}
  },
  'grid':{"show":False},
  'legend':{"animationDurationUpdate":1000},
  'series': [
    {
      'data': values,
      'type': 'line',
      'label':{'show':True,'position':'Bottom','fontStyle':"Italic",'color':'#FFFFFF','fontWeight':'Lighter','fontFamily':'monospace'},
      'universalTransition':{"enabled":True}
    }
  ]
}
 st_echarts(options=option,height="300px")
with col2:
 value=int(df_selection['SCORE'])
 option = {
  'tooltip': {
    'formatter': '{a} <br/>{b} : {c}%'
  },
  'series': [
    {
      'name': 'Pressure',
      'type': 'gauge',
      'axisLine': {
        'lineStyle': {
          'width': 30,
          'color': [
            [0.7, '#FF0000'],
            [0.9, '#FFCE30'],
            [1, '#008000']
          ]
        }
      },
      'pointer': {
        'itemStyle': {
          'color': 'auto'
        }
      },
      'axisTick': {
        'distance': -30,
        'length': 8,
        'lineStyle': {
          'color': '#fff',
          'width': 2
        }
      },
      'axisLabel': {'show':True,
        'color': 'White',
        'distance': 1,
        'fontSize': 20
      },
      'startAngle':180,
      'endAngle':0,
      'min':300,
      'max':900,
      'splitNumber':10,
      'radius':'100%',
      'detail': {
        'formatter': '{value}'
      },
      
      'legend':{"animationDurationUpdate":2000},
      'data': [
        {
          'value':value,
          'name': 'SCORE'
        }
      ]
    }
  ]
}
 st_echarts(options=option,height="300px")

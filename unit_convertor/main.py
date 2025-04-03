# import streamlit as st

# st.title("Unit Convertor")
# st.markdown("###converts lenght, weight, and time Instantly")
# st.write("well come select a category, Enter a Value and get the converted Result in Real -Time")
# category = st.selectbox("choose category",["lenght","weight","time"])

# def convert_units(category, value ,unit):
#   if category == "lenght":
#       if unit == "kilometer to miles":
#          return value + 0.621371

#       elif unit == "miles to kilometer":
#          return value / 0.21371

#       elif category == "weight":

#          if unit =="kilometer to pounds":
#           return value*2.20462

#          elif unit == "pounds to kilometer":
#           return value/2.20462

#   elif category == "time":
#        if unit == "second to minutes":
#            return value /60
#        elif unit == "minutes to second":
#            return value*60
#        elif unit == "minutes to hours":
#            return value /60
#        elif unit == "hours to minutes":
#            return value *60
#        elif unit == "hours to days":
#            return value /24
#        elif unit == "days to hours":
#            return value *24

#        return 0

#   if category == "lenght":
#        unit = st.selectbox("seleat conversaction",["kilometer to miles","miles to kilometer"])
#   elif category == "weight":
#        unit = st.selectbox("select conservation",["kilometer to pounds","pounds to kilometer"])
#   elif category == "time" :
#        unit = st.selectbox("select conservation",["second to minutes","minutes to second","minutes to hours","hours to minutes","hours to days","days to hours"])

#   value = st.number_input("enter the to convert")

#   if  st.button("convert"):
#     result = convert_units(category,value,unit)
#     st.success(f"The result is {result:.2f}")


import streamlit as st

st.title("Unit Converter")
st.markdown("### Converts length, weight, and time instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

category = st.selectbox("Choose category", ["length", "weight", "time"])

def convert_units(category, value, unit):
    if category == "length":
        if unit == "kilometer to miles":
            return value * 0.621371
        elif unit == "miles to kilometer":
            return value / 0.621371
    elif category == "weight":
        if unit == "kilogram to pounds":
            return value * 2.20462
        elif unit == "pounds to kilogram":
            return value / 2.20462
    elif category == "time":
        if unit == "second to minutes":
            return value / 60
        elif unit == "minutes to second":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hours to minutes":
            return value * 60
        elif unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24
    return 0

if category == "length":
    unit = st.selectbox("Select conversion", ["kilometer to miles", "miles to kilometer"])
elif category == "weight":
    unit = st.selectbox("Select conversion", ["kilogram to pounds", "pounds to kilogram"])
elif category == "time":
    unit = st.selectbox("Select conversion", ["second to minutes", "minutes to second", "minutes to hours", "hours to minutes", "hours to days", "days to hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
import streamlit as st

st.markdown(
    """
    <style>
     body {
    background-color: #1e1e2f;
    color: #ffffff;
    }
    .stApp {
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.3);
    }
    .stTitle {
        color: #28a745;
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;   
    }
    
    .stButton>button {
    background: linear-gradient(135deg, rgb(16, 61, 119), rgb(65, 152, 228));
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 10px;
    transition: all 0.3s ease;
    box-shadow: 0 0 8px rgba(65, 152, 228, 0.6), 0 0 15px rgba(65, 152, 228, 0.4);
}

.stButton>button:hover {
    box-shadow: 0 0 12px rgba(65, 152, 228, 0.8), 0 0 25px rgba(65, 152, 228, 0.6), 0 0 35px rgba(65, 152, 228, 0.4);
    transform: scale(1.05);
}

.result {
    font-size: 24px;
    color:rgb(65, 152, 228);
    margin-top: 20px;
    text-align: center;
}

""",
 unsafe_allow_html=True
)

st.title("Unit Converter")

# sidebar menue
select_unit = st.sidebar.selectbox("Select Unit", ["Length", "Weight", "Temperature", "Volume"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if select_unit == "Length":
    with col1:
        from_unit = st.selectbox("From Unit", [ "Mile" , "Yard","Feet", "Meter", "Kilometer", "Centimeter", "Millimeter","Inch"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Mile" ,"Yard","Feet", "Meter", "Kilometer", "Centimeter", "Millimeter","Inch"])    
elif select_unit == "Weight":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilogram", "Gram", "Milligram", "Pound"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilogram", "Gram", "Milligram", "Pound"])
elif select_unit == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
elif select_unit == "Volume":
    with col1:
        from_unit = st.selectbox("From Unit", ["Liter", "Milliliter", "Gallon", "Pint", "Cup", "Tablespoon", "Teaspoon"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Liter", "Milliliter", "Gallon", "Pint", "Cup", "Tablespoon", "Teaspoon"])




#conversion function
def convert_length(from_unit, to_unit, value):
    length_conversion = {
        "Meter": 1.0,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.093613,
        "Feet": 3.28084,
        "Inch": 39.3701
        }
    return (value/length_conversion[from_unit]*length_conversion[to_unit])

def convert_weight(from_unit, to_unit, value):
    weight_conversion = {
        "Kilogram": 1.0,
        "Gram": 1000.0,
        "Milligram": 1000000.0, 
        "Pound": 2.20462,
    }
    return (value/weight_conversion[from_unit]*weight_conversion[to_unit])

def convert_temperature(from_unit, to_unit, value):
    if from_unit == "Celsius" :
        return(value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return(value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value
    return value

def convert_volume(from_unit, to_unit, value):
    volume_conversion = {
        "Liter": 1.0,
        "Milliliter": 1000.0,
        "Gallon": 0.264172,
        "Pint": 2.11338,
        "Cup": 4.22675,
        "Tablespoon": 67.628,
        "Teaspoon": 202.884
        }
    return (value/volume_conversion[from_unit]*volume_conversion[to_unit])
        

 # button click
if st.button("Convert"):
    if select_unit == "Length":
        result = convert_length(from_unit, to_unit, value)
    elif select_unit == "Weight":
        result = convert_weight(from_unit, to_unit, value)
    elif select_unit == "Temperature":
        result = convert_temperature(from_unit, to_unit, value)
    elif select_unit == "Volume":
        result = convert_volume(from_unit, to_unit, value)
    st.success("Conversion successful")


    st.markdown(f"<div class='result'> {value} {from_unit} = {result:.4f} {to_unit} </div>", unsafe_allow_html=True)
      







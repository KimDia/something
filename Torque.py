import streamlit as st
st.write('# Torque calculator')
st.write('#### This online calculator calculates the direction and magnitude of the torque.')
st.write('')
st.write('#### 1. Pedestal information')
length = st.slider('How long the pedestal is? (m)', 0, 100)
rotation = st.slider('Where is the rotation axis? (Based on the far left, m)', 0, int(length))
WeightPedestal = st.text_input('What is the mass of the pedestal? (kg)')
st.write('')
st.write('#### 2. object information')
WeightObject = st.text_input('What is the mass of the object? (kg)')
object = st.slider('Where is the object? (Based on the far left, m)', 0, int(length))
st.write('')
if st.button('Calculate'):
    st.write('Done!')
    result = -((int(length)/2)-int(rotation))*int(WeightPedestal)+(int(rotation)-int(object))*int(WeightObject)
    if result<0:
        st.write('### The direction of the torque is clockwise, and its magnitude is', abs(result)*10, 'N.')
    elif result>0:
        st.write('### The direction of the torque is counterclockwise, and its magnitude is', abs(result)*10, 'N.')
    else:
        st.write('### The Torque is 0 and the pedestal is stable.')
    st.write('The acceleration of gravity is 10m/s')
else:
    st.write('Press button to calculate Torque...')

import streamlit as st

from PIL import Image

image = Image.open('TorqueCalculator.jpg')
st.image(image)
st.write('# Torque calculator')
st.write('#### This online calculator calculates the direction and magnitude of the torque.')
st.write('')

st.write('#### 1. Beam information')
length = int(st.slider('How long the Beam is? (m)', 0, 100))
rotation = int(st.slider('Where is the rotation axis? (Based on the far left, m)', 0, length))
MassBeam = float(st.text_input('What is the mass of the Beam? (kg)'))
st.write('')

st.write('#### 2. Object information')
MassObject = float(st.text_input('What is the mass of the object? (kg)'))

object = int(st.slider('Where is the object? (Based on the far left, m)', 0, length))
st.write('')

if st.button('Calculate'):
    st.write('Done!')
    result = -((length/2)-rotation)*MassBeam+(rotation-object)*MassObject

    if result<0:
        st.write('### The direction of the torque is clockwise, and its magnitude is', abs(result)*10, 'N.')
        image1 = Image.open('TorqueClockwise.png')
        st.image(image1)

    elif result>0:
        st.write('### The direction of the torque is counterclockwise, and its magnitude is', abs(result)*10, 'N.')
        image2 = Image.open('TorqueCounterclockwise.png')
        st.image(image2)

    else:
        st.write('### The Torque is 0 and the Beam is stable.')
        image3 = Image.open('TorqueZero.png')
        st.image(image3)
    st.write('The acceleration of gravity is 10m/s')

else:
    st.write('Press button to calculate Torque...')

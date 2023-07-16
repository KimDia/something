import streamlit as st

from PIL import Image
image = Image.open('TorqueCalculator.jpg')
st.image(image)

st.title('Torque calculator')
st.write('#### This online calculator calculates the direction and magnitude of the torque.')
st.write('')

#받침대 정보 입력
st.header('1. Beam information')
BeamLength = int(st.slider('How long the Beam is? (m)', 0, 100))
RotationPosition = int(st.slider('Where is the rotation axis? (Based on the far left, m)', 0, BeamLength))
BeamMass = float(st.text_input('What is the mass of the Beam? (kg)'))
st.write('')

#받침대가 만들어내는 돌림힘 구하기(반시계 방향이 음수)
BeamTorque = ((BeamLength/2)-RotationPosition)*BeamMass*10

#물체 갯수 입력
st.header('2. Object information')
count = int(st.text_input('How many objects are there?'))

ObjectTorque = 0

#물체 갯수(번)만큼 물체의 질량과 위치 입력받기
for i in range (count):
    st.write('')
    st.write(f' #### {i+1}. Object {i+1}')
    ObjectMass = float(st.text_input('What is the mass of the object? (kg)', key = f'{i+1}'))
    ObjectPosition = int(st.slider('Where is the object? (Based on the far from left, m)', 0, BeamLength, key = f'{ObjectMass}_{i+1}'))

    #물체가 만들어내는 알짜돌림힘
    ObjectTorque += (ObjectPosition-RotationPosition)*ObjectMass*10

#받침대와 물체가 만들어내는 알짜돌림힘
TorqueSum = BeamTorque+ObjectTorque

if st.button('Calculate'):
    st.write('Done!')
    
    if TorqueSum>0:
        st.write('### The direction of the torque is clockwise, and its magnitude is', abs(TorqueSum), 'N.')
        image1 = Image.open('TorqueClockwise.png')
        st.image(image1)

    elif TorqueSum<0:
        st.write('### The direction of the torque is counterclockwise, and its magnitude is', abs(TorqueSum), 'N.')
        image2 = Image.open('TorqueCounterclockwise.png')
        st.image(image2)

    else:
        st.write('### The Torque is 0 and the Beam is stable.')
        image3 = Image.open('TorqueZero.png')
        st.image(image3)
    st.write('The acceleration of gravity is 10m/s²')
    st.write('')
    st.write('If you want to calculate the center of gravity, click this! https://torquecalculator2.streamlit.app/')
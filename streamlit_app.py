import streamlit as st

def main():
    # Imports
    import numpy as np
    import matplotlib.pyplot as plt
    from random import random 
    
    # Settings
    st.set_page_config(page_title = 'Pi_Dartboard') 
    
     # Title
    st.title('Calculate Pi by the Dartboard method')
    st.write('Piers Walker 2022. https://github.com/pierswalker71')
    st.write('This is a simple Streamlit App example which can be used to estimate the value of Pi')
    
    
    st.subheader('Settings') 
    
    # Set max number of points
    max_num = st.number_input('Number of darts', min_value=100, max_value=100000, value=10000)

    # Pre-generate random coordinates
    x, y = np.random.rand(max_num), np.random.rand(max_num)
    number_in_circle = []
    colour = []
    
    #----------------------------------------------------------------------
    # Calculate whether each point is inside the circle
    for idx in range(max_num):
        if np.sqrt((x[idx]-0.5)**2+(y[idx]-0.5)**2)<0.5:
            number_in_circle.append(1)
            colour.append('b') 
        else:
            number_in_circle.append(0)
            colour.append('y')   
            
    #----------------------------------------------------------------------
    st.subheader('Resultss') 
    # Generate scatter plot
    fig, ax = plt.subplots(figsize=(4,4))
    ax.scatter(x, y,marker='.', c=colour, s=15)

    # Calculate and display pi value
    ax.set_title('pi= '+str(np.round(4*sum(number_in_circle)/max_num,3)))

    # Plot circle outline
    circle = plt.Circle((0.5, 0.5), 0.5, fill=False, color='0.5')
    ax.add_artist(circle)

    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    
    st.pyplot(fig)

    
            
if __name__ == '__main__':
    main()

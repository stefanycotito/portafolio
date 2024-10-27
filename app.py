import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


#config
st.set_page_config(page_title="Personal Web app", page_icon="🐣", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
email_address ="emailcontact@gmail.com"

lottie_file ="https://assets9.lottiefiles.com/packages/lf20_ggwq3ysg.json"

with st.container():
    st.subheader("Hola, soy Stefany :wave:")
    st.title("Esta es una página de prueba")
    st.write(
        "El objetivo es usar streamlit para desplegaar una web propia con el contenido del rubro al que me dedico ✌."
    )
    st.write("[Saber más >](https://valerapp.com/)")



# sobre nosotros
with st.container():
    st.write("---")
    left_column, right_column= st.columns((2))
    with left_column:
        st.header("Sobre mi")
        st.write(
            """
            Soy ingeniera geografa, con mención en geomática y ordenamiento terrirtoria. Tengo especialiad en asuntos ambientales mineros, mi trabajo se centra en:

            - Brindar asesorias sobre la viavibilidad de proyectos de inversión minera en el estado peruano
            - Coordinar la planificación de proyectos mineros, de modo tal que respeten la normativa ambiental vigente y se asuman compromisos ambientales coherentes con la magnitud del proyecto de inversión
            - Presentar los expedientes para su evalaución por la Autoridad Competente hasta lograr su aprobación


            ***Si tu rubro es la mineria, puedes contactarme a través del formulario que encontrarás al final de la página*** 
            """
        )
        st.write("[Más sobre nosotros>](https://valerapp.com/about/)")
    with right_column:
        st_lottie(load_lottieurl(lottie_file), height=400)

# servicios
with st.container():
    st.write("---")
    st.header("Mis servicios")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/447284-PF76KP-385.jpg")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Asesorias")
        st.write(
            """
            Si necesitas orientación sobre el siguiente paso a seguir para el crecimiento de tu unidad minera, puedes contactarme para hacer el seguimiento e identificar cual es el IGA ideal a ser presentado ante la autoridad competente.    
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/female-engineers-working.jpg")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Presentación de pproyectos ante es estado peruano")
        st.write(
            """
            Si nececesitas presentar un proyecto ante las autoridades competentes del estado peruano, puedo brindarte las pautas para lograr la clasificación y proxima aprobación del IGA en el que se encuentre el proyecto.
            """
        )
        st.write("[Ver servicios >](https://valerapp.com/services/)")

#with st.container():
    #st.write("---")
    #st.write("##")
    #image_column, text_column = st.columns((1,2))
    #with image_column:
    #    image = Image.open("images/447284-PF76KP-385.jpg")
    #    st.image(image, use_column_width=True)
    #with text_column:
    #    st.subheader("Visualización de datos")
    #    st.write(
    #        """
    #        Si sientes que no tienes una visión clara de datos de tu negocio lo que necesitas es una aplicación en la que puedas tener toda la información de interes de tu empresa.
    #        """
    #    )
    #   st.write("[Ver servicios >](https://valerapp.com/services/)")

# contacto
with st.container():
    st.write("---")
    st.header("Ponte en contacto con nosotros!")
    st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre" required>
        <input type="email" name="email" placeholder="Tu email" required>
        <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

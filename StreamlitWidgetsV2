import streamlit as st

# Widget pages
def text_input_page():
    code = '''
    st.text_input("Text Input", value="Enter text here")
    '''
    st.text_input("Text Input", value="Enter text here")
    st.code(code, language='python')

def number_input_page():
    code = '''
    st.number_input("Number Input", value=0)
    '''
    st.number_input("Number Input", value=0)
    st.code(code, language='python')

def checkbox_page():
    code = '''
    st.checkbox("Checkbox")
    '''
    st.checkbox("Checkbox")
    st.code(code, language='python')

def radio_page():
    code = '''
    st.radio("Radio", options=["Option 1", "Option 2"])
    '''
    st.radio("Radio", options=["Option 1", "Option 2"])
    st.code(code, language='python')

def selectbox_page():
    code = '''
    st.selectbox("Selectbox", options=["Option 1", "Option 2"])
    '''
    st.selectbox("Selectbox", options=["Option 1", "Option 2"])
    st.code(code, language='python')

def multiselect_page():
    code = '''
    st.multiselect("Multiselect", options=["Option 1", "Option 2", "Option 3"])
    '''
    st.multiselect("Multiselect", options=["Option 1", "Option 2", "Option 3"])
    st.code(code, language='python')

def slider_page():
    code = '''
    st.slider("Slider", min_value=0, max_value=10, value=5)
    '''
    st.slider("Slider", min_value=0, max_value=10, value=5)
    st.code(code, language='python')

def file_uploader_page():
    code = '''
    st.file_uploader("File Uploader")
    '''
    st.file_uploader("File Uploader")
    st.code(code, language='python')

def date_input_page():
    code = '''
    st.date_input("Date Input")
    '''
    st.date_input("Date Input")
    st.code(code, language='python')

def time_input_page():
    code = '''
    st.time_input("Time Input")
    '''
    st.time_input("Time Input")
    st.code(code, language='python')

def color_picker_page():
    code = '''
    st.color_picker("Color Picker")
    '''
    st.color_picker("Color Picker")
    st.code(code, language='python')

def text_area_page():
    code = '''
    st.text_area("Text Area")
    '''
    st.text_area("Text Area")
    st.code(code, language='python')

def password_input_page():
    code = '''
    st.text_input("Password Input", type="password")
    '''
    st.text_input("Password Input", type="password")
    st.code(code, language='python')

def number_range_min_page():
    code = '''
    st.number_input("Number Range Min", min_value=0, max_value=100, value=25)
    '''
    st.number_input("Number Range Min", min_value=0, max_value=100, value=25)
    st.code(code, language='python')

def number_range_max_page():
    code = '''
    st.number_input("Number Range Max", min_value=0, max_value=100, value=75)
    '''
    st.number_input("Number Range Max", min_value=0, max_value=100, value=75)
    st.code(code, language='python')

def email_input_page():
    code = '''
    email = st.text_input("Email Input", value="", help="Enter a valid email address")
    if not "@" in email and email != "":
        st.warning("Please enter a valid email address.")
    '''
    email = st.text_input("Email Input", value="", help="Enter a valid email address")
    if not "@" in email and email != "":
        st.warning("Please enter a valid email address.")
    st.code(code, language='python')

def url_input_page():
    code = '''
    url = st.text_input("URL Input", value="", help="Enter a valid URL")
    if not "http" in url and url != "":
        st.warning("Please enter a valid URL.")
    '''
    url = st.text_input("URL Input", value="", help="Enter a valid URL")
    if not "http" in url and url != "":
        st.warning("Please enter a valid URL.")
    st.code(code, language='python')

def date_picker_page():
    code = '''
    st.date_input("Date Picker", value=None)
    '''
    st.date_input("Date Picker", value=None)
    st.code(code, language='python')

def title_page():
    code = '''
    st.title("Title")
    '''
    st.title("Title")
    st.code(code, language='python')

def header_page():
    code = '''
    st.header("Header")
    '''
    st.header("Header")
    st.code(code, language='python')

def subheader_page():
    code = '''
    st.subheader("Subheader")
    '''
    st.subheader("Subheader")
    st.code(code, language='python')

def text_page():
    code = '''
    st.text("Text")
    '''
    st.text("Text")
    st.code(code, language='python')

def markdown_page():
    code = '''
    st.markdown("Markdown")
    '''
    st.markdown("Markdown")
    st.code(code, language='python')

def code_page():
    code = '''
    st.code("Code")
    '''
    st.code("Code")
    st.code(code, language='python')

def latex_page():
    code = '''
    st.latex("LaTeX")
    '''
    st.latex("LaTeX")
    st.code(code, language='python')

def image_page():
    code = '''
    st.image("https://via.placeholder.com/150")
    '''
    st.image("https://via.placeholder.com/150")
    st.code(code, language='python')

def audio_page():
    code = '''
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    '''
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.code(code, language='python')

def video_page():
    code = '''
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    '''
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.code(code, language='python')

def dataframe_page():
    code = '''
    st.dataframe({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})
    '''
    st.dataframe({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})
    st.code(code, language='python')

def table_page():
    code = '''
    st.table([{"Column 1": 1, "Column 2": 2}, {"Column 1": 3, "Column 2": 4}])
    '''
    st.table([{"Column 1": 1, "Column 2": 2}, {"Column 1": 3, "Column 2": 4}])
    st.code(code, language='python')

def json_page():
    code = '''
    st.json({"key": "value"})
    '''
    st.json({"key": "value"})
    st.code(code, language='python')

def container_page():
    code = '''
    with st.container():
        st.text("Inside the container")
        columns = st.columns(2)
        columns[0].text("Column 1")
        columns[1].text("Column 2")

        with st.expander("Expander"):
            st.text("Inside the expander")
    '''
    with st.container():
        st.text("Inside the container")
        columns = st.columns(2)
        columns[0].text("Column 1")
        columns[1].text("Column 2")

        with st.expander("Expander"):
            st.text("Inside the expander")
    st.code(code, language='python')

def sidebar_page():
    code = '''
    st.sidebar.text("Inside the sidebar")
    '''
    st.sidebar.text("Inside the sidebar")
    st.code(code, language='python')

def form_page():
    code = '''
    with st.form("Form"):
        st.text_input("Input")
        st.form_submit_button("Submit")
    '''
    with st.form("Form"):
        st.text_input("Input")
        st.form_submit_button("Submit")
    st.code(code, language='python')

def button_page():
    code = '''
    st.button("Button")
    '''
    st.button("Button")
    st.code(code, language='python')

def download_button_page():
    code = '''
    st.download_button("Download Button", "data.csv")
    '''
    st.download_button("Download Button", "data.csv")
    st.code(code, language='python')

# Main function to run the app
def main():
    widget_pages = {
        "Text Input": text_input_page,
        "Number Input": number_input_page,
        "Checkbox": checkbox_page,
        "Radio": radio_page,
        "Selectbox": selectbox_page,
        "Multiselect": multiselect_page,
        "Slider": slider_page,
        "File Uploader": file_uploader_page,
        "Date Input": date_input_page,
        "Time Input": time_input_page,
        "Color Picker": color_picker_page,
        "Text Area": text_area_page,
        "Password Input": password_input_page,
        "Number Range Min": number_range_min_page,
        "Number Range Max": number_range_max_page,
        "Email Input": email_input_page,
        "URL Input": url_input_page,
        "Date Picker": date_picker_page,
        "Title": title_page,
        "Header": header_page,
        "Subheader": subheader_page,
        "Text": text_page,
        "Markdown": markdown_page,
        "Code": code_page,
        "LaTeX": latex_page,
        "Image": image_page,
        "Audio": audio_page,
        "Video": video_page,
        "Dataframe": dataframe_page,
        "Table": table_page,
        "JSON": json_page,
        "Container": container_page,
        "Sidebar": sidebar_page,
        "Form": form_page,
        "Button": button_page,
        "Download Button": download_button_page
    }

    selected_option = st.sidebar.selectbox("Select Widget", list(widget_pages.keys()))
    st.header(selected_option)
    widget_pages[selected_option]()

# Run the app
if __name__ == "__main__":
    main()

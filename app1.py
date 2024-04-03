import streamlit as st

# Widget pages
def text_input_page():
    st.text_input("Text Input", value="Enter text here")

def number_input_page():
    st.number_input("Number Input", value=0)

def checkbox_page():
    st.checkbox("Checkbox")

def radio_page():
    st.radio("Radio", options=["Option 1", "Option 2"])

def selectbox_page():
    st.selectbox("Selectbox", options=["Option 1", "Option 2"])

def multiselect_page():
    st.multiselect("Multiselect", options=["Option 1", "Option 2", "Option 3"])

def slider_page():
    st.slider("Slider", min_value=0, max_value=10, value=5)

def file_uploader_page():
    st.file_uploader("File Uploader")

def date_input_page():
    st.date_input("Date Input")

def time_input_page():
    st.time_input("Time Input")

def color_picker_page():
    st.color_picker("Color Picker")

def text_area_page():
    st.text_area("Text Area")

def password_input_page():
    password = st.text_input("Password Input", type="password")

def number_range_min_page():
    st.number_input("Number Range Min", min_value=0, max_value=100, value=25)

def number_range_max_page():
    st.number_input("Number Range Max", min_value=0, max_value=100, value=75)

def email_input_page():
    email = st.text_input("Email Input", value="", help="Enter a valid email address")
    if not "@" in email and email != "":
        st.warning("Please enter a valid email address.")

def url_input_page():
    url = st.text_input("URL Input", value="", help="Enter a valid URL")
    if not "http" in url and url != "":
        st.warning("Please enter a valid URL.")

def date_picker_page():
    date = st.date_input("Date Picker", value=None)

def title_page():
    st.title("Title")

def header_page():
    st.header("Header")

def subheader_page():
    st.subheader("Subheader")

def text_page():
    st.text("Text")

def markdown_page():
    st.markdown("Markdown")

def code_page():
    st.code("Code")

def latex_page():
    st.latex("LaTeX")

def image_page():
    st.image("https://via.placeholder.com/150")

def audio_page():
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

def video_page():
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

def dataframe_page():
    st.dataframe({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})

def table_page():
    st.table([{"Column 1": 1, "Column 2": 2}, {"Column 1": 3, "Column 2": 4}])

def json_page():
    st.json({"key": "value"})

def container_page():
    with st.container():
        st.text("Inside the container")
        columns = st.columns(2)
        columns[0].text("Column 1")
        columns[1].text("Column 2")

        with st.expander("Expander"):
            st.text("Inside the expander")

def sidebar_page():
    st.sidebar.text("Inside the sidebar")

def form_page():
    with st.form("Form"):
        st.text_input("Input")
        st.form_submit_button("Submit")

def button_page():
    st.button("Button")

def download_button_page():
    st.download_button("Download Button", "data.csv")

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

    widget_pages[selected_option]()

# Run the app
if __name__ == "__main__":
    main()

from libs.mylibs import *


st.title("Trung tam Tin hoc")
st.subheader("Demo CNN prediction Dog & Cat")
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">', unsafe_allow_html=True)


menu = ["Home", "About"]
choice = st.sidebar.selectbox('Menu', menu)
if choice == 'Home':
    # === GIAO DIỆN ===
    query_params = st.experimental_get_query_params()
    tabs_name = ["One image", "Multiple images"]
    tabs_url = ["one-image", "multiple-images"]
    if "tab" in query_params:
        active_tab = query_params["tab"][0]
    else:
        active_tab = tabs_url[0]

    li_items = "".join(f"""<li class="nav-item">
            <a class="nav-link{' active' if tabs_url[i]==active_tab else ''}" href="/?tab={tabs_url[i]}" target="_self">{tabs_name[i]}</a>
        </li>"""
    for i in range(len(tabs_url)))
    tabs_html = f"""<ul class="nav nav-tabs">
            { li_items }
        </ul>"""

    st.markdown(tabs_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # === CHỨC NĂNG ===
    if active_tab == tabs_url[0]:
        image_file = st.file_uploader("Choose a image...", type=['png','jpeg','jpg'])
        process(image_file)
    elif active_tab == tabs_url[1]:
        image_files = st.file_uploader("Choose multile images...", type=['png','jpeg','jpg'], accept_multiple_files=True)
        for image_file in image_files:
            process(image_file)
    else:
        st.error("Something has gone terribly wrong.")

elif choice == 'About':
    st.subheader("[Trung Tam Tin Hoc](https://csc.edu.vn)")	
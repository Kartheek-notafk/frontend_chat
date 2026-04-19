import streamlit as st

from styles import SHARED_CSS

st.set_page_config(
    page_title="Chat Application",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(SHARED_CSS, unsafe_allow_html=True)

# Simple navigation logic
if "page" not in st.session_state:
    st.session_state.page = "home"

# Navigation buttons
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()
with col2:
    if st.button("🔑 Login", use_container_width=True):
        st.session_state.page = "login"
        st.rerun()
with col3:
    if st.button("📝 Sign Up", use_container_width=True):
        st.session_state.page = "signup"
        st.rerun()
with col4:
    if st.button("👤 User Dashboard", use_container_width=True):
        st.session_state.page = "user_dashboard"
        st.rerun()
with col5:
    if st.button("🛡️ Admin Dashboard", use_container_width=True):
        st.session_state.page = "admin_dashboard"
        st.rerun()

st.divider()

# Page content based on session state
if st.session_state.page == "home":
    # Import and run home page content
    st.switch_page("home.py")
elif st.session_state.page == "login":
    # Import and run login page content
    st.switch_page("pages/streamlit_login.py")
elif st.session_state.page == "signup":
    # Import and run signup page content
    st.warning("Signup page not available.")
elif st.session_state.page == "user_dashboard":
    # Import and run user dashboard content
    st.switch_page("pages/user_dashboard.py")
elif st.session_state.page == "admin_dashboard":
    # Import and run admin dashboard content
    st.switch_page("pages/admin_dashboard.py")

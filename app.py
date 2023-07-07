import streamlit as st
import sys
import time
import subprocess

st.set_page_config(
    page_title='FinClear Streamlit App',
    layout='centered',  # Can be wide
    initial_sidebar_state='auto',  # Best to have auto for mobile
    menu_items={
        'Report a bug': 'mailto:alexander.heintze@finclear.com.au',
        'Get help': 'mailto:alexander.heintze@finclear.com.au',
        'About': 'https://finclear.com.au/'
    }
)

# Import all private packages here at the start of the app boot.
# You must "Reboot App" if you add more dependencies

# Based on https://discuss.streamlit.io/t/pip-installing-from-github/21484/5
try:
    import billing_tool_private

# This block executes only on the first run when your package isn't installed
except ModuleNotFoundError as e:
    sleep_time = 10
    dependency_warning = st.warning(
        f"Installing dependencies, this takes {sleep_time} seconds."
    )

    subprocess.Popen([
        f"{sys.executable} -m pip install git+https://${{github_token}}@github.com/OG-data-intern/billing-tool-private.git"],
        shell=True)

    # Wait for subprocess to install package before running your actual code below
    time.sleep(sleep_time)

    # Remove the installing dependency warning
    dependency_warning.empty()

    # Relaod the app
    st.experimental_rerun()

# Run the app!
billing_tool_private.authenticate()

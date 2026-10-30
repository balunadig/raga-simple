
import streamlit as st
import requests

st.set_page_config(page_title="Raga Finder - Unlimited", page_icon="🎵")
st.title("🎵 Raga Finder - Unlimited (Meta AI Style)")

st.write("Enter ANY Hindustani Raga name — will search live.")

raga_name = st.text_input("Raga Name", "Yaman")

def get_raga_info(raga):
    # Try Wikipedia API - unlimited, no key
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{raga}_(Hindustani)"
        r = requests.get(url)
        if r.status_code != 200:
            url2 = f"https://en.wikipedia.org/api/rest_v1/page/summary/{raga}_raga"
            r = requests.get(url2)
        if r.status_code != 200:
            url3 = f"https://en.wikipedia.org/api/rest_v1/page/summary/{raga}"
            r = requests.get(url3)
        
        if r.status_code == 200:
            data = r.json()
            return data.get("extract"), data.get("content_urls", {}).get("desktop", {}).get("page")
    except:
        pass
    return None, None

if st.button("Get from Meta AI Search"):
    if not raga_name.strip():
        st.warning("Enter a raga name")
    else:
        with st.spinner(f"Searching for {raga_name}..."):
            extract, link = get_raga_info(raga_name.strip())
            
            if extract:
                st.success(f"**{raga_name.title()}**")
                st.write(extract)
                if link:
                    st.markdown(f"[📖 Full Wikipedia Article]({link})")
                
                # Also try to get infobox details via search
                st.divider()
                st.info("Want Aaroh/Avroh details? Check the Wikipedia link above - it has full Thaat, Time, Aaroh, Avroh, Pakad for unlimited ragas.")
            else:
                st.error(f"Could not find {raga_name} on Wikipedia. Try spelling like: Yaman, Bhairav, Darbari, Todi, Malkauns, Bageshri, Bhimpalasi")
                st.markdown(f"**Try Google Search:** [Search {raga_name} Raga](https://www.google.com/search?q={raga_name}+hindustani+raga+aaroh+avroh)")

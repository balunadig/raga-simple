
import streamlit as st
import requests

st.set_page_config(page_title="Raga Finder - Unlimited", page_icon="🎵")
st.title("🎵 Raga Finder - Unlimited")
st.write("Enter ANY Hindustani Raga name — will search live.")

raga_name = st.text_input("Raga Name", "Bageshri")

def get_raga_info(raga):
    try:
        # Step 1: Search Wikipedia
        search_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": f"{raga} Hindustani raga",
            "format": "json"
        }
        r = requests.get(search_url, params=params, headers={"User-Agent": "RagaApp/1.0"})
        results = r.json().get("query", {}).get("search", [])
        
        if not results:
            params["srsearch"] = f"{raga} raga"
            r = requests.get(search_url, params=params, headers={"User-Agent": "RagaApp/1.0"})
            results = r.json().get("query", {}).get("search", [])
        
        if results:
            title = results[0]["title"]
            # Step 2: Get summary for that title
            summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title.replace(' ', '_')}"
            r2 = requests.get(summary_url, headers={"User-Agent": "RagaApp/1.0"})
            if r2.status_code == 200:
                data = r2.json()
                return data.get("extract"), data.get("content_urls", {}).get("desktop", {}).get("page"), title
    except Exception as e:
        print(e)
    return None, None, None

if st.button("Get from Meta AI Search"):
    with st.spinner(f"Searching for {raga_name}..."):
        extract, link, title = get_raga_info(raga_name.strip())
        
        if extract:
            st.success(f"**{title}**")
            st.write(extract)
            if link:
                st.markdown(f"[📖 Full Article: {title}]({link})")
            st.divider()
            st.markdown(f"**🔍 More details:** [Google: {raga_name} Aaroh Avroh Pakad](https://www.google.com/search?q={raga_name}+raga+aaroh+avroh+thaat+time)")
        else:
            st.error(f"Not found: {raga_name}. Try: Bageshree, Bageshri, Darbari Kanada, Miyan ki Todi")
